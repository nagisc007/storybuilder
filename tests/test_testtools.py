# -*- coding: utf-8 -*-
"""Test for testtools.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.basesubject import Info, Nothing
from builder.person import Person
from builder.subject import DayTime, Item, Master, Stage, something, Word
import builder.testtools as testtools


_FILENAME = "testtools.py"


class PublicMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "public methods")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student", "me", "a man")
        self.hanako = Person("Hanako", 17, "female", "student", "me", "a cute girl")
        self.day = DayTime("A day", 10, 5, 2019, 12)
        self.room = Stage("Classroom")
        self.ma = Master("The test")
        self.story = self.ma.story("THE TEST",
                self.ma.comment("-- the test start --"),
                self.day.explain("warming afternoon"),
                self.room.explain("a silent room"),
                self.taro.tell("I am").set_flag("taro"),
                self.taro.tell("Boring").set_flag(1),
                self.hanako.come("in class"),
                self.taro.lose("love").set_deflag("taro"),
                self.taro.meet(self.hanako, "a cute girl").set_deflag(1),
                self.hanako.fall(self.taro, "love").negative(),
                )

    @unittest.skip("contains fail result")
    def test_followed_all_flags(self):
        data = [
                (self.ma.combine(
                    self.taro.talk().set_flag(1),
                    self.taro.talk().set_deflag(1),
                    ), True),
                (self.ma.combine(
                    self.taro.talk().set_flag(1),
                    self.taro.talk().set_deflag(2),
                    ), False),
                ]

        for story, expected in data:
            with self.subTest(story=story, expected=expected):
                self.assertEqual(testtools.followed_all_flags(self, story), expected)

    @unittest.skip("same _has_a_daytime_in_group")
    def test_has_a_daytime(self):
        pass

    @unittest.skip("same _has_a_item_in_group")
    def test_has_a_item(self):
        pass

    @unittest.skip("same _has_a_person_in_group")
    def test_has_a_person(self):
        pass

    @unittest.skip("same _has_a_stage_in_group")
    def test_has_a_stage(self):
        pass

    @unittest.skip("same _has_a_word_in_group")
    def test_has_a_word(self):
        pass

    @unittest.skip("contains fail result")
    def test_has_basic_infos(self):
        self.assertTrue(testtools.has_basic_infos(self, self.story, self.taro, self.hanako))

    @unittest.skip("contains fail result")
    def test_has_outline_infos(self):
        what_act = self.taro.tell("Boring")
        why_act = self.taro.lose("love")
        how_act = self.taro.meet(something(),"girl")
        res_act = self.hanako.fall(self.taro, "love").negative()
        self.assertTrue(testtools.has_outline_infos(self, self.story,
            what_act, why_act, how_act, res_act, True))

    @unittest.skip("same _has_the_action_in_group")
    def test_has_the_action(self):
        pass

    @unittest.skip("same _has_the_daytime_in_group")
    def test_has_the_daytime(self):
        pass

    @unittest.skip("same _has_the_item_in_group")
    def test_has_the_item(self):
        pass

    @unittest.skip("same _has_the_person_in_group")
    def test_has_the_person(self):
        pass

    @unittest.skip("same _has_the_stage_in_group")
    def test_has_the_stage(self):
        pass

    @unittest.skip("same _has_the_word_in_group")
    def test_has_the_word(self):
        pass

    @unittest.skip("same _is_actiongroup_all_actions")
    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))


class PrivateMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "private methods")

    def setUp(self):
        self.ma = Master("test")
        self.taro = Person("Taro", 17, "male", "student")
        self.day = DayTime("Test day")
        self.stage = Stage("Test stage")
        self.item = Item("A test")
        self.word = Word("A test")

    def test_count_info_in_objects(self):
        data = [
                ((Info("a"),), 1),
                ((Info("a"), Info("b")), 2),
                ((Info("a"), Info("b"), Info("c")), 3),
                ((), 0),
                ((Info("a"), something()), 1)
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._count_info_in_objects(v), expected)
        
    def test_count_nothing_in_objects(self):
        data = [
                ((Nothing(),), 1),
                ((Nothing(), Nothing()), 2),
                ((), 0),
                ((Nothing(), something()), 1),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._count_nothing_in_objects(v), expected)

    def test_count_something_in_objects(self):
        data = [
                ((something(),), 1),
                ((something(), something()), 2),
                ((), 0),
                ((something(), Nothing()), 1)
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._count_something_in_objects(v), expected)

    @unittest.skip("using fail message")
    def test_fail_message_with_target(self):
        pass

    def test_flag_gathered(self):
        data = [
                ("flag", "deflag", True, "flag"),
                ("flag", "", True, "flag"),
                ("", "", True, ""),
                ("flag", "deflag", False, "deflag"),
                ("flag", "", False, ""),
                ("", "", False, ""),
                ]

        for flg, dflg, is_flg, expected in data:
            with self.subTest(flg=flg, dflg=dflg, is_flg=is_flg, expected=expected):
                tmp = self.taro.tell("test").set_flag(flg).set_deflag(dflg)
                self.assertEqual(testtools._flag_gatherd(tmp, is_flg), expected)

    @unittest.skip("using action group")
    def test_flags_gathered_in_group(self):
        pass

    def test_has_a_daytime(self):
        data = [
                (self.day.explain("test"), True),
                (self.taro.explain("test"), False),
                (self.taro.talk(about=self.day), True),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._has_a_daytime(v), expected)

    @unittest.skip("using action group")
    def test_has_a_daytime_in_group(self):
        pass

    def test_has_a_item(self):
        data = [
                (self.item.explain("test"), True),
                (self.taro.explain("test"), False),
                (self.taro.talk(about=self.item), True),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._has_a_item(v), expected)

    @unittest.skip("using action group")
    def test_has_a_item_in_group(self):
        pass

    def test_has_a_person(self):
        data = [
                (self.taro.explain("test"), True),
                (self.item.explain("test"), False),
                (self.stage.explain(at=self.taro), True),
                ]
        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._has_a_person(v), expected)
    
    @unittest.skip("using action group")
    def test_has_a_person_in_group(self):
        pass

    def test_has_a_stage(self):
        data = [
                (self.stage.explain("test"), True),
                (self.taro.explain("test"), False),
                (self.taro.talk(about=self.stage), True),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._has_a_stage(v), expected)

    @unittest.skip("using action group")
    def test_has_a_stage_in_group(self):
        pass

    def test_has_a_word(self):
        data = [
                (self.word.explain("test"), True),
                (self.taro.explain("test"), False),
                (self.taro.talk(at=self.word), True),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._has_a_word(v), expected)

    @unittest.skip("using action group")
    def test_has_a_word_in_group(self):
        pass

    def test_has_info_at_action(self):
        data = [
                (Info("test").explain(), True),
                (self.taro.talk(self.item), False),
                (self.taro.talk("test"), True),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._has_info_at_action(v), expected)

    def test_has_info_in_objects(self):
        data = [
                ((Info("test"),), True),
                ((something(),), False)
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._has_info_in_objects(v), expected)

    def test_has_nothing_at_action(self):
        data = [
                (Nothing().explain(), True),
                (self.taro.talk(Nothing()), True),
                (self.taro.talk("test"), True),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._has_nothing_at_action(v), expected)

    def test_has_nothing_in_objects(self):
        data = [
                ((Info("test"),), False),
                ((Nothing(),), True),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._has_nothing_in_objects(v), expected)

    def test_has_something_at_action(self):
        data = [
                (something().explain(), True),
                (self.taro.talk("test"), False),
                (self.taro.talk(something()), True),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._has_something_at_action(v), expected)

    def test_has_something_in_objects(self):
        data = [
                ((something(),), True),
                ((Info("test"),), False),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools._has_something_in_objects(v), expected)

    @unittest.skip("using action group")
    def test_has_the_action_in_group(self):
        pass

    @unittest.skip("using action group")
    def test_has_the_action_in_group_with_fuzzy(self):
        pass

    def test_has_the_daytime(self):
        data = [
                (self.taro.talk(self.day), self.day, True),
                (self.day.explain(), self.day, True),
                (self.taro.talk(), self.day, False),
                ]

        for act, target, expected in data:
            with self.subTest(act=act, target=target, expected=expected):
                self.assertEqual(testtools._has_the_daytime(act, target), expected)

    @unittest.skip("using action group")
    def test_has_the_daytime_in_group(self):
        pass

    def test_has_the_info(self):
        data = [
                (Info("testing"), Info("test"), True),
                (Info("test"), Info("tention"), False),
                ]

        for val, target, expected in data:
            with self.subTest(val=val, target=target, expected=expected):
                self.assertEqual(testtools._has_the_info(val, target), expected)

    def test_has_the_infos(self):
        data = [
                ((Info("test"), Info("apple")),
                    (Info("apple"),), True),
                ((Info("test"), Info("apple")),
                    (Info("orange"),), False),
                ]

        for vals, targets, expected in data:
            with self.subTest(vals=vals, targets=targets, expected=expected):
                self.assertEqual(testtools._has_the_infos(vals, targets), expected)

    def test_has_the_item(self):
        data = [
                (self.item.explain(), self.item, True),
                (self.taro.talk(), self.item, False),
                (self.taro.talk(self.item), self.item, True),
                ]

        for act, target, expected in data:
            with self.subTest(act=act, target=target, expected=expected):
                self.assertEqual(testtools._has_the_item(act, target), expected)

    @unittest.skip("using action group")
    def test_has_the_item_in_group(self):
        pass

    def test_has_the_person(self):
        data = [
                (self.taro.talk(), self.taro, True),
                (self.stage.explain(), self.taro, False),
                (self.stage.explain(self.taro), self.taro, True),
                ]

        for act, target, expected in data:
            with self.subTest(act=act, target=target, expected=expected):
                self.assertEqual(testtools._has_the_person(act, target), expected)

    @unittest.skip("using action group")
    def test_has_the_person_in_group(self):
        pass

    def test_has_the_stage(self):
        data = [
                (self.stage.explain(), self.stage, True),
                (self.taro.talk(), self.stage, False),
                (self.taro.talk(self.stage), self.stage, True),
                ]

        for act, target, expected in data:
            with self.subTest(act=act, target=target, expected=expected):
                self.assertEqual(testtools._has_the_stage(act, target), expected)

    @unittest.skip("using action group")
    def test_has_the_stage_in_group(self):
        pass

    def test_has_the_word(self):
        data = [
                (self.word.explain(), self.word, True),
                (self.taro.talk(), self.word, False),
                (self.taro.talk(self.word), self.word, True),
                ]

        for act, target, expected in data:
            with self.subTest(act=act, target=target, expected=expected):
                self.assertEqual(testtools._has_the_word(act, target), expected)

    @unittest.skip("using action group")
    def test_has_the_word_in_group(self):
        pass

    def test_is_actiongroup_all_actions(self):
        data = [
                ((self.taro.talk(), self.taro.talk(),), True),
                ((self.taro.talk(), "test"), False),
                ]

        for vals, expected in data:
            with self.subTest(vals=vals, expected=expected):
                tmp = self.ma.combine(*vals)
                self.assertEqual(testtools._is_actiongroup_all_actions(tmp), expected)

    @unittest.skip("complex test")
    def test_is_the_action(self):
        pass

    def test_is_the_action_behavior(self):
        data = [
                (self.taro.talk(), self.taro.talk(), True),
                (self.taro.talk(), self.taro.take(), False),
                (self.taro.talk().must(), self.taro.talk().must(), True),
                (self.taro.talk().may(), self.taro.talk(), False),
                (self.taro.talk().non(), self.taro.talk().non(), True),
                (self.taro.talk().non(), self.taro.talk(), False),
                (self.taro.talk().ps(), self.taro.talk().ps(), True),
                (self.taro.talk().ps(), self.taro.talk(), False),
                (self.taro.talk().can().non().ps(), self.taro.talk().can().non().ps(), True),
                (self.taro.talk().should().non(), self.taro.talk().should().non().ps(), False),
                ]

        for act, target, expected in data:
            with self.subTest(act=act, target=target, expected=expected):
                self.assertEqual(testtools._is_the_action_behavior(act, target), expected)

    @unittest.skip("nearly eq is _is_the_infos")
    def test_is_the_action_infos(self):
        pass

    @unittest.skip("nearly eq is _is_the_subject")
    def test_is_the_action_subject(self):
        pass

    @unittest.skip("nearly eq is _is_the_objects")
    def test_is_the_action_objects(self):
        pass

    def test_is_the_infos(self):
        data = [
                (self.taro.talk("test"),
                    (Info("test"),), True),
                (self.taro.talk("test", "apple"),
                    (Info("apple"), Info("orrange")), False),
                (self.taro.talk("test", "apple"),
                    (Info("test"), Info("app")), False),
                ]

        for act, targets, expected in data:
            with self.subTest(act=act, targets=targets, expected=expected):
                self.assertEqual(testtools._is_the_infos(act.objects, targets), expected)

    def test_is_the_objects(self):
        data = [
                (self.taro.talk(self.item, self.word),
                    (self.item, self.word), True),
                (self.taro.talk(self.item, self.stage),
                    (self.item, self.word), False),
                ]

        for act, targets, expected in data:
            with self.subTest(act=act, targets=targets, expected=expected):
                self.assertEqual(testtools._is_the_objects(act.objects, targets), expected)

    def test_is_the_subject(self):
        data = [
                (self.taro, self.item, False),
                (self.taro, self.taro, True),
                (self.taro, Person("Taro", 0, "ma", "job"), True),
                ]

        for sub, target, expected in data:
            with self.subTest(sub=sub, target=target, expected=expected):
                self.assertEqual(testtools._is_the_subject(sub, target), expected)

    @unittest.skip("complex test")
    def test_near_eq_is_the_action(self):
        pass

    @unittest.skip("complex test")
    def test_near_eq_is_the_infos(self):
        pass

    @unittest.skip("complex test")
    def test_near_eq_is_the_objects(self):
        pass

    def test_near_eq_is_the_subject(self):
        data = [
                (self.taro, self.item, False),
                (self.taro, self.taro, True),
                (self.taro, something(), True),
                (something(), self.item, True),
                ]

        for sub, target, expected in data:
            with self.subTest(sub=sub, target=target, expected=expected):
                self.assertEqual(testtools._near_eq_is_the_subject(sub, target), expected)

