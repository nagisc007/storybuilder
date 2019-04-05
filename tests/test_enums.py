# -*- coding: utf-8 -*-
"""Test for enums.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.enums import ActType, AuxVerb, GroupType, LangType


_FILENAME = "enums.py"


class EnumsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Enums(ActType)")

    def test_act_type(self):
        data = [
                "ACT",
                "EXPLAIN",
                "TAG",
                "TELL",
                "TEST",
                ]
        idx = 0
        for act in ActType:
            self.assertEqual(str(act), data[idx])
            idx += 1
