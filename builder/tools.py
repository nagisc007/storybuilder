# -*- coding: utf-8 -*-
"""Utility tools for story building
"""

import sys
import os

from .base import ActType, Act, Must, Done, Title, Description
from .base import Person, Stage, Item, DayTime


def build_output_strings(story, is_debug=False):
    '''Output strings to build.
    '''
    output_str = []
    
    for s in story:
        # Symbol
        if s.act_type is ActType.SYMBOL:
            output_str.append("## {}\n".format(s.action))
        elif s.act_type is ActType.DESC:
            output_str.append("{}\n".format(s.action))
        elif s.act_type is ActType.ACT:
            output_str.append("{}\n".format(s.action))
        elif s.act_type is ActType.TELL:
            output_str.append("「{}」\n".format(s.action))
        elif s.act_type is ActType.THINK:
            output_str.append("{}\n".format(s.action))
        elif s.act_type is ActType.TEST and is_debug:
            output_str.append("> TEST:{}\n".format(s.action))
        elif s.act_type is ActType.MUST and is_debug:
            output_str.append("> MUST:{}\n".format(s.action))
        elif s.act_type is ActType.DONE and is_debug:
            output_str.append("> DONE:{}\n".format(s.action))
        else:
            pass

    return output_str


def output(story, is_debug=False):
    '''Output story to the console.
    '''
    strs = build_output_strings(story, is_debug)
    for p in strs:
        print(p)


def output_md(story, filename='story', build_dir='build', is_debug=False):
    '''Output story as a markdown file.
    '''
    EXT_MARKDOWN = 'md'

    # check build dir. it created if not exists.
    if not os.path.isdir(build_dir):
        os.makedirs(build_dir) # create build dir
    # create file
    filefullpath = os.path.join(build_dir, "{}.{}".format(filename, EXT_MARKDOWN))
    strs = build_output_strings(story, is_debug)
    with open(filefullpath, 'w') as f:
        for s in strs:
            f.write(s)


