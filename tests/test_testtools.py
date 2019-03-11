# -*- coding: utf-8 -*-
"""Test for testtools.py
"""
import unittest

from builder.acttypes import Behavior
from builder.base import Title, Person, Stage, DayTime
from builder.testtools import checked_if_all_actions
from builder.testtools import checked_has_basic_info


class TestCheckTools(unittest.TestCase):

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student", "he is a man")
        self.hanako = Person("Hanako", 17, "female", "student", "she is so cute")
        self.classroom = Stage("Classroom", "desk and chair")
        self.loveday = DayTime("Love day", 4, 10, 2019, 10, "both meet day")
        self.test_story = (
                Title("Test story 01", "this is a test"),
                self.taro.act("sleeping", Behavior.SLEEP),
                self.taro.want("find a girl friend"),
                self.taro.think("boring"),
                self.hanako.act("come in", Behavior.COME),
                self.hanako.look("transfer student"),
                self.classroom.look("bother space"),
                self.loveday.look("morning"),
                self.taro.result("meet Hanako"),
                )

    def test_checked_if_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.test_story))

    def test_checked_has_basic_info(self):
        self.assertTrue(
                checked_has_basic_info(self, self.test_story,
                                        self.taro, self.hanako,
                                        "boring", "transfer"))
