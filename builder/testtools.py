# -*- coding: utf-8 -*-
"""Useful tools for test with story builder
"""

import unittest

from .base import ActType, Act, Must, Done, Title, Description
from .base import Person, Stage, Item, DayTime


def checked_if_all_actions(acts):
    '''Check if actions is an action object.
    
    Args:
        acts (tuple:obj:`Act`): actions as scene or episodes.
    Returns:
        True:
    '''
    for a in acts:
        if not isinstance(a, Act):
            return False
    return True


def checked_has_basic_info(acts, hero, rival):
    '''Check to contain basic informations.

    Args:
        acts (tuple:obj:`Act`): actions as scene or episodes.
        hero (obj:'Person'): hero object to need instantiation.
        rival (obj:`Person`): rival object to need instantiation.
    Returns:
        True:
    '''
    ERR_NOT_EXISTS = "{} is not exists!"
    # Who:
    for a in acts:
        if isinstance(a.subject, Must) or isinstance(a.subject, Done) or isinstance(a.subject, Title) or isinstance(a.subject, Description):
            continue
        if hero.name is a.subject.name:
            break
    else:
        raise AssertionError(ERR_NOT_EXISTS.format(hero.name))
    # Whom:
    for a in acts:
        if isinstance(a.subject, Must) or isinstance(a.subject, Done) or isinstance(a.subject, Title) or isinstance(a.subject, Description):
            continue
        if rival.name is a.subject.name: break
    else:
        raise AssertionError(ERR_NOT_EXISTS.format(rival.name))
    # When:
    for a in acts:
        if isinstance(a.subject, DayTime): break
    else:
        raise AssertionError(ERR_NOT_EXISTS.format('DayTime'))
    # Where:
    for a in acts:
        if isinstance(a.subject, Stage): break
    else:
        raise AssertionError(ERR_NOT_EXISTS.format('Stage'))
    # What:
    for a in acts:
        if a.act_type is ActType.MUST: break
    else:
        raise AssertionError(ERR_NOT_EXISTS.format('Must'))
    # Why: in preparation
    # How: in preparation
    # Result:
    for a in acts:
        if a.act_type is ActType.DONE: break
    else:
        raise AssertionError(ERR_NOT_EXISTS.format('Done'))
    return True
