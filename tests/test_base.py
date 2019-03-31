# -*- coding: utf-8 -*-
"""Test for base.py
"""
import unittest
from builder.action import _BaseAction, Action, ActionGroup
from builder.basesubject import _BaseSubject
from builder.behavior import Behavior
from builder.enums import ActType, AuxVerb, GroupType, TagType
from builder.subject import _BasePerson, DayTime, Item, Master, Stage, Something, Word, something



class BasePersonTest(unittest.TestCase):

    def setUp(self):
        self.body = _BasePerson("Taro", 17, "male", "student", note="a man")

    def test_attributes(self):
        self.assertIsInstance(self.body, _BasePerson)
        self.assertEqual(self.body.name, "Taro")
        self.assertEqual(self.body.age, 17)
        self.assertEqual(self.body.sex, "male")
        self.assertEqual(self.body.job, "student")
        self.assertEqual(self.body.note, "a man")

    def test_act(self):
        acted = self.body.act(Behavior.TEST, None, "testing", "a test act")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.info, "testing")
        self.assertEqual(acted.note, "a test act")
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.behavior, Behavior.TEST)
        self.assertEqual(acted.objects, ())

    def test_tell(self):
        told = self.body.tell("I am Taro", note="Taro's voice")
        self.assertIsInstance(told, Action)
        self.assertEqual(told.info, "I am Taro")
        self.assertEqual(told.note, "Taro's voice")
        self.assertEqual(told.act_type, ActType.TELL)
        self.assertEqual(told.behavior, Behavior.TELL)


class StageTest(unittest.TestCase):

    def setUp(self):
        self.body = Stage("test stage", note="a test stage")

    def test_attributes(self):
        self.assertIsInstance(self.body, Stage)
        self.assertEqual(self.body.name, "test stage")
        self.assertEqual(self.body.note, "a test stage")


class ItemTest(unittest.TestCase):

    def setUp(self):
        self.body = Item("test item", note="a test item")

    def test_attributes(self):
        self.assertIsInstance(self.body, Item)
        self.assertEqual(self.body.name, "test item")
        self.assertEqual(self.body.note, "a test item")


class DayTimeTest(unittest.TestCase):

    def setUp(self):
        self.body = DayTime("test day", 10, 5, 2019, 12, 30, note="a sunny day")

    def test_attributes(self):
        self.assertIsInstance(self.body, DayTime)
        self.assertEqual(self.body.name, "test day")
        self.assertEqual(self.body.mon, 10)
        self.assertEqual(self.body.min, 30)
        self.assertEqual(self.body.day, 5)
        self.assertEqual(self.body.year, 2019)
        self.assertEqual(self.body.hour, 12)
        self.assertEqual(self.body.note, "a sunny day")


class MasterTest(unittest.TestCase):

    def setUp(self):
        self.body = Master("test story", "a info", "a test")

    def test_attributes(self):
        self.assertIsInstance(self.body, Master)
        self.assertEqual(self.body.name, "test story")
        self.assertEqual(self.body.info, "a info")
        self.assertEqual(self.body.note, "a test")
    
    def test_comment(self):
        acted = self.body.comment("a test comment")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.act_type, ActType.TAG)
        self.assertEqual(acted.info, "a test comment")
        self.assertEqual(acted.behavior, Behavior.NONE)
        self.assertEqual(acted.descriptions, ())
        self.assertEqual(acted.subject, self.body)
        self.assertEqual(acted.objects, ())

    def test_title(self):
        acted = self.body.title("a test title")
        self.assertIsInstance(acted, Action)
        self.assertEqual(acted.act_type, ActType.TAG)
        self.assertEqual(acted.info, "a test title")
        self.assertEqual(acted.behavior, Behavior.NONE)
        self.assertEqual(acted.descriptions, ())
        self.assertEqual(acted.subject, self.body)

    def test_scene(self):
        taro = _BasePerson("Taro", 17, "male", "student")
        acted = self.body.scene("test scene",
                taro.tell("a test"),
                taro.explain("a man"),
                )
        self.assertIsInstance(acted, ActionGroup)
        self.assertEqual(acted.group_type, GroupType.SCENE)
        self.assertEqual(len(acted.actions), 3)
        self.assertEqual(acted.actions[0].info, "test scene")

    def test_story(self):
        taro = _BasePerson("Taro", 17, "male", "student")
        acted = self.body.story(
                taro.tell("a test"),
                taro.explain("a man"),
                note="test story")
        self.assertIsInstance(acted, ActionGroup)
        self.assertEqual(acted.group_type, GroupType.STORY)
        self.assertEqual(acted.note, "test story")
        self.assertEqual(len(acted.actions), 2)
        for a in acted.actions:
            self.assertIsInstance(a, Action)

class SomethingTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_attributes(self):
        test_one = something()
        self.assertIsInstance(test_one, Something)
        self.assertEqual(test_one.name, Something._NAME)
        self.assertEqual(test_one.note, "")


class WordTest(unittest.TestCase):

    def setUp(self):
        self.body = Word("Test", "a test word", note="note is an empty")

    def test_attributes(self):
        self.assertIsInstance(self.body, Word)
        self.assertEqual(self.body.name, "Test")
        self.assertEqual(self.body.info, "a test word")
        self.assertEqual(self.body.note, "note is an empty")
