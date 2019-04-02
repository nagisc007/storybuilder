# -*- coding: utf-8 -*-
"""Test for enums.py
"""
import unittest
from builder.enums import ActType, AuxVerb, GroupType, LangType


_FILENAME = "enums.py"


class EnumsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        _print_title(_FILENAME, "Enums(ActType)")

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


# private functions
def _print_title(fname: str, title: str):
    print("\n**** TEST: {} - {} ****".format(fname, title))
