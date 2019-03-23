# -*- coding: utf-8 -*-
"""Module to build a story.
"""
from .acttypes import ActType, TagType, LangType
from .acttypes import tag_str_of
from .behavior import Behavior
from .behavior import behavior_str_of


class _BaseAction(object):
    """Base action class.

    Attributes:
        name (str): a name of this action.
        note (str, optional): a short description.
    """
    def __init__(self, name: str, note: str="nothing"):
        self.name = name
        self.note = note


class _BaseSubject(object):
    """Base subject class.

    Attributes:
        name (str): a name of this subject.
        note (str, optional): a short description.
    """
    def __init__(self, name: str, note:str ="nothing"):
        """
        Args:
            name (str): the name or title.
            note (str, optional): a short description.
        """
        self.name = name
        self.note = note

    def explain(self, info: str, obj=None, note: str="nothing"):
        """
        Args:
            info (str): a information.
            obj (:obj:`_BaseSubject`): a object of this action.
            note (str, optional): a short description.
        """
        return Action(self, ActType.EXPLAIN, Behavior.EXPLAIN, info, obj, behavior_str_of(Behavior.EXPLAIN), note=note)


class _BasePerson(_BaseSubject):
    """Basic character class.

    Attributes:
    """
    def __init__(self, name: str, age: int, sex: str, job: str, note: str="nothing"):
        """
        Args:
            name (str): character's name
            age (int): character's age
            sex (str): character's sex
            job (str): character's job
            note (str, optional): a short description.
        """
        super().__init__(name, note)
        self.age = age
        self.job = job
        self.sex = sex

    def act(self, action: str, behaviour: Behavior, obj: _BaseSubject, name: str, note: str="nothing"):
        """
        Args:
            action (str): an action string.
            behaviour (:enum:`Behavior`): a behavior type.
            obj (:obj:`_BaseSubject`): a object of this action.
            name (str): an action name.
            note (str, optional): a short description.
        Returns:
            Act object contained a personal action.
        """
        return Action(self, ActType.ACT, behaviour, action, obj, name, note=note)

    def tell(self, action: str, obj: _BaseSubject=None, note: str="nothing"):
        """
        Args:
            action (str): a short dialogue.
            obj (:obj:`_BaseSubject`): a object of this action.
            note (str, optional): a short description.
        Returns:
            Act object contained a dialogue.
        """
        return Action(self, ActType.TELL, Behavior.TELL, action, obj, behavior_str_of(Behavior.TELL), note=note)


class Action(_BaseAction):
    """A general action class.

    Attributes:
        act_type (:enum:`ActType`): an action category type.
        action (str): an action string.
        behavior (:enum:`Behavior`): a behavior type of this action.
        description (str): a description of this action.
        flag (str): a story flag to associate this action.
        deflag (str): a story deflag to associate this action.
        is_passive (bool, optional): if True is a passive mode.
        name (str): an action name.
        note (str): a short description.
        object (:obj:`_BaseSubject`): a object of this action.
        subject (:obj:`_BaseSubject`): a subject of this action.
    """

    def __init__(self, subject: _BaseSubject, act_type: ActType, behavior: Behavior, action: str="(something)",
            object_: _BaseSubject=None, name: str="行動", note: str="nothing"):
        """
        Args:
            subject (:obj:`_BaseSubject`): action subject.
            behavior (:enum:`Behavior`): action behavior type.
            action (str): description of this action.
            obj (:obj:`_BaseSubject`): an action object.
            name (str, optional): an action name.
            note (str, optional): a short description.
        """
        super().__init__(name, note)
        self.act_type = act_type
        self.action = action
        self.behavior = behavior
        self.description = ""
        self.flag = ""
        self.deflag = ""
        self.is_passive = False
        self.object = object_
        self.subject = subject

    def desc(self, desc_: str):
        self.description = desc_
        return self

    def passive(self, mode: bool=True):
        self.is_passive = mode
        return self

    def set_flag(self, flag_str: str):
        if self.flag: return self
        self.flag = flag_str
        return self

    def set_deflag(self, deflag_str: str):
        if self.deflag: return self
        self.deflag = deflag_str
        return self


class ActionGroup(_BaseAction):
    """Acrion grouping class.

    Attributes:
        actions (:tuple:obj:`Action`): action lists.
        lang (:enum:`LangType`): a language type.
        name (str): a goup name.
        note (str): a short description.
    """
    def __init__(self, *args: Action, lang: LangType=LangType.JPN, name: str="_actiongroup", note: str="nothing"):
        """
        Args:
            *args (:tuple:obj:`Action`): actions
            lang (:enum:`LangType`): a language type.
            name (str, optional): an action group name.
            note (str, optional): a short description.
        """
        super().__init__(name, note)
        self.actions = args
        self.lang = lang


class DayTime(_BaseSubject):
    """Day and Time management class.

    Attributes.
    """
    def __init__(self, name: str, mon: int=0, day: int=0, year: int=0, hour: int=0, note: str="nothing"):
        """
        Args:
            name (str): object name.
            mon (int): month number.
            day (int): day number.
            year (int): year number.
            hour (int): hour number.
            note (str, optional): a short description.
        """
        super().__init__(name, note)
        self.day = day
        self.hour = hour
        self.mon = mon
        self.year = year


class Item(_BaseSubject):
    """Item class.

    Attributes.
    """
    def __init__(self, name: str, note: str="nothing"):
        """
        Args:
            name (str): item's name.
            note (str, optional): a short description.
        """
        super().__init__(name, note)


class Master(_BaseSubject):
    """A story management class.

    Attributes:
    """
    def __init__(self, name, note="nothing"):
        super().__init__(name, note)

    def comment(self, comment_: str, obj: _BaseSubject=None, note: str="nothing"):
        return Action(self, ActType.TAG, Behavior.NONE, comment_, obj, tag_str_of(TagType.COMMENT), note)

    def story(self, *args: Action, lang: LangType=LangType.JPN, note: str="nothing"):
        return ActionGroup(name="_story", lang=lang, note=note, *args)

    def title(self, title_: str, note: str="nothing"):
        return Action(self, ActType.TAG, Behavior.NONE, title_, None, tag_str_of(TagType.TITLE), note)


class Stage(_BaseSubject):
    """Stage class.

    Attributes:
    """
    def __init__(self, name: str, note: str="nothing"):
        """
        Args:
            name (str): stage's name.
            note (str, optional): a short description.
        """
        super().__init__(name, note)


class Word(_BaseSubject):
    """Word class.

    Attributes.
    """
    def __init__(self, name: str, note: str="nothing"):
        """
        Args:
            name (str): a word title.
            note (str, optional): a short description.
        """
        super().__init__(name, note)

