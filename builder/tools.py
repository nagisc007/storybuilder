# -*- coding: utf-8 -*-
"""Utility tools for story building
"""
from __future__ import print_function
import os
import argparse
import re
from .sbutils import assert_isclass, assert_isbool, assert_isint, assert_isstr
from .action import Action, ActionGroup, TagAction
from .commons import behavior_with_np_of, descriptions_of_if, dialogue_from_description_if, dialogue_from_info
from .commons import extraspace_chopped, infos_of, object_names_of, sentence_from, subject_name_of
from .enums import ActType, GroupType, TagType, LangType
from .subject import _BaseSubject
from .person import Person


# functions
def build_to_story(story: ActionGroup):
    '''Build a story.

    Args:
        story (:obj:ActionGroup:): a story actions.
    Returns:
        True: if complete to success, otherwise False.
    '''
    assert_isclass(story, ActionGroup)

    FILE_NAME = "story"
    options = options_parsed()
    file_name = options.filename if options.filename else FILE_NAME
    return output_story(story, file_name, options.action, options.build, options.priority, options.debug)


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
    parser.add_argument('-p', '--priority', help="output an action filtered priorities", type=int, default=5)

    # get result
    args = parser.parse_args()

    return (args)


def output_story(story: ActionGroup, filename: str, is_action_data: bool=False,
        is_out_as_file: bool=False, pri_filter: int=Action.MIN_PRIORITY,
        is_debug: bool=False):
    '''Output a story.

    Args:
        story (:obj:`ActionGroup`): a story action group.
        filename (str): a filename.
        is_action_data (bool, optional): if True, output as an action data.
        is_out_as_file (bool, optional): if True, output to a markdown file.
        pri_filter (int, optional): the number has filtered to output an action.
        is_debug (bool, optional): if True, use a debug mode.
    Returns:
        True: if complete to success, otherwise False.
    '''
    assert_isclass(story, ActionGroup)
    assert_isstr(filename)
    assert_isbool(is_action_data)
    assert_isbool(is_out_as_file)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    if is_out_as_file:
        return _output_story_to_file(
                _story_data_converted(story, is_action_data, pri_filter, is_debug),
                filename, is_action_data, is_debug)
    else:
        return _output_story_to_console(
                _story_data_converted(story, is_action_data, pri_filter, is_debug),
                is_debug)


# private functions
def _action_of_by_tag(act: TagAction, group_type: GroupType, level: int) -> str:
    assert_isclass(act, TagAction)
    assert_isclass(group_type, GroupType)
    assert_isint(level)

    if act.tag is TagType.COMMENT:
        return _comment_of(act)
    elif act.tag is TagType.TITLE and group_type is GroupType.STORY:
        return _story_title_of(act, level)
    elif act.tag is TagType.TITLE and group_type is GroupType.SCENE:
        return _scene_title_of(act)
    elif act.tag is TagType.HR:
        return _hr_of()
    else:
        return ""


def _action_of_by_type(act: Action, lang: LangType, group_type: GroupType, level: int,
        pri_filter: int, is_debug: bool) -> str:
    assert_isclass(act, Action)
    assert_isclass(lang, LangType)
    assert_isclass(group_type, GroupType)
    assert_isint(level)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    if pri_filter > act.priority:
        return ""
    if act.act_type in (ActType.ACT, ActType.EXPLAIN):
        if lang is LangType.JPN:
            return _action_with_obj_and_info_as_jpn(act, group_type, False)
        else:
            return _action_with_obj_and_info_as_eng(act, group_type, False)
    elif act.act_type is ActType.TAG:
        return _action_of_by_tag(act, group_type, level)
    elif act.act_type == ActType.TELL:
        if lang is LangType.JPN:
            return _action_with_obj_and_info_as_jpn(act, group_type, True)
        else:
            return _action_with_obj_and_info_as_eng(act, group_type, True)
    elif act.act_type is ActType.TEST and is_debug:
        if lang is LangType.JPN:
            return _action_with_obj_and_info_as_jpn(act, group_type, False, True)
        else:
            return _action_with_obj_and_info_as_eng(act, group_type, False, True)
    else:
        return ""


