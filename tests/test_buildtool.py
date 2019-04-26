# -*- coding: utf-8 -*-
"""Test: buildtool.py
"""
import unittest
import os
import sys
from io import StringIO
from builder.testutils import print_test_title
from builder import action as act
from builder import enums as em
from builder import person as psn
from builder import day as dy
from builder import stage as stg
from builder import item as itm
from builder import buildtool as btl


_FILENAME = "buildtool.py"


class PrivateMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "private methods")

    def setUp(self):
        self.taro = psn.Person("Taro", 17, "male", "student")
        self.hanako = psn.Person("Hanako", 17, "female", "student")
        self.box = itm.Item("Box", "a box")
        self.bus = stg.Stage("Bus", "a bus")
        self.day = dy.Day("Test day")

    def test_action_from(self):
        data = [
                ((self.taro.be(),),
                    em.LangType.ENG, False,
                    ["- Taro    :be          /"]),
                ((self.taro.be(), self.hanako.have(self.box)),
                    em.LangType.ENG, False,
                    ["- Taro    :be          /", "- Hanako  :have        /Box",]),
                ((self.taro.talk(self.hanako, "好き"),),
                    em.LangType.JPN, False,
                    ["- Taro　　　　:talk        /Hanako/好き"])
                ]

        for v, lang, dbg, expected in data:
            with self.subTest(v=v, lang=lang, dbg=dbg, expected=expected):
                self.assertEqual(btl._actinfo_from(v, lang, dbg), expected)

    def test_acttypes_percents_from(self):
        def baselist(be=0, behav=0, deal=0, do=0, explain=0, feel=0, look=0, move=0,
                talk=0, think=0):
            return [
                    f"- be: {be:.2f}%", f"- behav: {behav:.2f}%", f"- deal: {deal:.2f}%",
                    f"- do: {do:.2f}%", f"- explain: {explain:.2f}%",
                    f"- feel: {feel:.2f}%",
                    f"- look: {look:.2f}%", f"- move: {move:.2f}%",
                    f"- talk: {talk:.2f}%", f"- think: {think:.2f}%",
                    ]
        data = [
                ((self.taro.be(),),
                    ["## Actions",
                        "- Total: 1"] + baselist(be=100)),
                ((self.taro.be(), self.taro.talk(), self.taro.talk(), self.taro.do()),
                    ["## Actions",
                        "- Total: 4"] + baselist(be=25, talk=50, do=25)),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(btl._acttypes_percents_from(v), expected)

    def test_charcount_from(self):
        data = [
                ((self.taro.be().d("test"),),
                    em.LangType.ENG,
                    ["## Characters", "- Total: 5", "- Estimated: 10"]),
                ]

        for v, lang, expected in data:
            with self.subTest(v=v, lang=lang, expected=expected):
                self.assertEqual(btl._charcount_from(v, lang), expected)

    def test_descs_count_from(self):
        taro = self.taro
        data = [
                ((taro.be().d("test"),),
                    em.LangType.ENG, 5),
                ((taro.be().d("test", "apple"),),
                    em.LangType.ENG, 11),
                ((taro.be().t("test", "apple"),),
                    em.LangType.JPN, 12),
                ((taro.be().d("test"), taro.be().d("apple")),
                    em.LangType.ENG, 11),
                ]

        for v, lang, expected in data:
            with self.subTest(v=v, lang=lang, expected=expected):
                self.assertEqual(btl._descs_count_from(v, lang), expected)

    def test_descs_from(self):
        taro = self.taro
        data = [
                ((taro.be().d("test"),),
                    em.LangType.ENG, False,
                    [" test."]),
                ((taro.be().d("test", "apple"),),
                    em.LangType.ENG, False,
                    [" test, apple."]),
                ((taro.be().d("test", "apple"),),
                    em.LangType.JPN, False,
                    ["　test、apple。"]),
                ((taro.be().t("test", "apple"),),
                    em.LangType.ENG, False,
                    ['"test, apple"']),
                ((taro.be().t("test", "apple"),),
                    em.LangType.JPN, False,
                    ["「test、apple」"]),
                ]

        for v, lang, dbg, expected in data:
            with self.subTest(v=v, lang=lang, dbg=dbg, expected=expected):
                self.assertEqual(btl._descs_from(v, lang, dbg), expected)

    def test_estimated_description_count_from(self):
        data = [
                ((self.taro.be(), self.taro.talk()),
                    em.LangType.JPN, 50),
                ]

        for v, lang, expected in data:
            with self.subTest(v=v, lang=lang, expected=expected):
                self.assertEqual(btl._estimated_description_count_from(v, lang), expected)

    def test_output_to_console(self):
        data = [
                (["test"], False,
                    "test\n"),
                (["test", "apple"], False,
                    "test\napple\n"),
                ]

        for v, dbg, expected in data:
            with self.subTest(v=v, dbg=dbg, expected=expected):
                tmp_stdout, sys.stdout = sys.stdout, StringIO()
                self.assertTrue(btl._output_to_console(v, dbg))
                self.assertEqual(sys.stdout.getvalue(), expected)
                sys.stdout = tmp_stdout # fallback

    def test_output_to_file(self):
        data = [
                (["test"], "testfile", "", False,
                    "build/", True),
                ]

        for v, fname, suf, dbg, bdir, expected in data:
            with self.subTest(v=v, fname=fname, suf=suf, dbg=dbg, bdir=bdir,
                    expected=expected):
                buildpath = os.path.join(os.getcwd(), bdir + fname + suf + ".md")
                self.assertTrue(btl._output_to_file(v, fname, suf, dbg))
                self.assertTrue(os.path.exists(buildpath))
