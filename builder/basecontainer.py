# -*- coding: utf-8 -*-
"""Define base container type class.
"""
from . import assertion


class BaseContainer(object):
    """Base class for a container.
    """
    def __init__(self, title: str):
        self._title = assertion.is_str(title)

    @property
    def title(self): return self._title

