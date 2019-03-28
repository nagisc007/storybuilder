# -*- coding: utf-8 -*-
"""Module to build a story.
"""
from .acttypes import ActType, GroupType, TagType, LangType
from .acttypes import group_name_of, tag_str_of
from .behavior import Behavior
from .behavior import behavior_str_of


class _BaseAction(object):
    """Base action class.

    Attributes:
        name (str): a name of the action.
        note (str): a short description.
    """
    def __init__(self, name: str, note):
        self.name = name
        self.note = note


class _BaseSubject(object):
    """Base subject class.

    Attributes:
        name (str): a name of this subject.
        note (str, optional): a short description.
    """
    def __init__(self, name: str, note:str =""):
        """
        Args:
            name (str): the name or title.
            note (str, optional): a short description.
        """
        self.name = name
        self.note = note

    def explain(self, info: str, obj=None, note: str=""):
        """
        Args:
            info (str): a information.
            obj (:obj:`_BaseSubject`, optional): a object of this action.
            note (str, optional): a short description.
        """
        return Action(self, ActType.EXPLAIN, Behavior.EXPLAIN, obj, info, note)


class _BasePerson(_BaseSubject):
    """Basic character class.

    Attributes:
    """
    def __init__(self, name: str, age: int, sex: str, job: str, note: str=""):
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

    def act(self, behaviour: Behavior, obj: _BaseSubject, info: str="", note: str=""):
        """
        Args:
            behaviour (:enum:`Behavior`): a behavior type.
            obj (:obj:`_BaseSubject`): a object of the action.
            info (str, optional): a information of the action.
            note (str, optional): a short description.
        Returns:
            Act object contained a personal action.
        """
        return Action(self, ActType.ACT, behaviour, obj, info, note)

    def tell(self, info: str, obj: _BaseSubject=None, note: str=""):
        """
        Args:
            info (str): a short dialogue.
            obj (:obj:`_BaseSubject`, optional): a object of this action.
            note (str, optional): a short description.
        Returns:
            Act object contained a dialogue.
        """
        return Action(self, ActType.TELL, Behavior.TELL, obj, info, note)


