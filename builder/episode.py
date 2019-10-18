# -*- coding: utf-8 -*-
"""Define episode class.
"""
from . import assertion
from .basecontainer import BaseContainer
from .scene import Scene
from .action import Action


class Episode(BaseContainer):
    """The container for scenes.
    """
    def __init__(self, title: str, outline: str, *args):
        super().__init__(title)
        self._outline = assertion.is_str(outline)
        self._scenes = Episode._validatedScenes(*args)
        self._priority = Action.DEF_PRIORITY

    def inherited(self, *scs):
        return Episode(self.title, self.outline, *scs).setPriority(self.priority)

    @property
    def outline(self): return self._outline

    @property
    def scenes(self): return self._scenes

    @property
    def priority(self): return self._priority

    def setPriority(self, pri: int):
        # TODO: min max check
        self._priority = pri
        return self

    def omit(self):
        self._priority = Action.MIN_PRIORITY
        return self

    # private
    def _validatedScenes(*args):
        for a in args:
            if not isinstance(a, Scene):
                raise AssertionError("Must be data type of 'Scene'!")
        return args
