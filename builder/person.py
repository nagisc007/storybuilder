# -*- coding: utf-8 -*-
"""Person class deined.
"""
from .base import _BasePerson
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
    def accept(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.ACCEPT, behavior_str_of(Behavior.ACCEPT), note)

    def acquire(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.ACQUIRE, behavior_str_of(Behavior.ACQUIRE), note)

    def add(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.ADD, behavior_str_of(Behavior.ADD), note)

    def advise(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.ADVISE, behavior_str_of(Behavior.ADVISE), note)

    def agree(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.AGREE, behavior_str_of(Behavior.AGREE), note)

    def aim(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.AIM, behavior_str_of(Behavior.AIM), note)

    def angry(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.ANGRY, behavior_str_of(Behavior.ANGRY), note)

    def answer(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.ANSWER, behavior_str_of(Behavior.ANSWER), note)

    def appear(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.APPEAR, behavior_str_of(Behavior.APPEAR), note)

    def apply(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.APPLY, behavior_str_of(Behavior.APPLY), note)

    def arrive(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.ARRIVE, behavior_str_of(Behavior.ARRIVE), note)

    def ask(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.ASK, behavior_str_of(Behavior.ASK), note)

    def attack(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.ATTACK, behavior_str_of(Behavior.ATTACK), note)

    def be(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.BE, behavior_str_of(Behavior.BE), note)

    def become(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.BECOME, behavior_str_of(Behavior.BECOME), note)

    def begin(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.BEGIN, behavior_str_of(Behavior.BEGIN), note)

    def believe(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.BELIEVE, behavior_str_of(Behavior.BELIEVE), note)

    def bet(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.BET, behavior_str_of(Behavior.BET), note)

    def bind(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.BIND, behavior_str_of(Behavior.BIND), note)

    def borrow(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.BORROW, behavior_str_of(Behavior.BORROW), note)

    def breaks(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.BREAK, behavior_str_of(Behavior.BREAK), note)

    def breathe(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.BREATHE, behavior_str_of(Behavior.BREATHE), note)

    def brow(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.BROW, behavior_str_of(Behavior.BROW), note)

    def build(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.BUILD, behavior_str_of(Behavior.BUILD), note)

    def burn(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.BURN, behavior_str_of(Behavior.BURN), note)

    def burst(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.BURST, behavior_str_of(Behavior.BURST), note)

    def bury(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.BURY, behavior_str_of(Behavior.BURY), note)

    def buy(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.BUY, behavior_str_of(Behavior.BUY), note)

    def calculate(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.CALCULATE, behavior_str_of(Behavior.CALCULATE), note)

    def call(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CALL, behavior_str_of(Behavior.CALL), note)

    def care(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CARE, behavior_str_of(Behavior.CARE), note)

    def carry(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CARRY, behavior_str_of(Behavior.CARRY), note)

    def catch(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CATCH, behavior_str_of(Behavior.CATCH), note)

    def change(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CHANGE, behavior_str_of(Behavior.CHANGE), note)

    def charm(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CHARM, behavior_str_of(Behavior.CHARM), note)

    def check(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CHECK, behavior_str_of(Behavior.CHECK), note)

    def cheer(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CHEER, behavior_str_of(Behavior.CHEER), note)

    def choose(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CHOOSE, behavior_str_of(Behavior.CHOOSE), note)

    def clean(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.CLEAN, behavior_str_of(Behavior.CLEAN), note)

    def click(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.CLICK, behavior_str_of(Behavior.CLICK), note)

    def climb(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CLIMB, behavior_str_of(Behavior.CLIMB), note)

    def close(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CLOSE, behavior_str_of(Behavior.CLOSE), note)

    def clothe(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CLOTHE, behavior_str_of(Behavior.CLOTHE), note)

    def coach(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.COACH, behavior_str_of(Behavior.COACH), note)

    def come(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.COME, behavior_str_of(Behavior.COME), note)
    
    def command(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.COMMAND, behavior_str_of(Behavior.COMMAND), note)

    def compare(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.COMPARE, behavior_str_of(Behavior.COMPARE), note)

    def complete(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.COMPLETE, behavior_str_of(Behavior.COMPLETE), note)

    def confess(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CONFESS, behavior_str_of(Behavior.CONFESS), note)

    def confuse(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.CONFUSE, behavior_str_of(Behavior.CONFUSE), note)

    def contact(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CONTACT, behavior_str_of(Behavior.CONTACT), note)

    def continues(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CONTINUE, behavior_str_of(Behavior.CONTINUE), note)

    def cooperate(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.COOPERATE, behavior_str_of(Behavior.COOPERATE), note)

    def cough(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.COUGH, behavior_str_of(Behavior.COUGH), note)

    def cook(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.COOK, behavior_str_of(Behavior.COOK), note)

    def create(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CREATE, behavior_str_of(Behavior.CREATE), note)

    def cry(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.CRY, behavior_str_of(Behavior.CRY), note)

    def cut(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.CUT, behavior_str_of(Behavior.CUT), note)

    def dance(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.DANCE, behavior_str_of(Behavior.DANCE), note)

    def deal(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.DEAL, behavior_str_of(Behavior.DEAL), note)

    def define(self ,action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.DEFINE, behavior_str_of(Behavior.DEFINE), note)

    def die(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.DIE, behavior_str_of(Behavior.DIE), note)

    def dig(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.DIG, behavior_str_of(Behavior.DIG), note)

    def disappear(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.DISAPPEAR, behavior_str_of(Behavior.DISAPPEAR), note)

    def disapprove(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.DISAPPROVE, behavior_str_of(Behavior.DISAPPROVE), note)

    def dislike(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.DISLIKE, behavior_str_of(Behavior.DISLIKE), note)

    def dispel(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.DISPEL, behavior_str_of(Behavior.DISPEL), note)

    def display(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.DISPLAY, behavior_str_of(Behavior.DISPLAY), note)

    def dive(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.DIVE, behavior_str_of(Behavior.DIVE), note)

    def do(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.DO, behavior_str_of(Behavior.DO), note)

    def doubt(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.DOUBT, behavior_str_of(Behavior.DOUBT), note)

    def draw(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.DRAW, behavior_str_of(Behavior.DRAW), note)

    def dream(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.DREAM, behavior_str_of(Behavior.DREAM), note)

    def dress(self ,action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.DRESS, behavior_str_of(Behavior.DRESS), note)

    def drink(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.DRINK, behavior_str_of(Behavior.DRINK), note)

    def drive(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.DRIVE, behavior_str_of(Behavior.DRIVE), note)

    def drop(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.DROP, behavior_str_of(Behavior.DROP), note)

    def dry(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.DRY, behavior_str_of(Behavior.DRY), note)

    def earn(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.EARN, behavior_str_of(Behavior.EARN), note)

    def eat(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.EAT, behavior_str_of(Behavior.EAT), note)

    def educate(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.EDUCATE, behavior_str_of(Behavior.EDUCATE), note)

    def email(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.EMAIL, behavior_str_of(Behavior.EMAIL), note)

    def employ(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.EMPLOY, behavior_str_of(Behavior.EMPLOY), note)

    def engage(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.ENGAGE, behavior_str_of(Behavior.ENGAGE), note)

    def enjoy(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.ENJOY, behavior_str_of(Behavior.ENJOY), note)

    def enter(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.ENTER, behavior_str_of(Behavior.ENTER), note)

    def envy(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.ENVY, behavior_str_of(Behavior.ENVY), note)

    def equip(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.EQUIP, behavior_str_of(Behavior.EQUIP), note)

    def exchange(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.EXCHANGE, behavior_str_of(Behavior.EXCHANGE), note)

    def examine(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.EXAMINE, behavior_str_of(Behavior.EXAMINE), note)

    def excite(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.EXCITE, behavior_str_of(Behavior.EXCITE), note)

    def explore(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.EXPLORE, behavior_str_of(Behavior.EXPLORE), note)

    def face(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.FACE, behavior_str_of(Behavior.FACE), note)

    def fail(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.FAIL, behavior_str_of(Behavior.FAIL), note)

    def fall(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.FALL, behavior_str_of(Behavior.FALL), note)

    def feel(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.FEEL, behavior_str_of(Behavior.FEEL), note)

    def fib(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.FIB, behavior_str_of(Behavior.FIB), note)

    def find(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.FIND, behavior_str_of(Behavior.FIND), note)

    def fight(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.FIGHT, behavior_str_of(Behavior.FIGHT), note)

    def fill(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.FILL, behavior_str_of(Behavior.FILL), note)

    def finish(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.FINISH, behavior_str_of(Behavior.FINISH), note)

    def fire(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.FIRE, behavior_str_of(Behavior.FIRE), note)

    def firejob(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.FIREJOB, behavior_str_of(Behavior.FIREJOB, note))

    def flash(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.FLASH, behavior_str_of(Behavior.FLASH), note)

    def float(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.FLOAT, behavior_str_of(Behavior.FLOAT), note)

    def fly(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.FLY, behavior_str_of(Behavior.FLY), note)

    def follow(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.FOLLOW, behavior_str_of(Behavior.FOLLOW), note)

    def forget(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.FORGET, behavior_str_of(Behavior.FORGET), note)

    def forgive(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.FORGIVE, behavior_str_of(Behavior.FORGIVE), note)

    def freeze(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.FREEZE, behavior_str_of(Behavior.FREEZE), note)

    def fry(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.FRY, behavior_str_of(Behavior.FRY), note)

    def gather(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.GATHER, behavior_str_of(Behavior.GATHER), note)

    def gaze(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.GAZE, behavior_str_of(Behavior.GAZE), note)

    def give(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.GIVE, behavior_str_of(Behavior.GIVE), note)

    def glad(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.GLAD, behavior_str_of(Behavior.GLAD), note)

    def go(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.GO, behavior_str_of(Behavior.GO), note)

    def graduate(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.GRADUATE, behavior_str_of(Behavior.GRADUATE), note)

    def greet(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.GREET, behavior_str_of(Behavior.GREET), note)

    def growl(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.GROWL, behavior_str_of(Behavior.GROWL), note)

    def guard(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.GUARD, behavior_str_of(Behavior.GUARD), note)

    def guide(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.GUIDE, behavior_str_of(Behavior.GUIDE), note)

    def hand(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.HAND, behavior_str_of(Behavior.HAND), note)

    def handle(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HANDLE, behavior_str_of(Behavior.HANDLE), note)

    def hang(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HANG, behavior_str_of(Behavior.HANG), note)

    def happen(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HAPPEN, behavior_str_of(Behavior.HAPPEN), note)

    def happy(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.HAPPY, behavior_str_of(Behavior.HAPPY), note)

    def hate(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HATE, behavior_str_of(Behavior.HATE), note)

    def have(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HAVE, behavior_str_of(Behavior.HAVE), note)

    def heal(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HEAL, behavior_str_of(Behavior.HEAL), note)

    def hear(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HEAR, behavior_str_of(Behavior.HEAR), note)

    def help(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.HELP, behavior_str_of(Behavior.HELP), note)

    def hide(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HIDE, behavior_str_of(Behavior.HIDE), note)

    def hire(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HIRE, behavior_str_of(Behavior.HIRE), note)

    def hit(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HIT, behavior_str_of(Behavior.HIT), note)

    def hold(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.HOLD, behavior_str_of(Behavior.HOLD), note)

    def hope(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.HOPE, behavior_str_of(Behavior.HOPE), note)

    def hug(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HUG, behavior_str_of(Behavior.HUG), note)

    def hunt(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.HUNT, behavior_str_of(Behavior.HUNT), note)

    def hurry(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.HURRY, behavior_str_of(Behavior.HURRY), note)

    def hurt(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.HURT, behavior_str_of(Behavior.HURT), note)

    def ignore(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.IGNORE, behavior_str_of(Behavior.IGNORE), note)

    def imagine(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.IMAGINE, behavior_str_of(Behavior.IMAGINE), note)

    def injure(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.INJURE, behavior_str_of(Behavior.INJURE), note)

    def instrument(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.INSTRUMENT, behavior_str_of(Behavior.INSTRUMENT), note)

    def introduce(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.INTRODUCE, behavior_str_of(Behavior.INTRODUCE), note)

    def invest(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.INVEST, behavior_str_of(Behavior.INVEST), note)

    def investigate(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.INVESTIGATE, behavior_str_of(Behavior.INVESTIGATE), note)

    def invite(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.INVITE, behavior_str_of(Behavior.INVITE), note)

    def jog(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.JOG, behavior_str_of(Behavior.JOG), note)

    def join(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.JOIN, behavior_str_of(Behavior.JOIN), note)

    def judge(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.JUDGE, behavior_str_of(Behavior.JUDGE), note)

    def jump(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.JUMP, behavior_str_of(Behavior.JUMP), note)

    def keep(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.KEEP, behavior_str_of(Behavior.KEEP), note)

    def keyboard(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.KEYBOARD, behavior_str_of(Behavior.KEYBOARD), note)

    def kick(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.KICK, behavior_str_of(Behavior.KICK), note)

    def kill(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.KILL, behavior_str_of(Behavior.KILL), note)

    def kiss(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.KISS, behavior_str_of(Behavior.KISS), note)

    def knit(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.KNIT, behavior_str_of(Behavior.KNIT), note)

    def knock(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.KNOCK, behavior_str_of(Behavior.KNOCK), note)

    def know(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.KNOW, behavior_str_of(Behavior.KNOW), note)

    def laugh(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.LAUGH, behavior_str_of(Behavior.LAUGH), note)

    def lay(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.LAY, behavior_str_of(Behavior.LAY), note)

    def learn(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.LEARN, behavior_str_of(Behavior.LEARN), note)

    def leave(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.LEAVE, behavior_str_of(Behavior.LEAVE), note)

    def let(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.LET, behavior_str_of(Behavior.LET), note)

    def lie(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.LIE, behavior_str_of(Behavior.LIE), note)

    def life(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.LIFE, behavior_str_of(Behavior.LIFE), note)

    def light(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.LIGHT, behavior_str_of(Behavior.LIGHT), note)

    def listen(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.LISTEN, behavior_str_of(Behavior.LISTEN), note)

    def live(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.LIVE, behavior_str_of(Behavior.LIVE), note)

    def look(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.LOOK, behavior_str_of(Behavior.LOOK), note)

    def lookdown(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.LOOKDOWN, behavior_str_of(Behavior.LOOKDOWN), note)

    def lock(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.LOCK, behavior_str_of(Behavior.LOCK), note)

    def lose(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.LOSE, behavior_str_of(Behavior.LOSE), note)

    def love(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.LOVE, behavior_str_of(Behavior.LOVE), note)
    
    def make(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MAKE, behavior_str_of(Behavior.MAKE), note)

    def makeup(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.MAKEUP, behavior_str_of(Behavior.MAKEUP), note)

    def manage(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MANAGE, behavior_str_of(Behavior.MANAGE), note)

    def manufacture(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MANUFACTURE, behavior_str_of(Behavior.MANUFACTURE), note)

    def maon(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.MAON, behavior_str_of(Behavior.MAON), note)

    def mark(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.MARK, behavior_str_of(Behavior.MARK), note)

    def marry(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.MARRY, behavior_str_of(Behavior.MARRY), note)

    def master(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MASTER, behavior_str_of(Behavior.MASTER), note)

    def measure(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MEASURE, behavior_str_of(Behavior.MEASURE), note)

    def meet(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MEET, behavior_str_of(Behavior.MEET), note)

    def melt(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.MELT, behavior_str_of(Behavior.MELT), note)

    def mean(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MEAN, behavior_str_of(Behavior.MEAN), note)

    def memo(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MEMO, behavior_str_of(Behavior.MEMO), note)

    def miss(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.MISS, behavior_str_of(Behavior.MISS), note)

    def mix(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MIX, behavior_str_of(Behavior.MIX), note)

    def modify(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MODIFY, behavior_str_of(Behavior.MODIFY), note)

    def move(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MOVE, behavior_str_of(Behavior.MOVE), note)

    def must(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.MUST, behavior_str_of(Behavior.MUST), note)

    def need(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.NEED, behavior_str_of(Behavior.NEED), note)

    def notice(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.NOTICE, behavior_str_of(Behavior.NOTICE), note)

    def obtain(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.OBTAIN, behavior_str_of(Behavior.OBTAIN), note)

    def occur(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.OCCUR, behavior_str_of(Behavior.OCCUR), note)

    def open(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.OPEN, behavior_str_of(Behavior.OPEN), note)

    def oppose(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.OPPOSE, behavior_str_of(Behavior.OPPOSE), note)

    def overcome(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.OVERCOME, behavior_str_of(Behavior.OVERCOME), note)

    def overflow(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.OVERFLOW, behavior_str_of(Behavior.OVERFLOW), note)

    def overlook(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.OVERLOOK, behavior_str_of(Behavior.OVERLOOK), note)

    def own(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.OWN, behavior_str_of(Behavior.OWN), note)

    def pack(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PACK, behavior_str_of(Behavior.PACK), note)

    def paint(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PAINT, behavior_str_of(Behavior.PAINT), note)

    def passes(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PASS, behavior_str_of(Behavior.PASS), note)

    def pause(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PAUSE, behavior_str_of(Behavior.PAUSE), note)

    def pay(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PAY, behavior_str_of(Behavior.PAY), note)

    def phone(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.PHONE, behavior_str_of(Behavior.PHONE), note)

    def play(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.PLAY, behavior_str_of(Behavior.PLAY), note)

    def plunge(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PLUNGE, behavior_str_of(Behavior.PLUNGE), note)

    def pray(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.PRAY, behavior_str_of(Behavior.PRAY), note)

    def practice(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PRACTICE, behavior_str_of(Behavior.PRACTICE), note)

    def press(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PRESS, behavior_str_of(Behavior.PRESS), note)

    def print(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.PRINT, behavior_str_of(Behavior.PRINT), note)

    def promise(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PROMISE, behavior_str_of(Behavior.PROMISE), note)

    def publish(self, action: str, note=DEF_NOTE):
        return self.act(action, Behavior.PUBLISH, behavior_str_of(Behavior.PUBLISH), note)

    def pull(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PULL, behavior_str_of(Behavior.PULL), note)

    def push(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PUSH, behavior_str_of(Behavior.PUSH), note)

    def put(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PUT, behavior_str_of(Behavior.PUT), note)

    def punch(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.PUNCH, behavior_str_of(Behavior.PUNCH), note)

    def puzzle(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.PUZZLE, behavior_str_of(Behavior.PUZZLE), note)

    def reach(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.REACH, behavior_str_of(Behavior.REACH), note)

    def react(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.REACT, behavior_str_of(Behavior.REACT), note)

    def read(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.READ, behavior_str_of(Behavior.READ), note)

    def realize(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.REALIZE, behavior_str_of(Behavior.REALIZE), note)

    def receive(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.RECEIVE, behavior_str_of(Behavior.RECEIVE), note)

    def recommend(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.RECOMMEND, behavior_str_of(Behavior.RECOMMEND), note)

    def reflect(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.REFLECT, behavior_str_of(Behavior.REFLECT), note)

    def refresh(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.REFRESH, behavior_str_of(Behavior.REFRESH), note)

    def regard(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.REGARD, behavior_str_of(Behavior.REGARD), note)

    def regret(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.REGRET, behavior_str_of(Behavior.REGRET), note)

    def release(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.RELEASE, behavior_str_of(Behavior.RELEASE), note)

    def remember(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.REMEMBER, behavior_str_of(Behavior.REMEMBER), note)

    def rent(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.RENT, behavior_str_of(Behavior.RENT), note)

    def reply(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.REPLY, behavior_str_of(Behavior.REPLY), note)

    def rescue(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.RESCUE, behavior_str_of(Behavior.RESCUE), note)
    
    def rest(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.REST, behavior_str_of(Behavior.REST), note)

    def returns(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.RETURN, behavior_str_of(Behavior.RETURN), note)

    def review(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.REVIEW, behavior_str_of(Behavior.REVIEW), note)

    def ride(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.RIDE, behavior_str_of(Behavior.RIDE), note)

    def ring(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.RING, behavior_str_of(Behavior.RING), note)

    def rise(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.RISE, behavior_str_of(Behavior.RISE), note)

    def rob(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.ROB, behavior_str_of(Behavior.ROB), note)

    def rock(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.ROCK, behavior_str_of(Behavior.ROCK), note)

    def roll(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.ROLL, behavior_str_of(Behavior.ROLL), note)

    def rub(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.RUB, behavior_str_of(Behavior.RUB), note)

    def runs(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.RUN, behavior_str_of(Behavior.RUN), note)

    def sacrifice(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SACRIFICE, behavior_str_of(Behavior.SACRIFICE), note)

    def sad(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SAD, behavior_str_of(Behavior.SAD), note)

    def save(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SAVE, behavior_str_of(Behavior.SAVE), note)

    def say(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SAY, behavior_str_of(Behavior.SAY), note)

    def scare(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SCARE, behavior_str_of(Behavior.SCARE), note)

    def scratch(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SCRATCH, behavior_str_of(Behavior.SCRATCH), note)

    def scream(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SCREAM, behavior_str_of(Behavior.SCREAM), note)

    def search(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEARCH, behavior_str_of(Behavior.SEARCH), note)

    def seat(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEAT, behavior_str_of(Behavior.SEAT), note)

    def see(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEE, behavior_str_of(Behavior.SEE), note)

    def seek(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEEK, behavior_str_of(Behavior.SEEK), note)

    def seem(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEEM, behavior_str_of(Behavior.SEEM), note)

    def sell(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SELL, behavior_str_of(Behavior.SELL), note)

    def send(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEND, behavior_str_of(Behavior.SEND), note)

    def separate(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SEPARATE, behavior_str_of(Behavior.SEPARATE), note)

    def set(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SET, behavior_str_of(Behavior.SET), note)

    def shake(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHAKE, behavior_str_of(Behavior.SHAKE), note)

    def share(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHARE, behavior_str_of(Behavior.SHARE), note)

    def shine(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHINE, behavior_str_of(Behavior.SHINE), note)

    def shock(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHOCK, behavior_str_of(Behavior.SHOCK), note)

    def shoot(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHOOT, behavior_str_of(Behavior.SHOOT), note)

    def show(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SHOW, behavior_str_of(Behavior.SHOW), note)

    def sigh(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SIGH, behavior_str_of(Behavior.SIGH), note)

    def sign(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SIGN, behavior_str_of(Behavior.SIGN), note)

    def sing(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SING, behavior_str_of(Behavior.SING), note)

    def sink(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SINK, behavior_str_of(Behavior.SINK), note)

    def sit(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SIT, behavior_str_of(Behavior.SIT), note)

    def skate(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SKATE, behavior_str_of(Behavior.SKATE), note)

    def sleep(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SLEEP, behavior_str_of(Behavior.SLEEP), note)

    def slice(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SLICE, behavior_str_of(Behavior.SLICE), note)

    def slide(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SLIDE, behavior_str_of(Behavior.SLIDE), note)

    def slip(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SLIP, behavior_str_of(Behavior.SLIP), note)

    def slobber(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SLOBBER, behavior_str_of(Behavior.SLOBBER), note)

    def smell(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SMELL, behavior_str_of(Behavior.SMELL), note)

    def smile(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SMILE, behavior_str_of(Behavior.SMILE), note)

    def smoke(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SMOKE, behavior_str_of(Behavior.SMOKE), note)

    def solve(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SOLVE, behavior_str_of(Behavior.SOLVE), note)

    def sound(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SOUND, behavior_str_of(Behavior.SOUND), note)

    def speak(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPEAK, behavior_str_of(Behavior.SPEAK), note)

    def spend(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPEND, behavior_str_of(Behavior.SPEND), note)

    def spill(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPILL, behavior_str_of(Behavior.SPILL), note)

    def spin(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPIN, behavior_str_of(Behavior.SPIN), note)

    def split(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPLIT, behavior_str_of(Behavior.SPLIT), note)

    def spread(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SPREAD, behavior_str_of(Behavior.SPREAD), note)

    def squeeze(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SQUEEZE, behavior_str_of(Behavior.SQUEEZE), note)

    def stand(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.STAND, behavior_str_of(Behavior.STAND), note)

    def stare(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.STARE, behavior_str_of(Behavior.STARE), note)

    def start(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.START, behavior_str_of(Behavior.START), note)

    def steal(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.STEAL, behavior_str_of(Behavior.STEAL), note)

    def stick(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.STICK, behavior_str_of(Behavior.STICK), note)

    def stop(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.STOP, behavior_str_of(Behavior.STOP), note)

    def store(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.STORE, behavior_str_of(Behavior.STORE), note)

    def study(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.STUDY, behavior_str_of(Behavior.STUDY), note)

    def succeed(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SUCCEED, behavior_str_of(Behavior.SUCCEED), note)

    def suggest(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SUGGEST, behavior_str_of(Behavior.SUGGEST), note)

    def supply(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SUPPLY, behavior_str_of(Behavior.SUPPLY), note)

    def support(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SUPPORT, behavior_str_of(Behavior.SUPPORT), note)

    def suppose(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SUPPOSE, behavior_str_of(Behavior.SUPPOSE), note)

    def surprise(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SURPRISE, behavior_str_of(Behavior.SURPRISE), note)

    def surround(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SURROUND, behavior_str_of(Behavior.SURROUND), note)

    def survive(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SURVIVE, behavior_str_of(Behavior.SURVIVE), note)

    def swim(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SWIM, behavior_str_of(Behavior.SWIM), note)

    def swing(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.SWING, behavior_str_of(Behavior.SWING), note)

    def sword(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.SWORD, behavior_str_of(Behavior.SWORD), note)

    def take(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.TAKE, behavior_str_of(Behavior.TAKE), note)

    def talk(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.TALK, behavior_str_of(Behavior.TALK), note)

    def tap(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.TAP, behavior_str_of(Behavior.TAP), note)

    def teach(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.TEACH, behavior_str_of(Behavior.TEACH), note)

    def thank(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.THANK, behavior_str_of(Behavior.THANK), note)

    def think(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.THINK, behavior_str_of(Behavior.THINK), note)

    def throw(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.THROW, behavior_str_of(Behavior.THROW), note)

    def tie(self, action: str, note=DEF_NOTE):
        return self.act(action, Behavior.TIE, behavior_str_of(Behavior.TIE), note)

    def toss(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.TOSS, behavior_str_of(Behavior.TOSS), note)

    def touch(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.TOUCH, behavior_str_of(Behavior.TOUCH), note)

    def train(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRAIN, behavior_str_of(Behavior.TRAIN), note)

    def transfer(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRANSFER, behavior_str_of(Behavior.TRANSFER), note)

    def transform(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRANSFORM, behavior_str_of(Behavior.TRANSFORM), note)

    def travel(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRAVEL, behavior_str_of(Behavior.TRAVEL), note)

    def trip(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRIP, behavior_str_of(Behavior.TRIP), note)

    def tries(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRY, behavior_str_of(Behavior.TRY), note)

    def trust(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.TRUST, behavior_str_of(Behavior.TRUST), note)

    def turn(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.TURN, behavior_str_of(Behavior.TURN), note)

    def twist(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.TWIST, behavior_str_of(Behavior.TWIST), note)

    def understand(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.UNDERSTAND, behavior_str_of(Behavior.UNDERSTAND), note)

    def unite(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.UNITE, behavior_str_of(Behavior.UNITE), note)

    def unlock(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.UNLOCK, behavior_str_of(Behavior.UNLOCK), note)

    def use(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.USE, behavior_str_of(Behavior.USE), note)

    def vanish(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.VANISH, behavior_str_of(Behavior.VANISH), note)

    def visit(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.VISIT, behavior_str_of(Behavior.VISIT), note)

    def wait(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.WAIT, behavior_str_of(Behavior.WAIT), note)

    def wake(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WAKE, behavior_str_of(Behavior.WAKE), note)

    def walk(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WALK, behavior_str_of(Behavior.WALK), note)

    def want(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.WANT, behavior_str_of(Behavior.WANT), note)

    def warm(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.WARM, behavior_str_of(Behavior.WARM), note)

    def waste(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WASTE, behavior_str_of(Behavior.WASTE), note)

    def watch(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.WATCH, behavior_str_of(Behavior.WATCH), note)

    def wave(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WAVE, behavior_str_of(Behavior.WAVE), note)

    def wear(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WEAR, behavior_str_of(Behavior.WEAR), note)

    def weigh(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WEIGH, behavior_str_of(Behavior.WEIGH), note)

    def welcome(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WELCOME, behavior_str_of(Behavior.WELCOME), note)

    def whisper(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WHISPER, behavior_str_of(Behavior.WHISPER), note)

    def wind(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.WIND, behavior_str_of(Behavior.WIND), note)

    def wipe(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.WIPE, behavior_str_of(Behavior.WIPE), note)

    def wish(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.WISH, behavior_str_of(Behavior.WISH), note)

    def wonder(self, action: str, note: str=DEF_NOTE):
        return self.act(action, Behavior.WONDER, behavior_str_of(Behavior.WONDER), note)

    def work(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WORK, behavior_str_of(Behavior.WORK), note)

    def worry(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WORRY, behavior_str_of(Behavior.WORRY), note)

    def wry(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WRY, behavior_str_of(Behavior.WRY), note)

    def write(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.WRITE, behavior_str_of(Behavior.WRITE), note)

    def yell(self, action: str=DEF_ACT, note: str=DEF_NOTE):
        return self.act(action, Behavior.YELL, behavior_str_of(Behavior.YELL), note)

