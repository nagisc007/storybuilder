# -*- coding: utf-8 -*-
"""The analyze tool.
"""
import re
from collections import Counter
from itertools import chain
import MeCab
from . import assertion
from . import world as wd
from .scene import Scene
from .episode import Episode
from .chapter import Chapter
from .combaction import CombAction
from .action import Action, ActType, TagAction, TagType
from .description import Description, DescType, NoDesc
from .flag import Flag, NoFlag, NoDeflag
from .person import Person
from .chara import Chara
from .basesubject import NoSubject


class Analyzer(object):
    """The story analyze tools.
    """
    DEF_BASEMENT = 10
    DEF_BASEROWS = 20
    DEF_BASECOLUMNS = 20

    def __init__(self):
        self.tokenizer = MeCab.Tagger()

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
                percent("Hear", ActType.HEAR),
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
        scene_num = 0
        for c in story.chapters:
            for e in c.episodes:
                for s in e.scenes:
                    total = _descs_count_in_scene(s)
                    _rows = _manupaper_count_rows_in_scene(s, columns)
                    _papers = _rows / rows
                    outline = _outline_count_in_scene(s)
                    _outrows = _outline_manupaper_count_in_scene(s, columns)
                    _outpapers = _outrows / rows
                    tmp.append(f"**{scene_num}. {s.title}**\n+ {total} [{_papers:0.3f}({_rows:0.2f}/{rows} x {columns})] / Outline {outline} [{_outpapers:0.3f}({_outrows:0.2f})]")
                    scene_num += 1
        return tmp

    def acttype_counts(self, story: wd.Story):
        return {
                ActType.ACT: _acttype_counts_in_story(story, ActType.ACT),
                ActType.BE: _acttype_counts_in_story(story, ActType.BE),
                ActType.COME: _acttype_counts_in_story(story, ActType.COME),
                ActType.GO: _acttype_counts_in_story(story, ActType.GO),
                ActType.HAVE: _acttype_counts_in_story(story, ActType.HAVE),
                ActType.HEAR: _acttype_counts_in_story(story, ActType.HEAR),
                ActType.LOOK: _acttype_counts_in_story(story, ActType.LOOK),
                ActType.MOVE: _acttype_counts_in_story(story, ActType.MOVE),
                ActType.TALK: _acttype_counts_in_story(story, ActType.TALK),
                ActType.THINK: _acttype_counts_in_story(story, ActType.THINK),
                }

    def flag_infos(self, story: wd.Story):
        allflags = list(chain.from_iterable(_flags_in_chapter(v) for v in story.chapters))
        flags = list(v for v in allflags if not v.isDeflag)
        deflags = list(v for v in allflags if v.isDeflag)
        return ["## Flag info",
                "- flags: {}".format(len(flags)),
                "- deflags: {}".format(len(deflags))] \
                + ["### Flag detail"] \
                + list("+ " + v.info for v in flags) \
                + ["### Deflag detail"] \
                + list("- " + v.info for v in deflags)

    def frequency_words(self, story: wd.Story):
        from .parser import descriptions_from
        is_comment = False
        descs = descriptions_from(story, is_comment)
        parsed = self.tokenizer.parse("\n".join(descs)).split("\n")
        tokens = (re.split('[\t,]', v) for v in parsed)
        def base_excepted(target: str):
            return target in ('EOS', '', 't', 'ー')
        verbs = []
        nouns = []
        adjectives = []
        adverbs = []
        conjuctions = []
        for v in tokens:
            if base_excepted(v[0]):
                continue
            elif len(v) == 1:
                continue
            elif v[1] == '名詞':
                nouns.append(v[0])
            elif v[1] == '動詞':
                verbs.append(v[0])
            elif v[1] == '形容詞':
                adjectives.append(v[0])
            elif v[1] == '副詞':
                adverbs.append(v[0])
            elif v[1] == '接続詞':
                conjuctions.append(v[0])
        noun_counter = Counter(nouns)
        verb_counter = Counter(verbs)
        adject_counter = Counter(adjectives)
        adverb_counter = Counter(adverbs)
        conjuct_counter = Counter(conjuctions)
        def _as_one_counts(counter: Counter):
            return ["others: " + ",".join([word for word, count in counter.most_common() if count == 1])]
        def _wordslist(counter: Counter):
            return [f"{word}: {count}" for word, count in counter.most_common() if count > 1]
        return ["## Frequency words"] \
                + ["\n### 名詞\n"] + [f"{word}: {count}" for word, count in noun_counter.most_common() if not "#" in word and not "*" in word and count > 1] \
                + _as_one_counts(noun_counter) \
                + ["\n### 動詞\n"] + _wordslist(verb_counter) \
                + _as_one_counts(verb_counter) \
                + ["\n### 形容詞\n"] + _wordslist(adject_counter) \
                + _as_one_counts(adject_counter) \
                + ["\n### 副詞\n"] + _wordslist(adverb_counter) \
                + _as_one_counts(adverb_counter) \
                + ["\n### 接続詞\n"] + _wordslist(conjuct_counter) \
                + _as_one_counts(conjuct_counter)

    def dialogue_infos(self, story: wd.Story):
        charalist = list(set(list(chain.from_iterable(_characters_in_chapter(v) for v in story.chapters))))
        dial_counts = self._dialogues_counts(story, charalist)
        each_charas = self._dialogues_by_char(story, charalist)
        return ["## Dialogue counts\n"] \
                + dial_counts \
                + ["\n## Dialogue each persons\n"] \
                + each_charas

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
            tmp[ActType.HEAR] * 2,
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

    def _dialogues_counts(self, story: wd.Story, charalist: list):
        return [f"{v.name}: {_dialogue_count_in_story(story, v)}" for v in charalist]

    def _dialogues_by_char(self, story: wd.Story, charalist):
        def _conv_list(chara: [Person, Chara, NoSubject], dialogues: list):
            return [f"{chara.name}:"] + [f"- {v}" for v in dialogues if v]
        return list(chain.from_iterable(_conv_list(v, _dialogues_bychara_in_story(story, v)) for v in charalist))

