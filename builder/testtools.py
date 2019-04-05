# -*- coding: utf-8 -*-
"""Useful tools for test with story builder
"""
import unittest
from .sbutils import assert_isclass
from .action import Action, ActionGroup
from .basesubject import _BaseSubject, Info, Nothing
from .commons import behavior_with_np_of, infos_of, object_names_of, objects_from_without_something, subject_name_of
from .person import Person
from .subject import DayTime, Item, Stage, Something, Word


_ASSERT_MSG = "{} Must be {}!"


# public functions
def followed_all_flags(test_case: unittest.TestCase, story: ActionGroup) -> bool:
    '''Check if all flags and deflags.
    '''
    assert_isclass(story, ActionGroup)

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
    assert_isclass(story, ActionGroup)

    return _has_a_daytime_in_group(story)


def has_a_item(story: ActionGroup) -> bool:
    '''Check if a item in the story.
    '''
    assert_isclass(story, ActionGroup)

    return _has_a_item_in_group(story)


def has_a_person(story: ActionGroup) -> bool:
    '''Check if a person in the story.
    '''
    assert_isclass(story, ActionGroup)

    return _has_a_person_in_group(story)


def has_a_stage(story: ActionGroup) -> bool:
    '''Check if a stage in the story.
    '''
    assert_isclass(story, ActionGroup)

    return _has_a_stage_in_group(story)


def has_a_word(story: ActionGroup) -> bool:
    '''Check if a word in the story.
    '''
    assert_isclass(story, ActionGroup)

    return _has_a_word_in_group(story)


def has_basic_infos(test_case: unittest.TestCase, story: ActionGroup,
        hero: Person, rival: Person) -> bool:
    '''Check basic info.

    Basic informations are Who, Whom, When, Where
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(hero, Person)
    assert_isclass(rival, Person)

    ERR_MSG = "is not exists!"
    is_succeeded = True
    # who
    if not _has_the_person_in_group(story, hero):
        test_case.fail("Hero {} {}".format(hero.name, ERR_MSG))
        is_succeeded = False
    # whom
    if not _has_the_person_in_group(story, rival):
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
        what: Action, why: Action, how: Action, result: Action,
        is_fuzzy: bool=False) -> bool:
    '''Check if the story has outline informations.
    '''
    assert_isclass(test_case, unittest.TestCase)
    assert_isclass(story, ActionGroup)
    assert_isclass(what, Action)
    assert_isclass(why, Action)
    assert_isclass(how, Action)
    assert_isclass(result, Action)

    is_succeed = True
    if is_fuzzy:
        if not _has_the_action_in_group_with_fuzzy(story, what): # what
            is_succeed = _fail_message_without_target(test_case, "Purpose", what)
        if not _has_the_action_in_group_with_fuzzy(story, why): # why
            is_succeed = _fail_message_without_target(test_case, "Reason", why)
        if not _has_the_action_in_group_with_fuzzy(story, how): # how
            is_succeed = _fail_message_without_target(test_case, "Process", how)
        if not _has_the_action_in_group_with_fuzzy(story, result): # result
            is_succeed = _fail_message_without_target(test_case, "Result", result)
    else:
        if not _has_the_action_in_group(story, what): # what
            is_succeed = _fail_message_without_target(test_case, "Purpose", what)
        if not _has_the_action_in_group(story, why): # why
            is_succeed = _fail_message_without_target(test_case, "Reason", why)
        if not _has_the_action_in_group(story, how): # how
            is_succeed = _fail_message_without_target(test_case, "Process", how)
        if not _has_the_action_in_group(story, result): # result
            is_succeed = _fail_message_without_target(test_case, "Result", result)

    return is_succeed


def has_the_action(story: ActionGroup, target: Action) -> bool:
    '''Check if the action in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, Action)

    return _has_the_action_in_group(story, target)


def has_the_daytime(story: ActionGroup, target: DayTime) -> bool:
    '''Check if the daytime in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, DayTime)

    return _has_the_daytime_in_group(story, target)


def has_the_item(story: ActionGroup, target: Item) -> bool:
    '''Check if the item in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, Item)

    return _has_the_item_in_group(story, target)


def has_the_person(story: ActionGroup, target: Person) -> bool:
    '''Check if the person in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, Person)

    return _has_the_person_in_group(story, target)


def has_the_stage(story: ActionGroup, target: Stage) -> bool:
    '''Check if the stage in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, Stage)

    return _has_the_stage_in_group(story, target)


