# -*- coding: utf-8 -*-
"""Common functions for storybuilder.
"""
from .action import Action, ActionGroup
from .basesubject import _BaseSubject
from .enums import LangType
from .subject import Something


def behavior_with_np_of(act: Action) -> str:
    tmp_head = ""
    tmp_tail = ""
    if act.is_negative:
        tmp_head += "~~"
        tmp_tail += "~~"
    if act.is_passive:
        tmp_head += "_"
        tmp_tail += "_"
    return "{}{}{}".format(tmp_head, str(act.behavior), tmp_tail)


def comma_of(lang: LangType) -> str:
    return "、" if lang == LangType.JPN else ", "


def description_str_from(act: Action, lang: LangType) -> str:
    return comma_of(lang).join(act.descriptions)


def descriptions_if(act: Action, lang: LangType) -> str:
    return description_str_from(act, lang)if act.descriptions else act.info


def dialogue_from_description(act: Action, lang: LangType) -> str:
    return "「」".format(description_str_from(act, lang)) if lang == LangType.JPN else ' "{}" '.format(description_str_from(act, lang))


def dialogue_from_description_if(act: Action, lang: LangType) -> str:
    return dialogue_from_description(act, lang) if act.descriptions else dialogue_from_info(act, lang)


def dialogue_from_info(act: Action, lang: LangType) -> str:
    return "「{}」".format(act.info) if lang == LangType.JPN else ' "{}" '.format(act.info)


def object_names_of(act: Action) -> str:
    tmp = []
    for obj in act.objects:
        if isinstance(obj, _BaseSubject):
            tmp.append(something_name_if(obj))
    return "/".join(tmp)


def sentence_from(act: Action, lang: LangType) -> str:
    return "　{}。".format(description_str_from(act, lang)) if lang == LangType.JPN else " {}. ".format(description_str_from(act, lang))


def something_name_if(obj: _BaseSubject) -> str:
    return "何か" if isinstance(obj, Something) else obj.name


def subject_name_of(act: Action) -> str:
    return something_name_if(act.subject) if act.subject else ""

