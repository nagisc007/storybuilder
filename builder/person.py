# -*- coding: utf-8 -*-
"""Person class deined.
"""
from .acttypes import Behavior
from .acttypes import behavior_str_of
from .base import _BasePerson


class Person(_BasePerson):
    """Character class.

    Attributes:
        selfcall (str, optioanl): a subject called himself.
    """
    def __init__(self, name:str, age: int, sex: str, job: str, selfcall: str="私", note: str="nothing"):
        super().__init__(name, age, sex, job, note)
        self.selfcall = selfcall

    # basic actions
    def acquire(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.ACQUIRE, behavior_str_of(Behavior.ACQUIRE), note)

    def agree(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.AGREE, behavior_str_of(Behavior.AGREE), note)

    def angry(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.ANGRY, behavior_str_of(Behavior.ANGRY), note)

    def ask(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.ASK, behavior_str_of(Behavior.ASK), note)

    def believe(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.BELIEVE, behavior_str_of(Behavior.BELIEVE), note)

    def brow(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.BROW, behavior_str_of(Behavior.BROW), note)

    def call(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.CALL, behavior_str_of(Behavior.CALL), note)

    def catch(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.CATCH, behavior_str_of(Behavior.CATCH), note)

    def check(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.CHECK, behavior_str_of(Behavior.CHECK), note)

    def click(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.CLICK, behavior_str_of(Behavior.CLICK), note)

    def close(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.CLOSE, behavior_str_of(Behavior.CLOSE), note)

    def come(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.COME, behavior_str_of(Behavior.COME), note)
    
    def confess(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.CONFESS, behavior_str_of(Behavior.CONFESS), note)

    def confuse(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.CONFUSE, behavior_str_of(Behavior.CONFUSE), note)

    def contact(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.CONTACT, behavior_str_of(Behavior.CONTACT), note)

    def create(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.CREATE, behavior_str_of(Behavior.CREATE), note)

    def deal(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.DEAL, behavior_str_of(Behavior.DEAL), note)

    def dispel(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.DISPEL, behavior_str_of(Behavior.DISPEL), note)

    def do(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.DO, behavior_str_of(Behavior.DO), note)

    def email(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.EMAIL, behavior_str_of(Behavior.EMAIL), note)

    def enter(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.ENTER, behavior_str_of(Behavior.ENTER), note)

    def envy(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.ENVY, behavior_str_of(Behavior.ENVY), note)

    def equip(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.EQUIP, behavior_str_of(Behavior.EQUIP), note)

    def face(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.FACE, behavior_str_of(Behavior.FACE), note)

    def fall(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.FALL, behavior_str_of(Behavior.FALL), note)
    def feel(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.FEEL, behavior_str_of(Behavior.FEEL), note)

    def fib(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.FIB, behavior_str_of(Behavior.FIB), note)

    def find(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.FIND, behavior_str_of(Behavior.FIND), note)

    def finish(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.FINISH, behavior_str_of(Behavior.FINISH), note)

    def fire(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.FIRE, behavior_str_of(Behavior.FIRE), note)

    def firejob(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.FIREJOB, behavior_str_of(Behavior.FIREJOB, note))

    def gaze(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.GAZE, behavior_str_of(Behavior.GAZE), note)

    def go(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.GO, behavior_str_of(Behavior.GO), note)

    def growl(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.GROWL, behavior_str_of(Behavior.GROWL), note)

    def handle(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.HANDLE, behavior_str_of(Behavior.HANDLE), note)

    def hear(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.HEAR, behavior_str_of(Behavior.HEAR), note)

    def keyboard(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.KEYBOARD, behavior_str_of(Behavior.KEYBOARD), note)

    def kick(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.KICK, behavior_str_of(Behavior.KICK), note)

    def kill(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.KILL, behavior_str_of(Behavior.KILL), note)

    def knock(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.KNOCK, behavior_str_of(Behavior.KNOCK), note)

    def know(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.KNOW, behavior_str_of(Behavior.KNOW), note)

    def laugh(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.LAUGH, behavior_str_of(Behavior.LAUGH), note)

    def learn(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.LEARN, behavior_str_of(Behavior.LEARN), note)

    def leave(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.LEAVE, behavior_str_of(Behavior.LEAVE), note)

    def let(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.LET, behavior_str_of(Behavior.LET), note)

    def life(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.LIFE, behavior_str_of(Behavior.LIFE), note)

    def live(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.LIVE, behavior_str_of(Behavior.LIVE), note)

    def lose(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.LOSE, behavior_str_of(Behavior.LOSE), note)

    def love(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.LOVE, behavior_str_of(Behavior.LOVE), note)
    
    def makeup(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.MAKEUP, behavior_str_of(Behavior.MAKEUP), note)

    def maon(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.MAON, behavior_str_of(Behavior.MAON), note)

    def marry(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.MARRY, behavior_str_of(Behavior.MARRY), note)

    def meet(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.MEET, behavior_str_of(Behavior.MEET), note)

    def melt(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.MELT, behavior_str_of(Behavior.MELT), note)

    def move(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.MOVE, behavior_str_of(Behavior.MOVE), note)

    def must(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.MUST, behavior_str_of(Behavior.MUST), note)

    def open(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.OPEN, behavior_str_of(Behavior.OPEN), note)

    def oppose(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.OPPOSE, behavior_str_of(Behavior.OPPOSE), note)

    def phone(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.PHONE, behavior_str_of(Behavior.PHONE), note)

    def punch(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.PUNCH, behavior_str_of(Behavior.PUNCH), note)

    def puzzle(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.PUZZLE, behavior_str_of(Behavior.PUZZLE), note)

    def react(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.REACT, behavior_str_of(Behavior.REACT), note)

    def remember(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.REMEMBER, behavior_str_of(Behavior.REMEMBER), note)

    def reply(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.REPLY, behavior_str_of(Behavior.REPLY), note)

    def release(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.RELEASE, behavior_str_of(Behavior.RELEASE), note)

    def search(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.SEARCH, behavior_str_of(Behavior.SEARCH), note)

    def see(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.SEE, behavior_str_of(Behavior.SEE), note)

    def sleep(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.SLEEP, behavior_str_of(Behavior.SLEEP), note)

    def smell(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.SMELL, behavior_str_of(Behavior.SMELL), note)

    def smile(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.SMILE, behavior_str_of(Behavior.SMILE), note)

    def smoke(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.SMOKE, behavior_str_of(Behavior.SMOKE), note)

    def speak(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.SPEAK, behavior_str_of(Behavior.SPEAK), note)

    def stare(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.STARE, behavior_str_of(Behavior.STARE), note)

    def surprise(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.SURPRISE, behavior_str_of(Behavior.SURPRISE), note)

    def sword(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.SWORD, behavior_str_of(Behavior.SWORD), note)

    def take(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.TAKE, behavior_str_of(Behavior.TAKE), note)

    def talk(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.TALK, behavior_str_of(Behavior.TALK), note)

    def visit(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.VISIT, behavior_str_of(Behavior.VISIT), note)

    def wait(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.WAIT, behavior_str_of(Behavior.WAIT), note)

    def wake(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.WAKE, behavior_str_of(Behavior.WAKE), note)

    def want(self, action: str, note: str="nothing"):
        return self.act(action, Behavior.WANT, behavior_str_of(Behavior.WANT), note)

