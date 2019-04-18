# -*- coding: utf-8 -*-
"""Test for strutils.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.enums import LangType
import builder.strutils as strutils


_FILENAME = "strutils.py"


class PublicMethodTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "public methods")

    def test_double_comma_chopped(self):
        data = [
                ("　これを。。ただしく。。", LangType.JPN,
                    "　これを。ただしく。"),
                (" This is a pen.. the pen. ", LangType.ENG,
                    " This is a pen. the pen. "),
                ]

        for v, lng, expected in data:
            with self.subTest(v=v, lng=lng, expected=expected):
                self.assertEqual(strutils.double_comma_chopped(v, lng), expected)

    def test_extraend_chopped(self):
        data = [
                ("！。", LangType.JPN,
                    "！"),
                ("？。", LangType.JPN,
                    "？"),
                ("!. ", LangType.ENG,
                    "!"),
                ("?. ", LangType.ENG,
                    "?")
                ]

        for v, lng, expected in data:
            with self.subTest(v=v, lng=lng, expected=expected):
                self.assertEqual(strutils.extraend_chopped(v, lng), expected)

    def test_extraspace_chopped(self):
        data = [
                ("　これを。　ただしくする。", LangType.JPN,
                    "　これを。ただしくする。"),
                (" This is a pen.  the pen. ", LangType.ENG,
                    " This is a pen. the pen. "),
                ("　これを。、ただしくして。", LangType.JPN,
                    "　これを。ただしくして。"),
                ("「これを」　正しくする。", LangType.JPN,
                    "「これを」正しくする。"),
                ]

        for v, lng, expected in data:
            with self.subTest(v=v, lng=lng, expected=expected):
                self.assertEqual(strutils.extraspace_chopped(v, lng), expected)


