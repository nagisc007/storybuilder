# -*- coding: utf-8 -*-
"""Test utility.
"""
import unittest
from . import action as act
from . import assertion as ast
from . import analyzer as ayz
from . import person as psn
from . import day as dy
from . import stage as stg
from . import parser as ps
from . import enums as em


# public methods
def exists_basic_infos(case: unittest.TestCase,
        story: list, hero: psn.Person, rival: psn.Person) -> bool:
    ERR_MSG = "is not exists!"
    is_successed = True

    if not ayz.has_the_subject_in(story, hero):
        case.fail(f"Hero {hero.name} {ERR_MSG}")
        is_successed = False
    if not ayz.has_the_subject_in(story, rival):
        case.fail(f"Rival {rival.name} {ERR_MSG}")
        is_successed = False
    if not ayz.has_a_subject_in(story, dy.Day):
        case.fail(f"Day {ERR_MSG}")
        is_successed = False
    if not ayz.has_a_subject_in(story, stg.Stage):
        case.fail(f"Stage {ERR_MSG}")
        is_successed = False

    return is_successed


def exists_basic_infos_by_data(case: unittest.TestCase,
        data: list): # pragma: no cover
    for title, story, hero, rival in ast.is_list(data):
        with case.subTest(title=title, story=story, hero=hero, rival=rival):
            case.assertTrue(exists_basic_infos(case, story, hero, rival))


def exists_looking_infos() -> bool:
    # TODO: implement
    return False


def exists_outline_infos(case: unittest.TestCase,
        story: list, what: act.Action, why: act.Action,
        how: act.Action, res: act.Action, is_fuzzy: bool=False) -> bool:
    # TODO: fuzzy match implement
    is_succeeded = True
    ERR_MSG = "is not exists!"
    baselang = em.LangType.JPN
    checker = ayz.contains_the_action_in if is_fuzzy else ayz.has_the_action_in
    formatmsg = lambda x: ps.actinfo_from_action(x, 0, baselang, False)
    if not checker(story, what):
        case.fail(f"Purpose: {formatmsg(what)}/{ERR_MSG}")
        is_succeeded = False
    if not checker(story, why):
        case.fail(f"Reason: {formatmsg(why)}/{ERR_MSG}")
        is_succeeded = False
    if not checker(story, how):
        case.fail(f"Process: {formatmsg(how)}/{ERR_MSG}")
        is_succeeded = False
    if not checker(story, res):
        case.fail(f"Result: {formatmsg(res)}/{ERR_MSG}")
        is_succeeded = False

    return is_succeeded


def exists_outline_infos_by_data(case: unittest.TestCase,
        data: list): # pragma: no cover
    for title, story, what, why, how, res, isfuzzy in data:
        with case.subTest(title=title, story=story, what=what, why=why,
                how=how, res=res, isfuzzy=isfuzzy):
            case.assertTrue(exists_outline_infos(case, story, what, why, how,
                res, isfuzzy))


def followed_all_flags() -> bool:
    # TODO: implement
    return False


def is_all_actions_in(story: list) -> bool:
    for v in ast.is_list(story):
        if not _is_all_actions_(v):
            return False
    return True


def print_test_title(fname: str, title: str) -> bool:
    assert isinstance(fname, str)
    assert isinstance(title, str)

    print("\n**** TEST: {} - {} ****".format(fname, title))

    return True


# private methods
def _is_all_actions_(val) -> bool:
    if isinstance(val, act.ActionGroup):
        return _is_all_actions_in_group(val)
    elif isinstance(val, act.TagAction):
        return True
    elif isinstance(val, act.Action):
        return True
    elif isinstance(val, list) or isinstance(val, tuple):
        return is_all_actions_in(val)
    else:
        return False


def _is_all_actions_in_group(group: act.ActionGroup) -> bool:
    for a in ast.is_instance(group, act.ActionGroup).actions:
        if not _is_all_actions_(a):
            return False
    return True

