# -*- coding: utf-8 -*-
"""Test for basesubject.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.basesubject import _BaseSubject, Info, Nothing
from builder.basesubject import _info_or_subject_from


_FILENAME = "basesubject.py"


class BaseSubjectTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "BaseSubject")

    def test_attributes(self):
        data = [
                ("Taro", "a man"),
                ("Hanako", ""),
                ]
        for name, note in data:
            with self.subTest(name=name, note=note):
                tmp = _BaseSubject(name, note) if note else _BaseSubject(name)
                self.assertIsInstance(tmp, _BaseSubject)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.note, note)
                self.assertEqual(tmp.parent, None)


class InfoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Info")

    def test_attributes(self):
        data = [
                "a info",
                ]

        for note in data:
            with self.subTest(note=note):
                tmp = Info(note)
                self.assertIsInstance(tmp, Info)
                self.assertEqual(tmp.name, Info.CLS_NAME)
                self.assertEqual(tmp.note, note)


class NothingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Nothing")

    def test_attributes(self):
        tmp = Nothing()
        self.assertIsInstance(tmp, Nothing)
        self.assertEqual(tmp.name, Nothing.CLS_NAME)
        self.assertEqual(tmp.note, "")
        self.assertEqual(tmp.parent, None)


class MethodUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "methods")

    def test_info_or_subject_from(self):
        data = [
                (_BaseSubject("a test"), _BaseSubject),
                ("a test", Info),
                (1, Info),
                (None, Nothing),
                ]

        for t, expected in data:
            with self.subTest(t=t, expected=expected):
                self.assertIsInstance(_info_or_subject_from(t), expected)
                
