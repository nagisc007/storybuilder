# -*- coding: utf-8 -*-
"""Module to build a story.
"""
from abc import ABCMeta, abstractmethod
from . import assertion as ast
from . import action as act
from . import enums as em
from . import basesubject as bs


class Subject(bs.BaseSubject, metaclass=ABCMeta):
    """Base class for all subjects.

    Attributes:
        name (str): a name.
        note (str): a short description.
    """
    def __init__(self, name: str, note: str=""):
        super().__init__(name, note)

    def act(self, *args, act_type: em.ActType, verb: str):
        # TODO: check and build objects data and aux verb
        auxverb = _auxverb_from_objects(args)
        return act.Action(act_type, self, verb, auxverb,
                _actobjects_valid_converted(args))

    def be(self, *args, verb: str="be"):
        return self.act(*args, act_type=em.ActType.BE, verb=verb)

    def do(self, *args, verb: str="do"):
        return self.act(*args, act_type=em.ActType.DO, verb=verb)

    def explain(self, *args, verb: str="explain"):
        return self.act(*args, act_type=em.ActType.EXPLAIN, verb=verb)

    @abstractmethod
    def inherited(self):
        pass


# private methods
def _auxverb_from_objects(args: tuple) -> em.AuxVerb:
    from . import parser as ps
    for a in ast.is_tuple(args):
        tmp = ps.auxverb_from(a)
        if not tmp is em.AuxVerb.NONE:
            return tmp
    else:
        return em.AuxVerb.NONE


def _actobjects_valid_converted(args: tuple) -> tuple:
    from . import parser as ps
    return tuple(ps.actobject_from(v) for v in ast.is_tuple(args) if not v in em.AuxVerb.tags())
