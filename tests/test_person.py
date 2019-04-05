# -*- coding: utf-8 -*-
"""Test for person.py.
"""
import unittest
from builder.sbutils import print_test_title
from builder.person import Person
from builder.person import Behavior
from builder.subject import Action, ActType, Item
from builder.basesubject import Info


_FILENAME = "person.py"


class PersonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Person")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student", "me", "a man", "he is a guy")
        self.hanako = Person("Hanako", 17, "female", "student", "me", "a girl", "she is so cute")

    def test_attributes(self):
        data = [
                ("Taro", 17, "male", "student", "me", "a man"),
                ("Hanako", 17, "female", "student", "me", ""),
                ("Kenta", 20, "male", "lower", "", ""),
                ("kotaro", 30, "male", "driver", {"me":"ore","taro":"ta"}, ""),
                ("miku", 15, "female", "idol", "me:miku:taro:Tan:hanako:Han", ""),
                ("mariko", 32, "female", "sheff", "taro:Taro-san:hanako:Hana-san", ""),
                ]

        def creator(name, age, sex, job, slf, note):
            if slf and note:
                return Person(name, age, sex, job, slf, note)
            elif slf:
                return Person(name, age, sex, job, slf)
            else:
                return Person(name, age, sex, job)

        def calling_from(slf):
            if isinstance(slf, dict):
                return slf
            elif ":" in slf:
                tmp = slf.split(":")
                ret = {}
                for k,v in zip(tmp[0::2], tmp[1::2]):
                    ret[k] = v
                if not "me" in ret.keys():
                    ret.update({"me":Person.DEF_SELFCALL})
                return ret
            elif slf:
                return {"me": slf}
            else:
                return {"me": Person.DEF_SELFCALL}

        for name, age, sex, job, slf, note in data:
            tmp = creator(name, age, sex, job, slf, note)
            calling = calling_from(slf)
            self.assertIsInstance(tmp, Person)
            self.assertEqual(tmp.name, name)
            self.assertEqual(tmp.age, age)
            self.assertEqual(tmp.sex, sex)
            self.assertEqual(tmp.job, job)
            self.assertEqual(tmp.calling, calling)
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

