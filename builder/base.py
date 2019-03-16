# -*- coding: utf-8 -*-
"""Module to build a story.
"""
from .acttypes import ActType, Behavior


class _BaseAction(object):
    """Base action object.
    """
    def __init__(self, data_class=None, title: str="action", note: str="nothing"):
        self.data = ()
        self.data_class = data_class
        self.note = note
        self.title = title

    def commit(self, *args: object):
        """
        Args:
            *args (:tuple:obj:): a core data tuple.
        Returns:
            this object.
        Raises:
            if double committed or the object type mismatch.
        """
        if self.is_double_commited():
            raise AssertionError("Cannot double commit!")

        for a in args:
            if not self.is_data_checked(a):
                raise AssertionError("Mismatch type object!")

        self.data = args
        return self

    def is_data_checked(self, arg):
        return isinstance(arg, self.data_class)

    def is_double_commited(self):
        return self.data


class Subject(object):
    """Subject of action.

    Attributes:
        name (str): name or title.
        info (str, optional): short description.
    """
    def __init__(self, name: str, note:str ="nothing"):
        """
        Args:
            name (str): the name or title.
            note (str, optional): a short description.
        """
        self.name = name
        self.note = note

    def look(self, state: str, note: str="nothing"):
        """
        Args:
            state (str): the subject looking.
        """
        return Act(self, ActType.DESC, Behavior.LOOK, state, "描写", note=note)


class Desc(object):
    """Description object.

    Attributes:
        description: a description of an action.
    """
    def __init__(self, description: str):
        self.description = description


class Act(_BaseAction):
    """Action object created.

    Attributes:
        act_type (:enum:`ActType`): an action major type.
        act_word (str): an action word.
        action (str): an action string.
        behavior (:enum:`Behavior`): a behavior type of this action.
        description (:obj:`Description`): a description of this action.
        subject (:obj:`Subject`): a subject of this action.
    """
    def __init__(self, subject: Subject, act_type: ActType, behavior: Behavior, title: str="(something)", act_word: str="", note: str="nothing"):
        """
        Args:
            subject (:obj:`Subject`): action subject.
            act_type (:enum:`ActType`): action type.
            behavior (:enum:`Behavior`): action behavior type.
            action (str): description of this action.
            act_word (str, optional): an action string.
        """
        super().__init__(Desc, title, note)
        self.act_type = act_type
        self.act_word = act_word
        self.behavior = behavior
        self.subject = subject

    def desc(self, *args: str):
        self.commit(*(self._desc_build_if_str(s) for s in args))
        return self

    def _desc_build_if_str(self, arg):
        return arg if isinstance(arg, Desc) else Desc(arg)


class BasePerson(Subject):
    """Basic character object created.

    Attributes:
    """
    def __init__(self, name: str, age: int, sex: str, job: str, note: str="nothing"):
        """
        Args:
            name (str): character's name
            age (int): character's age
            sex (str): character's sex
            job (str): character's job
            note (str, optional): a short description.
        """
        super().__init__(name, note)
        self.age = age
        self.job = job
        self.sex = sex

    def act(self, action: str, behaviour: Behavior=Behavior.DO, act_word: str="", note: str="nothing"):
        """
        Args:
            action (str): action string.
            behaviour (:enum:`Behavior`, optional): action behavior type.
            act_word (str, optional): action word.
        Returns:
            Act object contained a personal action.
        """
        return Act(self, ActType.ACT, behaviour, action, act_word, note=note)

    def tell(self, action: str, note: str="nothing"):
        """
        Args:
            action (str): a short description.
        Returns:
            Act object contained a dialogue.
        """
        return Act(self, ActType.TELL, Behavior.TALK, action, "言う", note=note)

    def think(self, action: str, note: str="nothing"):
        """
        Args:
            action (str): thinking strings.
        Returns:
            Act object contained a personal thought.
        """
        return Act(self, ActType.THINK, Behavior.FEEL, action, "思う", note=note)


class Stage(Subject):
    """Stage object created.

    Attributes:
    """
    def __init__(self, name: str, note: str="nothing"):
        """
        Args:
            name (str): stage's name.
            note (str, optional): a short description.
        """
        super().__init__(name, note)


class Item(Subject):
    """Item object created.

    Attributes.
    """
    def __init__(self, name: str, note: str="nothing"):
        """
        Args:
            name (str): item's name.
            note (str, optional): a short description.
        """
        super().__init__(name, note)


class DayTime(Subject):
    """Day and Time object created.

    Attributes.
    """
    def __init__(self, name: str, mon: int=0, day: int=0, year: int=0, hour: int=0, note: str="nothing"):
        """
        Args:
            name (str): object name.
            mon (int): month number.
            day (int): day number.
            year (int): year number.
            hour (int): hour number.
            note (str, optional): a short description.
        """
        super().__init__(name, note)
        self.day = day
        self.hour = hour
        self.mon = mon
        self.year = year

    def elapse(self, action: str, note: str="nothing"):
        """
        Args:
            action (str): action description.
        """
        return Act(self, ActType.DESC, Behavior.PASS, action, "過ぎる", note=note)


class Scene(_BaseAction):
    """Scene object that is a minimum story.
    """
    def __init__(self, title: str, note: str="nothing"):
        super().__init__(Act, title, note)


class Episode(_BaseAction):
    """Episode object that has some scenes.
    """
    def __init__(self, title: str, note: str="nothing"):
        super().__init__(Scene, title, note)


class Story(_BaseAction):
    """Story object.
    """
    def __init__(self, title: str, note: str="nothing"):
        super().__init__(Episode, title, note)

