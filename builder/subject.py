# -*- coding: utf-8 -*-
"""Module to build a story.
"""
from .action import _BaseAction, Action, ActionGroup
from .basesubject import _BaseSubject
from .behavior import Behavior
from .enums import ActType, GroupType, LangType, TagType


class _BasePerson(_BaseSubject):
    """Basic character class.

    Attributes:
    """
    def __init__(self, name: str, age: int, sex: str, job: str, info: str="", note: str="", parent: _BaseSubject=None):
        """
        Args:
            name (str): character's name
            age (int): character's age
            sex (str): character's sex
            job (str): character's job
            info (str, optional): a information.
            note (str, optional): a short description.
            parent (:obj:`_BaseSubject`): a parent person.
        """
        super().__init__(name, info, note, parent)
        self.age = age
        self.job = job
        self.sex = sex

    def act(self, behaviour: Behavior, objects: tuple, info: str="", note: str=""):
        """
        Args:
            behaviour (:enum:`Behavior`): a behavior type.
            objects (:tuple:obj:`_BaseSubject`): objects of the action.
            info (str, optional): a information of the action.
            note (str, optional): a short description.
        Returns:
            Act object contained a personal action.
        """
        return Action(self, ActType.ACT, behaviour, objects, info, note)

    def explain(self, info: str, a: _BaseSubject=None, about: _BaseSubject=None, asa: _BaseSubject=None, at: _BaseSubject=None, by: _BaseSubject=None, fo: _BaseSubject=None, frm: _BaseSubject=None, of: _BaseSubject=None, on: _BaseSubject=None, to: _BaseSubject=None, wth: _BaseSubject=None, note: str=""):
        """
        Args:
            info (str): a short dialogue.
            note (str, optional): a short description.
        Returns:
            Act object contained a dialogue.
        """
        return Action(self, ActType.EXPLAIN, Behavior.EXPLAIN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def inherit(self, name: str, age: int, sex: str, job: str, info: str="", note: str=""):
        """
        Args:
            name (str): a character name.
            age (int): a character age.
            sex (str): a character sex.
            job (str): a character job.
            info (str, optional): a information.
            note (str, optional): a short description.
        """
        return _BasePerson(name, age, sex, job, info, note, self)

    def tell(self, info: str, a: _BaseSubject=None, about: _BaseSubject=None, asa: _BaseSubject=None, at: _BaseSubject=None, by: _BaseSubject=None, fo: _BaseSubject=None, frm: _BaseSubject=None, of: _BaseSubject=None, on: _BaseSubject=None, to: _BaseSubject=None, wth: _BaseSubject=None, note: str=""):
        """
        Args:
            info (str): a short dialogue.
            obj (:obj:`_BaseSubject`, optional): a object of this action.
            note (str, optional): a short description.
        Returns:
            Act object contained a dialogue.
        """
        return Action(self, ActType.TELL, Behavior.TELL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)



class DayTime(_BaseSubject):
    """Day and Time management class.

    Attributes.
        day (int): a day number.
        hour (int): a hour number.
        info (str): a information.
        min (int): a minute number.
        mon (int): a month number.
        name (str): a day name.
        note (str): a short description.
        parent (:obj:`_BaseSubject`): a parent.
        year (int): a year number.
    """
    def __init__(self, name: str, mon: int=0, day: int=0, year: int=0, hour: int=0, min: int=0, info: str="", note: str="", parent: _BaseSubject=None):
        """
        Args:
            name (str): a day name.
            mon (int): a month number.
            day (int): a day number.
            year (int): a year number.
            hour (int): a hour number.
            min (int): a minute number.
            info (str, optional): a information.
            note (str, optional): a short description.
            parent (:obj:`_BaseSubject`): a parent.
        """
        super().__init__(name, info, note, parent)
        self.day = day
        self.hour = hour
        self.min = min
        self.mon = mon
        self.year = year

    def explain(self, info: str, a: _BaseSubject=None, about: _BaseSubject=None, asa: _BaseSubject=None, at: _BaseSubject=None, by: _BaseSubject=None, fo: _BaseSubject=None, frm: _BaseSubject=None, of: _BaseSubject=None, on: _BaseSubject=None, to: _BaseSubject=None, wth: _BaseSubject=None, note: str=""):
        """
        Args:
            info (str): a short dialogue.
            note (str, optional): a short description.
        Returns:
            Act object contained a dialogue.
        """
        return Action(self, ActType.EXPLAIN, Behavior.EXPLAIN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def inherit(self, name: str, mon: int=0, day: int=0, year: int=0, hour: int=0, min: int=0, note: str=""):
        return DayTime(
                name,
                mon if mon else self.mon,
                day if day else self.day,
                year if year else self.year,
                hour if hour else self.hour,
                min if min else self.min,
                note if note else self.notei,
                self)


class Item(_BaseSubject):
    """Item class.

    Attributes.
        info (str): a information.
        name (str): a item name.
        note (str, optional): a short description.
        parent (:obj:`_BaseSubject`): a parent.
    """
    def __init__(self, name: str, info: str="", note: str="", parent: _BaseSubject=None):
        """
        Args:
            name (str): a item name.
            info (str, optional): a information.
            note (str, optional): a short description.
            parent (:obj:`_BaseSubject`): a panret.
        """
        super().__init__(name, info, note, parent)

    def explain(self, info: str, a: _BaseSubject=None, about: _BaseSubject=None, asa: _BaseSubject=None, at: _BaseSubject=None, by: _BaseSubject=None, fo: _BaseSubject=None, frm: _BaseSubject=None, of: _BaseSubject=None, on: _BaseSubject=None, to: _BaseSubject=None, wth: _BaseSubject=None, note: str=""):
        """
        Args:
            info (str): a short dialogue.
            note (str, optional): a short description.
        Returns:
            Act object contained a dialogue.
        """
        return Action(self, ActType.EXPLAIN, Behavior.EXPLAIN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def inherit(self, name: str, info: str="", note: str=""):
        return Item(name, info, note, self)


class Master(_BaseSubject):
    """A story management class.

    Attributes:
    """
    def __init__(self, name: str, info: str="", note: str=""):
        """
        Args:
            name (str): a master name.
            info (str, optional): a information.
            note (str, optional): a short description.
        """
        super().__init__(name, info, note, None)

    def combine(self, *args: _BaseAction, lang: LangType=LangType.JPN, note: str=""):
        """
        Args:
            *args (:tuple:obj:`_BaseAction`): a combined actions.
            lang (:enum:`LangType`, optional): a language type.
            note (str, optional): a short description.
        """
        return ActionGroup(lang=lang, group_type=GroupType.COMBI, note=note, *args)

    def comment(self, comment_: str):
        """
        Args:
            comment_ (str): a comment.
        """
        return Action(self, ActType.TAG, Behavior.NONE, None, comment_, str(TagType.COMMENT))

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
        return Action(self, ActType.TAG, Behavior.NONE, None, title_, str(TagType.TITLE))


class Something(_BaseSubject):
    """Something object class.

    Attributes:
    """
    _NAME = "_something"
    def __init__(self):
        super().__init__(Something._NAME, "", "")


class Stage(_BaseSubject):
    """Stage class.

    Attributes:
        info (str): a information.
        name (str): a stage name.
        note (str): a short description.
        parent (:obj:`_BaseSubject`): a parent.
    """
    def __init__(self, name: str, info: str="", note: str="", parent: _BaseSubject=None):
        """
        Args:
            name (str): a stage name.
            info (str, optional): a infomation.
            note (str, optional): a short description.
            parent (:obj:`_BaseSubject`): a parent.
        """
        super().__init__(name, info, note, parent)

    def explain(self, info: str, a: _BaseSubject=None, about: _BaseSubject=None, asa: _BaseSubject=None, at: _BaseSubject=None, by: _BaseSubject=None, fo: _BaseSubject=None, frm: _BaseSubject=None, of: _BaseSubject=None, on: _BaseSubject=None, to: _BaseSubject=None, wth: _BaseSubject=None, note: str=""):
        """
        Args:
            info (str): a short dialogue.
            note (str, optional): a short description.
        Returns:
            Act object contained a dialogue.
        """
        return Action(self, ActType.EXPLAIN, Behavior.EXPLAIN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def inherit(self, name: str, info: str="", note: str=""):
        return Stage(name, info, note, self)


class Word(_BaseSubject):
    """Word class.

    Attributes.
        name (str): a word title.
        info (str): a information about the word.
        note (str): a short description.
        parent (:obj:`_BaseSubject`): a parent.
    """
    def __init__(self, name: str, info: str="", note: str="", parent: _BaseSubject=None):
        """
        Args:
            name (str): a word title.
            info (str, optional): a information.
            note (str, optional): a short description.
            parent (:obj:`_BaseSubject`): a parent.
        """
        super().__init__(name, info, note, parent)

    def explain(self, info: str, a: _BaseSubject=None, about: _BaseSubject=None, asa: _BaseSubject=None, at: _BaseSubject=None, by: _BaseSubject=None, fo: _BaseSubject=None, frm: _BaseSubject=None, of: _BaseSubject=None, on: _BaseSubject=None, to: _BaseSubject=None, wth: _BaseSubject=None, note: str=""):
        """
        Args:
            info (str): a short dialogue.
            note (str, optional): a short description.
        Returns:
            Act object contained a dialogue.
        """
        return Action(self, ActType.EXPLAIN, Behavior.EXPLAIN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def inherit(self, name: str, info: str="", note: str=""):
        return Word(name, info, note, self)


# functions
def something() -> Something:
    return Something()

