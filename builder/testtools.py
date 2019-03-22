# -*- coding: utf-8 -*-
"""Useful tools for test with story builder
"""
import unittest

from .behavior import behavior_str_of
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
        what_act: Action, why_act: Action, how_act: Action, res_act: Action) -> bool:
    ERR_MSG = "is not exists!"
    # what
    if not _has_the_word_in_group(story, what_act):
        test_case.fail("{}'s purpose {}{}{} {}".format(what_act.subject.name, what_act.action, behavior_str_of(what_act.behavior), _passive_str_if(what_act), ERR_MSG))
    # why
    if not _has_the_word_in_group(story, why_act):
        test_case.fail("{}'s reason {}{}{} {}".format(why_act.subject.name, why_act.action, behavior_str_of(why_act.behavior), _passive_str_if(why_act), ERR_MSG))
    # how
    if not _has_the_word_in_group(story, how_act):
        test_case.fail("{}'s process {}{}{} {}".format(how_act.subject.name, how_act.action, behavior_str_of(how_act.behavior), _passive_str_if(how_act), ERR_MSG))
    # result
    if not _has_the_word_in_group(story, res_act):
        test_case.fail("{}'s result {}{}{} {}".format(res_act.subject.name, res_act.action, behavior_str_of(res_act.behavior), _passive_str_if(res_act), ERR_MSG))

    return True


def _has_the_word_in_group(group: ActionGroup, act: Action) -> bool:
    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_word_in_group(a, act):
                return True
        else:
            if _has_the_word(a, act):
                return True
    return False


def _has_the_word(act: Action, comp_act: Action) -> bool:
    return _has_the_name(act, comp_act.subject) \
            and act.behavior == comp_act.behavior and act.is_passive == comp_act.is_passive \
            and _eq_action_object(act, comp_act) \
            and comp_act.action in act.action


def _eq_action_object(act: Action, comp_act: Action) -> bool:
    if act.object:
        return comp_act.object and act.object.name == comp_act.object.name
    else:
        return True


def _passive_str_if(act: Action) -> str:
    return "（受）" if act.is_passive else ""
