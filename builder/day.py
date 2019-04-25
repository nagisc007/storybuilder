# -*- coding: utf-8 -*-
"""Define day subject.
"""
from . import assertion as ast
from . import subject as sb
from . import utils as utl


class Day(sb.Subject):
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
        self.day = ast.is_int(day)
        self.hour = ast.is_int(hour)
        self.min = ast.is_int(min)
        self.mon = ast.is_int(mon)
        self.year = ast.is_int(year)

    def elapsed(self, name: str=None, mon: int=None, day: int=None, year: int=None,
            hour: int=None, min: int=None, note: str=None, is_added: bool=True):
        def added_if(body, val):
            return val if _is_added else 0
        tmp = self.inherited(name, mon, day, year, hour, min, note)
        if is_added:
            tmp.mon += utl.val_ifNone_default(self.mon, 0)
            tmp.day += utl.val_ifNone_default(self.day, 0)
            tmp.year += utl.val_ifNone_default(self.year, 0)
            tmp.hour += utl.val_ifNone_default(self.hour, 0)
            tmp.min += utl.val_ifNone_default(self.min, 0)
        return tmp

    def inherited(self, name: str=None, mon: int=None, day: int=None, year: int=None,
            hour: int=None, min: int=None, note: str=None):
        return Day(
                utl.val_ifNone_default(name, self.name),
                utl.val_ifNone_default(mon, self.mon),
                utl.val_ifNone_default(day, self.day),
                utl.val_ifNone_default(year, self.year),
                utl.val_ifNone_default(hour, self.hour),
                utl.val_ifNone_default(min, self.min),
                utl.val_ifNone_default(note, self.note),
                )

