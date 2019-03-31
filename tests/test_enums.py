# -*- coding: utf-8 -*-
"""Test for enums.py
"""
import unittest
from builder.enums import ActType, AuxVerb, GroupType, LangType


class EnumsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: enums.py - Enum ****")

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

