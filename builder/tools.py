# -*- coding: utf-8 -*-
"""Utility tools for story building
"""
from __future__ import print_function
import os
import argparse

from .acttypes import ActType


def story_builded(title, story, filename='story', build_dir='build', is_debug=False):
    '''Building a story.

    Args:
        title (str): a story title.
        story (:tuple:obj:`Act`): a story objects.
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


def build_action_strings(story, is_debug=False):
    '''Action strings to build.

    Returns:
        action strings converted from story objects.
    '''
    act_str = []
    
    for s in story:
        if s.act_type is ActType.SYMBOL:
            act_str.append("\n## {}\n\n".format(s.action))
        elif s.act_type is ActType.DESC or s.act_type is ActType.ACT:
            act_str.append("{}\n".format(_action_info_builded(s)))
        elif s.act_type is ActType.TELL:
            act_str.append("{}\n".format(_action_info_builded(s)))
        elif s.act_type is ActType.THINK:
            act_str.append("{}\n".format(_action_info_builded(s)))
        elif s.act_type is ActType.TEST and is_debug:
            act_str.append("> TEST:{}\n".format(_action_info_builded(s)))
        else:
            pass

    return act_str


def build_description_strings(story, is_debug=False):
    '''Description strings to build.

    Returns:
        description strings converted from story objects.
    '''
    desc_str = []

    for s in story:
        if s.act_type is ActType.SYMBOL:
            if s.description:
                desc_str.append("\n## {} -- {}\n\n".format(s.action, s.description.description))
            else:
                desc_str.append("\n## {}\n\n".format(s.action))
        elif s.act_type is ActType.DESC or s.act_type is ActType.ACT or s.act_type is ActType.THINK:
            desc_str.append("{}。\n".format( _description_selected(s)))
        elif s.act_type is ActType.TELL:
            desc_str.append("「{}」\n".format(_description_selected(s)))
        elif s.act_type is ActType.TEST and is_debug:
            desc_str.append("> TEST:{}\n".format(_description_selected(s)))

    return desc_str


def output(title, story, is_desc=False, is_debug=False):
    '''Output story to the console.

    Args:
        title (str): a story title.
        story (:tuple:obj:`Act`): a story object.
        is_desc (bool, optional): if True, as a description.
        is_debug (bool, optional): if True, use a debug mode.
    Returns:
        True if complete, otherwise False.
    '''
    strs = build_description_strings(story, is_debug) if is_desc else build_action_strings(story, is_debug)
    print("# {}{}\n".format(title, "" if is_desc else " (as Actions)"))
    for p in strs:
        print(p, end="")

    return True


def output_md(title, story, filename='story', build_dir='build', is_desc=False, is_debug=False):
    '''Output story as a markdown file.

    Args:
        title (str): a story title.
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
    strs = build_description_strings(story, is_debug) if is_desc else build_action_strings(story, is_debug)
    with open(filefullpath, 'w') as f:
        f.write("# {}{}\n".format(title, "" if is_desc else " (as Actions)"))
        for s in strs:
            f.write(s)

    return True


def _action_info_builded(act):
    '''Action string builder for a display.
    Args:
        :obj:`Act`: an action object.
    Returns:
        str: action info string.
    '''
    return "{} - {}: {}".format(act.subject.name, act.act_word,
            "「{}」".format(act.action) if act.act_type == ActType.TELL else act.action)


def _description_selected(act):
    '''Description selector.

    Returns:
        description if the act has a description, otherwise a action.
    '''
    if act.description:
        return act.description.description
    return act.action

