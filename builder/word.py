# -*- coding: utf-8 -*-
"""Define word class.
"""
from . import assertion
from .basedata import BaseData


class Word(BaseData):
    """Data type of a word.
    """
    def __init__(self, name: str, note: str):
        super().__init__(name)
        self._note = assertion.is_str(note)

    @property
    def note(self): return self._note

