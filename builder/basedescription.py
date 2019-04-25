# -*- coding: utf-8 -*-
"""Define base class for description.
"""
from . import assertion as ast
from . import enums as em
from . import sobject as so


class BaseDesc(so.SObject):
    """Base description class.

    Attributes:
        desc_type (:enum:`DescType`): a description type.
    """
    def __init__(self, desc_type: em.DescType):
        """
        Args:
            desc_type (:enum:`DescType`): a description type.
        """
        self.desc_type = ast.is_instance(desc_type, em.DescType)

