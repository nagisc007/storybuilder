# -*- coding: utf-8 -*-
"""The build tool.
"""
from __future__ import print_function
import os
import argparse
import re
from . import assertion
from . import world as wd
from .parser import outlines_from, scenarios_from, descriptions_from, story_filtered_by_priority, story_pronoun_replaced, description_connected, story_tag_replaced
from .strutils import dict_sorted
from .analyzer import Analyzer


class Build(object):
    """The story build tools.
    """
    DEF_FILENAME = "story"
    DEF_EXTENSION = "md" # NOTE: currently markdown only
    DEF_BUILD_DIR = "build"

    def __init__(self, story: wd.Story, world: wd.World):
        self._story = Build._validatedStory(story)
        self._words = Build._wordsFrom(world)
        self._filename = Build.DEF_FILENAME
        self._options = _options_parsed()
        self._extension = Build.DEF_EXTENSION
        self._builddir = Build.DEF_BUILD_DIR
        # TODO: build dir を指定（変更）できるように

    # methods
    def output_story(self):
        is_succeeded = True
        options = self._options
        filename = self._filename # TODO: ファイル名指定できるようにする
        pri_filter = options.priority # TODO: priority指定できるようにする
        formattype = options.format
        is_debug = options.debug # NOTE: 現在デバッグモードはコンソール出力のみ
        is_comment = options.comment # NOTE: コメント付き出力

        ''' NOTE: converted story content
                1) prioriy filter
                2) pronoun replaced
                3) description connected
                4) tag replaced
        '''
        story_converted = story_tag_replaced(
                    description_connected(
                    story_pronoun_replaced(
                    story_filtered_by_priority(self._story, pri_filter)
                )), self._words)

        analyzer = Analyzer()

        if options.outline:
            is_succeeded = self.to_outline(story_converted, filename, is_debug)
            if not is_succeeded:
                print("ERROR: output a outline failed!!")
                return is_succeeded

        if options.scenario:
            is_succeeded = self.to_scenario(story_converted, filename, is_debug)
            if not is_succeeded:
                print("ERROR: output a scenario failed!!")
                return is_succeeded

        if options.description:
            is_succeeded = self.to_description(story_converted, filename, formattype,
                    is_comment, is_debug)
            if not is_succeeded:
                print("ERROR: output a description failed!!")
                return is_succeeded

        if options.action:
            # TODO: action view output
            pass

        if options.info:
            # TODO: detail info output
            is_succeeded = self.to_detail_info(story_converted, analyzer, filename,
                    is_debug)
            if not is_succeeded:
                print("ERROR: output a detail info failed!!")
                return is_succeeded

        if options.analyze:
            # TODO: analyze documents
            is_succeeded = self.to_analyzed_info(story_converted, analyzer, filename,
                    is_debug)
            if not is_succeeded:
                print("ERROR: output an analyzed info failed!!")
                return is_succeeded

        if options.chara:
            # TODO: show character infos
            pass

        if options.dialogue:
            is_succeeded = self.to_dialogue_info(story_converted, analyzer, filename,
                    is_debug)
            if not is_succeeded:
                print("ERROR: output a dialogue info failed!!")
                return is_succeeded

        if options.version:
            # TODO: show version
            pass

        # total info (always display)
        is_succeeded = self.to_total_info(story_converted, analyzer)

        return is_succeeded

    def to_outline(self, story: wd.Story, filename: str, is_debug: bool):
        is_succeeded = True
        res = Build._outline_formatted(outlines_from(story))
        if is_debug:
            # out to console
            for v in res:
                print(v)
        else:
            is_succeeded = Build._out_to_file(res, filename, "_out", self._extension,
                    self._builddir)
        return is_succeeded

    def to_scenario(self, story: wd.Story, filename: str, is_debug: bool):
        is_succeeded = True
        res = Build._scenario_formatted(scenarios_from(story))
        if is_debug:
            # out to console
            for v in res:
                print(v)
        else:
            is_succeeded = Build._out_to_file(res, filename, "_sc", self._extension,
                    self._builddir)
        return is_succeeded

    def to_description(self, story: wd.Story, filename: str, formattype: str,
            is_comment: bool, is_debug: bool):
        is_succeeded = True
        res = Build._description_formatted(descriptions_from(story, is_comment), formattype)
        if is_debug:
            # out to console
            for v in res:
                print(v)
        else:
            is_succeeded = Build._out_to_file(res, filename, "", self._extension,
                    self._builddir)
        return is_succeeded

    def to_total_info(self, story: wd.Story, analyzer: Analyzer):
        is_succeeded = True
        charcounts = analyzer.characters_count(story)
        for v in charcounts:
            print(v)
        return is_succeeded

    def to_detail_info(self, story: wd.Story, analyzer: Analyzer, filename: str,
            is_debug: bool):
        is_succeeded = True
        # TODO: 最初にタイトルから章やシーンリスト
        # TODO: 文字数に続いて各シーンの簡易情報
        # TODO: 各分析情報
        # TODO: flag情報
        charcounts = analyzer.characters_count(story)
        scenes_characters = analyzer.characters_count_each_scenes(story)
        act_percents = analyzer.action_percent(story)
        flaginfo = analyzer.flag_infos(story)
        scene_num = ["## Scene info",
                "- scenes: {}\n".format(len(scenes_characters))]
        res = charcounts + [""] + scene_num + scenes_characters + act_percents \
                + flaginfo
        if is_debug: # out to console
            for v in res:
                print(v)
        else:
            is_succeeded = Build._out_to_file(res, filename, "_info", self._extension,
                    self._builddir)
        return is_succeeded

    def to_analyzed_info(self, story: wd.Story, analyzer: Analyzer, filename: str,
            is_debug: bool):
        is_succeeded = True
        # NOTE: 解析結果
        freq = analyzer.frequency_words(story)
        res = freq
        if is_debug:
            # out to console
            for v in res:
                print(v)
        else:
            is_succeeded = Build._out_to_file(res, filename, "_anal", self._extension,
                    self._builddir)
        return is_succeeded

    def to_dialogue_info(self, story: wd.Story, analyzer: Analyzer, filename: str,
            is_debug: bool):
        is_succeeded = True
        # NOTE: dialogue count and list
        info = analyzer.dialogue_infos(story)
        res = info
        if is_debug:
            # out to console
            for v in res:
                print(v)
        else:
            is_succeeded = Build._out_to_file(res, filename, "_dial", self._extension,
                    self._builddir)
        return is_succeeded

    # private
    def _validatedStory(story: wd.Story):
        if isinstance(story, wd.Story):
            return story
        else:
            raise AssertionError("Must be data type of 'Story'!")
        return False

    def _wordsFrom(world: wd.Word):
        '''To create the world dictionary.
        '''
        tmp = {}
        # persons and charas
        for k, v in assertion.is_instance(world, wd.World).items():
            if k in ('stage', 'day', 'time', 'item', 'word'):
                continue
            if isinstance(v, wd.Chara):
                tmp[k] = v.name
            elif isinstance(v, wd.Person):
                tmp['n_' + k] = v.name
                tmp['fn_' + k] = v.firstname
                tmp['ln_' + k] = v.lastname
                tmp['full_' + k] = v.fullname
                tmp['efull_' + k] = v.exfullname
        for k, v in world.stage.items():
            tmp['st_' + k] = v.name
        for k, v in world.item.items():
            tmp['t_' + k] = v.name
        for k, v in world.word.items():
            tmp['w_' + k] = v.name
        return dict_sorted(tmp)

    def _outline_formatted(outlines: list):
        tmp = []
        for v in outlines:
            tmp.append(v[0] + ": " + v[1])
        return tmp

    def _scenario_formatted(scenarios: list):
        from .scene import ScenarioType
        tmp = []
        for v in scenarios:
            if v[0] is ScenarioType.DIRECTION:
                tmp.append("　　" + v[1])
            else:
                tmp.append(v[1])
        return tmp

    def _description_formatted(descs: list, formattype: str):
        # TODO: format を選んで変更
        if formattype in ("estar",):
            return Build._descs_formatted_estar_style(descs)
        elif formattype in ("smartphone", "phone", "smart"):
            return Build._descs_formatted_smartphone_style(descs)
        elif formattype in ("web",):
            return Build._descs_formatted_webnovel_style(descs)
        else:
            return descs

    def _out_to_file(data: list, filename: str, suffix: str, extention: str,
            builddir: str):
        is_succeeded = True
        if not os.path.isdir(builddir):
            os.makedirs(builddir)
        fullpath = os.path.join(builddir, "{}{}.{}".format(
            assertion.is_str(filename), assertion.is_str(suffix),
            assertion.is_str(extention)
            ))
        with open(fullpath, 'w') as f:
            for v in data:
                f.write(f"{v}\n")
        return is_succeeded

    def _descs_formatted_estar_style(data: list):
        tmp = []
        inDialogue = False
        for v in assertion.is_list(data):
            current = v.startswith(('「', '『'))
            pre = "" if inDialogue == current else "\n"
            tmp.append(pre + v + "\n")
            inDialogue = current
        return tmp

    def _descs_formatted_smartphone_style(data: list):
        tmp = []
        for v in assertion.is_list(data):
            tmp.append(v + "\n")
        return tmp

    def _descs_formatted_webnovel_style(data: list) -> list:
        tmp = []
        inDialogue = False
        for v in assertion.is_list(data):
            current = v.startswith(('「', '『'))
            pre = "" if inDialogue == current else "\n"
            tmp.append(pre + v)
            inDialogue = current
        return tmp


