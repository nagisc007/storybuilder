# -*- coding: utf-8 -*-
"""Test for base.py
"""
import unittest

from builder.acttypes import ActType, Behavior
from builder.base import _BaseAction, Subject, Desc, Act
from builder.base import BasePerson, Stage, Item, DayTime
from builder.base import Story, Episode, Scene
from builder.person import Person


class SampleObj(object):
    def __init__(self, name):
        self.name = name


class BaseActionTest(unittest.TestCase):

    class SampleDataCls(object):
        def __init__(self, name):
            self.name = name

    def setUp(self):
        self.body = _BaseAction(BaseActionTest.SampleDataCls,
                "test title", "test note")

    def test_attributes(self):
        self.assertFalse(self.body.data)
        self.assertEqual(self.body.data, ())
        self.assertEqual(self.body.data_class, BaseActionTest.SampleDataCls)
        self.assertEqual(self.body.note, "test note")
        self.assertEqual(self.body.title, "test title")

    def test_is_data_checked(self):
        self.assertTrue(self.body.is_data_checked(BaseActionTest.SampleDataCls("testing")))

    def test_is_not_double_commited(self):
        self.assertFalse(self.body.is_double_commited())
        self.body.commit(BaseActionTest.SampleDataCls("sample"))
        self.assertTrue(self.body.is_double_commited())

    def test_commit(self):
        self.body.commit(BaseActionTest.SampleDataCls("sample"))
        self.assertEqual(self.body.data[0].name, "sample")


class SubjectTest(unittest.TestCase):


    def setUp(self):
        self.body = Subject("test name", "test note")

    def test_attributes(self):
        self.assertEqual(self.body.name, "test name")
        self.assertEqual(self.body.note, "test note")

    def test_feature_look(self):
        self.assertIsInstance(self.body.look("a test"), Act)


class DescTest(unittest.TestCase):

    def setUp(self):
        self.body = Desc("test")

    def test_attributes(self):
        self.assertEqual(self.body.description, "test")


class ActTest(unittest.TestCase):

    def setUp(self):
        self.body = Act(Subject("test taro", "a test"),
                ActType.ACT, Behavior.DO, "testing", "tested", "test note")

    def test_attributes(self):
        self.assertIsInstance(self.body.subject, Subject)
        self.assertEqual(self.body.act_type, ActType.ACT)
        self.assertEqual(self.body.behavior, Behavior.DO)
        self.assertEqual(self.body.title, "testing")
        self.assertEqual(self.body.act_word, "tested")
        self.assertEqual(self.body.note, "test note")

    def test_desc(self):
        self.assertFalse(self.body.data)
        self.body.desc("this is a test")
        self.assertIsInstance(self.body.data, tuple)
        self.assertIsInstance(self.body.data[0], Desc)
        self.assertEqual(self.body.data[0].description, "this is a test")

    def test_desc_with_many_strings(self):
        self.assertFalse(self.body.data)
        self.body.desc("test is one", "test is two", "test is three")
        self.assertIsInstance(self.body.data, tuple)
        self.assertEqual(len(self.body.data), 3)
        for d in self.body.data:
            self.assertIsInstance(d, Desc)
        self.assertEqual(self.body.data[0].description, "test is one")
        self.assertEqual(self.body.data[1].description, "test is two")
        self.assertEqual(self.body.data[2].description, "test is three")


class BasePersonTest(unittest.TestCase):

    def setUp(self):
        self.body = BasePerson("Taro", 17, "male", "student", "a man")

    def test_attributes(self):
        self.assertEqual(self.body.name, "Taro")
        self.assertEqual(self.body.age, 17)
        self.assertEqual(self.body.sex, "male")
        self.assertEqual(self.body.job, "student")
        self.assertEqual(self.body.note, "a man")

    def test_act(self):
        acted = self.body.act("testing", act_word="tested", note="a test act")
        self.assertIsInstance(acted, Act)
        self.assertEqual(acted.title, "testing")
        self.assertEqual(acted.act_word, "tested")
        self.assertEqual(acted.note, "a test act")
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.behavior, Behavior.DO)

    def test_tell(self):
        told = self.body.tell("I am Taro", note="Taro's voice")
        self.assertIsInstance(told, Act)
        self.assertEqual(told.title, "I am Taro")
        self.assertEqual(told.note, "Taro's voice")
        self.assertEqual(told.act_type, ActType.TELL)
        self.assertEqual(told.act_word, "言う")
        self.assertEqual(told.behavior, Behavior.TALK)

    def test_think(self):
        thought = self.body.think("I am", note="Taro's thought")
        self.assertIsInstance(thought, Act)
        self.assertEqual(thought.title, "I am")
        self.assertEqual(thought.note, "Taro's thought")
        self.assertEqual(thought.act_type, ActType.THINK)
        self.assertEqual(thought.act_word, "思う")
        self.assertEqual(thought.behavior, Behavior.FEEL)


class StageTest(unittest.TestCase):

    def setUp(self):
        self.body = Stage("test stage", "a test stage")

    def test_attributes(self):
        self.assertTrue(isinstance(self.body, Stage))
        self.assertEqual(self.body.name, "test stage")
        self.assertEqual(self.body.note, "a test stage")


class ItemTest(unittest.TestCase):

    def setUp(self):
        self.body = Item("test item", "a test item")

    def test_attributes(self):
        self.assertTrue(isinstance(self.body, Item))
        self.assertEqual(self.body.name, "test item")
        self.assertEqual(self.body.note, "a test item")


class DayTimeTest(unittest.TestCase):

    def setUp(self):
        self.body = DayTime("test day", 10, 5, 2019, 12, "a sunny day")

    def test_attributes(self):
        self.assertTrue(isinstance(self.body, DayTime))
        self.assertEqual(self.body.name, "test day")
        self.assertEqual(self.body.mon, 10)
        self.assertEqual(self.body.day, 5)
        self.assertEqual(self.body.year, 2019)
        self.assertEqual(self.body.hour, 12)
        self.assertEqual(self.body.note, "a sunny day")


class SceneTest(unittest.TestCase):

    def setUp(self):
        self.body = Scene("test scene", "action scene")

    def test_attributes(self):
        self.assertIsInstance(self.body, Scene)
        self.assertEqual(self.body.title, "test scene")
        self.assertEqual(self.body.note, "action scene")


class EpisodeTest(unittest.TestCase):

    def setUp(self):
        self.body = Episode("test episode", "hero meets a heroine")

    def test_attributes(self):
        self.assertIsInstance(self.body, Episode)
        self.assertEqual(self.body.title, "test episode")
        self.assertEqual(self.body.note, "hero meets a heroine")


class StoryTest(unittest.TestCase):

    def setUp(self):
        self.body = Story("test story", "a boring story")

    def test_attributes(self):
        self.assertIsInstance(self.body, Story)
        self.assertEqual(self.body.title, "test story")
        self.assertEqual(self.body.note, "a boring story")
