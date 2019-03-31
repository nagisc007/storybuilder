# -*- coding: utf-8 -*-
"""Test suite for all tests
"""
import unittest

import test_action
import test_basesubject
import test_commons
import test_enums
import test_person
import test_subject
import test_testtools
import test_tools


def suite():
    '''Packing all tests.
    '''
    suite = unittest.TestSuite()

    # action
    suite.addTest(unittest.makeSuite(test_action.BaseActionTest))
    suite.addTest(unittest.makeSuite(test_action.ActionTest))
    suite.addTest(unittest.makeSuite(test_action.ActionGroupTest))

    # basesubject
    suite.addTest(unittest.makeSuite(test_basesubject.BaseSubjectTest))

    # commons
    suite.addTest(unittest.makeSuite(test_commons.MethodUnitTest))

    # enums
    suite.addTest(unittest.makeSuite(test_enums.EnumsTest))

    # person
    suite.addTest(unittest.makeSuite(test_person.PersonTest))

    # subject
    suite.addTest(unittest.makeSuite(test_subject.BasePersonTest))
    suite.addTest(unittest.makeSuite(test_subject.DayTimeTest))
    suite.addTest(unittest.makeSuite(test_subject.ItemTest))
    suite.addTest(unittest.makeSuite(test_subject.MasterTest))
    suite.addTest(unittest.makeSuite(test_subject.SomethingTest))
    suite.addTest(unittest.makeSuite(test_subject.WordTest))

    # testtools
    suite.addTest(unittest.makeSuite(test_testtools.MethodUnitTest))

    # tools
    suite.addTest(unittest.makeSuite(test_tools.BasicClassTest))
    suite.addTest(unittest.makeSuite(test_tools.BasicMethodTest))

    return suite