# privates
def _options_parsed(): # pragma: no cover
    '''Get and setting a commandline option.

    Returns:
        :obj:`ArgumentParser`: contain commandline options.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--outline', help="output the outline", action='store_true')
    parser.add_argument('-s', '--scenario', help="output the scenario", action='store_true')
    parser.add_argument('-d', '--description', help="output the novel", action='store_true')
    # TODO: action view
    parser.add_argument('-a', '--action', help="output the monitoring action", action='store_true')
    parser.add_argument('-i', '--info', help="output adding the detail info", action='store_true')
    parser.add_argument('-z', '--analyze', help="output the analyzed info", action='store_true')
    # TODO: character info
    parser.add_argument('-c', '--chara', help="output characters info", action='store_true')
    parser.add_argument('-l', '--dialogue', help="output character dialogues", action='store_true')
    # TODO: help
    # TODO: version info
    parser.add_argument('-v', '--version', help="display this version", action='store_true')
    # TODO: advanced file name
    parser.add_argument('-f', '--file', help="advanced output the file name", type=str)
    # TODO: priority setting
    parser.add_argument('-p', '--priority', help="output filtered by the priority", type=int, default=wd.World.DEF_PRIORITY)
    parser.add_argument('--debug', help="with a debug mode", action='store_true')
    parser.add_argument('--format', help='output the format style', type=str)
    parser.add_argument('--comment', help='output with comment', action='store_true')

    # get result
    args = parser.parse_args()

    return (args)


