# -*- coding: utf-8 -*-
"""Module to build a story.
"""
from abc import ABCMeta, abstractmethod
from .sbutils import assert_are_int_str, assert_isstr, assert_isint
from .action import Action 
from .basesubject import _BaseSubject
from .enums import ActType


class Subject(_BaseSubject, metaclass=ABCMeta):
    """Base class for all subjects.

    Attributes:
        name (str): a name.
        note (str): a short description.
    """
    def __init__(self, name: str, note: str=""):
        super().__init__(name, note)

    def be(self, *args, verb: str="be"):
        return Action(ActType.BE, self, verb, self.objects_from(*args))

    def do(self, *args, verb: str="do"):
        return Action(ActType.DO, self, verb, self.objects_from(*args))

    def explain(self, *args, verb: str="explain"):
        return Action(ActType.EXPLAIN, self, verb, self.objects_from(*args))

    def objects_from(self, *args):
        return tuple(_info_or_subject_from(v) for v in args)

    @abstractmethod
    def inherited(self):
        pass


class Info(Subject):
    """Information class.
    """
    _NAME = "_information"
    def __init__(self, info: str):
        assert_isstr(info)

        super().__init__(Info._NAME, info)

    def inherited(self, info: str=None):
        return Info(info if info else self.note)


class Flag(Info):
    """Flag information class.
    """
    def __init__(self, info: [str, int]):
        assert_are_int_str(info)

        super().__init__(info if isinstance(info, str) else str(info))


class Nothing(Subject):
    """Nothing class.
    """
    _NAME = "_nothing"
    def __init__(self):
        super().__init__(Nothing._NAME, "")

    def inherited(self):
        return Nothing()


class Something(Subject):
    """Something class.
    """
    _NAME = "_something"
    def __init__(self):
        super().__init__(Something._NAME, "")

    def inherited(self):
        return Something()


class Person(Subject):
    """Person class.

    Attributes:
        age (int): an age.
        calling (dict): a calling dictionary.
        job (str): a job.
        name (str): a name.
        note (str): a short description.
        sex (str): a sex.
    """
    DEF_SELFCALL = "私"

    def __init__(self, name: str, age: int, sex: str, job: str, calling: [dict, str]=DEF_SELFCALL, note: str=""):
        """
        Args:
            name (str): a person name
            age (int): a person age
            sex (str): a person sex
            job (str): a person job
            calling ([dict, str]): a calling dictionary. 
            note (str, optional): a short description.
        """
        super().__init__(name, note)
        assert_isint(age)
        assert_isstr(job)
        assert_isstr(sex)

        self.age = age
        self.calling = self._calling_dict_from(calling)
        self.job = job
        self.sex = sex

    # private methods
    def _calling_dict_from(self, target: [str, dict]) -> dict:
        if isinstance(target, dict):
            return target
        elif isinstance(target, str):
            if ":" in target:
                tmp = target.split(":")
                ret = {}
                for k, v in zip(tmp[0::2], tmp[1::2]):
                    ret[k] = v
                if not "me" in ret.keys():
                    ret.update({"me":Person.DEF_SELFCALL})
                return ret
            else:
                return {"me": target}
        else:
            return {"me": target}

    def ask(self, *args, verb: str="ask"):
        return self.talk(*args, verb=verb)

    def behav(self, *args, verb: str="behav"):
        assert_isstr(verb)

        return Action(ActType.BEHAV, self, verb, self.objects_from(*args))

    def come(self, *args, verb: str="come"):
        return self.move(*args, verb=verb)

    def deal(self, *args, verb: str="deal"):
        assert_isstr(verb)

        return Action(ActType.DEAL, self, verb, self.objects_from(*args))

    def feel(self, *args, verb: str="feel"):
        assert_isstr(verb)

        return Action(ActType.FEEL, self, verb, self.objects_from(*args))

    def go(self, *args, verb: str="go"):
        return self.move(*args, verb=verb)

    def have(self, *args, verb: str="have"):
        return self.deal(*args, verb=verb)

    def hear(self, *args, verb: str="hear"):
        return self.talk(*args, verb=verb)

    def know(self, *args, verb: str="know"):
        return self.think(*args, verb=verb)

    def look(self, *args, verb: str="look"):
        assert_isstr(verb)

        return Action(ActType.LOOK, self, verb, self.objects_from(*args))

    def meet(self, *args, verb: str="meet"):
        assert_isstr(verb)

        return Action(ActType.LOOK, self, verb, self.objects_from(*args))

    def move(self, *args, verb: str="move"):
        assert_isstr(verb)

        return Action(ActType.MOVE, self, verb, self.objects_from(*args))

    def remember(self, *args, verb: str="remember"):
        return self.think(*args, verb=verb)

    def reply(self, *args, verb: str="reply"):
        assert_isstr(verb)

        return self.talk(*args, verb=verb)

    def talk(self, *args, verb: str="talk"):
        assert_isstr(verb)

        return Action(ActType.TALK, self, verb, self.objects_from(*args))

    def think(self, *args, verb: str="think"):
        assert_isstr(verb)

        return Action(ActType.THINK, self, verb, self.objects_from(*args))

    def inherited(self, name: str=None, age: int=None, sex: str=None, job: str=None,
            calling: str=None, note: str=None):
        return Person(
                name if name else self.name,
                age if not age is None else self.age,
                sex if sex else self.sex,
                job if job else self.job,
                calling if calling else self.calling,
                note if note else self.note)


