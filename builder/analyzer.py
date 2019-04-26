# -*- coding: utf-8 -*-
"""Utility for analyze.
"""
from . import action as act
from . import assertion as ast
from . import basesubject as bs
from . import enums as em
from . import info as inf


# public methods
def contains_the_action_in(story: list, target: act.Action) -> bool:
    for v in ast.is_list(story):
        if _contains_the_action_(v, target):
            return True
    return False


def count_acts(story: list) -> int:
    tmp = 0
    for v in ast.is_list(story):
        tmp += _count_acts_from_(v)
    return tmp


def count_acttypes(story: list) -> dict:
    return {
            em.ActType.BE: _count_acttype_from(story, em.ActType.BE),
            em.ActType.BEHAV: _count_acttype_from(story, em.ActType.BEHAV),
            em.ActType.DEAL: _count_acttype_from(story, em.ActType.DEAL),
            em.ActType.DO: _count_acttype_from(story, em.ActType.DO),
            em.ActType.EXPLAIN: _count_acttype_from(story, em.ActType.EXPLAIN),
            em.ActType.FEEL: _count_acttype_from(story, em.ActType.FEEL),
            em.ActType.LOOK: _count_acttype_from(story, em.ActType.LOOK),
            em.ActType.MOVE: _count_acttype_from(story, em.ActType.MOVE),
            em.ActType.TALK: _count_acttype_from(story, em.ActType.TALK),
            em.ActType.TEST: _count_acttype_from(story, em.ActType.TEST),
            em.ActType.THINK: _count_acttype_from(story, em.ActType.THINK),
            }


def count_descripton_at_action(ac: act.Action, strict: bool=False) -> int:
    delta = len(ac.description.data) if strict else 0
    return sum([len(v) for v in ac.description.data]) + delta


def count_subjects_in(story: list, subcls: bs.BaseSubject)-> int:
    tmp = 0
    for v in ast.is_list(story):
        tmp += _count_subjects_(v, subcls)
    return tmp


def has_a_subject_in(story: list, subcls: bs.BaseSubject) -> bool:
    for v in ast.is_list(story):
        if _has_a_subject_(v, subcls):
            return True
    else:
        return False


def has_the_action_in(story: list, target: act.Action) -> bool:
    for v in ast.is_list(story):
        if _has_the_action_(v, target):
            return True
    else:
        return False


def has_the_keyword(story: list) -> bool:
    # TODO: implement
    return False


def has_the_subject_in(story: list, target: bs.BaseSubject) -> bool:
    for v in ast.is_list(story):
        if _has_the_subject(v, target):
            return True
    else:
        return False


# private methods
def _compare_objects_with_something(origin: act.Action, target: act.Action) -> bool:
    mismatches = 0
    for t in target.objects:
        for o in origin.objects:
            if _contains_object(o, t):
                break
        else:
            mismatches += 1
    origin_somethings = _count_subjects_(origin.objects, inf.Something)
    target_somethings = _count_subjects_(target.objects, inf.Something)
    return mismatches - abs(target_somethings - origin_somethings) <= 0


def _contains_object(origin: bs.BaseSubject, target: bs.BaseSubject) -> bool:
    if isinstance(target, inf.Info):
        return isinstance(origin, inf.Info) and target.note in origin.note
    else:
        return origin == target


def _contains_the_action_(val, target: act.Action) -> bool:
    if isinstance(val, act.ActionGroup):
        return _contains_the_action_in_group(val, target)
    elif isinstance(val, act.TagAction):
        return False
    elif isinstance(val, act.Action):
        return val.act_type is ast.is_instance(target, act.Action).act_type \
                and val.subject == target.subject \
                and val.auxverb is target.auxverb \
                and _compare_objects_with_something(val, target)
    elif isinstance(val, list) or isinstance(val, tuple):
        return contains_the_action_in(val, target)
    else:
        return False


def _contains_the_action_in_group(group: act.ActionGroup, target: act.Action) -> bool:
    for a in ast.is_instance(group, act.ActionGroup).actions:
        if _contains_the_action_(a, target):
            return True
    return False


def _count_acts_from_(val) -> int:
    if isinstance(val, act.ActionGroup):
        return _count_acts_from_in_group(val)
    elif isinstance(val, act.TagAction):
        return 0
    elif isinstance(val, act.Action):
        return 1
    elif isinstance(val, list) or isinstance(val, tuple):
        return count_acts(val)
    return 0


