# -*- coding: utf-8 -*-
"""Define chapter class.
"""
from . import assertion
from .basecontainer import BaseContainer
from .episode import Episode
from .action import Action


class Chapter(BaseContainer):
    """The container for episodes.
    """
    def __init__(self, title: str, *args):
        super().__init__(title)
        self._episodes = Chapter._validatedEpisodes(*args)
        self._priority = Action.DEF_PRIORITY

    def inherited(self, *epis):
        return Chapter(self.title, *epis).setPriority(self.priority)

    @property
    def episodes(self): return self._episodes

    @property
    def priority(self): return self._priority

    def setPriority(self, pri: int):
        # TODO: min max check
        self._priority = pri
        return self

    def omit(self):
        self._priority = Action.MIN_PRIORITY
        return self

    # privates
    def _validatedEpisodes(*args):
        for a in args:
            if not isinstance(a, Episode):
                raise AssertionError("Must be data type of 'Episode'!")
        return args

