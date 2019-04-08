# -*- coding: utf-8 -*-
"""Test for action.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.action import _BaseAction, Action, ActionGroup, Desc, TagAction
from builder.action import _BaseSubject
from builder.action import Behavior
from builder.action import ActType, AuxVerb, GroupType, LangType, TagType
from builder.enums import DescType


_FILENAME = "action.py"


class BaseActionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "_BaseAction")

    def test_attributes(self):
        data = [
                "test",
                "",
                ]
        for name in data:
            with self.subTest(name=name):
                tmp = _BaseAction(name)
                self.assertIsInstance(tmp, _BaseAction)
                self.assertEqual(tmp.name, name)


class ActionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Action")

    def setUp(self):
        self.taro = _BaseSubject("Taro", "a man")
        self.act0 = Action(self.taro, ActType.ACT, Behavior.ACT, ())

    def test_attributes(self):
        data = [
                (self.taro, ActType.ACT, Behavior.ACT, ()),
                (self.taro, ActType.ACT, Behavior.ACT, (self.taro,)),
                ]
        for sub, act, behav, obj in data:
            with self.subTest(sub=sub, act=act, behav=behav, obj=obj):
                tmp = Action(sub, act, behav, obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.subject, sub)
                self.assertEqual(tmp.act_type, act)
                self.assertEqual(tmp.behavior, behav)
                self.assertEqual(tmp.objects, obj)
                self.assertEqual(tmp.descs.data, ())
                self.assertEqual(tmp._auxverb, AuxVerb.NONE)
                self.assertEqual(tmp._flag, "")
                self.assertEqual(tmp._deflag, "")
                self.assertEqual(tmp._is_negative, False)
                self.assertEqual(tmp._is_passive, False)
                self.assertEqual(tmp._priority, Action.DEFAULT_PRIORITY)

    def test_desc(self):
        data = [
                ("test0",),
                ("test1", "test is a test"),
                ("",),
                ]
        for d in data:
            with self.subTest(d=d):
                self.act0.desc(*d)
                self.assertIsInstance(self.act0.descs, Desc)
                self.assertEqual(self.act0.descs.data, d)

    def test_negative(self):
        self.assertFalse(self.act0.is_negative)
        self.act0.negative()
        self.assertTrue(self.act0.negative)

    def test_passive(self):
        self.assertFalse(self.act0.is_passive)
        self.act0.passive()
        self.assertTrue(self.act0.is_passive)

    def test_flag(self):
        data = [
                ("test", "test"),
                ("1", "1"),
                ]
        for flg, expected in data:
            with self.subTest(flg=flg, expected=expected):
                self.act0.set_flag(flg)
                self.assertEqual(self.act0.flag, expected)

    def test_deflag(self):
        data = [
                ("test", "test"),
                ("1", "1"),
                ]
        for flg, expected in data:
            with self.subTest(flg=flg, expected=expected):
                self.act0.set_deflag(flg)
                self.assertEqual(self.act0.deflag, expected)

    def test_priority(self):
        data_set = [(x, x) for x in range(1, 10)]
        for p1, p2 in data_set:
            with self.subTest(p1=p1, p2=p2):
                self.act0.set_priority(p1)
                self.assertEqual(self.act0.priority, p2)

    def test_auxverb(self):
        for v in AuxVerb:
            with self.subTest(v=v):
                if v is AuxVerb.CAN:
                    self.act0.can()
                elif v is AuxVerb.MAY:
                    self.act0.may()
                elif v is AuxVerb.MUST:
                    self.act0.must()
                elif v is AuxVerb.NONE:
                    continue
                elif v is AuxVerb.SHOULD:
                    self.act0.should()
                elif v is AuxVerb.THINK:
                    self.act0.think()
                elif v is AuxVerb.WANT:
                    self.act0.want()
                elif v is AuxVerb.WILL:
                    self.act0.will()
                else:
                    self.fail("Invalid value in AuxVerb")
                self.assertEqual(self.act0.auxverb, v)

    def test_omit(self):
        data = [
                ("test", None, Action.DEFAULT_PRIORITY),
                ("test", True, Action.MIN_PRIORITY),
                ]

        for v, omt, expected in data:
            with self.subTest(v=v, omt=omt, expected=expected):
                tmp = self.taro.explain()
                if omt:
                    tmp.omit()
                self.assertEqual(tmp.priority, expected)

    def test_tell(self):
        data = [
                ("test", False, DescType.DESCRIPTION),
                ("test", True, DescType.DIALOGUE),
                ]

        for doc, dial, expected in data:
            tmp = self.taro.explain()
            if dial:
                tmp.tell(doc)
            else:
                tmp.desc(doc)
            self.assertIsInstance(tmp.descs, Desc)
            self.assertEqual(tmp.descs.desc_type, expected)


class ActionGroupTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "ActionGroup")

    def setUp(self):
        self.taro = _BaseSubject("Taro", "a man")
        self.act0 = Action(self.taro, ActType.ACT, Behavior.ACT, ())
        self.act1 = Action(self.taro, ActType.ACT, Behavior.ACT, ())

    def test_attributes(self):
        data = [
                (GroupType.STORY, LangType.JPN, (self.act0,)),
                (GroupType.STORY, LangType.JPN, (self.act0, self.act1)),
                (GroupType.SCENE, None, (self.act0,)),
                ]
        for group, lng, acts in data:
            with self.subTest(group=group, lng=lng, acts=acts):
                tmp = ActionGroup(group_type=group, lang=lng, *acts) if lng else ActionGroup(group_type=group, *acts)
                self.assertIsInstance(tmp, ActionGroup)
                self.assertEqual(tmp.group_type, group)
                self.assertEqual(tmp.lang, lng if lng else LangType.JPN)
                self.assertEqual(tmp.actions, acts)


class TagActionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "TagAction")

    def test_attributes(self):
        data = [
                (TagType.COMMENT, "a test"),
                (TagType.TITLE, ""),
                ]

        for tag, note in data:
            with self.subTest(tag=tag, note=note):
                tmp = TagAction(tag, note) if note else TagAction(tag)
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tmp.act_type, ActType.TAG)
                self.assertEqual(tmp.behavior, Behavior.NONE)
                self.assertEqual(tmp.objects, ())
                self.assertEqual(tmp.tag, tag)
                self.assertEqual(tmp.note, note)

