# -*- coding: utf-8 -*-
"""Test for tools.py
"""

import unittest
import os
import sys
from io import StringIO
from builder.sbutils import print_test_title
from builder.action import TagAction, GroupType
from builder.enums import LangType
from builder.person import Person
from builder.subject import Item, Master, Word
import builder.tools as tools


_FILENAME = "tools.py"


class PublicMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "public methods")

    def setUp(self):
        self.sm = Master("test story")
        self.taro = Person("Taro", 17, "male", "student", "me")
        self.hanako = Person("Hanako", 17, "female", "student", "me")
        self.masao = Person("Masao", 17, "male", "student", "me")
        self.story = self.sm.story(
                "Taro and Hanako",
                self.hanako.come("in room").desc("a cute girl come in"),
                self.taro.tell("wow", to=self.hanako).desc("Nice to meet you"),
                self.hanako.tell("like").negative().desc("I'm not fine"),
                lang=LangType.ENG,
                )
        self.story_j = self.sm.story(
                "太郎と花子",
                self.hanako.come("部屋").desc("可愛い少女"),
                self.taro.tell("ああ").desc("よう"),
                self.hanako.tell("好き", to=self.taro, wth=self.masao).negative().desc("全然")
                )
        self.test_file = "test_file"

    @unittest.skip("almost same output_story")
    def test_build_to_story(self):
        pass

    @unittest.skip("must use stdout")
    def test_options_parsed(self):
        pass

    @unittest.skip("almost same _output_story_to_file and _output_story_to_console")
    def test_output_story(self):
        pass


class PrivateMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "private methods")

    def setUp(self):
        self.ma = Master("test story")
        self.taro = Person("Taro", 17, "male", "student", "me")
        self.hanako = Person("Hanako", 17, "female", "student", "me")
        self.masao = Person("Masao", 17, "male", "student", "me")
        self.item = Item("stick")
        self.story = self.ma.story(
                "Taro and Hanako",
                self.hanako.come("in room").desc("a cute girl come in"),
                self.taro.tell("wow", to=self.hanako).desc("Nice to meet you"),
                self.hanako.tell("like").negative().desc("I'm not fine"),
                lang=LangType.ENG,
                )
        self.story_j = self.ma.story(
                "太郎と花子",
                self.hanako.come("部屋").desc("可愛い少女"),
                self.taro.tell("ああ").desc("よう"),
                self.hanako.tell("好き", to=self.taro, wth=self.masao).negative().desc("全然")
                )
        self.test_file = "test_file"

    def test_action_of_by_tag(self):
        data = [
                (self.ma.comment("test"), GroupType.STORY, 1, "<!--test-->"),
                (self.ma.title("test"), GroupType.STORY, 1, "# test\n"),
                (self.ma.title("test"), GroupType.STORY, 2, "\n## test\n"),
                (self.ma.title("test"), GroupType.SCENE, 1, "**test**"),
                (self.ma.hr(), GroupType.STORY, 1, "--------" * 9),
                ]
        
        for act, gtype, lv, expected in data:
            with self.subTest(act=act, gtype=gtype, lv=lv, expected=expected):
                self.assertEqual(tools._action_of_by_tag(act, gtype, lv), expected)

    def test_action_of_by_type(self):
        data = [
                (self.taro.talk(), LangType.JPN, GroupType.STORY, 1, 5, False,
                    "- Taro　　:話す()　　/"),
                (self.taro.talk(self.hanako), LangType.JPN, GroupType.STORY, 1, 5, False,
                    "- Taro　　:話す(Hanako)/"),
                ]

        for act, lng, gtype, lv, pri, dbg, expected in data:
            with self.subTest(act=act, lng=lng, gtype=gtype, lv=lv, pri=pri, dbg=dbg,
                    expected=expected):
                self.assertEqual(tools._action_of_by_type(act, lng, gtype, lv, pri, dbg),
                        expected)

    def test_action_with_obj_and_info_as_eng(self):
        data = [
                (self.taro.talk(), GroupType.STORY, False, False,
                    "- Taro    :話す()    /"),
                ]

        for act, gtype, dial, istest, expected in data:
            with self.subTest(act=act, gtype=gtype, dial=dial, istest=istest,
                    expected=expected):
                self.assertEqual(tools._action_with_obj_and_info_as_eng(
                    act, gtype, dial, istest), expected)

    def test_action_with_obj_and_info_as_jpn(self):
        data = [
                (self.taro.talk(), GroupType.STORY, False, False,
                    "- Taro　　:話す()　　/"),
                ]

        for act, gtype, dial, istest, expected in data:
            with self.subTest(act=act, gtype=gtype, dial=dial, istest=istest,
                    expected=expected):
                self.assertEqual(tools._action_with_obj_and_info_as_jpn(
                    act, gtype, dial, istest), expected)

    def test_behavior_with_obj(self):
        data = [
                (self.taro.tell(self.hanako), "台詞(Hanako)"),
                (self.taro.tell("Hanako"), "台詞()"),
                (self.taro.tell(self.hanako, self.item), "台詞(Hanako/stick)"),
                ]

        for act, expected in data:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(tools._behavior_with_obj(act), expected)

    def test_comment_of(self):
        data = [
                ("a test", "<!--a test-->"),
                ]
        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.ma.comment(v)
                self.assertEqual(tools._comment_of(tmp), expected)

    def test_description_of_by_tag(self):
        data = [
                (self.ma.comment("test"), LangType.JPN, GroupType.STORY, 1, False,
                    ""),
                (self.ma.title("test"), LangType.JPN, GroupType.STORY, 1, False,
                    "# test\n"),
                (self.ma.title("test"), LangType.JPN, GroupType.SCENE, 1, False,
                    ""),
                (self.ma.hr(), LangType.JPN, GroupType.STORY, 1, False,
                    "--------" * 9),
                ]

        for act, lng, gtype, lv, dbg, expected in data:
            with self.subTest(act=act, lng=lng, gtype=gtype, lv=lv, dbg=dbg,
                    expected=expected):
                self.assertEqual(tools._description_of_by_tag(act, lng, gtype, lv, dbg),
                        expected)

    def test_description_of_by_type(self):
        data = [
                (self.taro.talk(), LangType.JPN, GroupType.STORY, 1, False,
                    ""),
                (self.taro.talk().desc("test"), LangType.JPN, GroupType.STORY, 1, False,
                    "　test。"),
                (self.taro.talk().desc("test", "is good"), LangType.JPN, GroupType.STORY, 1, False,
                    "　test、is good。"),
                (self.taro.talk().desc("test"), LangType.ENG, GroupType.STORY, 1, False,
                    " test. "),
                (self.taro.talk().desc("test").omit(), LangType.JPN, GroupType.STORY, 1, False,
                    ""),
                ]

        for act, lng, gtype, lv, dbg, expected in data:
            with self.subTest(act=act, lng=lng, gtype=gtype, lv=lv, dbg=dbg,
                    expected=expected):
                self.assertEqual(tools._description_of_by_type(act, lng, gtype, lv, dbg),
                        expected)

    def test_flag_info_if(self):
        data = [
                ("flag", "deflag", "[flag](f-flag)[D:deflag](d-deflag)"),
                ("flag", "", "[flag](f-flag)"),
                ("", "deflag", "[D:deflag](d-deflag)"),
                ]

        for flg, dflg, expected in data:
            with self.subTest(flg=flg, dflg=dflg, expected=expected):
                tmp = self.taro.talk()
                if flg and dflg:
                    tmp = self.taro.talk().set_flag(flg).set_deflag(dflg)
                elif flg:
                    tmp = self.taro.talk().set_flag(flg)
                elif dflg:
                    tmp = self.taro.talk().set_deflag(dflg)
                self.assertEqual(tools._flag_info_if(tmp), expected)

    def test_hr_of(self):
        data = [
                (0, ""),
                (1, "-" * 8),
                (5, "-" * (8 * 5)),
                (None, "-" * (8 * 9)),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = tools._hr_of(v) if not v is None else tools._hr_of()
                self.assertEqual(tmp, expected)

    def test_list_head_inserted(self):
        data = [
                (GroupType.COMBI, "        - "),
                (GroupType.SCENE, "    - "),
                (GroupType.STORY, "- "),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(tools._list_head_inserted(v), expected)

    def test_output_story_to_console(self):
        tmp_stdout, sys.stdout = sys.stdout, StringIO()
        self.assertTrue(tools._output_story_to_console(["# test story", "test"], False))
        self.assertEqual(
                sys.stdout.getvalue(),
                "# test story\ntest\n"
                )
        # fall back
        sys.stdout = tmp_stdout


    def test_output_story_to_file_as_action(self):
        self.assertTrue(tools._output_story_to_file(["# test story", "test"], self.test_file, True, False))
        build_path = os.path.join(os.getcwd(), "build/{}_a.md".format(self.test_file))
        self.assertTrue(os.path.exists(build_path))


    def test_output_story_to_file_as_description(self):
        self.assertTrue(tools._output_story_to_file(["# test story", "test"], self.test_file, False, False))
        build_path = os.path.join(os.getcwd(), "build/{}.md".format(self.test_file))
        self.assertTrue(os.path.exists(build_path))

    def test_output_with_linenumber(self):
        data = [
                ("a test", 0, True, "0: a test"),
                ("a test", 1, True, "1: a test"),
                ("a test", 10, True, "10: a test"),
                ("a test", 5, False, "a test")
                ]

        for v, n, dbg, expected in data:
            with self.subTest(v=v, n=n, dgb=dbg, expected=expected):
                self.assertEqual(tools._output_with_linenumber(v, n, dbg), expected)

    def test_scene_title_of(self):
        data = [
                ("a test", "**a test**"),
                ]

        for title, expected in data:
            with self.subTest(title=title, expected=expected):
                tmp = self.ma.title(title)
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tools._scene_title_of(tmp), expected)

    def test_story_converted_as_action(self):
        self.assertEqual(tools._story_converted_as_action(self.story, 0, False),
                ["# Taro and Hanako\n", "- Hanako  :来る()    /in room",
                    "- Taro    :台詞(Hanako)/ \"wow\" ",
                    "- Hanako  :~~台詞~~()/ \"like\" "])


    def test_story_converted_as_action_jpn(self):
        self.assertEqual(tools._story_converted_as_action(self.story_j, 0, False),
                ["# 太郎と花子\n", "- Hanako:来る()　　/部屋",
                    "- Taro　　:台詞()　　/「ああ」",
                    "- Hanako:~~台詞~~(Taro/Masao)/「好き」"])


    def test_story_converted_as_action_in_group(self):
        self.assertEqual(tools._story_converted_as_action_in_group(self.story, self.story.group_type, 1, 0, False),
                ["# Taro and Hanako\n", "- Hanako  :来る()    /in room",
                    "- Taro    :台詞(Hanako)/ \"wow\" ",
                    "- Hanako  :~~台詞~~()/ \"like\" "])


    def test_story_converted_as_description(self):
        self.assertEqual(tools._story_converted_as_description(self.story, False),
                ["# Taro and Hanako\n",
                    " a cute girl come in. ",
                    ' "Nice to meet you" ',
                    ' "I\'m not fine" '])


    def test_story_converted_as_description_in_group(self):
        self.assertEqual(tools._story_converted_as_description_in_group(self.story, self.story.group_type, 1, False),
                ["# Taro and Hanako\n",
                    " a cute girl come in. ",
                    ' "Nice to meet you" ',
                    ' "I\'m not fine" '])

    def test_story_data_converted(self):
        self.assertEqual(tools._story_data_converted(self.story, True, 0, False),
                ["# Taro and Hanako\n", "- Hanako  :来る()    /in room",
                     "- Taro    :台詞(Hanako)/ \"wow\" ",
                    "- Hanako  :~~台詞~~()/ \"like\" "])

    def test_story_title_of(self):
        ma = Master('test')

        data = [
                ("a test", 0, " a test\n"),
                ("a test", 1, "# a test\n"),
                ("a test", 2, "\n## a test\n"),
                ]

        for title, lv, expected in data:
            with self.subTest(title=title, lv=lv, expected=expected):
                tmp = ma.title(title)
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tools._story_title_of(tmp, lv), expected)

