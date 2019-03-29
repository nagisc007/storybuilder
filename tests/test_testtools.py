# -*- coding: utf-8 -*-
"""Test for testtools.py
"""
import unittest

from builder.base import Stage, DayTime, Master, something
from builder.person import Person
import builder.testtools as testtools


class BasicMethodTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: testtools.py ****")

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
                self.taro.meet(self.hanako, info="a cute girl").set_deflag(1),
                self.hanako.fall(self.taro, info="love").negative(),
                )

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story, self.taro, self.hanako))

    def test_has_outline_infos(self):
        what_act = self.taro.tell(info="Boring")
        why_act = self.taro.lose(info="love")
        how_act = self.taro.meet(something(),info="girl")
        res_act = self.hanako.fall(self.taro, info="love").negative()
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            what_act, why_act, how_act, res_act))

    def test_followed_all_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))

    def test__is_near_eq_at_objects(self):
        some = something()
        data_set = [
                (self.taro.meet(self.hanako), self.taro.meet(self.hanako), True),
                (self.taro.meet(self.hanako), self.taro.meet(), False),
                (self.taro.meet(some), self.taro.meet(self.hanako), True),
                (self.taro.meet(self.hanako), self.taro.meet(some), True),
                (self.taro.meet(some), self.taro.meet(), False),
                (self.taro.meet(), self.taro.meet(some), False),
                ]
        for a, b, expected in data_set:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(testtools._is_near_eq_at_objects(a, b), expected)

    def test__is_near_eq_at_subjects(self):
        some = something()
        data_set = [
                (self.taro.explain("test"), self.hanako.explain("test"), False),
                (self.taro.explain("test"), self.taro.tell("test"), True),
                (some.explain("test"), self.taro.explain("test"), True),
                (self.taro.explain("test"), some.explain("test"), True),
                ]
        for a, b, expected in data_set:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(testtools._is_near_eq_at_subjects(a, b), expected)
