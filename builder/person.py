# -*- coding: utf-8 -*-
"""Person class deined.
"""
from .base import _BaseSubject, _BasePerson
from .behavior import Behavior


class Person(_BasePerson):
    """Character class.

    Attributes:
        selfcall (str): a subject called himself.
    """
    DEF_ACT = "-"
    DEF_NOTE = "nothing"
    DEF_SELFCALL = "私"
    def __init__(self, name:str, age: int, sex: str, job: str, selfcall: str=DEF_SELFCALL, note: str=""):
        super().__init__(name, age, sex, job, note)
        self.selfcall = selfcall

    # basic actions
    def accept(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ACCEPT, obj, info, note)

    def acquire(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ACQUIRE, obj, info, note)

    def add(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ADD, obj, info, note)

    def advise(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ADVISE, obj, info, note)

    def agree(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.AGREE, obj, info, note)

    def aim(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.AIM, obj, info, note)

    def angry(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ANGRY, obj, info, note)

    def answer(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ANSWER, obj, info, note)

    def appear(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.APPEAR, obj, info, note)

    def apply(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.APPLY, obj, info, note)

    def arrive(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ARRIVE, obj, info, note)

    def ask(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ASK, obj, info, note)

    def attack(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ATTACK, obj, info, note)

    def be(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BE, obj, info, note)

    def become(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BECOME, obj, info, note)

    def begin(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BEGIN, obj, info, note)

    def believe(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BELIEVE, obj, info, note)

    def bet(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BET, obj, info, note)

    def bind(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BIND, obj, info, note)

    def borrow(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BORROW, obj, info, note)

    def breaks(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BREAK, obj, info, note)

    def breathe(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BREATHE, obj, info, note)

    def brow(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BROW, obj, info, note)

    def build(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BUILD, obj, info, note)

    def burn(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BURN, obj, info, note)

    def burst(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BURST, obj, info, note)

    def bury(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BURY, obj, info, note)

    def buy(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.BUY, obj, info, note)

    def calculate(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CALCULATE, obj, info, note)

    def call(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CALL, obj, info, note)

    def care(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CARE, obj, info, note)

    def carry(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CARRY, obj, info, note)

    def catch(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CATCH, obj, info, note)

    def change(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CHANGE, obj, info, note)

    def charm(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CHARM, obj, info, note)

    def check(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CHECK, obj, info, note)

    def cheer(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CHEER, obj, info, note)

    def choose(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CHOOSE, obj, info, note)

    def clean(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CLEAN, obj, info, note)

    def click(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CLICK, obj, info, note)

    def climb(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CLIMB, obj, info, note)

    def close(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CLOSE, obj, info, note)

    def clothe(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CLOTHE, obj, info, note)

    def coach(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.COACH, obj, info, note)

    def come(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.COME, obj, info, note)
    
    def command(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.COMMAND, obj, info, note)

    def compare(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.COMPARE, obj, info, note)

    def complete(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.COMPLETE, obj, info, note)

    def confess(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CONFESS, obj, info, note)

    def confuse(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CONFUSE, obj, info, note)

    def contact(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CONTACT, obj, info, note)

    def continues(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CONTINUE, obj, info, note)

    def cooperate(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.COOPERATE, obj, info, note)

    def cough(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.COUGH, obj, info, note)

    def cook(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.COOK, obj, info, note)

    def create(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CREATE, obj, info, note)

    def cry(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CRY, obj, info, note)

    def cut(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.CUT, obj, info, note)

    def dance(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DANCE, obj, info, note)

    def deal(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DEAL, obj, info, note)

    def define(self ,action: str, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DEFINE, obj, info, note)

    def die(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DIE, obj, info, note)

    def dig(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DIG, obj, info, note)

    def disappear(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DISAPPEAR, obj, info, note)

    def disapprove(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DISAPPROVE, obj, info, note)

    def dislike(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DISLIKE, obj, info, note)

    def dispel(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DISPEL, obj, info, note)

    def display(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DISPLAY, obj, info, note)

    def dive(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DIVE, obj, info, note)

    def do(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DO, obj, info, note)

    def doubt(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DOUBT, obj, info, note)

    def draw(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DRAW, obj, info, note)

    def dream(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DREAM, obj, info, note)

    def dress(self , obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DRESS, obj, info, note)

    def drink(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DRINK, obj, info, note)

    def drive(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DRIVE, obj, info, note)

    def drop(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DROP, obj, info, note)

    def dry(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.DRY, obj, info, note)

    def earn(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.EARN, obj, info, note)

    def eat(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.EAT, obj, info, note)

    def educate(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.EDUCATE, obj, info, note)

    def email(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.EMAIL, obj, info, note)

    def employ(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.EMPLOY, obj, info, note)

    def engage(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ENGAGE, obj, info, note)

    def enjoy(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ENJOY, obj, info, note)

    def enter(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ENTER, obj, info, note)

    def envy(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ENVY, obj, info, note)

    def equip(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.EQUIP, obj, info, note)

    def exchange(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.EXCHANGE, obj, info, note)

    def examine(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.EXAMINE, obj, info, note)

    def excite(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.EXCITE, obj, info, note)

    def explore(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.EXPLORE, obj, info, note)

    def face(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FACE, obj, info, note)

    def fail(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FAIL, obj, info, note)

    def fall(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FALL, obj, info, note)

    def feel(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FEEL, obj, info, note)

    def fib(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FIB, obj, info, note)

    def find(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FIND, obj, info, note)

    def fight(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FIGHT, obj, info, note)

    def fill(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FILL, obj, info, note)

    def finish(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FINISH, obj, info, note)

    def fire(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FIRE, obj, info, note)

    def firejob(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FIREJOB, obj, info, note)

    def flash(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FLASH, obj, info, note)

    def float(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FLOAT, obj, info, note)

    def fly(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FLY, obj, info, note)

    def follow(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FOLLOW, obj, info, note)

    def forget(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FORGET, obj, info, note)

    def forgive(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FORGIVE, obj, info, note)

    def freeze(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FREEZE, obj, info, note)

    def fry(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.FRY, obj, info, note)

    def gather(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.GATHER, obj, info, note)

    def gaze(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.GAZE, obj, info, note)

    def give(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.GIVE, obj, info, note)

    def glad(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.GLAD, obj, info, note)

    def go(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.GO, obj, info, note)

    def graduate(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.GRADUATE, obj, info, note)

    def greet(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.GREET, obj, info, note)

    def growl(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.GROWL, obj, info, note)

    def guard(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.GUARD, obj, info, note)

    def guide(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.GUIDE, obj, info, note)

    def hand(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HAND, obj, info, note)

    def handle(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HANDLE, obj, info, note)

    def hang(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HANG, obj, info, note)

    def happen(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HAPPEN, obj, info, note)

    def happy(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HAPPY, obj, info, note)

    def hate(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HATE, obj, info, note)

    def have(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HAVE, obj, info, note)

    def heal(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HEAL, obj, info, note)

    def hear(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HEAR, obj, info, note)

    def help(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HELP, obj, info, note)

    def hide(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HIDE, obj, info, note)

    def hire(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HIRE, obj, info, note)

    def hit(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HIT, obj, info, note)

    def hold(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HOLD, obj, info, note)

    def hope(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HOPE, obj, info, note)

    def hug(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HUG, obj, info, note)

    def hunt(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HUNT, obj, info, note)

    def hurry(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HURRY, obj, info, note)

    def hurt(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.HURT, obj, info, note)

    def ignore(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.IGNORE, obj, info, note)

    def imagine(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.IMAGINE, obj, info, note)

    def injure(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.INJURE, obj, info, note)

    def instrument(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.INSTRUMENT, obj, info, note)

    def introduce(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.INTRODUCE, obj, info, note)

    def invest(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.INVEST, obj, info, note)

    def investigate(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.INVESTIGATE, obj, info, note)

    def invite(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.INVITE, obj, info, note)

    def jog(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.JOG, obj, info, note)

    def join(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.JOIN, obj, info, note)

    def judge(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.JUDGE, obj, info, note)

    def jump(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.JUMP, obj, info, note)

    def keep(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.KEEP, obj, info, note)

    def keyboard(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.KEYBOARD, obj, info, note)

    def kick(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.KICK, obj, info, note)

    def kill(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.KILL, obj, info, note)

    def kiss(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.KISS, obj, info, note)

    def knit(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.KNIT, obj, info, note)

    def knock(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.KNOCK, obj, info, note)

    def know(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.KNOW, obj, info, note)

    def laugh(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LAUGH, obj, info, note)

    def lay(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LAY, obj, info, note)

    def learn(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LEARN, obj, info, note)

    def leave(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LEAVE, obj, info, note)

    def let(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LET, obj, info, note)

    def lie(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LIE, obj, info, note)

    def life(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LIFE, obj, info, note)

    def light(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LIGHT, obj, info, note)

    def listen(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LISTEN, obj, info, note)

    def live(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LIVE, obj, info, note)

    def look(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LOOK, obj, info, note)

    def lookdown(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LOOKDOWN, obj, info, note)

    def lock(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LOCK, obj, info, note)

    def lose(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LOSE, obj, info, note)

    def love(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.LOVE, obj, info, note)
    
    def make(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MAKE, obj, info, note)

    def makeup(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MAKEUP, obj, info, note)

    def manage(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MANAGE, obj, info, note)

    def manufacture(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MANUFACTURE, obj, info, note)

    def maon(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MAON, obj, info, note)

    def mark(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MARK, obj, info, note)

    def marry(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MARRY, obj, info, note)

    def master(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MASTER, obj, info, note)

    def measure(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MEASURE, obj, info, note)

    def meet(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MEET, obj, info, note)

    def melt(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MELT, obj, info, note)

    def mean(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MEAN, obj, info, note)

    def memo(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MEMO, obj, info, note)

    def miss(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MISS, obj, info, note)

    def mix(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MIX, obj, info, note)

    def modify(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MODIFY, obj, info, note)

    def move(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MOVE, obj, info, note)

    def must(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.MUST, obj, info, note)

    def need(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.NEED, obj, info, note)

    def notice(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.NOTICE, obj, info, note)

    def obtain(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.OBTAIN, obj, info, note)

    def occur(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.OCCUR, obj, info, note)

    def open(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.OPEN, obj, info, note)

    def oppose(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.OPPOSE, obj, info, note)

    def overcome(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.OVERCOME, obj, info, note)

    def overflow(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.OVERFLOW, obj, info, note)

    def overlook(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.OVERLOOK, obj, info, note)

    def own(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.OWN, obj, info, note)

    def pack(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PACK, obj, info, note)

    def paint(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PAINT, obj, info, note)

    def passes(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PASS, obj, info, note)

    def pause(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PAUSE, obj, info, note)

    def pay(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PAY, obj, info, note)

    def phone(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PHONE, obj, info, note)

    def play(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PLAY, obj, info, note)

    def plunge(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PLUNGE, obj, info, note)

    def pray(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PRAY, obj, info, note)

    def practice(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PRACTICE, obj, info, note)

    def press(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PRESS, obj, info, note)

    def print(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PRINT, obj, info, note)

    def promise(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PROMISE, obj, info, note)

    def publish(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PUBLISH, obj, info, note)

    def pull(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PULL, obj, info, note)

    def push(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PUSH, obj, info, note)

    def put(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PUT, obj, info, note)

    def punch(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PUNCH, obj, info, note)

    def puzzle(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.PUZZLE, obj, info, note)

    def reach(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.REACH, obj, info, note)

    def react(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.REACT, obj, info, note)

    def read(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.READ, obj, info, note)

    def realize(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.REALIZE, obj, info, note)

    def receive(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.RECEIVE, obj, info, note)

    def recommend(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.RECOMMEND, obj, info, note)

    def reflect(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.REFLECT, obj, info, note)

    def refresh(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.REFRESH, obj, info, note)

    def regard(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.REGARD, obj, info, note)

    def regret(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.REGRET, obj, info, note)

    def release(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.RELEASE, obj, info, note)

    def remember(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.REMEMBER, obj, info, note)

    def rent(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.RENT, obj, info, note)

    def reply(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.REPLY, obj, info, note)

    def rescue(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.RESCUE, obj, info, note)
    
    def rest(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.REST, obj, info, note)

    def returns(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.RETURN, obj, info, note)

    def review(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.REVIEW, obj, info, note)

    def ride(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.RIDE, obj, info, note)

    def ring(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.RING, obj, info, note)

    def rise(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.RISE, obj, info, note)

    def rob(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ROB, obj, info, note)

    def rock(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ROCK, obj, info, note)

    def roll(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.ROLL, obj, info, note)

    def rub(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.RUB, obj, info, note)

    def runs(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.RUN, obj, info, note)

    def sacrifice(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SACRIFICE, obj, info, note)

    def sad(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SAD, obj, info, note)

    def save(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SAVE, obj, info, note)

    def say(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SAY, obj, info, note)

    def scare(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SCARE, obj, info, note)

    def scratch(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SCRATCH, obj, info, note)

    def scream(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SCREAM, obj, info, note)

    def search(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SEARCH, obj, info, note)

    def seat(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SEAT, obj, info, note)

    def see(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SEE, obj, info, note)

    def seek(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SEEK, obj, info, note)

    def seem(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SEEM, obj, info, note)

    def sell(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SELL, obj, info, note)

    def send(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SEND, obj, info, note)

    def separate(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SEPARATE, obj, info, note)

    def set(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SET, obj, info, note)

    def shake(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SHAKE, obj, info, note)

    def share(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SHARE, obj, info, note)

    def shine(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SHINE, obj, info, note)

    def shock(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SHOCK, obj, info, note)

    def shoot(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SHOOT, obj, info, note)

    def show(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SHOW, obj, info, note)

    def sigh(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SIGH, obj, info, note)

    def sign(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SIGN, obj, info, note)

    def sing(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SING, obj, info, note)

    def sink(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SINK, obj, info, note)

    def sit(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SIT, obj, info, note)

    def skate(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SKATE, obj, info, note)

    def sleep(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SLEEP, obj, info, note)

    def slice(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SLICE, obj, info, note)

    def slide(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SLIDE, obj, info, note)

    def slip(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SLIP, obj, info, note)

    def slobber(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SLOBBER, obj, info, note)

    def smell(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SMELL, obj, info, note)

    def smile(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SMILE, obj, info, note)

    def smoke(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SMOKE, obj, info, note)

    def solve(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SOLVE, obj, info, note)

    def sound(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SOUND, obj, info, note)

    def speak(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SPEAK, obj, info, note)

    def spend(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SPEND, obj, info, note)

    def spill(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SPILL, obj, info, note)

    def spin(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SPIN, obj, info, note)

    def split(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SPLIT, obj, info, note)

    def spread(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SPREAD, obj, info, note)

    def squeeze(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SQUEEZE, obj, info, note)

    def stand(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.STAND, obj, info, note)

    def stare(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.STARE, obj, info, note)

    def start(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.START, obj, info, note)

    def steal(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.STEAL, obj, info, note)

    def stick(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.STICK, obj, info, note)

    def stop(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.STOP, obj, info, note)

    def store(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.STORE, obj, info, note)

    def study(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.STUDY, obj, info, note)

    def succeed(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SUCCEED, obj, info, note)

    def suggest(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SUGGEST, obj, info, note)

    def supply(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SUPPLY, obj, info, note)

    def support(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SUPPORT, obj, info, note)

    def suppose(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SUPPOSE, obj, info, note)

    def surprise(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SURPRISE, obj, info, note)

    def surround(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SURROUND, obj, info, note)

    def survive(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SURVIVE, obj, info, note)

    def swim(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SWIM, obj, info, note)

    def swing(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SWING, obj, info, note)

    def sword(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.SWORD, obj, info, note)

    def take(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TAKE, obj, info, note)

    def talk(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TALK, obj, info, note)

    def tap(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TAP, obj, info, note)

    def teach(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TEACH, obj, info, note)

    def thank(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.THANK, obj, info, note)

    def think(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.THINK, obj, info, note)

    def throw(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.THROW, obj, info, note)

    def tie(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TIE, obj, info, note)

    def toss(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TOSS, obj, info, note)

    def touch(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TOUCH, obj, info, note)

    def train(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TRAIN, obj, info, note)

    def transfer(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TRANSFER, obj, info, note)

    def transform(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TRANSFORM, obj, info, note)

    def travel(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TRAVEL, obj, info, note)

    def trip(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TRIP, obj, info, note)

    def tries(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TRY, obj, info, note)

    def trust(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TRUST, obj, info, note)

    def turn(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TURN, obj, info, note)

    def twist(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.TWIST, obj, info, note)

    def understand(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.UNDERSTAND, obj, info, note)

    def unite(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.UNITE, obj, info, note)

    def unlock(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.UNLOCK, obj, info, note)

    def use(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.USE, obj, info, note)

    def vanish(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.VANISH, obj, info, note)

    def visit(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.VISIT, obj, info, note)

    def wait(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WAIT, obj, info, note)

    def wake(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WAKE, obj, info, note)

    def walk(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WALK, obj, info, note)

    def want(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WANT, obj, info, note)

    def warm(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WARM, obj, info, note)

    def waste(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WASTE, obj, info, note)

    def watch(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WATCH, obj, info, note)

    def wave(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WAVE, obj, info, note)

    def wear(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WEAR, obj, info, note)

    def weigh(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WEIGH, obj, info, note)

    def welcome(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WELCOME, obj, info, note)

    def whisper(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WHISPER, obj, info, note)

    def wind(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WIND, obj, info, note)

    def wipe(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WIPE, obj, info, note)

    def wish(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WISH, obj, info, note)

    def wonder(self, obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WONDER, obj, info, note)

    def work(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WORK, obj, info, note)

    def worry(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WORRY, obj, info, note)

    def wry(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WRY, obj, info, note)

    def write(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.WRITE, obj, info, note)

    def yell(self,  obj: _BaseSubject=None, info: str="", note: str=""):
        return self.act(Behavior.YELL, obj, info, note)

