# -*- coding: utf-8 -*-
"""Test for person.py.
"""
import unittest

from builder.acttypes import ActType, Behavior
from builder.acttypes import behavior_str_of
from builder.base import Action
from builder.person import Person


class PersonTest(unittest.TestCase):

    def setUp(self):
        self.body = Person("Taro", 17, "male", "student", "me", "a man")

    def test_attributes(self):
        self.assertIsInstance(self.body, Person)
        self.assertEqual(self.body.name, "Taro")
        self.assertEqual(self.body.age, 17)
        self.assertEqual(self.body.sex, "male")
        self.assertEqual(self.body.job, "student")
        self.assertEqual(self.body.selfcall, "me")
        self.assertEqual(self.body.note, "a man")

    def test_acquire(self):
        acted = self.body.acquire("a box", "a testing")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.action, "a box")
        self.assertEqual(acted.behavior, Behavior.ACQUIRE)
        self.assertEqual(acted.description, "")
        self.assertEqual(acted.name, behavior_str_of(Behavior.ACQUIRE))
        self.assertEqual(acted.note, "a testing")

    def test_remember(self):
        acted = self.body.remember("his girl friend", "a cute girl")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.action, "his girl friend")
        self.assertEqual(acted.behavior, Behavior.REMEMBER)
        self.assertEqual(acted.description, "")
        self.assertEqual(acted.name, behavior_str_of(Behavior.REMEMBER))
        self.assertEqual(acted.note, "a cute girl")
