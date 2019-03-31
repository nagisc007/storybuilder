# -*- coding: utf-8 -*-
"""Test for action.py
"""
import unittest
from builder.action import _BaseAction, Action, ActionGroup
from builder.basesubject import _BaseSubject
from builder.behavior import Behavior
from builder.enums import ActType, AuxVerb, GroupType, LangType


class BaseActionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: action.py - _BaseAction ****")

    def test_attributes(self):
        data = [
                ("test", "a note"),
                ("", ""),
                ]
        for name, note in data:
            with self.subTest(name=name, note=note):
                tmp = _BaseAction(name, note)
                self.assertIsInstance(tmp, _BaseAction)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.note, note)


class ActionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: action.py - Action ****")

    def setUp(self):
        self.taro = _BaseSubject("Taro", "a man", "he is a boy")
        self.act0 = Action(self.taro, ActType.ACT, Behavior.ACT, (), "test0", "a test0")

    def test_attributes(self):
        data = [
                (self.taro, ActType.ACT, Behavior.ACT, (), "test1", "a test"),
                (self.taro, ActType.ACT, Behavior.ACT, (self.taro,), "test2", "a test2"),
                ]
        for sub, act, behav, obj, info, note in data:
            with self.subTest(sub=sub, act=act, behav=behav, obj=obj, info=info, note=note):
                tmp = Action(sub, act, behav, obj, info, note)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.subject, sub)
                self.assertEqual(tmp.act_type, act)
                self.assertEqual(tmp.behavior, behav)
                self.assertEqual(tmp.objects, obj)
                self.assertEqual(tmp.info, info)
                self.assertEqual(tmp.note, note)
                self.assertEqual(tmp.descriptions, ())
                self.assertEqual(tmp.flag, "")
                self.assertEqual(tmp.deflag, "")
                self.assertEqual(tmp.is_negative, False)
                self.assertEqual(tmp.is_passive, False)
                self.assertEqual(tmp.priority, Action.DEFAULT_PRIORITY)

    def test_desc(self):
        data = [
                ("test0",),
                ("test1", "test is a test"),
                ("",),
                ]
        for d in data:
            with self.subTest(d=d):
                self.act0.desc(*d)
                self.assertEqual(self.act0.descriptions, d)

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
                self.assertEqual(self.act0.aux_verb, v)


class ActionGroupTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: action.py - ActionGroup ****")

    def setUp(self):
        self.taro = _BaseSubject("Taro", "a man", "he is a boy")
        self.act0 = Action(self.taro, ActType.ACT, Behavior.ACT, None, "test act0", "a test0")
        self.act1 = Action(self.taro, ActType.ACT, Behavior.ACT, None, "test act1", "a test1")

    def test_attributes(self):
        data = [
                (GroupType.STORY, LangType.JPN, "test0", (self.act0,)),
                (GroupType.STORY, LangType.JPN, "test1", (self.act0, self.act1)),
                (GroupType.SCENE, None, "test2", (self.act0,)),
                ]
        for group, lng, note, acts in data:
            with self.subTest(group=group, lng=lng, note=note, acts=acts):
                tmp = ActionGroup(group_type=group, lang=lng, note=note, *acts) if lng else ActionGroup(group_type=group, note=note, *acts)
                self.assertIsInstance(tmp, ActionGroup)
                self.assertEqual(tmp.group_type, group)
                self.assertEqual(tmp.lang, lng if lng else LangType.JPN)
                self.assertEqual(tmp.note, note)
                self.assertEqual(tmp.actions, acts)

