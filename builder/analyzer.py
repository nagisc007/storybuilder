# -*- coding: utf-8 -*-
"""The analyze tool.
"""
from . import assertion
from . import world as wd
from .scene import Scene
from .episode import Episode
from .chapter import Chapter
from .combaction import CombAction
from .action import Action, ActType
from .description import Description, DescType, NoDesc


class Analyzer(object):
    """The story analyze tools.
    """
    DEF_BASEMENT = 10
    DEF_BASEROWS = 20
    DEF_BASECOLUMNS = 20

    # main analyzing methods
    def action_percent(self, story):
        acttypes = self.acttype_counts(story)
        total = sum(v for v in acttypes.values())
        def percent(char, atype):
            return "- {}: {:.2f}%".format(
                    char,
                    acttypes[atype] / total * 100 if total else 0
                    )
        return ["## Actions",
                f"- Total: {total}",
                percent("Act", ActType.ACT),
                percent("Be", ActType.BE),
                percent("Come", ActType.COME),
                percent("Go", ActType.GO),
                percent("Have", ActType.HAVE),
                percent("Look", ActType.LOOK),
                percent("Move", ActType.MOVE),
                percent("Talk", ActType.TALK),
                percent("Think", ActType.THINK),
                ]

    def characters_count(self, story: wd.Story):
        # TODO: outline文字数／シナリオ用
        total = self._descs_count(story) # NOTE: 総文字数
        outline = self._outline_count(story) # NOTE: outline文字数
        estimated = self._descs_estimated_count(story) # NOTE: 予想文字数
        manupp = self._descs_manupaper_counts(story, Analyzer.DEF_BASEROWS, Analyzer.DEF_BASECOLUMNS) # NOTE: 原稿用紙換算枚数
        outlinemanupp = self._outline_manupaper_count(story, Analyzer.DEF_BASEROWS, Analyzer.DEF_BASECOLUMNS) # NOTE: outline原稿用紙換算枚数
        return [
                "## Characters",
                f"- Total: {total} / Outline: {outline}",
                f"- Estimated: {estimated}",
                f"- Manupapers: {manupp} / Outline {outlinemanupp}",
                ]

    def characters_count_each_scenes(self, story: wd.Story):
        tmp = []
        rows = Analyzer.DEF_BASEROWS
        columns = Analyzer.DEF_BASECOLUMNS
        for c in story.chapters:
            for e in c.episodes:
                for s in e.scenes:
                    total = _descs_count_in_scene(s)
                    _rows = _manupaper_count_rows_in_scene(s, columns)
                    _papers = _rows / rows
                    outline = _outline_count_in_scene(s)
                    _outrows = _outline_manupaper_count_in_scene(s, columns)
                    _outpapers = _outrows / rows
                    tmp.append(f"**{s.title}**\n+ {total} [{_papers:0.3f}({_rows:0.2f}/{rows} x {columns})] / Outline {outline} [{_outpapers:0.3f}({_outrows:0.2f})]")
        return tmp

    def acttype_counts(self, story: wd.Story):
        return {
                ActType.ACT: _acttype_counts_in_story(story, ActType.ACT),
                ActType.BE: _acttype_counts_in_story(story, ActType.BE),
                ActType.COME: _acttype_counts_in_story(story, ActType.COME),
                ActType.GO: _acttype_counts_in_story(story, ActType.GO),
                ActType.HAVE: _acttype_counts_in_story(story, ActType.HAVE),
                ActType.LOOK: _acttype_counts_in_story(story, ActType.LOOK),
                ActType.MOVE: _acttype_counts_in_story(story, ActType.MOVE),
                ActType.TALK: _acttype_counts_in_story(story, ActType.TALK),
                ActType.THINK: _acttype_counts_in_story(story, ActType.THINK),
                }

    # privates (hook)
    def _descs_count(self, story: wd.Story):
        tmp = []
        for v in story.chapters:
            tmp.append(_descs_count_in_chapter(v))
        return sum(tmp)

    def _descs_estimated_count(self, story: wd.Story, basement: int=DEF_BASEMENT):
        tmp = self.acttype_counts(story)
        return sum([
            tmp[ActType.ACT] * 4,
            tmp[ActType.BE] * 1,
            tmp[ActType.COME] * 2,
            tmp[ActType.GO] * 2,
            tmp[ActType.HAVE] * 2,
            tmp[ActType.LOOK] * 4,
            tmp[ActType.MOVE] * 2,
            tmp[ActType.TALK] * 4,
            tmp[ActType.THINK] * 4,
                ]) * basement

    def _descs_manupaper_counts(self, story: wd.Story, rows: int, columns: int):
        return _manupapers_count(story, rows, columns)

    def _outline_count(self, story: wd.Story):
        return sum(_outline_count_in_chapter(x) for x in story.chapters)

    def _outline_manupaper_count(self, story: wd.Story, rows: int, columns: int):
        return _outline_manupapers_count(story, rows, columns)

