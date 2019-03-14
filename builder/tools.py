# -*- coding: utf-8 -*-
"""Utility tools for story building
"""

import os

from .acttypes import ActType


def build_action_strings(story, is_debug=False):
    '''Action strings to build.

    Returns:
        action strings converted from story objects.
    '''
    act_str = []
    
    for s in story:
        if s.act_type is ActType.SYMBOL:
            act_str.append("\n## {}\n\n".format(_action_with_act_word_if_selected(s)))
        elif s.act_type is ActType.DESC or s.act_type is ActType.ACT:
            act_str.append("{}\n".format(_action_with_act_word_if_selected(s)))
        elif s.act_type is ActType.TELL:
            act_str.append("「{}」{}\n".format(s.action, s.act_word))
        elif s.act_type is ActType.THINK:
            act_str.append("{}\n".format(_action_with_act_word_if_selected(s)))
        elif s.act_type is ActType.TEST and is_debug:
            act_str.append("> TEST:{}\n".format(_action_with_act_word_if_selected(s)))
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
                desc_str.append("\n## {} -- {}\n\n".format(s.action, s.description))
            else:
                desc_str.append("\n## {}\n\n".format(s.action))
        elif s.act_type is ActType.DESC or s.act_type is ActType.ACT or s.act_type is ActType.THINK:
            desc_str.append("{}。\n".format( _description_selected(s)))
        elif s.act_type is ActType.TELL:
            desc_str.append("「{}」\n".format(_description_selected(s)))
        elif s.act_type is ActType.TEST and is_debug:
            desc_str.append("> TEST:{}\n".format(_description_selected(s)))

    return desc_str


def output(story, is_desc=False, is_debug=False):
    '''Output story to the console.

    Returns:
        True if complete, otherwise False.
    '''
    strs = build_description_strings(story, is_debug) if is_desc else build_action_strings(story, is_debug)
    for p in strs:
        print(p)

    return True


def output_md(story, filename='story', build_dir='build', is_desc=False, is_debug=False):
    '''Output story as a markdown file.

    Returns:
        True if compelete, otherwise False
    '''
    EXT_MARKDOWN = 'md'

    # check build dir. it created if not exists.
    if not os.path.isdir(build_dir):
        os.makedirs(build_dir) # create build dir
    # create file
    filefullpath = os.path.join(build_dir, "{}.{}".format(filename, EXT_MARKDOWN))
    strs = build_description_strings(story, is_debug) if is_desc else build_action_strings(story, is_debug)
    with open(filefullpath, 'w') as f:
        for s in strs:
            f.write(s)

    return True


def _description_selected(act):
    '''Description selector.

    Returns:
        description if the act has a description, otherwise a action.
    '''
    if act.description:
        return act.description
    return act.action


def _action_with_act_word_if_selected(act):
    '''Action string created with selecting act word.

    Returns:
        str: action string.
    '''
    return "{}{}".format(act.action, act.act_word) if act.with_act else act.action