class Day(Subject):
    """Day and Time management class.

    Attributes.
        day (int): a day number.
        hour (int): a hour number.
        min (int): a minute number.
        mon (int): a month number.
        name (str): a day name.
        note (str): a short description.
        year (int): a year number.
    """
    def __init__(self, name: str, mon: int=0, day: int=0, year: int=0,
            hour: int=0, min: int=0, note: str=""):
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

    def _val_if_isNone_0(self, val: [int, None]) -> int:
        return val if not val is None else 0

    def elapse(self, mon: int=None, day: int=None, year: int=None,
            hour: int=None, min: int=None, note: str=None):
        etime = self.elapsed_day(mon, day, year, hour, min, note)
        return Action(ActType.BE, etime, "elapse", self.objects_from((etime,)))

    def elapsed(self, *args, mon: int=None, day: int=None, year: int=None,
            hour: int=None, min: int=None, note: str=None, is_added: bool=True):
        eday = self.elapsed_day(mon, day, year, hour, min, note, is_added)
        return eday.explain(*args)

    def elapsed_info(self, mon: int=None, day: int=None, year: int=None,
            hour: int=None, min: int=None, note: str=None, is_added: bool=True):
        return Info(self.elapsed_day(mon, day, year, hhour, min, note, is_added).time_str())

    def elapsed_day(self, mon: int=None, day: int=None, year: int=None,
            hour: int=None, min: int=None, note: str=None, is_added: bool=True):
        def added_if(val, _is_added):
            return val if _is_added else 0
        return self.inherited(
                self.name,
                added_if(self.mon, is_added) + self._val_if_isNone_0(mon),
                added_if(self.day, is_added) + self._val_if_isNone_0(day),
                added_if(self.year, is_added) + self._val_if_isNone_0(year),
                added_if(self.hour, is_added) + self._val_if_isNone_0(hour),
                added_if(self.min, is_added) + self._val_if_isNone_0(min),
                note if note else self.note,
                )

    def inherited(self, name: str=None, mon: int=None, day: int=None, year: int=None,
            hour: int=None, min_: int=None, note: str=None):
        return Day(
                name if name else self.name,
                mon if not mon is None else self.mon,
                day if not day is None else self.day,
                year if not year is None else self.year,
                hour if not hour is None else self.hour,
                min_ if not min_ is None else self.min,
                note if note else self.note)

    def time_str(self) -> str:
        return "{year}/{mon}/{day}-{hour}:{minu}".format(
                year=self.year,
                mon=self.mon,
                day=self.day,
                hour=self.hour,
                minu=self.min,
                )

class Item(Subject):
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

    def move(self, *args, verb: str="move"):
        return Action(ActType.MOVE, self, verb, self.objects_from(*args))

    def inherited(self, name: str=None, note: str=None):
        return Item(name if name else self.name, note if note else self.note)


class Stage(Subject):
    """Stage class.

    Attributes:
        name (str): a stage name.
        note (str): a short description.
        parent (obj:`Stage`): a parent stage.
    """
    def __init__(self, name: str, note: str="", parent=None):
        """
        Args:
            name (str): a stage name.
            note (str, optional): a short description.
            parent (obj:`Stage`): a parent stage.
        """
        super().__init__(name, note)
        self.parent = parent

    def move(self, *args, verb: str="move"):
        return Action(ActType.MOVE, self, verb, self.objects_from(*args))

    def inherited(self, name: str=None, note: str=None):
        return Stage(name if name else self.name, note if note else self.note, parent=self)

    def insided(self, name: str=None, note: str=None):
        return self.inherited(name, note)


class Word(Subject):
    """Word class.

    Attributes.
        name (str): a word title.
        note (str): a short description.
    """
    def __init__(self, name: str, note: str=""):
        """
        Args:
            name (str): a word title.
            note (str, optional): a short description.
        """
        super().__init__(name, note)

    def inherited(self, name: str=None, note: str=None):
        return Word(name if name else self.name, note if note else self.note)


# private functions
def _info_or_subject_from(target) -> [Info, Nothing, _BaseSubject]:
    if isinstance(target, _BaseSubject):
        return target
    elif isinstance(target, str):
        return Info(target)
    elif isinstance(target, int):
        return Info("number_" + str(target))
    else:
        return Nothing()