# privates (detail)
def _descs_count_in_chapter(chapter: Chapter):
    tmp = []
    for v in chapter.episodes:
        tmp.append(_descs_count_in_episode(v))
    return sum(tmp)

def _descs_count_in_episode(episode: Episode):
    tmp = []
    for v in episode.scenes:
        tmp.append(_descs_count_in_scene(v))
    return sum(tmp)

def _descs_count_in_scene(scene: Scene):
    tmp = []
    for v in scene.actions:
        if isinstance(v, CombAction):
            for c in v.actions:
                if isinstance(c.description, NoDesc):
                    tmp.append(0)
                else:
                    tmp.append(len("".join(c.description.descs)))
        elif isinstance(v.description, NoDesc):
            tmp.append(0)
        else:
            tmp.append(len("".join(v.description.descs)))
    return sum(tmp)

def _outline_count_in_chapter(chapter: Chapter):
    return sum(_outline_count_in_episode(x) for x in chapter.episodes)

def _outline_count_in_episode(episode: Episode):
    return sum(_outline_count_in_scene(x) for x in episode.scenes)

def _outline_count_in_scene(scene: Scene):
    tmp = []
    for v in scene.actions:
        if isinstance(v, CombAction):
            for c in v.actions:
                tmp.append(len(c.outline))
        else:
            tmp.append(len(v.outline))
    return sum(tmp)

def _outline_manupapers_count(story: wd.Story, rows: int, columns: int):
    _rows = sum(_outline_manupaper_count_in_chapter(x, columns) for x in story.chapters)
    _papers = _rows / rows
    return f"{_papers:0.3f} ({_rows:0.2f}/{rows} x {columns})"

def _outline_manupaper_count_in_chapter(chapter: Chapter, columns: int):
    return sum(_outline_manupaper_count_in_episode(x, columns) for x in chapter.episodes)

def _outline_manupaper_count_in_episode(episode: Episode, columns: int):
    return sum(_outline_manupaper_count_in_scene(x, columns) for x in episode.scenes)

def _outline_manupaper_count_in_scene(scene: Scene, columns: int):
    tmp = []
    tmp.append(2) # NOTE: title pillar
    for v in scene.actions:
        if isinstance(v, CombAction):
            for c in v.actions:
                tmp.append(int_ceiled(len(c.outline), columns))
        else:
            tmp.append(int_ceiled(len(v.outline), columns))
    return sum(tmp)

def _acttype_counts_in_story(story: wd.Story, act_type: ActType):
    tmp = []
    for v in story.chapters:
        tmp.append(_acttype_counts_in_chapter(v, act_type))
    return sum(tmp)

def _acttype_counts_in_chapter(chapter: Chapter, act_type: ActType):
    tmp = []
    for v in chapter.episodes:
        tmp.append(_acttype_counts_in_episode(v, act_type))
    return sum(tmp)

def _acttype_counts_in_episode(episode: Episode, act_type: ActType):
    tmp = []
    for v in episode.scenes:
        tmp.append(_acttype_counts_in_scene(v, act_type))
    return sum(tmp)

def _acttype_counts_in_scene(scene: Scene, act_type: ActType):
    tmp = []
    for v in scene.actions:
        if isinstance(v, CombAction):
            tmp.append(1)
        else:
            tmp.append(v.act_type is act_type)
    return sum(tmp)

def _manupapers_count(story: wd.Story, rows: int, columns: int):
    _rows = _manupaper_count_rows_in_story(story, columns)
    _papers = _rows / rows
    return f"{_papers:0.3f} ({_rows:0.2f}/{rows} x {columns})"

def _manupaper_count_rows_in_story(story: wd.Story, columns):
    tmp = []
    for v in story.chapters:
        tmp.append(_manupaper_count_rows_in_chapter(v, columns))
    return sum(tmp)

def _manupaper_count_rows_in_chapter(chapter: Chapter, columns: int):
    tmp = []
    for v in chapter.episodes:
        tmp.append(_manupaper_count_rows_in_episode(v, columns))
    return sum(tmp)

def _manupaper_count_rows_in_episode(episode: Episode, columns: int):
    tmp = []
    for v in episode.scenes:
        tmp.append(_manupaper_count_rows_in_scene(v, columns))
    return sum(tmp)

def _manupaper_count_rows_in_scene(scene: Scene, columns: int):
    tmp = []
    for v in scene.actions:
        if isinstance(v, CombAction):
            for c in v.actions:
                if isinstance(c.description, NoDesc):
                    continue
                else:
                    tmp.append(int_ceiled(
                        len("".join(c.description.descs)), columns))
        elif isinstance(v.description, NoDesc):
            continue
        else:
            tmp.append(int_ceiled(len("".join(v.description.descs)), columns))
    return sum(tmp)


# math utility
def int_ceiled(a: [int, float], b: [int, float]) -> int:
    return -(-a // b)
