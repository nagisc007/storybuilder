# -*- coding: utf-8 -*-
"""Define item subject.
"""
from . import assertion as ast
from . import subject as sb


class Item(sb.Subject):
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

    def move(self, *args, verb: str="move", is_desc: bool=True):
        return self.act(*args, act_type=sb.em.ActType.MOVE, verb=verb, is_desc=is_desc)

    def inherited(self, name: str=None, note: str=None):
        return Item(name if name else self.name, note if note else self.note)


