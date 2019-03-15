# -*- coding: utf-8 -*-
"""Person class deined.
"""
from .acttypes import ActType, Behavior
from .base import Act, BasePerson


class Person(BasePerson):
    """Character object created.

    Attributes:
        selfcall (str, optioanl): a subject called himself.
    """
    def __init__(self, name, age, sex, job, selfcall="私", note="nothing"):
        super().__init__(name, age, sex, job, note)
        self.selfcall = selfcall

    # basic actions
    def deal(self, action, act_word="扱う"):
        return Act(self, ActType.ACT, Behavior.DEAL, action, act_word)

    def do(self, action, act_word="行う"):
        return Act(self, ActType.ACT, Behavior.DO, action, act_word)

    def feel(self, action, act_word="感じる"):
        return Act(self, ActType.ACT, Behavior.FEEL, action, act_word)

    def handle(self, action, act_word="操作する"):
        return Act(self, ActType.ACT, Behavior.HANDLE, action, act_word)

    def hear(self, action, act_word="聞く"):
        return Act(self, ActType.ACT, Behavior.HEAR, action, act_word)

    def move(self, action, act_word="動く"):
        return Act(self, ActType.ACT, Behavior.MOVE, action, act_word)

    def react(self, action, act_word="反応する"):
        return Act(self, ActType.ACT, Behavior.REACT, action, act_word)

    def see(self, action, act_word="見る"):
        return Act(self, ActType.ACT, Behavior.SEE, action, act_word)

    def talk(self, action, act_word="話す"):
        return Act(self, ActType.ACT, Behavior.TALK, action, act_word)

    # sub actions
    def acquire(self, action): return self.deal(action, "手に入れる")

    def agree(self, action): return self.react(action, "頷く")

    def ask(self, action): return self.hear(action, "尋ねる")

    def brow(self, action): return self.feel(action, "眉を顰める")

    def call(self, action): return self.talk(action, "呼ぶ")

    def catch(self, action): return self.deal(action, "捕まえる")

    def check(self, action): return self.deal(action, "確認する")

    def close(self, action): return self.handle(action, "閉める")

    def come(self, action): return self.move(action, "来る")

    def confuse(self, action): return self.feel(action, "困惑する")

    def explain(self, action): return self.talk(action, "説明する")

    def gaze(self, action): return self.see(action, "見つめる")

    def go(self, action): return self.move(action, "行く")

    def growl(self, action): return self.feel(action, "唸る")

    def maon(self, action): return self.feel(action, "呻く")

    def open(self, action): return self.handle(action, "開く")

    def oppose(self, action): return self.react(action, "反対する")

    def punch(self, action): return self.handle(action, "殴る")

    def remember(self, action): return self.think(action, "思い出す")

    def reply(self, action): return self.react(action, "返事する")

    def release(self, action): return self.deal(action, "解放する")

    def sleep(self, action): return self.do(action, "眠る")

    def smell(self, action): return self.deal(action, "匂う")

    def smile(self, action): return self.feel(action, "微笑する")

    def speak(self, action): return self.talk(action, "声を出す")

    def stare(self, action): return self.see(action, "睨む")

    def surprise(self, action): return self.react(action, "驚く")

    def take(self, action): return self.move(action, "連れて行く")

    def visit(self, action): return self.move(action, "訪れる")

    def wake(self, action): return self.do(action, "目覚める")
