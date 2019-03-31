# -*- coding: utf-8 -*-
"""Useful tools for test with story builder
"""
import unittest

from .action import Action, ActionGroup
from .commons import behavior_with_np_of, object_names_of, subject_name_of
from .enums import LangType
from .person import Person
from .subject import DayTime, Stage, Something


def contains_the_word(story: ActionGroup, target: Action) -> bool:
    '''Check if the word in the story by an ation.
    '''
    return _contains_the_word_in_group(story, target)


def followed_all_flags(test_case: unittest.TestCase, story: ActionGroup) -> bool:
    '''Check if all flags and deflags.
    '''
    flags = set(_flags_gathered_in_group(story))
    deflags = set(_flags_gathered_in_group(story, False))
    result = flags & deflags
    if len(result) != len(flags):
        test_case.fail("Unsolved flags or deflags: {}".format((flags | deflags) - result))
        return False
    return True


def has_a_daytime(story: ActionGroup) -> bool:
    '''Check if a day time in the story.
    '''
    return _has_a_daytime_in_group(story)


def has_a_stage(story: ActionGroup) -> bool:
    '''Check if a stage in the story.
    '''
    return _has_a_stage_in_group(story)


def has_basic_infos(test_case: unittest.TestCase, story: ActionGroup,
        hero: Person, rival: Person) -> bool:
    '''Check basic info.

    Basic informations are Who, Whom, When, Where
    '''
    ERR_MSG = "is not exists!"
    is_succeeded = True
    # who
    if not _has_the_name_in_group(story, hero):
        test_case.fail("Hero {} {}".format(hero.name, ERR_MSG))
        is_succeeded = False
    # whom
    if not _has_the_name_in_group(story, rival):
        test_case.fail("Rival {} {}".format(rival.name, ERR_MSG))
        is_succeeded = False
    # when
    if not _has_a_daytime_in_group(story):
        test_case.fail("DayTime {}".format(ERR_MSG))
        is_succeeded = False
    # where
    if not _has_a_stage_in_group(story):
        test_case.fail("Stage {}".format(ERR_MSG))
        is_succeeded = False

    return is_succeeded


def has_outline_infos(test_case: unittest.TestCase, story: ActionGroup,
        what_act: Action, why_act: Action, how_act: Action, res_act: Action) -> bool:
    '''Check if the story has outline informations.
    '''
    ERR_MSG = "is not exists!"
    # what
    if not _contains_the_word_in_group(story, what_act):
        test_case.fail("{}'s purpose {}({}):{} {}".format(
            subject_name_of(what_act),
            behavior_with_np_of(what_act),
            object_names_of(what_act),
            what_act.info, ERR_MSG))
    # why
    if not _contains_the_word_in_group(story, why_act):
        test_case.fail("{}'s reason {}({}):{} {}".format(
            subject_name_of(why_act),
            behavior_with_np_of(why_act),
            object_names_of(why_act),
            why_act.info, ERR_MSG))
    # how
    if not _contains_the_word_in_group(story, how_act):
        test_case.fail("{}'s process {}({}):{} {}".format(
            subject_name_of(how_act),
            behavior_with_np_of(how_act),
            object_names_of(how_act),
            how_act.info, ERR_MSG))
    # result
    if not _contains_the_word_in_group(story, res_act):
        test_case.fail("{}'s result {}({}):{} {}".format(
            subject_name_of(res_act),
            behavior_with_np_of(res_act),
            object_names_of(res_act),
            res_act.info, ERR_MSG))

    return True


def has_the_name(story: ActionGroup, target: Person) -> bool:
    '''Check if the name in the story.
    '''
    return _has_the_name_in_group(story, target)


def has_the_action(story: ActionGroup, target: Action) -> bool:
    '''Check if the word in the story.
    '''
    return _has_the_action_in_group(story, target)


def is_all_actions(story: ActionGroup) -> bool:
    '''Check if the story is all of an action and an action group.
    '''
    return _is_actiongroup_all_actions(story)


# private functions
def _contains_something_in_objects(act: Action) -> bool:
    for o in act.objects:
        if isinstance(o, Something):
            return True
    return False


def _contains_the_word(act: Action, target: Action) -> bool:
    return isinstance(act, Action) and isinstance(target, Action) \
            and _is_near_eq_actions(act, target) \
            and target.info in act.info


def _contains_the_word_in_group(group: ActionGroup, target: Action) -> bool:
    if isinstance(group, ActionGroup):
        for a in group.actions:
            if isinstance(a, ActionGroup):
                if _contains_the_word_in_group(a, target):
                    return True
            else:
                if _contains_the_word(a, target):
                    return True
    else:
        return _contains_the_word(group, target)


