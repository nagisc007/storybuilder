# -*- coding: utf-8 -*-
"""Define enum types for action object.
"""
from enum import Enum, auto


class ActType(Enum):
    """Act type enum.
    """
    ACT = auto() # general type
    EXPLAIN = auto() # information type
    TAG = auto() # structure type
    TELL = auto() # dialogue type
    TEST = auto() # test type


class TagType(Enum):
    """Tag type enum.
    """
    NONE = auto()
    TITLE = auto()
    COMMENT = auto()
    HR = auto()


def tag_str_of(tag: TagType) -> str:
    return {
            TagType.NONE: "_tag_nothing",
            TagType.COMMENT: "_tag_comment",
            TagType.HR: "_tag_hr",
            TagType.TITLE: "_tag_title",
            }[tag]


class LangType(Enum):
    """Language type enum.
    """
    ENG = auto()
    JPN = auto()

