# -*- coding: utf-8 -*-
"""Useful tools for test with story builder
"""

from .acttypes import ActType, Behavior
from .base import Act, Stage, DayTime


def checked_if_all_actions(acts):
    '''Check if actions is an action object.
    
    Args:
        acts (:tuple:obj:`Act`): actions as scene or episodes.
    Returns:
        True if tuple is all Act objects, otherwise False
    '''
    for a in acts:
        if not isinstance(a, Act):
            return False
    return True


def checked_has_basic_info(test_case, acts, hero, rival, why_keyword, how_keyword):
    '''Check to contain basic informations.

    Args:
        acts (:tuple:obj:`Act`): actions as scene or episodes.
        hero (:obj:'Person'): hero object to need instantiation.
        rival (:obj:`Person`): rival object to need instantiation.
    Returns:
        True if complete checked, otherwise False
    Raise:
        if no contain the target.
    '''
    ERR_NOT_EXISTS = "{} is not exists!"
    # Who:
    for a in acts:
        if hero.name is a.subject.name:
            break
    else:
        test_case.fail(ERR_NOT_EXISTS.format(hero.name))
    # Whom:
    for a in acts:
        if rival.name is a.subject.name: break
    else:
        test_case.fail(ERR_NOT_EXISTS.format(rival.name))
    # When:
    for a in acts:
        if isinstance(a.subject, DayTime): break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('DayTime'))
    # Where:
    for a in acts:
        if isinstance(a.subject, Stage): break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('Stage'))
    # What:
    for a in acts:
        if hero.name is a.subject.name:
            if a.behavior in (Behavior.MUST_DO, Behavior.WANT):
                break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('Purpose'))
    # Why:
    for a in acts:
        if a.act_type is ActType.THINK:
            if why_keyword in a.action:
                break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('Reason'))
    # How:
    for a in acts:
        if a.act_type in (ActType.ACT, ActType.DESC, ActType.TELL):
            if how_keyword in a.action:
                break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('Process'))
    # Result:
    for a in acts:
        if a.behavior is Behavior.RESULT: break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('Result'))

    return True
