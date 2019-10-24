# -*- coding: utf-8 -*-
"""The parser.
"""
from . import assertion
from .action import Action, ActType
from .story import Story
from .chapter import Chapter
from .episode import Episode
from .scene import Scene, ScenarioType
from .action import Action, ActType
from .who import Who
from .description import Description, DescType, NoDesc
from .basesubject import NoSubject
from .strutils import str_replaced_tag_by_dictionary, str_duplicated_chopped, extraspace_chopped
from .combaction import CombAction


# publics
def outlines_from(story: Story):
    tmp = [("# " + story.title, "\n")]
    for a in story.chapters:
        res = _outlines_in_chapter(a)
        if res:
            tmp.extend(res)
    return tmp

def scenarios_from(story: Story):
    tmp = [("# " + story.title, "\n")]
    for a in story.chapters:
        res = _scenario_in_chapter(a)
        if res:
            tmp.extend(res)
    return tmp

def descriptions_from(story: Story):
    tmp = ["# " + story.title + "\n"]
    for a in story.chapters:
        res = _desc_in_chapter(a)
        if res:
            tmp.extend(res)
    return tmp

def description_connected(story: Story):
    tmp = []
    for v in story.chapters:
        tmp.append(_desc_connected_in_chapter(v))
    return story.inherited(*tmp)

def story_filtered_by_priority(story: Story, pri_filter: int):
    tmp = []
    for v in story.chapters:
        tmp.append(_story_chapter_filtered(v, pri_filter))
    return story.inherited(*tmp)

def story_pronoun_replaced(story: Story):
    tmp = []
    for v in story.chapters:
        tmp.append(_story_pronoun_replaced_in_chapter(v))
    return story.inherited(*tmp)

def story_tag_replaced(story: Story, words: dict):
    tmp = []
    for v in story.chapters:
        tmp.append(_story_tag_replaced_in_chapter(v, words))
    return story.inherited(*tmp)


# privates
def _outlines_in_chapter(chapter: Chapter):
    tmp = [("## " + chapter.title, "\n")]
    for a in chapter.episodes:
        res = _outlines_in_episode(a)
        if res:
            tmp.extend(res)
    return tmp

def _outlines_in_episode(episode: Episode):
    tmp = []
    if episode.outline:
        tmp.append(("\n### " + episode.title, episode.outline + "\n"))
    else:
        tmp.append(("\n### " + episode.title, "\n"))
    for a in episode.scenes:
        if a.outline:
            tmp.append(("- " + a.title, a.outline))
    return tmp

def _scenario_in_chapter(chapter: Chapter):
    tmp = [(ScenarioType.TITLE, "## " + chapter.title + "\n")]
    for a in chapter.episodes:
        res =_scenario_in_episode(a)
        if res:
            tmp.extend(res)
    return tmp

def _scenario_in_episode(episode: Episode):
    tmp = [(ScenarioType.TITLE, "\n### " + episode.title + "\n")]
    for a in episode.scenes:
        res = _scenario_in_scene(a)
        if res:
            tmp.extend(res)
    return tmp

def _scenario_in_scene(scene: Scene):
    tmp = [(ScenarioType.TITLE, "\n**" + scene.title + "**\n")]
    tmp.append((ScenarioType.PILLAR, "◯{}".format(scene.stage.name)))
    for a in scene.actions:
        if isinstance(a, CombAction):
            res = _scenario_in_scene_comaction(a)
            if res:
                tmp.extend(res)
        elif a.act_type is ActType.TALK:
            tmp.append((ScenarioType.DIALOGUE,
                "{}「{}」".format(a.subject.name,
                    str_duplicated_chopped(a.outline))))
        else:
            tmp.append((ScenarioType.DIRECTION,
                str_duplicated_chopped(a.outline + "。")))
    return tmp

def _scenario_in_scene_comaction(act: CombAction):
    tmp = []
    for v in act.actions:
        if v.act_type is ActType.TALK:
            tmp.append((ScenarioType.DIALOGUE,
                "{}「{}」".format(v.subject.name,
                    str_duplicated_chopped(v.outline))))
        else:
            tmp.append((ScenarioType.DIRECTION,
                str_duplicated_chopped(v.outline + "。")))
    return tmp

def _desc_in_chapter(chapter: Chapter):
    tmp = ["## " + chapter.title + "\n"]
    for a in chapter.episodes:
        res = _desc_in_episode(a)
        if res:
            tmp.extend(res)
    return tmp

def _desc_in_episode(episode: Episode):
    tmp = ["\n### " + episode.title + "\n"]
    for a in episode.scenes:
        res = _desc_in_scene(a)
        if res:
            tmp.extend(res)
    return tmp

def _desc_in_scene(scene: Scene):
    tmp = ["\n**" + scene.title + "**\n"]
    # TODO: 時間帯の表示
    for a in scene.actions:
        if isinstance(a, CombAction):
            res = _desc_in_scene_combaction(a)
            if res:
                tmp.append(res)
        elif isinstance(a.description, NoDesc):
            continue
        elif isinstance(a.description, Description):
            if a.description.desc_type is DescType.DIALOGUE:
                tmp.append(str_duplicated_chopped(
                    "「" + "".join(v for v in a.description.descs) + "」"))
            elif a.description.desc_type is DescType.COMPLEX:
                tmp.append("".join(v for v in a.description.descs))
            else:
                tmp.append(str_duplicated_chopped(
                    "　" + "".join(v for v in a.description.descs) + "。"))
    return tmp

