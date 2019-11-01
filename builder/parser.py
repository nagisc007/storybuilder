# -*- coding: utf-8 -*-
"""The parser.
"""
from itertools import chain
from . import assertion
from .action import Action, ActType
from .story import Story
from .chapter import Chapter
from .episode import Episode
from .scene import Scene, ScenarioType
from .action import Action, ActType, TagAction, TagType
from .who import Who
from .description import Description, DescType, NoDesc
from .basesubject import NoSubject
from .strutils import str_replaced_tag_by_dictionary, str_duplicated_chopped, extraspace_chopped, duplicate_bracket_chop_and_replaceed
from .combaction import CombAction


# publics
def outlines_from(story: Story):
    return [("# " + story.title, "\n")] \
            + list(chain.from_iterable(_outlines_in_chapter(v) for v in story.chapters))

def scenarios_from(story: Story):
    return [("# " + story.title, "\n")] \
            + list(chain.from_iterable(_scenario_in_chapter(v) for v in story.chapters))

def descriptions_from(story: Story, is_comment: bool):
    return ["# " + story.title + "\n"] \
            + list(chain.from_iterable(_desc_in_chapter(v, is_comment) for v in story.chapters))

def description_connected(story: Story):
    return story.inherited(*[_desc_connected_in_chapter(v) for v in story.chapters])

def story_filtered_by_priority(story: Story, pri_filter: int):
    return story.inherited(*[_story_chapter_filtered(v, pri_filter) for v in story.chapters])

def story_pronoun_replaced(story: Story):
    return story.inherited(*[_story_pronoun_replaced_in_chapter(v) for v in story.chapters])

def story_tag_replaced(story: Story, words: dict):
    return story.inherited(*[_story_tag_replaced_in_chapter(v, words) for v in story.chapters])


# privates
def _outlines_in_chapter(chapter: Chapter):
    return [("## " + chapter.title, "\n")] \
            + list(chain.from_iterable(_outlines_in_episode(v) for v in chapter.episodes))

def _outlines_in_episode(episode: Episode):
    def _title_outline(scene: Scene):
        return [("- " + scene.title, scene.outline)]
    return [("\n### " + episode.title, episode.outline + "\n")] \
            + list(chain.from_iterable(_title_outline(v) for v in episode.scenes))

def _scenario_in_chapter(chapter: Chapter):
    return [(ScenarioType.TITLE, "## " + chapter.title + "\n")] \
            + list(chain.from_iterable(_scenario_in_episode(v) for v in chapter.episodes))

def _scenario_in_episode(episode: Episode):
    return [(ScenarioType.TITLE, "\n### " + episode.title + "\n")] \
            + list(chain.from_iterable(_scenario_in_scene(v) for v in episode.scenes))

def _scenario_in_scene(scene: Scene):
    # TODO: 時間帯の表示
    return [(ScenarioType.TITLE, f"\n**{scene.title}**\n")] \
            + [(ScenarioType.PILLAR, f"◯{scene.stage.name}")] \
            + list(chain.from_iterable(_scenario_in_action(v) for v in scene.actions))

def _scenario_in_action(action: [Action, CombAction, TagAction]):
    def _as_combaction(act: CombAction):
        return list(chain.from_iterable(_scenario_in_action(v) for v in act.actions))
    if isinstance(action, CombAction):
        return _as_combaction(action)
    elif action.act_type is ActType.TALK:
        return [(ScenarioType.DIALOGUE,
                f"{action.subject.name}「{str_duplicated_chopped(action.outline)}」")]
    else:
        return [(ScenarioType.DIRECTION,
            str_duplicated_chopped(f"{action.outline}。"))]

def _desc_in_chapter(chapter: Chapter, is_comment: bool):
    return ["##" + chapter.title + "\n"] \
            + list(chain.from_iterable(_desc_in_episode(v, is_comment) for v in chapter.episodes))

def _desc_in_episode(episode: Episode, is_comment: bool):
    return ["\n### " + episode.title + "\n"] \
            + list(chain.from_iterable(_desc_in_scene(v, is_comment) for v in episode.scenes))

def _desc_in_scene(scene: Scene, is_comment: bool):
    return ["\n**" + scene.title + "**\n"] \
            + list(chain.from_iterable(_desc_in_action(v, is_comment) for v in scene.actions))

