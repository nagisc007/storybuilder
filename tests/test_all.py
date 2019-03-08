# -*- coding: utf-8 -*-
"""Test suite for all tests
"""
import unittest

from test_base import ClassCheckTest
from test_tools import TestOutput
from test_example_story01 import Story01Test
from test_example_story01 import EpisodeTest_meeting
from test_example_story01 import EpisodeTest_confess

def suite():
    '''Packing all tests.
    '''
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ClassCheckTest))
    suite.addTest(unittest.makeSuite(TestOutput))
    suite.addTest(unittest.makeSuite(Story01Test))
    suite.addTest(unittest.makeSuite(EpisodeTest_meeting))
    suite.addTest(unittest.makeSuite(EpisodeTest_confess))
    return suite

