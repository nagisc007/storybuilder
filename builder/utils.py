# -*- coding: utf-8 -*-
"""Common utilities.
"""
from typing import Any
from . import assertion as ast


# public methods
def val_ifNone_default(val: Any, defval: Any) -> Any:
    return val if not val is None else defval


def int_ceiled(a: [int, float], b: [int, float]) -> int:
    return -(-a // b)
