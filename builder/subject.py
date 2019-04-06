# -*- coding: utf-8 -*-
"""Module to build a story.
"""
from .sbutils import assert_isstr, assert_isint
from .action import _BaseAction, Action, ActionGroup, TagAction
from .basesubject import _BaseSubject
from .behavior import Behavior
from .enums import ActType, GroupType, LangType, TagType


class _BasePerson(_BaseSubject):
    """Basic character class.

    Attributes:
        age (int): an age.
        job (str): a job.
        name (str): a name.
        note (str): a short description.
        sex (str): a sex.
    """
    CLS_NAME = "_baseperson"
    def __init__(self, name: str, age: int, sex: str, job: str, note: str="", parent: _BaseSubject=None):
        """
        Args:
            name (str): character's name
            age (int): character's age
            sex (str): character's sex
            job (str): character's job
            note (str, optional): a short description.
            parent (:obj:`_BaseSubject`): a parent person.
        """
        super().__init__(name, note, parent)
        assert_isint(age)
        assert_isstr(job)
        assert_isstr(sex)

        self.age = age
        self.job = job
        self.sex = sex

    def act(self, behaviour: Behavior, objects: tuple):
        """
        Args:
            behaviour (:enum:`Behavior`): a behavior type.
            objects (:tuple:obj:`_BaseSubject`): objects of the action.
        Returns:
            Act object contained a personal action.
        """
        return Action(self, ActType.ACT, behaviour, objects)

    def inherit(self, name: str, age: int, sex: str, job: str, note: str=""):
        """
        Args:
            name (str): a character name.
            age (int): a character age.
            sex (str): a character sex.
            job (str): a character job.
            note (str, optional): a short description.
        """
        return _BasePerson(name, age, sex, job, note, self)

    def tell(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None) -> Action:
        """
        Args:
            info (str): a short dialogue.
            obj (:obj:`_BaseSubject`, optional): a object of this action.
        Returns:
            Act object contained a dialogue.
        """
        return Action(self, ActType.TELL, Behavior.TELL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))



class DayTime(_BaseSubject):
    """Day and Time management class.

    Attributes.
        day (int): a day number.
        hour (int): a hour number.
        min (int): a minute number.
        mon (int): a month number.
        name (str): a day name.
        note (str): a short description.
        parent (:obj:`_BaseSubject`): a parent.
        year (int): a year number.
    """
    CLS_NAME = "_daytime"
    def __init__(self, name: str, mon: int=0, day: int=0, year: int=0, hour: int=0, min: int=0, note: str="", parent: _BaseSubject=None):
        """
        Args:
            name (str): a day name.
            mon (int): a month number.
            day (int): a day number.
            year (int): a year number.
            hour (int): a hour number.
            min (int): a minute number.
            note (str, optional): a short description.
            parent (:obj:`_BaseSubject`): a parent.
        """
        super().__init__(name, note, parent)
        assert_isint(day)
        assert_isint(hour)
        assert_isint(min)
        assert_isint(mon)
        assert_isint(year)

        self.day = day
        self.hour = hour
        self.min = min
        self.mon = mon
        self.year = year

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
        name (str): a item name.
        note (str, optional): a short description.
        parent (:obj:`_BaseSubject`): a parent.
    """
    CLS_NAME = "_item"
    def __init__(self, name: str, note: str="", parent: _BaseSubject=None):
        """
        Args:
            name (str): a item name.
            note (str, optional): a short description.
            parent (:obj:`_BaseSubject`): a panret.
        """
        super().__init__(name, note, parent)

    def inherit(self, name: str, note: str=""):
        return Item(name, note, self)


class Master(_BaseSubject):
    """A story management class.

    Attributes:
        name (str): a name.
        note (str): a short description.
    """
    CLS_NAME = "_master"
    def __init__(self, name: str, note: str=""):
        """
        Args:
            name (str): a master name.
            note (str, optional): a short description.
        """
        super().__init__(name, note, None)

    def _args_with_title_if(self, title: str, args: tuple) -> tuple:
        if isinstance(title, str):
            return (self.title(title),) + args
        else:
            return (title,) + args
 
    def break_symbol(self, char: str) -> TagAction:
        """
        Args:
            char (str): a symbol character.
        Returns:
            TagAction object.
        """
        assert_isstr(char)

        return TagAction(TagType.SYMBOL, char)

    def combine(self, *args: _BaseAction, lang: LangType=LangType.JPN):
        """
        Args:
            *args (:tuple:obj:`_BaseAction`): a combined actions.
            lang (:enum:`LangType`, optional): a language type.
        """
        return ActionGroup(lang=lang, group_type=GroupType.COMBI,  *args)

    def comment(self, comment_: str):
        """
        Args:
            comment_ (str): a comment.
        """
        return TagAction(TagType.COMMENT, comment_)

    def hr(self):
        """Horizontal line.
        """
        return TagAction(TagType.HR, "")

    def scene(self, title: str, *args: _BaseAction, lang: LangType=LangType.JPN):
        """
        Args:
            title (str): a scene title.
            *args (:tuple:obj:`_BaseAction`): a scene actions.
            lang (:enum:`LangType`): a scene language type.
        """
        return ActionGroup(lang=lang, group_type=GroupType.SCENE, *self._args_with_title_if(title, args))

    def story(self, title: str, *args: _BaseAction, lang: LangType=LangType.JPN):
        """
        Args:
            title (str): a story title.
            *args (:tuple:obj:`_BaseAction`): a story actions.
            lang (:enum:`LangType`): a story language type.
        """
        return ActionGroup(lang=lang, group_type=GroupType.STORY, *self._args_with_title_if(title, args))

    def title(self, title_: str):
        """
        Args:
            title_ (str): a story title inserted.
        """
        return TagAction(TagType.TITLE, title_)


class Something(_BaseSubject):
    """Something object class.

    Attributes:
        (nothing)
    """
    CLS_NAME = "_something"
    def __init__(self):
        super().__init__(Something.CLS_NAME, "", None)


class Stage(_BaseSubject):
    """Stage class.

    Attributes:
        name (str): a stage name.
        note (str): a short description.
        parent (:obj:`_BaseSubject`): a parent.
    """
    CLS_NAME = "_stage"
    def __init__(self, name: str, note: str="", parent: _BaseSubject=None):
        """
        Args:
            name (str): a stage name.
            note (str, optional): a short description.
            parent (:obj:`_BaseSubject`): a parent.
        """
        super().__init__(name, note, parent)

    def inherit(self, name: str, note: str=""):
        return Stage(name, note, self)


class Word(_BaseSubject):
    """Word class.

    Attributes.
        name (str): a word title.
        note (str): a short description.
        parent (:obj:`_BaseSubject`): a parent.
    """
    CLS_NAME = "_word"
    def __init__(self, name: str, note: str="", parent: _BaseSubject=None):
        """
        Args:
            name (str): a word title.
            note (str, optional): a short description.
            parent (:obj:`_BaseSubject`): a parent.
        """
        super().__init__(name, note, parent)

    def inherit(self, name: str, note: str=""):
        return Word(name, note, self)


# functions
def something() -> Something:
    return Something()

