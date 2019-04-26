# -*- coding: utf-8 -*-
"""Define an action class.
"""
from . import assertion as ast
from . import description as ds
from . import enums as em
from . import baseaction as ba
from . import basesubject as bs


class Action(ba.BaseAction):
    """A general action class.

    Attributes:
        act_type (:enum:`ActType`): an action category type.
        auxverb (:enum:`AuxVerb`): an auxiliary verb.
        description (:obj:`BaseDesc`): an associated description.
        objects (:tuple:obj:`BaseSubject`): an action objects.
        priority (int): an action priotiry.
        subject (:obj:`BaseSubject`): an action subject.
        verb (str): an action verb.
    """
    PRIORITY_DEFAULT = 5
    PRIORITY_MAX = 10
    PRIORITY_MIN = 0

    def __init__(self, act_type: em.ActType, subject: bs.BaseSubject, verb: str, auxverb: em.AuxVerb,
            objects: tuple):
        """
        Args:
            act_type (:enum:`ActType`): an action type.
            subject (:obj:`BaseSubject`): a subject.
            verb (str): an action verbs.
            auxverb (:enum:`AuxVerb`): an auxiliary verb.
            objects (:tuple:obj:`_BaseSubject`): objects.
        """
        super().__init__(act_type)
        self.auxverb = ast.is_instance(auxverb, em.AuxVerb)
        self.priority = Action.PRIORITY_DEFAULT
        self.description = ds.NoDesc()
        self.objects = objects # check and build data
        self.subject = ast.is_instance(subject, bs.BaseSubject)
        self.verb = ast.is_str(verb)

    def d(self, *args):
        return self.desc(*args)

    def desc(self, *args):
        self.description = ds.Desc(*args)
        return self

    def omit(self):
        """Set minimum priority.
        """
        self.priority = Action.PRIORITY_MIN
        return self

    def pri(self, pri):
        self.priority = ast.is_between(pri, Action.PRIORITY_MAX, Action.PRIORITY_MIN)
        return self

    def t(self, *args):
        return self.tell(*args)

    def tell(self, *args):
        self.description = ds.Desc(*args, desc_type=em.DescType.DIALOGUE)
        return self


class ActionGroup(ba.BaseAction):
    """Action grouping class.

    Attributes:
        act_type (:enum:`ActType`): a type of this group.
        actions (:tuple:obj:`Action`): actions.
        group_type (:enum:`GroupType`): a type of this group.
        lang (:enum:`LangType`): a language type.
    """
    def __init__(self, *args: Action, group_type: em.GroupType, lang: em.LangType=em.LangType.JPN):
        """
        Args:
            *args (:tuple:obj:`Action`): actions
            group_type (:enum:`GroupType`): a group type.
            lang (:enum:`LangType`, optional): a language type.
        """
        super().__init__(em.ActType.GROUP)
        self.actions = args # TODO: check and build data
        self.group_type = ast.is_instance(group_type, em.GroupType)
        self.lang = ast.is_instance(lang, em.LangType)

    def inherited(self, *args):
        return ActionGroup(*args,
                group_type=self.group_type,
                lang=self.lang)


class TagAction(ba.BaseAction):
    """Action class for tag specialized.

    Attributes:
        act_type (:enum:`ActType`): a type of this tag.
        tag (:enum:`TagType`): a tag type.
        info (str): a tag information.
    """
    def __init__(self, tag: em.TagType, info: str=""):
        super().__init__(em.ActType.TAG)
        self.tag = ast.is_instance(tag, em.TagType)
        self.info = ast.is_str(info)

