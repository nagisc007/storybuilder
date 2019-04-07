# -*- coding: utf-8 -*-
"""Define an action class.
"""
from .sbutils import assert_isclass, assert_isstr, assert_isbool, assert_isbetween
from .enums import ActType, AuxVerb, GroupType, LangType, TagType
from .basesubject import _BaseSubject, Nothing
from .behavior import Behavior


class _BaseAction(object):
    """Base action class.

    Attributes:
        name (str): a name of the action.
    """
    def __init__(self, name: str):
        """
        Args:
            name (str): an action name.
        """
        assert_isstr(name)

        self.name = name


class Description(object):
    """Description class.

    Attributes:
        descs (:tuple:str): description strings.
        is_dialogue (:bool): if True, treating as a dialogue.
    """
    def __init__(self, descs, is_dialogue: bool=False):
        """
        Args:
            descs (:tuple:str): descriptions
        """
        assert_isbool(is_dialogue)

        self.data = self._descs_from(descs)
        self.is_dialogue = is_dialogue

    def _descs_from(self, descs) -> tuple:
        if descs:
            if isinstance(descs, str):
                return (descs,)
            else:
                return descs
        return ()

    def dialogue(self):
        self.is_dialogue = True


class Action(_BaseAction):
    """A general action class.

    Attributes:
        act_type (:enum:`ActType`): an action category type.
        behavior (:enum:`Behavior`): a behavior type of this action.
        descs (:obj:`Description`): descriptions data object.
        objects (:tuple:obj:`_BaseSubject`): objects of this action.
        subject (:obj:`_BaseSubject`): a subject of this action.
        _auxverb (:enum:`AuxVerb`): an auxiliary verb.
        _deflag (str): a story deflag to associate this action.
        _flag (str): a story flag to associate this action.
        _is_negative (bool): if True is a negative mode.
        _is_passive (bool): if True is a passive mode.
        _priority (:int): a action priotiry.
    """
    CLS_NAME = "_action"
    DEFAULT_PRIORITY = 5
    MAX_PRIORITY = 10
    MIN_PRIORITY = 0

    def __init__(self, subject: _BaseSubject, act_type: ActType, behavior: Behavior, objects: tuple):
        """
        Args:
            subject (:obj:`_BaseSubject`): a subject.
            act_type (:enum:`ActType`): an action type.
            behavior (:enum:`Behavior`): a behavior type.
            objects (:tuple:obj:`_BaseSubject`): objects.
        """
        assert_isclass(subject, _BaseSubject)
        assert_isclass(act_type, ActType)
        assert_isclass(behavior, Behavior)

        super().__init__(Action.CLS_NAME)
        self._auxverb = AuxVerb.NONE
        self._deflag = ""
        self._flag = ""
        self._is_negative = False
        self._is_passive = False
        self._priority = Action.DEFAULT_PRIORITY
        self.act_type = act_type
        self.behavior = behavior
        self.descs = Description("")
        self.objects = objects
        self.subject = subject

    @property
    def auxverb(self) -> AuxVerb:
        return self._auxverb

    @property
    def deflag(self) -> str:
        return self._deflag

    @property
    def flag(self) -> str:
        return self._flag

    @property
    def is_negative(self) -> bool:
        return self._is_negative

    @property
    def is_passive(self) -> bool:
        return self._is_passive

    @property
    def priority(self) -> int:
        return self._priority

    def can(self):
        self._auxverb = AuxVerb.CAN
        return self

    def d(self, *args):
        return self.desc(*args)

    def desc(self, *args, is_dialogue: bool=False):
        self.descs = Description(args, is_dialogue=True) if is_dialogue else Description(args)
        return self

    def may(self):
        self._auxverb = AuxVerb.MAY
        return self

    def must(self):
        self._auxverb = AuxVerb.MUST
        return self

    def negative(self):
        self._is_negative = True
        return self

    def non(self): return self.negative()

    def omit(self):
        """Set minimum priority.
        """
        self._priority = Action.MIN_PRIORITY
        return self

    def passive(self):
        self._is_passive = True
        return self

    def ps(self): return self.passive()

    def set_flag(self, f):
        self._flag = f
        return self

    def set_deflag(self, f):
        self._deflag = f
        return self

    def set_priority(self, pri):
        assert_isbetween(pri, Action.MAX_PRIORITY, Action.MIN_PRIORITY)

        self._priority = pri
        return self

    def should(self):
        self._auxverb = AuxVerb.SHOULD
        return self

    def tell(self, *args):
        self.desc(*args, is_dialogue=True)
        return self

    def think(self):
        self._auxverb = AuxVerb.THINK
        return self

    def want(self):
        self._auxverb = AuxVerb.WANT
        return self

    def will(self):
        self._auxverb = AuxVerb.WILL
        return self


class ActionGroup(_BaseAction):
    """Acrion grouping class.

    Attributes:
        actions (:tuple:obj:`Action`): action lists.
        group_type (:enum:`GroupType`): a group type.
        lang (:enum:`LangType`): a language type.
    """
    CLS_NAME = "_actiongroup"

    def __init__(self, *args: Action, group_type: GroupType, lang: LangType=LangType.JPN):
        """
        Args:
            *args (:tuple:obj:`Action`): actions
            group_type (:enum:`GroupType`): a group type.
            lang (:enum:`LangType`, optional): a language type.
        """
        assert_isclass(group_type, GroupType)
        assert_isclass(lang, LangType)

        super().__init__(ActionGroup.CLS_NAME)
        self.actions = args
        self.group_type = group_type
        self.lang = lang


class TagAction(Action):
    """Action for tag.
    """
    def __init__(self, tag: TagType, note: str=""):
        super().__init__(Nothing(), ActType.TAG, Behavior.NONE, ())
        assert_isclass(tag, TagType)
        assert_isstr(note)
        
        self.note = note
        self.tag = tag

