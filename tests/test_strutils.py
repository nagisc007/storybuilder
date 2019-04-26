# -*- coding: utf-8 -*-
"""Test for strutils.py
"""
import unittest
from builder.testutils import print_test_title
from builder import enums as em
from builder import strutils as utl


_FILENAME = "strutils.py"


class PublicMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "public methods")

    def test_comment_tag_from(self):
        data = [
                ("test", "<!--test-->"),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(utl.comment_tag_from(v), expected)

    def test_double_comma_chopped(self):
        data = [
                ("　これを。。ただしく。。", em.LangType.JPN,
                    "　これを。ただしく。"),
                (" This is a pen.. the pen. ", em.LangType.ENG,
                    " This is a pen. the pen. "),
                ]

        for v, lang, expected in data:
            with self.subTest(v=v, lang=lang, expected=expected):
                self.assertEqual(utl.double_comma_chopped(v, lang), expected)

    def test_em_tag_from(self):
        data = [
                ("test", 1, "_test_"),
                ("test", 2, "**test**"),
                ("test", 3, "***test***"),
                ]

        for v, lv, expected in data:
            with self.subTest(v=v, lv=lv, expected=expected):
                self.assertEqual(utl.em_tag_from(v, lv), expected)

    def test_extraend_chopped(self):
        data = [
                ("！。", em.LangType.JPN,
                    "！"),
                ("？。", em.LangType.JPN,
                    "？"),
                ("!. ", em.LangType.ENG,
                    "!"),
                ("?. ", em.LangType.ENG,
                    "?")
                ]

        for v, lang, expected in data:
            with self.subTest(v=v, lang=lang, expected=expected):
                self.assertEqual(utl.extraend_chopped(v, lang), expected)

    def test_extraspace_chopped(self):
        data = [
                ("　これを。　ただしくする。", em.LangType.JPN,
                    "　これを。ただしくする。"),
                (" This is a pen.  the pen. ", em.LangType.ENG,
                    " This is a pen. the pen. "),
                ("　これを。、ただしくして。", em.LangType.JPN,
                    "　これを。ただしくして。"),
                ("「これを」　正しくする。", em.LangType.JPN,
                    "「これを」正しくする。"),
                ]

        for v, lang, expected in data:
            with self.subTest(v=v, lang=lang, expected=expected):
                self.assertEqual(utl.extraspace_chopped(v, lang), expected)

    def test_head_tag_from(self):
        data = [
                ("test", 1, "# test"),
                ("test", 2, "## test"),
                ]

        for v, lv, expected in data:
            with self.subTest(v=v, lv=lv, expected=expected):
                self.assertEqual(utl.head_tag_from(v, lv), expected)

    def test_hr_tag_from(self):
        data = [
                (1, "--------"),
                (2, "--------"*2),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(utl.hr_tag_from(v), expected)

    def test_link_tag_from(self):
        data = [
                ("test", "apple", "[test](apple)"),
                ]

        for v, link, expected in data:
            with self.subTest(v=v, link=link, expected=expected):
                self.assertEqual(utl.link_tag_from(v, link), expected)

    def test_quote_tag_from(self):
        data = [
                ("test", "> test"),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(utl.quote_tag_from(v), expected)

    def test_reflink_tag_from(self):
        data = [
                ("test", "[test]:test"),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(utl.reflink_tag_from(v), expected)

    def test_strike_tag_from(self):
        data = [
                ("test", "~~test~~"),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(utl.strike_tag_from(v), expected)

    def test_ul_tag_from(self):
        data = [
                ("test", 1, "    - test"),
                ("test", 2, "        - test"),
                ]

        for v, lv, expected in data:
            with self.subTest(v=v, lv=lv, expected=expected):
                self.assertEqual(utl.ul_tag_from(v, lv), expected)

    def test_ul_tag_space_removed(self):
        data = [
                ("    - test", 1, "- test"),
                ("        - test", 2, "- test"),
                ("        - test", 1, "    - test"),
                ]

        for v, lv, expected in data:
            with self.subTest(v=v, lv=lv, expected=expected):
                self.assertEqual(utl.ul_tag_space_removed(v, lv), expected)

    def test_ul_tag_replaced(self):
        data = [
                ("- test", "*", "* test"),
                ("+ test", "-", "- test"),
                ]

        for v, mark, expected in data:
            with self.subTest(v=v, mark=mark, expected=expected):
                self.assertEqual(utl.ul_tag_replaced(v, mark), expected)
