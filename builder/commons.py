# -*- coding: utf-8 -*-
"""Common functions for storybuilder.
"""
from .acttypes import LangType
from .behavior import behavior_str_of
from .base import Action, ActionGroup, _BaseSubject


def behavior_with_np_of(act: Action) -> str:
    tmp_head = ""
    tmp_tail = ""
    if act.is_negative:
        tmp_head += "~~"
        tmp_tail += "~~"
    if act.is_passive:
        tmp_head += "_"
        tmp_tail += "_"
    return "{}{}{}".format(tmp_head, behavior_str_of(act.behavior), tmp_tail)


def description_if(act: Action) -> str:
    return act.description if act.description else act.info


def dialogue_from_description(act: Action, lang: LangType) -> str:
    return "「」".format(act.description) if lang == LangType.JPN else ' "{}" '.format(act.description)


def dialogue_from_description_if(act: Action, lang: LangType) -> str:
    return dialogue_from_description(act, lang) if act.description else dialogue_from_info(act, lang)


def dialogue_from_info(act: Action, lang: LangType) -> str:
    return "「{}」".format(act.info) if lang == LangType.JPN else ' "{}" '.format(act.info)


def object_name_of(act: Action) -> str:
    return act.object.name if act.object and isinstance(act.object, _BaseSubject) else ""


def sentence_from(act: Action, lang: LangType) -> str:
    return "　{}。".format(act.description) if lang == LangType.JPN else " {}. ".format(act.description)


def subject_name_of(act: Action) -> str:
    return act.subject.name if act.subject else ""

