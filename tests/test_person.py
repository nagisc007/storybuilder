# -*- coding: utf-8 -*-
"""Test for person.py.
"""
import unittest

from builder.person import Person
from builder.person import Behavior
from builder.subject import Action, ActType, Item
from builder.basesubject import Info


_FILENAME = "person.py"


class PersonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        _print_title(_FILENAME, "Person")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student", "me", "a man", "he is a guy")
        self.hanako = Person("Hanako", 17, "female", "student", "me", "a girl", "she is so cute")

    def test_attributes(self):
        data = [
                ("Taro", 17, "male", "student", "me", "a man"),
                ("Hanako", 17, "female", "student", "me", ""),
                ("Kenta", 20, "male", "lower", "", ""),
                ]

        def creator(name, age, sex, job, slf, note):
            if slf and note:
                return Person(name, age, sex, job, slf, note)
            elif slf:
                return Person(name, age, sex, job, slf)
            else:
                return Person(name, age, sex, job)

        for name, age, sex, job, slf, note in data:
            tmp = creator(name, age, sex, job, slf, note)
            self.assertIsInstance(tmp, Person)
            self.assertEqual(tmp.name, name)
            self.assertEqual(tmp.age, age)
            self.assertEqual(tmp.sex, sex)
            self.assertEqual(tmp.job, job)
            self.assertEqual(tmp.selfcall, slf if slf else Person.DEF_SELFCALL)
            self.assertEqual(tmp.note, note)

    def test_inherit(self):
        pass

    def test_personal_actions(self):
        data = [
                ("accept", "a test"),
                ("acquire", "a test"),
                ("add", "a test"),
                ]

        for attr, a in data:
            with self.subTest(attr=attr, a=a):
                try:
                    tmp = getattr(self.taro, attr)(a)
                except AttributeError:
                    self.fail("Attribute {} is nothing".format(attr))
                self.assertIsInstance(tmp, Action)
                self.assertIsInstance(tmp.objects[0], Info)
                self.assertEqual(tmp.objects[0].note, a)


# private functions
def _print_title(fname: str, title: str):
    print("\n**** TEST: {} - {} ****".format(fname, title))
