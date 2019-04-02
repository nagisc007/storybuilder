# -*- coding: utf-8 -*-
"""Person class deined.
"""
from .behavior import Behavior
from .subject import _BasePerson


class Person(_BasePerson):
    """Character class.

    Attributes:
        age (int): a age.
        job (str): a job.
        name (str): a name.
        note (str): a short description.
        parent (:obj:`_BasePerson`): a parent.
        selfcall (str): a subject called himself.
        sex (str): a sex.
    """
    CLS_NAME = "_person"
    DEF_SELFCALL = "私"
    
    def __init__(self, name: str, age: int, sex: str, job: str, selfcall: str=DEF_SELFCALL, note: str="", parent: _BasePerson=None):
        """
        Args:
            name (str): a name.
            age (int): a age.
            sex (str): a sex.
            job (str): a job.
            selfcall (str, optional): a name called by myself.
            note (str, optional): a short description.
        """
        super().__init__(name, age, sex, job, note, parent)
        self.selfcall = selfcall

    # methods
    def inherit(self, name: str, age: int, sex: str, job: str, selfcall: str=DEF_SELFCALL, note: str=""):
        return Person(name, age, sex, job, selfcall, note, self)

    # basic actions
    def abandon(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ABANDON, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def absorb(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ABSORB, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def abuse(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ABUSE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def accept(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ACCEPT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def accompany(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ACCOMPANY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def acquire(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ACQUIRE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def add(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ADD, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def adhere(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ADHERE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def adjust(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ADJUST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def admire(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ADMIRE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def admit(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ADMIT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def advise(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ADVISE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def affect(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.AFFECT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def agree(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.AGREE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def aid(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.AID, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def aim(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.AIM, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def allege(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ALLEGE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def allow(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ALLOW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def angry(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ANGRY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def announce(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ANNOUNCE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def annoy(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ANNOY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def answer(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ANSWER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def apologize(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.APOLOGIZE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def appeal(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.APPEAL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def appear(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.APPEAR, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def apply(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.APPLY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def appoint(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.APPOINT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def appriciate(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.APPRICIATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def approach(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.APPROACH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def approve(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.APPROVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def argue(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ARGUE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def arrive(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ARRIVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def arrange(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ARRANGE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def arrest(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ARREST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def ask(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ASK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def assist(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ASSIST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def assume(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ASSUME, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def attach(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ATTACH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def attack(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ATTACK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def attend(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ATTEND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def attract(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ATTRACT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))
    
    def avoid(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.AVOID, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def award(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.AWARD, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bake(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BAKE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def be(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bear(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BEAR, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))
    
    def beat(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BEAT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def become(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BECOME, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def beg(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BEG, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def begin(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BEGIN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def behave(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BEHAVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def believe(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BELIEVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def belong(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BELONG, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bet(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BET, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def betray(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BETRAY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bind(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BIND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def birth(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BIRTH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bite(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BITE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def blame(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BLAME, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bleed(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BLEED, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def blend(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BLEND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bless(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BLESS, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def block(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BLOCK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def boast(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BOAST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def boil(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BOIL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bore(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BORE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def borrow(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BORROW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bother(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BOTHER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bow(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BOW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def breaks(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BREAK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def breathe(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BREATHE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bring(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BRING, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def brow(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BROW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def build(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BUILD, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def burn(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BURN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def burst(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BURST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def bury(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BURY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def buy(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.BUY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def calculate(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CALCULATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def call(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CALL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def care(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CARE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def capture(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CAPTURE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def care(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CARE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def carry(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CARRY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def catch(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CATCH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def change(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CHANGE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def charm(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CHARM, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def chase(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CHASE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cheat(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CHEAT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def check(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CHECK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cheer(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CHEER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def chew(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CHEW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def choose(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CHOOSE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def chop(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CHOP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def claim(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CLAIM, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def clean(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CLEAN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def click(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CLICK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def climb(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CLIMB, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cling(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CLING, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def close(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CLOSE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def clothe(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CLOTHE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def coach(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COACH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def collapse(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COLLAPSE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def collect(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COLLECT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def come(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COME, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))
    
    def command(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COMMAND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def communicate(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COMMUNICATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def compare(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COMPARE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def complete(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COMPLETE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def concern(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CONCERN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def confess(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CONFESS, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def confuse(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CONFUSE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def consider(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CONSIDER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def contact(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CONTACT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def continues(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CONTINUE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cook(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COOK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cool(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COOL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cooperate(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COOPERATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def correct(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CORRECT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cost(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cough(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.COUGH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def create(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CREATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cross(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CROSS, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CRY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cure(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CURE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def curious(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CURIOUS, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def cut(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.CUT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def damage(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DAMAGE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def dance(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DANCE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def dare(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DARE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def deal(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DEAL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def decay(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DECAY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def decide(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DECIDE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def defeat(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DEFEAT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def define(self ,action: str, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DEFINE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def deliver(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DELIVER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def deny(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DENY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def depend(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DEPEND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def destroy(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DESTROY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def determine(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DETERMINE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def die(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DIE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def dig(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DIG, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def disappear(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DISAPPEAR, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def disappoint(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DISAPPOINT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def disapprove(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DISAPPROVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def discover(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DISCOVER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def dislike(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DISLIKE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def dispel(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DISPEL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def display(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DISPLAY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def dive(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DIVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def do(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DO, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def doubt(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DOUBT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def draw(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DRAW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def dream(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DREAM, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def dress(self , a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DRESS, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def drink(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DRINK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def drive(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DRIVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def drop(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DROP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def dry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.DRY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def earn(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EARN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def eat(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EAT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def educate(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EDUCATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def email(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EMAIL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def embarrass(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EMBARRASS, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def employ(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EMPLOY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def encounter(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ENCOUNTER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def engage(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ENGAGE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def enjoy(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ENJOY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def ensure(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ENSURE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def enter(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ENTER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def envy(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ENVY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def equip(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EQUIP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def escape(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ESCAPE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def exchange(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EXCHANGE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def examine(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EXAMINE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def excite(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EXCITE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def exist(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EXIST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def expect(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EXPECT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def explore(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.EXPLORE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def face(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FACE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def fail(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FAIL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def fall(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FALL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def feel(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FEEL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def fib(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FIB, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def find(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FIND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def fight(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FIGHT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def fill(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FILL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def finish(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FINISH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def fire(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FIRE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def firejob(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FIREJOB, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def flash(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FLASH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def float(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FLOAT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def fly(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FLY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def follow(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FOLLOW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def forget(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FORGET, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def forgive(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FORGIVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def freeze(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FREEZE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def fry(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.FRY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def gather(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.GATHER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def gaze(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.GAZE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def give(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.GIVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def glad(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.GLAD, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def go(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.GO, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def graduate(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.GRADUATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def greet(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.GREET, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def growl(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.GROWL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def guard(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.GUARD, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def guide(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.GUIDE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hand(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HAND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def handle(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HANDLE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hang(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HANG, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def happen(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HAPPEN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def happy(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HAPPY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hate(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def have(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HAVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def heal(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HEAL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hear(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HEAR, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def help(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HELP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hesitate(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HESITATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hide(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HIDE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hire(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HIRE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hit(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HIT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hold(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HOLD, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hope(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HOPE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hug(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HUG, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hunt(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HUNT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hurry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HURRY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def hurt(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.HURT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def ignore(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.IGNORE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def illustrate(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ILLUSTRATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def imagine(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.IMAGINE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def imply(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.IMPLY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def injure(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.INJURE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def instrument(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.INSTRUMENT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def interest(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.INTEREST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def introduce(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.INTRODUCE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def invest(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.INVEST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def investigate(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.INVESTIGATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def invite(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.INVITE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def jog(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.JOG, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def join(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.JOIN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def judge(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.JUDGE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def jump(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.JUMP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def keep(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.KEEP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def keyboard(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.KEYBOARD, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def kick(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.KICK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def kill(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.KILL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def kiss(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.KISS, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def knit(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.KNIT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def knock(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.KNOCK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def know(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.KNOW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def laugh(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LAUGH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def lay(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LAY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def learn(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LEARN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def leave(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LEAVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def let(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LET, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def lie(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LIE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def life(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LIFE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def light(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LIGHT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def listen(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LISTEN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def live(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LIVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def look(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LOOK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def lookdown(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LOOKDOWN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def lock(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LOCK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def lose(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LOSE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def love(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.LOVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))
    
    def make(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MAKE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def makeup(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MAKEUP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def manage(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MANAGE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def manufacture(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MANUFACTURE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def maon(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MAON, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def mark(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MARK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def marry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MARRY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def master(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MASTER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def measure(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MEASURE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def meet(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MEET, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def melt(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MELT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def mean(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MEAN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def memo(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MEMO, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def miss(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MISS, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def mix(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MIX, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def modify(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MODIFY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def move(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.MOVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def need(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.NEED, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def notice(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.NOTICE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def obtain(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.OBTAIN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def occur(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.OCCUR, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def open(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.OPEN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def oppose(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.OPPOSE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def overcome(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.OVERCOME, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def overflow(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.OVERFLOW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def overlook(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.OVERLOOK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def own(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.OWN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def pack(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PACK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def paint(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PAINT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def passes(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PASS, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def pause(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PAUSE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def pay(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PAY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def phone(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PHONE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def play(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PLAY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def plunge(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PLUNGE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def pray(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PRAY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def practice(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PRACTICE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def press(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PRESS, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def print(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PRINT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def promise(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PROMISE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def publish(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PUBLISH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def pull(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PULL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def push(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PUSH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def put(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PUT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def punch(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PUNCH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def puzzle(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.PUZZLE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def quarrel(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.QUARREL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def reach(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.REACH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def react(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.REACT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def read(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.READ, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def realize(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.REALIZE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def receive(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RECEIVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def recommend(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RECOMMEND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def reflect(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.REFLECT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def refresh(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.REFRESH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def regard(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.REGARD, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def regret(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.REGRET, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def release(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RELEASE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def remember(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.REMEMBER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def rent(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RENT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def reply(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.REPLY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def rescue(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RESCUE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def research(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RESEARCH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def rest(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.REST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def returns(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RETURN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def review(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.REVIEW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def ride(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RIDE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def ring(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RING, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def rise(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RISE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def rob(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ROB, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def rock(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ROCK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def roll(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.ROLL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def rub(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RUB, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def runs(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.RUN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def sacrifice(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SACRIFICE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def sad(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SAD, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def save(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SAVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def say(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SAY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def scare(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SCARE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def scratch(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SCRATCH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def scream(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SCREAM, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def search(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SEARCH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def seat(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SEAT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def see(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SEE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def seek(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SEEK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def seem(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SEEM, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def sell(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SELL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def send(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SEND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def separate(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SEPARATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def set(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SET, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def shake(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SHAKE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def share(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SHARE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def shine(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SHINE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def shock(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SHOCK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def shoot(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SHOOT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def show(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SHOW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def sigh(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SIGH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def sign(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SIGN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def sing(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SING, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def sink(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SINK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def sit(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SIT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def skate(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SKATE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def sleep(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SLEEP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def slice(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SLICE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def slide(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SLIDE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def slip(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SLIP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def slobber(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SLOBBER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def smell(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SMELL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def smile(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SMILE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def smoke(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SMOKE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def solve(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SOLVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def sound(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SOUND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def speak(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SPEAK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def spend(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SPEND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def spill(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SPILL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def spin(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SPIN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def split(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SPLIT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def spread(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SPREAD, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def squeeze(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SQUEEZE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def stand(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.STAND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def stare(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.STARE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def start(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.START, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def steal(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.STEAL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def stick(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.STICK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def stop(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.STOP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def store(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.STORE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def study(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.STUDY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def succeed(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SUCCEED, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def suggest(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SUGGEST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def supply(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SUPPLY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def support(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SUPPORT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def suppose(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SUPPOSE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def surprise(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SURPRISE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def surround(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SURROUND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def survive(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SURVIVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def swim(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SWIM, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def swing(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SWING, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def sword(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.SWORD, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def take(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TAKE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def talk(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TALK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def tap(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TAP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def teach(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TEACH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def thank(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.THANK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def thinkof(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.THINK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def throw(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.THROW, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def tie(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TIE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def toss(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TOSS, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def touch(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TOUCH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def train(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TRAIN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def transfer(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TRANSFER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def transform(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TRANSFORM, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def travel(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TRAVEL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def trip(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TRIP, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def tries(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TRY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def trust(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TRUST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def turn(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TURN, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def twist(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.TWIST, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def understand(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.UNDERSTAND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def unite(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.UNITE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def unlock(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.UNLOCK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def use(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.USE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def vanish(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.VANISH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def visit(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.VISIT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def wait(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WAIT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def wake(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WAKE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def walk(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WALK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def wantto(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WANT, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def warm(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WARM, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def waste(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WASTE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def watch(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WATCH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def wave(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WAVE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def wear(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WEAR, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def weigh(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WEIGH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def welcome(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WELCOME, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def whisper(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WHISPER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def wind(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WIND, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def wipe(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WIPE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def wish(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WISH, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def wonder(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WONDER, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def work(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WORK, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def worry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WORRY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def wry(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WRY, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def write(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.WRITE, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def yell(self,  a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        return self.act(Behavior.YELL, self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

