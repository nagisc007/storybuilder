# -*- coding: utf-8 -*-
"""Test for description.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.description import _BaseDesc, Desc, DescGroup, DescType


_FILENAME = "description.py"


class BaseDescTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "_BaseDesc")

    def test_attributes(self):
        pass


class DescTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Desc")

    def test_attributes(self):
        data = [
                (("test",), DescType.DESCRIPTION,
                    ("test",), DescType.DESCRIPTION),
                (("test", "apple"), DescType.DESCRIPTION,
                    ("test", "apple"), DescType.DESCRIPTION),
                ("", DescType.DESCRIPTION,
                    (), DescType.DESCRIPTION),
                ]

        for v, dtype, expected, exp_type in data:
            with self.subTest(v=v, dtype=dtype, expected=expected, exp_type=exp_type):
                tmp = Desc(v, dtype)
                self.assertIsInstance(tmp, Desc)
                self.assertEqual(tmp.data, expected)
                self.assertEqual(tmp.desc_type, exp_type)


class DescGroupTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "DescGroup")

    def test_attributes(self):
        pass