def _flags_gathered_in_group(group: ActionGroup, is_flag: bool=True) -> list:
    if isinstance(group, ActionGroup):
        tmp = []
        for a in group.actions:
            if isinstance(a, ActionGroup):
                tmp.extend(_flags_gathered_in_group(a, is_flag))
            else:
                tmp.append(_flag_gatherd(a, is_flag))
        return tmp
    else:
        return [_flag_gatherd(group, is_flag)]


def _flag_gatherd(act: Action, is_flag: bool) ->str:
    if not isinstance(act, Action):
        return ""
    if is_flag:
        return act.flag or ""
    else:
        return act.deflag or ""


def _has_a_daytime(act: Action) -> bool:
    return isinstance(act, Action) and isinstance(act.subject, DayTime)


def _has_a_daytime_in_group(group: ActionGroup) -> bool:
    if isinstance(group, ActionGroup):
        for a in group.actions:
            if isinstance(a, ActionGroup):
                if _has_a_daytime_in_group(a):
                    return True
            else:
                if _has_a_daytime(a):
                    return True
        else:
            return False
    else:
        return _has_a_daytime(group)


def _has_a_stage(act: Action) -> bool:
    return isinstance(act, Action) and isinstance(act.subject, Stage)


def _has_a_stage_in_group(group: ActionGroup) -> bool:
    if isinstance(group, ActionGroup):
        for a in group.actions:
            if isinstance(a, ActionGroup):
                if _has_a_stage_in_group(a):
                    return True
            else:
                if _has_a_stage(a):
                    return True
        else:
            return False
    return _has_a_stage(group)


def _has_the_action(act: Action, target: Action) -> bool:
    return isinstance(act, Action) and isinstance(target, Action) \
            and act.act_type == target.act_type \
            and act.behavior == target.behavior \
            and act.info == target.info \
            and act.is_negative == target.is_negative \
            and act.is_passive == target.is_passive \
            and subject_name_of(act) == subject_name_of(target)


def _has_the_action_in_group(group: ActionGroup, target: Action) -> bool:
    if isinstance(group, ActionGroup):
        for a in group.actions:
            if isinstance(a, ActionGroup):
                if _has_the_action_in_group(a, target):
                    return True
            else:
                if _has_the_action(a, target):
                    return True
        else:
            return False
    else:
        return _has_the_action(group, target)


def _has_the_name(act: Action, target: Person) -> bool:
    return isinstance(act, Action) and isinstance(target, Person) \
            and subject_name_of(act) == target.name


def _has_the_name_in_group(group: ActionGroup, target: Person) -> bool:
    if isinstance(group, ActionGroup):
        for a in group.actions:
            if isinstance(a, ActionGroup):
                if _has_the_name_in_group(a, target):
                    return True
            else:
                if _has_the_name(a, target):
                    return True
        else:
            return False
    return _has_the_name(group, target)


def _is_actiongroup_all_actions(group: ActionGroup) -> bool:
    if isinstance(group, ActionGroup):
        for a in group.actions:
            if isinstance(a, ActionGroup):
                if not _is_actiongroup_all_actions(a):
                    return False
            else:
                if not isinstance(a, Action):
                    return False
        return True
    else:
        return isinstance(a, Action)


def _is_near_eq_actions(a: Action, b: Action) -> bool:
    return a.act_type == b.act_type \
            and a.behavior == b.behavior \
            and a.is_negative == b.is_negative \
            and a.is_passive == b.is_passive \
            and _is_near_eq_at_subjects(a, b) \
            and _is_near_eq_at_objects(a, b)


def _is_near_eq_at_subjects(a: Action, b: Action) -> bool:
    return isinstance(a.subject, Something) or isinstance(b.subject, Something) \
            or subject_name_of(a) == subject_name_of(b)


def _is_near_eq_at_objects(a: Action, b: Action) -> bool:
    if _contains_something_in_objects(a) or _contains_something_in_objects(b):
        a_somethings = _count_something_in_objects(a)
        b_somethings = _count_something_in_objects(b)
        if a_somethings > b_somethings:
            tmp = set(b.objects) - set(a.objects)
            return len(tmp) == a_somethings
        else:
            tmp = set(a.objects) - set(b.objects)
            return len(tmp) == b_somethings
    else:
        return object_names_of(a) == object_names_of(b)


def _count_something_in_objects(act: Action) -> int:
    tmp = 0
    for o in act.objects:
        if isinstance(o, Something):
            tmp += 1
    return tmp

