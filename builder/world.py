# -*- coding: utf-8 -*-
"""Define class that world management.
"""
from typing import Any
from . import assertion
from .basedata import BaseData
from .chapter import Chapter
from .episode import Episode
from .story import Story
from .scene import Scene
from .person import Person
from .chara import Chara
from .stage import Stage
from .item import Item
from .day import Day
from .time import Time
from .item import Item
from .word import Word
from . import action as ac
from .flag import Flag
from .combaction import CombAction


class UtilityDict(dict):
    """Useful dictionary class.
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class World(UtilityDict):
    """World class.
    """
    DEF_PRIORITY = ac.Action.DEF_PRIORITY
    MAX_PRIORITY = ac.Action.MAX_PRIORITY
    MIN_PRIORITY = ac.Action.MIN_PRIORITY

    def __init__(self):
        super().__init__()
        self.day = UtilityDict()
        self.item = UtilityDict()
        self.stage = UtilityDict()
        self.time = UtilityDict()
        self.word = UtilityDict()
        # TODO: priorityを先か後で調整できるようにする
        self._priority = World.DEF_PRIORITY

    # tag
    def br(self):
        return self

    def comment(self):
        return self

    def hr(self):
        return self

    # creations
    def chapter(self, *args, **kwargs):
        '''To create a chapter.
        '''
        return Chapter(*args, **kwargs)

    def episode(self, *args, **kwargs):
        '''To create a episode.
        '''
        return Episode(*args, **kwargs)

    def scene(self, *args, **kwargs):
        '''To create a scene.
        '''
        return Scene(*args, **kwargs)

    def story(self, *args, **kwargs):
        '''To create a story.
        '''
        return Story(*args, **kwargs)

    # db management
    def append_chara(self, key: str, val: Any):
        return self._appendOne(key, val, self, Chara)

    def append_day(self, key: str, val: Any):
        return self._appendOne(key, val, self.day, Day)

    def append_item(self, key: str, val: Any):
        return self._appendOne(key, val, self.item, Item)

    def append_person(self, key: str, val: Any):
        return self._appendOne(key, val, self, Person)

    def append_stage(self, key: str, val: Any):
        return self._appendOne(key, val, self.stage, Stage)

    def append_time(self, key: str, val: Any):
        return self._appendOne(key, val, self.time, Time)

    def append_word(self, key: str, val: Any):
        return self._appendOne(key, val, self.word, Word)

    def set_charas(self, charas: list):
        for v in assertion.is_list(charas):
            self.append_chara(v[0], v[1:])
        return self

    def set_days(self, days: list):
        for v in assertion.is_list(days):
            self.append_day(v[0], v[1:])
        return self

    def set_items(self, items: list):
        for v in assertion.is_list(items):
            self.append_item(v[0], v[1:])
        return self

    def set_persons(self, persons: list):
        for v in assertion.is_list(persons):
            self.append_person(v[0], v[1:])
        return self

    def set_stages(self, stages: list):
        for v in assertion.is_list(stages):
            self.append_stage(v[0], v[1:])
        return self

    def set_times(self, times: list):
        for v in assertion.is_list(times):
            self.append_time(v[0], v[1:])
        return self

    def set_words(self, words: list):
        for v in assertion.is_list(words):
            self.append_word(v[0], v[1:])
        return self

    def set_db(self, persons: list, charas: list,
            stages: list, days: list, times: list,
            items: list, words: list):
        if persons:
            self.set_persons(persons)
        if charas:
            self.set_charas(charas)
        if items:
            self.set_items(items)
        if stages:
            self.set_stages(stages)
        if days:
            self.set_days(days)
        if times:
            self.set_times(times)
        if words:
            self.set_words(words)
        return self

    # controls
    def elapsed(self, time: Time, hour: int=0, min: int=0):
        '''To elapse a time.
        '''
        return Time(hour=hour + time.hour, min=min + time.min)

    def passed(self, base: Day, mon: int=0, day: int=0, year: int=0):
        '''To pass a day.
        '''
        return Day(mon=mon + base.mon, day=day + base.day, year=year + base.year)

    # actions
    def combine(self, *args):
        return CombAction(*args)

    def act(self, subject: [str, Person, Chara, None],
            outline: str=""):
        return ac.Action(subject, outline, act_type=ac.ActType.ACT)

    def be(self, subject: [Person, Chara, None],
            outline: str=""):
        return ac.Action(subject, outline, act_type=ac.ActType.BE)

    def come(self, subject: [Person, Chara, None],
            outline: str=""):
        return ac.Action(subject, outline, act_type=ac.ActType.COME)

    def go(self, subject: [Person, Chara, None],
            outline: str=""):
        return ac.Action(subject, outline, act_type=ac.ActType.GO)

    def have(self, subject: [Person, Chara, None],
            outline: str=""):
        return ac.Action(subject, outline, act_type=ac.ActType.HAVE)

    def hear(self, subject: [Person, Chara, None],
            outline: str=""):
        return ac.Action(subject, outline, act_type=ac.ActType.HEAR)

    def look(self, subject: [Person, Chara, None],
            outline: str=""):
        return ac.Action(subject, outline, act_type=ac.ActType.LOOK)

    def move(self, subject: [Person, Chara, None],
            outline: str=""):
        return ac.Action(subject, outline, act_type=ac.ActType.MOVE)

    def talk(self, subject: [Person, Chara, None],
            outline: str=""):
        return ac.Action(subject, outline, act_type=ac.ActType.TALK)

    def think(self, subject: [Person, Chara, None],
            outline: str=""):
        return ac.Action(subject, outline, act_type=ac.ActType.THINK)

    # build
    def build(self, val: Story):
        '''To build this story world.
        '''
        from .buildtool import Build
        bd = Build(val, self)
        return bd.output_story()

    # private
    def _appendOne(self, key: str, val: Any, body: [UtilityDict, dict],
            datatype: BaseData):
        if body is self:
            self.__setitem__(assertion.is_str(key), self._dataFrom(val, datatype))
        else:
            assertion.is_instance(body, UtilityDict).__setitem__(
                    assertion.is_str(key), self._dataFrom(val, datatype))
        return self

    def _dataFrom(self, val: Any, datatype: BaseData):
        return val if isinstance(val, datatype) else datatype(*val)
