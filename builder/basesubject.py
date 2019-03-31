# -*- coding: utf-8 -*-
"""Define a base subject class.
"""


class _BaseSubject(object):
    """Base subject class.

    Attributes:
        info (str): a information.
        name (str): a name of this subject.
        note (str, optional): a short description.
        parent (:obj:`_BaseSubject`): a parent subject.
    """
    def __init__(self, name: str, info: str, note: str, parent=None):
        """
        Args:
            name (str): the name or title.
            info (str): a information.
            note (str): a short description.
            parent (:obj:`_BaseSubject`): a parent subject.
        """
        self.info = info
        self.name = name
        self.note = note
        self.parent = parent

