# -*- coding: utf-8 -*-
"""Test for tools.py
"""

import unittest
import os
import sys
from io import StringIO

from builder.acttypes import LangType
from builder.base import Master, Word
from builder.person import Person
import builder.tools as tools


class BasicClassTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: tools.py - classes ****")

    def setUp(self):
        self.db = tools.StoryDB([], [], [], [], [])

    def test_create_class(self):
        self.assertIsInstance(self.db, tools.StoryDB)

    def test_attr_append_chara(self):
        data = [
                ("taro", "Taro", 17, "male", "student", "me", "a man", "he is a funny"),
                ("hanako", "Hanako", 17, "female", "student", "me", "a girl", "she is a cute"),
                ("taro", "Kotaro", 40, "male", "lower", "me", "a parent", "he has a hige")
                ]
        for k, name, age, sex, job, slf, info, note in data:
            with self.subTest(k=k, name=name, age=age, sex=sex, job=job, slf=slf, info=info, note=note):
                self.db.append_chara(k, (name, age, sex, job, slf, info, note))
                key = k if name != "Kotaro" else "p_taro"
                self.assertEqual(self.db[key].name, name)
                self.assertEqual(self.db[key].age, age)
                self.assertEqual(self.db[key].sex, sex)
                self.assertEqual(self.db[key].job, job)
                self.assertEqual(self.db[key].selfcall, slf)
                self.assertEqual(self.db[key].info, info)
                self.assertEqual(self.db[key].note, note)

    def test_attr_append_word(self):
        data = [
                ("w", "word", "a word", "note: word"),
                ("t", "test", "a test", "note: test"),
                ("w", "word2", "a word2", "note: word2")
                ]
        for k, name, info, note in data:
            with self.subTest(k=k, name=name, info=info, note=note):
                self.db.append_word(k, (name, info, note))
                key = k if name != "word2" else "w_w"
                self.assertEqual(self.db[key].name, name)
                self.assertEqual(self.db[key].info, info)
                self.assertEqual(self.db[key].note, note)

    def test_attr_append_word_lacked(self):
        data0 = ("w", "word")
        data1 = ("t", "test", "a test")
        self.db.append_word(data0[0], data0[1:])
        self.db.append_word(data1[0], data1[1:])
        self.assertEqual(self.db.w.name, "word")
        self.assertEqual(self.db.w.info, "")
        self.assertEqual(self.db.w.note, "")
        self.assertEqual(self.db.t.name, "test")
        self.assertEqual(self.db.t.info, "a test")
        self.assertEqual(self.db.t.note, "")

    def test_attr_append_word_using_cls(self):
        self.db.append_word("w", Word("word"))
        self.assertEqual(self.db.w.name, "word")
        self.assertEqual(self.db.w.info, "")
        self.assertEqual(self.db.w.note, "")


class BasicMethodTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: tools.py - methods ****")

    def setUp(self):
        self.sm = Master("test story")
        self.taro = Person("Taro", 17, "male", "student", "me")
        self.hanako = Person("Hanako", 17, "female", "student", "me")
        self.masao = Person("Masao", 17, "male", "student", "me")
        self.story = self.sm.story(
                "Taro and Hanako",
                self.hanako.come(info="in room").desc("a cute girl come in"),
                self.taro.tell("wow", to=self.hanako).desc("Nice to meet you"),
                self.hanako.tell("like").negative().desc("I'm not fine"),
                lang=LangType.ENG,
                )
        self.story_j = self.sm.story(
                "太郎と花子",
                self.hanako.come(info="部屋").desc("可愛い少女"),
                self.taro.tell("ああ").desc("よう"),
                self.hanako.tell("好き", to=self.taro, wth=self.masao).negative().desc("全然")
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
        self.assertEqual(tools._story_data_converted(self.story, True, 0, False),
                ["# Taro and Hanako\n", "- Hanako  :来る()    /in room",
                     "- Taro    :台詞(Hanako)/ \"wow\" ",
                    "- Hanako  :~~台詞~~()/ \"like\" "])


    def test__story_converted_as_action(self):
        self.assertEqual(tools._story_converted_as_action(self.story, 0, False),
                ["# Taro and Hanako\n", "- Hanako  :来る()    /in room",
                    "- Taro    :台詞(Hanako)/ \"wow\" ",
                    "- Hanako  :~~台詞~~()/ \"like\" "])


    def test__story_converted_as_action_jpn(self):
        self.assertEqual(tools._story_converted_as_action(self.story_j, 0, False),
                ["# 太郎と花子\n", "- Hanako:来る()　　/部屋",
                    "- Taro　　:台詞()　　/「ああ」",
                    "- Hanako:~~台詞~~(Taro/Masao)/「好き」"])


    def test__story_converted_as_action_in_group(self):
        self.assertEqual(tools._story_converted_as_action_in_group(self.story, self.story.group_type, 1, 0, False),
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

