# -*- coding: utf-8 -*-
"""Common functions for storybuilder.
"""
from .action import Action, ActionGroup, Description
from .basesubject import _BaseSubject, Info, Nothing
from .enums import LangType
from .subject import Something


_ASSERT_MSG = "{} Must be {}!"


def behavior_with_np_of(act: Action) -> str:
    assert isinstance(act, Action), "act Must be Action class!"

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


def description_of(act: Action, lang: LangType) -> str:
    return comma_of(lang).join(act.descs.data)


def descriptions_of_if(act: Action, lang: LangType) -> str:
    return description_of(act, lang) if act.descs.data else ""


def dialogue_from_description(act: Action, lang: LangType) -> str:
    return "「{}」".format(description_of(act, lang)) if lang == LangType.JPN else ' "{}" '.format(description_of(act, lang))


def dialogue_from_description_if(act: Action, lang: LangType) -> str:
    return dialogue_from_description(act, lang) if act.descs.data else dialogue_from_info(act, lang)


def dialogue_from_info(act: Action, lang: LangType) -> str:
    return "「{}」".format(infos_of(act).replace('/', '、')) if lang == LangType.JPN else ' "{}" '.format(infos_of(act).replace('/', ', '))


def infos_of(act: Action) -> str:
    '''Informations string from the action.

    Args:
        act (:obj:`Action`): an action.
    Returns:
        infromation string that the action has all Info.
    '''
    assert isinstance(act, Action), "act Must be Action class!"

    return "/".join(v.note for v in act.objects if isinstance(v, Info))


def infos_from(act: Action) -> set:
    assert isinstance(act, Action), _ASSERT_MSG.format("act", "Action")

    return set(v.note for v in act.objects if isinstance(v, Info))


def object_names_of(act: Action) -> str:
    tmp = []
    for obj in act.objects:
        if isinstance(obj, Info) or isinstance(obj, Nothing):
            continue
        elif isinstance(obj, _BaseSubject):
            tmp.append(something_name_if(obj))
    return "/".join(tmp)


def object_names_of_without_something(act: Action) -> str:
    assert isinstance(act, Action), _ASSERT_MSG.format("act", "Action")

    tmp = []
    for obj in act.objects:
        if isinstance(obj, Info) or isinstance(obj, Nothing) or isinstance(obj, Something):
            continue
        elif isinstance(obj, _BaseSubject):
            tmp.append(obj.name)
    return "/".join(tmp)


def objects_all_from(act: Action) -> set:
    tmp = []
    for obj in act.objects:
        if isinstance(obj, Nothing):
            continue
        elif isinstance(obj, Info):
            tmp.append("{}:{}".format(str(obj.CLS_NAME), obj.note))
        elif isinstance(obj, _BaseSubject):
            tmp.append("{}:{}".format(str(obj.CLS_NAME), something_name_if(obj)))
    return set(tmp)


def objects_from(act: Action) -> set:
    '''Gathering an action object's basic data.

    Args:
        act (:obj:`Action`): a target action.
    Returns:
        :set:str: the objects contain types and names.
    '''
    tmp = []
    for obj in act.objects:
        if isinstance(obj, Info) or isinstance(obj, Nothing):
            continue
        elif isinstance(obj, _BaseSubject):
            tmp.append("{}:{}".format(str(obj.CLS_NAME), something_name_if(obj)))
    return set(tmp)


def objects_from_without_something(objs: tuple) -> set:
    tmp = []
    for obj in objs:
        if isinstance(obj, Info) or isinstance(obj, Nothing) or isinstance(obj, Something):
            continue
        elif isinstance(obj, _BaseSubject):
            tmp.append("{}:{}".format(str(obj.CLS_NAME), obj.name))
    return set(tmp)


def objects_from_action_without_something(act: Action) -> set:
    assert isinstance(act, Action), _ASSERT_MSG.format("act", "Action")

    tmp = []
    for obj in act.objects:
        if isinstance(obj, Info) or isinstance(obj, Nothing) or isinstance(obj, Something):
            continue
        elif isinstance(obj, _BaseSubject):
            tmp.append("{}:{}".format(str(obj.CLS_NAME), obj.name))
    return set(tmp)


def sentence_from(act: Action, lang: LangType) -> str:
    return "　{}。".format(description_of(act, lang)) if lang == LangType.JPN else " {}. ".format(description_of(act, lang))


def something_name_if(obj: _BaseSubject) -> str:
    return "何か" if isinstance(obj, Something) else obj.name


def subject_name_of(act: Action) -> str:
    return something_name_if(act.subject) if act.subject else ""

