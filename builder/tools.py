# -*- coding: utf-8 -*-
"""Utility tools for story building
"""
from __future__ import print_function
import os
import argparse

from .acttypes import ActType, TagType, LangType
from .acttypes import behavior_str_of
from .acttypes import tag_str_of
from .base import Action, ActionGroup


# output

def build_to_story(story: ActionGroup):
    '''Build a story.

    Args:
        story (:obj:ActionGroup:): a story actions.
    Returns:
        True: if complete to success, otherwise False.
    '''
    assert isinstance(story, ActionGroup), "The story is not ActionGroup"
    FILE_NAME = "story"
    options = options_parsed()
    file_name = options.filename if options.filename else FILE_NAME
    return output_story(story, file_name, options.action, options.build, options.debug)


def options_parsed():
    '''Get and setting a commandline option.

    Returns:
        :obj:`ArgumentParser`: contain commandline options.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--action', help="output as action data", action='store_true')
    parser.add_argument('-b', '--build', help="build and output as a file", action='store_true')
    parser.add_argument('-d', '--debug', help="with debug mode", action='store_true')
    parser.add_argument('-i', '--info', help="display with informations", action='store_true')
    parser.add_argument('-f', '--filename', help="advanced output file name")

    # get result
    args = parser.parse_args()

    return (args)


def output_story(story: ActionGroup, filename: str, is_action_data: bool=False, is_out_as_file: bool=False, is_debug: bool=False):
    '''Output a story.

    Args:
        story (:obj:`ActionGroup`): a story action group.
    Returns:
        True: if complete to success, otherwise False.
    '''
    if is_out_as_file:
        return _output_story_to_file(
                _story_data_converted(story, is_action_data, is_debug),
                filename, is_action_data, is_debug)
    else:
        return _output_story_to_console(
                _story_data_converted(story, is_action_data, is_debug),
                is_debug)


def _story_data_converted(story: ActionGroup, is_action_data: bool, is_debug: bool) -> list:
    return  _story_converted_as_action(story, is_debug) if is_action_data else _story_converted_as_description(story, is_debug)


def _output_story_to_console(story: list, is_debug: bool):
    for s in story:
        print(s)
    return True


def _output_story_to_file(story: list, filename: str, is_action_data: bool, is_debug: bool):
    EXT_MARKDOWN = 'md'
    BUILD_DIR = 'build'
    if not os.path.isdir(BUILD_DIR):
        os.makedirs(BUILD_DIR)
    fullpath = os.path.join(BUILD_DIR, "{}.{}".format("{}_a".format(filename) if is_action_data else filename, EXT_MARKDOWN))
    with open(fullpath, 'w') as f:
        for s in story:
            f.write("{}\n".format(s))

    return True


def _story_converted_as_action(story: ActionGroup, is_debug: bool) -> list:
    return _story_converted_as_action_in_group(story, 1, is_debug)


def _story_converted_as_action_in_group(group: ActionGroup, level: int, is_debug: bool) -> list:
    tmp = []
    for a in group.actions:
        if isinstance(a, ActionGroup):
            tmp.extend(_story_converted_as_action_in_group(a, level + 1, is_debug))
        else:
            tmp.append(_action_str_by_type(a, group.lang, level, is_debug))
    return tmp


def _action_str_by_type(act: Action, lang: LangType, level: int, is_debug: bool) -> str:
    if act.act_type == ActType.ACT:
        if lang == LangType.JPN:
            return "{:\u3000<8s}:{:\u3000<8s}:{}:{}".format(act.subject.name, behavior_str_of(act.behavior), act.action, "" if act.note == "nothing" or not act.note else act.note)
        else:
            return "{:8}:{:8}:{}:{}".format(act.subject.name, behavior_str_of(act.behavior), act.action, "" if act.note == "nothing" or not act.note else act.note)
    elif act.act_type == ActType.EXPLAIN:
        if lang == LangType.JPN:
            return "{:\u3000<8s}:{:\u3000<8s}:{}:{}".format(act.subject.name, behavior_str_of(act.behavior), act.action, "" if act.note == "nothing" or not act.note else act.note)
        else:
            return "{:8}:{:8}:{}:{}".format(act.subject.name, behavior_str_of(act.behavior), act.action, "" if act.note == "nothing" or not act.note else act.note)
    elif act.act_type == ActType.TAG:
        return _action_str_by_tag(act, level)
    elif act.act_type == ActType.TELL:
        if lang == LangType.JPN:
            return "{:\u3000<8s}:{:\u3000<8s}:「{}」:{}".format(act.subject.name, behavior_str_of(act.behavior), act.action, "" if act.note == "nothing" or act.note else act.note)
        else:
            return "{:8}:{:8}:「{}」:{}".format(act.subject.name, behavior_str_of(act.behavior), act.action, "" if act.note == "nothing" or act.note else act.note)
    elif act.act_type == ActType.TEST and is_debug:
        if lang == LangType.JPN:
            return "> {:\u3000<8s}:{:\u3000<8s}:{}:{}".format(act.subject.name, behavior_str_of(act.behavior), act.action, "" if act.note == "nothing" or act.note else act.note)
        else:
            return "> {:8}:{:8}:{}:{}".format(act.subject.name, behavior_str_of(act.behavior), act.action, "" if act.note == "nothing" or act.note else act.note)
    else:
        return ""

def _action_str_by_tag(act: Action, level: int) -> str:
    if act.name == tag_str_of(TagType.COMMENT):
        return "<!-- {} -->".format(act.action)
    elif act.name == tag_str_of(TagType.TITLE):
        return "{} {}".format("#" * level, act.action)
    else:
        return ""


def _story_converted_as_description(story: ActionGroup, is_debug: bool):
    return _story_converted_as_description_in_group(story, 1, is_debug)


def _story_converted_as_description_in_group(group: ActionGroup, level: int, is_debug: bool):
    tmp = []
    for a in group.actions:
        if isinstance(a, ActionGroup):
            tmp.extend(_story_converted_as_description_in_group(a, level + 1, is_debug))
        else:
            tmp.append(_description_str_by_type(a, group.lang, level, is_debug))
    return tmp


def _description_str_by_type(act: Action, lang: LangType, level: int, is_debug: bool) -> str:
    if act.act_type in (ActType.ACT, ActType.EXPLAIN):
        return "{}{}{}".format(_paragraphtop_by_lang(lang), act.description, _period_by_lang(lang))
    elif act.act_type == ActType.TELL:
        return "{}{}{}".format(_double_quatation_by_lang(lang), act.description, _double_quatation_by_lang(lang, False))
    elif act.act_type == ActType.TAG:
        return _description_str_by_tag(act, level, is_debug)
    elif act.act_type == ActType.TEST and is_debug:
        return "> {}".format(act.description if act.description else act.action)
    else:
        return ""


def _description_str_by_tag(act: Action, level: int, is_debug: bool) -> str:
    if act.name == tag_str_of(TagType.COMMENT):
        return ""
    elif act.name == tag_str_of(TagType.TITLE):
        return "{} {}".format("#" * level, act.description if act.description else act.action)
    else:
        return ""

def _period_by_lang(lang: LangType) -> str:
    return "。" if lang == LangType.JPN else ". "


def _comma_by_lang(lang: LangType) -> str:
    return "、" if lang == LangType.JPN else ", "


def _paragraphtop_by_lang(lang: LangType) -> str:
    return "　" if lang == LangType.JPN else " "


def _double_quatation_by_lang(lang: LangType, is_top: bool=True) -> str:
    if is_top:
        return "「" if lang == LangType.JPN else ' "'
    else:
        return "」" if lang == LangType.JPN else '" '
