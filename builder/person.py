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
    def acquire(self, action, act_word="手に入れる", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.ACQUIRE, action, act_word, with_act, with_sub)

    def catch(self, action, act_word="捕まえる", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.CATCH, action, act_word, with_act, with_sub)

    def close(self, action, act_word="閉める", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.CLOSE, action, act_word, with_act, with_sub)

    def come(self, action, act_word="来る", withAct=True, withS=False):
        return Act(self, ActType.ACT, Behavior.COME, action, act_word, with_act, with_sub)

    def feel(self, action, act_word="感じる", withAct=True, withS=False):
        return Act(self, ActType.THINK, Behavior.FEEL, action, act_word, with_act, with_sub)

    def go(self, action, act_word="行く", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.GO, action, act_word, with_act, with_sub)

    def hear(self, action, act_word="聞く", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.HEAR, action, act_word, with_act, with_sub)

    def move(self, action, act_word="動く", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.MOVE, action, act_word, with_act, with_sub)

    def open(self, action, act_word="開く", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.OPEN, action, act_word, with_act, with_sub)

    def punch(self, action, act_word="殴る", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.PUNCH, action, act_word, with_act, with_sub)

    def remember(self, action, act_word="思い出す", with_act=True, with_sub=False):
        return Act(self, ActType.THINK, Behavior.REMEMBER, action, act_word, with_act, with_sub)

    def reply(self, action, act_word="返事する", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.REPLY, action, act_word, with_act, with_sub)

    def see(self, action, act_word="見る", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.SEE, action, act_word, with_act, with_sub)

    def sleep(self, action, act_word="眠る", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.SLEEP, action, act_word, with_act, with_sub)

    def smell(self, action, act_word="匂う", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.SMELL, action, act_word, with_act, with_sub)

    def smile(self, action, act_word="微笑する", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.SMILE, action, act_word, with_act, with_sub)

    def speak(self, action, act_word="声を出す", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.SPEAK, action, act_word, with_act, with_sub)

    def release(self, action, act_word="解放する", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.RELEASE, action, act_word, with_act, with_sub)

    def talk(self, action, act_word="話す", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.TALK, action, withS)

    def wake(self, action, act_word="目覚める", with_act=True, with_sub=False):
        return Act(self, ActType.ACT, Behavior.WAKE, action, act_word, with_act, with_sub)

    # sub actions
    def agree(self, action, act_word="頷く", with_act=True, with_sub=False):
        return reply(action, act_word, with_act, with_sub)

    def ask(self, action, act_word="尋ねる", with_act=True, with_sub=False):
        return hear(action, act_word, with_act, with_sub)

    def brow(self, action, act_word="眉を顰める", with_act=True, with_sub=False):
        return feel(action, act_word, with_act, with_sub)

    def call(self, action, act_word="呼ぶ", with_act=True, with_sub=False):
        return speak(action, act_word, with_act, with_sub)

    def check(self, action, act_word="確認する", with_act=True, with_sub=False):
        return hear(action, act_word, with_act, with_sub)

    def confuse(self, action, act_word="困惑する", with_act=True, with_sub=False):
        return feel(action, act_word, with_act, with_sub)

    def explain(self, action, act_word="説明する", with_act=True, with_sub=False):
        return talk(action, act_word, with_act, with_sub)

    def gaze(self, action, act_word="見つめる", with_act=True, with_sub=False):
        return see(action, act_word, with_act, with_sub)

    def growl(self, action, act_word="唸る", with_act=True, with_sub=False):
        return speak(action, act_word, with_act, with_sub)

    def maon(self, action, act_word="呻く", with_act=True, with_sub=False):
        return speak(action, act_word, with_act, with_sub)

    def oppose(self, action, act_word="反対する", with_act=True, with_sub=False):
        return reply(action, act_word, with_act, with_sub)

    def surprise(self, action, act_word="驚く", with_act=True, with_sub=False):
        return feel(action, act_word, with_act, with_sub)

    def stare(self, action, act_word="睨む", with_act=True, with_sub=False):
        return see(action, act_word, with_act, with_sub)

    def take(self, action, act_word="連れて行く", with_act=True, with_sub=False):
        return go(action, act_word, with_act, with_sub)

    def visit(self, action, act_word="訪れる", with_act=True, with_sub=False):
        return go(action, act_word, with_act, with_sub)

