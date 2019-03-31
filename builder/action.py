# -*- coding: utf-8 -*-
"""Define an action class.
"""
from .enums import ActType, AuxVerb, GroupType, LangType
from .basesubject import _BaseSubject
from .behavior import Behavior


class _BaseAction(object):
    """Base action class.

    Attributes:
        name (str): a name of the action.
        note (str): a short description.
    """
    def __init__(self, name: str, note):
        """
        Args:
            name (str): an action name.
            note (str): a short description.
        """
        self.name = name
        self.note = note


class Action(_BaseAction):
    """A general action class.

    Attributes:
        act_type (:enum:`ActType`): an action category type.
        aux_verb (:enum:`AuxVerb`): an auxiliary verb.
        behavior (:enum:`Behavior`): a behavior type of this action.
        descriptions (:tuple:str): descriptions of this action.
        flag (str): a story flag to associate this action.
        deflag (str): a story deflag to associate this action.
        info (str): a information of the action.
        is_negative (bool): if True is a negative mode.
        is_passive (bool): if True is a passive mode.
        note (str): a short description.
        objects (:tuple:obj:`_BaseSubject`): objects of this action.
        priority (:int): a action priotiry.
        subject (:obj:`_BaseSubject`): a subject of this action.
    """
    CLS_NAME = "_action"
    DEFAULT_PRIORITY = 5
    MAX_PRIORITY = 10
    MIN_PRIORITY = 0

    def __init__(self, subject: _BaseSubject, act_type: ActType, behavior: Behavior,
            objects: tuple, info: str, note: str):
        """
        Args:
            subject (:obj:`_BaseSubject`): action subject.
            behavior (:enum:`Behavior`): action behavior type.
            objects (:tuple:obj:`_BaseSubject`): an action objects.
            info (str, optional): an action name.
            note (str, optional): a short description.
        """
        super().__init__(Action.CLS_NAME, note)
        self.act_type = act_type
        self.aux_verb = AuxVerb.NONE
        self.behavior = behavior
        self.deflag = ""
        self.descriptions = ()
        self.flag = ""
        self.info = info
        self.is_negative = False
        self.is_passive = False
        self.objects = _assertion_objects(objects)
        self.priority = Action.DEFAULT_PRIORITY
        self.subject = _assertion_subject(subject)

    def can(self):
        self.aux_verb = AuxVerb.CAN
        return self

    def desc(self, *args):
        self.descriptions = args
        return self

    def may(self):
        self.aux_verb = AuxVerb.MAY
        return self

    def must(self):
        self.aux_verb = AuxVerb.MUST
        return self

    def negative(self):
        self.is_negative = True
        return self

    def non(self): return self.negative()

    def passive(self):
        self.is_passive = True
        return self

    def ps(self): return self.passive()

    def should(self):
        self.aux_verb = AuxVerb.SHOULD
        return self

    def set_flag(self, f):
        self.flag = f
        return self

    def set_deflag(self, f):
        self.deflag = f
        return self

    def set_priority(self, pri):
        self.priority = _assertion_priority(pri, Action.MAX_PRIORITY, Action.MIN_PRIORITY)
        return self

    def think(self):
        self.aux_verb = AuxVerb.THINK
        return self

    def want(self):
        self.aux_verb = AuxVerb.WANT
        return self

    def will(self):
        self.aux_verb = AuxVerb.WILL
        return self


class ActionGroup(_BaseAction):
    """Acrion grouping class.

    Attributes:
        actions (:tuple:obj:`Action`): action lists.
        group_type (:enum:`GroupType`): a group type.
        lang (:enum:`LangType`): a language type.
        note (str): a short description.
    """
    CLS_NAME = "_actiongroup"
    def __init__(self, *args: Action, group_type: GroupType, lang: LangType=LangType.JPN, note: str=""):
        """
        Args:
            *args (:tuple:obj:`Action`): actions
            group_type (:enum:`GroupType`): a group type.
            lang (:enum:`LangType`, optional): a language type.
            note (str, optional): a short description.
        """
        super().__init__(ActionGroup.CLS_NAME, note)
        self.actions = args
        self.group_type = group_type
        self.lang = lang


# functions
def _assertion_objects(targets: tuple):
    if not targets or set(targets) == {None}:
        return ()
    for t in set(targets) - {None}:
        assert isinstance(t, _BaseSubject), "The object type {} is a mismatch!".format(type(t))
    return targets


def _assertion_priority(pri: int, max_: int, min_: int) -> int:
    assert pri <= max_ and pri >= min_, "The priority {} is over number!".format(pri)
    return pri


def _assertion_subject(target: _BaseSubject) -> _BaseSubject:
    if not target:
        return None
    assert isinstance(target, _BaseSubject), "The subject type {} is a mismatch!".format(type(target))
    return target

