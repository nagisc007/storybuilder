# -*- coding: utf-8 -*-
"""Test for analyzer.py
"""
import unittest
from builder.testutils import print_test_title
from builder import action as act
from builder import enums as em
from builder import person as psn
from builder import item as itm
from builder import analyzer as ayz


_FILENAME = "analyzer.py"


class PublicMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "public methods")

    def setUp(self):
        self.taro = psn.Person("Taro", 17, "male", "student")
        self.box = itm.Item("Box", "a box")

    def test_count_acttypes(self):
        data = [
                ((self.taro.be(),),
                    em.ActType.BE, 1),
                ((self.taro.be(), self.taro.do(), self.taro.do()),
                    em.ActType.DO, 2),
                ]

        for v, atype, expected in data:
            with self.subTest(v=v, atype=atype, expected=expected):
                tmp = ayz.count_acttypes(v)
                self.assertIsInstance(tmp, dict)
                self.assertEqual(tmp[atype], expected)

    def test_count_description_at_action(self):
        data = [
                (self.taro.be().d("test"),
                    False, 4),
                (self.taro.be().d("test", "apple"),
                    False, 9),
                (self.taro.be().d("test", "apple"),
                    True, 11),
                ]

        for v, strict, expected in data:
            with self.subTest(v=v, strict=strict, expected=expected):
                self.assertEqual(ayz.count_descripton_at_action(v, strict), expected)

    def test_count_subjects_in(self):
        taro1 = self.taro.be("test")
        data = [
                ((taro1,),
                    psn.Person, 1),
                ]

        for v, target, expected in data:
            with self.subTest(v=v, target=target, expected=expected):
                self.assertEqual(ayz.count_subjects_in(v, target), expected)

    def test_has_a_subject_in(self):
        data = [
                ((self.taro.be(),),
                    psn.Person, True),
                ((self.taro.be(),),
                    itm.Item, False),
                ((self.taro.have(self.box),),
                    itm.Item, True),
                ]

        for v, cls, expected in data:
            with self.subTest(v=v, cls=cls, expected=expected):
                self.assertEqual(ayz.has_a_subject_in(v, cls), expected)

    def test_has_the_action_in(self):
        data = [
                ((self.taro.be(),),
                    self.taro.be(), True),
                ]

        for v, target, expected in data:
            with self.subTest(v=v, target=target, expected=expected):
                self.assertEqual(ayz.has_the_action_in(v, target), expected)

    def test_has_the_subject_in(self):
        data = [
                ((self.taro.be(),),
                    self.taro, True),
                ]

        for v, target, expected in data:
            with self.subTest(v=v, target=target, expected=expected):
                self.assertEqual(ayz.has_the_subject_in(v, target), expected)
