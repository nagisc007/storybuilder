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

    def look(self, state, act_word="見える", with_act=False, with_sub=False):
        """
        Args:
            state (str): the subject looking.
            act_word (str, optional): action string.
            with_act (bool, optional): with act word.
            with_sub (bool, optional): with subject.
        """
        return Act(self, ActType.DESC, Behavior.LOOK, state, act_word, with_act, with_sub)


class Act(object):
    """Action object created.

    Attributes:
        act_type (:enum:ActType): action major type.
        act_word (str): base action word.
        action (str): action describes.
        behavior (:enum:Behavior): action behavior type.
        description (str): a description of this action.
        subject (:obj:`Subject`): subject of this action.
        with_act (bool): which has desplayed with act word.
        with_sub (bool): which has desplayed with subject.
    """
    def __init__(self, subject, act_type, behavior, action, act_word="", with_act=False, with_sub=False):
        """
        Args:
            subject (:obj:`Subject`): action subject.
            act_type (:enum:`ActType`): action type.
            behavior (:enum:`Behavior`): action behavior type.
            action (str): description of this action.
            act_word (str, optional): an action string.
            with_act (bool, optional): if True, action displays with act word
            with_sub (bool, optional): if True, description displays with subject.
        """
        self.action = action
        self.act_type = act_type
        self.act_word = act_word
        self.behavior = behavior
        self.description = ""
        self.subject = subject
        self.with_act = with_act
        self.with_sub = with_sub

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

    def act(self, action, behaviour=Behavior.DO, act_word="", with_act=False, with_sub=False):
        """
        Args:
            action (str): action string.
            behaviour (:enum:`Behavior`, optional): action behavior type.
            act_word (str, optional): action word.
            with_act (bool, optional): with act word.
            with_sub (bool, optional): with subject.
        Returns:
            Act object contained a personal action.
        """
        return Act(self, ActType.ACT, behaviour, action, act_word, with_act, with_sub)

    def tell(self, action, act_word="", with_act=False, with_sub=False):
        """
        Args:
            action (str): short description.
            act_word (str, optional): action string.
            with_act (bool, optional): with act word.
            with_sub (bool, optional): with subject.
        Returns:
            Act object contained a dialogue.
        """
        return Act(self, ActType.TELL, Behavior.TALK, action, act_word, with_act, with_sub)

    def think(self, action, act_word="思う", with_act=False, with_sub=False):
        """
        Args:
            action (str): thinking strings.
            act_word (str, optional): action string.
            with_act (bool, optional): with act word.
            with_sub (bool, optional): with subject.
        Returns:
            Act object contained a personal thought.
        """
        return Act(self, ActType.THINK, Behavior.FEEL, action, act_word, with_act, with_sub)

    def must(self, action, act_word="しなければならない", with_act=False, with_sub=False):
        """
        Args:
            action (str): a subject must do something.
            act_word (str, optional): action string.
            with_act (bool, optional): with act word.
            with_sub (bool, optional): with subject.
        Returns:
            Act object contained a personal thought.
        """
        return Act(self, ActType.THINK, Behavior.MUST_DO, action, act_word, with_act, with_sub)

    def want(self, action, act_word="したい", with_act=False, with_sub=False):
        """
        Args:
            action (str): a subject want to do something.
            act_word (str, optional): action string.
            with_act (bool, optional): with act word.
            with_sub (bool, optional): with subject.
        Returns:
            Act object contained a personal thought.
        """
        return Act(self, ActType.THINK, Behavior.WANT, action, act_word, with_act, with_sub)

    def result(self, action, act_word="だった", with_act=False, with_sub=False):
        """
        Args:
            action (str): a subject got any result.
            act_word (str, optional): act string.
            with_act (bool, optional): with act word.
            with_sub (bool, optional): with subject.
        Returns:
            Act object contained a personal thought.
        """
        return Act(self, ActType.ACT, Behavior.RESULT, action, act_word, with_act, with_sub)


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

    def elapse(self, action, act_word="過ぎる", with_act=True, with_sub=False):
        """
        Args:
            action (str): action description.
            act_word (str, optional): action string.
            with_act (bool, optional): with act word.
            with_sub (bool, optional): with subject.
        """
        return Act(self, ActType.DESC, Behavior.PASS, action, act_word, with_act, with_sub)