class Action(_BaseAction):
    """A general action class.

    Attributes:
        act_type (:enum:`ActType`): an action category type.
        behavior (:enum:`Behavior`): a behavior type of this action.
        descriptions (:tuple:str): descriptions of this action.
        flag (str): a story flag to associate this action.
        deflag (str): a story deflag to associate this action.
        info (str): a information of the action.
        is_negative (bool): if True is a negative mode.
        is_passive (bool): if True is a passive mode.
        note (str): a short description.
        object (:obj:`_BaseSubject`): a object of this action.
        priority (:int): a action priotiry.
        subject (:obj:`_BaseSubject`): a subject of this action.
    """
    @classmethod
    def assert_subject(cls, target: _BaseSubject):
        if not target:
            return None
        assert isinstance(target, _BaseSubject), "object type {} is a mismatch!".format(type(target))
        return target

    CLS_NAME = "_action"
    DEFAULT_PRIORITY = 5
    MAX_PRIORITY = 10
    MIN_PRIORITY = 0

    def __init__(self, subject: _BaseSubject, act_type: ActType, behavior: Behavior,
            object_: _BaseSubject, info: str, note: str):
        """
        Args:
            subject (:obj:`_BaseSubject`): action subject.
            behavior (:enum:`Behavior`): action behavior type.
            obj (:obj:`_BaseSubject`): an action object.
            info (str, optional): an action name.
            note (str, optional): a short description.
        """
        super().__init__(Action.CLS_NAME, note)
        self.act_type = act_type
        self.behavior = behavior
        self.deflag = ""
        self.descriptions = ()
        self.flag = ""
        self.info = info
        self.is_negative = False
        self.is_passive = False
        self.object = Action.assert_subject(object_)
        self.priority = Action.DEFAULT_PRIORITY
        self.subject = Action.assert_subject(subject)
        

    def desc(self, *args):
        self.descriptions = args
        return self

    def negative(self):
        self.is_negative = True
        return self

    def non(self): return self.negative()

    def passive(self):
        self.is_passive = True
        return self

    def ps(self): return self.passive()

    def set_flag(self, flag_str: str):
        if self.flag: return self
        self.flag = flag_str
        return self

    def set_deflag(self, deflag_str: str):
        if self.deflag: return self
        self.deflag = deflag_str
        return self

    def set_priority(self, pri: int):
        self.priority = pri
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
            lang (:enum:`LangType`): a language type.
            note (str, optional): a short description.
        """
        super().__init__(ActionGroup.CLS_NAME, note)
        self.actions = args
        self.group_type = group_type
        self.lang = lang


class DayTime(_BaseSubject):
    """Day and Time management class.

    Attributes.
        day (int): a day number.
        hour (int): a hour number.
        min (int): a minute number.
        mon (int): a month number.
        name (str): a day name.
        year (int): a year number.
    """
    def __init__(self, name: str, mon: int=0, day: int=0, year: int=0, hour: int=0, min: int=0, note: str=""):
        """
        Args:
            name (str): a day name.
            mon (int): a month number.
            day (int): a day number.
            year (int): a year number.
            hour (int): a hour number.
            min (int): a minute number.
            note (str, optional): a short description.
        """
        super().__init__(name, note)
        self.day = day
        self.hour = hour
        self.min = min
        self.mon = mon
        self.year = year


class Item(_BaseSubject):
    """Item class.

    Attributes.
        name (str): a item name.
        note (str, optional): a short description.
    """
    def __init__(self, name: str, note: str=""):
        """
        Args:
            name (str): a item name.
            note (str, optional): a short description.
        """
        super().__init__(name, note)


class Master(_BaseSubject):
    """A story management class.

    Attributes:
    """
    def __init__(self, name, note=""):
        """
        Args:
            name (str): a master name.
            note (str, optional): a short description.
        """
        super().__init__(name, note)

    def combine(self, *args: _BaseAction, lang: LangType.JPN, note: str=""):
        """
        Args:
            *args (:tuple:obj:`_BaseAction`): a combined actions.
            lang (:enum:`LangType`): a language type.
            note (str, optional): a short description.
        """
        return ActionGroup(lang=lang, group_type=GroupType.COMBI, note=note, *args)

    def comment(self, comment_: str):
        """
        Args:
            comment_ (str): a comment.
        """
        return Action(self, ActType.TAG, Behavior.NONE, None, comment_, tag_str_of(TagType.COMMENT))

    def scene(self, title: str, *args: _BaseAction, lang: LangType=LangType.JPN, note: str=""):
        """
        Args:
            title (str): a scene title.
            *args (:tuple:obj:`_BaseAction`): a scene actions.
            lang (:enum:`LangType`): a scene language type.
            note (str, optional): a short description.
        """
        tmp = ()
        if isinstance(title, str):
            tmp = (self.title(title),) + args
        else:
            tmp = (title,) + args
        return ActionGroup(lang=lang, group_type=GroupType.SCENE, note=note, *tmp)

    def story(self, title: str, *args: _BaseAction, lang: LangType=LangType.JPN, note: str=""):
        """
        Args:
            title (str): a story title.
            *args (:tuple:obj:`_BaseAction`): a story actions.
            lang (:enum:`LangType`): a story language type.
            note (str, optional): a short description.
        """
        tmp = ()
        if isinstance(title, str):
            tmp = (self.title(title),) + args
        else:
            tmp = (title,) + args
        return ActionGroup(lang=lang, group_type=GroupType.STORY, note=note, *tmp)

    def title(self, title_: str):
        """
        Args:
            title_ (str): a story title inserted.
        """
        return Action(self, ActType.TAG, Behavior.NONE, None, title_, tag_str_of(TagType.TITLE))


class Stage(_BaseSubject):
    """Stage class.

    Attributes:
        name (str): a stage name.
        note (str): a short description.
    """
    def __init__(self, name: str, note: str=""):
        """
        Args:
            name (str): a stage name.
            note (str, optional): a short description.
        """
        super().__init__(name, note)


class Word(_BaseSubject):
    """Word class.

    Attributes.
        name (str): a word title.
        info (str): a information about the word.
        note (str): a short description.
    """
    def __init__(self, name: str, info: str="", note: str=""):
        """
        Args:
            name (str): a word title.
            info (str, optional): a information.
            note (str, optional): a short description.
        """
        super().__init__(name, note)
        self.info = info

