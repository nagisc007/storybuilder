# -*- coding: utf-8 -*-
"""Define descriptions.
"""
from . import assertion as ast
from . import basedescription as bd
from . import enums as em


class Desc(bd.BaseDesc):
    """Description class.

    Attributes:
        desc_type (:enum:`DescType`): a description type.
        data (:tuple:str): description data.
    """
    def __init__(self, *args, desc_type: em.DescType=em.DescType.DESCRIPTION):
        """
        Args:
            *args ([str, tuple]): description strings.
            desc_type (:enum:`DescType`, optional): a description type.
        """
        from . import parser
        super().__init__(desc_type)
        self.data = parser.str_to_tuple_from_args(args)


class DescGroup(bd.BaseDesc):
    """Description group class.

    Attributes:
        desc_type (:enum:`DescType`): a group type.
        descriptions (:tuple:`Desc`): descriptions.
    """
    def __init__(self, *args: bd.BaseDesc, base_type: em.DescType=em.DescType.DESCRIPTION):
        """
        Args:
            *args (:obj:`BaseDesc`): descriptions in this container.
            base_type (:enum:`DescType`): a basic type for this container.
        """
        super().__init__(base_type)
        self.descriptions = args # TODO: check and build data


class NoDesc(bd.BaseDesc):
    """Specific description that have nothing.
    """
    def __init__(self):
        super().__init__(em.DescType.NONE)
