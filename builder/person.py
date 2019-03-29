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
    def accept(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ACCEPT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def acquire(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ACQUIRE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def add(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ADD, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def advise(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ADVISE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def agree(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.AGREE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def aim(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.AIM, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def angry(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ANGRY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def answer(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ANSWER, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def appear(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.APPEAR, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def apply(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.APPLY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def arrive(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ARRIVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def ask(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ASK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def attack(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ATTACK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def be(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def become(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BECOME, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def begin(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BEGIN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def believe(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BELIEVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def bet(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BET, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def bind(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BIND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def borrow(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BORROW, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def breaks(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BREAK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def breathe(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BREATHE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def brow(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BROW, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def build(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BUILD, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def burn(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BURN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def burst(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BURST, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def bury(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BURY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def buy(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.BUY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def calculate(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CALCULATE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def call(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CALL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def care(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CARE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def carry(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CARRY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def catch(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CATCH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def change(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CHANGE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def charm(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CHARM, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def check(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CHECK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def cheer(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CHEER, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def choose(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CHOOSE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def clean(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CLEAN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def click(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CLICK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def climb(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CLIMB, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def close(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CLOSE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def clothe(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CLOTHE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def coach(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.COACH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def come(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.COME, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)
    
    def command(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.COMMAND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def compare(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.COMPARE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def complete(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.COMPLETE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def confess(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CONFESS, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def confuse(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CONFUSE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def contact(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CONTACT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def continues(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CONTINUE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def cooperate(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.COOPERATE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def cough(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.COUGH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def cook(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.COOK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def create(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CREATE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def cry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CRY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def cut(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.CUT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def dance(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DANCE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def deal(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DEAL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def define(self ,action: str, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DEFINE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def die(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DIE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def dig(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DIG, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def disappear(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DISAPPEAR, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def disapprove(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DISAPPROVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def dislike(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DISLIKE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def dispel(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DISPEL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def display(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DISPLAY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def dive(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DIVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def do(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DO, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def doubt(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DOUBT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def draw(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DRAW, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def dream(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DREAM, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def dress(self , a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DRESS, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def drink(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DRINK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def drive(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DRIVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def drop(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DROP, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def dry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.DRY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def earn(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.EARN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def eat(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.EAT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def educate(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.EDUCATE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def email(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.EMAIL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def employ(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.EMPLOY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def engage(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ENGAGE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def enjoy(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ENJOY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def enter(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ENTER, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def envy(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ENVY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def equip(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.EQUIP, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def exchange(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.EXCHANGE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def examine(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.EXAMINE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def excite(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.EXCITE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def explore(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.EXPLORE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def face(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FACE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def fail(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FAIL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def fall(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FALL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def feel(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FEEL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def fib(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FIB, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def find(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FIND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def fight(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FIGHT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def fill(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FILL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def finish(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FINISH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def fire(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FIRE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def firejob(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FIREJOB, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def flash(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FLASH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def float(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FLOAT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def fly(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FLY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def follow(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FOLLOW, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def forget(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FORGET, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def forgive(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FORGIVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def freeze(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FREEZE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def fry(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.FRY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def gather(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.GATHER, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def gaze(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.GAZE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def give(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.GIVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def glad(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.GLAD, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def go(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.GO, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def graduate(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.GRADUATE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def greet(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.GREET, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def growl(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.GROWL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def guard(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.GUARD, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def guide(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.GUIDE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hand(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HAND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def handle(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HANDLE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hang(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HANG, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def happen(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HAPPEN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def happy(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HAPPY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hate(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HATE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def have(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HAVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def heal(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HEAL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hear(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HEAR, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def help(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HELP, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hide(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HIDE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hire(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HIRE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hit(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HIT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hold(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HOLD, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hope(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HOPE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hug(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HUG, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hunt(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HUNT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hurry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HURRY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def hurt(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.HURT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def ignore(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.IGNORE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def imagine(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.IMAGINE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def injure(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.INJURE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def instrument(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.INSTRUMENT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def introduce(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.INTRODUCE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def invest(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.INVEST, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def investigate(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.INVESTIGATE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def invite(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.INVITE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def jog(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.JOG, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def join(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.JOIN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def judge(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.JUDGE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def jump(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.JUMP, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def keep(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.KEEP, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def keyboard(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.KEYBOARD, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def kick(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.KICK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def kill(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.KILL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def kiss(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.KISS, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def knit(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.KNIT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def knock(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.KNOCK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def know(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.KNOW, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def laugh(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LAUGH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def lay(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LAY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def learn(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LEARN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def leave(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LEAVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def let(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LET, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def lie(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LIE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def life(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LIFE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def light(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LIGHT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def listen(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LISTEN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def live(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LIVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def look(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LOOK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def lookdown(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LOOKDOWN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def lock(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LOCK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def lose(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LOSE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def love(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.LOVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)
    
    def make(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MAKE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def makeup(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MAKEUP, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def manage(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MANAGE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def manufacture(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MANUFACTURE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def maon(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MAON, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def mark(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MARK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def marry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MARRY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def master(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MASTER, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def measure(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MEASURE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def meet(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MEET, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def melt(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MELT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def mean(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MEAN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def memo(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MEMO, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def miss(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MISS, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def mix(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MIX, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def modify(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MODIFY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def move(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.MOVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def need(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.NEED, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def notice(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.NOTICE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def obtain(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.OBTAIN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def occur(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.OCCUR, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def open(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.OPEN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def oppose(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.OPPOSE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def overcome(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.OVERCOME, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def overflow(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.OVERFLOW, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def overlook(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.OVERLOOK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def own(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.OWN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def pack(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PACK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def paint(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PAINT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def passes(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PASS, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def pause(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PAUSE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def pay(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PAY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def phone(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PHONE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def play(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PLAY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def plunge(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PLUNGE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def pray(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PRAY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def practice(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PRACTICE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def press(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PRESS, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def print(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PRINT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def promise(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PROMISE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def publish(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PUBLISH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def pull(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PULL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def push(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PUSH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def put(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PUT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def punch(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PUNCH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def puzzle(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.PUZZLE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def reach(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.REACH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def react(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.REACT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def read(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.READ, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def realize(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.REALIZE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def receive(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.RECEIVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def recommend(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.RECOMMEND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def reflect(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.REFLECT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def refresh(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.REFRESH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def regard(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.REGARD, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def regret(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.REGRET, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def release(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.RELEASE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def remember(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.REMEMBER, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def rent(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.RENT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def reply(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.REPLY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def rescue(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.RESCUE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)
    
    def rest(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.REST, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def returns(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.RETURN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def review(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.REVIEW, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def ride(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.RIDE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def ring(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.RING, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def rise(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.RISE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def rob(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ROB, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def rock(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ROCK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def roll(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.ROLL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def rub(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.RUB, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def runs(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.RUN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def sacrifice(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SACRIFICE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def sad(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SAD, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def save(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SAVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def say(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SAY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def scare(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SCARE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def scratch(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SCRATCH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def scream(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SCREAM, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def search(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SEARCH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def seat(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SEAT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def see(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SEE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def seek(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SEEK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def seem(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SEEM, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def sell(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SELL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def send(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SEND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def separate(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SEPARATE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def set(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SET, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def shake(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SHAKE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def share(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SHARE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def shine(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SHINE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def shock(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SHOCK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def shoot(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SHOOT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def show(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SHOW, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def sigh(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SIGH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def sign(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SIGN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def sing(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SING, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def sink(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SINK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def sit(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SIT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def skate(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SKATE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def sleep(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SLEEP, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def slice(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SLICE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def slide(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SLIDE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def slip(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SLIP, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def slobber(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SLOBBER, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def smell(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SMELL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def smile(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SMILE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def smoke(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SMOKE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def solve(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SOLVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def sound(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SOUND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def speak(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SPEAK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def spend(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SPEND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def spill(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SPILL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def spin(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SPIN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def split(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SPLIT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def spread(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SPREAD, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def squeeze(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SQUEEZE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def stand(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.STAND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def stare(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.STARE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def start(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.START, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def steal(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.STEAL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def stick(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.STICK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def stop(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.STOP, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def store(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.STORE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def study(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.STUDY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def succeed(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SUCCEED, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def suggest(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SUGGEST, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def supply(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SUPPLY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def support(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SUPPORT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def suppose(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SUPPOSE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def surprise(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SURPRISE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def surround(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SURROUND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def survive(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SURVIVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def swim(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SWIM, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def swing(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SWING, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def sword(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.SWORD, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def take(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TAKE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def talk(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TALK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def tap(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TAP, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def teach(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TEACH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def thank(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.THANK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def thinkof(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.THINK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def throw(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.THROW, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def tie(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TIE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def toss(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TOSS, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def touch(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TOUCH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def train(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TRAIN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def transfer(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TRANSFER, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def transform(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TRANSFORM, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def travel(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TRAVEL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def trip(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TRIP, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def tries(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TRY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def trust(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TRUST, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def turn(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TURN, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def twist(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.TWIST, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def understand(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.UNDERSTAND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def unite(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.UNITE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def unlock(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.UNLOCK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def use(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.USE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def vanish(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.VANISH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def visit(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.VISIT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def wait(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WAIT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def wake(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WAKE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def walk(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WALK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def wantto(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WANT, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def warm(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WARM, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def waste(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WASTE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def watch(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WATCH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def wave(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WAVE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def wear(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WEAR, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def weigh(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WEIGH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def welcome(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WELCOME, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def whisper(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WHISPER, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def wind(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WIND, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def wipe(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WIPE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def wish(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WISH, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def wonder(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WONDER, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def work(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WORK, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def worry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WORRY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def wry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WRY, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def write(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.WRITE, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

    def yell(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None, info: str="", note: str=""):
        return self.act(Behavior.YELL, (a, about, asa, at, by, fo, frm, of, on, to, wth), info, note)

