# -*- coding: utf-8 -*-
"""Test for tools.py
"""

import unittest
import sys
from io import StringIO

from builder.acttypes import ActType, Behavior
from builder.base import Act, Stage, DayTime
from builder.base import Story, Episode, Scene
from builder.person import Person
import builder.tools as tools

class BasicMethodTest(unittest.TestCase):

    def setUp(self):
        self.story = Story("test story")
        self.story.commit(
                Episode("episodeA"),
                Episode("episodeB"),
                Episode("episodeC")
                )
        self.episode = Episode("test episode")
        self.episode.commit(
                Scene("sceneA"),
                Scene("sceneB"),
                Scene("sceneC")
                )
        self.scene = Scene("test scene")
        self.taro = Person("Taro", 17, "male", "student")
        self.scene.commit(
                self.taro.come("in room"),
                self.taro.tell("wow"),
                self.taro.see("Hanako"),
                )
        self.acted = self.taro.go("to school")
        self.told = self.taro.tell("wow")
        self.thought = self.taro.think("so good")
        self.looked = self.taro.look("a man")
        #
        self.test_story = Story("test story")
        self.test_episodeA = Episode("episodeA")
        self.test_episodeB = Episode("episodeB")
        self.test_sceneA1 = Scene("sceneA1")
        self.test_sceneA2 = Scene("sceneA2")
        self.test_sceneB1 = Scene("sceneB1")
        self.test_sceneB2 = Scene("sceneB2")
        self.test_sceneA1.commit(
                self.taro.come("in room").desc("部屋に入る"),
                self.taro.tell("the room").desc("部屋だな"),
                )
        self.test_sceneA2.commit(
                self.taro.go("out from").desc("外に出る"),
                self.taro.think("about Hanako").desc("花子がいるかな"),
                )
        self.test_sceneB1.commit(
                self.taro.smile("www").desc("微笑だった"),
                self.taro.gaze("Hanako").desc("花子を見つめていた")
                )
        self.test_sceneB2.commit(
                self.taro.talk("to Hanako").desc("花子に話しかけた"),
                self.taro.ask("love me").desc("俺のことどう思うかと"),
                )
        self.test_episodeA.commit(
                self.test_sceneA1,
                self.test_sceneA2
                )
        self.test_episodeB.commit(
                self.test_sceneB1,
                self.test_sceneB2
                )
        self.test_story.commit(
                self.test_episodeA,
                self.test_episodeB
                )

    def test_story_builded(self):
        pass

    def test_options_parsed(self):
        pass

    def test_story_strings_as_actions(self):
        pass

    def test_story_strings_as_descriptions(self):
        pass

    def test_story_strings_as_infos(self):
        pass

    def test_output(self):
        tmp_stdout, sys.stdout = sys.stdout, StringIO()
        # testing
        self.assertTrue(tools.output(self.test_story, False, False))
        self.assertEqual(
                sys.stdout.getvalue(),
                "test story\n===\n\n## episodeA\n\n\n### sceneA1\n\nTaro - 来る: in room\nTaro - 言う: 「the room」\n\n### sceneA2\n\nTaro - 行く: out from\nTaro - 思う: about Hanako\n\n## episodeB\n\n\n### sceneB1\n\nTaro - 微笑する: www\nTaro - 見つめる: Hanako\n\n### sceneB2\n\nTaro - 話す: to Hanako\nTaro - 尋ねる: love me\n"
                )
        # fall back
        sys.stdout = tmp_stdout

    def test_output_as_desc(self):
        tmp_stdout, sys.stdout = sys.stdout, StringIO()
        # testing
        self.assertTrue(tools.output(self.test_story, True, False))
        self.assertEqual(
                sys.stdout.getvalue(),
                "test story\n===\n\n## episodeA\n\n\n### sceneA1\n\n部屋に入る。\n「部屋だな」\n\n### sceneA2\n\n外に出る。\n花子がいるかな。\n\n## episodeB\n\n\n### sceneB1\n\n微笑だった。\n花子を見つめていた。\n\n### sceneB2\n\n花子に話しかけた。\n俺のことどう思うかと。\n"
                )
        # fall back
        sys.stdout = tmp_stdout

    def test_output_md(self):
        '''
        Todo: in preparation
        '''
        pass

    def test__action_string_builded_with_type(self):
        self.assertEqual(tools._action_string_builded_with_type(
            Act(self.taro, ActType.SYMBOL, Behavior.DISPLAY, "Symbol", "display"), False),
            "**Taro - display: Symbol**\n")
        self.assertEqual(tools._action_string_builded_with_type(self.acted, False),
                "Taro - 行く: to school\n")
        self.assertEqual(tools._action_string_builded_with_type(self.told, False),
                "Taro - 言う: 「wow」\n")
        self.assertEqual(tools._action_string_builded_with_type(self.thought, False),
                "Taro - 思う: so good\n")
        self.assertEqual(tools._action_string_builded_with_type(self.looked, False),
                "Taro - 描写: a man\n")

    def test__action_string_builded(self):
        self.assertEqual(tools._action_string_builded(self.acted), "Taro - 行く: to school")
        self.assertEqual(tools._action_string_builded(self.told), "Taro - 言う: 「wow」")
        self.assertEqual(tools._action_string_builded(self.thought), "Taro - 思う: so good")
        self.assertEqual(tools._action_string_builded(self.looked), "Taro - 描写: a man")

    def test__description_builded_with_type(self):
        self.assertEqual(tools._description_builded_with_type(
            Act(self.taro, ActType.SYMBOL, Behavior.DISPLAY, "Symbol", "display").desc("String field"), False),
            "**String field**\n")
        self.acted.desc("test moved")
        self.told.desc("wow wow")
        self.thought.desc("so good")
        self.looked.desc("a good look man")

        self.assertEqual(tools._description_builded_with_type(self.acted, False),
                "test moved。\n")
        self.assertEqual(tools._description_builded_with_type(self.told, False),
                "「wow wow」\n")
        self.assertEqual(tools._description_builded_with_type(self.thought, False),
                "so good。\n")
        self.assertEqual(tools._description_builded_with_type(self.looked, False),
                "a good look man。\n")

    def test__description_builded_with_type_many_descs(self):
        self.assertEqual(tools._description_builded_with_type(
            Act(self.taro, ActType.SYMBOL, Behavior.DISPLAY, "Symbol", "display")
            .desc("String field", "it's green"), False),
            "**String field - it's green**\n")
        self.acted.desc("the test man", "he moved to home")
        self.assertEqual(tools._description_builded_with_type(self.acted, False),
                "the test man、he moved to home。\n")

    def test__description_builded(self):
        self.acted.desc("test moved")
        self.told.desc("wow wow")
        self.thought.desc("so good man")
        self.looked.desc("a shiny man")

        self.assertEqual(tools._description_builded(self.acted),
                "test moved。")
        self.assertEqual(tools._description_builded(self.told),
                "「wow wow」")
        self.assertEqual(tools._description_builded(self.thought),
                "so good man。")
        self.assertEqual(tools._description_builded(self.looked),
                "a shiny man。")

    def test__description_builded_many_descs(self):
        self.acted.desc("the test man", "he moved to home")
        self.assertEqual(tools._description_builded(self.acted),
                "the test man、he moved to home。")

    def test__story_title_of(self):
        self.assertEqual(tools._story_title_of(self.story), "test story\n===\n")

    def test__episode_title_of(self):
        self.assertEqual(tools._episode_title_of(self.episode), "\n## test episode\n\n")

    def test__scene_title_of(self):
        self.assertEqual(tools._scene_title_of(self.scene), "\n### test scene\n\n")

