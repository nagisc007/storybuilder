# -*- coding: utf-8 -*-
"""Test suite for all tests
"""
import unittest

import test_base
import test_tools
import test_testtools


def suite():
    '''Packing all tests.
    '''
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(test_base.SubjectTest))
    suite.addTest(unittest.makeSuite(test_base.ActTest))
    suite.addTest(unittest.makeSuite(test_base.TitleTest))
    suite.addTest(unittest.makeSuite(test_base.PersonTest))
    suite.addTest(unittest.makeSuite(test_base.StageTest))
    suite.addTest(unittest.makeSuite(test_base.ItemTest))
    suite.addTest(unittest.makeSuite(test_base.DayTimeTest))

    suite.addTest(unittest.makeSuite(test_tools.TestTools))

    suite.addTest(unittest.makeSuite(test_testtools.TestCheckTools))

    return suite

