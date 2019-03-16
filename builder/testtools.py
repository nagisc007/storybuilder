# -*- coding: utf-8 -*-
"""Useful tools for test with story builder
"""
import unittest

from .acttypes import ActType, Behavior
from .base import Act, Stage, DayTime, Story, Episode, Scene
from .person import Person


def is_story_structed_episodes(test_case: unittest.TestCase, story: Story):
    '''Check the story.
    '''
    test_case.assertTrue(story.data, "A story's data not exists!")
    for a in story.data:
        test_case.assertIsInstance(a, Episode, "The story's episode is not a mismatch type!")

    return True


def is_episode_structed_scenes(test_case: unittest.TestCase, episode: Episode):
    '''Check the episode.
    '''
    test_case.assertTrue(episode.data, "A episode's data not exists!")
    for a in episode.data:
        test_case.assertIsInstance(a, Scene, "The episode's scene is not a mismatch type!")

    return True


def is_scene_structed_acts(test_case: unittest.TestCase, scene: Scene):
    '''Check the scene.
    '''
    test_case.assertTrue(scene.data, "A scene's data not exists!")
    for a in scene.data:
        test_case.assertIsInstance(a, Act, "The scene's act is not a mismatch type!")

    return True


def has_scene_basic_infos(test_case: unittest.TestCase, scene: Scene, hero: Person, rival: Person):
    '''Check the scene contained basic infos.
    '''
    test_case.assertIsInstance(scene, Scene, "It is not a Scene object!")
    ERR_MSG = "not exists in the scene!"
    # Who
    for a in scene.data:
        if is_contained_the_name(a, hero.name): break
    else:
        test_case.fail("{} (as hero) {}".format(hero.name, ERR_MSG))
    # Whom
    for a in scene.data:
        if is_contained_the_name(a, rival.name): break
    else:
        test_case.fail("{} (as rival) {}".format(rival.name, ERR_MSG))
    # When
    for a in scene.data:
        if isinstance(a.subject, Stage): break
    else:
        test_case.fail("The Stage {}".format(ERR_MSG))
    # Where
    for a in scene.data:
        if isinstance(a.subject, DayTime): break
    else:
        test_case.fail("The DayTime {}".format(ERR_MSG))

    return True 


def has_episode_outline_infos(test_case: unittest.TestCase, episode: Episode,
        purpose, reason, process, result):
    '''Check the episode contained outline infos.
    '''
    test_case.assertIsInstance(episode, Episode, "It is not a Episode object!")
    ERR_MSG = "not exists in the episode!"
    # What
    for s in episode.data:
        for a in s.data:
            if has_contained_the_purpose(a, purpose): break
    else:
        test_case.fail("The purpose ({}) {}".format(purpose, ERR_MSG))
    # Why
    for s in episode.data:
        for a in s.data:
            if has_contained_the_reason(a, reason): break
    else:
        test_case.fail("The reason ({}) {}".format(reason, ERR_MSG))
    # How
    for s in episode.data:
        for a in s.data:
            if has_contained_the_process(a, process): break
    else:
        test_case.fail("The process ({}) {}".format(process, ERR_MSG))
    # Result
    for s in episode.data:
        for a in s.data:
            if has_contained_the_result(a, result): break
    else:
        test_case.fail("The result ({}) {}".format(result, ERR_MSG))

    return True


def is_contained_the_name(act: Act, name: str):
    return name in act.subject.name


def has_contained_the_purpose(act: Act, purpose: str):
    return act.act_type in (ActType.TELL, ActType.THINK) \
            and purpose in act.title


def has_contained_the_reason(act: Act, reason: str):
    return act.act_type in (ActType.ACT, ActType.TELL, ActType.THINK) \
            and reason in act.title


def has_contained_the_process(act: Act, process: str):
    return act.act_type == ActType.ACT and process in act.title


def has_contained_the_result(act: Act, result: str):
    return act.act_type in (ActType.ACT, ActType.TELL, ActType.THINK) \
            and result in act.title

