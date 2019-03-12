# -*- coding: utf-8 -*-
"""Test for base.py
"""
import unittest

from builder.acttypes import ActType, Behavior
from builder.base import Subject, Act, Title, Person, Stage, Item, DayTime


class SampleObj(object):
    def __init__(self, name):
        self.name = name


class SubjectTest(unittest.TestCase):

    def test_feature_look(self):
        sbj = Subject("test1", "test info")
        subjected = sbj.look("this is test")

        self.assertTrue(isinstance(subjected, Act))
        self.assertEqual(sbj.name, "test1")
        self.assertEqual(sbj.info, "test info")
        self.assertEqual(subjected.subject, sbj)


class ActTest(unittest.TestCase):

    def setUp(self):
        self.subject = Subject("test_subject", "this is test")

    def test_attributes(self):
        act = Act(self.subject, ActType.TEST, Behavior.DO, "test act")

        self.assertTrue(isinstance(act, Act))
        self.assertEqual(act.subject, self.subject)
        self.assertEqual(act.act_type, ActType.TEST)
        self.assertEqual(act.behavior, Behavior.DO)
        self.assertEqual(act.action, "test act")

    def test_desc(self):
        act = Act(self.subject, ActType.TEST, Behavior.DO, "test act")

        self.assertEqual(act.description, "")
        
        acted = act.desc("this is an action")

        self.assertTrue(isinstance(acted, Act))
        self.assertEqual(acted.description, "this is an action")


class TitleTest(unittest.TestCase):

    def test_attributes(self):
        ttl = Title("test1", "this is test")

        self.assertTrue(isinstance(ttl, Act))
        self.assertEqual(ttl.act_type, ActType.SYMBOL)
        self.assertEqual(ttl.behavior, Behavior.DISPLAY)
        self.assertEqual(ttl.action, "test1")
        self.assertEqual(ttl.subject.info, "this is test")


class PersonTest(unittest.TestCase):

    def test_attributes(self):
        psn = Person("Taro", 15, "male", "student", "he is a man")

        self.assertTrue(isinstance(psn, Person))
        self.assertEqual(psn.name, "Taro")
        self.assertEqual(psn.age, 15)
        self.assertEqual(psn.sex, "male")
        self.assertEqual(psn.job, "student")
        self.assertEqual(psn.info, "he is a man")

    def test_act(self):
        psn = Person("Taro", 15, "male", "student", "he is a man")

        acted = psn.act("he acts with his smile")

        self.assertTrue(isinstance(acted, Act))
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.behavior, Behavior.DO)
        self.assertEqual(acted.action, "he acts with his smile")

    def test_act_with_behavior(self):
        psn = Person("Taro", 15, "male", "student", "he is a man")

        acted = psn.act("go home", Behavior.GO)

        self.assertTrue(isinstance(acted, Act))
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.action, "go home")
        self.assertEqual(acted.behavior, Behavior.GO)

    def test_reply(self):
        psn = Person("Taro", 15, "male", "student", "he is a man")

        acted = psn.reply("Yes")

        self.assertTrue(isinstance(acted, Act))
        self.assertEqual(acted.act_type, ActType.TELL)
        self.assertEqual(acted.action, "Yes返事")
        self.assertEqual(acted.behavior, Behavior.REPLY)

    def test_tell(self):
        psn = Person("Taro", 15, "male", "student", "he is a man")

        acted = psn.tell("So so")

        self.assertTrue(isinstance(acted, Act))
        self.assertEqual(acted.act_type, ActType.TELL)
        self.assertEqual(acted.action, "So so言う")
        self.assertEqual(acted.behavior, Behavior.TALK)

    def test_think(self):
        psn = Person("Taro", 15, "male", "student", "he is a man")

        acted = psn.think("about himself")

        self.assertTrue(isinstance(acted, Act))
        self.assertEqual(acted.act_type, ActType.THINK)
        self.assertEqual(acted.action, "about himself思う")
        self.assertEqual(acted.behavior, Behavior.FEEL)

    def test_must(self):
        psn = Person("Taro", 15, "male", "student", "he is a man")

        acted = psn.must("home work")

        self.assertTrue(isinstance(acted, Act))
        self.assertEqual(acted.act_type, ActType.THINK)
        self.assertEqual(acted.action, "home workしなければならない")
        self.assertEqual(acted.behavior, Behavior.MUST_DO)

    def test_want(self):
        psn = Person("Taro", 15, "male", "student", "he is a man")

        acted = psn.want("sleep")

        self.assertTrue(isinstance(acted, Act))
        self.assertEqual(acted.act_type, ActType.THINK)
        self.assertEqual(acted.action, "sleepしたい")
        self.assertEqual(acted.behavior, Behavior.WANT)

    def test_result(self):
        psn = Person("Taro", 15, "male", "student", "he is a man")

        acted = psn.result("forget his home work")

        self.assertTrue(isinstance(acted, Act))
        self.assertEqual(acted.act_type, ActType.ACT)
        self.assertEqual(acted.action, "forget his home workであった")
        self.assertEqual(acted.behavior, Behavior.RESULT)


class StageTest(unittest.TestCase):

    def test_attributes(self):
        stg = Stage("test1", "here is a test")

        self.assertTrue(isinstance(stg, Stage))
        self.assertEqual(stg.name, "test1")
        self.assertEqual(stg.info, "here is a test")

    def test_look(self):
        stg = Stage("test1", "here is a test")

        staged = stg.look("a black stage")

        self.assertTrue(isinstance(staged, Act))
        self.assertEqual(staged.action, "a black stage")


class ItemTest(unittest.TestCase):

    def test_attributes(self):
        itm = Item("test1", "this is an item")

        self.assertTrue(isinstance(itm, Item))
        self.assertEqual(itm.name, "test1")
        self.assertEqual(itm.info, "this is an item")

    def test_look(self):
        itm = Item("test1", "this is an item")

        itemed = itm.look("a shiny ball")

        self.assertTrue(isinstance(itemed, Act))
        self.assertEqual(itemed.action, "a shiny ball")


class DayTimeTest(unittest.TestCase):

    def test_attributes(self):
        dt = DayTime("test1", mon=10, day=5, year=2019, hour=12, explain="this is a test")

        self.assertTrue(isinstance(dt, DayTime))
        self.assertEqual(dt.name, "test1")
        self.assertEqual(dt.mon, 10)
        self.assertEqual(dt.day, 5)
        self.assertEqual(dt.year, 2019)
        self.assertEqual(dt.hour, 12)
        self.assertEqual(dt.info, "this is a test")

    def test_look(self):
        dt = DayTime("test1", mon=10, day=5, year=2019, hour=12, explain="this is a test")

        dayed = dt.look("a rainy day")

        self.assertTrue(isinstance(dayed, Act))
        self.assertEqual(dayed.action, "a rainy day")