def _action_with_obj_and_info_as_eng(act: Action, group_type: GroupType, is_dialogue: bool, is_test: bool=False) -> str:
    assert_isclass(act, Action)
    assert_isclass(group_type, GroupType)
    assert_isbool(is_dialogue)
    assert_isbool(is_test)

    return "{}{}{:8}:{:8}/{}{}".format(
            "> " if is_test else "",
            _list_head_inserted(group_type),
            subject_name_of(act),
            _behavior_with_obj(act),
            dialogue_from_info(act, LangType.ENG) if is_dialogue else infos_of(act),
            _flag_info_if(act)
            )
   

def _action_with_obj_and_info_as_jpn(act: Action, group_type: GroupType, is_dialogue: bool, is_test: bool=False) -> str:
    assert_isclass(act, Action)
    assert_isclass(group_type, GroupType)
    assert_isbool(is_dialogue)
    assert_isbool(is_test)

    return "{}{}{:\u3000<6s}:{:\u3000<6s}/{}{}".format(
            "> " if is_test else "",
            _list_head_inserted(group_type),
            subject_name_of(act),
            _behavior_with_obj(act),
            dialogue_from_info(act, LangType.JPN) if is_dialogue else infos_of(act),
            _flag_info_if(act)
            )

def _behavior_with_obj(act: Action) -> str:
    assert_isclass(act, Action)

    return "{}({})".format(behavior_with_np_of(act), object_names_of(act))


def _comment_of(act: TagAction) -> str:
    assert_isclass(act, TagAction)

    return "<!--{}-->".format(act.note)


def _desc_str_replaced_tag(descstr: str, subject: _BaseSubject) -> str:
    assert_isstr(descstr)
    assert_isclass(subject, _BaseSubject)

    if isinstance(subject, Person):
        tmp = descstr
        for k, v in subject.calling.items():
            tmp = re.sub(r'\${}'.format(k), v, tmp)
        return re.sub(r'\$S', subject.calling['me'], tmp)
    return descstr


def _description_of_by_tag(act: TagAction, lang: LangType, group_type: GroupType, level: int, is_debug: bool) -> str:
    assert_isclass(act, TagAction)
    assert_isclass(lang, LangType)
    assert_isclass(group_type, GroupType)
    assert_isint(level)
    assert_isbool(is_debug)

    if act.tag is TagType.COMMENT:
        return _comment_of(act) if is_debug else ""
    elif act.tag is TagType.TITLE and group_type is GroupType.STORY:
        return _story_title_of(act, level)
    elif act.tag is TagType.TITLE and group_type is GroupType.SCENE and is_debug:
        return _scene_title_of(act)
    elif act.tag is TagType.HR:
        return _hr_of()
    else:
        return ""


def _description_of_by_type(act: Action, lang: LangType, group_type: GroupType, level: int, is_debug: bool) -> str:
    assert_isclass(act, Action)
    assert_isclass(lang, LangType)
    assert_isclass(group_type, GroupType)
    assert_isint(level)
    assert_isbool(is_debug)

    if act.descs.is_omitted:
        return ""
    elif act.act_type is ActType.TAG:
        return _description_of_by_tag(act, lang, group_type, level, is_debug)
    elif act.act_type is ActType.TEST and is_debug:
        return "> {}".format(descriptions_of_if(act, lang))
    elif not act.descs.data:
        return ""
    elif act.act_type in (ActType.ACT, ActType.EXPLAIN) and not act.descs.is_dialogue:
        return _desc_str_replaced_tag(sentence_from(act, lang), act.subject)
    elif act.act_type is ActType.TELL or act.descs.is_dialogue:
        return _desc_str_replaced_tag(dialogue_from_description_if(act, lang), act.subject)
    else:
        return ""


def _flag_info_if(act: Action) -> str:
    assert_isclass(act, Action)

    tmp = ""
    if act.flag:
        tmp += "[" + act.flag + "](f-" + act.flag + ")"
    if act.deflag:
        tmp += "[D:" + act.deflag + "](d-" + act.deflag + ")"
    return tmp


def _hr_of(num: int=9) -> str:
    assert_isint(num)

    return "--------" * num


def _list_head_inserted(group_type: GroupType) -> str:
    assert_isclass(group_type, GroupType)

    if group_type is GroupType.COMBI:
        return "    " * 2 + "- "
    elif group_type is GroupType.SCENE:
        return "    " * 1 + "- "
    else:
        return "- "