# privates (detail)
def _characters_in_chapter(chapter: Chapter):
    # TODO: need to collect none subject chara
    return chain.from_iterable(_characters_in_episode(v) for v in chapter.episodes)

def _characters_in_episode(episode: Episode):
    return chain.from_iterable(_characters_in_scene(v) for v in episode.scenes)

def _characters_in_scene(scene: Scene):
    return chain.from_iterable(_characters_in_action(v) for v in scene.actions)

def _characters_in_action(action: [Action, CombAction, TagAction]):
    def _as_combaction(act: CombAction):
        return list(chain.from_iterable(_characters_in_action(v) for v in act.actions))
    if isinstance(action, CombAction):
        return _as_combaction(action)
    elif isinstance(action, TagAction):
        return []
    else:
        return [action.subject]

def _descs_count_in_chapter(chapter: Chapter):
    return sum(_descs_count_in_episode(v) for v in chapter.episodes)

def _descs_count_in_episode(episode: Episode):
    return sum(_descs_count_in_scene(v) for v in episode.scenes)

def _descs_count_in_scene(scene: Scene):
    def _as_combaction(combact: CombAction):
        return sum(_descs_count_in_action(v) for v in combact.actions)
    return sum(_as_combaction(v) if isinstance(v, CombAction) else _descs_count_in_action(v) for v in scene.actions)

def _descs_count_in_action(action: Action):
    if isinstance(action.description, NoDesc):
        return 0
    else:
        return len("".join(action.description.descs))

def _dialogue_count_in_story(story: wd.Story, target: [Person, Chara, NoSubject]):
    return sum(_dialogue_count_in_chapter(v, target) for v in story.chapters)

def _dialogue_count_in_chapter(chapter: Chapter, target: [Person, Chara, NoSubject]):
    return sum(_dialogue_count_in_episode(v, target) for v in chapter.episodes)

def _dialogue_count_in_episode(episode: Episode, target: [Person, Chara, NoSubject]):
    return sum(_dialogue_count_in_scene(v, target) for v in episode.scenes)

def _dialogue_count_in_scene(scene: Scene, target: [Person, Chara, NoSubject]):
    return sum(_dialogue_count_in_action(v, target) for v in scene.actions)

def _dialogue_count_in_action(action: [Action, CombAction, TagAction], target: [Person, Chara, NoSubject]):
    def _as_combaction(act: CombAction, target):
        return sum(_dialogue_count_in_action(v, target) for v in act.actions)
    if isinstance(action, CombAction):
        return _as_combaction(action, target)
    elif isinstance(action, TagAction):
        return 0
    else:
        return action.act_type is ActType.TALK and action.subject is target

def _dialogues_bychara_in_story(story: wd.Story, target: [Person, Chara, NoSubject]):
    return list(chain.from_iterable(_dialogues_bychara_in_chapter(v, target) for v in story.chapters))

def _dialogues_bychara_in_chapter(chapter: Chapter, target: [Person, Chara, NoSubject]):
    return chain.from_iterable(_dialogues_bychara_in_episode(v, target) for v in chapter.episodes)

def _dialogues_bychara_in_episode(episode: Episode, target: [Person, Chara, NoSubject]):
    return chain.from_iterable(_dialogues_bychara_in_scene(v, target) for v in episode.scenes)

def _dialogues_bychara_in_scene(scene: Scene, target: [Person, Chara, NoSubject]):
    return chain.from_iterable(_dialogues_bychara_in_action(v, target) for v in scene.actions)

def _dialogues_bychara_in_action(action: [Action, CombAction, TagAction], target: [Person, Chara, NoSubject]):
    def _as_combaction(act: CombAction, target):
        return chain.from_iterable(_dialogues_bychara_in_action(v, target) for v in act.actions)
    if isinstance(action, CombAction):
        return _as_combaction(action, target)
    elif isinstance(action, TagAction):
        return []
    else:
        return ["".join(action.description.descs)] if action.act_type is ActType.TALK and action.subject is target else []

