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


def checked_has_basic_info(test_case, acts, hero, rival, what_word, why_word, how_word, result_word):
    '''Check to contain basic informations.

    Args:
        acts (:tuple:obj:`Act`): actions as scene or episodes.
        hero (:obj:'Person'): hero object to need instantiation.
        rival (:obj:`Person`): rival object to need instantiation.
        what_word (str): check the word as the purpose.
        why_word (str): check the word as the reason.
        how_word (str): check the word as the process.
        result_word (str): check the word as the result.
    Returns:
        True if complete checked, otherwise False
    Raise:
        if no contain the target.
    '''
    ERR_NOT_EXISTS = "{} is not exists!i -- {}"
    # Who:
    for a in acts:
        if hero.name == a.subject.name: break
    else:
        test_case.fail(ERR_NOT_EXISTS.format(hero.name, "need to set the Person"))
    # Whom:
    for a in acts:
        if rival.name == a.subject.name: break
    else:
        test_case.fail(ERR_NOT_EXISTS.format(rival.name, "need to set the Person"))
    # When:
    for a in acts:
        if isinstance(a.subject, DayTime): break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('DayTime', "need to set a DayTime"))
    # Where:
    for a in acts:
        if isinstance(a.subject, Stage): break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('Stage', "need to set a Stage"))
    # What:
    for a in acts:
        if hero.name == a.subject.name:
            if a.act_type in (ActType.THINK, ActType.TELL):
                if what_word in a.action:
                    break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('Purpose', "need to set an Act with Behavior.MUST_DO or WANT"))
    # Why:
    for a in acts:
        if a.act_type in (ActType.THINK, ActType.TELL):
            if why_word in a.action:
                break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('Reason', "need to set an Act with ActType.THINK or TELL"))
    # How:
    for a in acts:
        if a.act_type in (ActType.ACT, ActType.DESC, ActType.TELL):
            if how_word in a.action:
                break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('Process', "need to set an actional Act with the keyword"))
    # Result:
    for a in acts:
        if a.act_type in (ActType.ACT, ActType.TELL, ActType.THINK):
            if result_word in a.action:
                break
    else:
        test_case.fail(ERR_NOT_EXISTS.format('Result', "need to set an Act with Behavior.RESULT"))

    return True
