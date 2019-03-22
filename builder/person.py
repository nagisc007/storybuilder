# -*- coding: utf-8 -*-
"""Person class deined.
"""
from .base import _BaseSubject, _BasePerson
from .behavior import Behavior
from .behavior import behavior_str_of


class Person(_BasePerson):
    """Character class.

    Attributes:
        selfcall (str, optioanl): a subject called himself.
    """
    def __init__(self, name:str, age: int, sex: str, job: str, selfcall: str="私", note: str="nothing"):
        super().__init__(name, age, sex, job, note)
        self.selfcall = selfcall

    DEF_ACT = "-"
    DEF_NOTE = "nothing"

    # basic actions
    def accept(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ACCEPT, obj, behavior_str_of(Behavior.ACCEPT), note)

    def acquire(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ACQUIRE, obj, behavior_str_of(Behavior.ACQUIRE), note)

    def add(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ADD, obj, behavior_str_of(Behavior.ADD), note)

    def advise(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ADVISE, obj, behavior_str_of(Behavior.ADVISE), note)

    def agree(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.AGREE, obj, behavior_str_of(Behavior.AGREE), note)

    def aim(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.AIM, obj, behavior_str_of(Behavior.AIM), note)

    def angry(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ANGRY, obj, behavior_str_of(Behavior.ANGRY), note)

    def answer(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ANSWER, obj, behavior_str_of(Behavior.ANSWER), note)

    def appear(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.APPEAR, obj, behavior_str_of(Behavior.APPEAR), note)

    def apply(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.APPLY, obj, behavior_str_of(Behavior.APPLY), note)

    def arrive(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ARRIVE, obj, behavior_str_of(Behavior.ARRIVE), note)

    def ask(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ASK, obj, behavior_str_of(Behavior.ASK), note)

    def attack(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ATTACK, obj, behavior_str_of(Behavior.ATTACK), note)

    def be(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BE, obj, behavior_str_of(Behavior.BE), note)

    def become(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BECOME, obj, behavior_str_of(Behavior.BECOME), note)

    def begin(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BEGIN, obj, behavior_str_of(Behavior.BEGIN), note)

    def believe(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BELIEVE, obj, behavior_str_of(Behavior.BELIEVE), note)

    def bet(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BET, obj, behavior_str_of(Behavior.BET), note)

    def bind(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BIND, obj, behavior_str_of(Behavior.BIND), note)

    def borrow(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BORROW, obj, behavior_str_of(Behavior.BORROW), note)

    def breaks(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BREAK, obj, behavior_str_of(Behavior.BREAK), note)

    def breathe(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BREATHE, obj, behavior_str_of(Behavior.BREATHE), note)

    def brow(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BROW, obj, behavior_str_of(Behavior.BROW), note)

    def build(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BUILD, obj, behavior_str_of(Behavior.BUILD), note)

    def burn(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BURN, obj, behavior_str_of(Behavior.BURN), note)

    def burst(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BURST, obj, behavior_str_of(Behavior.BURST), note)

    def bury(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BURY, obj, behavior_str_of(Behavior.BURY), note)

    def buy(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.BUY, obj, behavior_str_of(Behavior.BUY), note)

    def calculate(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CALCULATE, obj, behavior_str_of(Behavior.CALCULATE), note)

    def call(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CALL, obj, behavior_str_of(Behavior.CALL), note)

    def care(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CARE, obj, behavior_str_of(Behavior.CARE), note)

    def carry(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CARRY, obj, behavior_str_of(Behavior.CARRY), note)

    def catch(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CATCH, obj, behavior_str_of(Behavior.CATCH), note)

    def change(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CHANGE, obj, behavior_str_of(Behavior.CHANGE), note)

    def charm(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CHARM, obj, behavior_str_of(Behavior.CHARM), note)

    def check(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CHECK, obj, behavior_str_of(Behavior.CHECK), note)

    def cheer(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CHEER, obj, behavior_str_of(Behavior.CHEER), note)

    def choose(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CHOOSE, obj, behavior_str_of(Behavior.CHOOSE), note)

    def clean(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CLEAN, obj, behavior_str_of(Behavior.CLEAN), note)

    def click(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CLICK, obj, behavior_str_of(Behavior.CLICK), note)

    def climb(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CLIMB, obj, behavior_str_of(Behavior.CLIMB), note)

    def close(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CLOSE, obj, behavior_str_of(Behavior.CLOSE), note)

    def clothe(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CLOTHE, obj, behavior_str_of(Behavior.CLOTHE), note)

    def coach(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.COACH, obj, behavior_str_of(Behavior.COACH), note)

    def come(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.COME, obj, behavior_str_of(Behavior.COME), note)
    
    def command(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.COMMAND, obj, behavior_str_of(Behavior.COMMAND), note)

    def compare(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.COMPARE, obj, behavior_str_of(Behavior.COMPARE), note)

    def complete(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.COMPLETE, obj, behavior_str_of(Behavior.COMPLETE), note)

    def confess(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CONFESS, obj, behavior_str_of(Behavior.CONFESS), note)

    def confuse(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CONFUSE, obj, behavior_str_of(Behavior.CONFUSE), note)

    def contact(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CONTACT, obj, behavior_str_of(Behavior.CONTACT), note)

    def continues(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CONTINUE, obj, behavior_str_of(Behavior.CONTINUE), note)

    def cooperate(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.COOPERATE, obj, behavior_str_of(Behavior.COOPERATE), note)

    def cough(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.COUGH, obj, behavior_str_of(Behavior.COUGH), note)

    def cook(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.COOK, obj, behavior_str_of(Behavior.COOK), note)

    def create(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CREATE, obj, behavior_str_of(Behavior.CREATE), note)

    def cry(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CRY, obj, behavior_str_of(Behavior.CRY), note)

    def cut(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.CUT, obj, behavior_str_of(Behavior.CUT), note)

    def dance(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DANCE, obj, behavior_str_of(Behavior.DANCE), note)

    def deal(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DEAL, obj, behavior_str_of(Behavior.DEAL), note)

    def define(self ,action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DEFINE, obj, behavior_str_of(Behavior.DEFINE), note)

    def die(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DIE, obj, behavior_str_of(Behavior.DIE), note)

    def dig(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DIG, obj, behavior_str_of(Behavior.DIG), note)

    def disappear(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DISAPPEAR, obj, behavior_str_of(Behavior.DISAPPEAR), note)

    def disapprove(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DISAPPROVE, obj, behavior_str_of(Behavior.DISAPPROVE), note)

    def dislike(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DISLIKE, obj, behavior_str_of(Behavior.DISLIKE), note)

    def dispel(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DISPEL, obj, behavior_str_of(Behavior.DISPEL), note)

    def display(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DISPLAY, obj, behavior_str_of(Behavior.DISPLAY), note)

    def dive(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DIVE, obj, behavior_str_of(Behavior.DIVE), note)

    def do(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DO, obj, behavior_str_of(Behavior.DO), note)

    def doubt(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DOUBT, obj, behavior_str_of(Behavior.DOUBT), note)

    def draw(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DRAW, obj, behavior_str_of(Behavior.DRAW), note)

    def dream(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DREAM, obj, behavior_str_of(Behavior.DREAM), note)

    def dress(self ,action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DRESS, obj, behavior_str_of(Behavior.DRESS), note)

    def drink(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DRINK, obj, behavior_str_of(Behavior.DRINK), note)

    def drive(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DRIVE, obj, behavior_str_of(Behavior.DRIVE), note)

    def drop(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DROP, obj, behavior_str_of(Behavior.DROP), note)

    def dry(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.DRY, obj, behavior_str_of(Behavior.DRY), note)

    def earn(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.EARN, obj, behavior_str_of(Behavior.EARN), note)

    def eat(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.EAT, obj, behavior_str_of(Behavior.EAT), note)

    def educate(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.EDUCATE, obj, behavior_str_of(Behavior.EDUCATE), note)

    def email(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.EMAIL, obj, behavior_str_of(Behavior.EMAIL), note)

    def employ(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.EMPLOY, obj, behavior_str_of(Behavior.EMPLOY), note)

    def engage(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ENGAGE, obj, behavior_str_of(Behavior.ENGAGE), note)

    def enjoy(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ENJOY, obj, behavior_str_of(Behavior.ENJOY), note)

    def enter(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ENTER, obj, behavior_str_of(Behavior.ENTER), note)

    def envy(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ENVY, obj, behavior_str_of(Behavior.ENVY), note)

    def equip(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.EQUIP, obj, behavior_str_of(Behavior.EQUIP), note)

    def exchange(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.EXCHANGE, obj, behavior_str_of(Behavior.EXCHANGE), note)

    def examine(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.EXAMINE, obj, behavior_str_of(Behavior.EXAMINE), note)

    def excite(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.EXCITE, obj, behavior_str_of(Behavior.EXCITE), note)

    def explore(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.EXPLORE, obj, behavior_str_of(Behavior.EXPLORE), note)

    def face(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FACE, obj, behavior_str_of(Behavior.FACE), note)

    def fail(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FAIL, obj, behavior_str_of(Behavior.FAIL), note)

    def fall(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FALL, obj, behavior_str_of(Behavior.FALL), note)

    def feel(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FEEL, obj, behavior_str_of(Behavior.FEEL), note)

    def fib(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FIB, obj, behavior_str_of(Behavior.FIB), note)

    def find(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FIND, obj, behavior_str_of(Behavior.FIND), note)

    def fight(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FIGHT, obj, behavior_str_of(Behavior.FIGHT), note)

    def fill(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FILL, obj, behavior_str_of(Behavior.FILL), note)

    def finish(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FINISH, obj, behavior_str_of(Behavior.FINISH), note)

    def fire(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FIRE, obj, behavior_str_of(Behavior.FIRE), note)

    def firejob(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FIREJOB, obj, behavior_str_of(Behavior.FIREJOB, note))

    def flash(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FLASH, obj, behavior_str_of(Behavior.FLASH), note)

    def float(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FLOAT, obj, behavior_str_of(Behavior.FLOAT), note)

    def fly(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FLY, obj, behavior_str_of(Behavior.FLY), note)

    def follow(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FOLLOW, obj, behavior_str_of(Behavior.FOLLOW), note)

    def forget(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FORGET, obj, behavior_str_of(Behavior.FORGET), note)

    def forgive(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FORGIVE, obj, behavior_str_of(Behavior.FORGIVE), note)

    def freeze(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FREEZE, obj, behavior_str_of(Behavior.FREEZE), note)

    def fry(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.FRY, obj, behavior_str_of(Behavior.FRY), note)

    def gather(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.GATHER, obj, behavior_str_of(Behavior.GATHER), note)

    def gaze(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.GAZE, obj, behavior_str_of(Behavior.GAZE), note)

    def give(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.GIVE, obj, behavior_str_of(Behavior.GIVE), note)

    def glad(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.GLAD, obj, behavior_str_of(Behavior.GLAD), note)

    def go(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.GO, obj, behavior_str_of(Behavior.GO), note)

    def graduate(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.GRADUATE, obj, behavior_str_of(Behavior.GRADUATE), note)

    def greet(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.GREET, obj, behavior_str_of(Behavior.GREET), note)

    def growl(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.GROWL, obj, behavior_str_of(Behavior.GROWL), note)

    def guard(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.GUARD, obj, behavior_str_of(Behavior.GUARD), note)

    def guide(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.GUIDE, obj, behavior_str_of(Behavior.GUIDE), note)

    def hand(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HAND, obj, behavior_str_of(Behavior.HAND), note)

    def handle(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HANDLE, obj, behavior_str_of(Behavior.HANDLE), note)

    def hang(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HANG, obj, behavior_str_of(Behavior.HANG), note)

    def happen(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HAPPEN, obj, behavior_str_of(Behavior.HAPPEN), note)

    def happy(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HAPPY, obj, behavior_str_of(Behavior.HAPPY), note)

    def hate(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HATE, obj, behavior_str_of(Behavior.HATE), note)

    def have(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HAVE, obj, behavior_str_of(Behavior.HAVE), note)

    def heal(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HEAL, obj, behavior_str_of(Behavior.HEAL), note)

    def hear(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HEAR, obj, behavior_str_of(Behavior.HEAR), note)

    def help(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HELP, obj, behavior_str_of(Behavior.HELP), note)

    def hide(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HIDE, obj, behavior_str_of(Behavior.HIDE), note)

    def hire(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HIRE, obj, behavior_str_of(Behavior.HIRE), note)

    def hit(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HIT, obj, behavior_str_of(Behavior.HIT), note)

    def hold(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HOLD, obj, behavior_str_of(Behavior.HOLD), note)

    def hope(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HOPE, obj, behavior_str_of(Behavior.HOPE), note)

    def hug(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HUG, obj, behavior_str_of(Behavior.HUG), note)

    def hunt(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HUNT, obj, behavior_str_of(Behavior.HUNT), note)

    def hurry(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HURRY, obj, behavior_str_of(Behavior.HURRY), note)

    def hurt(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.HURT, obj, behavior_str_of(Behavior.HURT), note)

    def ignore(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.IGNORE, obj, behavior_str_of(Behavior.IGNORE), note)

    def imagine(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.IMAGINE, obj, behavior_str_of(Behavior.IMAGINE), note)

    def injure(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.INJURE, obj, behavior_str_of(Behavior.INJURE), note)

    def instrument(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.INSTRUMENT, obj, behavior_str_of(Behavior.INSTRUMENT), note)

    def introduce(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.INTRODUCE, obj, behavior_str_of(Behavior.INTRODUCE), note)

    def invest(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.INVEST, obj, behavior_str_of(Behavior.INVEST), note)

    def investigate(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.INVESTIGATE, obj, behavior_str_of(Behavior.INVESTIGATE), note)

    def invite(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.INVITE, obj, behavior_str_of(Behavior.INVITE), note)

    def jog(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.JOG, obj, behavior_str_of(Behavior.JOG), note)

    def join(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.JOIN, obj, behavior_str_of(Behavior.JOIN), note)

    def judge(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.JUDGE, obj, behavior_str_of(Behavior.JUDGE), note)

    def jump(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.JUMP, obj, behavior_str_of(Behavior.JUMP), note)

    def keep(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.KEEP, obj, behavior_str_of(Behavior.KEEP), note)

    def keyboard(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.KEYBOARD, obj, behavior_str_of(Behavior.KEYBOARD), note)

    def kick(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.KICK, obj, behavior_str_of(Behavior.KICK), note)

    def kill(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.KILL, obj, behavior_str_of(Behavior.KILL), note)

    def kiss(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.KISS, obj, behavior_str_of(Behavior.KISS), note)

    def knit(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.KNIT, obj, behavior_str_of(Behavior.KNIT), note)

    def knock(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.KNOCK, obj, behavior_str_of(Behavior.KNOCK), note)

    def know(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.KNOW, obj, behavior_str_of(Behavior.KNOW), note)

    def laugh(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LAUGH, obj, behavior_str_of(Behavior.LAUGH), note)

    def lay(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LAY, obj, behavior_str_of(Behavior.LAY), note)

    def learn(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LEARN, obj, behavior_str_of(Behavior.LEARN), note)

    def leave(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LEAVE, obj, behavior_str_of(Behavior.LEAVE), note)

    def let(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LET, obj, behavior_str_of(Behavior.LET), note)

    def lie(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LIE, obj, behavior_str_of(Behavior.LIE), note)

    def life(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LIFE, obj, behavior_str_of(Behavior.LIFE), note)

    def light(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LIGHT, obj, behavior_str_of(Behavior.LIGHT), note)

    def listen(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LISTEN, obj, behavior_str_of(Behavior.LISTEN), note)

    def live(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LIVE, obj, behavior_str_of(Behavior.LIVE), note)

    def look(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LOOK, obj, behavior_str_of(Behavior.LOOK), note)

    def lookdown(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LOOKDOWN, obj, behavior_str_of(Behavior.LOOKDOWN), note)

    def lock(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LOCK, obj, behavior_str_of(Behavior.LOCK), note)

    def lose(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LOSE, obj, behavior_str_of(Behavior.LOSE), note)

    def love(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.LOVE, obj, behavior_str_of(Behavior.LOVE), note)
    
    def make(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MAKE, obj, behavior_str_of(Behavior.MAKE), note)

    def makeup(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MAKEUP, obj, behavior_str_of(Behavior.MAKEUP), note)

    def manage(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MANAGE, obj, behavior_str_of(Behavior.MANAGE), note)

    def manufacture(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MANUFACTURE, obj, behavior_str_of(Behavior.MANUFACTURE), note)

    def maon(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MAON, obj, behavior_str_of(Behavior.MAON), note)

    def mark(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MARK, obj, behavior_str_of(Behavior.MARK), note)

    def marry(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MARRY, obj, behavior_str_of(Behavior.MARRY), note)

    def master(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MASTER, obj, behavior_str_of(Behavior.MASTER), note)

    def measure(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MEASURE, obj, behavior_str_of(Behavior.MEASURE), note)

    def meet(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MEET, obj, behavior_str_of(Behavior.MEET), note)

    def melt(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MELT, obj, behavior_str_of(Behavior.MELT), note)

    def mean(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MEAN, obj, behavior_str_of(Behavior.MEAN), note)

    def memo(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MEMO, obj, behavior_str_of(Behavior.MEMO), note)

    def miss(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MISS, obj, behavior_str_of(Behavior.MISS), note)

    def mix(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MIX, obj, behavior_str_of(Behavior.MIX), note)

    def modify(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MODIFY, obj, behavior_str_of(Behavior.MODIFY), note)

    def move(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MOVE, obj, behavior_str_of(Behavior.MOVE), note)

    def must(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.MUST, obj, behavior_str_of(Behavior.MUST), note)

    def need(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.NEED, obj, behavior_str_of(Behavior.NEED), note)

    def notice(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.NOTICE, obj, behavior_str_of(Behavior.NOTICE), note)

    def obtain(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.OBTAIN, obj, behavior_str_of(Behavior.OBTAIN), note)

    def occur(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.OCCUR, obj, behavior_str_of(Behavior.OCCUR), note)

    def open(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.OPEN, obj, behavior_str_of(Behavior.OPEN), note)

    def oppose(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.OPPOSE, obj, behavior_str_of(Behavior.OPPOSE), note)

    def overcome(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.OVERCOME, obj, behavior_str_of(Behavior.OVERCOME), note)

    def overflow(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.OVERFLOW, obj, behavior_str_of(Behavior.OVERFLOW), note)

    def overlook(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.OVERLOOK, obj, behavior_str_of(Behavior.OVERLOOK), note)

    def own(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.OWN, obj, behavior_str_of(Behavior.OWN), note)

    def pack(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PACK, obj, behavior_str_of(Behavior.PACK), note)

    def paint(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PAINT, obj, behavior_str_of(Behavior.PAINT), note)

    def passes(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PASS, obj, behavior_str_of(Behavior.PASS), note)

    def pause(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PAUSE, obj, behavior_str_of(Behavior.PAUSE), note)

    def pay(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PAY, obj, behavior_str_of(Behavior.PAY), note)

    def phone(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PHONE, obj, behavior_str_of(Behavior.PHONE), note)

    def play(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PLAY, obj, behavior_str_of(Behavior.PLAY), note)

    def plunge(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PLUNGE, obj, behavior_str_of(Behavior.PLUNGE), note)

    def pray(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PRAY, obj, behavior_str_of(Behavior.PRAY), note)

    def practice(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PRACTICE, obj, behavior_str_of(Behavior.PRACTICE), note)

    def press(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PRESS, obj, behavior_str_of(Behavior.PRESS), note)

    def print(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PRINT, obj, behavior_str_of(Behavior.PRINT), note)

    def promise(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PROMISE, obj, behavior_str_of(Behavior.PROMISE), note)

    def publish(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PUBLISH, obj, behavior_str_of(Behavior.PUBLISH), note)

    def pull(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PULL, obj, behavior_str_of(Behavior.PULL), note)

    def push(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PUSH, obj, behavior_str_of(Behavior.PUSH), note)

    def put(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PUT, obj, behavior_str_of(Behavior.PUT), note)

    def punch(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PUNCH, obj, behavior_str_of(Behavior.PUNCH), note)

    def puzzle(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.PUZZLE, obj, behavior_str_of(Behavior.PUZZLE), note)

    def reach(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.REACH, obj, behavior_str_of(Behavior.REACH), note)

    def react(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.REACT, obj, behavior_str_of(Behavior.REACT), note)

    def read(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.READ, obj, behavior_str_of(Behavior.READ), note)

    def realize(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.REALIZE, obj, behavior_str_of(Behavior.REALIZE), note)

    def receive(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.RECEIVE, obj, behavior_str_of(Behavior.RECEIVE), note)

    def recommend(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.RECOMMEND, obj, behavior_str_of(Behavior.RECOMMEND), note)

    def reflect(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.REFLECT, obj, behavior_str_of(Behavior.REFLECT), note)

    def refresh(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.REFRESH, obj, behavior_str_of(Behavior.REFRESH), note)

    def regard(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.REGARD, obj, behavior_str_of(Behavior.REGARD), note)

    def regret(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.REGRET, obj, behavior_str_of(Behavior.REGRET), note)

    def release(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.RELEASE, obj, behavior_str_of(Behavior.RELEASE), note)

    def remember(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.REMEMBER, obj, behavior_str_of(Behavior.REMEMBER), note)

    def rent(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.RENT, obj, behavior_str_of(Behavior.RENT), note)

    def reply(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.REPLY, obj, behavior_str_of(Behavior.REPLY), note)

    def rescue(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.RESCUE, obj, behavior_str_of(Behavior.RESCUE), note)
    
    def rest(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.REST, obj, behavior_str_of(Behavior.REST), note)

    def returns(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.RETURN, obj, behavior_str_of(Behavior.RETURN), note)

    def review(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.REVIEW, obj, behavior_str_of(Behavior.REVIEW), note)

    def ride(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.RIDE, obj, behavior_str_of(Behavior.RIDE), note)

    def ring(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.RING, obj, behavior_str_of(Behavior.RING), note)

    def rise(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.RISE, obj, behavior_str_of(Behavior.RISE), note)

    def rob(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ROB, obj, behavior_str_of(Behavior.ROB), note)

    def rock(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ROCK, obj, behavior_str_of(Behavior.ROCK), note)

    def roll(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.ROLL, obj, behavior_str_of(Behavior.ROLL), note)

    def rub(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.RUB, obj, behavior_str_of(Behavior.RUB), note)

    def runs(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.RUN, obj, behavior_str_of(Behavior.RUN), note)

    def sacrifice(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SACRIFICE, obj, behavior_str_of(Behavior.SACRIFICE), note)

    def sad(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SAD, obj, behavior_str_of(Behavior.SAD), note)

    def save(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SAVE, obj, behavior_str_of(Behavior.SAVE), note)

    def say(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SAY, obj, behavior_str_of(Behavior.SAY), note)

    def scare(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SCARE, obj, behavior_str_of(Behavior.SCARE), note)

    def scratch(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SCRATCH, obj, behavior_str_of(Behavior.SCRATCH), note)

    def scream(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SCREAM, obj, behavior_str_of(Behavior.SCREAM), note)

    def search(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEARCH, obj, behavior_str_of(Behavior.SEARCH), note)

    def seat(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEAT, obj, behavior_str_of(Behavior.SEAT), note)

    def see(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEE, obj, behavior_str_of(Behavior.SEE), note)

    def seek(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEEK, obj, behavior_str_of(Behavior.SEEK), note)

    def seem(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEEM, obj, behavior_str_of(Behavior.SEEM), note)

    def sell(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SELL, obj, behavior_str_of(Behavior.SELL), note)

    def send(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEND, obj, behavior_str_of(Behavior.SEND), note)

    def separate(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEPARATE, obj, behavior_str_of(Behavior.SEPARATE), note)

    def set(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SET, obj, behavior_str_of(Behavior.SET), note)

    def shake(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHAKE, obj, behavior_str_of(Behavior.SHAKE), note)

    def share(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHARE, obj, behavior_str_of(Behavior.SHARE), note)

    def shine(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHINE, obj, behavior_str_of(Behavior.SHINE), note)

    def shock(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHOCK, obj, behavior_str_of(Behavior.SHOCK), note)

    def shoot(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHOOT, obj, behavior_str_of(Behavior.SHOOT), note)

    def show(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHOW, obj, behavior_str_of(Behavior.SHOW), note)

    def sigh(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SIGH, obj, behavior_str_of(Behavior.SIGH), note)

    def sign(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SIGN, obj, behavior_str_of(Behavior.SIGN), note)

    def sing(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SING, obj, behavior_str_of(Behavior.SING), note)

    def sink(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SINK, obj, behavior_str_of(Behavior.SINK), note)

    def sit(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SIT, obj, behavior_str_of(Behavior.SIT), note)

    def skate(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SKATE, obj, behavior_str_of(Behavior.SKATE), note)

    def sleep(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SLEEP, obj, behavior_str_of(Behavior.SLEEP), note)

    def slice(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SLICE, obj, behavior_str_of(Behavior.SLICE), note)

    def slide(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SLIDE, obj, behavior_str_of(Behavior.SLIDE), note)

    def slip(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SLIP, obj, behavior_str_of(Behavior.SLIP), note)

    def slobber(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SLOBBER, obj, behavior_str_of(Behavior.SLOBBER), note)

    def smell(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SMELL, obj, behavior_str_of(Behavior.SMELL), note)

    def smile(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SMILE, obj, behavior_str_of(Behavior.SMILE), note)

    def smoke(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SMOKE, obj, behavior_str_of(Behavior.SMOKE), note)

    def solve(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SOLVE, obj, behavior_str_of(Behavior.SOLVE), note)

    def sound(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SOUND, obj, behavior_str_of(Behavior.SOUND), note)

    def speak(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPEAK, obj, behavior_str_of(Behavior.SPEAK), note)

    def spend(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPEND, obj, behavior_str_of(Behavior.SPEND), note)

    def spill(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPILL, obj, behavior_str_of(Behavior.SPILL), note)

    def spin(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPIN, obj, behavior_str_of(Behavior.SPIN), note)

    def split(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPLIT, obj, behavior_str_of(Behavior.SPLIT), note)

    def spread(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPREAD, obj, behavior_str_of(Behavior.SPREAD), note)

    def squeeze(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SQUEEZE, obj, behavior_str_of(Behavior.SQUEEZE), note)

    def stand(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.STAND, obj, behavior_str_of(Behavior.STAND), note)

    def stare(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.STARE, obj, behavior_str_of(Behavior.STARE), note)

    def start(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.START, obj, behavior_str_of(Behavior.START), note)

    def steal(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.STEAL, obj, behavior_str_of(Behavior.STEAL), note)

    def stick(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.STICK, obj, behavior_str_of(Behavior.STICK), note)

    def stop(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.STOP, obj, behavior_str_of(Behavior.STOP), note)

    def store(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.STORE, obj, behavior_str_of(Behavior.STORE), note)

    def study(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.STUDY, obj, behavior_str_of(Behavior.STUDY), note)

    def succeed(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SUCCEED, obj, behavior_str_of(Behavior.SUCCEED), note)

    def suggest(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SUGGEST, obj, behavior_str_of(Behavior.SUGGEST), note)

    def supply(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SUPPLY, obj, behavior_str_of(Behavior.SUPPLY), note)

    def support(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SUPPORT, obj, behavior_str_of(Behavior.SUPPORT), note)

    def suppose(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SUPPOSE, obj, behavior_str_of(Behavior.SUPPOSE), note)

    def surprise(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SURPRISE, obj, behavior_str_of(Behavior.SURPRISE), note)

    def surround(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SURROUND, obj, behavior_str_of(Behavior.SURROUND), note)

    def survive(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SURVIVE, obj, behavior_str_of(Behavior.SURVIVE), note)

    def swim(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SWIM, obj, behavior_str_of(Behavior.SWIM), note)

    def swing(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SWING, obj, behavior_str_of(Behavior.SWING), note)

    def sword(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.SWORD, obj, behavior_str_of(Behavior.SWORD), note)

    def take(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TAKE, obj, behavior_str_of(Behavior.TAKE), note)

    def talk(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TALK, obj, behavior_str_of(Behavior.TALK), note)

    def tap(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TAP, obj, behavior_str_of(Behavior.TAP), note)

    def teach(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TEACH, obj, behavior_str_of(Behavior.TEACH), note)

    def thank(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.THANK, obj, behavior_str_of(Behavior.THANK), note)

    def think(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.THINK, obj, behavior_str_of(Behavior.THINK), note)

    def throw(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.THROW, obj, behavior_str_of(Behavior.THROW), note)

    def tie(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TIE, obj, behavior_str_of(Behavior.TIE), note)

    def toss(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TOSS, obj, behavior_str_of(Behavior.TOSS), note)

    def touch(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TOUCH, obj, behavior_str_of(Behavior.TOUCH), note)

    def train(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRAIN, obj, behavior_str_of(Behavior.TRAIN), note)

    def transfer(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRANSFER, obj, behavior_str_of(Behavior.TRANSFER), note)

    def transform(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRANSFORM, obj, behavior_str_of(Behavior.TRANSFORM), note)

    def travel(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRAVEL, obj, behavior_str_of(Behavior.TRAVEL), note)

    def trip(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRIP, obj, behavior_str_of(Behavior.TRIP), note)

    def tries(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRY, obj, behavior_str_of(Behavior.TRY), note)

    def trust(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRUST, obj, behavior_str_of(Behavior.TRUST), note)

    def turn(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TURN, obj, behavior_str_of(Behavior.TURN), note)

    def twist(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.TWIST, obj, behavior_str_of(Behavior.TWIST), note)

    def understand(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.UNDERSTAND, obj, behavior_str_of(Behavior.UNDERSTAND), note)

    def unite(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.UNITE, obj, behavior_str_of(Behavior.UNITE), note)

    def unlock(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.UNLOCK, obj, behavior_str_of(Behavior.UNLOCK), note)

    def use(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.USE, obj, behavior_str_of(Behavior.USE), note)

    def vanish(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.VANISH, obj, behavior_str_of(Behavior.VANISH), note)

    def visit(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.VISIT, obj, behavior_str_of(Behavior.VISIT), note)

    def wait(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WAIT, obj, behavior_str_of(Behavior.WAIT), note)

    def wake(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WAKE, obj, behavior_str_of(Behavior.WAKE), note)

    def walk(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WALK, obj, behavior_str_of(Behavior.WALK), note)

    def want(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WANT, obj, behavior_str_of(Behavior.WANT), note)

    def warm(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WARM, obj, behavior_str_of(Behavior.WARM), note)

    def waste(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WASTE, obj, behavior_str_of(Behavior.WASTE), note)

    def watch(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WATCH, obj, behavior_str_of(Behavior.WATCH), note)

    def wave(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WAVE, obj, behavior_str_of(Behavior.WAVE), note)

    def wear(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WEAR, obj, behavior_str_of(Behavior.WEAR), note)

    def weigh(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WEIGH, obj, behavior_str_of(Behavior.WEIGH), note)

    def welcome(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WELCOME, obj, behavior_str_of(Behavior.WELCOME), note)

    def whisper(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WHISPER, obj, behavior_str_of(Behavior.WHISPER), note)

    def wind(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WIND, obj, behavior_str_of(Behavior.WIND), note)

    def wipe(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WIPE, obj, behavior_str_of(Behavior.WIPE), note)

    def wish(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WISH, obj, behavior_str_of(Behavior.WISH), note)

    def wonder(self, action: str, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WONDER, obj, behavior_str_of(Behavior.WONDER), note)

    def work(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WORK, obj, behavior_str_of(Behavior.WORK), note)

    def worry(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WORRY, obj, behavior_str_of(Behavior.WORRY), note)

    def wry(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WRY, obj, behavior_str_of(Behavior.WRY), note)

    def write(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.WRITE, obj, behavior_str_of(Behavior.WRITE), note)

    def yell(self, action: str=DEF_ACT, obj: _BaseSubject=None, note: str=DEF_NOTE):
        return self.act(action, Behavior.YELL, obj, behavior_str_of(Behavior.YELL), note)

