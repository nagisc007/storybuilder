# -*- coding: utf-8 -*-
"""Test suite for all tests
"""
import unittest

import test_action
import test_basesubject
import test_commons
import test_enums
import test_person
import test_storydb
import test_subject
import test_testtools
import test_tools


def suite():
    '''Packing all tests.
    '''
    suite = unittest.TestSuite()

    # action
    suite.addTest(unittest.makeSuite(test_action.BaseActionTest))
    suite.addTest(unittest.makeSuite(test_action.DescriptionTest))
    suite.addTest(unittest.makeSuite(test_action.ActionTest))
    suite.addTest(unittest.makeSuite(test_action.ActionGroupTest))
    suite.addTest(unittest.makeSuite(test_action.TagActionTest))

    # basesubject
    suite.addTest(unittest.makeSuite(test_basesubject.BaseSubjectTest))
    suite.addTest(unittest.makeSuite(test_basesubject.InfoTest))
    suite.addTest(unittest.makeSuite(test_basesubject.NothingTest))
    suite.addTest(unittest.makeSuite(test_basesubject.MethodUnitTest))

    # commons
    suite.addTest(unittest.makeSuite(test_commons.PublicMethodsTest))
    suite.addTest(unittest.makeSuite(test_commons.PrivateMethodsTest))

    # enums
    suite.addTest(unittest.makeSuite(test_enums.EnumsTest))

    # person
    suite.addTest(unittest.makeSuite(test_person.PersonTest))

    # storydb
    suite.addTest(unittest.makeSuite(test_storydb.StoryDBTEST))

    # subject
    suite.addTest(unittest.makeSuite(test_subject.BasePersonTest))
    suite.addTest(unittest.makeSuite(test_subject.DayTimeTest))
    suite.addTest(unittest.makeSuite(test_subject.ItemTest))
    suite.addTest(unittest.makeSuite(test_subject.MasterTest))
    suite.addTest(unittest.makeSuite(test_subject.SomethingTest))
    suite.addTest(unittest.makeSuite(test_subject.WordTest))

    # testtools
    suite.addTest(unittest.makeSuite(test_testtools.PublicMethodsTest))
    suite.addTest(unittest.makeSuite(test_testtools.PrivateMethodsTest))

    # tools
    suite.addTest(unittest.makeSuite(test_tools.PublicMethodsTest))
    suite.addTest(unittest.makeSuite(test_tools.PrivateMethodsTest))

    return suite

