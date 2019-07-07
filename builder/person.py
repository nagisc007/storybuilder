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
    Attributes(features):
        body (str): a body info.
        eyes (str): eyes info.
        fashion (str): a fashion info.
        hair (str): a hair info.
        height (str): a height info.
        ornament (str): a ornament info.
        weight (str): a weight info.
    """
    DEF_CALLING = "私"
    DEF_HAIR = "黒髪"

    def __init__(self, name: str, age: int, sex: str, job: str, calling: [dict, str]=DEF_CALLING,
            note: str="", features: [dict, str]=""):
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
        self._set_features(features)

    def ask(self, *args, verb: str="ask", is_desc: bool=False):
        return self.talk(*args, verb=verb, is_desc=is_desc)

    def behav(self, *args, verb: str="behav", is_desc: bool=True):
        return self.act(*args, act_type=em.ActType.BEHAV, verb=verb, is_desc=is_desc)

    def come(self, *args, verb: str="come", is_desc: bool=True):
        return self.move(*args, verb=verb, is_desc=is_desc)

    def deal(self, *args, verb: str="deal", is_desc: bool=True):
        return self.act(*args, act_type=em.ActType.DEAL, verb=verb, is_desc=is_desc)

    def feel(self, *args, verb: str="feel", is_desc: bool=True):
        return self.act(*args, act_type=em.ActType.FEEL, verb=verb, is_desc=is_desc)

    def go(self, *args, verb: str="go", is_desc: bool=True):
        return self.move(*args, verb=verb, is_desc=is_desc)

    def have(self, *args, verb: str="have", is_desc: bool=True):
        return self.deal(*args, verb=verb, is_desc=is_desc)

    def hear(self, *args, verb: str="hear", is_desc: bool=True):
        return self.talk(*args, verb=verb, is_desc=is_desc)

    def know(self, *args, verb: str="know", is_desc: bool=True):
        return self.think(*args, verb=verb, is_desc=is_desc)

    def look(self, *args, verb: str="look", is_desc: bool=True):
        return self.act(*args, act_type=em.ActType.LOOK, verb=verb, is_desc=is_desc)

    def meet(self, *args, verb: str="meet", is_desc: bool=True):
        return self.look(*args, verb=verb, is_desc=is_desc)

    def move(self, *args, verb: str="move", is_desc: bool=True):
        return self.act(*args, act_type=em.ActType.MOVE, verb=verb, is_desc=is_desc)

    def remember(self, *args, verb: str="remember", is_desc: bool=True):
        return self.think(*args, verb=verb, is_desc=is_desc)

    def reply(self, *args, verb: str="reply", is_desc: bool=False):
        return self.talk(*args, verb=verb, is_desc=is_desc)

    def talk(self, *args, verb: str="talk", is_desc: bool=False):
        return self.act(*args, act_type=em.ActType.TALK, verb=verb, is_desc=is_desc)

    def think(self, *args, verb: str="think", is_desc: bool=True):
        return self.act(*args, act_type=em.ActType.THINK, verb=verb, is_desc=is_desc)

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
    # private
    def _set_features(self, features: [dict, str]):
        tmp = ps.str_to_dict_by_splitter(features, "hair", Person.DEF_HAIR)
        def creator(dct, key):
            return dct[key] if key in dct else ""
        self.body = creator(tmp, "body")
        self.eyes = creator(tmp, "eyes")
        self.fashion = creator(tmp, "fashion")
        self.hair = creator(tmp, "hair")
        self.height = creator(tmp, "height")
        self.ornament = creator(tmp, "ornament")
        self.weight = creator(tmp, "weight")

