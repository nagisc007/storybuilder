# -*- coding: utf-8 -*-
"""Module to build a story.
"""
from .acttypes import ActType, Behavior


class Subject(object):
    """Subject of action.

    Attributes:
        name (str): name or title.
        info (str, optional): short description.
    """
    def __init__(self, name, note="nothing"):
        """
        Args:
            name (str): the name or title.
            note (str, optional): a short description.
        """
        self.name = name
        self.note = note

    def look(self, state):
        """
        Args:
            state (str): the subject looking.
        """
        return Act(self, ActType.DESC, Behavior.LOOK, state, "描写")


class Description(object):
    """Description object.

    Attributes:
        description: a description of an action.
    """
    def __init__(self, description):
        self.description = description


class Act(object):
    """Action object created.

    Attributes:
        act_type (:enum:`ActType`): an action major type.
        act_word (str): an action word.
        action (str): an action string.
        behavior (:enum:`Behavior`): a behavior type of this action.
        description (:obj:`Description`): a description of this action.
        subject (:obj:`Subject`): a subject of this action.
    """
    def __init__(self, subject, act_type, behavior, action, act_word=""):
        """
        Args:
            subject (:obj:`Subject`): action subject.
            act_type (:enum:`ActType`): action type.
            behavior (:enum:`Behavior`): action behavior type.
            action (str): description of this action.
            act_word (str, optional): an action string.
        """
        self.action = action
        self.act_type = act_type
        self.act_word = act_word
        self.behavior = behavior
        self.description = None
        self.subject = subject

    def desc(self, description):
        """
        Args:
            description (str): a description sentence.
        Returns:
            This action object.
        """
        self.description = Description(description)
        return self


class Title(Act):
    """Title action object created.

    Attributes:
        title (str): a title string.
        note (str, optional): a short description.
    """
    def __init__(self, title, note="nothing"):
        """
        Args:
            title (str): a title string.
            note (str, optional): a short description.
        """
        super().__init__(Subject(title, note), ActType.SYMBOL, Behavior.DISPLAY, title)


class BasePerson(Subject):
    """Basic character object created.

    Attributes:
    """
    def __init__(self, name, age, sex, job, note="nothing"):
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

    def act(self, action, behaviour=Behavior.DO, act_word=""):
        """
        Args:
            action (str): action string.
            behaviour (:enum:`Behavior`, optional): action behavior type.
            act_word (str, optional): action word.
        Returns:
            Act object contained a personal action.
        """
        return Act(self, ActType.ACT, behaviour, action, act_word)

    def tell(self, action):
        """
        Args:
            action (str): a short description.
        Returns:
            Act object contained a dialogue.
        """
        return Act(self, ActType.TELL, Behavior.TALK, action, "言う")

    def think(self, action):
        """
        Args:
            action (str): thinking strings.
        Returns:
            Act object contained a personal thought.
        """
        return Act(self, ActType.THINK, Behavior.FEEL, action, "思う")


class Stage(Subject):
    """Stage object created.

    Attributes:
    """
    def __init__(self, name, note="nothing"):
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
    def __init__(self, name, note="nothing"):
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
    def __init__(self, name, mon=0, day=0, year=0, hour=0, note="nothing"):
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

    def elapse(self, action):
        """
        Args:
            action (str): action description.
        """
        return Act(self, ActType.DESC, Behavior.PASS, action, "過ぎる")

