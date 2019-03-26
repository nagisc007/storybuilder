# -*- coding: utf-8 -*-
"""Test for tools.py
"""

import unittest
import os
import sys
from io import StringIO

from builder.acttypes import LangType
from builder.base import Master
from builder.person import Person
import builder.tools as tools


class BasicMethodTest(unittest.TestCase):

    def setUp(self):
        self.sm = Master("test story")
        self.taro = Person("Taro", 17, "male", "student", "me")
        self.hanako = Person("Hanako", 17, "female", "student", "me")
        self.story = self.sm.story(
                "Taro and Hanako",
                self.hanako.come(info="in room").desc("a cute girl come in"),
                self.taro.tell("wow", self.hanako).desc("Nice to meet you"),
                self.hanako.tell("like").negative().desc("I'm not fine"),
                lang=LangType.ENG,
                )
        self.story_j = self.sm.story(
                "太郎と花子",
                self.hanako.come(info="部屋").desc("可愛い少女"),
                self.taro.tell("ああ").desc("よう"),
                self.hanako.tell("好き").negative().desc("全然")
                )
        self.test_file = "test_file"

    def test_build_to_story(self):
        pass

    def test_options_parsed(self):
        pass

    def test_output_story(self):
        pass

    def test__output_story_to_console(self):
        tmp_stdout, sys.stdout = sys.stdout, StringIO()
        self.assertTrue(tools._output_story_to_console(["# test story", "test"], False))
        self.assertEqual(
                sys.stdout.getvalue(),
                "# test story\ntest\n"
                )
        # fall back
        sys.stdout = tmp_stdout


    def test__output_story_to_file_as_action(self):
        self.assertTrue(tools._output_story_to_file(["# test story", "test"], self.test_file, True, False))
        build_path = os.path.join(os.getcwd(), "build/{}_a.md".format(self.test_file))
        self.assertTrue(os.path.exists(build_path))


    def test__output_story_to_file_as_description(self):
        self.assertTrue(tools._output_story_to_file(["# test story", "test"], self.test_file, False, False))
        build_path = os.path.join(os.getcwd(), "build/{}.md".format(self.test_file))
        self.assertTrue(os.path.exists(build_path))


    def test__story_data_converted(self):
        self.assertEqual(tools._story_data_converted(self.story, True, False),
                ["# Taro and Hanako\n", "- Hanako  :来る()    /in room",
                     "- Taro    :台詞(Hanako)/ \"wow\" ",
                    "- Hanako  :~~台詞~~()/ \"like\" "])


    def test__story_converted_as_action(self):
        self.assertEqual(tools._story_converted_as_action(self.story, False),
                ["# Taro and Hanako\n", "- Hanako  :来る()    /in room",
                    "- Taro    :台詞(Hanako)/ \"wow\" ",
                    "- Hanako  :~~台詞~~()/ \"like\" "])


    def test__story_converted_as_action_jpn(self):
        self.assertEqual(tools._story_converted_as_action(self.story_j, False),
                ["# 太郎と花子\n", "- Hanako:来る()　　/部屋",
                    "- Taro　　:台詞()　　/「ああ」",
                    "- Hanako:~~台詞~~()/「好き」"])


    def test__story_converted_as_action_in_group(self):
        self.assertEqual(tools._story_converted_as_action_in_group(self.story, self.story.group_type, 1, False),
                ["# Taro and Hanako\n", "- Hanako  :来る()    /in room",
                    "- Taro    :台詞(Hanako)/ \"wow\" ",
                    "- Hanako  :~~台詞~~()/ \"like\" "])


    def test__story_converted_as_description(self):
        self.assertEqual(tools._story_converted_as_description(self.story, False),
                ["# Taro and Hanako\n",
                    " a cute girl come in. ",
                    ' "Nice to meet you" ',
                    ' "I\'m not fine" '])


    def test__story_converted_as_description_in_group(self):
        self.assertEqual(tools._story_converted_as_description_in_group(self.story, self.story.group_type, 1, False),
                ["# Taro and Hanako\n",
                    " a cute girl come in. ",
                    ' "Nice to meet you" ',
                    ' "I\'m not fine" '])

