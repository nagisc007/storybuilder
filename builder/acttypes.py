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


class AuxVerb(Enum):
    """Auxiliary verb type enum.
    """
    NONE = auto()
    CAN = auto()
    MAY = auto()
    MUST = auto()
    SHOULD = auto()
    THINK = auto()
    WANT = auto()
    WILL = auto()


class GroupType(Enum):
    """Action group type enum.
    """
    COMBI = auto()
    SCENE = auto()
    STORY = auto()


class LangType(Enum):
    """Language type enum.
    """
    ENG = auto()
    JPN = auto()


class TagType(Enum):
    """Tag type enum.
    """
    NONE = auto()
    TITLE = auto()
    COMMENT = auto()
    HR = auto()


# functions
def auxverb_of(auxv: AuxVerb) -> str:
    return {
            AuxVerb.CAN: "can",
            AuxVerb.MAY: "may",
            AuxVerb.MUST: "must",
            AuxVerb.NONE: "",
            AuxVerb.SHOULD: "should",
            AuxVerb.THINK: "think",
            AuxVerb.WANT: "want",
            AuxVerb.WILL: "will",
            }[auxv]


def group_name_of(group: GroupType) -> str:
    return {
            GroupType.COMBI: "_group_combi",
            GroupType.SCENE: "_group_scene",
            GroupType.STORY: "_group_story",
            }[group]


def tag_str_of(tag: TagType) -> str:
    return {
            TagType.NONE: "_tag_nothing",
            TagType.COMMENT: "_tag_comment",
            TagType.HR: "_tag_hr",
            TagType.TITLE: "_tag_title",
            }[tag]

