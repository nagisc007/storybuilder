# -*- coding: utf-8 -*-
"""Test for base.py
"""
import unittest

from builder.acttypes import ActType, TagType
from builder.acttypes import tag_str_of
from builder.behavior import Behavior
from builder.base import _BaseAction, _BaseSubject, Action, ActionGroup
from builder.base import _BasePerson, Stage, Item, DayTime, Word
from builder.base import Master


class BaseActionTest(unittest.TestCase):

    def setUp(self):
        self.body = _BaseAction("test act", "a test note")

    def test_attributes(self):
        self.assertIsInstance(self.body, _BaseAction)
        self.assertEqual(self.body.name, "test act")
        self.assertEqual(self.body.note, "a test note")


class BaseSubjectTest(unittest.TestCase):


    def setUp(self):
        self.body = _BaseSubject("test subject", "a test note")

    def test_attributes(self):
        self.assertIsInstance(self.body, _BaseSubject)
        self.assertEqual(self.body.name, "test subject")
        self.assertEqual(self.body.note, "a test note")

    def test_explain(self):
        acted = self.body.explain("a test", "this is a test")
        self.assertIsInstance(acted, Action)


class ActionTest(unittest.TestCase):

    def setUp(self):
        self.sub = _BaseSubject("Taro", "a test subject")
        self.body = Action(self.sub,
                ActType.ACT, Behavior.ACT, "testing", None, "test", "a test note")

    def test_attributes(self):
        self.assertIsInstance(self.body.subject, _BaseSubject)
        self.assertEqual(self.body.act_type, ActType.ACT)
        self.assertEqual(self.body.behavior, Behavior.ACT)
        self.assertEqual(self.body.description, "")
        self.assertEqual(self.body.action, "testing")
        self.assertEqual(self.body.note, "a test note")
        self.assertEqual(self.body.name, "test")
        self.assertEqual(self.body.object, None)
        self.assertEqual(self.body.flag, "")
        self.assertEqual(self.body.deflag, "")

    def test_desc(self):
        self.assertFalse(self.body.description)
        self.body.desc("this is a test")
        self.assertIsInstance(self.body.description, str)
        self.assertEqual(self.body.description, "this is a test")

    def test_passive(self):
        self.assertFalse(self.body.is_passive)
        self.body.passive()
        self.assertTrue(self.body.is_passive)

    def test_flag(self):
        self.assertEqual(self.body.flag, "")
        self.body.set_flag("test")
        self.assertEqual(self.body.flag, "test")

    def test_deflag(self):
        self.assertEqual(self.body.deflag, "")
        self.body.set_deflag("test")
        self.assertEqual(self.body.deflag, "test")


class ActionGroupTest(unittest.TestCase):

    def setUp(self):
        self.taro = _BasePerson("Taro", 17, "male", "student", "a man")

    def test_attributes(self):
        group = ActionGroup(self.taro.tell("wow"),self.taro.explain("the man"),
                name="test group", note="test note")
        self.assertIsInstance(group, ActionGroup)
        self.assertEqual(group.name, "test group")
        self.assertEqual(group.note, "test note")
        self.assertEqual(len(group.actions), 2)
        for a in group.actions:
            self.assertIsInstance(a, Action)


class BasePersonTest(unittest.TestCase):

    def setUp(self):
        self.body = _BasePerson("Taro", 17, "male", "student", "a man")

    def test_attributes(self):
        self.assertIsInstance(self.body, _BasePerson)
        self.assertEqual(self.body.name, "Taro")
        self.assertEqual(self.body.age, 17)
        self.assertEqual(self.body.sex, "male")
        self.assertEqual(self.body.job, "student")
        self.assertEqual(self.body.note, "a man")

    def test_act(self):
        acted = self.body.act("testing", Behavior.TEST, None, "test", "a test act")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.action, "testing")
        self.assertEqual(acted.note, "a test act")
        self.assertEqual(acted.name, "test")
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.behavior, Behavior.TEST)
        self.assertEqual(acted.object, None)

    def test_tell(self):
        told = self.body.tell("I am Taro", note="Taro's voice")
        self.assertIsInstance(told, Action)
        self.assertEqual(told.action, "I am Taro")
        self.assertEqual(told.note, "Taro's voice")
        self.assertEqual(told.act_type, ActType.TELL)
        self.assertEqual(told.behavior, Behavior.TELL)


class StageTest(unittest.TestCase):

    def setUp(self):
        self.body = Stage("test stage", "a test stage")

    def test_attributes(self):
        self.assertIsInstance(self.body, Stage)
        self.assertEqual(self.body.name, "test stage")
        self.assertEqual(self.body.note, "a test stage")


class ItemTest(unittest.TestCase):

    def setUp(self):
        self.body = Item("test item", "a test item")

    def test_attributes(self):
        self.assertIsInstance(self.body, Item)
        self.assertEqual(self.body.name, "test item")
        self.assertEqual(self.body.note, "a test item")


class DayTimeTest(unittest.TestCase):

    def setUp(self):
        self.body = DayTime("test day", 10, 5, 2019, 12, "a sunny day")

    def test_attributes(self):
        self.assertIsInstance(self.body, DayTime)
        self.assertEqual(self.body.name, "test day")
        self.assertEqual(self.body.mon, 10)
        self.assertEqual(self.body.day, 5)
        self.assertEqual(self.body.year, 2019)
        self.assertEqual(self.body.hour, 12)
        self.assertEqual(self.body.note, "a sunny day")


class MasterTest(unittest.TestCase):

    def setUp(self):
        self.body = Master("test story", "a test")

    def test_attributes(self):
        self.assertIsInstance(self.body, Master)
        self.assertEqual(self.body.name, "test story")
        self.assertEqual(self.body.note, "a test")
    
    def test_comment(self):
        acted = self.body.comment("a test comment", note="this is a test")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.act_type, ActType.TAG)
        self.assertEqual(acted.action, "a test comment")
        self.assertEqual(acted.behavior, Behavior.NONE)
        self.assertEqual(acted.description, "")
        self.assertEqual(acted.name, tag_str_of(TagType.COMMENT))
        self.assertEqual(acted.note, "this is a test")
        self.assertEqual(acted.subject, self.body)
        self.assertEqual(acted.object, None)

    def test_title(self):
        acted = self.body.title("a test title", "this is a title")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.act_type, ActType.TAG)
        self.assertEqual(acted.action, "a test title")
        self.assertEqual(acted.behavior, Behavior.NONE)
        self.assertEqual(acted.description, "")
        self.assertEqual(acted.name, tag_str_of(TagType.TITLE))
        self.assertEqual(acted.note, "this is a title")
        self.assertEqual(acted.subject, self.body)

    def test_story(self):
        taro = _BasePerson("Taro", 17, "male", "student")
        acted = self.body.story(taro.tell("a test"), taro.explain("a man"),
                note="test story")
        self.assertIsInstance(acted, ActionGroup)
        self.assertEqual(acted.name, "_story")
        self.assertEqual(acted.note, "test story")
        self.assertEqual(len(acted.actions), 2)
        for a in acted.actions:
            self.assertIsInstance(a, Action)


class WordTest(unittest.TestCase):

    def setUp(self):
        self.body = Word("Test", "a test word")

    def test_attributes(self):
        self.assertIsInstance(self.body, Word)
        self.assertEqual(self.body.name, "Test")
        self.assertEqual(self.body.note, "a test word")
