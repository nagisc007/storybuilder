# -*- coding: utf-8 -*-
"""Utility story DB class.
"""
from .sbutils import assert_isstr
from .person import Person
from .subject import DayTime, Item, Stage, Word


# classes
class StoryDB(dict):
    """Database for a story.

    Attributes:
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    def __init__(self, charas: list, stages: list, days: list, items: list, words: list):
        for c in charas:
            self.append_chara(c[0], c[1:])
        for s in stages:
            self.append_stage(s[0], s[1:])
        for d in days:
            self.append_day(d[0], d[1:])
        for i in items:
            self.append_item(i[0], i[1:])
        for w in words:
            self.append_word(w[0], w[1:])

    def _setattr_with_prefix_if(self, pref: str, key: str, data):
        if key in self.keys():
            self.__setitem__(pref + key, data)
        else:
            self.__setitem__(key, data)

    def append_chara(self, key: str, chara):
        assert_isstr(key)

        data = chara if isinstance(chara, Person) else Person(*chara)
        self._setattr_with_prefix_if('p_', key, data)
        return self

    def append_day(self, key: str, day):
        assert_isstr(key)

        data = day if isinstance(day, DayTime) else DayTime(*day)
        self._setattr_with_prefix_if('d_', key, data)
        return self

    def append_item(self, key: str, item):
        assert_isstr(key)

        data = item if isinstance(item, Item) else Item(*item)
        self._setattr_with_prefix_if('i_', key, data)
        return self

    def append_stage(self, key: str, stage):
        assert_isstr(key)

        data = stage if isinstance(stage, Stage) else Stage(*stage)
        self._setattr_with_prefix_if('s_', key, data)
        return self

    def append_word(self, key: str, word):
        assert_isstr(key)

        data = word if isinstance(word, Word) else Word(*word)
        self._setattr_with_prefix_if('w_', key, data)
        return self

