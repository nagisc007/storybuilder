# -*- coding: utf-8 -*-
"""Test for storydb.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.action import Action, ActionGroup, TagAction
from builder.behavior import Behavior
from builder.enums import ActType, GroupType, LangType, TagType
from builder.master import Master, Word, Person


_FILENAME = "master.py"


class MasterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Master")

    def setUp(self):
        self.ma = Master("test")
        self.taro = Person("Taro", 17, "male", "student")

    def test_attributes(self):
        data = [
                ("a test", "a note"),
                ("a test", ""),
                ]

        for name, note in data:
            with self.subTest(name=name, note=note):
                tmp = Master(name, note) if note else Master(name)
                self.assertIsInstance(tmp, Master)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.note, note)

    def test_attr_append_person(self):
        data = [
                ("taro", "Taro", 17, "male", "student", "me", "a man"),
                ("hanako", "Hanako", 17, "female", "student", "me", "a girl"),
                ("taro", "Kotaro", 40, "male", "lower", "me", "a parent"),
                ("takeshi", "Takeshi", 35, "male", "driver", {"taro":"Ta", "hanako":"Ha"}, ""),
                ]

        def calling_from(slf):
            if isinstance(slf, dict):
                return slf
            elif slf:
                return {"me":slf}
            else:
                return {"me":Person.DEF_SELFCALL}

        for k, name, age, sex, job, slf, note in data:
            with self.subTest(k=k, name=name, age=age, sex=sex, job=job, slf=slf, note=note):
                self.ma.append_person(k, (name, age, sex, job, slf, note))
                key = k if name != "Kotaro" else "p_taro"
                self.assertEqual(self.ma[key].name, name)
                self.assertEqual(self.ma[key].age, age)
                self.assertEqual(self.ma[key].sex, sex)
                self.assertEqual(self.ma[key].job, job)
                self.assertEqual(self.ma[key].calling, calling_from(slf))
                self.assertEqual(self.ma[key].note, note)

    def test_attr_append_word(self):
        data = [
                ("w", "word", "a word"),
                ("t", "test", "a test"),
                ("w", "word2", "a word2")
                ]

        for k, name, note in data:
            with self.subTest(k=k, name=name, note=note):
                self.ma.append_word(k, (name, note))
                key = k if name != "word2" else "w_w"
                self.assertEqual(self.ma[key].name, name)
                self.assertEqual(self.ma[key].note, note)

    def test_attr_append_word_lacked(self):
        data0 = ("w", "word")
        data1 = ("t", "test", "a test")
        self.ma.append_word(data0[0], data0[1:])
        self.ma.append_word(data1[0], data1[1:])
        self.assertEqual(self.ma.w.name, "word")
        self.assertEqual(self.ma.w.note, "")
        self.assertEqual(self.ma.t.name, "test")
        self.assertEqual(self.ma.t.note, "a test")

    def test_attr_append_word_using_cls(self):
        self.ma.append_word("w", Word("word"))
        self.assertEqual(self.ma.w.name, "word")
        self.assertEqual(self.ma.w.note, "")

    def test_break_symbol(self):
        data = [
                ("****", "****"),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.ma.break_symbol(v)
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tmp.act_type, ActType.TAG)
                self.assertEqual(tmp.behavior, Behavior.NONE)
                self.assertEqual(tmp.tag, TagType.SYMBOL)
                self.assertEqual(tmp.note, expected)

    def test_combine(self):
        data = [
                ((self.taro.tell("a test"),), 1),
                ((self.taro.tell("a test"), self.taro.tell("a test")), 2),
                ]

        for args, expected in data:
            with self.subTest(args=args, expected=expected):
                tmp = self.ma.combine(*args)
                self.assertIsInstance(tmp, ActionGroup)
                self.assertEqual(len(tmp.actions), expected)
                self.assertEqual(tmp.actions, args)

    def test_comment(self):
        data = [
                ("a test"),
                ]
        for cmt in data:
            with self.subTest(cmt=cmt):
                tmp = self.ma.comment(cmt)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, ActType.TAG)
                self.assertEqual(tmp.behavior, Behavior.NONE)
                self.assertEqual(tmp.tag, TagType.COMMENT)
                self.assertEqual(tmp.note, cmt)

    def test_scene(self):
        pass

    def test_story(self):
        pass

    def test_title(self):
        pass

