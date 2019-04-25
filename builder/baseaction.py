# -*- coding: utf-8 -*-
"""Define basic action class.
"""
from . import assertion as ast
from . import sobject as so
from . import enums as em


class BaseAction(so.SObject):
    """Base action class.

    Attributes:
        act_type (:enum:`ActType`): a type of action.
    """
    def __init__(self, act_type: em.ActType):
        """
        Args:
            act_type (:enum:`ActType`): a type of action.
        """
        self.act_type = ast.is_instance(act_type, em.ActType)

