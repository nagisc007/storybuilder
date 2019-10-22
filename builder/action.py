# -*- coding: utf-8 -*-
"""Define action class.
"""
from enum import Enum
from . import assertion
from .basedata import BaseData
from .description import Description, NoDesc, DescType
from .flag import Flag, NoFlag, NoDeflag
from .basesubject import NoSubject
from .person import Person
from .chara import Chara
from .who import Who


class ActType(Enum):
    """Action type.
    """
    ACT = "act" # 全般
    MOVE = "move" # 動かす
    COME = "come" # 出現
    GO = "go" # 消去
    LOOK = "look" # 描画
    BE = "be" # 外部状態
    THINK = "think" # 内部状態
    HAVE = "have" # 所有変更
    HEAR = "hear" # 効果音などの音声
    TALK = "talk" # 台詞


class Action(BaseData):
    """Data type of an action.
    """
    DEF_PRIORITY = 5
    MAX_PRIORITY = 10
    MIN_PRIORITY = 0

    def __init__(self, subject: [Person, Chara, None],
            outline: str="", act_type: ActType=ActType.ACT):
        super().__init__("__action__")
        _subject_is_str = isinstance(subject, str)
        # TODO: subjectが文字列だったらsubjectにはWhoを入れてそのままoutlineにスライドさせる
        self._subject = Who() if _subject_is_str else Action._validatedSubject(subject)
        self._outline = assertion.is_str(subject if _subject_is_str else outline)
        self._act_type = assertion.is_instance(act_type, ActType)
        self._description = NoDesc()
        self._flag = NoFlag()
        self._deflag = NoDeflag()
        self._priority = Action.DEF_PRIORITY

    def inherited(self, subject=None, outline=None, desc=None):
        return Action(subject if subject else self.subject,
                outline if outline else self.outline,
                self.act_type) \
                    .flag(self.getFlag()).deflag(self.getDeflag()) \
                    ._setDescription(desc if desc else self.description,
                            self.description.desc_type) \
                    .setPriority(self.priority)

    @property
    def act_type(self): return self._act_type

    @property
    def subject(self): return self._subject

    @property
    def outline(self): return self._outline

    @property
    def description(self): return self._description

    @property
    def priority(self): return self._priority

    def setPriority(self, pri: int):
        self._priority = pri
        return self

    def flag(self, val: [str, NoFlag]):
        self._flag = NoFlag() if isinstance(val, NoFlag) else assertion.is_str(val)
        return self

    def deflag(self, val: [str, NoDeflag]):
        self._deflag = NoDeflag() if isinstance(val, NoDeflag) else assertion.is_str(val)
        return self

    def getFlag(self): return self._flag

    def getDeflag(self): return self._deflag

    def omit(self):
        self._priority = Action.MIN_PRIORITY
        return self

    # methods
    def desc(self, *args):
        self._description = Description(*args, desc_type=DescType.DESC)
        return self

    def d(self, *args): return self.desc(*args)

    def tell(self, *args):
        self._description = Description(*args, desc_type=DescType.DIALOGUE)
        return self

    def t(self, *args): return self.tell(*args)

    def comp(self, *args):
        self._description = Description(*args, desc_type=DescType.COMPLEX)
        return self

    def same(self, desc_type: str='d'):
        if desc_type in ('t', 'tell'):
            self.tell(self.outline)
        elif desc_type in ('c', 'comp'):
            self.comp(self.outline)
        else:
            self.desc(self.outline)
        return self

    # private
    def _validatedSubject(sub: [str, Person, Chara, None]):
        if isinstance(sub, str):
            return Who()
        elif isinstance(sub, (Person, Chara)):
            return sub
        else:
            return NoSubject()

    def _setDescription(self, descs, desc_type: DescType):
        if isinstance(descs, Description):
            self._description = descs
        else:
            self._description = Description(*descs,
                    desc_type=desc_type)
        return self

