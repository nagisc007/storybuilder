# -*- coding: utf-8 -*-
"""Define person subject.
"""
from . import assertion as ast
from . import enums as em
from . import subject as sb
from . import parser as ps
from . import utils as utl
from . import strutils as sutl


class Person(sb.Subject):
    """Person class.

    Attributes:
        age (int): an age.
        calling (dict): a calling dictionary.
        firstname (str): a first name.
        lastname (str): a last name.
        job (str): a job.
        name (str): a name (full name).
        note (str): a short description.
        sex (str): a sex.
    """
    DEF_CALLING = "私"

    def __init__(self, name: str, age: int, sex: str, job: str, calling: [dict, str]=DEF_CALLING, note: str=""):
        """
        Args:
            name (str): a person name
            age (int): a person age
            sex (str): a person sex
            job (str): a person job
            calling ([dict, str]): a calling dictionary.
            note (str, optional): a short description.
        """
        _lastname, _firstname = sutl.name_divided_from(name)
        _fullname = _lastname + _firstname if ',' in name else name
        super().__init__(_fullname, note)
        self.age = ast.is_int(age)
        self.calling = ps.str_to_dict_by_splitter(calling, "me", Person.DEF_CALLING)
        self.firstname = _firstname
        self.lastname = _lastname
        self.job = ast.is_str(job)
        self.sex = ast.is_str(sex)

    def ask(self, *args, verb: str="ask"):
        return self.talk(*args, verb=verb)

    def behav(self, *args, verb: str="behav"):
        return self.act(*args, act_type=em.ActType.BEHAV, verb=verb)

    def come(self, *args, verb: str="come"):
        return self.move(*args, verb=verb)

    def deal(self, *args, verb: str="deal"):
        return self.act(*args, act_type=em.ActType.DEAL, verb=verb)

    def feel(self, *args, verb: str="feel"):
        return self.act(*args, act_type=em.ActType.FEEL, verb=verb)

    def go(self, *args, verb: str="go"):
        return self.move(*args, verb=verb)

    def have(self, *args, verb: str="have"):
        return self.deal(*args, verb=verb)

    def hear(self, *args, verb: str="hear"):
        return self.talk(*args, verb=verb)

    def know(self, *args, verb: str="know"):
        return self.think(*args, verb=verb)

    def look(self, *args, verb: str="look"):
        return self.act(*args, act_type=em.ActType.LOOK, verb=verb)

    def meet(self, *args, verb: str="meet"):
        return self.look(*args, verb=verb)

    def move(self, *args, verb: str="move"):
        return self.act(*args, act_type=em.ActType.MOVE, verb=verb)

    def remember(self, *args, verb: str="remember"):
        return self.think(*args, verb=verb)

    def reply(self, *args, verb: str="reply"):
        return self.talk(*args, verb=verb)

    def talk(self, *args, verb: str="talk"):
        return self.act(*args, act_type=em.ActType.TALK, verb=verb)

    def think(self, *args, verb: str="think"):
        return self.act(*args, act_type=em.ActType.THINK, verb=verb)

    def inherited(self, name: str=None, age: int=None, sex: str=None, job: str=None,
            calling: str=None, note: str=None):
        return Person(
                utl.val_ifNone_default(name, self.name),
                utl.val_ifNone_default(age, self.age),
                utl.val_ifNone_default(sex, self.sex),
                utl.val_ifNone_default(job, self.job),
                utl.val_ifNone_default(calling, self.calling),
                utl.val_ifNone_default(note, self.note),
                )
