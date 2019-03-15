# -*- coding: utf-8 -*-
"""Test for testtools.py
"""
import unittest

from builder.acttypes import Behavior
from builder.base import Title, Stage, DayTime
from builder.person import Person
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
                self.taro.think("find a girl friend"),
                self.taro.think("boring"),
                self.hanako.come("in the room"),
                self.hanako.look("transfer student"),
                self.classroom.look("bother space"),
                self.loveday.look("morning"),
                self.taro.think("meet Hanako"),
                )

    def test_checked_if_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.test_story))

    def test_checked_has_basic_info(self):
        self.assertTrue(
                checked_has_basic_info(
                    self, self.test_story, self.taro, self.hanako,
                    "find", "boring", "transfer", "meet"))

    def test_checked_has_basic_info_why_by_tell(self):
        why_tell_story = self.test_story + (self.taro.tell("bored"),)

        self.assertTrue(
                checked_has_basic_info(
                    self, why_tell_story, self.taro, self.hanako,
                    "find", "bored", "transfer", "meet"
                    ))