def has_the_word(story: ActionGroup, target: Word) -> bool:
    '''Check if the word in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, Word)

    return _has_the_word_in_group(story, target)


def is_all_actions(story: ActionGroup) -> bool:
    '''Check if the story is all of an action and an action group.
    '''
    assert_isclass(story, ActionGroup)

    return _is_actiongroup_all_actions(story)


# private functions
def _count_info_in_objects(objs: tuple) -> int:
    assert_isclass(objs, tuple)

    return len(tuple(v for v in objs if isinstance(v, Info)))


def _count_nothing_in_objects(objs: tuple) -> int:
    assert_isclass(objs, tuple)

    return len(tuple(v for v in objs if isinstance(v, Nothing)))


def _count_something_in_objects(objs: tuple) -> int:
    assert_isclass(objs, tuple)

    return len(tuple(v for v in objs if isinstance(v, Something)))


def _fail_message_without_target(test_case: unittest.TestCase,
        title: str, act: Action) -> bool:
    assert_isclass(test_case, unittest.TestCase)
    assert_isclass(title, str)
    assert_isclass(act, Action)

    ERR_MSG = "is not exists!"

    test_case.fail("{} = {}({}):{} - {}".format(
        title,
        subject_name_of(act),
        behavior_with_np_of(act),
        object_names_of(act),
        infos_of(act),
        ERR_MSG
        ))

    return False


def _flag_gatherd(act: Action, is_flag: bool) ->str:
    assert_isclass(act, Action)
    
    return act.flag if is_flag else act.deflag


def _flags_gathered_in_group(group: ActionGroup, is_flag: bool=True) -> list:
    assert_isclass(group, ActionGroup)

    tmp = []
    for a in group.actions:
        if isinstance(a, ActionGroup):
            tmp.extend(_flags_gathered_in_group(a, is_flag))
        else:
            tmp.append(_flag_gatherd(a, is_flag))
    return tmp


def _has_a_daytime(act: Action) -> bool:
    assert_isclass(act, Action)

    return isinstance(act.subject, DayTime) \
            or len(tuple(v for v in act.objects if isinstance(v, DayTime))) > 0


def _has_a_daytime_in_group(group: ActionGroup) -> bool:
    assert_isclass(group, ActionGroup)
    
    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_a_daytime_in_group(a):
                return True
        else:
            if _has_a_daytime(a):
                return True
    else:
        return False


def _has_a_item(act: Action) -> bool:
    assert_isclass(act, Action)

    return isinstance(act.subject, Item) \
            or len(tuple(v for v in act.objects if isinstance(v, Item))) > 0


def _has_a_item_in_group(group: ActionGroup) -> bool:
    assert_isclass(group, ActionGroup)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_a_item_in_group(a):
                return True
        else:
            if _has_a_item(a):
                return True
    else:
        return False


def _has_a_person(act: Action) -> bool:
    assert_isclass(act, Action)

    return isinstance(act.subject, Person) \
            or len(tuple(v for v in act.objects if isinstance(v, Person))) > 0


def _has_a_person_in_group(group: ActionGroup) -> bool:
    assert_isclass(group, ActionGroup)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_a_person_in_group(a):
                return True
        else:
            if _has_a_person(a):
                return True
    else:
        return False


def _has_a_stage(act: Action) -> bool:
    assert_isclass(act, Action)

    return isinstance(act.subject, Stage) \
            or len(tuple(v for v in act.objects if isinstance(v, Stage))) > 0


def _has_a_stage_in_group(group: ActionGroup) -> bool:
    assert_isclass(group, ActionGroup)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_a_stage_in_group(a):
                return True
        else:
            if _has_a_stage(a):
                return True
    else:
        return False


def _has_a_word(act: Action) -> bool:
    assert_isclass(act, Action)
   
    return isinstance(act.subject, Word) \
            or len(tuple(v for v in act.objects if isinstance(v, Word))) > 0


def _has_a_word_in_group(group: ActionGroup) -> bool:
    assert_isclass(group, ActionGroup)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_a_word_in_group(a):
                return True
        else:
            if _has_a_word(a):
                return True
    else:
        return False


def _has_info_at_action(act: Action) -> bool:
    assert_isclass(act, Action)

    return isinstance(act.subject, Info) \
            or _has_info_in_objects(act.objects)


def _has_info_in_objects(objs: tuple) -> bool:
    assert_isclass(objs, tuple)

    return _count_info_in_objects(objs) > 0


def _has_nothing_at_action(act: Action) -> bool:
    assert_isclass(act, Action)

    return isinstance(act.subject, Nothing) \
            or _has_nothing_in_objects(act.objects)


def _has_nothing_in_objects(objs: tuple) -> bool:
    assert_isclass(objs, tuple)

    return _count_nothing_in_objects(objs) > 0


def _has_something_at_action(act: Action) -> bool:
    assert_isclass(act, Action)

    return isinstance(act.subject, Something) \
            or _has_something_in_objects(act.objects)


def _has_something_in_objects(objs: tuple) -> bool:
    assert_isclass(objs, tuple)

    return _count_something_in_objects(objs) > 0


def _has_the_action_in_group(group: ActionGroup, target: Action) -> bool:
    assert_isclass(group, ActionGroup)
    assert_isclass(target, Action)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_action_in_group(a, target):
                return True
        else:
            if _is_the_action(a, target):
                return True
    else:
        return False


def _has_the_action_in_group_with_fuzzy(group: ActionGroup, target: Action) -> bool:
    assert_isclass(group, ActionGroup)
    assert_isclass(target, Action)
    
    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_action_in_group_with_fuzzy(a, target):
                return True
        else:
            if _near_eq_is_the_action(a, target):
                return True
    else:
        return False


def _has_the_daytime(act: Action, target: DayTime) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, DayTime)

    if not _has_a_daytime(act):
        return False

    if isinstance(act.subject, DayTime) and _is_the_subject(act.subject, target):
        return True

    for obj in act.objects:
        if isinstance(obj, DayTime) and _is_the_subject(obj, target):
            return True
    else:
        return False


def _has_the_daytime_in_group(group: ActionGroup, target: DayTime) -> bool:
    assert_isclass(group, ActionGroup)
    assert_isclass(target, DayTime)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_daytime_in_group(a, target):
                return True
        else:
            if _has_the_daytime(a, target):
                return True
    else:
        return False


def _has_the_info(info: Info, target: Info) -> bool:
    assert_isclass(info, Info)
    assert_isclass(target, Info)

    return target.note in info.note


def _has_the_infos(objs: tuple, targets: tuple) -> bool:
    for target in targets:
        if isinstance(target, Info):
            is_matched = False
            for obj in objs:
                if isinstance(obj, Info) and _has_the_info(obj, target):
                    is_matched = True
                    break
            if not is_matched:
                return False
    return True


def _has_the_item(act: Action, target: Item) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Item)

    if not _has_a_item(act):
        return False

    if isinstance(act.subject, Item) and _is_the_subject(act.subject, target):
        return True

    for obj in act.objects:
        if isinstance(obj, Item) and _is_the_subject(obj, target):
            return True
    else:
        return False


def _has_the_item_in_group(group: ActionGroup, target: Item) -> bool:
    assert_isclass(group, ActionGroup)
    assert_isclass(target, Item)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_item_in_group(a, target):
                return True
        else:
            if _has_the_item(a, target):
                return True
    else:
        return False


def _has_the_person(act: Action, target: Person) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Person)

    if not _has_a_person(act):
        return False

    if isinstance(act.subject, Person) and _is_the_subject(act.subject, target):
        return True

    for obj in act.objects:
        if isinstance(obj ,Person) and _is_the_subject(obj, target):
            return True
    else:
        return False


def _has_the_person_in_group(group: ActionGroup, target: Person) -> bool:
    assert_isclass(group, ActionGroup)
    assert_isclass(target, Person)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_person_in_group(a, target):
                return True
        else:
            if _has_the_person(a, target):
                return True
    else:
        return False


def _has_the_stage(act: Action, target: Stage) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Stage)

    if not _has_a_stage(act):
        return False

    if isinstance(act.subject, Stage) and _is_the_subject(act.subject, target):
        return True

    for obj in act.objects:
        if isinstance(obj, Stage) and _is_the_subject(obj, target):
            return True
    else:
        return False


def _has_the_stage_in_group(group: ActionGroup, target: Stage) -> bool:
    assert_isclass(group, ActionGroup)
    assert_isclass(target, Stage)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_stage_in_group(a, target):
                return True
        else:
            if _has_the_stage(a, target):
                return True
    else:
        return False


def _has_the_word(act: Action, target: Word) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Word)

    if not _has_a_word(act):
        return False

    if isinstance(act.subject, Word) and _is_the_subject(act.subject, target):
        return True

    for obj in act.objects:
        if isinstance(obj, Word) and _is_the_subject(obj, target):
            return True
    else:
        return False


def _has_the_word_in_group(group: ActionGroup, target: Word) -> bool:
    assert_isclass(group, ActionGroup)
    assert_isclass(target, Word)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_word_in_group(a, target):
                return True
        else:
            if _has_the_word(a, target):
                return True
    else:
        return False


def _is_actiongroup_all_actions(group: ActionGroup) -> bool:
    assert_isclass(group, ActionGroup)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if not _is_actiongroup_all_actions(a):
                return False
        else:
            if not isinstance(a, Action):
                return False
    else:
        return True


def _is_the_action(act: Action, target: Action) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Action)

    return act.act_type is target.act_type \
            and _is_the_action_behavior(act, target) \
            and _is_the_action_subject(act, target) \
            and _is_the_action_objects(act, target) \
            and _is_the_action_infos(act, target)


def _is_the_action_behavior(act: Action, target: Action) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Action)

    return act.behavior is target.behavior \
            and act.auxverb is target.auxverb \
            and act.is_negative == target.is_negative \
            and act.is_passive == target.is_passive


def _is_the_action_infos(act: Action, target: Action) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Action)

    return _is_the_infos(act.objects, target.objects)


def _is_the_action_subject(act: Action, target: Action) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Action)

    return _is_the_subject(act.subject, target.subject)


def _is_the_action_objects(act: Action, target: Action) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Action)

    return _is_the_objects(act.objects, target.objects)


def _is_the_infos(objs: tuple, targets: tuple) -> bool:
    assert_isclass(objs, tuple)

    for target in targets:
        if isinstance(target, Info):
            is_matched = False
            for obj in objs:
                if _is_the_subject(target, obj):
                    is_matched = True
                    break
            if not is_matched:
                return False
    return True


def _is_the_objects(objs: tuple, targets: tuple) -> bool:
    assert_isclass(objs, tuple)

    for target in targets:
        if isinstance(target, Info) or isinstance(target, Nothing):
            continue
        is_matched = False
        for obj in objs:
            if _is_the_subject(target, obj):
                is_matched = True
                break
        if not is_matched:
            return False
    return True


def _is_the_subject(subject: _BaseSubject, target: _BaseSubject) -> bool:
    assert_isclass(subject, _BaseSubject)
    assert_isclass(target, _BaseSubject)

    return type(subject) == type(target) \
            and subject.name == target.name \
            and subject.note == target.note


def _near_eq_is_the_action(act: Action, target: Action) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Action)

    return act.act_type is target.act_type \
            and _is_the_action_behavior(act, target) \
            and _near_eq_is_the_subject(act.subject, target.subject) \
            and _near_eq_is_the_objects(act.objects, target.objects) \
            and _near_eq_is_the_infos(act.objects, target.objects)


def _near_eq_is_the_infos(objs: tuple, targets: tuple) -> bool:
    assert_isclass(objs, tuple)
    assert_isclass(targets, tuple)

    if _has_something_in_objects(objs) or _has_something_in_objects(targets):
        origins_num = _count_something_in_objects(objs) + _count_info_in_objects(objs)
        targets_num = _count_something_in_objects(targets) + _count_info_in_objects(targets)
        fail_count = 0
        for target in targets:
            if isinstance(target, Info):
                is_matched = False
                for obj in objs:
                    if isinstance(obj, Info) and _has_the_info(obj, target):
                        is_matched = True
                        break
                if is_matched:
                    fail_count += 1

        if origins_num > targets_num:
            return (fail_count - (origins_num - targets_num)) <= 0
        else:
            return (fail_count - (targets_num - origins_num)) <= 0
    else:
        return _has_the_infos(objs, targets)


def _near_eq_is_the_objects(objs: tuple, targets: tuple) -> bool:
    assert_isclass(objs, tuple)
    assert_isclass(targets, tuple)

    if _has_something_in_objects(objs) or _has_something_in_objects(targets):
        origins_num = _count_something_in_objects(objs) + _count_info_in_objects(objs)
        targets_num = _count_something_in_objects(targets) + _count_info_in_objects(targets)
        if origins_num  > targets_num:
            tmp = objects_from_without_something(targets) - objects_from_without_something(objs)
            return len(tmp) == (origins_num - targets_num)
        else:
            tmp = objects_from_without_something(objs) - objects_from_without_something(targets)
            return len(tmp) == (targets_num - origins_num)
    else:
        return _is_the_objects(objs, targets)


def _near_eq_is_the_subject(subject: _BaseSubject, target: _BaseSubject) -> bool:
    assert_isclass(subject, _BaseSubject)
    assert_isclass(target, _BaseSubject)

    return isinstance(subject, Something) or isinstance(target, Something) \
            or _is_the_subject(subject, target)

