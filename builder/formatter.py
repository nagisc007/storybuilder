# -*- coding: utf-8 -*-
"""For format class.
"""
from . import assertion


class Formatter(object):
    """The output format tools.
    """

    # methods
    def asDescription(self, data: list, format_type: str):
        if format_type in ("estar"):
            return _descriptionsAsEstar(data)
        elif format_type in ("smartphone", "phone", "smart"):
            return _descriptionsAsSmartphone(data)
        elif format_type in ("web"):
            return _descriptionsAsWebnovel(data)
        else:
            return data

    def asOutline(self, data: list):
        tmp = []
        for v in data:
            if "###" in v[0]:
                tmp.append(f"{v[0]}\n\n\t{v[1]}")
            elif "#" in v[0]:
                tmp.append(f"{v[0]}")
            else:
                tmp.append(f"- 「{v[0]}」: {v[1]}")
        return tmp

    def asScenario(self, data: list):
        from .scene import ScenarioType
        tmp = []
        for v in data:
            if v[0] is ScenarioType.DIRECTION:
                tmp.append("　　" + v[1])
            else:
                tmp.append(v[1])
        return tmp

## privates
def _descriptionsAsEstar(data: list) -> list:
    tmp = []
    inDialogue = False
    for v in assertion.is_list(data):
        cur = v.startswith(('「', '『'))
        pre = "" if inDialogue == cur else "\n"
        tmp.append(pre + v + "\n")
        inDialogue = cur
    return tmp

def _descriptionsAsSmartphone(data: list) -> list:
    return [f"{v}\n" for v in assertion.is_list(data)]

def _descriptionsAsWebnovel(data: list) -> list:
    tmp = []
    inDialogue = False
    for v in assertion.is_list(data):
        cur = v.startswith(('「', '『'))
        pre = "" if inDialogue == cur else "\n"
        tmp.append(pre + v)
        inDialogue = cur
    return tmp

