# -*- coding: utf-8 -*-
"""Building story.
"""
from __future__ import print_function
import os
import argparse
from . import assertion as ast
from . import action as act
from . import analyzer as ayz
from . import enums as em
from . import parser as ps
from . import strutils as sutl


_BASEMENT = 10 # for estimated count


# public methods
def build_to_story(story: list, lang: em.LangType) -> bool: # pragma: no cover
    '''Build a story.

    Args:
        story (:list:obj:`BaseAction`): a story objects.
    Returns:
        True if complete to success, otherwise False.
    '''
    FILENAME = "story"
    options = _options_parsed()
    filename = options.filename if options.filename else FILENAME
    is_succeeded = True
    as_file = options.build
    pri_filter = options.priority
    is_debug = options.debug
    story_filtered = ps.story_filtered_by_priority(story, pri_filter)

    if options.action:
        if not _output_story_as_actinfo(story_filtered, lang, filename, as_file, is_debug):
            is_succeeded = False

    if options.description:
        if not _output_story_as_descriptions(story_filtered, lang, filename, as_file, is_debug):
            is_succeeded = False

    if options.info:
        if not _output_story_as_info(story_filtered, lang, filename, as_file, is_debug):
            is_succeeded = False

    if not _output_baseinfo(story_filtered, lang, is_debug):
        is_succeeded = False

    return is_succeeded


# private methods
def _actinfo_from_(val, lv: int, lang: em.LangType, is_debug: bool) -> list:
    if isinstance(val, act.ActionGroup):
        lv2 += 1 if val.group_type is em.GroupType.COMBI else 0
        return _actinfo_from_in_group(val, lv2, lang, is_debug)
    elif isinstance(val, act.TagAction):
        v = ps.actinfo_from_tag(val)
        return [v] if v else []
    elif isinstance(val, act.Action):
        v = ps.actinfo_from_action(val, lv, lang, is_debug)
        return [v] if v else []
    else:
        return []


def _actinfo_from(story: list, lang: em.LangType, is_debug: bool) -> list:
    tmp = []
    for v in ast.is_list(story):
        tmp.extend(_actinfo_from_(v, 0, lang, is_debug))
    return tmp


def _actinfo_from_in_group(group: act.ActionGroup, lv: int, lang: em.LangType,
        is_debug: bool) -> list:
    tmp = []
    for a in ast.is_instance(group, act.ActionGroup).actions:
        tmp.extend(_actinfo_from_(a, lv, lang, is_debug))
    return tmp


def _acttypes_percents_from(story: list) -> list:
    acttypes = ayz.count_acttypes(story)
    total = ayz.count_acts(story)
    def act_percent(char, atype):
        return "- {}: {:.2f}%".format(
                char,
                acttypes[atype] / total * 100
                )
    return [
            "## Actions",
            f"- Total: {total}",
            act_percent("be", em.ActType.BE),
            act_percent("behav", em.ActType.BEHAV),
            act_percent("deal", em.ActType.DEAL),
            act_percent("do", em.ActType.DO),
            act_percent("explain", em.ActType.EXPLAIN),
            act_percent("feel", em.ActType.FEEL),
            act_percent("look", em.ActType.LOOK),
            act_percent("move", em.ActType.MOVE),
            act_percent("talk", em.ActType.TALK),
            act_percent("think", em.ActType.THINK),
            ]


def _charcount_from(story: list, lang: em.LangType) -> list:
    total = _descs_count_from(story, lang)
    estimated = _estimated_description_count_from(story, lang)
    return [
            "## Characters",
            f"- Total: {total}",
            f"- Estimated: {estimated}",
            ]


def _descs_count_from_(val, lang: em.LangType) -> int:
    if isinstance(val, act.ActionGroup):
        return _descs_count_from_in_group(val, lang)
    elif isinstance(val, act.TagAction):
        return 0
    elif isinstance(val, act.Action):
        return len(sutl.str_space_chopped(
            ps.description_from_action(val, lang)))
    else:
        return 0


def _descs_count_from(story: list, lang: em.LangType) -> int:
    tmp = 0
    for v in ast.is_list(story):
        tmp += _descs_count_from_(v, lang)
    return tmp


def _descs_count_from_in_group(group: act.ActionGroup, lang: em.LangType) -> int:
    tmp = 0
    for a in ast.is_instance(group, act.ActionGroup).actions:
        tmp += _descs_count_from_(a, lang)
    return tmp


def _descs_from_(val, lang: em.LangType, is_debug: bool) -> list:
    if isinstance(val, act.ActionGroup):
        return _descs_from_in_group(val, lang, is_debug)
    elif isinstance(val, act.TagAction):
        v = ps.description_from_tag(val)
        return [v] if v else []
    elif isinstance(val, act.Action):
        v = ps.description_from_action(val, lang)
        return [v] if v else []
    else:
        return []


