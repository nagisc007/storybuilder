# -*- coding: utf-8 -*-
"""Utility for analyze.
"""
from typing import Any
from . import action as act
from . import assertion as ast
from . import basesubject as bs
from . import enums as em
from . import info as inf


# public methods
def contains_the_action_in(story: list, target: act.Action) -> bool:
    return _contains_the_action_in(story, target)


def count_acts(story: list) -> int:
    return _count_acts_from_in(story)


def count_acttypes(story: list) -> dict:
    return {
            em.ActType.BE: _count_acttype_in(story, em.ActType.BE),
            em.ActType.BEHAV: _count_acttype_in(story, em.ActType.BEHAV),
            em.ActType.DEAL: _count_acttype_in(story, em.ActType.DEAL),
            em.ActType.DO: _count_acttype_in(story, em.ActType.DO),
            em.ActType.EXPLAIN: _count_acttype_in(story, em.ActType.EXPLAIN),
            em.ActType.FEEL: _count_acttype_in(story, em.ActType.FEEL),
            em.ActType.LOOK: _count_acttype_in(story, em.ActType.LOOK),
            em.ActType.MOVE: _count_acttype_in(story, em.ActType.MOVE),
            em.ActType.TALK: _count_acttype_in(story, em.ActType.TALK),
            em.ActType.TEST: _count_acttype_in(story, em.ActType.TEST),
            em.ActType.THINK: _count_acttype_in(story, em.ActType.THINK),
            }


def count_descripton_at_action(ac: act.Action, strict: bool=False) -> int:
    delta = len(ac.description.data) if strict else 0
    return sum([len(v) for v in ac.description.data]) + delta


def count_subjects_in(story: list, subcls: bs.BaseSubject)-> int:
    return _count_subjects_in(story, subcls)


def has_a_subject_in(story: list, subcls: bs.BaseSubject) -> bool:
    return _has_a_subject_in(story, subcls)


def has_the_action_in(story: list, target: act.Action) -> bool:
    return _has_the_action_in(story, target)


def has_the_keyword(story: list, target: str, strict: bool=False) -> bool:
    return _has_the_keyword_in(story, target, strict)


def has_the_keyword_in_descriptions(story: list, target: str) -> bool:
    return _has_the_keyword_in_desc_in(story, target)


def has_the_subject_in(story: list, target: bs.BaseSubject) -> bool:
    return _has_the_subject_in(story, target)


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
    if isinstance(val, (act.ActionGroup, list, tuple)):
        return _contains_the_action_in(val, target)
    elif isinstance(val, act.TagAction):
        return False
    elif isinstance(val, act.Action):
        return val.act_type is ast.is_instance(target, act.Action).act_type \
                and val.subject == target.subject \
                and val.auxverb is target.auxverb \
                and _compare_objects_with_something(val, target)
    else:
        return False


def _contains_the_action_in(vals: [act.ActionGroup, list, tuple],
        target: act.Action) -> bool:
    group = vals.actions if isinstance(vals, act.ActionGroup) else vals
    for a in group:
        if _contains_the_action_(a, target):
            return True
    else:
        return False


def _count_acts_from_(val) -> int:
    if isinstance(val, (act.ActionGroup, list, tuple)):
        return _count_acts_from_in(val)
    elif isinstance(val, act.TagAction):
        return 0
    elif isinstance(val, act.Action):
        return 1
    return 0


def _count_acts_from_in(vals: [act.ActionGroup, list, tuple]) -> int:
    group = vals.actions if isinstance(vals, act.ActionGroup) else vals
    return sum([_count_acts_from_(v) for v in group])


def _count_acttype_(val, acttype: em.ActType) -> int:
    if isinstance(val, (act.ActionGroup, list, tuple)):
        return _count_acttype_in(val, acttype)
    elif isinstance(val, act.TagAction):
        return 0
    elif isinstance(val ,act.Action):
        return 1 if val.act_type is acttype else 0
    else:
        return 0


def _count_acttype_in(vals: [act.ActionGroup, list, tuple],
        acttype: em.ActType) -> int:
    group = vals.actions if isinstance(vals, act.ActionGroup) else vals
    return sum([_count_acttype_(v, acttype) for v in group])


def _count_subjects_(val, subcls: bs.BaseSubject) -> int:
    if isinstance(val, (act.ActionGroup, list, tuple)):
        return _count_subjects_in(val, subcls)
    elif isinstance(val, act.TagAction):
        return 0
    elif isinstance(val, act.Action):
        tmp = 1 if isinstance(val.subject, ast.is_subclass(subcls, bs.BaseSubject)) else 0
        return tmp + len([v for v in val.objects if isinstance(v, subcls)])
    elif isinstance(val, bs.BaseSubject):
        return 1 if isinstance(val, ast.is_subclass(subcls, bs.BaseSubject)) else 0
    else:
        return 0


def _count_subjects_in(vals: [act.ActionGroup, list, tuple],
        subcls: bs.BaseSubject) -> int:
    group = vals.actions if isinstance(vals, act.ActionGroup) else vals
    return sum([_count_subjects_(v, subcls) for v in group])


