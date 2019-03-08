# -*- coding: utf-8 -*-
"""Example story test.
"""
import unittest

from builder.base import ActType, Act, Must, Done, Title, Description, Person, Stage, Item, DayTime

from examples.story01 import Taro, Hanako, Teacher
from examples.story01 import ClassRoom
from examples.story01 import Sky
from examples.story01 import FirstDay, LastDay
from examples.story01 import story
from examples.story01 import meeting
from examples.story01 import confession

from builder.testtools import checked_if_all_actions
from builder.testtools import checked_has_basic_info


class Story01Test(unittest.TestCase):

    def setUp(self):
        self.acts = story()

    def test_story_is_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_story_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Taro(), Hanako()))


class EpisodeTest_meeting(unittest.TestCase):
    def setUp(self):
        self.acts =  meeting(ClassRoom(), FirstDay(), Taro(), Hanako(), Teacher(), Sky())

    def test_episode_is_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_episode_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Taro(), Hanako()))


class EpisodeTest_confess(unittest.TestCase):
    
    def setUp(self):
        self.acts = confession(ClassRoom(), LastDay(), Taro(), Hanako())

    def test_episode_is_all_actions(self):
        self.assertTrue(checked_if_all_actions(self.acts))

    def test_episode_has_basic_infos(self):
        self.assertTrue(checked_has_basic_info(self.acts, Taro(), Hanako()))
