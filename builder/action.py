# -*- coding: utf-8 -*-
"""Define an action class.
"""
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
        self.name = name


class Description(object):
    """Description class.
    """
    def __init__(self, descs):
        """
        Args:
            descs (:tuple:str): descriptions
        """
        self.data = self._descs_from(descs)

    def _descs_from(self, descs) -> tuple:
        if descs:
            if isinstance(descs, str):
                return (descs,)
            else:
                return descs
        return ()


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
        assert isinstance(subject, _BaseSubject), "subject Must be Subject(_BaseSubject) class!"
        assert isinstance(act_type, ActType), "act_type Must be ActType!"
        assert isinstance(behavior, Behavior), "behavior Mue be Behavior!"

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

    def desc(self, *args):
        self.descs = Description(args)
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
        assert pri <= Action.MAX_PRIORITY and pri >= Action.MIN_PRIORITY, "pri Must be between {} to {}".format(Action.MAX_PRIORITY, Action.MIN_PRIORITY)

        self._priority = pri
        return self

    def should(self):
        self._auxverb = AuxVerb.SHOULD
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
        assert isinstance(group_type, GroupType), "group_type Must be GroupType!"

        super().__init__(ActionGroup.CLS_NAME)
        self.actions = args
        self.group_type = group_type
        self.lang = lang


class TagAction(Action):
    """Action for tag.
    """
    def __init__(self, tag: TagType, note: str=""):
        super().__init__(Nothing(), ActType.TAG, Behavior.NONE, ())
        self.note = note
        self.tag = tag

