# -*- coding: utf-8 -*-
"""Test for testtools.py
"""
import unittest

from builder.base import Stage, DayTime, Master
from builder.person import Person
import builder.testtools as testtools


class BasicMethodTest(unittest.TestCase):

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student", "me", "a man")
        self.hanako = Person("Hanako", 17, "female", "student", "me", "a cute girl")
        self.day = DayTime("A day", 10, 5, 2019, 12)
        self.room = Stage("Classroom")
        self.sm = Master("The test", "a test story")
        self.story = self.sm.story("THE TEST",
                self.sm.comment("-- the test start --"),
                self.day.explain("warming afternoon"),
                self.room.explain("a silent room"),
                self.taro.tell("I am").set_flag("taro"),
                self.taro.tell("Boring").set_flag(1),
                self.hanako.come(info="in class"),
                self.taro.lose(info="love").set_deflag("taro"),
                self.taro.meet(info="a cute girl").set_deflag(1),
                self.hanako.fall(self.taro, info="love").negative(),
                )

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story, self.taro, self.hanako))

    def test_has_outline_infos(self):
        what_act = self.taro.tell(info="Boring")
        why_act = self.taro.lose(info="love")
        how_act = self.taro.meet(info="girl")
        res_act = self.hanako.fall(self.taro, info="love").negative()
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            what_act, why_act, how_act, res_act))

    def test_followed_all_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))
