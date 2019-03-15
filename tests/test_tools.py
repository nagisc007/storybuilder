# -*- coding: utf-8 -*-
"""Test for tools.py
"""

import unittest

from builder.acttypes import ActType, Behavior
from builder.base import Act, Title, Stage, DayTime
from builder.person import Person
from builder.tools import build_action_strings
from builder.tools import build_description_strings
from builder.tools import output
from builder.tools import output_md
from builder.tools import _action_info_builded
from builder.tools import _description_selected

class TestTools(unittest.TestCase):

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student", "he is a man")
        self.hanako = Person("Hanako", 17, "female", "student", "she is so cute")
        self.classroom = Stage("Classroom", "desk and chair")
        self.loveday = DayTime("Love day", 4, 10, 2019, 10, "both meet day")
        self.test_story = (
                Title("Test story 01", "this is a test"),
                self.taro.sleep("sleeping"),
                self.hanako.come("come in"),
                self.classroom.look("bother space"),
                self.loveday.look("morning"),
                )
        self.test_story_for_desc = (
                Title("Test story 01", "this is a test").desc("good test"),
                self.taro.sleep("sleeping").desc("good sleeping"),
                self.hanako.come("come in").desc("come in the room"),
                self.classroom.look("bother space").desc("all students sit their chair"),
                self.loveday.look("morning").desc("bother morning"),
                )

    def test__description_selected(self):
        normal_act = Act(self.taro, ActType.ACT, Behavior.GO, "go to room")

        self.assertEqual(_description_selected(normal_act), "go to room")

    def test__description_selected_with_description(self):
        normal_act = Act(self.taro, ActType.ACT, Behavior.GO, "go to room")
        act_with_desc = normal_act.desc("walk so slowly to the room")

        self.assertEqual(_description_selected(act_with_desc), "walk so slowly to the room")

    def test_build_action_strings(self):
        actions = build_action_strings(self.test_story)
        
        self.assertEqual(actions[0], "\n## Test story 01\n\n")
        self.assertEqual(actions[1], "Taro - 眠る: sleeping\n")
        self.assertEqual(actions[2], "Hanako - 来る: come in\n")
        self.assertEqual(actions[3], "Classroom - 描写: bother space\n")
        self.assertEqual(actions[4], "Love day - 描写: morning\n")

    def test_build_description_strings(self):
        descs = build_description_strings(self.test_story_for_desc)

        self.assertEqual(descs[0], "\n## Test story 01 -- good test\n\n")
        self.assertEqual(descs[1], "good sleeping。\n")
        self.assertEqual(descs[2], "come in the room。\n")
        self.assertEqual(descs[3], "all students sit their chair。\n")
        self.assertEqual(descs[4], "bother morning。\n")

    def test_output(self):
        """TODO: in preparation
        """
        pass

    def test_output_md(self):
        """TODO: in preparation
        """
        pass

