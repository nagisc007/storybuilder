# -*- coding: utf-8 -*-
"""Test for subject.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.subject import Person, Day, Item, Stage, Word
from builder.subject import Something, Info, Flag, Nothing
from builder.subject import Action
from builder.enums import ActType


_FILENAME = "subject.py"


class InfoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Info")

    def test_attributes(self):
        data = [
                ("test",
                    Info._NAME, "test"),
                ]

        for v, exp_name, exp_note in data:
            tmp = Info(v)
            self.assertIsInstance(tmp, Info)
            self.assertEqual(tmp.name, exp_name)
            self.assertEqual(tmp.note, exp_note)


class FlagTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Flag")

    def test_attributes(self):
        data = [
                ("test",
                    "test")
                ]

        for v, expected in data:
            tmp = Flag(v)
            self.assertIsInstance(tmp, Flag)
            self.assertEqual(tmp.note, expected)


class NothingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Nothing")

    def test_attributes(self):
        data = [
                (Nothing._NAME, ""),
                ]
        for exp_name, exp_note in data:
            with self.subTest(exp_name=exp_name, exp_note=exp_note):
                tmp = Nothing()
                self.assertIsInstance(tmp, Nothing)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)

class SomethingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Something")

    def test_attributes(self):
        data = [
                (Something._NAME, ""),
                ]

        for exp_name, exp_note in data:
            with self.subTest(exp_name=exp_name, exp_note=exp_note):
                tmp = Something()
                self.assertIsInstance(tmp, Something)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)


class PersonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Person")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student")
        self.hanako = Person("Hanako", 17, "female", "student")

    def test_attributes(self):
        data = [
                ("Taro", 17, "male", "student", "俺", "a man",
                    "Taro", 17, "male", "student", {"me":"俺"}, "a man"),
                ]
        for name, age, sex, job, calling, note, exp_name, exp_age, exp_sex, exp_job, exp_calling, exp_note in data:
            with self.subTest(name=name, age=age, sex=sex, job=job, calling=calling, note=note,
                    exp_name=exp_name, exp_age=exp_age, exp_sex=exp_sex, exp_job=exp_job,
                    exp_calling=exp_calling, exp_note=exp_note):
                tmp = Person(name, age, sex, job, calling, note)
                self.assertIsInstance(tmp, Person)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.age, exp_age)
                self.assertEqual(tmp.sex, exp_sex)
                self.assertEqual(tmp.job, exp_job)
                self.assertEqual(tmp.calling, exp_calling)
                self.assertEqual(tmp.note, exp_note)

    def test_behaviors(self):
        data = [
                ("ask", (self.taro,), "",
                    ActType.TALK, self.hanako, "ask", (self.taro,)),
                ("behav", (self.taro,), "",
                    ActType.BEHAV, self.hanako, "behav", (self.taro,)),
                ("come", (self.taro,), "",
                    ActType.MOVE, self.hanako, "come", (self.taro,)),
                ("deal", (self.taro,), "",
                    ActType.DEAL, self.hanako, "deal", (self.taro,)),
                ("feel", (self.taro,), "",
                    ActType.FEEL, self.hanako, "feel", (self.taro,)),
                ("go", (self.taro,), "",
                    ActType.MOVE, self.hanako, "go", (self.taro,)),
                ("have", (self.taro,), "",
                    ActType.DEAL, self.hanako, "have", (self.taro,)),
                ("hear", (self.taro,), "",
                    ActType.TALK, self.hanako, "hear", (self.taro,)),
                ("know", (self.taro,), "",
                    ActType.THINK, self.hanako, "know", (self.taro,)),
                ("look", (self.taro,), "",
                    ActType.LOOK, self.hanako, "look", (self.taro,)),
                ("move", (self.taro,), "",
                    ActType.MOVE, self.hanako, "move", (self.taro,)),
                ("remember", (self.taro,), "",
                    ActType.THINK, self.hanako, "remember", (self.taro,)),
                ("reply", (self.taro,), "",
                    ActType.TALK, self.hanako, "reply", (self.taro,)),
                ("talk", (self.taro,), "",
                    ActType.TALK, self.hanako, "talk", (self.taro,)),
                ("think", (self.taro,), "",
                    ActType.THINK, self.hanako, "think", (self.taro,)),
                ]

        for attr, obj, verb, exp_type, exp_sub, exp_verb, exp_obj in data:
            with self.subTest(attr=attr, obj=obj, verb=verb,
                    exp_type=exp_type, exp_sub=exp_sub, exp_verb=exp_verb, exp_obj=exp_obj):
                doing = getattr(self.hanako, attr)
                tmp = doing(*obj, verb=verb) if verb else doing(*obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, exp_type)
                self.assertEqual(tmp.subject, exp_sub)
                self.assertEqual(tmp.verb, exp_verb)
                self.assertEqual(tmp.objects, exp_obj)


class DayTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Day")

    def test_attributes(self):
        data = [
                ("test1", 1, 10, 2000, 12, 30, "a note",
                    "test1", 1, 10, 2000, 12, 30, "a note"),
                ("test2", 2, 11, 2001, 13, 31, "",
                    "test2", 2, 11, 2001, 13, 31, ""),
                ("test3", 3, 12, 2002, 14, 32, "",
                    "test3", 3, 12, 2002, 14, 32, ""),
                ("test4", 4, 13, 2003, 15, None, "",
                    "test4", 4, 13, 2003, 15, 0, ""),
                ("test5", 5, 14, 2004, None, None, "",
                    "test5", 5, 14, 2004, 0, 0, ""),
                ("test6", 6, 15, None, None, None, "",
                    "test6", 6, 15, 0, 0, 0, ""),
                ("test7", 7, None, None, None, None, "",
                    "test7", 7, 0, 0, 0, 0, ""),
                ("test8", None, None, None, None, None, "",
                    "test8", 0, 0, 0, 0, 0, ""),
                ]

        def creator(name, mon, day, year, hour, mi, note):
            if mon and day and year and hour and mi and note:
                return Day(name, mon, day, year, hour, mi, note)
            elif mon and day and year and hour and mi:
                return Day(name, mon, day, year, hour, mi)
            elif mon and day and year and hour:
                return Day(name, mon, day, year, hour)
            elif mon and day and year:
                return Day(name, mon, day, year)
            elif mon and day:
                return Day(name, mon, day)
            elif mon:
                return Day(name, mon)
            else:
                return Day(name)

        for name, mon, day, year, hour, mi, note, exp_name, exp_mon, exp_day, exp_year, exp_hour, exp_mi, exp_note in data:
            with self.subTest(name=name, mon=mon, day=day, year=year, hour=hour, mi=mi, note=note,
                exp_name=exp_name, exp_mon=exp_mon, exp_day=exp_day, exp_hour=exp_hour,
                exp_mi=exp_mi, exp_note=exp_note):
                tmp = creator(name, mon, day, year, hour, mi, note)
                self.assertIsInstance(tmp, Day)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.mon, exp_mon)
                self.assertEqual(tmp.day, exp_day)
                self.assertEqual(tmp.year, exp_year)
                self.assertEqual(tmp.hour, exp_hour)
                self.assertEqual(tmp.min, exp_mi)
                self.assertEqual(tmp.note, exp_note)

    def test_elapse(self):
        BASE_NAME = "testday"
        BASE_MON = 10
        BASE_DAY = 10
        BASE_YEAR = 2000
        BASE_HOUR = 12
        BASE_MIN = 30
        BASE_NOTE = "test"
        data = [
                (1, 1, 1, 1, 1, "apple",
                    BASE_MON + 1, BASE_DAY + 1, BASE_YEAR + 1, BASE_HOUR + 1, BASE_MIN + 1,
                    "apple"),
                ]

        for mon, day, year, hour, minu, note, exp_mon, exp_day, exp_year, exp_hour, exp_minu, exp_note in data:
            with self.subTest(mon=mon, day=day, year=year, hour=hour, minu=minu, note=note,
                    exp_mon=exp_mon, exp_day=exp_day, exp_year=exp_year,
                    exp_hour=exp_hour, exp_minu=exp_minu, exp_note=exp_note):
                tmp = Day(BASE_NAME, BASE_MON, BASE_DAY, BASE_YEAR, BASE_HOUR, BASE_MIN, BASE_NOTE)
                act = tmp.elapse(mon, day, year, hour, minu, note)
                self.assertIsInstance(act, Action)
                self.assertEqual(act.subject.name, tmp.name)
                self.assertEqual(act.subject.mon, exp_mon)
                self.assertEqual(act.subject.day, exp_day)
                self.assertEqual(act.subject.year, exp_year)
                self.assertEqual(act.subject.hour, exp_hour)
                self.assertEqual(act.subject.min, exp_minu)
                self.assertEqual(act.subject.note, exp_note)

    def test_elapsed(self):
        base_day = {"mon": 10, "day": 5, "year": 2000, "hour": 12, "min": 30, "note": "base"}
        data = [
                (("test",), 1, 1, 1, 1, 1, "a test", True,
                    ("test",), 11, 6, 2001, 13, 31, "a test"),
                (("test", "apple"), 1, 1, 1, 1, 1, "not added", False,
                    ("test", "apple"), 1, 1, 1, 1, 1, "not added"),
                ]

        for v, mon, day, year, hour, min, note, isadd, exp_v, exp_mon, exp_day, exp_year, exp_hour, exp_min, exp_note in data:
            with self.subTest(v=v, mon=mon, day=day, year=year, hour=hour, min=min, note=note, isadd=isadd,
                    exp_v=exp_v, exp_mon=exp_mon, exp_day=exp_day, exp_year=exp_year,
                    exp_hour=exp_hour, exp_min=exp_min, exp_note=exp_note):
                test_day = Day("test", base_day["mon"], base_day["day"], base_day["year"],
                        base_day["hour"], base_day["min"], base_day["note"])
                tmp = test_day.elapsed(*v, mon=mon, day=day, year=year, hour=hour, min=min, note=note, is_added=isadd)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, ActType.EXPLAIN)
                for o, exp in zip(tmp.objects, exp_v):
                    self.assertEqual(o.note, exp)
                self.assertIsInstance(tmp.subject, Day)
                self.assertEqual(tmp.subject.name, "test")
                self.assertEqual(tmp.subject.mon, exp_mon)
                self.assertEqual(tmp.subject.day, exp_day)
                self.assertEqual(tmp.subject.year, exp_year)
                self.assertEqual(tmp.subject.hour, exp_hour)
                self.assertEqual(tmp.subject.min, exp_min)
                self.assertEqual(tmp.subject.note, exp_note)


class ItemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Item")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student")
        self.hanako = Person("Hanako", 17, "female", "student")

    def test_attributes(self):
        data = [
                ("test", "a note",
                    "test", "a note"),
                ("test", "",
                    "test", ""),
                ]
        for name, note, exp_name, exp_note in data:
            with self.subTest(name=name, note=note, exp_name=exp_name, exp_note=exp_note):
                tmp = Item(name, note) if note else Item(name)
                self.assertIsInstance(tmp, Item)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)

    def test_move(self):
        data = [
                ("move", (self.taro,), "",
                    ActType.MOVE, self.hanako, "move", (self.taro,)),
                ]

        for attr, obj, verb, exp_type, exp_sub, exp_verb, exp_obj in data:
            with self.subTest(attr=attr, obj=obj, verb=verb,
                    exp_type=exp_type, exp_sub=exp_sub, exp_verb=exp_verb, exp_obj=exp_obj):
                doing = getattr(self.hanako, attr)
                tmp = doing(*obj, verb=verb) if verb else doing(*obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, exp_type)
                self.assertEqual(tmp.subject, exp_sub)
                self.assertEqual(tmp.verb, exp_verb)
                self.assertEqual(tmp.objects, exp_obj)


class StageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Stage")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student")
        self.hanako = Person("Hanako", 17, "female", "student")


    def test_attributes(self):
        stage1 = Stage("base", "a base stage")
        data = [
                ("test", "a note", None,
                    "test", "a note", None),
                ("test", "", None,
                    "test", "", None),
                ("child", "a child", stage1,
                    "child", "a child", stage1),
                ]

        for name, note, parent, exp_name, exp_note, exp_parent in data:
            with self.subTest(name=name, note=note, parent=parent,
                    exp_name=exp_name, exp_note=exp_note, exp_parent=exp_parent):
                tmp = Stage(name, note, parent) if note else Stage(name)
                self.assertIsInstance(tmp, Stage)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)
                self.assertEqual(tmp.parent, exp_parent)

    def test_move(self):
        data = [
                ("move", (self.taro,), "",
                    ActType.MOVE, self.hanako, "move", (self.taro,)),
                ]

        for attr, obj, verb, exp_type, exp_sub, exp_verb, exp_obj in data:
            with self.subTest(attr=attr, obj=obj, verb=verb,
                    exp_type=exp_type, exp_sub=exp_sub, exp_verb=exp_verb, exp_obj=exp_obj):
                doing = getattr(self.hanako, attr)
                tmp = doing(*obj, verb=verb) if verb else doing(*obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, exp_type)
                self.assertEqual(tmp.subject, exp_sub)
                self.assertEqual(tmp.verb, exp_verb)
                self.assertEqual(tmp.objects, exp_obj)

    def test_insided(self):
        data = [
                ("test", "a note",
                    "test", "a note"),
                ]

        for name, note, exp_name, exp_note in data:
            with self.subTest(name=name, note=note, exp_name=exp_name, exp_note=exp_note):
                tmp = Stage("base", "a base")
                testtmp = tmp.insided(name, note)
                self.assertIsInstance(testtmp, Stage)
                self.assertEqual(testtmp.name, exp_name)
                self.assertEqual(testtmp.note, exp_note)


class WordTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Word")

    def test_attributes(self):
        data = [
                ("test", "a note",
                    "test", "a note"),
                ("test", "",
                    "test", "")
                ]

        for name, note, exp_name, exp_note in data:
            with self.subTest(name=name, note=note, exp_name=exp_name, exp_note=exp_note):
                tmp = Word(name, note) if note else Word(name)
                self.assertIsInstance(tmp, Word)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)

