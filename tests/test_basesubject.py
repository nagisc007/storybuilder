# -*- coding: utf-8 -*-
"""Test for basesubject.py
"""
import unittest
from builder.basesubject import _BaseSubject


class BaseSubjectTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n**** TEST: basesubject.py - BaseSubject ****")

    def test_attributes(self):
        data = [
                ("Taro", "a man", "he is a boy"),
                ("Hanako", "a woman", "she is a girl"),
                ]
        for name, info, note in data:
            with self.subTest(name=name, info=info, note=note):
                tmp = _BaseSubject(name, info, note)
                self.assertIsInstance(tmp, _BaseSubject)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.info, info)
                self.assertEqual(tmp.note, note)
                self.assertEqual(tmp.parent, None)

