# -*- coding: utf-8 -*-
"""Test for commons.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.action import Action, Description
from builder.basesubject import _BaseSubject
from builder.behavior import Behavior
from builder.enums import ActType, LangType
from builder.person import Person
from builder.subject import Something, Item
import builder.commons as commons


_FILENAME = "commons.py"


class PublicMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "public methods")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student")
        self.hanako = Person("Hanako", 17, "female", "student")
        self.item = Item("stick")

    def test_behavior_with_np_of(self):
        data = [
                (Behavior.DO, True, False, "~~する~~"),
                (Behavior.DO, False, True, "_する_"),
                (Behavior.DO, True, True, "~~_する~~_"),
                ]

        for behav, nega, pas, expected in data:
            with self.subTest(behav=behav, nega=nega, pas=pas, expected=expected):
                tmp = Action(self.taro, ActType.ACT, behav, ())
                self.assertFalse(tmp.is_negative)
                self.assertFalse(tmp.is_passive)
                if nega:
                    tmp.negative()
                if pas:
                    tmp.passive()
                self.assertEqual(tmp.is_negative, nega)
                self.assertEqual(tmp.is_passive, pas)
                self.assertEqual(commons.behavior_with_np_of(tmp), expected)

    def test_comma_of(self):
        data = [
                (LangType.JPN, "、"),
                (LangType.ENG, ", ")
                ]
        for lang, expected in data:
            with self.subTest(lang=lang, expected=expected):
                self.assertEqual(commons.comma_of(lang), expected)

    def test_description_of(self):
        data = [
                (("test",), LangType.JPN, "test"),
                (("test", "is"), LangType.JPN, "test、is"),
                (("test", "is"), LangType.ENG, "test, is"),
                ]

        for dsc, lng, expected in data:
            tmp = Action(self.taro, ActType.ACT, Behavior.DO, ())
            self.assertIsInstance(tmp, Action)
            self.assertIsInstance(tmp.descs, Description)
            self.assertFalse(tmp.descs.data)
            tmp.desc(*dsc)
            self.assertIsInstance(tmp.descs, Description)
            self.assertEqual(tmp.descs.data, dsc)
            self.assertEqual(commons.description_of(tmp, lng), expected)

    def test_description_of_if(self):
        data = [
                (self.taro.talk().desc("test"), LangType.JPN,
                    "test"),
                (self.taro.talk().desc("test", "apple"), LangType.JPN,
                    "test、apple"),
                (self.taro.talk().desc("test", "apple"), LangType.ENG,
                    "test, apple"),
                (self.taro.talk(), LangType.JPN,
                    "")
                ]

        for act, lng, expected in data:
            with self.subTest(act=act, lng=lng, expected=expected):
                self.assertEqual(commons.descriptions_of_if(act, lng), expected)

    def test_dialogue_from_description(self):
        data = [
                (self.taro.tell().desc("test"), LangType.JPN,
                    "「test」"),
                (self.taro.tell().desc("test", "test"), LangType.JPN,
                    "「test、test」"),
                (self.taro.tell().desc("test", "test"), LangType.ENG,
                    ' "test, test" '),
                ]

        for act, lng, expected in data:
            with self.subTest(act=act, lng=lng, expected=expected):
                self.assertEqual(commons.dialogue_from_description(act, lng), expected)

    def test_dialogue_from_description_if(self):
        data = [
                (self.taro.tell().desc("test"), LangType.JPN,
                    "「test」"),
                (self.taro.tell("a test"), LangType.JPN,
                    "「a test」"),
                ]

        for act, lng, expected in data:
            with self.subTest(act=act, lng=lng, expected=expected):
                self.assertEqual(commons.dialogue_from_description_if(act, lng), expected)

    def test_dialogue_from_info(self):
        data = [
                (self.taro.tell("test"), LangType.JPN,
                    "「test」"),
                (self.taro.tell("test", "apple"), LangType.JPN,
                    "「test、apple」"),
                (self.taro.tell("test", "apple"), LangType.ENG,
                    ' "test, apple" ')
                ]

        for act, lng, expected in data:
            with self.subTest(act=act, lng=lng, expected=expected):
                self.assertEqual(commons.dialogue_from_info(act, lng), expected)

    def test_extraspace_chopped(self):
        data = [
                ("　これを。　ただしくする。", LangType.JPN,
                    "　これを。ただしくする。"),
                (" This is a pen.  the pen. ", LangType.ENG,
                    " This is a pen. the pen. "),
                ]

        for v, lng, expected in data:
            with self.subTest(v=v, lng=lng, expected=expected):
                self.assertEqual(commons.extraspace_chopped(v, lng), expected)

    def test_infos_of(self):
        taro = Person("Taro", 17, "male", "student")
        data = [
                (("test",), "test"),
                (("test", "must"), "test/must"),
                ((taro,), ""),
                ((taro, "test"), "test"),
                ]

        for infos, expected in data:
            with self.subTest(infos=infos, expected=expected):
                tmp = taro.tell(*infos)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(commons.infos_of(tmp), expected)

    def test_object_names_of(self):
        data = [
                (self.taro.talk(self.hanako),
                    "Hanako"),
                (self.taro.talk(self.hanako, self.item),
                    "Hanako/stick"),
                (self.taro.talk("test"),
                    ""),
                ]

        for act, expected in data:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(commons.object_names_of(act), expected)

    def test_object_names_of_without_something(self):
        data = [
                (self.taro.talk(),
                    ""),
                (self.taro.talk(self.hanako),
                    "Hanako"),
                (self.taro.talk(self.hanako, self.item),
                    "Hanako/stick"),
                (self.taro.talk("test", self.hanako),
                    "Hanako"),
                (self.taro.talk(Something()),
                    "")
                ]

        for act, expected in data:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(commons.object_names_of_without_something(act),
                        expected)


    def test_objects_all_from(self):
        data = [
                (self.taro.talk(),
                    ()),
                (self.taro.talk(self.hanako),
                    ("_person:Hanako",)),
                (self.taro.talk(self.hanako, self.item),
                    ("_person:Hanako", "_item:stick")),
                (self.taro.talk(self.hanako, "test"),
                    ("_person:Hanako", "_information:test"))
                ]

        for act, expected in data:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(commons.objects_all_from(act), set(expected))

    def test_objects_from(self):
        data = [
                (self.taro.talk(),
                    ()),
                (self.taro.talk(self.hanako),
                    ("_person:Hanako",)),
                (self.taro.talk(self.hanako, self.item),
                    ("_person:Hanako", "_item:stick")),
                (self.taro.talk(self.hanako, "test"),
                    ("_person:Hanako",)),
                (self.taro.talk(self.hanako, Something()),
                    ("_person:Hanako", "_something:何か"))
                ]

        for act, expected in data:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(commons.objects_from(act), set(expected))

    def test_objects_from_without_something(self):
        data = [
                (self.taro.talk(self.hanako),
                    ("_person:Hanako",)),
                (self.taro.talk(self.hanako, "test"),
                    ("_person:Hanako",)),
                (self.taro.talk(self.hanako, Something()),
                    ("_person:Hanako",))
                ]

        for act, expected in data:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(commons.objects_from_without_something(act.objects),
                        set(expected))

    def test_objects_from_action_without_something(self):
         data = [
                (self.taro.talk(self.hanako),
                    ("_person:Hanako",)),
                (self.taro.talk(self.hanako, "test"),
                    ("_person:Hanako",)),
                (self.taro.talk(self.hanako, Something()),
                    ("_person:Hanako",))
                ]

         for act, expected in data:
             with self.subTest(act=act, expected=expected):
                self.assertEqual(commons.objects_from_action_without_something(act),
                     set(expected))

    def test_sentence_from(self):
        data = [
                (self.taro.talk().desc("test"), LangType.JPN,
                    "　test。"),
                (self.taro.talk().desc("test", "apple"), LangType.JPN,
                    "　test、apple。"),
                (self.taro.talk().desc("test", "apple"), LangType.ENG,
                    ' test, apple. ')
                ]

        for act, lng, expected in data:
            with self.subTest(act=act, lng=lng, expected=expected):
                self.assertEqual(commons.sentence_from(act, lng), expected)

    def test_something_name_if(self):
        data = [
                (_BaseSubject("test taro", ""), "test taro"),
                (Something(), "何か")
                ]
        for obj, expected in data:
            with self.subTest(obj=obj, expected=expected):
                self.assertEqual(commons.something_name_if(obj), expected)

    def test_subject_name_of(self):
        taro = Person("Taro", 17, "male", "student")
        some = Something()
        data = [
                (taro.explain("test taro"), "Taro"),
                (Action(some, ActType.ACT, Behavior.NONE, ()), "何か"),
                ]
        for act, expected in data:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(commons.subject_name_of(act), expected)


class PrivateMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "private methods")

    def test_space_replaced_if_with_symbol(self):
        data = [
                ("!,", LangType.ENG, "! "),
                ("?,", LangType.ENG, "? "),
                ("!?,", LangType.ENG, "!? "),
                ("！、", LangType.JPN, "！　"),
                ("？、", LangType.JPN, "？　"),
                ("！？、", LangType.JPN, "！？　"),
                ]

        for origin, lng, expected in data:
            with self.subTest(origin=origin, lng=lng, expected=expected):
                self.assertEqual(commons._space_replaced_if_with_symbol(
                    origin, lng), expected)

    def test_endpoint_replaced_if_with_comma(self):
        data = [
                (",.", LangType.ENG, "."),
                (", .", LangType.ENG, ", ."),
                ("、。", LangType.JPN, "。"),
                ]

        for origin, lng, expected in data:
            with self.subTest(origin=origin, lng=lng, expected=expected):
                self.assertEqual(commons._endpoint_replaced_if_with_comma(
                    origin, lng), expected)