def _count_acts_from_in_group(group: act.ActionGroup) -> int:
    tmp = 0
    for a in ast.is_instance(group, act.ActionGroup).actions:
        tmp += _count_acts_from_(a)
    return tmp


def _count_acttype_(val, actype: em.ActType) -> int:
    if isinstance(val, act.ActionGroup):
        return _count_acttype_from_in_group(val, acttype)
    elif isinstance(val, act.TagAction):
        return 0
    elif isinstance(val ,act.Action):
        return 1 if val.act_type is actype else 0
    elif isinstance(val, list) or isinstance(val, tuple):
        return count_acttypes(val, acttype)
    else:
        return 0


def _count_acttype_from(story: list, acttype: em.ActType) -> int:
    tmp = 0
    for v in ast.is_list(story):
        tmp += _count_acttype_(v, acttype)
    return tmp


def _count_acttype_from_in_group(group: act.ActionGroup, acttype: em.ActType) -> int:
    tmp = 0
    for a in ast.is_instance(group, act.ActionGroup).actions:
        tmp += _count_acttype_(a, acttype)
    return tmp


def _count_subjects_(val, subcls: bs.BaseSubject) -> int:
    if isinstance(val, act.ActionGroup):
        return _count_subjects_in_group(val, subcls)
    elif isinstance(val, act.TagAction):
        return 0
    elif isinstance(val, act.Action):
        tmp = 1 if isinstance(val.subject, ast.is_subclass(subcls, bs.BaseSubject)) else 0
        return tmp + len([v for v in val.objects if isinstance(v, subcls)])
    elif isinstance(val, bs.BaseSubject):
        return 1 if isinstance(val, ast.is_subclass(subcls, bs.BaseSubject)) else 0
    elif isinstance(val, list) or isinstance(val, tuple):
        return count_subjects_in(val, subcls)
    else:
        return 0

def _count_subjects_in_group(group: act.ActionGroup, subcls: bs.BaseSubject) -> int:
    tmp = 0
    for a in ast.is_instance(group, act.ActionGroup).actions:
        tmp += _count_subjects_(a, subcls)
    return tmp


def _has_a_subject_(val, subcls: bs.BaseSubject) -> bool:
    if isinstance(val, act.ActionGroup):
        return _has_a_subject_in_group(val, subcls)
    elif isinstance(val, act.TagAction):
        return False
    elif isinstance(val, act.Action):
        return isinstance(val.subject, ast.is_subclass(subcls, bs.BaseSubject)) \
                or len([v for v in val.objects if isinstance(v, subcls)]) >= 1
    elif isinstance(val, list) or isinstance(val, tuple):
        return has_a_subject_in(val, subcls)
    else:
        return False


def _has_a_subject_in_group(group: act.ActionGroup, subcls: bs.BaseSubject) -> bool:
    for a in ast.is_instance(group, act.ActionGroup).actions:
        if _has_a_subject_(a, subcls):
            return True
    else:
        return False


def _has_the_action_(val, target: act.Action) -> bool:
    if isinstance(val, act.ActionGroup):
        return _has_the_action_in_group(val, target)
    elif isinstance(val, act.TagAction):
        return False
    elif isinstance(val, act.Action):
        return val == ast.is_instance(target, act.Action)
    elif isinstance(val, list) or isinstance(val, tuple):
        return has_the_action_in(val, target)
    else:
        return False


def _has_the_action_in_group(group: act.ActionGroup, target: act.Action) -> bool:
    for a in ast.is_instance(group, act.ActionGroup).actions:
        if _has_the_action_(a, target):
            return True
    else:
        return False


def _has_the_subject(val, target: bs.BaseSubject) -> bool:
    if isinstance(val, act.ActionGroup):
        return _has_the_subject_in_group(val, target)
    elif isinstance(val, act.TagAction):
        return False
    elif isinstance(val, act.Action):
        return val.subject == ast.is_instance(target, bs.BaseSubject) \
                or len([v for v in val.objects if v == target]) >= 1
    elif isinstance(val, list) or isinstance(val, tuple):
        return has_the_subject_in(val)
    else:
        return False


def _has_the_subject_in_group(group: act.ActionGroup, target: bs.BaseSubject) -> bool:
    for a in ast.is_instance(group, act.ActionGroup).actions:
        if _has_the_subject(a, target):
            return True
    else:
        return False
