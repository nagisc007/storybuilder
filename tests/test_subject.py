# -*- coding: utf-8 -*-
"""Test for subject.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.subject import _BasePerson, DayTime, Item, Master, Stage, Word
from builder.subject import Something, something
from builder.subject import Action, ActionGroup, TagAction
from builder.subject import Behavior
from builder.subject import ActType, TagType

_FILENAME = "subject.py"


class BasePersonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "BasePerson")

    def setUp(self):
        self.taro = _BasePerson("Taro", 17, "male", "student", "a man")
        self.hanako = _BasePerson("Hanako", 17, "female", "student", "a girl")

    def test_attributes(self):
        data = [
                ("Taro", 17, "male", "student", "a man"),
                ("Hanako", 17, "female", "student", ""),
                ]

        def creator(name, age, sex, job, note):
            if note:
                return _BasePerson(name, age, sex, job, note)
            else:
                return _BasePerson(name, age, sex, job)

        for name, age, sex, job, note in data:
            with self.subTest(name=name, age=age, sex=sex, job=job, note=note):
                tmp = creator(name, age, sex, job, note)
                self.assertIsInstance(tmp, _BasePerson)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.age, age)
                self.assertEqual(tmp.sex, sex)
                self.assertEqual(tmp.job, job)
                self.assertEqual(tmp.note, note)
                self.assertEqual(tmp.parent, None)

    def test_act(self):
        data = [
                (Behavior.ACT, (self.taro,)),
                (Behavior.DO, (self.taro, self.hanako)),
                (Behavior.TEST, ()),
                ]

        for behav, obj in data:
            with self.subTest(behav=behav, obj=obj):
                tmp = self.taro.act(behav, obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, ActType.ACT)
                self.assertEqual(tmp.behavior, behav)
                self.assertEqual(tmp.subject, self.taro)
                self.assertEqual(tmp.objects, obj)

    def test_inherit(self):
        pass

    def test_tell(self):
        pass


class DayTimeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "DayTime")

    def test_attributes(self):
        data = [
                ("test1", 1, 10, 2000, 12, 30, "a note"),
                ("test2", 2, 11, 2001, 13, 31, ""),
                ("test3", 3, 12, 2002, 14, 32, ""),
                ("test4", 4, 13, 2003, 15, None, ""),
                ("test5", 5, 14, 2004, None, None, ""),
                ("test6", 6, 15, None, None, None, ""),
                ("test7", 7, None, None, None, None, ""),
                ("test8", None, None, None, None, None, ""),
                ]

        def creator(name, mon, day, year, hour, mi, note):
            if mon and day and year and hour and mi and note:
                return DayTime(name, mon, day, year, hour, mi, note)
            elif mon and day and year and hour and mi:
                return DayTime(name, mon, day, year, hour, mi)
            elif mon and day and year and hour:
                return DayTime(name, mon, day, year, hour)
            elif mon and day and year:
                return DayTime(name, mon, day, year)
            elif mon and day:
                return DayTime(name, mon, day)
            elif mon:
                return DayTime(name, mon)
            else:
                return DayTime(name)

        def _val_if(v):
            return v if v else 0

        for name, mon, day, year, hour, mi, note in data:
            with self.subTest(name=name, mon=mon, day=day, year=year, hour=hour, mi=mi, note=note):
                tmp = creator(name, mon, day, year, hour, mi, note)
                self.assertIsInstance(tmp, DayTime)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.mon, _val_if(mon))
                self.assertEqual(tmp.day, _val_if(day))
                self.assertEqual(tmp.year, _val_if(year))
                self.assertEqual(tmp.hour, _val_if(hour))
                self.assertEqual(tmp.min, _val_if(mi))
                self.assertEqual(tmp.note, note)

    def test_inherit(self):
        pass


class ItemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Item")

    def test_attributes(self):
        data = [
                ("a test", "a note"),
                ("a test", ""),
                ]
        for name, note in data:
            with self.subTest(name=name, note=note):
                tmp = Item(name, note) if note else Item(name)
                self.assertIsInstance(tmp, Item)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.note, note)

    def test_inherit(self):
        pass


class MasterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: subject.py - Master ****")

    def setUp(self):
        self.ma = Master('test')
        self.taro = _BasePerson("Taro", 17, "male", "student")

    def test_attributes(self):
        data = [
                ("a test", "a note"),
                ("a test", ""),
                ]

        for name, note in data:
            with self.subTest(name=name, note=note):
                tmp = Master(name, note) if note else Master(name)
                self.assertIsInstance(tmp, Master)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.note, note)

    def test_break_symbol(self):
        data = [
                ("****", "****"),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.ma.break_symbol(v)
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tmp.act_type, ActType.TAG)
                self.assertEqual(tmp.behavior, Behavior.NONE)
                self.assertEqual(tmp.tag, TagType.SYMBOL)
                self.assertEqual(tmp.note, expected)

    def test_combine(self):
        data = [
                ((self.taro.tell("a test"),), 1),
                ((self.taro.tell("a test"), self.taro.tell("a test")), 2),
                ]

        for args, expected in data:
            with self.subTest(args=args, expected=expected):
                tmp = self.ma.combine(*args)
                self.assertIsInstance(tmp, ActionGroup)
                self.assertEqual(len(tmp.actions), expected)
                self.assertEqual(tmp.actions, args)

    def test_comment(self):
        data = [
                ("a test"),
                ]
        for cmt in data:
            with self.subTest(cmt=cmt):
                tmp = self.ma.comment(cmt)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, ActType.TAG)
                self.assertEqual(tmp.behavior, Behavior.NONE)
                self.assertEqual(tmp.tag, TagType.COMMENT)
                self.assertEqual(tmp.note, cmt)

    def test_scene(self):
        pass

    def test_story(self):
        pass

    def test_title(self):
        pass


class StageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Stage")

    def test_attributes(self):
        data = [
                ("a test", "a note"),
                ("a test", ""),
                ]

        for name, note in data:
            with self.subTest(name=name, note=note):
                tmp = Stage(name, note) if note else Stage(name)
                self.assertIsInstance(tmp, Stage)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.note, note)

    def test_inherit(self):
        pass


class SomethingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Something")

    def test_attributes(self):
        data = [
                (Something.CLS_NAME, "")
                ]
        for name, note in data:
            with self.subTest(name=name, note=note):
                tmp = Something()
                self.assertIsInstance(tmp, Something)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.note, note)


class WordTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Word")

    def test_attributes(self):
        data = [
                ("a test", "a note"),
                ("a test", "")
                ]

        for name, note in data:
            with self.subTest(name=name, note=note):
                tmp = Word(name, note) if note else Word(name)
                self.assertIsInstance(tmp, Word)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.note, note)

    def test_inherit(self):
        data = [
                ("test", "a test"),
                ("1", "123"),
                ]

        for name, note in data:
            with self.subTest(name=name, note=note):
                tmp = Word(name, note)
                tmp2 = tmp.inherit(name, note)
                self.assertIsInstance(tmp, Word)
                self.assertIsInstance(tmp2, Word)
                self.assertNotEqual(tmp, tmp2)

