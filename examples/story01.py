# -*- coding: utf-8 -*-
"""Example usage: story 01
"""

from builder.base import Act, ActType, Must, Done, Title, Description, Person, Stage, Item, DayTime


# Characters config

class Taro(Person):
    def __init__(self):
        super().__init__("太郎", 17, "male", "高校生")
        self.lastname = "坂下"
        self.callself = '俺'


class Hanako(Person):
    def __init__(self):
        super().__init__("花子", 17, "female", "高校生")
        self.lastname = "如月"
        self.fullname = self.lastname + self.name
        self.callself = 'わたし'

class Teacher(Person):
    def __init__(self):
        super().__init__("先生", 36, "male", "国語教師")

# Stages config

class ClassRoom(Stage):
    def __init__(self):
        super().__init__("教室", "殺風景な机と椅子が並べられた部屋")


# Items config


class Sky(Item):
    def __init__(self):
        super().__init__("空", "空模様")

# DayTime config

class FirstDay(DayTime):
    def __init__(self):
        super().__init__("一日目", mon=7, day=1, year=2019)


class LastDay(DayTime):
    def __init__(self):
        super().__init__("最終日", mon=7, day=20, year=2019)


def meeting(classroom, firstday, taro, hanako, teacher, sky):
    '''Episode: Taro meets hanako.
    '''
    return (
            classroom.desc("机が整然と並ぶ教室"),
            sky.desc("薄曇りが広がっていた"),
            firstday.desc("七月が始まったところだった"),
            taro.think("つまらない学校生活"),
            Must(taro, "このつまらない生活を何とかしたい"),
            teacher.act("教室に入ってくる", True),
            hanako.act("彼女は先生について一緒に入ってきた"),
            hanako.desc("この時代には珍しく黒髪を二つのお下げに結んでいた"),
            hanako.desc("黒縁が目立つ眼鏡を掛けて"),
            hanako.desc("少し照れたように頬を染め"),
            hanako.act("俯いていた"),
            taro.act("目を奪われた"),
            teacher.tell("転校生を紹介する。{}さんだ".format(hanako.fullname)),
            hanako.tell("宜しく、お願いします"),
            Done(taro, "彼女と出会った"),
            )

def confession(classroom, lastday, taro, hanako):
    '''Episode: Taro confesses Hanako.
    '''
    return (
            lastday.desc("一学期の終業式を終え"),
            classroom.desc("閑散とした教室だった"),
            taro.act("彼女を待っていた"),
            Must(taro, "{}に告白する".format(hanako.name)),
            hanako.act("そっと足音もなく現れた"),
            hanako.tell("用事って何"),
            hanako.desc("目を細めて{}を見ている".format(taro.name)),
            taro.tell("なあ。どうして転校してきたんだ？"),
            hanako.tell("{}君に会う為、だと言ったら？".format(taro.lastname)),
            taro.act("心臓が飛び出そうだった"),
            hanako.tell("{}はね、未来から来たの。あなたに会う為に".format(hanako.callself)),
            taro.tell("もうそんな嘘はいい"),
            hanako.tell("本当よ。信じなくてもいいけど"),
            hanako.tell("でもね、これだけは知っておいて欲しい。{}は必死でここまで来た。だからあなたの素っ気ない手紙に応えて、ここにいるってこと".format(hanako.callself)),
            taro.tell("じゃあ、今から{}が何を言うかも分かってるんだな？".format(taro.callself)),
            hanako.act("小さく頷く"),
            taro.tell("{}さん。{}と、付き合って下さい".format(hanako.fullname, taro.callself)),
            hanako.act("再び小さく頷いた"),
            Done(taro, "{}に告白した".format(hanako.name)),
            )

def story():
    '''Main story created.

    Returns:
        obj:`Tuple`:'Act': story actions.
    '''
    # characters
    taro = Taro()
    hanako = Hanako()
    teacher = Teacher()
    # stages
    classroom = ClassRoom()
    # items
    sky = Sky()
    # daytimes
    firstday = FirstDay()
    lastday = LastDay()

    return meeting(classroom, firstday, taro, hanako, teacher, sky) +\
            confession(classroom, lastday, taro, hanako)

