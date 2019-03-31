# -*- coding: utf-8 -*-
"""Test for person.py.
"""
import unittest

from builder.action import Action
from builder.behavior import Behavior
from builder.enums import ActType
from builder.person import Person
from builder.subject import Item


class PersonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: person.py - Person ****")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student", "me", "a man", "he is a guy")
        self.hanako = Person("Hanako", 17, "female", "student", "me", "a girl", "she is so cute")

    def test_attributes(self):
        data = [
                ("Taro", 17, "male", "student", "me", "a man", "he is a guy"),
                ("Hanako", 17, "female", "student", "me", "a girl", None),
                ("Kenta", 20, "male", "lower", "me", None, None),
                ("Miki", 25, "female", "mother", None, None, None),
                ]
        def creator(name, age, sex, job, slf, info, note):
            if slf and info and note:
                return Person(name, age, sex, job, slf, info, note)
            elif slf and info:
                return Person(name, age, sex, job, slf, info)
            elif slf:
                return Person(name, age, sex, job, slf)
            else:
                return Person(name, age, sex, job)
        for name, age, sex, job, slf, info, note in data:
            tmp = creator(name, age, sex, job, slf, info, note)
            self.assertIsInstance(tmp, Person)
            self.assertEqual(tmp.name, name)
            self.assertEqual(tmp.age, age)
            self.assertEqual(tmp.sex, sex)
            self.assertEqual(tmp.job, job)
            self.assertEqual(tmp.selfcall, slf if slf else Person.DEF_SELFCALL)
            self.assertEqual(tmp.info, info if info else "")
            self.assertEqual(tmp.note, note if note else "")

    def test_acquire(self):
        acted = self.taro.acquire(info="a box", note="a testing")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.info, "a box")
        self.assertEqual(acted.behavior, Behavior.ACQUIRE)
        self.assertEqual(acted.descriptions, ())
        self.assertEqual(acted.note, "a testing")
        self.assertEqual(acted.objects, ())

    def test_remember(self):
        acted = self.taro.remember(info="his girl friend", note="a cute girl")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.info, "his girl friend")
        self.assertEqual(acted.behavior, Behavior.REMEMBER)
        self.assertEqual(acted.descriptions, ())
        self.assertEqual(acted.note, "a cute girl")
        self.assertEqual(acted.objects, ())
