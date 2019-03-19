# -*- coding: utf-8 -*-
"""Useful tools for test with story builder
"""
import unittest

from .acttypes import Behavior
from .acttypes import behavior_str_of
from .base import Action, ActionGroup, Stage, DayTime
from .person import Person


def is_all_actions(test_case: unittest.TestCase, acts: ActionGroup) -> bool:
    '''Check all action and action group.
    '''
    test_case.assertIsInstance(acts, ActionGroup)
    return _is_actiongroup_all_actions(test_case, acts)


def _is_actiongroup_all_actions(test_case: unittest.TestCase, group: ActionGroup) -> bool:
    for a in group.actions:
        if isinstance(a, ActionGroup):
            if not _is_actiongroup_all_actions(test_case, a):
                return False
        else:
            if not isinstance(a, Action):
                return False
    return True


def has_basic_infos(test_case: unittest.TestCase, story: ActionGroup,
        hero: Person, rival: Person) -> bool:
    '''Check basic info.

    Basic informations are Who, Whom, When, Where
    '''
    ERR_MSG = "is not exists!"
    # who
    if not _has_the_name_in_group(story, hero):
        test_case.fail("Hero {} {}".format(hero.name, ERR_MSG))
    # whom
    if not _has_the_name_in_group(story, rival):
        test_case.fail("Rival {} {}".format(rival.name, ERR_MSG))
    # when
    if not _has_a_daytime_in_group(story):
        test_case.fail("DayTime {}".format(ERR_MSG))
    # where
    if not _has_a_stage_in_group(story):
        test_case.fail("Stage {}".format(ERR_MSG))

    return True


def _has_the_name_in_group(group: ActionGroup, target: Person) -> bool:
    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_name_in_group(a, target):
                return True
        else:
            if _has_the_name(a, target):
                return True
    return False


def _has_the_name(act: Action, target: Person) -> bool:
    return act.subject.name == target.name


def _has_a_stage_in_group(group: ActionGroup) -> bool:
    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_a_stage_in_group(a):
                return True
        else:
            if _has_a_stage(a):
                return True
    return False


def _has_a_stage(act: Action) -> bool:
    return isinstance(act.subject, Stage)


def _has_a_daytime_in_group(group: ActionGroup) -> bool:
    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_a_daytime_in_group(a):
                return True
        else:
            if _has_a_daytime(a):
                return True
    return False


def _has_a_daytime(act: Action) -> bool:
    return isinstance(act.subject, DayTime)


def has_outline_infos(test_case: unittest.TestCase, story: ActionGroup,
        what_sub: Person, what_behav: Behavior, purpose: str,
        why_sub: Person, why_behav: Behavior, reason: str,
        how_sub: Person, how_behav: Behavior, process: str,
        res_sub: Person, res_behav: Behavior, result: str) -> bool:
    ERR_MSG = "is not exists!"
    # what
    if not _has_the_word_in_group(story, what_sub, what_behav, purpose):
        test_case.fail("{}'s purpose {}{} {}".format(what_sub.name, purpose, behavior_str_of(what_behav), ERR_MSG))
    # why
    if not _has_the_word_in_group(story, why_sub, why_behav, reason):
        test_case.fail("{}'s reason {}{} {}".format(why_sub.name, reason, behavior_str_of(why_behav), ERR_MSG))
    # how
    if not _has_the_word_in_group(story, how_sub, how_behav, process):
        test_case.fail("{}'s process {}{} {}".format(how_sub.name, process, behavior_str_of(how_behav), ERR_MSG))
    # result
    if not _has_the_word_in_group(story, res_sub, res_behav, result):
        test_case.fail("{}'s result {}{} {}".format(res_sub.name, result, behavior_str_of(res_behav), ERR_MSG))

    return True


def _has_the_word_in_group(group: ActionGroup, target: Person, behavior: Behavior,
        word: str) -> bool:
    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_word_in_group(a, target, behavior, word):
                return True
        else:
            if _has_the_word(a, target, behavior, word):
                return True
    return False


def _has_the_word(act: Action, target: Person, behavior: Behavior,
        word: str) -> bool:
    return _has_the_name(act, target) and act.behavior == behavior and word in act.action
