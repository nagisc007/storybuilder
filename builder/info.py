# -*- coding: utf-8 -*-
"""Define information subjects.
"""
from . import assertion as ast
from . import subject as sb
from . import utils as utl


class Info(sb.Subject):
    """Information class.
    """
    _NAME = "information"

    def __init__(self, info: str):
        super().__init__(Info._NAME, info)

    def inherited(self, info: str=None):
        return Info(utl.val_ifNone_default(info, self.note))


class Flag(Info):
    """Flag information class.
    """
    def __init__(self, info: [str, int]):
        super().__init__(info if isinstance(info, str) else str(info))

    def inherited(self, info: str):
        return Flag(info)


class Deflag(Info):
    """Resolved flag information.
    """
    def __init__(self, info: str):
        super().__init__(info)

    def inherited(self, info: str):
        return Deflag(info)


class Selector(Flag): # pragma: no cover
    """Selection information class.
    """
    # TODO: implement
    def __init__(self, info):
        super().__init__(info)

    def inherited(self, info: str):
        return Selector(info)


class Nothing(sb.Subject):
    """Nothing class.
    """
    _NAME = "nothing"
    def __init__(self):
        super().__init__(Nothing._NAME, "")

    def inherited(self):
        return Nothing()


class Something(sb.Subject):
    """Something class.
    """
    _NAME = "something"
    def __init__(self):
        super().__init__(Something._NAME, "")

    def inherited(self):
        return Something()

