# -*- coding: utf-8 -*-
"""Define a base subject class.
"""


class _BaseSubject(object):
    """Base subject class.

    Attributes:
        name (str): a name of this subject.
        note (str): a short description.
        parent (:obj:`_BaseSubject`): a parent subject.
    """
    CLS_NAME = "_basesubject"
    def __init__(self, name: str, note: str="", parent=None):
        """
        Args:
            name (str): the name or title.
            note (str, optional): a short description.
            parent (:obj:`_BaseSubject`, optional): a parent subject.
        """
        self.name = name
        self.note = note
        self.parent = parent

    def explain(self, a=None, about=None, asa=None, at=None, by=None, fo=None, frm=None, of=None, on=None, to=None, wth=None):
        from .action import Action, ActType
        from .behavior import Behavior
        return Action(self, ActType.EXPLAIN, Behavior.EXPLAIN,
                self.infos_converted(a, about, asa, at, by, fo, frm, of, on, to, wth))

    def infos_converted(self, a, about, asa, at, by, fo, frm, of, on, to, wth) -> tuple:
        return tuple(_info_or_subject_from(v) for v in (a, about, asa, at, by, fo, frm, of, on, to, wth))


class Info(_BaseSubject):
    """Information class.
    """
    CLS_NAME = "_information"
    def __init__(self, note: str):
        super().__init__(Info.CLS_NAME, note, None)


class Nothing(_BaseSubject):
    """Nothing class.
    """
    CLS_NAME = "_nothing"
    def __init__(self):
        super().__init__(Nothing.CLS_NAME, "", None)


# private functions
def _info_or_subject_from(target) -> [Info, Nothing, _BaseSubject]:
    if isinstance(target, _BaseSubject):
        return target
    elif isinstance(target, str):
        return Info(target)
    elif isinstance(target, int):
        return Info("number_" + str(target))
    else:
        return Nothing()

