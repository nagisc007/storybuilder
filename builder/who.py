# -*- coding: utf-8 -*-
"""Define who class.
"""
from . import assertion
from .basesubject import BaseSubject


class Who(BaseSubject):
    """For a pronoun class.
    """
    DEF_NAME = "__who__"

    def __init__(self):
        super().__init__(Who.DEF_NAME)

