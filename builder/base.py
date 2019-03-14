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
    def __init__(self, name, info="nothing"):
        """
        Args:
            name (str): name or title.
            info (str, optional): short description.
        """
        self.info = info
        self.name = name

    def look(self, state, withS=False):
        """
        Args:
            state (str): the subject looking.
            withS (bool): with subject.
        """
        return Act(self, ActType.DESC, Behavior.LOOK, state, withS)


class Act(object):
    """Action object created.

    Attributes:
        act_type (:enum:ActType): action major type.
        action (str): action describes.
        behavior (:enum:Behavior): action behavior type.
        description (str): a description of this action.
        subject (:obj:`Subject`): subject of this action.
        withS (bool): which has desplayed with subject.
    """
    def __init__(self, subject, act_type, behavior, action, withS=False):
        """
        Args:
            subject (:obj:`Subject`): action subject.
            act_type (:enum:`ActType`): action type.
            behavior (:enum:`Behavior`): action behavior type.
            action (str): description of this action.
            withS (bool): if True, description displays with subject.
        """
        self.action = action
        self.act_type = act_type
        self.behavior = behavior
        self.description = ""
        self.subject = subject
        self.withS = withS

    def desc(self, description):
        """
        Args:
            description (str): sentence for the action.
        Returns:
            This action object.
        """
        self.description = description
        return self


class Title(Act):
    """Title action object created.

    Attributes:
        title (str): a title string.
        info (str, optional): a short description.
    """
    def __init__(self, title, info="nothing"):
        """
        Args:
            title (str): a title string.
            info (str, optional): a short description.
        """
        super().__init__(Subject(title, info), ActType.SYMBOL, Behavior.DISPLAY, title)


class BasePerson(Subject):
    """Basic character object created.

    Attributes:
    """
    def __init__(self, name, age, sex, job, info):
        """
        Args:
            name (str): character's name
            age (int): character's age
            sex (str): character's sex
            job (str): character's job
            info (str): a short description.
        """
        super().__init__(name, info)
        self.age = age
        self.job = job
        self.sex = sex

    def act(self, action, behaviour=Behavior.DO, withS=False):
        """
        Args:
            action (str): action string.
            behaviour (:enum:`Behavior`): action behavior type.
            withS (bool): with subject.
        Returns:
            Act object contained a personal action.
        """
        return Act(self, ActType.ACT, behaviour, action, withS)

    def tell(self, action, withS=False):
        """
        Args:
            action (str): short description.
            withS (bool): with subject.
        Returns:
            Act object contained a dialogue.
        """
        return Act(self, ActType.TELL, Behavior.TALK, action, withS)

    def think(self, action, withS=False):
        """
        Args:
            action (str): thinking strings.
            withS (bool): with subject.
        Returns:
            Act object contained a personal thought.
        """
        return Act(self, ActType.THINK, Behavior.FEEL, action, withS)

    def must(self, action, withS=False):
        """
        Args:
            action (str): a subject must do something.
            withS (bool): with subject.
        Returns:
            Act object contained a personal thought.
        """
        return Act(self, ActType.THINK, Behavior.MUST_DO, action, withS)

    def want(self, action, withS=False):
        """
        Args:
            action (str): a subject want to do something.
            withS (bool): with subject.
        Returns:
            Act object contained a personal thought.
        """
        return Act(self, ActType.THINK, Behavior.WANT, action, withS)

    def result(self, action, withS=False):
        """
        Args:
            action (str): a subject got any result.
            withS (bool): with subject.
        Returns:
            Act object contained a personal thought.
        """
        return Act(self, ActType.ACT, Behavior.RESULT, action, withS)


class Stage(Subject):
    """Stage object created.

    Attributes:
    """
    def __init__(self, name, info="nothing"):
        """
        Args:
            name (str): stage's name.
            info (str, optional): a short description.
        """
        super().__init__(name, info)


class Item(Subject):
    """Item object created.

    Attributes.
    """
    def __init__(self, name, info="nothing"):
        """
        Args:
            name (str): item's name.
            info (str, optional): a short description.
        """
        super().__init__(name, info)


class DayTime(Subject):
    """Day and Time object created.

    Attributes.
    """
    def __init__(self, name, mon=0, day=0, year=0, hour=0, info="nothing"):
        """
        Args:
            name (str): object name.
            mon (int): month number.
            day (int): day number.
            year (int): year number.
            hour (int): hour number.
            info (str, optional): a short description.
        """
        super().__init__(name, info)
        self.day = day
        self.hour = hour
        self.mon = mon
        self.year = year

    def elapse(self, action="過ぎる", withS=False):
        return Act(self, ActType.DESC, Behavior.PASS, action, withS)