def _desc_in_action(action: [Action, CombAction], is_comment: bool):
    if isinstance(action, TagAction):
        # TODO: 処理を切り離す
        if action.tag_type is TagType.COMMENT and is_comment:
            return [f"<!--{action.info}-->"]
        elif action.tag_type is TagType.BR:
            return ["\n\n"]
        elif action.tag_type is TagType.HR:
            return ["----" * 8]
        elif action.tag_type is TagType.SYMBOL:
            return [f"\n{action.info}\n"]
        elif action.tag_type is TagType.TITLE:
            num = int(action.subinfo)
            return ["{} {}".format("#" * num, action.info)]
        else:
            return []
    elif isinstance(action, Action):
        if isinstance(action.description, NoDesc):
            return []
        else:
            if action.description.desc_type is DescType.DIALOGUE:
                return [str_duplicated_chopped("「" + "".join(x for x in action.description.descs) + "」")]
            elif action.description.desc_type is DescType.COMPLEX:
                return ["".join(x for x in action.description.descs)]
            else:
                return [str_duplicated_chopped("　" + "".join(x for x in action.description.descs) + "。")]
        return []
    elif isinstance(action, CombAction):
        return [duplicate_bracket_chop_and_replaceed(extraspace_chopped("".join(chain.from_iterable(_desc_in_action(x, is_comment) for x in action.actions))))]
    else:
        return []

def _desc_connected_in_chapter(chapter: Chapter):
    return chapter.inherited(*[_desc_connected_in_episode(v) for v in chapter.episodes])

def _desc_connected_in_episode(episode: Episode):
    return episode.inherited(*[_desc_connected_in_scene(v) for v in episode.scenes])

def _desc_connected_in_scene(scene: Scene):
    return scene.inherited(*[_desc_connected_in_action(v) for v in scene.actions])

def _desc_connected_in_action(action: [Action, CombAction, TagAction]):
    def _as_combaction(act: CombAction):
        return act.inherited(*[_desc_connected_in_action(v) for v in act.actions])
    if isinstance(action, CombAction):
        return _as_combaction(action)
    elif isinstance(action, TagAction):
        return action
    elif isinstance(action.description, NoDesc):
        return action
    else:
        return action.inherited(desc=str_duplicated_chopped("。".join(action.description.descs)))

def _story_chapter_filtered(chapter: Chapter, pri_filter: int):
    # TODO: chapter priority
    return chapter.inherited(*[_story_episode_filtered(v, pri_filter) for v in chapter.episodes])

def _story_episode_filtered(episode: Episode, pri_filter: int):
    # TODO: episode priority
    return episode.inherited(*[_story_scene_filtered(v, pri_filter) for v in episode.scenes])

def _story_scene_filtered(scene: Scene, pri_filter: int):
    tmp = []
    def _as_combaction(act: CombAction, pri: int):
        return act.inherited(*[v for v in act.actions if v.priority >= pri])
    for v in scene.actions:
        if isinstance(v, CombAction):
            tmp.append(_as_combaction(v, pri_filter))
        elif v.priority >= pri_filter:
            tmp.append(v)
    return scene.inherited(*tmp)

def _story_pronoun_replaced_in_chapter(chapter: Chapter):
    return chapter.inherited(*[_story_pronoun_replaced_in_episode(v) for v in chapter.episodes])

def _story_pronoun_replaced_in_episode(episode: Episode):
    return episode.inherited(*[_story_pronoun_replaced_in_scene(v) for v in episode.scenes])

def _story_pronoun_replaced_in_scene(scene: Scene):
    tmp = []
    cur_sub = NoSubject()
    for a in scene.actions:
        if isinstance(a, CombAction):
            tmp_c = []
            for v in a.actions:
                if isinstance(v, TagAction):
                    tmp_c.append(v)
                elif isinstance(v.subject, Who):
                    tmp_c.append(v.inherited(subject=cur_sub))
                else:
                    cur_sub = v.subject
                    tmp_c.append(v)
            tmp.append(a.inherited(*tmp_c))
        elif isinstance(a, TagAction):
            tmp.append(a)
        elif isinstance(a.subject, Who):
            tmp.append(a.inherited(subject=cur_sub))
        else:
            cur_sub = a.subject
            tmp.append(a)
    return scene.inherited(*tmp)

def _story_tag_replaced_in_chapter(chapter: Chapter, words: dict):
    return chapter.inherited(*[_story_tag_replaced_in_episode(v, words) for v in chapter.episodes])

def _story_tag_replaced_in_episode(episode: Episode, words: dict):
    return episode.inherited(*[_story_tag_replaced_in_scene(v, words) for v in episode.scenes])

def _story_tag_replaced_in_scene(scene: Scene, words: dict):
    def _as_combaction(act: CombAction, words: dict):
        return act.inherited(*[_story_tag_replaced_in_action(v, words) for v in act.actions])
    return scene.inherited(*[_as_combaction(v, words) if isinstance(v, CombAction) else _story_tag_replaced_in_action(v, words) for v in scene.actions])

def _story_tag_replaced_in_action(act: [Action, TagAction], words: dict):
    if isinstance(act, TagAction):
        return act
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