def _exists_the_keyword_in_action(val: act.Action, target: str) -> bool:
    if ast.is_str(target) in ast.is_instance(val, act.Action).subject.name:
        return True
    for o in val.objects:
        if isinstance(o, inf.Info) and target in o.note:
            return True
        elif target in o.name:
            return True
    else:
        return False


def _exists_the_keyword_in_description(val: act.ds.Desc, target: str) -> bool:
    if isinstance(val, act.ds.DescGroup):
        # TODO: desc group implement
        return False
    elif isinstance(val, act.ds.NoDesc):
        return False
    elif isinstance(val, act.ds.Desc):
        return len([v for v in val.data if target in v]) > 0
    else:
        return _exists_the_keyword_in_description(val.description, target)


def _has_a_subject_(val, subcls: bs.BaseSubject) -> bool:
    if isinstance(val, (act.ActionGroup, list, tuple)):
        return _has_a_subject_in(val, subcls)
    elif isinstance(val, act.TagAction):
        return False
    elif isinstance(val, act.Action):
        return isinstance(val.subject, ast.is_subclass(subcls, bs.BaseSubject)) \
                or len([v for v in val.objects if isinstance(v, subcls)]) >= 1
    else:
        return False


def _has_a_subject_in(vals: [act.ActionGroup, list, tuple],
        subcls: bs.BaseSubject) -> bool:
    group = vals.actions if isinstance(vals, act.ActionGroup) else vals
    return len([v for v in group if _has_a_subject_(v, subcls)]) > 0


def _has_the_action_(val, target: act.Action) -> bool:
    if isinstance(val, (act.ActionGroup, list, tuple)):
        return _has_the_action_in(val, target)
    elif isinstance(val, act.TagAction):
        return False
    elif isinstance(val, act.Action):
        return val == ast.is_instance(target, act.Action)
    else:
        return False


def _has_the_action_in(vals: [act.ActionGroup, list, tuple],
        target: act.Action) -> bool:
    group = vals.actions if isinstance(vals, act.ActionGroup) else vals
    return len([v for v in group if _has_the_action_(v, target)]) > 0


def _has_the_keyword_(val: Any, target: str, strict: bool) -> bool:
    if isinstance(val, (act.ActionGroup, list, tuple)):
        return _has_the_keyword_in(val, target, strict)
    elif isinstance(val, act.TagAction):
        return False
    elif isinstance(val, act.Action):
        if strict:
            return _is_the_keyword_in_action(val, target)
        else:
            return _exists_the_keyword_in_action(val, target)
    else:
        return False


def _has_the_keyword_in(vals: [act.ActionGroup, list, tuple],
        target: str, strict: bool) -> bool:
    group = vals.actions if isinstance(vals, act.ActionGroup) else vals
    return len([v for v in group if _has_the_keyword_(v, target, strict)]) > 0


def _has_the_keyword_in_desc_(val: Any, target: str) -> bool:
    if isinstance(val, (act.ActionGroup, list, tuple)):
        return _has_the_keyword_in_desc_in(val, target)
    elif isinstance(val, act.TagAction):
        return False
    elif isinstance(val, act.Action):
        return _exists_the_keyword_in_description(val, target)
    else:
        return False


def _has_the_keyword_in_desc_in(vals: [act.ActionGroup, list, tuple],
        target :str) -> bool:
    group = vals.actions if isinstance(vals, act.ActionGroup) else vals
    return len([v for v in group if _has_the_keyword_in_desc_(v, target)]) > 0


def _has_the_subject(val, target: bs.BaseSubject) -> bool:
    if isinstance(val, (act.ActionGroup, list, tuple)):
        return _has_the_subject_in(val, target)
    elif isinstance(val, act.TagAction):
        return False
    elif isinstance(val, act.Action):
        return val.subject == ast.is_instance(target, bs.BaseSubject) \
                or len([v for v in val.objects if v == target]) >= 1
    else:
        return False


def _has_the_subject_in(vals: [act.ActionGroup, list, tuple],
        target: bs.BaseSubject) -> bool:
    group = vals.actions if isinstance(vals, act.ActionGroup) else vals
    return len([v for v in group if _has_the_subject(v, target)]) > 0


def _is_the_keyword_in_action(val: act.Action, target: str) -> bool:
    if ast.is_str(target) == ast.is_instance(val, act.Action).subject.name:
        return True
    for o in val.objects:
        if isinstance(o, inf.Info) and target == o.note:
            return True
        elif target == o.name:
            return True
    else:
        return False


def _is_the_keyword_in_description(val: [act.Action, act.ds.Desc],
        target: str) -> bool:
    if isinstance(val, act.ds.DescGroup):
        # TODO: implement desc group
        return False
    elif isinstance(val, act.ds.Desc):
        return len([v for v in val.data if ast.is_str(target) == v]) > 0
    elif isinstance(val, act.Action):
        return _is_the_keyword_in_description(val.description, target)
    else:
        return False

