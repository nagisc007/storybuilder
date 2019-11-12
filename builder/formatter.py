# -*- coding: utf-8 -*-
"""For format class.
"""
from . import assertion


class Formatter(object):
    """The output format tools.
    """

    # methods
    def asOutline(self, data: list):
        tmp = []
        for v in data:
            if "###" in v[0]:
                tmp.append(f"{v[0]}\n\n\t{v[1]}")
            elif "#" in v[0]:
                tmp.append(f"{v[0]}")
            else:
                tmp.append(f"- 「{v[0]}」: {v[1]}")
        return tmp
