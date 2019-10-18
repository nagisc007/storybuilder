# -*- coding: utf-8 -*-
"""Define an action container class.
"""
from . import assertion
from .basecontainer import BaseContainer
from .action import Action


class CombAction(BaseContainer):
    """The container for actions.
    """
    def __init__(self, *args):
        super().__init__("__comb__")
        self._actions = CombAction._validatedActions(*args)

    @property
    def actions(self): return self._actions

    # privates
    def _validatedActions(*args):
        for a in args:
            if not isinstance(a, Action):
                raise AssertionError("Must be data type of 'Action'!")
        return args
