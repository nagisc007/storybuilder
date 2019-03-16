# -*- coding: utf-8 -*-
"""Test for testtools.py
"""
import unittest

from builder.acttypes import ActType, Behavior
from builder.base import Act, Stage, DayTime
from builder.base import Story, Episode, Scene
from builder.person import Person
import builder.testtools as testtools

class BasicMethodTest(unittest.TestCase):

    def setUp(self):
        self.story = Story("test story")
        self.story.commit(
                Episode("episodeA"),
                Episode("episodeB"),
                Episode("episodeC")
                )
        self.episode = Episode("test episoe")
        self.episode.commit(
                Scene("sceneA"),
                Scene("sceneB"),
                Scene("sceneC")
                )
        self.taro = Person("Taro", 17, "male", "student")
        self.scene = Scene("test scene")
        self.scene.commit(
                Act(self.taro, ActType.ACT, Behavior.DO, "actA"),
                Act(self.taro, ActType.TELL, Behavior.TALK, "call me"),
                Act(self.taro, ActType.THINK, Behavior.FEEL, "I am free")
                )

    def test_is_story_structed_episodes(self):
        self.assertTrue(testtools.is_story_structed_episodes(self, self.story))

    def test_is_episode_structed_scenes(self):
        self.assertTrue(testtools.is_episode_structed_scenes(self, self.episode))

    def test_is_scene_structed_acts(self):
        self.assertTrue(testtools.is_scene_structed_acts(self, self.scene))

    def test_is_contained_the_name(self):
        taro_talk = self.taro.tell("Wow")
        self.assertFalse(testtools.is_contained_the_name(taro_talk, "Hanako"))
        self.assertTrue(testtools.is_contained_the_name(taro_talk, "Taro"))

    def test_has_contained_the_purpose(self):
        acted = self.taro.move("to home")
        told = self.taro.tell("I am home")
        thought = self.taro.think("that home")
        looked = self.taro.look("at home")
        self.assertFalse(testtools.has_contained_the_purpose(acted, "home"))
        self.assertTrue(testtools.has_contained_the_purpose(told, "home"))
        self.assertTrue(testtools.has_contained_the_purpose(thought, "home"))
        self.assertFalse(testtools.has_contained_the_purpose(looked, "home"))

    def test_has_contained_the_reason(self):
        acted = self.taro.move("to home")
        told = self.taro.tell("I am home")
        thought = self.taro.think("that home")
        looked = self.taro.look("at home")
        self.assertTrue(testtools.has_contained_the_reason(acted, "home"))
        self.assertTrue(testtools.has_contained_the_reason(told, "home"))
        self.assertTrue(testtools.has_contained_the_reason(thought, "home"))
        self.assertFalse(testtools.has_contained_the_reason(looked, "home"))

    def test_has_contained_the_process(self):
        acted = self.taro.move("to home")
        told = self.taro.tell("I am home")
        thought = self.taro.think("that home")
        looked = self.taro.look("at home")
        self.assertTrue(testtools.has_contained_the_process(acted, "home"))
        self.assertFalse(testtools.has_contained_the_process(told, "home"))
        self.assertFalse(testtools.has_contained_the_process(thought, "home"))
        self.assertFalse(testtools.has_contained_the_process(looked, "home"))

    def test_has_contained_the_result(self):
        acted = self.taro.move("to home")
        told = self.taro.tell("I am home")
        thought = self.taro.think("that home")
        looked = self.taro.look("at home")
        self.assertTrue(testtools.has_contained_the_result(acted, "home"))
        self.assertTrue(testtools.has_contained_the_result(told, "home"))
        self.assertTrue(testtools.has_contained_the_result(thought, "home"))
        self.assertFalse(testtools.has_contained_the_result(looked, "home"))