def _descs_from(story: list, lang: em.LangType, is_debug: bool) -> list:
    tmp = []
    for v in ast.is_list(story):
        tmp.extend(_descs_from_(v, lang, is_debug))
    return tmp


def _descs_from_in_group(group: act.ActionGroup, lang: em.LangType,
        is_debug: bool) -> list:
    tmp = []
    for a in ast.is_instance(group, act.ActionGroup).actions:
        tmp.extend(_descs_from_(a, lang, is_debug))
    return tmp


def _estimated_description_count_from(story: list, lang: em.LangType) -> int:
    acttypes = ayz.count_acttypes(story)
    return sum([
        acttypes[em.ActType.BE] * 1,
        acttypes[em.ActType.BEHAV] * 1,
        acttypes[em.ActType.DEAL] * 2,
        acttypes[em.ActType.DO] * 2,
        acttypes[em.ActType.EXPLAIN] * 4,
        acttypes[em.ActType.FEEL] * 2,
        acttypes[em.ActType.LOOK] * 4,
        acttypes[em.ActType.MOVE] * 2,
        acttypes[em.ActType.TALK] * 4,
        acttypes[em.ActType.THINK] * 4,
            ]) * _BASEMENT

def _options_parsed(): # pragma: no cover
    '''Get and setting a commandline option.

    Returns:
        :obj:`ArgumentParser`: contain commandline options.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--action', help="output as action data", action='store_true')
    parser.add_argument('-b', '--build', help="build and output as a file", action='store_true')
    parser.add_argument('-d', '--description', help="output as descriptions", action='store_true')
    parser.add_argument('-i', '--info', help="display with informations", action='store_true')
    parser.add_argument('-f', '--filename', help="advanced output file name")
    parser.add_argument('-p', '--priority', help="output an action filtered priorities", type=int, default=act.Action.PRIORITY_DEFAULT)
    parser.add_argument('--debug', help="with a debug mode", action='store_true')

    # get result
    args = parser.parse_args()

    return (args)


def _output_baseinfo(story: list, lang: em.LangType,
        is_debug: bool) -> bool: # pragma: no cover
    '''Output a basic information.

    Output infos:
        * total description characters
        * act type percent
    '''
    tmp = _charcount_from(story, lang) + _acttypes_percents_from(story)
    return _output_to_console(tmp, is_debug)


def _output_story_as_actinfo(story: list, lang: em.LangType, filename: str, asfile: bool,
        is_debug: bool) -> bool: # pragma: no cover
    '''
    Action infos:
        * action infos
    '''
    # contents heads
    actinfos = _actinfo_from(story, 1, lang, is_debug)
    # flags
    tmp = actinfos
    if asfile:
        return _output_to_file(tmp, filename, "_a", is_debug)
    else:
        return _output_to_console(tmp, is_debug)


def _output_story_as_descriptions(story: list, lang: em.LangType, filename: str,
        asfile: bool, is_debug: bool) -> bool: # pragma: no cover
    '''
    Descriptions:
        * descriptions
    '''
    # TODO: 各種フォーマット選択
    # contents heads
    descriptions = _descs_from(story, lang, is_debug)
    tmp = descriptions
    if asfile:
        return _output_to_file(tmp, filename, "", is_debug)
    else:
        return _output_to_console(tmp, is_debug)


def _output_story_as_info(story: list, filename: str, asfile: bool,
        is_debug: bool) -> bool: # pragma: no cover
    '''
    Story info:
        * total description characters
        * act type percents
    '''
    _output_charcounts(story)
    _output_acttype_percents(story)
    # flags
    # 各種db
    tmp = []
    if asfile:
        return _output_to_file(tmp, filename, "_i", is_debug)
    else:
        return _output_to_console(tmp, is_debug)


def _output_to_console(data: list, is_debug: bool) -> bool:
    is_succeeded = True
    idx = 0
    for d in data:
        tmp = "{idx}: {d}" if is_debug else d
        print(f"{tmp}")
        idx += 1
    return is_succeeded


def _output_to_file(data: list, filename: str, suffix: str, is_debug: bool) -> bool:
    EXT_MARKDOWN = 'md' # TODO: select file type
    BUILD_DIR = 'build' # TODO: select build dir
    if not os.path.isdir(BUILD_DIR):
        os.makedirs(BUILD_DIR)
    fullpath = os.path.join(BUILD_DIR, "{}{}.{}".format(
        ast.is_str(filename), ast.is_str(suffix), EXT_MARKDOWN))
    is_succeeded = True
    with open(fullpath, 'w') as f:
        idx = 0
        for d in data:
            tmp = "{idx}: {d}" if is_debug else d
            f.write(f"{tmp}\n")
            idx += 1

    return is_succeeded

