# -*- coding: utf-8 -*-
"""Test suite for all tests
"""
import unittest

import test_base
import test_person
import test_testtools
import test_tools


def suite():
    '''Packing all tests.
    '''
    suite = unittest.TestSuite()

    # base
    suite.addTest(unittest.makeSuite(test_base.BaseActionTest))
    suite.addTest(unittest.makeSuite(test_base.BaseSubjectTest))
    suite.addTest(unittest.makeSuite(test_base.ActionTest))
    suite.addTest(unittest.makeSuite(test_base.ActionGroupTest))
    suite.addTest(unittest.makeSuite(test_base.BasePersonTest))
    suite.addTest(unittest.makeSuite(test_base.StageTest))
    suite.addTest(unittest.makeSuite(test_base.ItemTest))
    suite.addTest(unittest.makeSuite(test_base.DayTimeTest))
    suite.addTest(unittest.makeSuite(test_base.MasterTest))
    suite.addTest(unittest.makeSuite(test_base.WordTest))

    # person
    suite.addTest(unittest.makeSuite(test_person.PersonTest))

    # testtools
    suite.addTest(unittest.makeSuite(test_testtools.BasicMethodTest))

    # tools
    suite.addTest(unittest.makeSuite(test_tools.BasicMethodTest))

    return suite