def _flags_in_chapter(chapter: Chapter):
    return chain.from_iterable(_flags_in_episode(v) for v in chapter.episodes)

def _flags_in_episode(episode: Episode):
    return chain.from_iterable(_flags_in_scene(v) for v in episode.scenes)

def _flags_in_scene(scene: Scene):
    return chain.from_iterable(_flags_in_action(v) for v in scene.actions)

def _flags_in_action(action: [Action, CombAction]):
    def _is_flag_or_deflag(flag: [Flag, NoFlag, NoDeflag]):
        return not isinstance(flag, (NoFlag, NoDeflag)) or not isinstance(flag, (NoFlag, NoDeflag))
    if isinstance(action, Action):
        return [v for v in (action.getFlag(), action.getDeflag()) if _is_flag_or_deflag(v)]
    elif isinstance(action, CombAction):
        return chain.from_iterable(_flags_in_action(v) for v in action.actions)
    else:
        return []

def _outline_count_in_chapter(chapter: Chapter):
    return sum(_outline_count_in_episode(x) for x in chapter.episodes)

def _outline_count_in_episode(episode: Episode):
    return sum(_outline_count_in_scene(x) for x in episode.scenes)

def _outline_count_in_scene(scene: Scene):
    def _as_combaction(act: CombAction):
        return sum(len(v.outline) for v in act.actions)
    return sum(_as_combaction(v) if isinstance(v, CombAction) else len(v.outline) for v in scene.actions)

def _outline_manupapers_count(story: wd.Story, rows: int, columns: int):
    _rows = sum(_outline_manupaper_count_in_chapter(x, columns) for x in story.chapters)
    _papers = _rows / rows
    return f"{_papers:0.3f} ({_rows:0.2f}/{rows} x {columns})"

def _outline_manupaper_count_in_chapter(chapter: Chapter, columns: int):
    return sum(_outline_manupaper_count_in_episode(x, columns) for x in chapter.episodes)

def _outline_manupaper_count_in_episode(episode: Episode, columns: int):
    return sum(_outline_manupaper_count_in_scene(x, columns) for x in episode.scenes)

def _outline_manupaper_count_in_scene(scene: Scene, columns: int):
    def _as_combaction(act: CombAction):
        return sum(int_ceiled(len(v.outline), columns) for v in act.actions)
    # NOTE: +2 is title pillar
    return sum(_as_combaction(v) if isinstance(v, CombAction) else int_ceiled(len(v.outline), columns) for v in scene.actions) + 2

def _acttype_counts_in_story(story: wd.Story, act_type: ActType):
    return sum(_acttype_counts_in_chapter(v, act_type) for v in story.chapters)

def _acttype_counts_in_chapter(chapter: Chapter, act_type: ActType):
    return sum(_acttype_counts_in_episode(v, act_type) for v in chapter.episodes)

def _acttype_counts_in_episode(episode: Episode, act_type: ActType):
    return sum(_acttype_counts_in_scene(v, act_type) for v in episode.scenes)

def _acttype_counts_in_scene(scene: Scene, act_type: ActType):
    def _as_combaction(act: CombAction, act_type: ActType):
        return sum(1 for v in act.actions if v.act_type is act_type)
    def _as_single_action(act: Action, act_type: ActType):
        return act.act_type is act_type
    return sum(_as_combaction(v, act_type) if isinstance(v, CombAction) else _as_single_action(v, act_type) for v in scene.actions)

def _manupapers_count(story: wd.Story, rows: int, columns: int):
    _rows = _manupaper_count_rows_in_story(story, columns)
    _papers = _rows / rows
    return f"{_papers:0.3f} ({_rows:0.2f}/{rows} x {columns})"

def _manupaper_count_rows_in_story(story: wd.Story, columns):
    return sum(_manupaper_count_rows_in_chapter(v, columns) for v in story.chapters)

def _manupaper_count_rows_in_chapter(chapter: Chapter, columns: int):
    return sum(_manupaper_count_rows_in_episode(v, columns) for v in chapter.episodes)

def _manupaper_count_rows_in_episode(episode: Episode, columns: int):
    return sum(_manupaper_count_rows_in_scene(v, columns) for v in episode.scenes)

def _manupaper_count_rows_in_scene(scene: Scene, columns: int):
    def _desc_count(act: Action, columns: int):
        return int_ceiled(len("".join(act.description.descs)), columns)
    def _as_combaction(act: CombAction, columns: int):
        return sum(_desc_count(v, columns) for v in act.actions)
    return sum(_as_combaction(v, columns) if isinstance(v, CombAction) else _desc_count(v, columns) for v in scene.actions)


# math utility
def int_ceiled(a: [int, float], b: [int, float]) -> int:
    return -(-a // b)
