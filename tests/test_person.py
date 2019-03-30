# -*- coding: utf-8 -*-
"""Test for person.py.
"""
import unittest

from builder.acttypes import ActType
from builder.base import Action, Item
from builder.person import Person
from builder.behavior import Behavior
from builder.behavior import behavior_str_of


class PersonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: person.py ****")

    def setUp(self):
        self.body = Person("Taro", 17, "male", "student", "me", note="a man")
        self.box = Item("Box", "a box")
        self.doll = Item("Doll", "a substitute of a person")

    def test_attributes(self):
        self.assertIsInstance(self.body, Person)
        self.assertEqual(self.body.name, "Taro")
        self.assertEqual(self.body.age, 17)
        self.assertEqual(self.body.sex, "male")
        self.assertEqual(self.body.job, "student")
        self.assertEqual(self.body.selfcall, "me")
        self.assertEqual(self.body.note, "a man")

    def test_acquire(self):
        acted = self.body.acquire(info="a box", note="a testing")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.info, "a box")
        self.assertEqual(acted.behavior, Behavior.ACQUIRE)
        self.assertEqual(acted.descriptions, ())
        self.assertEqual(acted.note, "a testing")
        self.assertEqual(acted.objects, ())

    def test_remember(self):
        acted = self.body.remember(info="his girl friend", note="a cute girl")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.info, "his girl friend")
        self.assertEqual(acted.behavior, Behavior.REMEMBER)
        self.assertEqual(acted.descriptions, ())
        self.assertEqual(acted.note, "a cute girl")
        self.assertEqual(acted.objects, ())
