# -*- coding: utf-8 -*-
"""Test for base.py
"""
import unittest

from base import ActType, Act, Must, Done, Title, Description, Person, Stage, Item, DayTime

class SampleObj(object):
    def __init__(self, name):
        self.name = name


class ClassCheckTest(unittest.TestCase):
    def test_act_is_not_basic_object(self):
        act1 = Act(SampleObj("testact"), ActType.TEST, "test is good")
        sample1 = SampleObj("test1")

        self.assertNotEqual(act1, sample1) # act object is object?
        self.assertNotEqual(type(act1), type(sample1)) # act object is not object?

    def test_act_params(self):
        sample1 = SampleObj("test1")
        act1 = Act(sample1, ActType.TEST, "test is good")

        self.assertEqual(act1.act_type, ActType.TEST) # act type check
        self.assertEqual(act1.subject, sample1) # subject check
        self.assertEqual(act1.action, "test is good") # action check
        self.assertEqual(act1.withS, False) # with subject check

    def test_title_is_act(self):
        title1 = Title("test1")
        act1 = Act(SampleObj("test1"), ActType.SYMBOL, "test1")

        self.assertNotEqual(title1, act1) # title object is action?
        self.assertTrue(isinstance(title1, type(act1))) # title object is action object

    def test_title_params(self):
        title1 = Title("test1")

        self.assertEqual(title1.action, "test1") # check title
        self.assertEqual(title1.act_type, ActType.SYMBOL) # check type

    def test_description_is_act(self):
        desc1 = Description("test1")
        act1 = Act(SampleObj("test1"), ActType.DESC, "test1")

        self.assertNotEqual(desc1, act1) # description object is action?
        self.assertTrue(isinstance(desc1, type(act1))) # description object is action object

    def test_description_params(self):
        desc1 = Description("test1")

        self.assertEqual(desc1.action, "test1") # check description
        self.assertEqual(desc1.act_type, ActType.DESC) # check type

    def test_person_is_not_action(self):
        person1 = Person("test1", 10, "male", "test is good")
        act1 = Act(SampleObj("test1"), ActType.ACT, "test is good")

        self.assertNotEqual(person1, act1) # person object is action?
        self.assertNotEqual(type(act1), type(person1)) # person object is not action object?

    def test_person_params(self):
        person1 = Person("test1", 10, "male", "worker")

        self.assertEqual(person1.name, "test1") # check name
        self.assertEqual(person1.age, 10) # check age
        self.assertEqual(person1.sex, "male") # check sex
        self.assertEqual(person1.job, "worker") # check job

    def test_stage_is_not_action(self):
        stage1 = Stage("test1", "test is good")
        act1 = Act(SampleObj("test1"), ActType.ACT, "test is good")

        self.assertNotEqual(stage1, act1) # stage object is action?
        self.assertNotEqual(type(stage1), type(act1)) # stage object is not action object?

    def test_stage_params(self):
        stage1 = Stage("test1", "test is good")

        self.assertEqual(stage1.name, "test1") # check name
        self.assertEqual(stage1.explain, "test is good") # check explain

    def test_item_is_not_action(self):
        item1 = Item("test1", "test is good")
        act1 = Act(SampleObj("test1"), ActType.ACT, "test is good")

        self.assertNotEqual(item1, act1) # item object is action?
        self.assertNotEqual(type(item1), type(act1)) # item object is not action object?

    def test_item_params(self):
        item1 = Item("test1", "test is good")

        self.assertEqual(item1.name, "test1") # check name
        self.assertEqual(item1.explain, "test is good") # check explain

    def test_daytime_is_not_action(self):
        daytime1 = DayTime("test1", 1, 10, 2019, 12)
        act1 = Act(SampleObj("test1"), ActType.ACT, "test is good")

        self.assertNotEqual(daytime1, act1) # daytime object is action?
        self.assertNotEqual(type(daytime1), type(act1)) # daytime object is not action object?

    def test_daytime_params(self):
        daytime1 = DayTime("test1", 1, 10, 2019, 12)

        self.assertEqual(daytime1.name, "test1") # check name
        self.assertEqual(daytime1.mon, 1) # check mon
        self.assertEqual(daytime1.day, 10) # check day
        self.assertEqual(daytime1.year, 2019) # check year
        self.assertEqual(daytime1.hour, 12) # check hour
