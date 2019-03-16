# -*- coding: utf-8 -*-
"""Utility tools for story building
"""
from __future__ import print_function
import os
import argparse

from .acttypes import ActType
from .base import Act
from .base import Story, Episode, Scene


def story_builded(title: str, story: Story, filename: str='story', build_dir: str='build', is_debug: bool=False):
    '''Building a story.

    Args:
        title (str): a story title.
        story (:tuple:obj:`Story`): a story objects.
        filename (str, optional): a file name.
        build_dir (str, optional): a build path.
        is_debug (bool, optional): if True, with a debug mode.
    Returns:
        True: if complete success, otherwise False
    '''
    options = options_parsed()

    if options.action: # output as an action
        if options.build:
            output_md(title, story, is_desc=False, is_debug=is_debug)
        else:
            output(title, story, is_desc=False, is_debug=is_debug)
    if not options.descoff: # output as a description
        if options.build:
            output_md(title, story, is_desc=True, is_debug=is_debug)
        else:
            output(title, story, is_desc=True, is_debug=is_debug)
    if options.info: # output as an info
        # in preparation
        pass

    return True


def options_parsed():
    '''Get and setting a commandline option.

    Returns:
        :obj:`ArgumentParser`: contain commandline options.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--action', help="display with action data", action='store_false')
    parser.add_argument('-b', '--build', help="build and output a file", action='store_false')
    parser.add_argument('-d', '--descoff', help="off display the description", action='store_false')
    parser.add_argument('-i', '--info', help="display with informations", action='store_false')

    # get result
    args = parser.parse_args()

    return (args)


def story_strings_as_actions(story: Story, is_debug: bool=False):
    '''Action strings to build.

    Args:
        story (:obj:`Story`): a story object.
        is_debug (bool, optional): if True, with a debug mode.
    Returns:
        action strings converted from story objects.
    '''
    tmp = []

    tmp.append(_story_title_of(story))
    for episode in story.data:
        tmp.append(_episode_title_of(episode))
        for scene in episode.data:
            tmp.append(_scene_title_of(scene))
            for a in scene.data:
                tmp.append(_action_string_builded_with_type(a, is_debug))
    return tmp


def story_strings_as_descriptions(story: Story, is_debug: bool=False):
    '''Description strings to build.

    Returns:
        description strings converted from story objects.
    '''
    tmp = []

    tmp.append(_story_title_of(story))
    for episode in story.data:
        tmp.append(_episode_title_of(episode))
        for scene in episode.data:
            tmp.append(_scene_title_of(scene))
            for a in scene.data:
                tmp.append(_description_builded_with_type(a, is_debug))
    return tmp


def story_strings_as_infos(story: Story, is_debug: bool=False):
    '''Information strings build.

    Todo: in preparation
    '''
    tmp = []
    return tmp


def output(story: Story, is_desc: bool=False, is_debug: bool=False):
    '''Output story to the console.

    Args:
        story (:tuple:obj:`Act`): a story object.
        is_desc (bool, optional): if True, as a description.
        is_debug (bool, optional): if True, use a debug mode.
    Returns:
        True if complete, otherwise False.
    '''
    strs = story_strings_as_descriptions(story, is_debug) if is_desc else story_strings_as_actions(story, is_debug)
    for p in strs:
        print(p, end="")

    return True


def output_md(story: Story, filename: str='story', build_dir: str='build', is_desc: bool=False, is_debug: bool=False):
    '''Output story as a markdown file.

    Args:
        story (:tuple:obj:`Act`): the story object.
        filename (str, optional): a file name.
        build_dir (str, optional): a build directory path.
        is_desc (bool, optional): if True, as a description.
        is_debug (bool, optional)
    Returns:
        True if compelete, otherwise False
    '''
    EXT_MARKDOWN = 'md'

    # check build dir. it created if not exists.
    if not os.path.isdir(build_dir):
        os.makedirs(build_dir) # create build dir
    # create file
    filefullpath = os.path.join(build_dir, "{}.{}".format(filename if is_desc else "{}_a".format(filename), EXT_MARKDOWN))
    strs = story_strings_as_descriptions(story, is_debug) if is_desc else story_strings_as_actions(story, is_debug)
    with open(filefullpath, 'w') as f:
        for s in strs:
            f.write(s)

    return True


def _action_string_builded_with_type(act: Act, is_debug: bool):
    '''Action string build.
    '''
    if act.act_type == ActType.SYMBOL:
        return "**{}**\n".format(_action_string_builded(act))
    elif act.act_type in (ActType.ACT, ActType.DESC, ActType.THINK):
        return "{}\n".format(_action_string_builded(act))
    elif act.act_type == ActType.TELL:
        return "{}\n".format(_action_string_builded(act))
    elif act.act_type == ActType.TEST:
        return "> TEST: {}\n".format(_action_string_builded(act)) if is_debug else ""
    else:
        assert False, "Unknown type of an action!"
        return ""


def _action_string_builded(act: Act):
    '''Action string builder for a display.
    Args:
        :obj:`Act`: an action object.
    Returns:
        str: action info string.
    '''
    return "{} - {}: {}".format(act.subject.name, act.act_word,
            "「{}」".format(act.title) if act.act_type == ActType.TELL else act.title)


def _description_builded_with_type(act: Act, is_debug: bool):
    '''Description build.
    '''
    if act.act_type == ActType.SYMBOL:
        return "**{}**\n".format(_description_builded(act))
    elif act.act_type in (ActType.ACT, ActType.DESC, ActType.THINK):
        return "{}\n".format(_description_builded(act))
    elif act.act_type == ActType.TELL:
        return "{}\n".format(_description_builded(act))
    elif act.act_type == ActType.TEST:
        return "> TEST: {}\n".format(_description_builded(act)) if is_debug else ""
    else:
        assert False, "Unknown type of an action!"
        return ""


def _description_builded(act: Act):
    '''Description string build.
    '''
    tmp = []
    for d in act.data:
        tmp.append(d.description)
    if act.act_type == ActType.SYMBOL:
        return " - ".join(tmp)
    return "「{}」".format("、".join(tmp)) if act.act_type == ActType.TELL else "{}。".format("、".join(tmp))


def _story_title_of(story: Story):
    '''Story title.
    '''
    return "{}\n===\n".format(story.title)


def _episode_title_of(episode: Episode):
    '''Episode title.
    '''
    return "\n## {}\n\n".format(episode.title)


def _scene_title_of(scene: Scene):
    '''Scene title.
    '''
    return "\n### {}\n\n".format(scene.title)
