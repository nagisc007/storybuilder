# -*- coding: utf-8 -*-
"""Utility tools for story building
"""
from __future__ import print_function
import os
import argparse

from .acttypes import ActType, GroupType, TagType, LangType
from .acttypes import tag_str_of
from .base import Action, ActionGroup
from .commons import behavior_with_np_of, description_if, dialogue_from_description_if, dialogue_from_info, object_name_of, sentence_from, subject_name_of


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
        filename (str): a filename.
        is_action_data (bool, optional): if True, output as an action data.
        is_out_as_file (bool, optional): if True, output to a markdown file.
        is_debug (bool, optional): if True, use a debug mode.
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


# private functions
def _action_str_by_tag(act: Action, group_type: GroupType, level: int) -> str:
    if act.note == tag_str_of(TagType.COMMENT):
        return "<!-- {} -->".format(act.info)
    elif act.note == tag_str_of(TagType.TITLE):
        if group_type == GroupType.STORY:
            return "{} {}\n".format("#" * level, act.info)
        elif group_type == GroupType.SCENE:
            return "**{}**".format(act.info)
        else:
            return ""
    else:
        return ""


def _action_str_by_type(act: Action, lang: LangType, group_type: GroupType, level: int, is_debug: bool) -> str:
    if act.act_type == ActType.ACT:
        if lang == LangType.JPN:
            return "{}{:\u3000<6s}:{:\u3000<6s}/{}{}{}".format(
                    _list_head_inserted(level),
                    subject_name_of(act),
                    _behavior_with_obj(act),
                    act.info, _flag_info_if(act), _note_info_if(act))
        else:
            return "{}{:8}:{:8}/{}{}{}".format(
                    _list_head_inserted(level),
                    act.subject.name,
                    _behavior_with_obj(act),
                    act.info, _flag_info_if(act), _note_info_if(act))
    elif act.act_type == ActType.EXPLAIN:
        if lang == LangType.JPN:
            return "{}{:\u3000<6s}:{:\u3000<6s}/{}{}{}".format(
                    _list_head_inserted(level),
                    act.subject.name,
                    _behavior_with_obj(act),
                    act.info, _flag_info_if(act), _note_info_if(act))
        else:
            return "{}{:8}:{:8}/{}{}{}".format(
                    _list_head_inserted(level),
                    act.subject.name,
                    _behavior_with_obj(act),
                    act.info, _flag_info_if(act), _note_info_if(act))
    elif act.act_type == ActType.TAG:
        return _action_str_by_tag(act, group_type, level)
    elif act.act_type == ActType.TELL:
        if lang == LangType.JPN:
            return "{}{:\u3000<6s}:{:\u3000<6s}/{}{}{}".format(
                    _list_head_inserted(level),
                    act.subject.name,
                    _behavior_with_obj(act),
                    dialogue_from_info(act, lang), _flag_info_if(act), _note_info_if(act))
        else:
            return "{}{:8}:{:8}/{}{}{}".format(
                    _list_head_inserted(level),
                    act.subject.name,
                    _behavior_with_obj(act),
                    dialogue_from_info(act, lang), _flag_info_if(act), _note_info_if(act))
    elif act.act_type == ActType.TEST and is_debug:
        if lang == LangType.JPN:
            return "> {:\u3000<6s}:{:\u3000<6s}/{}{}{}".format(act.subject.name,
                    _behavior_with_obj(act),
                    act.info, _flag_info_if(act), _note_info_if(act))
        else:
            return "> {:8}:{:8}{}/{}{}{}".format(act.subject.name,
                    _behavior_with_obj(act),
                    act.info, _flag_info_if(act), _note_info_if(act))
    else:
        return ""


def _behavior_with_obj(act: Action) -> str:
    return "{}({})".format(behavior_with_np_of(act), object_name_of(act))


def _description_str_by_tag(act: Action, group_type: GroupType, level: int, is_debug: bool) -> str:
    if act.note == tag_str_of(TagType.COMMENT):
        return ""
    elif act.note == tag_str_of(TagType.TITLE):
        if group_type == GroupType.STORY:
            return "{} {}\n".format("#" * level, description_if(act))
        elif group_type == GroupType.SCENE:
            return "**{}**".format(description_if(act))
        else:
            return ""
    else:
        return ""


def _description_str_by_type(act: Action, lang: LangType, group_type: GroupType, level: int, is_debug: bool) -> str:
    if act.act_type in (ActType.ACT, ActType.EXPLAIN):
        return sentence_from(act, lang)
    elif act.act_type == ActType.TELL:
        return dialogue_from_description_if(act, lang)
    elif act.act_type == ActType.TAG:
        return _description_str_by_tag(act, group_type, level, is_debug)
    elif act.act_type == ActType.TEST and is_debug:
        return "> {}".format(act.description if act.description else act.info)
    else:
        return ""


def _list_head_inserted(level: int) -> str:
    return "    " * (level - 1) + "- "


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
    return _story_converted_as_action_in_group(story, story.group_type, 1, is_debug)


def _story_converted_as_action_in_group(group: ActionGroup, group_type: GroupType, level: int, is_debug: bool) -> list:
    tmp = []
    if isinstance(group, ActionGroup):
        for a in group.actions:
            if isinstance(a, ActionGroup):
                tmp.extend(_story_converted_as_action_in_group(a, a.group_type, level + 1, is_debug))
            else:
                tmp.append(_action_str_by_type(a, group.lang, group.group_type, level, is_debug))
    else:
        tmp.append(_action_str_by_type(group, group.lang, group.group_type, level, is_debug))
    return tmp



def _story_converted_as_description(story: ActionGroup, is_debug: bool):
    return _story_converted_as_description_in_group(story, story.group_type, 1, is_debug)


def _story_converted_as_description_in_group(group: ActionGroup, group_type: GroupType, level: int, is_debug: bool):
    tmp = []
    for a in group.actions:
        if isinstance(a, ActionGroup):
            tmp.extend(_story_converted_as_description_in_group(a, a.group_type, level + 1, is_debug))
        else:
            tmp.append(_description_str_by_type(a, group.lang, group.group_type, level, is_debug))
    return tmp


def _story_data_converted(story: ActionGroup, is_action_data: bool, is_debug: bool) -> list:
    '''Story data converter.
    
    Args:
        story (:obj:`ActionGroup`): a story action group.
        is_action_data (bool, optional): if True, output as an action data.
        is_debug (bool, optional): if True, use a debug mode.
    Returns:
        :list:str: strings list as a story.
    '''
    return  _story_converted_as_action(story, is_debug) if is_action_data else _story_converted_as_description(story, is_debug)


def _note_info_if(act: Action) -> str:
    return "" if (act.note == "nothing" or not act.note) else ":{}".format(act.note)


def _flag_info_if(act: Action) -> str:
    tmp = ""
    if act.flag:
        tmp += "F(" + act.flag + ")"
    if act.deflag:
        tmp += "D(" + act.deflag + ")"
    return tmp
