# -*- coding: utf-8 -*-
"""Define a base subject class.
"""
from . import assertion as ast
from . import sobject as so


class BaseSubject(so.SObject):
    """Base subject class.

    Attributes:
        name (str): a name of this subject.
        note (str): a short description.
    """
    def __init__(self, name: str, note: str):
        """
        Args:
            name (str): the name or title.
            note (str): a short description.
        """
        self.name = ast.is_str(name)
        self.note = ast.is_str(note)

