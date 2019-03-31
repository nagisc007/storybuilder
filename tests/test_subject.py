# -*- coding: utf-8 -*-
"""Test for subject.py
"""
import unittest
from builder.action import Action, ActionGroup
from builder.behavior import Behavior
from builder.enums import ActType, TagType
from builder.subject import _BasePerson, DayTime, Item, Master, Stage, Word
from builder.subject import Something, something


class BasePersonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: subject.py - BasePerson ****")

    def setUp(self):
        self.taro = _BasePerson("Taro", 17, "male", "student", "a man", "a note")
        self.hanako = _BasePerson("Hanako", 17, "female", "student", "a girl", "a diary")

    def test_attributes(self):
        data = [
                ("Taro", 17, "male", "student", "a man", "a note"),
                ("Hanako", 17, "female", "student", "a girl", None),
                ("Kenta", 20, "male", "driver", None, None),
                ]
        def creator(name, age, sex, job, info, note):
            if info and note:
                return _BasePerson(name, age, sex, job, info, note)
            elif info:
                return _BasePerson(name, age, sex, job, info)
            else:
                return _BasePerson(name, age, sex, job)
        for name, age, sex, job, info, note in data:
            with self.subTest(name=name, age=age, sex=sex, job=job, info=info, note=note):
                tmp = creator(name, age, sex, job, info, note)
                self.assertIsInstance(tmp, _BasePerson)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.age, age)
                self.assertEqual(tmp.sex, sex)
                self.assertEqual(tmp.job, job)
                self.assertEqual(tmp.info, info if info else "")
                self.assertEqual(tmp.note, note if note else "")

    def test_act(self):
        tmp = self.taro.act(Behavior.TEST, None, "a test", "a test note")
        self.assertIsInstance(tmp, Action)
        self.assertEqual(tmp.act_type, ActType.ACT)
        self.assertEqual(tmp.behavior, Behavior.TEST)
        self.assertEqual(tmp.info, "a test")
        self.assertEqual(tmp.note, "a test note")
        self.assertEqual(tmp.objects, ())

    def test_explain(self):
        data = [
                ("a test0", "a note0", ()),
                ("a test1", "a note1", (self.hanako,)),
                ("a test2", "a note2", (self.taro, self.hanako)),
                ("a test3", "", ()),
                ]
        def creator(info, note, obj):
            if note and obj:
                return self.taro.explain(info, *obj, note=note)
            elif note:
                return self.taro.explain(info, note=note)
            else:
                return self.taro.explain(info)
        for info, note, obj in data:
            with self.subTest(info=info, note=note, obj=obj):
                tmp = creator(info, note, obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, ActType.EXPLAIN)
                self.assertEqual(tmp.behavior, Behavior.EXPLAIN)
                self.assertEqual(tmp.info, info)
                self.assertEqual(tmp.note, note)
                self.assertEqual(set(tmp.objects) - {None}, set(obj))

    def test_tell(self):
        data = [
                ("a test0", "a note0", ()),
                ("a test1", "a note1", (self.hanako,)),
                ("a test2", "a note2", (self.taro, self.hanako)),
                ("a test3", "", ()),
                ]
        def creator(info, note, obj):
            if note and obj:
                return self.taro.tell(info, *obj, note=note)
            elif note:
                return self.taro.tell(info, note=note)
            else:
                return self.taro.tell(info)
        for info, note, obj in data:
            with self.subTest(info=info, note=note, obj=obj):
                tmp = creator(info, note, obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, ActType.TELL)
                self.assertEqual(tmp.behavior, Behavior.TELL)
                self.assertEqual(tmp.info, info)
                self.assertEqual(tmp.note, note)
                self.assertEqual(set(tmp.objects) - {None}, set(obj))


class DayTimeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: subject.py - DayTime ****")

    def test_attributes(self):
        data = [
                ("test1", 1, 10, 2000, 12, 30, "a info", "a note"),
                ("test2", 2, 11, 2001, 13, 31, "a info", None),
                ("test3", 3, 12, 2002, 14, 32, None, None),
                ("test4", 4, 13, 2003, 15, None, None, None),
                ("test5", 5, 14, 2004, None, None, None, None),
                ("test6", 6, 15, None, None, None, None, None),
                ("test7", 7, None, None, None, None, None, None),
                ("test8", None, None, None, None, None, None, None),
                ]
        def creator(name, mon, day, year, hour, mi, info, note):
            if mon and day and year and hour and mi and info and note:
                return DayTime(name, mon, day, year, hour, mi, info, note)
            elif mon and day and year and hour and mi and info:
                return DayTime(name, mon, day, year, hour, mi, info)
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
        for name, mon, day, year, hour, mi, info, note in data:
            with self.subTest(name=name, mon=mon, day=day, year=year, hour=hour, mi=mi, info=info, note=note):
                tmp = creator(name, mon, day, year, hour, mi, info, note)
                self.assertIsInstance(tmp, DayTime)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.mon, mon if mon else 0)
                self.assertEqual(tmp.day, day if day else 0)
                self.assertEqual(tmp.year, year if year else 0)
                self.assertEqual(tmp.hour, hour if hour else 0)
                self.assertEqual(tmp.min, mi if mi else 0)
                self.assertEqual(tmp.info, info if info else "")
                self.assertEqual(tmp.note, note if note else "")


class ItemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: subject.py - Item ****")

    def test_attributes(self):
        data = [
                ("a test", "a info", "a note"),
                ("a test", "a info", ""),
                ("a test", "", ""),
                ]
        def creator(name, info, note):
            if info and note:
                return Item(name, info, note)
            elif info:
                return Item(name, info)
            else:
                return Item(name)
        for name, info, note in data:
            with self.subTest(name=name, info=info, note=note):
                tmp = creator(name, info, note)
                self.assertIsInstance(tmp, Item)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.info, info)
                self.assertEqual(tmp.note, note)


class MasterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: subject.py - Master ****")

    def setUp(self):
        self.ma = Master('test')
        self.taro = _BasePerson("Taro", 17, "male", "student")

    def test_attributes(self):
        data = [
                ("a test", "a info", "a note"),
                ("a test", "a info", ""),
                ("a test", "", ""),
                ]

        def creator(name, info, note):
            if info and note:
                return Master(name, info, note)
            elif info:
                return Master(name, info)
            else:
                return Master(name)

        for name, info, note in data:
            with self.subTest(name=name, info=info, note=note):
                tmp = creator(name, info, note)
                self.assertIsInstance(tmp, Master)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.info, info)
                self.assertEqual(tmp.note, note)

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
                self.assertEqual(tmp.info, cmt)
                self.assertEqual(tmp.note, str(TagType.COMMENT))

    def test_scene(self):
        pass

    def test_story(self):
        pass

    def test_title(self):
        pass


class StageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: subject.py - Stage ****")

    def test_attributes(self):
        data = [
                ("a test", "a info", "a note"),
                ("a test", "a info", ""),
                ("a test", "", ""),
                ]

        def creator(name, info, note):
            if info and note:
                return Stage(name, info, note)
            elif info:
                return Stage(name, info)
            else:
                return Stage(name)

        for name, info, note in data:
            with self.subTest(name=name, info=info, note=note):
                self.assertIsInstance(tmp, Stage)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.info, info)
                self.assertEqual(tmp.note, note)


class SomethingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: subject.py - Something ****")

    def test_attributes(self):
        data = [
                (Something._NAME, "", "")
                ]
        for name, info, note in data:
            with self.subTest(name=name, info=info, note=note):
                tmp = Something()
                self.assertIsInstance(tmp, Something)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.info, info)
                self.assertEqual(tmp.note, note)


class WordTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: subject.py - Word ****")

    def test_attributes(self):
        data = [
                ("a test", "a info", "a note"),
                ("a test", "a info", ""),
                ("a test", "", "")
                ]

        def creator(name, info, note):
            if info and note:
                return Word(name, info, note)
            elif info:
                return Word(name, info)
            else:
                return Word(name)

        for name, info, note in data:
            with self.subTest(name=name, info=info, note=note):
                tmp = creator(name, info, note)
                self.assertIsInstance(tmp, Word)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.info, info)
                self.assertEqual(tmp.note, note)

