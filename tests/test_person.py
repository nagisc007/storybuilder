# -*- coding: utf-8 -*-
"""Test: person.py
"""
import unittest
from builder.testutils import print_test_title
from builder import enums as em
from builder import person as psn


_FILENAME = "person.py"


class PersonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Person")

    def setUp(self):
        self.taro = psn.Person("Taro", 17, "male", "student")
        self.hanako = psn.Person("Hanako", 17, "female", "student")

    def test_attributes(self):
        data = [
                ("Taro", 17, "male", "student", "俺", "a man",
                    "Taro", 17, "male", "student", {"me":"俺"}, "a man"),
                ]
        for name, age, sex, job, calling, note, exp_name, exp_age, exp_sex, exp_job, exp_calling, exp_note in data:
            with self.subTest(name=name, age=age, sex=sex, job=job, calling=calling, note=note,
                    exp_name=exp_name, exp_age=exp_age, exp_sex=exp_sex, exp_job=exp_job,
                    exp_calling=exp_calling, exp_note=exp_note):
                tmp = psn.Person(name, age, sex, job, calling, note)
                self.assertIsInstance(tmp, psn.Person)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.age, exp_age)
                self.assertEqual(tmp.sex, exp_sex)
                self.assertEqual(tmp.job, exp_job)
                self.assertEqual(tmp.calling, exp_calling)
                self.assertEqual(tmp.note, exp_note)

    def test_behaviors(self):
        data = [
                ("ask", (self.taro,), "",
                    em.ActType.TALK, self.hanako, "ask", (self.taro,)),
                ("behav", (self.taro,), "",
                    em.ActType.BEHAV, self.hanako, "behav", (self.taro,)),
                ("come", (self.taro,), "",
                    em.ActType.MOVE, self.hanako, "come", (self.taro,)),
                ("deal", (self.taro,), "",
                    em.ActType.DEAL, self.hanako, "deal", (self.taro,)),
                ("feel", (self.taro,), "",
                    em.ActType.FEEL, self.hanako, "feel", (self.taro,)),
                ("go", (self.taro,), "",
                    em.ActType.MOVE, self.hanako, "go", (self.taro,)),
                ("have", (self.taro,), "",
                    em.ActType.DEAL, self.hanako, "have", (self.taro,)),
                ("hear", (self.taro,), "",
                    em.ActType.TALK, self.hanako, "hear", (self.taro,)),
                ("know", (self.taro,), "",
                    em.ActType.THINK, self.hanako, "know", (self.taro,)),
                ("look", (self.taro,), "",
                    em.ActType.LOOK, self.hanako, "look", (self.taro,)),
                ("meet", (self.taro,), "",
                    em.ActType.LOOK, self.hanako, "meet", (self.taro,)),
                ("move", (self.taro,), "",
                    em.ActType.MOVE, self.hanako, "move", (self.taro,)),
                ("remember", (self.taro,), "",
                    em.ActType.THINK, self.hanako, "remember", (self.taro,)),
                ("reply", (self.taro,), "",
                    em.ActType.TALK, self.hanako, "reply", (self.taro,)),
                ("talk", (self.taro,), "",
                    em.ActType.TALK, self.hanako, "talk", (self.taro,)),
                ("think", (self.taro,), "",
                    em.ActType.THINK, self.hanako, "think", (self.taro,)),
                ]

        for attr, obj, verb, exp_type, exp_sub, exp_verb, exp_obj in data:
            with self.subTest(attr=attr, obj=obj, verb=verb,
                    exp_type=exp_type, exp_sub=exp_sub, exp_verb=exp_verb, exp_obj=exp_obj):
                doing = getattr(self.hanako, attr)
                tmp = doing(*obj, verb=verb) if verb else doing(*obj)
                self.assertIsInstance(tmp, psn.sb.act.Action)
                self.assertEqual(tmp.act_type, exp_type)
                self.assertEqual(tmp.subject, exp_sub)
                self.assertEqual(tmp.verb, exp_verb)
                self.assertEqual(tmp.objects, exp_obj)

    def test_inherited(self):
        taro = psn.Person("Taro", 17, "male", "student", "俺", "a man")
        data = [
                (taro,
                    "Taro", 17, "male", "student", {"me":"俺"}, "a man"),
                ]

        for v, name, age, sex, job, calling, note in data:
            with self.subTest(v=v, name=name, age=age, sex=sex, job=job, calling=calling, note=note):
                tmp = taro.inherited()
                self.assertIsInstance(tmp, psn.Person)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.age, age)
                self.assertEqual(tmp.sex, sex)
                self.assertEqual(tmp.job, job)
                self.assertEqual(tmp.calling, calling)
                self.assertEqual(tmp.note, note)
