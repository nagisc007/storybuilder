# -*- coding: utf-8 -*-
"""Define enum types for storybuilder.
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

    def __str__(self) -> str:
        return {
                self.ACT.value: "ACT",
                self.EXPLAIN.value: "EXPLAIN",
                self.TAG.value: "TAG",
                self.TELL.value: "TELL",
                self.TEST.value: "TEST",
                }[self.value]


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

    def __str__(self) -> str:
        return {
                self.CAN.value: "CAN",
                self.MAY.value: "MAY",
                self.MUST.value: "MUST",
                self.NONE.value: "NONE",
                self.SHOULD.value: "SHOULD",
                self.THINK.value: "THINK",
                self.WANT.value: "WANT",
                self.WANT.value: "WILL",
                }[self.value]


class GroupType(Enum):
    """Action group type enum.
    """
    COMBI = auto()
    SCENE = auto()
    STORY = auto()

    def __str__(self) -> str:
        return {
                self.COMBI.value: "_COMBI",
                self.SCENE.value: "_SCENE",
                self.STORY.value: "_STORY",
                }[self.value]


class LangType(Enum):
    """Language type enum.
    """
    ENG = auto()
    JPN = auto()

    def __str__(self) -> str:
        return {
                self.ENG.value: "_ENG",
                self.JPN.value: "_JPN",
                }[self.value]


class TagType(Enum):
    """Tag type enum.
    """
    NONE = auto()
    TITLE = auto()
    BR = auto()
    COMMENT = auto()
    HR = auto()
    SYMBOL = auto()

    def __str__(self) -> str:
        return {
                self.BR.value: "_BR",
                self.COMMENT.value: "_COMMENT",
                self.HR.value: "_HR",
                self.NONE.value: "_NONE",
                self.TITLE.value: "_TITLE",
                self.SYMBOL.value: "_SYMBOL",
                }[self.value]

