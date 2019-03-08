# -*- coding: utf-8 -*-
"""Test for tools.py
"""

import unittest

from builder.base import ActType, Act, Must, Done, Title, Description
from builder.base import Person, Stage, Item, DayTime
from builder.tools import output
from builder.tools import output_md

class TestOutput(unittest.TestCase):

    def setUp(self):
        self.test_story = (
                Act("act1", ActType.ACT, "act action"),
                Act("act2", ActType.TEST, "test action"),
                Act("act3", ActType.SYMBOL, "symbol action")
                )

    def test_output(self):
        output(self.test_story, is_debug=True)

    def test_output_md(self):
        output_md(self.test_story, 'test_file', is_debug=True)
