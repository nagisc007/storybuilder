# -*- coding: utf-8 -*-
"""Test for sbutils.py
"""
import unittest

from builder.sbutils import assert_isclass, assert_isstr, assert_isint
from builder.sbutils import print_test_title


class PublicMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title("sbutils.py", "public methods")

    def test_assert_isclass(self):
        class Sample(object):
            def __init__(self, na):
                self.na = na

        data = [
                (Sample("test"), Sample),
                (("test",), tuple)
                ]

        for v, t in data:
            with self.subTest(v=v, t=t):
                self.assertTrue(assert_isclass(v, t))

    def test_assert_isstr(self):
        data = [
                "test",
                "list",
                ]

        for v in data:
            with self.subTest(v=v):
                self.assertTrue(assert_isstr(v))

    def test_assert_isint(self):
        data = [
                1,
                2,
                ]

        for v in data:
            with self.subTest(v=v):
                self.assertTrue(assert_isint(v))
