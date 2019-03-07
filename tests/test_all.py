# -*- coding: utf-8 -*-
"""Test suite for all tests
"""
import unittest

from test_base import ClassCheckTest


def suite():
    '''Packing all tests.
    '''
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ClassCheckTest))
    return suite

