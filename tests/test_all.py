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

    # base
    suite.addTest(unittest.makeSuite(test_base.BaseActionTest))
    suite.addTest(unittest.makeSuite(test_base.SubjectTest))
    suite.addTest(unittest.makeSuite(test_base.DescTest))
    suite.addTest(unittest.makeSuite(test_base.ActTest))
    suite.addTest(unittest.makeSuite(test_base.BasePersonTest))
    suite.addTest(unittest.makeSuite(test_base.StageTest))
    suite.addTest(unittest.makeSuite(test_base.ItemTest))
    suite.addTest(unittest.makeSuite(test_base.DayTimeTest))
    suite.addTest(unittest.makeSuite(test_base.SceneTest))
    suite.addTest(unittest.makeSuite(test_base.EpisodeTest))
    suite.addTest(unittest.makeSuite(test_base.StoryTest))

    # testtools
    suite.addTest(unittest.makeSuite(test_testtools.BasicMethodTest))

    # tools
    suite.addTest(unittest.makeSuite(test_tools.BasicMethodTest))

    return suite

