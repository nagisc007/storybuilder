# -*- coding: utf-8 -*-
"""Test for commons.py
"""
import unittest
from builder.action import Action
from builder.basesubject import _BaseSubject
from builder.behavior import Behavior
from builder.enums import ActType, LangType
from builder.person import Person
from builder.subject import Something
import builder.commons as commons


class MethodUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: commons.py - methods ****")

    def test_behavior_with_np_of(self):
        pass

    def test_comma_of(self):
        data = [
                (LangType.JPN, "、"),
                (LangType.ENG, ", ")
                ]
        for lang, expected in data:
            with self.subTest(lang=lang, expected=expected):
                self.assertEqual(commons.comma_of(lang), expected)

    def test_description_str_from(self):
        pass

    def test_description_if(self):
        pass

    def test_dialogue_from_description(self):
        pass

    def test_dialogue_from_description_if(self):
        pass

    def test_dialogue_from_info(self):
        pass

    def test_object_name_of(self):
        pass

    def test_sentence_from(self):
        pass

    def test_something_name_if(self):
        data = [
                (_BaseSubject("test taro", "", ""), "test taro"),
                (Something(), "何か")
                ]
        for obj, expected in data:
            with self.subTest(obj=obj, expected=expected):
                self.assertEqual(commons.something_name_if(obj), expected)

    def test_subject_name_of(self):
        taro = Person("Taro", 17, "male", "student")
        some = Something()
        data = [
                (taro.explain("test taro"), "Taro"),
                (Action(None, ActType.ACT, Behavior.NONE, None, "no info", "no note"), ""),
                ]
        for act, expected in data:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(commons.subject_name_of(act), expected)
