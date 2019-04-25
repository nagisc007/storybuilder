# -*- coding: utf-8 -*-
"""Test: testutils.py
"""
import unittest
from builder.testutils import print_test_title
from builder import action as act
from builder import enums as em
from builder import person as psn
from builder import day as dy
from builder import stage as stg
from builder import info as inf
from builder import item as itm
from builder import testutils as tutl


_FILENAME = "testutils.py"


class PublicMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "public methods")

    def setUp(self):
        self.taro = psn.Person("Taro", 17, "male", "student")
        self.hanako = psn.Person("Hanako", 17, "female", "student")
        self.box = itm.Item("Box", "a box")
        self.bus = stg.Stage("Bus", "a bus")
        self.day = dy.Day("Test day")

    def test_exists_basic_infos(self):
        data = [
                ((self.taro.be(self.bus, self.day), self.hanako.be()),
                    self.taro, self.hanako, False, True),
                ((self.taro.be(),),
                    self.hanako, self.hanako, True, False),
                ((self.taro.be(), self.hanako.be()),
                    self.taro, self.hanako, True, False),
                ]

        for v, hero, rival, isfail, expected in data:
            with self.subTest(v=v, hero=hero, rival=rival, isfail=isfail,
                    expected=expected):
                if isfail:
                    with self.assertRaises(AssertionError):
                        self.assertEqual(tutl.exists_basic_infos(self, v, hero, rival),
                                expected)
                else:
                    self.assertEqual(tutl.exists_basic_infos(self, v, hero, rival),
                            expected)

    def test_exists_outline_infos(self):
        data = [
                ((self.taro.go(), self.taro.talk(), self.taro.meet(self.hanako), self.taro.ask()),
                    self.taro.go(), self.taro.talk(),
                    self.taro.meet(self.hanako), self.taro.ask(),
                    False, False, True),
                ((self.taro.be(), self.taro.talk(self.hanako), self.taro.go()),
                    self.taro.go(), self.taro.be(),
                    self.taro.talk(), self.taro.go(),
                    False, True, False),
                ((self.taro.be(), self.taro.talk(self.hanako), self.taro.go()),
                    self.taro.go(), self.taro.be(),
                    self.taro.talk(), self.taro.go(),
                    True, False, True),
                ]

        for v, what, why, how, res, fuz, isfail, expected in data:
            with self.subTest(v=v, what=what, why=why, how=how, res=res, fuz=fuz,
                    isfail=isfail, expected=expected):
                if isfail:
                    with self.assertRaises(AssertionError):
                        self.assertEqual(tutl.exists_outline_infos(self, v, what, why,
                            how, res, fuz), expected)
                else:
                    self.assertEqual(tutl.exists_outline_infos(self, v, what, why, how,
                        res, fuz), expected)

    def test_followed_all_flags(self):
        pass

    def test_is_all_actions_in(self):
        data = [
                ((self.taro.be(), self.hanako.be()),
                    True),
                ((self.taro,),
                    False),
                ((act.ActionGroup(self.taro.be(), self.taro.be(),
                    group_type=em.GroupType.SCENE),),
                    True),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(tutl.is_all_actions_in(v), expected)