def _output_story_to_console(story: list, is_debug: bool) -> bool:
    assert_isclass(story, list)
    assert_isbool(is_debug)

    idx = 0
    for s in story:
        print(_output_with_linenumber(s, idx, is_debug))
        idx += 1
    return True


def _output_story_to_file(story: list, filename: str, is_action_data: bool, is_debug: bool) -> bool:
    assert_isclass(story, list)
    assert_isstr(filename)
    assert_isbool(is_action_data)
    assert_isbool(is_debug)

    EXT_MARKDOWN = 'md'
    BUILD_DIR = 'build'
    if not os.path.isdir(BUILD_DIR):
        os.makedirs(BUILD_DIR)
    fullpath = os.path.join(BUILD_DIR, "{}.{}".format("{}_a".format(filename) if is_action_data else filename, EXT_MARKDOWN))
    with open(fullpath, 'w') as f:
        idx = 0
        for s in story:
            f.write("{}\n".format(_output_with_linenumber(s, idx, is_debug)))
            idx += 1

    return True


def _output_with_linenumber(val: str, num: int, is_debug: bool) -> str:
    assert_isstr(val)
    assert_isint(num)
    assert_isbool(is_debug)

    return "{}: {}".format(num, val) if is_debug else val


def _scene_title_of(act: TagAction) -> str:
    assert_isclass(act, TagAction)

    return "**{}**".format(act.note)


def _story_converted_as_action(story: ActionGroup, pri_filter: int, is_debug: bool) -> list:
    '''
    Args:
        story (:obj:`ActionGroup`): a story action group.
        pri_filter (int): a number filtered an action.
        is_debug (bool): if True, with a debug mode.
    '''
    assert_isclass(story, ActionGroup)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    return _story_converted_as_action_in_group(story, story.group_type, 1, pri_filter, is_debug)


def _story_converted_as_action_in_group(group: ActionGroup, group_type: GroupType,
        level: int, pri_filter: int, is_debug: bool) -> list:
    assert_isclass(group, ActionGroup)
    assert_isclass(group_type, GroupType)
    assert_isint(level)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    tmp = []
    for a in group.actions:
        if isinstance(a, ActionGroup):
            tmp.extend(_story_converted_as_action_in_group(a, a.group_type, level + 1, pri_filter, is_debug))
        else:
            tmp.append(_action_of_by_type(a, group.lang, group.group_type, level, pri_filter, is_debug))
    return tmp


def _story_converted_as_description(story: ActionGroup, is_debug: bool):
    assert_isclass(story, ActionGroup)
    assert_isbool(is_debug)

    return _story_converted_as_description_in_group(story, story.group_type, 1, is_debug)


def _story_converted_as_description_in_group(group: ActionGroup, group_type: GroupType, level: int, is_debug: bool):
    assert_isclass(group, ActionGroup)
    assert_isclass(group_type, GroupType)
    assert_isint(level)
    assert_isbool(is_debug)

    tmp = []
    for a in group.actions:
        if isinstance(a, ActionGroup):
            tmp.extend(_story_converted_as_description_in_group(a, a.group_type, level + 1, is_debug))
        else:
            val = _description_of_by_type(a, group.lang, group.group_type, level, is_debug)
            if val:
                tmp.append(val)
    if group_type is GroupType.COMBI:
        return extraspace_chopped("".join(tmp), group.lang)
    else:
        return tmp


def _story_data_converted(story: ActionGroup, is_action_data: bool, pri_filter: int, is_debug: bool) -> list:
    '''Story data converter.
    
    Args:
        story (:obj:`ActionGroup`): a story action group.
        is_action_data (bool): if True, output as an action data.
        pri_filter (int): the number filtered an action.
        is_debug (bool): if True, use a debug mode.
    Returns:
        :list:str: strings list as a story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isbool(is_action_data)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    return  _story_converted_as_action(story, pri_filter, is_debug) if is_action_data else _story_converted_as_description(story, is_debug)


def _story_title_of(act: TagAction, level: int) -> str:
    assert_isclass(act, TagAction)
    assert_isint(level)

    return "{}{} {}\n".format("\n" if level > 1 else "", "#" * level, act.note)

