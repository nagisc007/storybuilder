# -*- coding: utf-8 -*-
"""Test for commons.py
"""
import unittest
from builder.acttypes import ActType, LangType
from builder.base import _BaseSubject, Action, Something
from builder.behavior import Behavior
from builder.person import Person
from builder.commons import behavior_str_of
from builder.commons import comma_of
from builder.commons import something_name_if
from builder.commons import subject_name_of


class BasicMethodTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: commons.py ****")

    def setUp(self):
        pass

    def test_comma_of(self):
        data_set = [
                (LangType.JPN, "、"),
                (LangType.ENG, ", ")
                ]
        for lang, expected in data_set:
            with self.subTest(lang=lang, expected=expected):
                self.assertEqual(comma_of(lang), expected)

    def test_something_name_if(self):
        data_set = [
                (_BaseSubject("test taro", "", ""), "test taro"),
                (Something(), "何か")
                ]
        for obj, expected in data_set:
            with self.subTest(obj=obj, expected=expected):
                self.assertEqual(something_name_if(obj), expected)

    def test_subject_name_of(self):
        taro = Person("Taro", 17, "male", "student")
        some = Something()
        data_set = [
                (taro.explain("test taro"), "Taro"),
                (some.explain("test some"), "何か"),
                (Action(None, ActType.ACT, Behavior.NONE, None, "no info", "no note"), ""),
                ]
        for act, expected in data_set:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(subject_name_of(act), expected)
