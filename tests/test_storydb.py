# -*- coding: utf-8 -*-
"""Test for storydb.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.storydb import StoryDB, Word, Person


_FILENAME = "storydb.py"


class StoryDBTEST(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "StoryDB")

    def setUp(self):
        self.db = StoryDB([], [], [], [], [])

    def test_attr_append_chara(self):
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
                self.db.append_chara(k, (name, age, sex, job, slf, note))
                key = k if name != "Kotaro" else "p_taro"
                self.assertEqual(self.db[key].name, name)
                self.assertEqual(self.db[key].age, age)
                self.assertEqual(self.db[key].sex, sex)
                self.assertEqual(self.db[key].job, job)
                self.assertEqual(self.db[key].calling, calling_from(slf))
                self.assertEqual(self.db[key].note, note)

    def test_attr_append_word(self):
        data = [
                ("w", "word", "a word"),
                ("t", "test", "a test"),
                ("w", "word2", "a word2")
                ]

        for k, name, note in data:
            with self.subTest(k=k, name=name, note=note):
                self.db.append_word(k, (name, note))
                key = k if name != "word2" else "w_w"
                self.assertEqual(self.db[key].name, name)
                self.assertEqual(self.db[key].note, note)

    def test_attr_append_word_lacked(self):
        data0 = ("w", "word")
        data1 = ("t", "test", "a test")
        self.db.append_word(data0[0], data0[1:])
        self.db.append_word(data1[0], data1[1:])
        self.assertEqual(self.db.w.name, "word")
        self.assertEqual(self.db.w.note, "")
        self.assertEqual(self.db.t.name, "test")
        self.assertEqual(self.db.t.note, "a test")

    def test_attr_append_word_using_cls(self):
        self.db.append_word("w", Word("word"))
        self.assertEqual(self.db.w.name, "word")
        self.assertEqual(self.db.w.note, "")

