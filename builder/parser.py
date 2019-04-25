# -*- coding: utf-8 -*-
"""Utility for parsing, converting and more.
"""
from . import assertion as ast
from . import action as act
from . import basesubject as bs
from . import enums as em
from . import info as inf
from . import strutils as sutl


# public methods
def actinfo_from_action(ac: act.Action, lv: int, lang: em.LangType, is_debug: bool) -> str:
    space = "\u3000" if lang is em.LangType.JPN else " "
    return "{test}{lihead}{subject:{space}<8s}:{verb}/{obj}".format(
            test="> " if is_debug else "",
            lihead=sutl.ul_tag_from("", lv),
            subject=ac.subject.name,
            space=space,
            verb=verb_from(ac),
            obj=actobject_names_from(ac),
            )


def actinfo_from_tag(ac: act.TagAction) -> str:
    if ast.is_instance(ac, act.TagAction).tag is em.TagType.BR:
        return "\n"
    elif ac.tag is em.TagType.COMMENT:
        return sutl.comment_tag_from(ac.info)
    elif ac.tag in (em.TagType.HEAD1, em.TagType.HEAD2, em.TagType.HEAD3):
        return sutl.head_tag_from(ac.info, title_level_of(ac.tag))
    elif ac.tag is em.TagType.HR:
        return sutl.hr_tag_from()
    elif ac.tag is em.TagType.SYMBOL:
        return f"\n{ac.info}\n"
    else:
        return ""


def actobject_from(val) -> bs.BaseSubject:
    if isinstance(val, bs.BaseSubject):
        return val
    elif isinstance(val, str):
        return inf.Info(val)
    else:
        return inf.Nothing()


def actobject_name_of(obj: bs.BaseSubject) -> str:
    if isinstance(obj, inf.Info):
        return obj.note
    elif isinstance(obj, inf.Nothing):
        return ""
    elif isinstance(obj, inf.Something):
        return "X"
    elif isinstance(obj, bs.BaseSubject):
        return obj.name
    return ""


def actobject_names_from(ac: act.Action) -> str:
    return "/".join([actobject_name_of(v) for v in ast.is_instance(ac, act.Action).objects])


def description_from_action(ac: act.Action, lang: em.LangType) -> str:
    if ac.description.desc_type is em.DescType.DESCRIPTION:
        return _desc_as_description_from(ac.description, lang)
    elif ac.description.desc_type is em.DescType.DIALOGUE:
        return _desc_as_dialogue_from(ac.description, lang)
    else:
        # TODO: desc group implement
        return ""


def description_from_tag(ac: act.TagAction) -> str:
    if ast.is_instance(ac, act.TagAction).tag is em.TagType.BR:
        return "\n"
    elif ac.tag is em.TagType.COMMENT:
        return ""
    elif ac.tag in (em.TagType.HEAD1, em.TagType.HEAD2, em.TagType.HEAD3):
        return sutl.head_tag_from(ac.info, title_level_of(ac.tag))
    elif ac.tag is em.TagType.HR:
        return sutl.hr_tag_from()
    elif ac.tag is em.TagType.SYMBOL:
        return f"\n{ac.info}\n"
    else:
        return ""


def story_filtered_by_priority(story: list, pri_filter: int) -> list:
    tmp = []
    for v in ast.is_list(story):
        if isinstance(v, act.ActionGroup):
            tmp.extend(_story_filtered_by_pri_in_group(v, pri_filter))
        elif isinstance(v, act.TagAction):
            tmp.append(v)
        elif isinstance(v, act.Action):
            if v.priority >= pri_filter:
                tmp.append(v)
        else:
            return []
    return tmp


def str_to_dict_by_splitter(target: [str, dict], defkey: str, defval: str) -> dict:
    if isinstance(target, dict):
        return target
    elif isinstance(target, str):
        if ":" in target:
            tmp = target.split(":")
            ret = {}
            for k, v in zip(tmp[0::2], tmp[1::2]):
                ret[k] = v
            if not ast.is_str(defkey) in ret.keys():
                ret.update({defkey: ast.is_str(defval)})
            return ret
        else:
            return {defkey: target}
    else:
        return {ast.is_str(defkey): ast.is_str(defval)}


def str_to_tuple_from_args(args) -> tuple:
    if args:
        if isinstance(args, str):
            return (args,)
        else:
            return tuple(ast.is_list(args))
    else:
        return ()


def subjects_retrieved_from(story: list, subcls: bs.BaseSubject) -> list:
    tmp = []
    for v in ast.is_list(story):
        tmp.extend(_subjects_retrieved_from_(v, subcls))
    return tmp


def title_level_of(tag: em.TagType) -> int:
    if ast.is_instance(tag, em.TagType) is em.TagType.HEAD1:
        return 1
    elif tag is em.TagType.HEAD2:
        return 2
    elif tag is em.TagType.HEAD3:
        return 3
    else:
        return 0


def titles_retrieved_from(story: list) -> list:
    tmp = []
    for v in ast.is_list(story):
        tmp.extend(_titles_retrieved_from_(v))
    return tmp


def verb_from(ac: act.Action) -> str:
    return ast.is_instance(ac, act.Action).verb


# private methods
def _desc_as_description_from(dsc: act.ds.Desc, lang: em.LangType) -> str:
    return sutl.description_from(
            sutl.comma_by(lang).join(dsc.data),
            lang)


def _desc_as_dialogue_from(dsc: act.ds.Desc, lang: em.LangType) -> str:
    return sutl.dialogue_from(
            sutl.comma_by(lang).join(dsc.data),
            lang)


def _story_filtered_by_pri_in_group(group: act.ActionGroup, pri_filter: int) -> list:
    tmp = []
    for a in ast.is_instance(group, act.ActionGroup).actions:
        if isinstance(a, act.ActionGroup):
            tmp.extend(_story_filtered_by_pri_in_group(a, pri_filter))
        elif isinstance(a, act.TagAction):
            tmp.append(a)
        elif isinstance(a, act.Action):
            if a.priority >= pri_filter:
                tmp.append(a)
        else:
            return []
    return tmp


def _subjects_retrieved_from_(val, subcls: bs.BaseSubject) -> list:
    if isinstance(val, act.ActionGroup):
        return _subjects_retrieved_from_in_group(val, subcls)
    elif isinstance(val, act.TagAction):
        return []
    elif isinstance(val, act.Action):
        tmp = [val.subject] if isinstance(ast.is_instance(val, act.Action).subject, ast.is_subclass(subcls, bs.BaseSubject)) else []
        return tmp + [v for v in val.objects if isinstance(v, subcls)]


def _subjects_retrieved_from_in_group(group: act.ActionGroup, subcls: bs.BaseSubject) -> list:
    tmp = []
    for a in ast.is_instance(group, act.ActionGroup).actions:
        tmp.extend(_subjects_retrieved_from_(a, subcls))
    return tmp


def _titles_retrieved_from_(val) -> list:
    if isinstance(val, act.ActionGroup):
        return _titles_retrieved_from_in_group(val)
    elif isinstance(val, act.TagAction):
        return [val] if val.tag in (em.TagType.HEAD1, em.TagType.HEAD2, em.TagType.HEAD3) else []
    elif isinstance(val, act.Action):
        return []
    else:
        return []


def _titles_retrieved_from_in_group(group: act.ActionGroup) -> list:
    tmp = []
    for a in ast.is_instance(group, act.ActionGroup).actions:
        tmp.extend(_titles_retrieved_from_(a))
    return tmp