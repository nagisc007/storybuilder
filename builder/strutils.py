# -*- coding: utf-8 -*-
"""String utilities.
"""
import re
from .sbutils import assert_isclass, assert_isstr
from .enums import LangType


# public functions
def double_comma_chopped(target: str, lang: LangType=LangType.JPN) -> str:
    '''Single symbol from double

        、、｜。。 → 、｜。
    '''
    assert_isstr(target)
    assert_isclass(lang, LangType)

    if lang is LangType.JPN:
        return re.sub(r'([、。]){2}', r'\1', target)
    else:
        return re.sub(r'([,\.]){2}', r'\1', target)


def extraend_chopped(target: str, lang: LangType) -> str:
    '''Symbol mark with invalid endmark chopped
    '''
    assert_isstr(target)
    assert_isclass(lang, LangType)

    if lang is LangType.JPN:
        return re.sub(r'([！？])。$', r'\1', target)
    else:
        return re.sub(r'([!?])\. $', r'\1', target)


def extraspace_chopped(target: str, lang: LangType) -> str:
    '''Endmark with invalid space removed.
    '''
    assert_isstr(target)
    assert_isclass(lang, LangType)

    if lang is LangType.JPN:
        return re.sub(r'([。」])[　、](.)', r'\1\2', target)
    else:
        return re.sub(r' +', r' ', target)

