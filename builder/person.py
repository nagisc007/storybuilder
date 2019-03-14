# -*- coding: utf-8 -*-
"""Person class deined.
"""
from .acttypes import ActType, Behavior
from .base import Act, BasePerson


class Person(BasePerson):
    """Character object created.

    Attributes:
    (inherited)
        act (action, behavior, withS): basic action attr.
        look (action, withS): looking description attr.
        tell (action, withS): dialogue attr.
        think (action, withS): subject's thought attr.
        must (action, withS): for episode purpose attr.
        want (action, withS): for episode reason attr.
        result (action, withS): for episode result attr.
    """
    def __init__(self, name, age, sex, job, selfcall="私", info="nothing"):
        super().__init__(name, age, sex, job, info)
        self.selfcall = selfcall

    # basic actions
    def acquire(self, action="手に入れる", withS=False):
        return Act(self, ActType.ACT, Behavior.ACQUIRE, action, withS)

    def catch(self, action="捕まえる", withS=False):
        return Act(self, ActType.ACT, Behavior.CATCH, action, withS)

    def close(self, action="閉める", withS=False):
        return Act(self, ActType.ACT, Behavior.CLOSE, action, withS)

    def come(self, action="来る", withS=False):
        return Act(self, ActType.ACT, Behavior.COME, action, withS)

    def feel(self, action="感じる", withS=False):
        return Act(self, ActType.THINK, Behavior.FEEL, action, withS)

    def go(self, action="行く", withS=False):
        return Act(self, ActType.ACT, Behavior.GO, action, withS)

    def hear(self, action="聞く", withS=False):
        return Act(self, ActType.ACT, Behavior.HEAR, action, withS)

    def move(self, action="動く", withS=False):
        return Act(self, ActType.ACT, Behavior.MOVE, action, withS)

    def open(self, action="開く", withS=False):
        return Act(self, ActType.ACT, Behavior.OPEN, action, withS)

    def punch(self, action="殴る", withS=False):
        return Act(self, ActType.ACT, Behavior.PUNCH, action, withS)

    def remember(self, action="思い出す", withS=False):
        return Act(self, ActType.THINK, Behavior.REMEMBER, action, withS)

    def reply(self, action="返事する", withS=False):
        return Act(self, ActType.ACT, Behavior.REPLY, action, withS)

    def see(self, action="見る", withS=False):
        return Act(self, ActType.ACT, Behavior.SEE, action, withS)

    def sleep(self, action="眠る", withS=False):
        return Act(self, ActType.ACT, Behavior.SLEEP, action, withS)

    def smell(self, action="匂う", withS=False):
        return Act(self, ActType.ACT, Behavior.SMELL, action, withS)

    def smile(self, action="微笑する", withS=False):
        return Act(self, ActType.ACT, Behavior.SMILE, action, withS)

    def speak(self, action="声を出す", withS=False):
        return Act(self, ActType.ACT, Behavior.SPEAK, action, withS)

    def release(self, action="解放する", withS=False):
        return Act(self, ActType.ACT, Behavior.RELEASE, action, withS)

    def talk(self, action="話す", withS=False):
        return Act(self, ActType.ACT, Behavior.TALK, action, withS)

    def wake(self, action="目覚める", withS=False):
        return Act(self, ActType.ACT, Behavior.WAKE, action, withS)

    # sub actions
    def agree(self, action="頷く", withS=False):
        return reply(action, withS)

    def ask(self, action="尋ねる", withS=False):
        return hear(action, withS)

    def brow(self, action="眉を顰める", withS=False):
        return feel(action, withS)

    def call(self, action="呼ぶ", withS=False):
        return speak(action, withS)

    def check(self, action="確認する", withS=False):
        return hear(action, withS)

    def confuse(self, action="困惑する", withS=False):
        return feel(action, withS)

    def explain(self, action="説明する", withS=False):
        return talk(action, withS)

    def gaze(self, action="見つめる", withS=False):
        return see(action, withS)

    def growl(self, action="唸る", withS=False):
        return speak(action, withS)

    def maon(self, action="呻く", withS=False):
        return speak(action, withS)

    def oppose(self, action="反対する", withS=False):
        return reply(action, withS)

    def surprise(self, action="驚く", withS=False):
        return feel(action, withS)

    def stare(self, action="睨む", withS=False):
        return see(action, withS)

    def take(self, action="連れて行く", withS=False):
        return go(action, withS)

    def visit(self, action="訪れる", withS=False):
        return go(action, withS)