def _desc_in_scene_combaction(act: CombAction):
    tmp = []
    for v in act.actions:
        if isinstance(v.description, NoDesc):
            continue
        if isinstance(v.description, Description):
            if v.description.desc_type is DescType.DIALOGUE:
                tmp.append(str_duplicated_chopped(
                    "「" + "".join(x for x in v.description.descs) + "」"))
            elif v.description.desc_type is DescType.COMPLEX:
                tmp.append("".join(x for x in v.description.descs))
            else:
                tmp.append(str_duplicated_chopped(
                    "　" + "".join(x for x in v.description.descs) + "。"))
    return extraspace_chopped("".join(tmp))

def _desc_connected_in_chapter(chapter: Chapter):
    tmp = []
    for v in chapter.episodes:
        tmp.append(_desc_connected_in_episode(v))
    return chapter.inherited(*tmp)

def _desc_connected_in_episode(episode: Episode):
    tmp = []
    for v in episode.scenes:
        tmp.append(_desc_connected_in_scene(v))
    return episode.inherited(*tmp)

def _desc_connected_in_scene(scene: Scene):
    tmp = []
    for a in scene.actions:
        if isinstance(a, CombAction):
            tmp.append(_desc_connected_in_scene_combaction(a))
        elif isinstance(a.description, NoDesc):
            tmp.append(a)
        else:
            tmp.append(a.inherited(desc=str_duplicated_chopped(
                "。".join(a.description.descs))))
    return scene.inherited(*tmp)

def _desc_connected_in_scene_combaction(act: CombAction):
    tmp = []
    for v in act.actions:
        if isinstance(v.description, NoDesc):
            tmp.append(v)
        else:
            tmp.append(v.inherited(desc=str_duplicated_chopped(
                "。".join(v.description.descs))))
    return CombAction(*tmp)

def _story_chapter_filtered(chapter: Chapter, pri_filter: int):
    tmp = []
    for v in chapter.episodes:
        if v.priority >= pri_filter:
            tmp.append(_story_episode_filtered(v, pri_filter))
    return chapter.inherited(*tmp)

def _story_episode_filtered(episode: Episode, pri_filter: int):
    tmp = []
    for v in episode.scenes:
        if v.priority >= pri_filter:
            tmp.append(_story_scene_filtered(v, pri_filter))
    return episode.inherited(*tmp)

def _story_scene_filtered(scene: Scene, pri_filter: int):
    tmp = []
    for a in scene.actions:
        if isinstance(a, CombAction):
            tmp.append(_story_scene_filtered_combaction(a, pri_filter))
        elif a.priority >= pri_filter:
            tmp.append(a)
    return scene.inherited(*tmp)

def _story_scene_filtered_combaction(act: CombAction, pri_filter: int):
    tmp = []
    for a in act.actions:
        if a.priority >= pri_filter:
            tmp.append(a)
    return CombAction(*tmp)

def _story_pronoun_replaced_in_chapter(chapter: Chapter):
    tmp = []
    for v in chapter.episodes:
        tmp.append(_story_pronoun_replaced_in_episode(v))
    return chapter.inherited(*tmp)

def _story_pronoun_replaced_in_episode(episode: Episode):
    tmp = []
    for v in episode.scenes:
        tmp.append(_story_pronoun_replaced_in_scene(v))
    return episode.inherited(*tmp)

def _story_pronoun_replaced_in_scene(scene: Scene):
    tmp = []
    cur_sub = NoSubject()
    for a in scene.actions:
        if isinstance(a, CombAction):
            tmp_c = []
            for v in a.actions:
                if isinstance(v.subject, Who):
                    tmp_c.append(v.inherited(subject=cur_sub))
                else:
                    cur_sub = v.subject
                    tmp_c.append(v)
            tmp.append(CombAction(*tmp_c))
        elif isinstance(a.subject, Who):
            tmp.append(a.inherited(subject=cur_sub))
        else:
            cur_sub = a.subject
            tmp.append(a)
    return scene.inherited(*tmp)

def _story_tag_replaced_in_chapter(chapter: Chapter, words: dict):
    tmp = []
    for v in chapter.episodes:
        tmp.append(_story_tag_replaced_in_episode(v, words))
    return chapter.inherited(*tmp)

def _story_tag_replaced_in_episode(episode: Episode, words: dict):
    tmp = []
    for v in episode.scenes:
        tmp.append(_story_tag_replaced_in_scene(v, words))
    return episode.inherited(*tmp)

def _story_tag_replaced_in_scene(scene: Scene, words: dict):
    tmp = []
    for a in scene.actions:
        if isinstance(a, CombAction):
            tmp.append(_story_tag_replaced_in_scene_combaction(a, words))
        else:
            tmp.append(_story_tag_replaced_in_action(a, words))
    return scene.inherited(*tmp)

def _story_tag_replaced_in_scene_combaction(act: CombAction, words: dict):
    tmp = []
    for v in act.actions:
        tmp.append(_story_tag_replaced_in_action(v, words))
    return CombAction(*tmp)

def _story_tag_replaced_in_action(act: Action, words: dict):
    is_nodesc = isinstance(act.description, NoDesc)
    outline = act.outline
    desc = NoDesc() if is_nodesc else "".join(act.description.descs)
    if hasattr(act.subject, "calling"):
        outline = str_replaced_tag_by_dictionary(act.outline, act.subject.calling)
        if not is_nodesc:
            desc = str_replaced_tag_by_dictionary(desc, act.subject.calling)
    outline = str_replaced_tag_by_dictionary(outline, words)
    if not is_nodesc:
        desc = str_replaced_tag_by_dictionary(desc, words)
    if _isInvalidatedTagReplaced(outline): raise AssertionError("Cannot convert tags in:", outline)
    if not is_nodesc and _isInvalidatedTagReplaced(desc): raise AssertionError("Cannot convert tags in:", desc)
    return act.inherited(outline=outline, desc=desc)

## checker
def _isInvalidatedTagReplaced(target: str, prefix: str='$'):
    return prefix in target

