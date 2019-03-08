# -*- coding: utf-8 -*-
"""Module to build a story.
"""
from enum import Enum, auto


class ActType(Enum):
    """Act type enum.
    """
    ACT = auto()
    DESC = auto()
    DONE = auto() # for result action
    MUST = auto() # for purpose action
    SYMBOL = auto() # for title etc
    TELL = auto()
    TEST = auto()
    THINK = auto()

class Act(object):
    """Action object created.

    Attributes:
        nothing
    """
    def __init__(self, subject, act_type, action, withS=False):
        """
        Args:
            subject (obj): action subject.
            act_type (ActType): action type.
            action (str): description of this action.
            withS (bool): if True, description displays with subject.
        """
        self.action = action
        self.act_type = act_type
        self.subject = subject
        self.withS = withS


class Must(Act):
    """Special action object created.
    """
    def __init__(self, subject, action, withS=False):
        """
        Args:
            subject (obj): action subject.
            action (str): description of this action.
            withS (bool): if True, description displays with subject.
        """
        super().__init__(subject, ActType.MUST, action, withS)


class Done(Act):
    """Special action object created.
    """
    def __init__(self, subject, action, withS=False):
        """
        Args:
            subject (obj): action subject.
            action (str): description of this action.
            withS (bool): if True, description displays with subject.
        """
        super().__init__(subject, ActType.DONE, action, withS)


class Title(Act):
    """Title action object created.

    Attributes:
    """
    def __init__(self, title):
        super().__init__(self, ActType.SYMBOL, title)


class Description(Act):
    """Description action object created.

    Attributes:
    """
    def __init__(self, act):
        super().__init__(self, ActType.DESC, act)


class Person(object):
    """Character object created.

    Attributes:
    """
    def __init__(self, name, age, sex, job):
        """
        Args:
            name (str): character's name
            age (int): character's age
            sex (str): character's sex
            job (str): character's job
        """
        self.age = age
        self.job = job
        self.name = name
        self.sex = sex

    def act(self, behaviour, withS=False):
        """
        Args:
            behaviour (str): action strings.
            withS (bool): with subject.
        Returns:
            obj:`Act`: action object contained a personal action.
        """
        return Act(self, ActType.ACT, behaviour, withS)

    def desc(self, description, withS=False):
        """
        Args:
            description (str): description strings.
            withS (bool): with subject.
        Returns:
            obj:`Act`: action object contained a description.
        """
        return Act(self, ActType.DESC, description, withS)

    def tell(self, what, withS=False):
        """
        Args:
            what (str): dialogue strings.
            withS (bool): with subject.
        Returns:
            obj:`Act`: action object contained a dialogue.
        """
        return Act(self, ActType.TELL, "「{}」".format(what), withS)

    def think(self, what, withS=False):
        """
        Args:
            what (str): thinking strings.
            withS (bool): with subject.
        Returns:
            obj:`Act`: action object contained a thinking.
        """
        return Act(self, ActType.THINK, what, withS)


class Stage(object):
    """Stage object created.

    Attributes:
    """
    def __init__(self, name, explain):
        """
        Args:
            name (str): stage's name.
            explain (str): short description.
        """
        self.explain = explain
        self.name = name

    def desc(self, description, withS=False):
        """
        Args:
            description (str): description strings.
            withS (bool): with subject.
        Returns:
            obj:`Act`: action object contained a description.
        """
        return Act(self, ActType.DESC, description, withS)


class Item(object):
    """Item object created.

    Attributes.
    """
    def __init__(self, name, explain):
        """
        Args:
            name (str): item's name.
            explain (str): short description.
        """
        self.explain = explain
        self.name = name

    def desc(self, description, withS=False):
        """
        Args:
            description (str): description strings.
            withS (bool): with subject.
        Returns:
            obj:`Act`: action object contained a description.
        """
        return Act(self, ActType.DESC, description, withS)


class DayTime(object):
    """Day and Time object created.

    Attributes.
    """
    def __init__(self, name, mon=0, day=0, year=0, hour=0):
        """
        Args:
            name (str): object name.
            mon (int): month number.
            day (int): day number.
            year (int): year number.
            hour (int): hour number.
        """
        self.day = day
        self.hour = hour
        self.mon = mon
        self.name = name
        self.year = year

    def desc(self, description):
        """
        Args:
            description (str): description strings.
        Returns:
            obj:`Act`: action object contained a description.
        """
        return Act(self, ActType.DESC, description)

