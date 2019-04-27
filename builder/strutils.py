# -*- coding: utf-8 -*-
"""String utilities.
"""
import re
from . import assertion as ast
from . import enums as em


# public methods
def comma_by(lang: em.LangType) -> str:
    return "、" if lang is em.LangType.JPN else ", "


def comment_tag_from(target: str) -> str:
    return "<!--{}-->".format(ast.is_str(target))


def description_from(target: str, lang: em.LangType) -> str:
    return period_added_if_none(target, lang)


def dialogue_from(target: str, lang: em.LangType) -> str:
    return f'「{target}」' if lang is em.LangType.JPN else f'"{target}"'


def double_comma_chopped(target: str, lang: em.LangType=em.LangType.JPN) -> str:
    '''Single symbol from double

        、、｜。。 → 、｜。
    '''
    if ast.is_instance(lang, em.LangType) is em.LangType.JPN:
        return re.sub(r'(。)+', r'\1',
                re.sub(r'(、)+', r'\1', ast.is_str(target)))
    else:
        return re.sub(r'(\.)+', r'\1',
                re.sub(r'(,|\.)+', r'\1', ast.is_str(target)))


def em_tag_from(target: str, lv: int=1) -> str:
    tag = "***" if lv >= 3 else ("**" if lv == 2 else "_")
    return "{tag}{target}{tag}".format(tag=tag, target=ast.is_str(target))


def extraend_chopped(target: str, lang: em.LangType) -> str:
    '''Symbol mark with invalid endmark chopped
    '''
    if ast.is_instance(lang, em.LangType) is em.LangType.JPN:
        return re.sub(r'([！？])。$', r'\1', ast.is_str(target))
    else:
        return re.sub(r'([!?])\. $', r'\1', ast.is_str(target))


def extraspace_chopped(target: str, lang: em.LangType) -> str:
    '''Endmark with invalid space removed.
    '''
    if ast.is_instance(lang, em.LangType) is em.LangType.JPN:
        return re.sub(r'([。」])[　、](.)', r'\1\2', ast.is_str(target))
    else:
        return re.sub(r' +', r' ', ast.is_str(target))


def head_tag_from(target: str, lv: int=1) -> str:
    return "{} {}".format("#" * ast.is_int(lv), ast.is_str(target))


def hr_tag_from(num: int=9) -> str:
    return "--------" * ast.is_int(num)


def link_tag_from(target: str, link: str) -> str:
    return "[{}]({})".format(ast.is_str(target), ast.is_str(link))


def paragraph_head_inserted(target: str, lang: em.LangType) -> str:
    if lang is em.LangType.JPN:
        return target if re.match(r'\A[　#「\-\*]', target) else "　" + target
    else:
        return target if re.match(r'\A[ #"\-\*]', target) else " " + target


def period_added_if_none(target: str, lang: em.LangType) -> str:
    if lang is em.LangType.JPN:
        return target if re.match(r'\Z、', target) else target + "。"
    else:
        return target if re.match(r'\Z,', target) else target + "."


def punctuation_duplicated_chopped(target: str, lang: em.LangType) -> str:
    if lang is em.LangType.JPN:
        return re.sub(r'。、', r'。', target)
    else:
        return re.sub(r'\.,', r'.', target)


def quote_tag_from(target: str) -> str:
    return "> {}".format(ast.is_str(target))


def reflink_tag_from(target: str) -> str:
    return "[{0}]:{0}".format(ast.is_str(target))


def str_replaced_tag(target: str, tags: dict, defkey: str="me", prefix: str="$") -> str:
    tmp = target
    for k, v in ast.is_dict(tags).items():
        tmp = re.sub(r'\{}{}'.format(ast.is_str(prefix), k), v, tmp)
    if defkey in tags:
        return re.sub(r'\{}S'.format(prefix), tags[ast.is_str(defkey)], tmp)
    else:
        return tmp


def str_space_chopped(target: str) -> str:
    return re.sub(r'[ 　]', r'', target)


def strike_tag_from(target: str) -> str:
    return "~~{}~~".format(ast.is_str(target))


def ul_tag_from(target: str, space: int=0) -> str:
    return "{}- {}".format("    " * ast.is_int(space), ast.is_str(target))


def ul_tag_space_removed(target: str, space: int=1) -> str:
    return re.sub(r'\A{}( *[\-\+\*] )'.format("    "*space), r'\1', target)


def ul_tag_replaced(target: str, mark: str='+') -> str:
    return re.sub(r'[\-\+\*] ', r'{} '.format(mark), target)
