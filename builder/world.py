# -*- coding: utf-8 -*-
"""Define story manager class.
"""
from typing import Any
from . import action as act
from . import assertion as ast
from . import basesubject as bs
from . import day as dy
from . import enums as em
from . import info as inf
from . import item as itm
from . import person as psn
from . import stage as stg
from . import buildtool as btool


# classes
class AuxverbDict(object):
    """Utility dictionary for auxiliary verbs.
    """
    def __init__(self):
        self.can = em.AuxVerb.CAN
        self.may = em.AuxVerb.MAY
        self.must = em.AuxVerb.MUST
        self.none = em.AuxVerb.NONE
        self.should = em.AuxVerb.SHOULD
        self.want = em.AuxVerb.WANT
        self.will = em.AuxVerb.WILL


class SDict(dict):
    """Useful dictionary class.
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class TagManager(object):
    """Utility class for tag management.
    """
    def br(self) -> act.TagAction:
        return act.TagAction(em.TagType.BR)

    def comment(self, note: str) -> act.TagAction:
        return act.TagAction(em.TagType.COMMENT, note)

    def hr(self) -> act.TagAction:
        return act.TagAction(em.TagType.HR)

    def symbol(self, info: str) -> act.TagAction:
        return act.TagAction(em.TagType.SYMBOL, info)

    def title(self, title: str, lv: int=1) -> act.TagAction:
        tag = em.TagType.HEAD1 if lv <= 1 else (em.TagType.HEAD2 if lv == 2 else em.TagType.HEAD3)
        return act.TagAction(tag, title)


class World(SDict):
    """Story management class.

    Attributes:
        aux (:obj:`AuxverbDict`): auxiliary dictionary.
        day (:obj:`SDict`): day objects dictionary.
        deflag (:obj:`SDict`): deflag objects dictionary.
        flag (:obj:`SDict`): flag objects dictionary.
        i (:obj:`SDict`): info objects dictionary.
        lang (:enum:`LangType`): a language type.
        name (str): a name.
        note (str): a short description.
        stage (:obj:`SDict`): stage object dictionary.
        tag (:obj:`TagManager`): tag management.
    """
    def __init__(self, name: str, note: str="", lang: em.LangType=em.LangType.JPN):
        super().__init__()
        self.aux = AuxverbDict()
        self.day = SDict()
        self.deflag = SDict()
        self.flag = SDict()
        self.i = SDict()
        self.lang = ast.is_instance(lang, em.LangType)
        self.name = ast.is_str(name)
        self.note = ast.is_str(note)
        self.stage = SDict()
        self.tag = TagManager()

    def append_day(self, key: str, val: Any):
        return self._append_one(key, val, self.day, dy.Day)

    def append_flag(self, key: str, val: Any):
        self._append_one(key, val, self.flag, inf.Flag)
        return self._append_one(key, val, self.deflag, inf.Deflag)

    def append_info(self, key: str, val: Any):
        return self._append_one(key, val, self.i, inf.Info)

    def append_item(self, key: str, val: Any):
        return self._append_one(key, val, self, itm.Item)

    def append_person(self, key: str, val: Any):
        return self._append_one(key, val, self, psn.Person)

    def append_stage(self, key: str, val: Any):
        return self._append_one(key, val, self.stage, stg.Stage)

    def build(self, story: list) -> bool:
        return btool.build_to_story(story, self.lang)

    def chaptertitle(self, title: str) -> act.TagAction:
        return self.tag.title(title, 2)

    def combine(self, *args, lang: em.LangType=em.LangType.NONE) -> act.ActionGroup:
        return act.ActionGroup(*args,
                group_type=em.GroupType.COMBI,
                lang=lang if not lang is em.LangType.NONE else self.lang)

    def info(self, info: str) -> inf.Info:
        return inf.Info(info)

    def maintitle(self, title: str) -> act.TagAction:
        return self.tag.title(title, 1)

    def nothing(self) -> inf.Nothing:
        return inf.Nothing()

    def scene(self, title: str, *args,
            lang: em.LangType=em.LangType.NONE) -> act.ActionGroup:
        # TODO: stage and day setting
        tmp = ()
        if title:
            tmp = (self.tag.title(title, 3),) + args
        else:
            tmp = args
        return act.ActionGroup(*tmp,
                group_type=em.GroupType.SCENE,
                lang=lang if not lang is em.LangType.NONE else self.lang)

    def set_days(self, days: list):
        for v in ast.is_list(days):
            self.append_day(v[0], v[1:])
        return self

    def set_db(self, persons: list=None, stages: list=None, days: list=None,
            items: list=None, infos: list=None, flags: list=None):
        if persons:
            self.set_persons(persons)
        if stages:
            self.set_stages(stages)
        if days:
            self.set_days(days)
        if items:
            self.set_items(items)
        if infos:
            self.set_infos(infos)
        if flags:
            self.set_flags(flags)
        return self

    def set_flags(self, flags: list):
        for v in ast.is_list(flags):
            self.append_flag(v[0], v[1:])
        return self

    def set_infos(self, infos: list):
        for v in ast.is_list(infos):
            self.append_info(v[0], v[1:])
        return self

    def set_items(self, items: list):
        for v in ast.is_list(items):
            self.append_item(v[0], v[1:])
        return self

    def set_persons(self, persons: list):
        for v in ast.is_list(persons):
            self.append_person(v[0], v[1:])
        return self

    def set_stages(self, stages: list):
        for v in ast.is_list(stages):
            self.append_stage(v[0], v[1:])
        return self

    def something(self) -> inf.Something:
        return inf.Something()

    def X(self) -> inf.Something:
        return self.something()

    # privates
    def _append_one(self, key: str, val: Any, body: [SDict, dict], subcls: bs.BaseSubject):
        # TODO: duplicated name
        if body is self:
            self.__setitem__(ast.is_str(key), self._data_from(val, subcls))
        else:
            ast.is_instance(body, SDict).__setitem__(
                    ast.is_str(key), self._data_from(val, subcls))
        return self

    def _data_from(self, val: Any, subcls: bs.BaseSubject):
        return val if isinstance(val, subcls) else subcls(*val)

    def _lang_if(self, lang: em.LangType) -> em.LangType:
        return lang if not lang is em.LangType.NONE else self.lang
