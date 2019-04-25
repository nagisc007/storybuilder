# -*- coding: utf-8 -*-
"""Define basic object for story builder.
"""
from . import assertion as ast


class SObject(object):
    """Base object class for story.

    Note:
        all object must be inherited this.
        because this implements a useful equal features.
    """
    def __eq__(self, other) -> bool:
        if other is None or type(self) != type(other):
            return False
        else:
            return self.__dict__ == other.__dict__

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
