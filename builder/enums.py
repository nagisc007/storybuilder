# -*- coding: utf-8 -*-
"""Define enum types for storybuilder.
"""
from enum import Enum, auto


class ActType(Enum):
    """Action types.
    """
    BE = auto() # state type
    BEHAV = auto() # behavior type
    DEAL = auto() # deal type
    DO = auto() # general act type
    EXPLAIN = auto() # information type
    FEEL = auto() # feel type
    GROUP = auto() # for groups
    LOOK = auto() # look type
    MOVE = auto() # move type
    NONE = auto() # none type
    TAG = auto() # for tags
    TALK = auto() # talk type
    TEST = auto() # test type
    THINK = auto() # thinking type

    def __str__(self) -> str:
        return {
                self.BE.value: "BE",
                self.BEHAV.value: "BEHAV",
                self.DEAL.value: "DEAL",
                self.DO.value: "DO",
                self.EXPLAIN.value: "EXPLAIN",
                self.FEEL.value: "FEEL",
                self.GROUP.value: "GROUP",
                self.LOOK.value: "LOOK",
                self.MOVE.value: "MOVE",
                self.NONE.value: "NONE",
                self.TAG.value: "TAG",
                self.TALK.value: "TALK",
                self.TEST.value: "TEST",
                self.THINK.value: "THINK",
                }[self.value]


class AuxVerb(Enum):
    """Auxiliary verb types.
    """
    CAN = auto()
    MAY = auto()
    MUST = auto()
    NONE = auto()
    SHOULD = auto()
    WANT = auto()
    WILL = auto()

    def __str__(self) -> str:
        return {
                self.CAN.value: "CAN",
                self.MAY.value: "MAY",
                self.MUST.value: "MUST",
                self.NONE.value: "NONE",
                self.SHOULD.value: "SHOULD",
                self.WANT.value: "WANT",
                self.WILL.value: "WILL",
                }[self.value]

    def tags() -> tuple:
        return (
                "$can",
                "$may",
                "$must",
                "$should",
                "$want",
                "$will",
                )


class DescType(Enum):
    """Description type enum.
    """
    DESCRIPTION = auto()
    DIALOGUE = auto()
    NONE = auto()
    TAG = auto()

    def __str__(self) -> str:
        return {
                self.DESCRIPTION.value: "DESCRIPTION",
                self.DIALOGUE.value: "DIALOGUE",
                self.NONE.value: "NONE",
                self.TAG.value: "TAG",
                }[self.value]


class GroupType(Enum):
    """Action group type enum.
    """
    COMBI = auto()
    NONE = auto()
    SCENE = auto()

    def __str__(self) -> str:
        return {
                self.COMBI.value: "COMBI",
                self.NONE.value: "NONE",
                self.SCENE.value: "SCENE",
                }[self.value]


class LangType(Enum):
    """Language type enum.
    """
    ENG = auto()
    JPN = auto()
    NONE = auto()

    def __str__(self) -> str:
        return {
                self.ENG.value: "ENG",
                self.JPN.value: "JPN",
                self.NONE.value: "NONE",
                }[self.value]


class TagType(Enum):
    """Tag type enum.
    """
    BR = auto()
    COMMENT = auto()
    HEAD1 = auto()
    HEAD2 = auto()
    HEAD3 = auto()
    HR = auto()
    NONE = auto()
    SYMBOL = auto()

    def __str__(self) -> str:
        return {
                self.BR.value: "BR",
                self.COMMENT.value: "COMMENT",
                self.HEAD1.value: "HEAD1",
                self.HEAD2.value: "HEAD2",
                self.HEAD3.value: "HEAD3",
                self.HR.value: "HR",
                self.NONE.value: "NONE",
                self.SYMBOL.value: "SYMBOL",
                }[self.value]

