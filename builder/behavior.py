# -*- coding: utf-8 -*-
"""Define behaviors.
"""
from enum import Enum, auto


class BehavType(Enum):
    """Categorized behavior type enum.
    """
    DONE = auto() # 行為全般
    COOKED = auto() # 料理系
    DEALT = auto() # 取扱系
    DIALOGUE = auto() # 台詞
    EXPRESSED = auto() # 表現系
    FELT = auto() # 感覚系
    HANDLED = auto() # 操作系
    MOVED = auto() # 移動系
    TALKED = auto() # 話す系
    THOUGHT = auto() # 思考系
    VIEWED = auto() # 視覚系

    def __str__(self) -> str:
        return {
                self.COOKED.value: "_COOK",
                self.DEALT.value: "_DEAL",
                self.DIALOGUE.value: "_DIALOGUE",
                self.DONE.value: "_DO",
                self.EXPRESSED.value: "_EXPRESS",
                self.FELT.value: "_FEEL",
                self.HANDLED.value: "_HANDLE",
                self.MOVED.value: "_MOVE",
                self.TALKED.value: "_TALK",
                self.THOUGHT.value: "_THINK",
                self.VIEWED.value: "_VIEW",
                }[self.value]


class Behavior(Enum):
    """Behavior type enum.
    """
    # nothing
    NONE = auto()
    # act behavior
    ABANDON = auto() # 放棄する
    ABSORB = auto() # 吸い取る
    ABUSE = auto() # 乱用する
    ACCEPT = auto() # 受け入れる
    ACCOMPANY = auto() # 伴う
    ACCORD = auto() # 調和する
    ACCOUNT = auto() # 勘定する
    ACCUSE = auto() # 訴える
    ACHIEVE = auto() # 果たす
    ACQUIRE = auto() # 得る
    ACT = auto() # 行動する
    ADD = auto() # 加える
    ADDRESS = auto() # 
    ADHERE = auto()
    ADJUST = auto() # 調整する
    ADMIRE = auto() # 憧れる
    ADMIT = auto() # 認める
    ADOPT = auto() # 採用する
    ADVANCE = auto() # 進める
    ADVERTISE = auto() # 宣伝する
    ADVISE = auto() # 助言する
    AFFECT = auto()
    AFFORD = auto()
    AGREE = auto()
    AID = auto()
    AIM = auto()
    ALLEGE = auto()
    ALLOW = auto()
    ALTER = auto()
    ANGRY = auto()
    ANNOUNCE = auto()
    ANNOY = auto()
    ANSWER = auto()
    ANTICIPATE = auto()
    APOLOGIZE = auto()
    APPEAL = auto()
    APPEAR = auto()
    APPLY = auto()
    APPOINT = auto()
    APPRICIATE = auto()
    APPROACH = auto()
    APPROVE = auto()
    ARGUE = auto()
    ARRANGE = auto()
    ARREST = auto()
    ARRIVE = auto()
    ASK = auto()
    ASSIST = auto()
    ASSUME = auto()
    ASSURE = auto()
    ATTACH = auto()
    ATTACK = auto()
    ATTEMPT = auto()
    ATTEND = auto()
    ATTRACT = auto()
    AVOID = auto()
    AWARD = auto()
    BAKE = auto()
    BAN = auto()
    BASE = auto()
    BE = auto()
    BEAR = auto()
    BEAT = auto()
    BECOME = auto()
    BEG = auto()
    BEGIN = auto()
    BEHAVE = auto()
    BELIEVE = auto()
    BELONG = auto()
    BEND = auto()
    BET = auto()
    BETRAY = auto()
    BID = auto()
    BIND = auto()
    BITE = auto()
    BLAME = auto()
    BLEED = auto()
    BLEND = auto()
    BLESS = auto()
    BLOCK = auto()
    BLOW = auto()
    BOAST = auto()
    BOIL = auto()
    # BOOK = auto() # 予約
    BORE = auto()
    BORROW = auto()
    BOTHER = auto()
    BOUND = auto()
    BOW = auto()
    BREAK = auto()
    BREATHE = auto()
    BRING = auto()
    BROW = auto() # 眉を顰める
    BUILD = auto()
    BURN = auto()
    BURST = auto()
    BURY = auto()
    BUY = auto()
    CALCULATE = auto()
    CALL = auto()
    CANCEL = auto()
    CAPTURE = auto()
    CARE = auto()
    CARRY = auto()
    CAST = auto()
    CATCH = auto()
    CAUSE = auto()
    CEASE = auto()
    CELEBRATE = auto()
    CHANGE = auto()
    CHARGE = auto()
    CHARM = auto()
    CHASE = auto()
    CHEAT = auto()
    CHECK = auto()
    CHEER = auto()
    CHEW = auto()
    CHOOSE = auto()
    CHOP = auto()
    CLAIM = auto()
    CLEAN = auto()
    CLICK = auto()
    CLIMB = auto()
    CLING = auto()
    CLIP = auto()
    CLOSE = auto()
    CLOTHE = auto()
    COACH = auto()
    COLLAPSE = auto()
    COLLECT = auto()
    COMBINE = auto()
    COME = auto()
    COMFORT = auto()
    COMMAND = auto()
    COMMIT = auto()
    COMMUNICATE = auto()
    COMPARE = auto()
    COMPETE = auto()
    COMPLAIN = auto()
    COMPLETE = auto()
    COMPOSE = auto()
    CONCEIVE = auto()
    CONCENTRATE = auto()
    CONCERN = auto()
    CONCLUDE = auto()
    CONDUCT = auto()
    CONFESS = auto()
    CONFIRM = auto()
    CONFRONT = auto()
    CONFUSE = auto()
    CONNECT = auto()
    CONSIDER = auto()
    CONSIST = auto()
    CONSTRUCT = auto()
    CONSUME = auto()
    CONTACT = auto()
    CONTAIN = auto()
    CONTINUE = auto()
    CONTRIBUTE = auto()
    CONTROL = auto()
    CONVERT = auto()
    CONVEY = auto()
    CONVINCE = auto()
    COOK = auto()
    COOL = auto()
    COOPERATE = auto()
    COPE = auto()
    COPY = auto()
    CORRECT = auto()
    COST = auto()
    COUGH = auto()
    COUNT = auto()
    COUNTER = auto()
    COVER = auto()
    CRACK = auto()
    CRASH = auto()
    CRAWL = auto()
    CREATE = auto()
    CRITICIZE = auto()
    CROSS = auto()
    CRUSH = auto()
    CRY = auto()
    CURE = auto()
    CURL = auto()
    CUT = auto()
    DANCE = auto()
    DAMAGE = auto()
    DARE = auto()
    DEAL = auto() # 扱う
    DECAY = auto()
    DECIDE = auto()
    DECLARE = auto()
    DECLINE = auto()
    DECORATE = auto()
    DECREASE = auto()
    DEFEAT = auto()
    DEFEND = auto()
    DEFINE = auto()
    DELAY = auto()
    DELIVER = auto()
    DEMONSTRATE = auto()
    DENY = auto()
    DEPEND = auto()
    DEPOSITE = auto()
    DERIVE = auto()
    DESCEND = auto()
    DESCRIBE = auto()
    DESERT = auto()
    DESERVE = auto()
    DESIRE = auto()
    DESTROY = auto()
    DETERMINE = auto()
    DEVELOP = auto()
    DEVISE = auto()
    DEVOTE = auto()
    DIAL = auto()
    DIE = auto()
    DIG = auto()
    DIGEST = auto()
    DISAPPEAR = auto()
    DISAPPOINT = auto()
    DISAPPROVE = auto()
    DISCHARGE = auto()
    DISCOVER = auto()
    DISCUSS = auto()
    DISGUISE = auto()
    DISGUST = auto()
    DISLIKE = auto()
    DISMISS = auto()
    DISPEL = auto()
    DISPLAY = auto() # for symbols
    DISTINGUISH = auto()
    DISTRIBUTE = auto()
    DIVE = auto()
    DIVIDE = auto()
    DIVORCE = auto()
    DO = auto()
    DOMINATE = auto()
    DOUBT = auto()
    DRAG = auto()
    DRAW = auto()
    DREAM = auto()
    DRESS = auto()
    DRIFT = auto()
    DRINK = auto()
    DRIVE = auto()
    DROP = auto()
    DROWN = auto()
    DRY = auto()
    EARN = auto()
    EASE = auto()
    EAT = auto()
    EDUCATE = auto()
    ELECT = auto()
    ELIMINATE = auto()
    EMAIL = auto()
    EMBARRASS = auto()
    EMERGE = auto()
    EMPHASIZE = auto()
    EMPLOY = auto()
    ENABLE = auto()
    ENCOUNTER = auto()
    ENCOURAGE = auto()
    END = auto()
    ENDURE = auto()
    ENGAGE = auto()
    ENJOY = auto()
    ENSURE = auto()
    ENTER = auto()
    ENTERTAIN = auto()
    ENVY = auto()
    EQUIP = auto()
    ESCAPE = auto()
    ESTABLISH = auto()
    ESTIMATE = auto()
    EXAMINE = auto()
    EXCHANGE = auto()
    EXCITE = auto()
    EXCUSE = auto()
    EXHAUST = auto()
    EXHIBIT = auto()
    EXIST = auto()
    EXPAND = auto()
    EXPECT = auto()
    EXPLAIN = auto()
    EXPLODE = auto()
    EXPLORE = auto()
    EXPORT = auto()
    EXPOSE = auto()
    EXPRESS = auto()
    EXTEND = auto()
    FACE = auto()
    FAIL = auto()
    FALL = auto()
    FASTEN = auto()
    FEED = auto()
    FEEL = auto() # for think action
    FIB = auto() # 嘘
    FIGHT = auto()
    FILL = auto()
    FIND = auto()
    FINISH = auto()
    FIRE = auto()
    FIREJOB = auto()
    FIT = auto()
    FIX = auto()
    FLASH = auto()
    FLEE = auto()
    FLOAT = auto()
    FLOW = auto()
    FLY = auto()
    FOCUS = auto()
    FOLD = auto()
    FOLLOW = auto()
    FORCE = auto()
    FORGET = auto()
    FORGIVE = auto()
    FORM = auto()
    # FOUND = auto() # 創立
    FREEZE = auto()
    FRIGHTEN = auto()
    FROWN = auto()
    FRY = auto()
    FULFILL = auto()
    GAIN = auto()
    GATHER = auto()
    GAZE = auto()
    GET = auto()
    GIVE = auto()
    GLAD = auto()
    GLANCE = auto()
    GLOW = auto()
    GO = auto()
    GOVERN = auto()
    GRADUATE = auto()
    GREET = auto()
    GRIN = auto()
    GROW = auto()
    GROWL = auto() # 唸る
    GUARANTEE = auto()
    GUARD = auto()
    GUESS = auto()
    GUIDE = auto()
    HAND = auto()
    HANDLE = auto()
    HANG = auto()
    HAPPEN = auto()
    HAPPY = auto()
    HARVEST = auto()
    HATE = auto()
    HAVE = auto()
    HEAD = auto()
    HEAL = auto()
    HEAR = auto()
    HELP = auto()
    HESITATE = auto()
    HIDE = auto()
    HIRE = auto()
    HIT = auto()
    HOLD = auto()
    HOP = auto()
    HUG = auto()
    HUNT = auto()
    HOPE = auto()
    HURT = auto()
    HURRY = auto()
    IDENTIFY = auto()
    IGNORE = auto()
    ILLUSTRATE = auto()
    IMAGINE = auto()
    IMPLY = auto()
    IMPRESS = auto()
    IMPORT = auto()
    IMPOSE = auto()
    IMPROVE = auto()
    INCLUDE = auto()
    INCREASE = auto()
    INDICATE = auto()
    INFLUENCE = auto()
    INFORM = auto()
    INHERIT = auto()
    INJURE = auto()
    INSIST = auto()
    INSPIRE = auto()
    INSTALL = auto()
    INSTRUCT = auto()
    INSTRUMENT = auto()
    INSULT = auto()
    INTEND = auto()
    INTERFERE = auto()
    INTERPRET = auto()
    INTERRUPT = auto()
    INTRODUCE = auto()
    INVADE = auto()
    INVENT = auto()
    INVEST = auto()
    INVESTIGATE = auto()
    INVITE = auto()
    INVOLVE = auto()
    ISSUE = auto()
    JOG = auto()
    JOIN = auto()
    JUDGE = auto()
    JUMP = auto()
    JUSTIFY = auto()
    KEEP = auto()
    KEYBOARD = auto()
    KICK = auto()
    KILL = auto()
    KISS = auto()
    KNIT = auto()
    KNOCK = auto()
    KNOW = auto()
    LAND = auto()
    # LAST = auto() # 続く、足りる、生き続ける
    LAUGH = auto()
    LAUNCH = auto()
    LAY = auto()
    LEAD = auto()
    LEAN = auto()
    LEAP = auto()
    LEARN = auto()
    LEAVE = auto()
    LEND = auto()
    LET = auto()
    LIE = auto()
    LIFE = auto()
    LIFT = auto()
    LIGHT = auto()
    LIKE = auto()
    LINE = auto()
    LISTEN = auto()
    LIVE = auto()
    LOAD = auto()
    LOAN = auto()
    LOCK = auto()
    LOOK = auto()
    LOOKDOWN = auto()
    LOSE = auto()
    LOVE = auto()
    MAINTAIN = auto()
    MAKE = auto()
    MAKEUP = auto()
    MANAGE = auto()
    MANUFACTURE = auto()
    MAON = auto()
    MARK = auto()
    MARRY = auto()
    MARVEL = auto()
    MASTER = auto()
    MATCH = auto()
    MATTER = auto()
    MEAN = auto()
    MEASURE = auto()
    MEET = auto()
    MELT = auto()
    MEMO = auto()
    MEND = auto()
    MENTION = auto()
    MIND = auto()
    MISS = auto()
    MISUNDERSTAND = auto()
    MIX = auto()
    MODIFY = auto()
    MONITOR = auto()
    MOUNT = auto()
    MOVE = auto()
    MULTIPLY = auto()
    MUST = auto()
    NEED = auto()
    NEGLECT = auto()
    NOD = auto()
    NOTE = auto()
    NOTICE = auto()
    OBEY = auto()
    OBJECT = auto()
    OBSERVE = auto()
    OBTAIN = auto()
    OCCUPY = auto()
    OCCUR = auto()
    OFFEND = auto()
    OFFER = auto()
    OPEN = auto()
    OPERATE = auto()
    OPPOSE = auto()
    ORGANIZE = auto()
    OVERCOME = auto()
    OVERFLOW = auto()
    OVERLOOK = auto()
    OWE = auto()
    OWN = auto()
    PACK = auto()
    PAINT = auto()
    PARK = auto()
    PARTICIPATE = auto()
    PASS = auto()
    PAT = auto()
    PAUSE = auto()
    PAY = auto()
    PERCEIVE = auto()
    PERFORM = auto()
    PERMIT = auto()
    PERSUADE = auto()
    PHONE = auto()
    PICK = auto()
    PITY = auto()
    PLACE = auto()
    PLANT = auto()
    PLAY = auto()
    PLEASE = auto()
    PLUNGE = auto()
    POINT = auto()
    POP = auto()
    POSE = auto()
    POSSESS = auto()
    POSTPONE = auto()
    POUR = auto()
    PRACTICE = auto()
    PRAISE = auto()
    PRAY = auto()
    PREDICT = auto()
    PREFER = auto()
    PREPARE = auto()
    PRESENT = auto()
    PRESERVE = auto()
    PRESS = auto()
    PRETEND = auto()
    PREVENT = auto()
    PRINT = auto()
    PROCEED = auto()
    PRODUCE = auto()
    PROFESS = auto()
    PROMISE = auto()
    PROMOTE = auto()
    PROMPT = auto()
    PRONOUNCE = auto()
    PROPOSE = auto()
    PROTECT = auto()
    PROTEST = auto()
    PROVE = auto()
    PROVIDE = auto()
    PUBLISH = auto()
    PULL = auto()
    PUNCH = auto()
    PUNISH = auto()
    PURCHASE = auto()
    PURSUE = auto()
    PUSH = auto()
    PUT = auto()
    PUZZLE = auto()
    QUATE = auto()
    QUIT = auto()
    RAISE = auto()
    RANGE = auto()
    REACH = auto()
    REACT = auto()
    READ = auto()
    REALIZE = auto()
    REBEL = auto()
    RECALL = auto()
    RECEIVE = auto()
    RECKON = auto()
    RECOGNZE = auto()
    RECOLLECT = auto()
    RECOMMEND = auto()
    RECOVER = auto()
    REDUCE = auto()
    REFER = auto()
    REFLECT = auto()
    REFORM = auto()
    REFRESH = auto()
    REFUSE = auto()
    REGARD = auto()
    REGRET = auto()
    REJECT = auto()
    RELATE = auto()
    RELAX = auto()
    RELAY = auto()
    RELEASE = auto()
    RELY = auto()
    REMAIN = auto()
    REMARK = auto()
    REMEMBER = auto()
    REMIND = auto()
    REMOVE = auto()
    RENT = auto()
    REPAIR = auto()
    REPEAT = auto()
    REPLACE = auto()
    REPLY = auto()
    REPORT = auto()
    REPRESENT = auto()
    REQUEST = auto()
    RESCUE = auto()
    RESEMBLE = auto()
    RESIST = auto()
    RESOLVE = auto()
    RESPOND = auto()
    REST = auto()
    RESTORE = auto()
    RETRICT = auto()
    RETURN = auto()
    REQUIRE = auto()
    RESERVE = auto()
    RESPECT = auto()
    RESULT = auto()
    RETIRE = auto()
    REVEAL = auto()
    REVIEW = auto()
    REWARD = auto()
    RID = auto()
    RIDE = auto()
    RING = auto()
    RISE = auto()
    ROB = auto()
    ROCK = auto()
    ROLL = auto()
    ROW = auto()
    RUB = auto()
    RUIN = auto()
    RULE = auto()
    RUN = auto()
    RUSH = auto()
    SACRIFICE = auto()
    SAD = auto()
    SAIL = auto()
    SATISFY = auto()
    SAVE = auto()
    SAY = auto()
    SCARE = auto()
    SCATTER = auto()
    SCOLD = auto()
    SCRATCH = auto()
    SCREAM = auto()
    SEAL = auto()
    SEARCH = auto()
    SEAT = auto()
    SECURE = auto()
    SEE = auto()
    SEEK = auto()
    SEEM = auto()
    SEIZE = auto()
    SELECT = auto()
    SELL = auto()
    SEND = auto()
    SEPARATE = auto()
    SERVE = auto()
    SET = auto()
    SETTLE = auto()
    SHAKE = auto()
    SHARE = auto()
    SHIFT = auto()
    SHINE = auto()
    SHOCK = auto()
    SHOOT = auto()
    SHOP = auto()
    SHOUT = auto()
    SHOW = auto()
    SHRUG = auto()
    SHUT = auto()
    SIGH = auto()
    SIGN = auto()
    SING = auto()
    SINK = auto()
    SIT = auto()
    SKATE = auto()
    SKIP = auto()
    SLEEP = auto()
    SLICE = auto()
    SLIDE = auto()
    SLIP = auto()
    SLOBBER = auto()
    SMASH = auto()
    SMELL = auto()
    SMILE = auto()
    SMOKE = auto()
    SNAP = auto()
    SOLVE = auto()
    SOUND = auto()
    SPARE = auto()
    SPECIALIZE = auto()
    SPEAK = auto()
    SPEND = auto()
    SPILL = auto()
    SPIN = auto()
    SPLIT = auto()
    SPOIL = auto()
    SPREAD = auto()
    SQUEEZE = auto()
    STAND = auto()
    STARE = auto()
    START = auto()
    STARVE = auto()
    # STATE = auto # 明言する
    STAY = auto()
    STEAL = auto()
    STICK = auto()
    STIMULATE = auto()
    STIR = auto()
    STOP = auto()
    STORE = auto()
    STRAIN = auto()
    STRESS = auto()
    STRETCH = auto()
    STRIKE = auto()
    STRUGGLE = auto()
    STUDY = auto()
    SUBMIT = auto()
    SUBSCRIBE = auto()
    SUCCEED = auto()
    SUCK = auto()
    SUFFER = auto()
    SUGGEST = auto()
    SUIT = auto()
    SUPPLY = auto()
    SUPPORT = auto()
    SUPPOSE = auto()
    SURPRISE = auto()
    SURROUND = auto()
    SURVIVE = auto()
    SUSPECT = auto()
    SUSPEND = auto()
    SWEAR = auto()
    SWEEP = auto()
    SWIM = auto()
    SWING = auto()
    SWITCH = auto()
    SWORD = auto()
    TAKE = auto()
    TALK = auto()
    TAP = auto()
    TEACH = auto()
    TEND = auto()
    TEAR = auto()
    TELL = auto()
    TEST = auto()
    THANK = auto()
    THINK = auto()
    THREATEN = auto()
    THROW = auto()
    TIE = auto()
    TOSS = auto()
    TOUCH = auto()
    TRAVEL = auto()
    TRAIN = auto()
    TRANSFER = auto()
    TRANSFORM = auto()
    TRANSLATE = auto()
    TRANSPORT = auto()
    TREAT = auto()
    TRIP = auto()
    TRUST = auto()
    TRY = auto()
    TURN = auto()
    TWIST = auto()
    TYPE = auto()
    UNDERGO = auto()
    UNDERLINE = auto()
    UNDERSTAND = auto()
    UNITE = auto()
    UNLOCK = auto()
    URGE = auto()
    UPSET = auto()
    USE = auto()
    VANISH = auto()
    VARY = auto()
    VIEW = auto()
    VISIT = auto()
    VOTE = auto()
    WAIT = auto()
    WAKE = auto()
    WALK = auto()
    WANT = auto()
    WARM = auto()
    WARN = auto()
    WASTE = auto()
    WATCH = auto()
    WAVE = auto()
    WEAKEN = auto()
    WEAR = auto()
    WEIGH = auto()
    WELCOME = auto()
    WHIP = auto()
    WHISPER = auto()
    WHISTLE = auto()
    WIN = auto()
    WIND = auto()
    WIPE = auto()
    WISH = auto()
    WITHDRAW = auto()
    WONDER = auto()
    WORK = auto()
    WORRY = auto()
    WOUND = auto()
    WRAP = auto()
    WRITE = auto()
    WRY = auto()
    YAWN = auto()
    YELL = auto()

    def __str__(self) -> str:
        return {
                self.ABANDON.value: "放棄",
                self.ABSORB.value: "吸収",
                self.ABUSE.value: "悪用",
                self.ACCEPT.value: "受け取る",
                self.ACCOMPANY.value: "同行",
                self.ACCORD.value: "一致",
                self.ACCOUNT.value: "見做す",
                self.ACCUSE.value: "訴える",
                self.ACHIEVE.value: "達成",
                self.ACQUIRE.value: "得る",
                self.ACT.value: "行動",
                self.ADD.value: "加える",
                self.ADDRESS.value: "宛てる",
                self.ADHERE.value: "付く",
                self.ADJUST.value: "調整",
                self.ADMIRE.value: "憧れ",
                self.ADMIT.value: "認める",
                self.ADOPT.value: "採用",
                self.ADVANCE.value: "進める",
                self.ADVERTISE.value: "宣伝",
                self.ADVISE.value: "助言",
                self.AFFECT.value: "影響",
                self.AFFORD.value: "与える",
                self.AGREE.value: "賛成",
                self.AID.value: "援助",
                self.AIM.value: "向ける",
                self.ALLEGE.value: "言い張る",
                self.ALLOW.value: "許す",
                self.ALTER.value: "変える",
                self.ANGRY.value: "怒る",
                self.ANNOUNCE.value: "知らせる",
                self.ANNOY.value: "苛つかせる",
                self.ANSWER.value: "答える",
                self.ANTICIPATE.value: "見込む",
                self.APOLOGIZE.value: "謝る",
                self.APPEAL.value: "哀願",
                self.APPEAR.value: "現れる",
                self.APPLY.value: "当てる",
                self.APPOINT.value: "指名する",
                self.APPRICIATE.value: "感謝",
                self.APPROACH.value: "接近",
                self.APPROVE.value: "承認",
                self.ARGUE.value: "論じる",
                self.ARRANGE.value: "整える",
                self.ARREST.value: "逮捕",
                self.ARRIVE.value: "着く",
                self.ASK.value: "尋ねる",
                self.ASSIST.value: "支援",
                self.ASSUME.value: "思い込む",
                self.ASSURE.value: "請け負う",
                self.ATTACH.value: "取り付ける",
                self.ATTACK.value: "攻撃",
                self.ATTEMPT.value: "試みる",
                self.ATTEND.value: "出席",
                self.ATTRACT.value: "引きつける",
                self.AVOID.value: "避ける",
                self.AWARD.value: "授与",
                self.BAKE.value: "焼く",
                self.BAN.value: "禁じる",
                self.BASE.value: "基礎",
                self.BE.value: "である",
                self.BEAR.value: "露出",
                self.BEAT.value: "叩く",
                self.BECOME.value: "なる",
                self.BEG.value: "乞う",
                self.BEGIN.value: "始める",
                self.BEHAVE.value: "振る舞う",
                self.BELIEVE.value: "信じる",
                self.BELONG.value: "所属",
                self.BEND.value: "曲げる",
                self.BET.value: "賭ける",
                self.BETRAY.value: "裏切る",
                self.BID.value: "提示",
                self.BIND.value: "縛る",
                self.BITE.value: "噛む",
                self.BLAME.value: "非難",
                self.BLEED.value: "出血",
                self.BLEND.value: "混ぜる",
                self.BLESS.value: "祝福",
                self.BLOCK.value: "妨害",
                self.BLOW.value: "吹く",
                self.BOAST.value: "自慢",
                self.BOIL.value: "茹でる",
                self.BORE.value: "うんざり",
                self.BORROW.value: "借りる",
                self.BOTHER.value: "煩わす",
                self.BOUND.value: "束縛",
                self.BOW.value: "お辞儀",
                self.BREAK.value: "壊す",
                self.BREATHE.value: "呼吸",
                self.BRING.value: "持ち運ぶ",
                self.BROW.value: "眉を顰める",
                self.BUILD.value: "建てる",
                self.BURN.value: "燃やす",
                self.BURST.value: "弾ける",
                self.BURY.value: "埋葬",
                self.BUY.value: "買う",
                self.CALCULATE.value: "計算",
                self.CALL.value: "呼ぶ",
                self.CANCEL.value: "取り消す",
                self.CAPTURE.value: "捕らえる",
                self.CARE.value: "気にする",
                self.CARRY.value: "運ぶ",
                self.CAST.value: "投げる",
                self.CATCH.value: "捕まえる",
                self.CAUSE.value: "原因",
                self.CEASE.value: "止める",
                self.CELEBRATE.value: "祝う",
                self.CHANGE.value: "変える",
                self.CHARGE.value: "請求",
                self.CHARM.value: "魅了",
                self.CHASE.value: "追う",
                self.CHEAT.value: "騙す",
                self.CHECK.value: "確認",
                self.CHEER.value: "応援",
                self.CHEW.value: "噛む",
                self.CHOOSE.value: "選ぶ",
                self.CHOP.value: "切り刻む",
                self.CLAIM.value: "クレーム",
                self.CLEAN.value: "掃除",
                self.CLICK.value: "クリック",
                self.CLIMB.value: "登る",
                self.CLING.value: "しがみつく",
                self.CLIP.value: "刈る",
                self.CLOSE.value: "閉じる",
                self.CLOTHE.value: "着せる",
                self.COACH.value: "指導",
                self.COLLAPSE.value: "崩れる",
                self.COLLECT.value: "集める",
                self.COMBINE.value: "組み合わせる",
                self.COME.value: "来る",
                self.COMFORT.value: "励ます",
                self.COMMAND.value: "命令",
                self.COMMIT.value: "委託",
                self.COMMUNICATE.value: "伝達",
                self.COMPARE.value: "比べる",
                self.COMPETE.value: "争う",
                self.COMPLAIN.value: "文句",
                self.COMPLETE.value: "完遂",
                self.COMPOSE.value: "組み立てる",
                self.CONCEIVE.value: "思いつく",
                self.CONCENTRATE.value: "集中",
                self.CONCERN.value: "関心",
                self.CONCLUDE.value: "締め括る",
                self.CONDUCT.value: "指揮",
                self.CONFESS.value: "告白",
                self.CONFIRM.value: "確かめる",
                self.CONFRONT.value: "直面",
                self.CONFUSE.value: "混乱",
                self.CONNECT.value: "繋ぐ",
                self.CONSIDER.value: "熟考",
                self.CONSIST.value: "成り立つ",
                self.CONSTRUCT.value: "組み立てる",
                self.CONSUME.value: "消費",
                self.CONTACT.value: "連絡",
                self.CONTAIN.value: "含む",
                self.CONTINUE.value: "続く",
                self.CONTRIBUTE.value: "貢献",
                self.CONTROL.value: "操作",
                self.CONVERT.value: "転換",
                self.CONVEY.value: "搬送",
                self.CONVINCE.value: "納得させる",
                self.COOK.value: "料理",
                self.COOL.value: "格好良い",
                self.COOPERATE.value: "協力",
                self.COPE.value: "対処",
                self.COPY.value: "コピィ",
                self.CORRECT.value: "正しい",
                self.COST.value: "費やす",
                self.COUGH.value: "咳",
                self.COUNT.value: "数える",
                self.COUNTER.value: "反撃",
                self.COVER.value: "覆う",
                self.CRACK.value: "割れる",
                self.CRASH.value: "衝突",
                self.CRAWL.value: "這う",
                self.CREATE.value: "創る",
                self.CRITICIZE.value: "批判",
                self.CROSS.value: "渡る",
                self.CRUSH.value: "潰れる",
                self.CRY.value: "叫ぶ",
                self.CURE.value: "治す",
                self.CURL.value: "カール",
                self.CUT.value: "切る",
                self.DAMAGE.value: "損傷",
                self.DANCE.value: "踊る",
                self.DARE.value: "敢えてする",
                self.DEAL.value: "扱う",
                self.DECAY.value: "腐る",
                self.DECIDE.value: "決める",
                self.DECLARE.value: "宣言",
                self.DECLINE.value: "断る",
                self.DECORATE.value: "飾る",
                self.DECREASE.value: "減る",
                self.DEFEAT.value: "負かす",
                self.DEFEND.value: "守る",
                self.DEFINE.value: "定義",
                self.DELAY.value: "遅らせる",
                self.DELIVER.value: "届ける",
                self.DEMONSTRATE: "証明",
                self.DENY.value: "拒む",
                self.DEPEND.value: "頼る",
                self.DEPOSITE.value: "預ける",
                self.DERIVE.value: "由来",
                self.DESCEND.value: "下りる",
                self.DESCRIBE.value: "述べる",
                self.DESERT.value: "去る",
                self.DESERVE.value: "価値がある",
                self.DESIRE.value: "欲求",
                self.DESTROY.value: "破壊",
                self.DETERMINE.value: "決意",
                self.DEVELOP.value: "開発",
                self.DEVISE.value: "考案",
                self.DEVOTE.value: "捧げる",
                self.DIAL.value: "ダイヤル",
                self.DIE.value: "死ぬ",
                self.DIG.value: "掘る",
                self.DIGEST.value: "消化",
                self.DISAPPEAR.value: "消える",
                self.DISAPPOINT.value: "失望",
                self.DISAPPROVE.value: "不可",
                self.DISCHARGE.value: "排出",
                self.DISCOVER.value: "発見",
                self.DISCUSS.value: "話し合う",
                self.DISGUISE.value: "変装",
                self.DISGUST.value: "嫌気",
                self.DISLIKE.value: "嫌う",
                self.DISMISS.value: "解散",
                self.DISPEL.value: "晴らす",
                self.DISPLAY.value: "表示",
                self.DISTINGUISH.value: "見分ける",
                self.DISTRIBUTE.value: "配る",
                self.DO.value: "する",
                self.DOMINATE.value: "支配",
                self.DOUBT.value: "疑う",
                self.DRAG.value: "引きずる",
                self.DRAW.value: "描く",
                self.DREAM.value: "夢見る",
                self.DRESS.value: "着飾る",
                self.DRIFT.value: "漂う",
                self.DRIVE.value: "運転",
                self.DROP.value: "落ちる",
                self.DROWN.value: "濡らす",
                self.DRY.value: "乾く",
                self.EARN.value: "儲ける",
                self.EASE.value: "和らぐ",
                self.EAT.value: "食べる",
                self.EDUCATE.value: "教育",
                self.ELECT.value: "選ぶ",
                self.ELIMINATE.value: "省く",
                self.EMAIL.value: "メール",
                self.EMBARRASS.value: "辱める",
                self.EMERGE.value: "浮上",
                self.EMPHASIZE.value: "力説",
                self.EMPLOY.value: "雇う",
                self.ENABLE.value: "可能",
                self.ENCOUNTER.value: "出遭う",
                self.ENCOURAGE.value: "勇気づける",
                self.END.value: "終わる",
                self.ENDURE.value: "耐える",
                self.ENGAGE.value: "従事する",
                self.ENJOY.value: "楽しむ",
                self.ENSURE.value: "確保",
                self.ENTER.value: "入る",
                self.ENTERTAIN.value: "楽しませる",
                self.ENVY.value: "恨む",
                self.EQUIP.value: "装備",
                self.ESCAPE.value: "逃げる",
                self.ESTABLISH.value: "設立",
                self.ESTIMATE.value: "見積もる",
                self.EXAMINE.value: "試験",
                self.EXCHANGE.value: "交換",
                self.EXCITE.value: "興奮",
                self.EXCUSE.value: "許す",
                self.EXHAUST.value: "使い果たす",
                self.EXHIBIT.value: "展示",
                self.EXIST.value: "存在",
                self.EXPAND.value: "広げる",
                self.EXPECT.value: "期待",
                self.EXPLAIN.value: "説明",
                self.EXPLODE.value: "爆発",
                self.EXPLORE.value: "探る",
                self.EXPORT.value: "輸出",
                self.EXPOSE.value: "晒す",
                self.EXPRESS.value: "表す",
                self.EXTEND.value: "延ばす",
                self.FACE.value: "顔を合わせる",
                self.FAIL.value: "失敗",
                self.FALL.value: "落ちる",
                self.FASTEN.value: "留める",
                self.FEED.value: "餌を与える",
                self.FEEL.value: "感じる",
                self.FIB.value: "嘘",
                self.FIGHT.value: "戦う",
                self.FILL.value: "満たす",
                self.FIND.value: "見つける",
                self.FINISH.value: "終わる",
                self.FIRE.value: "火を点ける",
                self.FIREJOB.value: "首にする",
                self.FIT.value: "合う",
                self.FIX.value: "直す",
                self.FLASH.value: "輝く",
                self.FLEE.value: "逃げる",
                self.FLOAT.value: "浮かぶ",
                self.FLOW.value: "流れる",
                self.FLY.value: "飛ぶ",
                self.FOCUS.value: "注目",
                self.FOLD.value: "折る",
                self.FOLLOW.value: "従う",
                self.FORCE.value: "強要",
                self.FORGET.value: "忘れる",
                self.FORGIVE.value: "許す",
                self.FORM.value: "形成",
                self.FREEZE.value: "凍らす",
                self.FRIGHTEN.value: "驚かす",
                self.FROWN.value: "睨む",
                self.FRY.value: "揚げる",
                self.FULFILL.value: "果たす",
                self.GAIN.value: "増加",
                self.GATHER.value: "集める",
                self.GAZE.value: "見つめる",
                self.GET.value: "得る",
                self.GIVE.value: "与える",
                self.GLAD.value: "喜ぶ",
                self.GLANCE.value: "一瞥",
                self.GLOW.value: "白熱",
                self.GO.value: "行く",
                self.GOVERN.value: "統治",
                self.GRADUATE.value: "卒業",
                self.GREET.value: "挨拶",
                self.GRIN.value: "にっこり",
                self.GROW.value: "育つ",
                self.GROWL.value: "唸る",
                self.GUARANTEE.value: "保証",
                self.GUARD.value: "守る",
                self.GUESS.value: "思う",
                self.GUIDE.value: "案内",
                self.HAND.value: "握る",
                self.HANDLE.value: "操作",
                self.HANG.value: "掴む",
                self.HAPPEN.value: "起こる",
                self.HAPPY.value: "幸せ",
                self.HARVEST.value: "収穫",
                self.HATE.value: "憎む",
                self.HAVE.value: "持つ",
                self.HEAD.value: "進む",
                self.HEAL.value: "癒やす",
                self.HEAR.value: "聞く",
                self.HELP.value: "助ける",
                self.HESITATE.value: "躊躇う",
                self.HIDE.value: "隠す",
                self.HIRE.value: "雇う",
                self.HIT.value: "打つ",
                self.HOLD.value: "掴む",
                self.HOP.value: "跳ぶ",
                self.HOPE.value: "望む",
                self.HUG.value: "抱く",
                self.HUNT.value: "狩る",
                self.HURRY.value: "急ぐ",
                self.HURT.value: "傷つける",
                self.IDENTIFY.value: "見分ける",
                self.IGNORE.value: "無視",
                self.ILLUSTRATE.value: "例える",
                self.IMAGINE.value: "想像",
                self.IMPLY.value: "仄めかす",
                self.IMPORT.value: "輸入",
                self.IMPOSE.value: "課す",
                self.IMPRESS.value: "印象",
                self.IMPROVE.value: "改善",
                self.INCLUDE.value: "含む",
                self.INCREASE.value: "増える",
                self.INDICATE.value: "示す",
                self.INFLUENCE.value: "影響",
                self.INFORM.value: "告げる",
                self.INHERIT.value: "受け継ぐ",
                self.INJURE.value: "負傷",
                self.INSIST.value: "言い張る",
                self.INSPIRE.value: "激励",
                self.INSTALL.value: "インストール",
                self.INSTRUCT.value: "指示",
                self.INSTRUMENT.value: "演奏",
                self.INSULT.value: "侮辱",
                self.INTEND.value: "意図",
                self.INTERFERE.value: "干渉",
                self.INTERPRET.value: "解釈",
                self.INTERRUPT.value: "割り込む",
                self.INTRODUCE.value: "紹介",
                self.INVADE.value: "侵す",
                self.INVENT.value: "考案",
                self.INVEST.value: "投資",
                self.INVESTIGATE.value: "捜査",
                self.INVITE.value: "招く",
                self.INVOLVE.value: "巻き込む",
                self.ISSUE.value: "生じる",
                self.JOG.value: "ジョギング",
                self.JOIN.value: "加わる",
                self.JUDGE.value: "審判",
                self.JUMP.value: "ジャンプ",
                self.JUSTIFY.value: "正当化",
                self.KEEP.value: "保つ",
                self.KEYBOARD.value: "キーボード",
                self.KICK.value: "蹴る",
                self.KILL.value: "殺す",
                self.KISS.value: "キス",
                self.KNIT.value: "編む",
                self.KNOCK.value: "ノック",
                self.KNOW.value: "知る",
                self.LAND.value: "上陸",
                self.LAUGH.value: "笑う",
                self.LAUNCH.value: "打ち上げ",
                self.LAY.value: "横たえる",
                self.LEAD.value: "先導",
                self.LEAN.value: "傾く",
                self.LEAP.value: "跳躍",
                self.LEARN.value: "学ぶ",
                self.LEAVE.value: "残る",
                self.LEND.value: "貸す",
                self.LET.value: "させる",
                self.LIE.value: "横たわる",
                self.LIFE.value: "暮らす",
                self.LIFT.value: "持ち上げる",
                self.LIGHT.value: "明かりを点ける",
                self.LIKE.value: "好き",
                self.LINE.value: "線を引く",
                self.LISTEN.value: "聴く",
                self.LIVE.value: "生きる",
                self.LOAD.value: "導く",
                self.LOAN.value: "貸付",
                self.LOCK.value: "鍵を掛ける",
                self.LOOK.value: "見る",
                self.LOOKDOWN.value: "見下ろす",
                self.LOSE.value: "失う",
                self.LOVE.value: "愛す",
                self.MAINTAIN.value: "維持",
                self.MAKE.value: "作る",
                self.MAKEUP.value: "化粧",
                self.MANAGE.value: "管理",
                self.MANUFACTURE.value: "造る",
                self.MAON.value: "呻く",
                self.MARK.value: "印",
                self.MARRY.value: "結婚",
                self.MARVEL.value: "驚嘆",
                self.MASTER.value: "習得",
                self.MATCH.value: "合う",
                self.MATTER.value: "問題",
                self.MEAN.value: "意味",
                self.MEASURE.value: "測る",
                self.MEET.value: "会う",
                self.MELT.value: "溶ける",
                self.MEMO.value: "メモ",
                self.MEND.value: "繕う",
                self.MENTION.value: "述べる",
                self.MIND.value: "心がける",
                self.MISS.value: "ミス",
                self.MISUNDERSTAND.value: "誤解",
                self.MIX.value: "混ぜる",
                self.MODIFY.value: "修正",
                self.MONITOR.value: "監視",
                self.MOUNT.value: "登る",
                self.MOVE.value: "動く",
                self.MULTIPLY.value: "掛ける",
                self.MUST.value: "義務",
                self.NEED.value: "必要",
                self.NEGLECT.value: "怠る",
                self.NOD.value: "会釈",
                self.NONE.value: "ない",
                self.NOTE.value: "ノート",
                self.NOTICE.value: "気づく",
                self.OBEY.value: "服従",
                self.OBJECT.value: "異議",
                self.OBSERVE.value: "観察",
                self.OBTAIN.value: "入手",
                self.OCCUPY.value: "占める",
                self.OCCUR.value: "起こる",
                self.OFFEND.value: "怒らせる",
                self.OFFER.value: "申し出る",
                self.OPEN.value: "開く",
                self.OPERATE.value: "手術",
                self.OPPOSE.value: "対抗",
                self.ORGANIZE.value: "組織",
                self.OVERCOME.value: "打ち勝つ",
                self.OVERFLOW.value: "はみ出る",
                self.OVERLOOK.value: "見落とす",
                self.OWE.value: "負う",
                self.OWN.value: "所有",
                self.PACK.value: "梱包",
                self.PAINT.value: "塗る",
                self.PARK.value: "駐車",
                self.PARTICIPATE.value: "携わる",
                self.PASS.value: "通る",
                self.PAT.value: "叩く",
                self.PAUSE.value: "休む",
                self.PAY.value: "支払う",
                self.PERCEIVE.value: "気づく",
                self.PERFORM.value: "演じる",
                self.PERMIT.value: "許す",
                self.PERSUADE.value: "説得",
                self.PHONE.value: "電話",
                self.PICK.value: "摘む",
                self.PITY.value: "憐れむ",
                self.PLACE.value: "置く",
                self.PLANT.value: "植える",
                self.PLAY.value: "遊ぶ",
                self.PLEASE.value: "喜び",
                self.PLUNGE.value: "突っ込む",
                self.POINT.value: "指す",
                self.POP.value: "鳴る",
                self.POSE.value: "ポーズを取る",
                self.POSSESS.value: "所有",
                self.POSTPONE.value: "後回し",
                self.POUR.value: "注ぐ",
                self.PRACTICE.value: "練習",
                self.PRAISE.value: "賛美",
                self.PRAY.value: "祈る",
                self.PREDICT.value: "占う",
                self.PREFER.value: "好む",
                self.PREPARE.value: "備える",
                self.PRESENT.value: "贈る",
                self.PRESERVE.value: "保存",
                self.PRESS.value: "押す",
                self.PRETEND.value: "偽る",
                self.PREVENT.value: "予防",
                self.PRINT.value: "印刷",
                self.PROCEED.value: "続行",
                self.PRODUCE.value: "生み出す",
                self.PROFESS.value: "公言",
                self.PROMISE.value: "約束",
                self.PROMOTE.value: "促進",
                self.PROMPT.value: "促す",
                self.PRONOUNCE.value: "発音",
                self.PROPOSE.value: "申し込む",
                self.PROTECT.value: "防ぐ",
                self.PROTEST.value: "断言",
                self.PROVE.value: "証明",
                self.PROVIDE.value: "供給",
                self.PUBLISH.value: "出版",
                self.PULL.value: "引く",
                self.PUNCH.value: "殴る",
                self.PUNISH.value: "罰する",
                self.PURCHASE.value: "購入",
                self.PURSUE.value: "追跡",
                self.PUSH.value: "押す",
                self.PUT.value: "置く",
                self.PUZZLE.value: "困らせる",
                self.QUATE.value: "引用",
                self.QUIT.value: "止める",
                self.RAISE.value: "上げる",
                self.RANGE.value: "及ぶ",
                self.REACH.value: "届く",
                self.REACT.value: "反応",
                self.READ.value: "読む",
                self.REALIZE.value: "気がつく",
                self.REBEL.value: "反逆",
                self.RECALL.value: "撤回",
                self.RECEIVE.value: "受け取る",
                self.RECKON.value: "数える",
                self.RECOGNZE.value: "認める",
                self.RECOLLECT.value: "回想",
                self.RECOMMEND.value: "勧める",
                self.RECOVER.value: "取り戻す",
                self.REDUCE.value: "減らす",
                self.REFER.value: "参照",
                self.REFLECT.value: "反射",
                self.REFORM.value: "改正",
                self.REFRESH.value: "爽やか",
                self.REFUSE.value: "断る",
                self.REGARD.value: "注視",
                self.REGRET.value: "後悔",
                self.REJECT.value: "却下",
                self.RELATE.value: "似る",
                self.RELAX.value: "くつろぐ",
                self.RELAY.value: "中継",
                self.RELEASE.value: "離す",
                self.RELY.value: "頼る",
                self.REMAIN.value: "残る",
                self.REMARK.value: "感想",
                self.REMEMBER.value: "思い出す",
                self.REMIND.value: "思い出させる",
                self.REMOVE.value: "削除",
                self.RENT.value: "賃借",
                self.REPAIR.value: "修繕",
                self.REPEAT.value: "繰り返す",
                self.REPORT.value: "報告",
                self.REPRESENT.value: "代表",
                self.REQUEST.value: "要求",
                self.REQUIRE.value: "必要",
                self.RESCUE.value: "救護",
                self.RESEMBLE.value: "似る",
                self.RESERVE.value: "予約",
                self.RESIST.value: "抵抗",
                self.RESOLVE.value: "解く",
                self.RESPECT.value: "尊敬",
                self.RESPOND.value: "応じる",
                self.REST.value: "休む",
                self.RESTORE.value: "復元",
                self.RESULT.value: "結果",
                self.RETIRE.value: "引退",
                self.RETRICT.value: "制限",
                self.RETURN.value: "戻る",
                self.REVEAL.value: "漏らす",
                self.REVIEW.value: "見直す",
                self.REWARD.value: "報いる",
                self.RID.value: "除去",
                self.RIDE.value: "乗る",
                self.RING.value: "鳴る",
                self.RISE.value: "立ち上がる",
                self.ROB.value: "奪う",
                self.ROCK.value: "揺れる",
                self.ROLL.value: "転がる",
                self.ROW.value: "並べる",
                self.RUB.value: "擦る",
                self.RUIN.value: "荒廃",
                self.RULE.value: "裁定",
                self.RUN.value: "走る",
                self.RUSH.value: "急ぐ",
                self.SACRIFICE.value: "犠牲",
                self.SAD.value: "悲しむ",
                self.SAIL.value: "航海",
                self.SATISFY.value: "満たす",
                self.SAVE.value: "セーブ",
                self.SAY.value: "言う",
                self.SCARE.value: "怯える",
                self.SCATTER.value: "散る",
                self.SCOLD.value: "叱る",
                self.SCRATCH.value: "引っ掻く",
                self.SCREAM.value: "叫び声",
                self.SEAL.value: "封印",
                self.SEARCH.value: "探す",
                self.SEAT.value: "座らせる",
                self.SECURE.value: "確保",
                self.SEE.value: "見る",
                self.SEEK.value: "探す",
                self.SEEM.value: "思う",
                self.SEIZE.value: "握る",
                self.SELECT.value: "選ぶ",
                self.SELL.value: "売る",
                self.SEND.value: "送る",
                self.SEPARATE.value: "分ける",
                self.SERVE.value: "仕える",
                self.SET.value: "設定",
                self.SETTLE.value: "落ち着く",
                self.SHAKE.value: "振る",
                self.SHARE.value: "分ける",
                self.SHIFT.value: "移す",
                self.SHINE.value: "輝く",
                self.SHOCK.value: "ショック",
                self.SHOOT.value: "撃つ",
                self.SHOP.value: "買い物",
                self.SHOUT.value: "叫ぶ",
                self.SHOW.value: "見せる",
                self.SHRUG.value: "肩を竦める",
                self.SHUT.value: "閉める",
                self.SIGH.value: "溜息",
                self.SIGN.value: "サイン",
                self.SING.value: "歌う",
                self.SINK.value: "沈む",
                self.SIT.value: "座る",
                self.SKATE.value: "スケート",
                self.SKIP.value: "スキップ",
                self.SLEEP.value: "眠る",
                self.SLICE.value: "薄く切る",
                self.SLIDE.value: "滑る",
                self.SLIP.value: "転ぶ",
                self.SLOBBER.value: "涎を垂らす",
                self.SMASH.value: "粉砕",
                self.SMELL.value: "匂う",
                self.SMILE.value: "微笑",
                self.SMOKE.value: "煙草を吸う",
                self.SNAP.value: "鳴らす",
                self.SOLVE.value: "解く",
                self.SOUND.value: "音が鳴る",
                self.SPARE.value: "控える",
                self.SPEAK.value: "喋る",
                self.SPECIALIZE.value: "専門化",
                self.SPEND.value: "費やす",
                self.SPILL.value: "零す",
                self.SPIN.value: "紡ぐ",
                self.SPLIT.value: "分かれる",
                self.SPOIL.value: "駄目になる",
                self.SPREAD.value: "拡散",
                self.STAND.value: "立つ",
                self.STARE.value: "凝視",
                self.START.value: "開始",
                self.STARVE.value: "飢える",
                self.STAY.value: "留まる",
                self.STEAL.value: "盗む",
                self.STICK.value: "刺す",
                self.STIMULATE.value: "促す",
                self.STIR.value: "かき回す",
                self.STOP.value: "止める",
                self.STORE.value: "収める",
                self.STRAIN.value: "引っ張る",
                self.STRESS.value: "緊張",
                self.STRETCH.value: "伸び",
                self.STRIKE.value: "ぶつかる",
                self.STRUGGLE.value: "藻掻く",
                self.STUDY.value: "勉強",
                self.SUBMIT.value: "提示",
                self.SUBSCRIBE.value: "寄付",
                self.SUCCEED.value: "成功",
                self.SUCK.value: "吸う",
                self.SUFFER.value: "苦しむ",
                self.SUGGEST.value: "提案",
                self.SUIT.value: "相応しい",
                self.SUPPLY.value: "供給",
                self.SUPPOSE.value: "提案",
                self.SUPPORT.value: "サポート",
                self.SURPRISE.value: "驚かす",
                self.SURROUND.value: "囲む",
                self.SURVIVE.value: "生き残る",
                self.SUSPECT.value: "疑う",
                self.SUSPEND.value: "吊るす",
                self.SWEAR.value: "誓う",
                self.SWEEP.value: "掃く",
                self.SWIM.value: "泳ぐ",
                self.SWING.value: "振る",
                self.SWITCH.value: "スイッチ",
                self.SWORD.value: "剣を振るう",
                self.TAKE.value: "取る",
                self.TALK.value: "話す",
                self.TAP.value: "叩く",
                self.TEACH.value: "教える",
                self.TEAR.value: "破る",
                self.TELL.value: "台詞",
                self.TEND.value: "傾向",
                self.TEST.value: "テスト",
                self.THANK.value: "感謝",
                self.THINK.value: "考える",
                self.THREATEN.value: "脅かす",
                self.THROW.value: "投げる",
                self.TIE.value: "結ぶ",
                self.TOSS.value: "トス",
                self.TOUCH.value: "触れる",
                self.TRAIN.value: "訓練",
                self.TRANSFER.value: "移す",
                self.TRANSFORM.value: "変形",
                self.TRANSLATE.value: "翻訳",
                self.TRANSPORT.value: "輸送",
                self.TRAVEL.value: "旅行",
                self.TREAT.value: "扱う",
                self.TRIP.value: "旅する",
                self.TRUST.value: "信じる",
                self.TRY.value: "挑戦",
                self.TURN.value: "回る",
                self.TWIST.value: "捻る",
                self.TYPE.value: "分類",
                self.UNDERGO.value: "経験",
                self.UNDERLINE.value: "下線",
                self.UNDERSTAND.value: "理解",
                self.UNITE.value: "合わせる",
                self.UNLOCK.value: "鍵を開ける",
                self.UPSET.value: "ひっくり返す",
                self.URGE.value: "駆り立てる",
                self.USE.value: "使う",
                self.VANISH.value: "消える",
                self.VARY.value: "変える",
                self.VIEW.value: "見渡す",
                self.VISIT.value: "訪れる",
                self.VOTE.value: "投票",
                self.WAIT.value: "待つ",
                self.WAKE.value: "目覚める",
                self.WALK.value: "歩く",
                self.WANT.value: "欲しい",
                self.WARM.value: "温める",
                self.WARN.value: "警告",
                self.WASTE.value: "無駄",
                self.WATCH.value: "見る",
                self.WAVE.value: "うねる",
                self.WEAKEN.value: "弱める",
                self.WEAR.value: "着る",
                self.WEIGH.value: "計る",
                self.WELCOME.value: "歓迎",
                self.WHIP.value: "はためく",
                self.WHISPER.value: "囁く",
                self.WHISTLE.value: "囀る",
                self.WIN.value: "勝つ",
                self.WIND.value: "風",
                self.WIPE.value: "拭く",
                self.WISH.value: "願う",
                self.WITHDRAW.value: "取り下げる",
                self.WONDER.value: "不思議",
                self.WORK.value: "働く",
                self.WORRY.value: "心配",
                self.WOUND.value: "負傷",
                self.WRAP.value: "包む",
                self.WRITE.value: "書く",
                self.WRY.value: "嘲笑",
                self.YAWN.value: "欠伸",
                self.YAWN.value: "大声",
                }[self.value]

    def type_of(self) -> BehavType:
        return {
                self.ABANDON.value: BehavType.DONE,
                self.ABSORB.value: BehavType.DONE,
                self.ABUSE.value: BehavType.DONE,
                self.ACCEPT.value: BehavType.DEALT,
                self.ACCOMPANY.value: BehavType.MOVED,
                self.ACCORD.value: BehavType.THOUGHT,
                self.ACCOUNT.value: BehavType.THOUGHT,
                self.ACCUSE.value: BehavType.DEALT,
                self.ACHIEVE.value: BehavType.DEALT,
                self.ACQUIRE.value: BehavType.DEALT,
                self.ACT.value: BehavType.DONE,
                self.ADD.value: BehavType.DONE,
                self.ADDRESS.value: BehavType.DEALT,
                self.ADHERE.value: BehavType.DONE,
                self.ADJUST.value: BehavType.DEALT,
                self.ADMIRE.value: BehavType.THOUGHT,
                self.ADMIT.value: BehavType.THOUGHT,
                self.ADOPT.value: BehavType.DEALT,
                self.ADVANCE.value: BehavType.DEALT,
                self.ADVERTISE.value: BehavType.DEALT,
                self.ADVISE.value: BehavType.THOUGHT,
                self.AFFECT.value: BehavType.DONE,
                self.AFFORD.value: BehavType.DEALT,
                self.AGREE.value: BehavType.THOUGHT,
                self.AID.value: BehavType.DEALT,
                self.AIM.value: BehavType.MOVED,
                self.ALLEGE.value: BehavType.TALKED,
                self.ALLOW.value: BehavType.THOUGHT,
                self.ALTER.value: BehavType.DONE,
                self.ANGRY.value: BehavType.FELT,
                self.ANNOUNCE.value: BehavType.DONE,
                self.ANNOY.value: BehavType.FELT,
                self.ANSWER.value: BehavType.TALKED,
                self.ANTICIPATE.value: BehavType.THOUGHT,
                self.APOLOGIZE.value: BehavType.TALKED,
                self.APPEAL.value: BehavType.TALKED,
                self.APPEAR.value: BehavType.VIEWED,
                self.APPLY.value: BehavType.DONE,
                self.APPOINT.value: BehavType.DEALT,
                self.APPRICIATE.value: BehavType.THOUGHT,
                self.APPROACH.value: BehavType.MOVED,
                self.APPROVE.value: BehavType.THOUGHT,
                self.ARGUE.value: BehavType.TALKED,
                self.ARRANGE.value: BehavType.DEALT,
                self.ARREST.value: BehavType.DEALT,
                self.ARRIVE.value: BehavType.MOVED,
                self.ASK.value: BehavType.TALKED,
                self.ASSIST.value: BehavType.DEALT,
                self.ASSUME.value: BehavType.DEALT,
                self.ASSURE.value: BehavType.DEALT,
                self.ATTACH.value: BehavType.HANDLED,
                self.ATTACK.value: BehavType.DEALT,
                self.ATTEMPT.value: BehavType.THOUGHT,
                self.ATTEND.value: BehavType.DEALT,
                self.ATTRACT.value: BehavType.DONE,
                self.AVOID.value: BehavType.MOVED,
                self.AWARD.value: BehavType.DEALT,
                self.BAKE.value: BehavType.COOKED,
                self.BAN.value: BehavType.DEALT,
                self.BASE.value: BehavType.DONE,
                self.BE.value: BehavType.EXPRESSED,
                self.BEAR.value: BehavType.EXPRESSED,
                self.BEAT.value: BehavType.MOVED,
                self.BECOME.value: BehavType.EXPRESSED,
                self.BEG.value: BehavType.DEALT,
                self.BEGIN.value: BehavType.DONE,
                self.BEHAVE.value: BehavType.DONE,
                self.BELIEVE.value: BehavType.THOUGHT,
                self.BELONG.value: BehavType.DEALT,
                self.BEND.value: BehavType.MOVED,
                self.BET.value: BehavType.DEALT,
                self.BETRAY.value: BehavType.THOUGHT,
                self.BID.value: BehavType.DEALT,
                self.BIND.value: BehavType.DEALT,
                self.BITE.value: BehavType.MOVED,
                self.BLAME.value: BehavType.TALKED,
                self.BLEED.value: BehavType.DONE,
                self.BLEND.value: BehavType.COOKED,
                self.BLESS.value: BehavType.THOUGHT,
                self.BLOCK.value: BehavType.DEALT,
                self.BLOW.value: BehavType.MOVED,
                self.BOAST.value: BehavType.TALKED,
                self.BOIL.value: BehavType.COOKED,
                self.BORE.value: BehavType.FELT,
                self.BORROW.value: BehavType.DEALT,
                self.BOTHER.value: BehavType.FELT,
                self.BOUND.value: BehavType.DEALT,
                self.BOW.value: BehavType.MOVED,
                self.BREAK.value: BehavType.DONE,
                self.BREATHE.value: BehavType.MOVED,
                self.BRING.value: BehavType.DEALT,
                self.BROW.value: BehavType.EXPRESSED,
                self.BUILD.value: BehavType.DEALT,
                self.BURN.value: BehavType.COOKED,
                self.BURST.value: BehavType.DONE,
                self.BURY.value: BehavType.DONE,
                self.BUY.value: BehavType.DEALT,
                self.CALCULATE.value: BehavType.DEALT,
                self.CALL.value: BehavType.TALKED,
                self.CANCEL.value: BehavType.DEALT,
                self.CAPTURE.value: BehavType.DEALT,
                self.CARE.value: BehavType.FELT,
                self.CARRY.value: BehavType.DEALT,
                self.CAST.value: BehavType.MOVED,
                self.CATCH.value: BehavType.MOVED,
                self.CAUSE.value: BehavType.THOUGHT,
                self.CEASE.value: BehavType.DONE,
                self.CELEBRATE.value: BehavType.TALKED,
                self.CHANGE.value: BehavType.DONE,
                self.CHARGE.value: BehavType.DEALT,
                self.CHARM.value: BehavType.FELT,
                self.CHASE.value: BehavType.MOVED,
                self.CHEAT.value: BehavType.THOUGHT,
                self.CHECK.value: BehavType.DEALT,
                self.CHEER.value: BehavType.TALKED,
                self.CHEW.value: BehavType.MOVED,
                self.CHOOSE.value: BehavType.DEALT,
                self.CHOP.value: BehavType.MOVED,
                self.CLAIM.value: BehavType.TALKED,
                self.CLEAN.value: BehavType.DONE,
                self.CLICK.value: BehavType.HANDLED,
                self.CLIMB.value: BehavType.MOVED,
                self.CLING.value: BehavType.MOVED,
                self.CLIP.value: BehavType.MOVED,
                self.CLOSE.value: BehavType.DEALT,
                self.CLOTHE.value: BehavType.DONE,
                self.COACH.value: BehavType.TALKED,
                self.COLLAPSE.value: BehavType.DONE,
                self.COLLECT.value: BehavType.DONE,
                self.COMBINE.value: BehavType.DEALT,
                self.COME.value: BehavType.MOVED,
                self.COMFORT.value: BehavType.TALKED,
                self.COMMAND.value: BehavType.DEALT,
                self.COMMIT.value: BehavType.DEALT,
                self.COMMUNICATE.value: BehavType.TALKED,
                self.COMPARE.value: BehavType.DEALT,
                self.COMPETE.value: BehavType.DEALT,
                self.COMPLETE.value: BehavType.DONE,
                self.COMPLAIN.value: BehavType.TALKED,
                self.COMPOSE.value: BehavType.DEALT,
                self.CONCEIVE.value: BehavType.THOUGHT,
                self.CONCENTRATE.value: BehavType.FELT,
                self.CONCERN.value: BehavType.THOUGHT,
                self.CONCLUDE.value: BehavType.DONE,
                self.CONDUCT.value: BehavType.DEALT,
                self.CONFESS.value: BehavType.TALKED,
                self.CONFIRM.value: BehavType.THOUGHT,
                self.CONFRONT.value: BehavType.DONE,
                self.CONFUSE.value: BehavType.THOUGHT,
                self.CONNECT.value: BehavType.HANDLED,
                self.CONSIDER.value: BehavType.THOUGHT,
                self.CONSIST.value: BehavType.DEALT,
                self.CONSTRUCT.value: BehavType.DEALT,
                self.CONSUME.value: BehavType.DEALT,
                self.CONTACT.value: BehavType.TALKED,
                self.CONTAIN.value: BehavType.DONE,
                self.CONTINUE.value: BehavType.DONE,
                self.CONTRIBUTE.value: BehavType.DEALT,
                self.CONTROL.value: BehavType.HANDLED,
                self.CONVERT.value: BehavType.DEALT,
                self.CONVEY.value: BehavType.DEALT,
                self.CONVINCE.value: BehavType.THOUGHT,
                self.COOK.value: BehavType.COOKED,
                self.COOL.value: BehavType.FELT,
                self.COOPERATE.value: BehavType.DEALT,
                self.COPE.value: BehavType.DEALT,
                self.COPY.value: BehavType.DONE,
                self.CORRECT.value: BehavType.THOUGHT,
                self.COST.value: BehavType.DEALT,
                self.COUGH.value: BehavType.EXPRESSED,
                self.COUNT.value: BehavType.DONE,
                self.COUNTER.value: BehavType.DEALT,
                self.COVER.value: BehavType.DEALT,
                self.CRACK.value: BehavType.DONE,
                self.CRASH.value: BehavType.DONE,
                self.CRAWL.value: BehavType.MOVED,
                self.CREATE.value: BehavType.DONE,
                self.CRITICIZE.value: BehavType.TALKED,
                self.CROSS.value: BehavType.MOVED,
                self.CRUSH.value: BehavType.DONE,
                self.CRY.value: BehavType.TALKED,
                self.CURE.value: BehavType.DEALT,
                self.CURL.value: BehavType.EXPRESSED,
                self.CUT.value: BehavType.DONE,
                self.DAMAGE.value: BehavType.EXPRESSED,
                self.DANCE.value: BehavType.MOVED,
                self.DARE.value: BehavType.DEALT,
                self.DEAL.value: BehavType.DEALT,
                self.DECAY.value: BehavType.EXPRESSED,
                self.DECIDE.value: BehavType.THOUGHT,
                self.DECLARE.value: BehavType.TALKED,
                self.DECLINE.value: BehavType.THOUGHT,
                self.DECORATE.value: BehavType.DEALT,
                self.DECREASE.value: BehavType.EXPRESSED,
                self.DEFEAT.value: BehavType.DONE,
                self.DEFEND.value: BehavType.DONE,
                self.DEFINE.value: BehavType.DEALT,
                self.DELAY.value: BehavType.EXPRESSED,
                self.DELIVER.value: BehavType.DEALT,
                self.DEMONSTRATE: BehavType.DEALT,
                self.DENY.value: BehavType.THOUGHT,
                self.DEPEND.value: BehavType.THOUGHT,
                self.DEPOSITE.value: BehavType.DEALT,
                self.DERIVE.value: BehavType.DONE,
                self.DESCEND.value: BehavType.MOVED,
                self.DESCRIBE.value: BehavType.TALKED,
                self.DESERT.value: BehavType.MOVED,
                self.DESERVE.value: BehavType.THOUGHT,
                self.DESIRE.value: BehavType.THOUGHT,
                self.DESTROY.value: BehavType.DONE,
                self.DETERMINE.value: BehavType.THOUGHT,
                self.DEVELOP.value: BehavType.DEALT,
                self.DEVISE.value: BehavType.THOUGHT,
                self.DEVOTE.value: BehavType.DONE,
                self.DIAL.value: BehavType.HANDLED,
                self.DIE.value: BehavType.DONE,
                self.DIG.value: BehavType.MOVED,
                self.DIGEST.value: BehavType.DONE,
                self.DISAPPEAR.value: BehavType.VIEWED,
                self.DISAPPOINT.value: BehavType.THOUGHT,
                self.DISAPPROVE.value: BehavType.THOUGHT,
                self.DISCHARGE.value: BehavType.DEALT,
                self.DISCOVER.value: BehavType.DONE,
                self.DISCUSS.value: BehavType.TALKED,
                self.DISGUISE.value: BehavType.DEALT,
                self.DISGUST.value: BehavType.FELT,
                self.DISLIKE.value: BehavType.FELT,
                self.DISMISS.value: BehavType.DEALT,
                self.DISPEL.value: BehavType.DEALT,
                self.DISPLAY.value: BehavType.VIEWED,
                self.DISTINGUISH.value: BehavType.DEALT,
                self.DISTRIBUTE.value: BehavType.DEALT,
                self.DO.value: BehavType.DONE,
                self.DOMINATE.value: BehavType.DEALT,
                self.DOUBT.value: BehavType.THOUGHT,
                self.DRAG.value: BehavType.MOVED,
                self.DRAW.value: BehavType.MOVED,
                self.DREAM.value: BehavType.THOUGHT,
                self.DRESS.value: BehavType.VIEWED,
                self.DRIFT.value: BehavType.EXPRESSED,
                self.DRIVE.value: BehavType.HANDLED,
                self.DROP.value: BehavType.EXPRESSED,
                self.DROWN.value: BehavType.EXPRESSED,
                self.DRY.value: BehavType.EXPRESSED,
                self.EARN.value: BehavType.DEALT,
                self.EASE.value: BehavType.EXPRESSED,
                self.EAT.value: BehavType.COOKED,
                self.EDUCATE.value: BehavType.DEALT,
                self.ELECT.value: BehavType.DEALT,
                self.ELIMINATE.value: BehavType.THOUGHT,
                self.EMAIL.value: BehavType.TALKED,
                self.EMBARRASS.value: BehavType.FELT,
                self.EMERGE.value: BehavType.EXPRESSED,
                self.EMPHASIZE.value: BehavType.TALKED,
                self.EMPLOY.value: BehavType.DEALT,
                self.ENABLE.value: BehavType.EXPRESSED,
                self.ENCOUNTER.value: BehavType.MOVED,
                self.ENCOURAGE.value: BehavType.THOUGHT,
                self.END.value: BehavType.EXPRESSED,
                self.ENDURE.value: BehavType.FELT,
                self.ENGAGE.value: BehavType.DEALT,
                self.ENJOY.value: BehavType.FELT,
                self.ENSURE.value: BehavType.DEALT,
                self.ENTER.value: BehavType.MOVED,
                self.ENTERTAIN.value: BehavType.FELT,
                self.ENVY.value: BehavType.THOUGHT,
                self.EQUIP.value: BehavType.VIEWED,
                self.ESCAPE.value: BehavType.MOVED,
                self.ESTABLISH.value: BehavType.DEALT,
                self.ESTIMATE.value: BehavType.DEALT,
                self.EXAMINE.value: BehavType.DEALT,
                self.EXCHANGE.value: BehavType.DEALT,
                self.EXCITE.value: BehavType.FELT,
                self.EXCUSE.value: BehavType.THOUGHT,
                self.EXHAUST.value: BehavType.DEALT,
                self.EXHIBIT.value: BehavType.DEALT,
                self.EXIST.value: BehavType.EXPRESSED,
                self.EXPAND.value: BehavType.EXPRESSED,
                self.EXPECT.value: BehavType.THOUGHT,
                self.EXPLAIN.value: BehavType.TALKED,
                self.EXPLODE.value: BehavType.EXPRESSED,
                self.EXPLORE.value: BehavType.VIEWED,
                self.EXPORT.value: BehavType.DEALT,
                self.EXPOSE.value: BehavType.VIEWED,
                self.EXPRESS.value: BehavType.VIEWED,
                self.EXTEND.value: BehavType.DEALT,
                self.FACE.value: BehavType.VIEWED,
                self.FAIL.value: BehavType.DONE,
                self.FALL.value: BehavType.MOVED,
                self.FASTEN.value: BehavType.DEALT,
                self.FEED.value: BehavType.DEALT,
                self.FEEL.value: BehavType.FELT,
                self.FIB.value: BehavType.TALKED,
                self.FIGHT.value: BehavType.DONE,
                self.FILL.value: BehavType.DEALT,
                self.FIND.value: BehavType.VIEWED,
                self.FINISH.value: BehavType.DEALT,
                self.FIRE.value: BehavType.HANDLED,
                self.FIREJOB.value: BehavType.DEALT,
                self.FIT.value: BehavType.EXPRESSED,
                self.FIX.value: BehavType.DEALT,
                self.FLASH.value: BehavType.EXPRESSED,
                self.FLEE.value: BehavType.MOVED,
                self.FLOAT.value: BehavType.EXPRESSED,
                self.FLOW.value: BehavType.EXPRESSED,
                self.FLY.value: BehavType.MOVED,
                self.FOCUS.value: BehavType.VIEWED,
                self.FOLD.value: BehavType.DEALT,
                self.FOLLOW.value: BehavType.THOUGHT,
                self.FORCE.value: BehavType.THOUGHT,
                self.FORGET.value: BehavType.THOUGHT,
                self.FORGIVE.value: BehavType.THOUGHT,
                self.FORM.value: BehavType.DEALT,
                self.FREEZE.value: BehavType.EXPRESSED,
                self.FRIGHTEN.value: BehavType.FELT,
                self.FROWN.value: BehavType.VIEWED,
                self.FRY.value: BehavType.COOKED,
                self.FULFILL.value: BehavType.DEALT,
                self.GAIN.value: BehavType.EXPRESSED,
                self.GATHER.value: BehavType.DEALT,
                self.GAZE.value: BehavType.VIEWED,
                self.GET.value: BehavType.DEALT,
                self.GIVE.value: BehavType.DEALT,
                self.GLAD.value: BehavType.FELT,
                self.GLANCE.value: BehavType.VIEWED,
                self.GLOW.value: BehavType.EXPRESSED,
                self.GO.value: BehavType.MOVED,
                self.GOVERN.value: BehavType.DEALT,
                self.GRADUATE.value: BehavType.DEALT,
                self.GREET.value: BehavType.TALKED,
                self.GRIN.value: BehavType.VIEWED,
                self.GROW.value: BehavType.DEALT,
                self.GROWL.value: BehavType.TALKED,
                self.GUARANTEE.value: BehavType.DEALT,
                self.GUARD.value: BehavType.DONE,
                self.GUESS.value: BehavType.THOUGHT,
                self.GUIDE.value: BehavType.DEALT,
                self.HAND.value: BehavType.MOVED,
                self.HANDLE.value: BehavType.HANDLED,
                self.HANG.value: BehavType.MOVED,
                self.HAPPEN.value: BehavType.DONE,
                self.HAPPY.value: BehavType.FELT,
                self.HARVEST.value: BehavType.DEALT,
                self.HATE.value: BehavType.THOUGHT,
                self.HAVE.value: BehavType.DEALT,
                self.HEAD.value: BehavType.DONE,
                self.HEAL.value: BehavType.DEALT,
                self.HEAR.value: BehavType.TALKED,
                self.HELP.value: BehavType.DEALT,
                self.HESITATE.value: BehavType.THOUGHT,
                self.HIDE.value: BehavType.DEALT,
                self.HIRE.value: BehavType.DEALT,
                self.HIT.value: BehavType.MOVED,
                self.HOLD.value: BehavType.MOVED,
                self.HOP.value: BehavType.MOVED,
                self.HOPE.value: BehavType.THOUGHT,
                self.HUG.value: BehavType.MOVED,
                self.HUNT.value: BehavType.DEALT,
                self.HURRY.value: BehavType.FELT,
                self.HURT.value: BehavType.DEALT,
                self.IDENTIFY.value: BehavType.DEALT,
                self.IGNORE.value: BehavType.THOUGHT,
                self.ILLUSTRATE.value: BehavType.TALKED,
                self.IMAGINE.value: BehavType.THOUGHT,
                self.IMPLY.value: BehavType.TALKED,
                self.IMPORT.value: BehavType.DEALT,
                self.IMPOSE.value: BehavType.THOUGHT,
                self.IMPRESS.value: BehavType.FELT,
                self.IMPROVE.value: BehavType.DEALT,
                self.INCLUDE.value: BehavType.DONE,
                self.INCREASE.value: BehavType.EXPRESSED,
                self.INDICATE.value: BehavType.TALKED,
                self.INFLUENCE.value: BehavType.EXPRESSED,
                self.INFORM.value: BehavType.TALKED,
                self.INHERIT.value: BehavType.DEALT,
                self.INJURE.value: BehavType.VIEWED,
                self.INSIST.value: BehavType.TALKED,
                self.INSPIRE.value: BehavType.TALKED,
                self.INSTALL.value: BehavType.HANDLED,
                self.INSTRUCT.value: BehavType.DEALT,
                self.INSTRUMENT.value: BehavType.DONE,
                self.INSULT.value: BehavType.THOUGHT,
                self.INTEND.value: BehavType.THOUGHT,
                self.INTERFERE.value: BehavType.EXPRESSED,
                self.INTERPRET.value: BehavType.THOUGHT,
                self.INTERRUPT.value: BehavType.DEALT,
                self.INTRODUCE.value: BehavType.TALKED,
                self.INVADE.value: BehavType.DEALT,
                self.INVENT.value: BehavType.THOUGHT,
                self.INVEST.value: BehavType.DEALT,
                self.INVESTIGATE.value: BehavType.DEALT,
                self.INVITE.value: BehavType.DEALT,
                self.INVOLVE.value: BehavType.DEALT,
                self.ISSUE.value: BehavType.EXPRESSED,
                self.JOG.value: BehavType.MOVED,
                self.JOIN.value: BehavType.DEALT,
                self.JUDGE.value: BehavType.DEALT,
                self.JUMP.value: BehavType.MOVED,
                self.JUSTIFY.value: BehavType.DEALT,
                self.KEEP.value: BehavType.EXPRESSED,
                self.KEYBOARD.value: BehavType.HANDLED,
                self.KICK.value: BehavType.MOVED,
                self.KILL.value: BehavType.DONE,
                self.KISS.value: BehavType.MOVED,
                self.KNIT.value: BehavType.DEALT,
                self.KNOCK.value: BehavType.MOVED,
                self.KNOW.value: BehavType.THOUGHT,
                self.LAND.value: BehavType.DEALT,
                self.LAUGH.value: BehavType.TALKED,
                self.LAUNCH.value: BehavType.DEALT,
                self.LAY.value: BehavType.MOVED,
                self.LEAD.value: BehavType.DEALT,
                self.LEAN.value: BehavType.EXPRESSED,
                self.LEAP.value: BehavType.MOVED,
                self.LEARN.value: BehavType.THOUGHT,
                self.LEAVE.value: BehavType.EXPRESSED,
                self.LEND.value: BehavType.DEALT,
                self.LET.value: BehavType.DEALT,
                self.LIE.value: BehavType.MOVED,
                self.LIFE.value: BehavType.EXPRESSED,
                self.LIFT.value: BehavType.MOVED,
                self.LIGHT.value: BehavType.HANDLED,
                self.LIKE.value: BehavType.THOUGHT,
                self.LINE.value: BehavType.MOVED,
                self.LISTEN.value: BehavType.DONE,
                self.LIVE.value: BehavType.EXPRESSED,
                self.LOAD.value: BehavType.DEALT,
                self.LOAN.value: BehavType.DEALT,
                self.LOCK.value: BehavType.HANDLED,
                self.LOOK.value: BehavType.VIEWED,
                self.LOOKDOWN.value: BehavType.VIEWED,
                self.LOSE.value: BehavType.DONE,
                self.LOVE.value: BehavType.THOUGHT,
                self.MAINTAIN.value: BehavType.EXPRESSED,
                self.MAKE.value: BehavType.DEALT,
                self.MAKEUP.value: BehavType.VIEWED,
                self.MANAGE.value: BehavType.DEALT,
                self.MANUFACTURE.value: BehavType.DEALT,
                self.MAON.value: BehavType.TALKED,
                self.MARK.value: BehavType.DEALT,
                self.MARRY.value: BehavType.DEALT,
                self.MARVEL.value: BehavType.THOUGHT,
                self.MASTER.value: BehavType.DEALT,
                self.MATCH.value: BehavType.DEALT,
                self.MATTER.value: BehavType.EXPRESSED,
                self.MEAN.value: BehavType.EXPRESSED,
                self.MEASURE.value: BehavType.DEALT,
                self.MEET.value: BehavType.MOVED,
                self.MELT.value: BehavType.EXPRESSED,
                self.MEMO.value: BehavType.DEALT,
                self.MEND.value: BehavType.DEALT,
                self.MENTION.value: BehavType.TALKED,
                self.MIND.value: BehavType.THOUGHT,
                self.MISS.value: BehavType.DEALT,
                self.MISUNDERSTAND.value: BehavType.THOUGHT,
                self.MIX.value: BehavType.DEALT,
                self.MODIFY.value: BehavType.DEALT,
                self.MONITOR.value: BehavType.DEALT,
                self.MOUNT.value: BehavType.MOVED,
                self.MOVE.value: BehavType.MOVED,
                self.MULTIPLY.value: BehavType.DEALT,
                self.MUST.value: BehavType.THOUGHT,
                self.NEED.value: BehavType.THOUGHT,
                self.NEGLECT.value: BehavType.THOUGHT,
                self.NOD.value: BehavType.TALKED,
                self.NONE.value: BehavType.DONE,
                self.NOTE.value: BehavType.DEALT,
                self.NOTICE.value: BehavType.THOUGHT,
                self.OBEY.value: BehavType.THOUGHT,
                self.OBJECT.value: BehavType.TALKED,
                self.OBSERVE.value: BehavType.VIEWED,
                self.OBTAIN.value: BehavType.DEALT,
                self.OCCUPY.value: BehavType.DEALT,
                self.OCCUR.value: BehavType.EXPRESSED,
                self.OFFEND.value: BehavType.FELT,
                self.OFFER.value: BehavType.TALKED,
                self.OPEN.value: BehavType.DEALT,
                self.OPERATE.value: BehavType.DEALT,
                self.OPPOSE.value: BehavType.DEALT,
                self.ORGANIZE.value: BehavType.DEALT,
                self.OVERCOME.value: BehavType.DONE,
                self.OVERFLOW.value: BehavType.EXPRESSED,
                self.OVERLOOK.value: BehavType.VIEWED,
                self.OWE.value: BehavType.DEALT,
                self.OWN.value: BehavType.EXPRESSED,
                self.PACK.value: BehavType.DEALT,
                self.PAINT.value: BehavType.DEALT,
                self.PARK.value: BehavType.HANDLED,
                self.PARTICIPATE.value: BehavType.DEALT,
                self.PASS.value: BehavType.MOVED,
                self.PAT.value: BehavType.MOVED,
                self.PAUSE.value: BehavType.DEALT,
                self.PAY.value: BehavType.DEALT,
                self.PERCEIVE.value: BehavType.THOUGHT,
                self.PERFORM.value: BehavType.MOVED,
                self.PERMIT.value: BehavType.THOUGHT,
                self.PERSUADE.value: BehavType.TALKED,
                self.PHONE.value: BehavType.TALKED,
                self.PICK.value: BehavType.DEALT,
                self.PITY.value: BehavType.THOUGHT,
                self.PLACE.value: BehavType.DEALT,
                self.PLANT.value: BehavType.DEALT,
                self.PLAY.value: BehavType.DONE,
                self.PLEASE.value: BehavType.FELT,
                self.PLUNGE.value: BehavType.MOVED,
                self.POINT.value: BehavType.MOVED,
                self.POP.value: BehavType.DONE,
                self.POSE.value: BehavType.MOVED,
                self.POSSESS.value: BehavType.EXPRESSED,
                self.POSTPONE.value: BehavType.DEALT,
                self.POUR.value: BehavType.DEALT,
                self.PRACTICE.value: BehavType.DEALT,
                self.PRAISE.value: BehavType.THOUGHT,
                self.PRAY.value: BehavType.THOUGHT,
                self.PREDICT.value: BehavType.DEALT,
                self.PREFER.value: BehavType.THOUGHT,
                self.PREPARE.value: BehavType.DEALT,
                self.PRESENT.value: BehavType.DEALT,
                self.PRESERVE.value: BehavType.DEALT,
                self.PRESS.value: BehavType.MOVED,
                self.PRETEND.value: BehavType.THOUGHT,
                self.PREVENT.value: BehavType.DEALT,
                self.PRINT.value: BehavType.HANDLED,
                self.PROCEED.value: BehavType.DEALT,
                self.PRODUCE.value: BehavType.DONE,
                self.PROFESS.value: BehavType.TALKED,
                self.PROMISE.value: BehavType.TALKED,
                self.PROMOTE.value: BehavType.DEALT,
                self.PROMPT.value: BehavType.DEALT,
                self.PRONOUNCE.value: BehavType.TALKED,
                self.PROPOSE.value: BehavType.DEALT,
                self.PROTECT.value: BehavType.DEALT,
                self.PROTEST.value: BehavType.TALKED,
                self.PROVE.value: BehavType.THOUGHT,
                self.PROVIDE.value: BehavType.DEALT,
                self.PUBLISH.value: BehavType.DEALT,
                self.PULL.value: BehavType.MOVED,
                self.PUNCH.value: BehavType.MOVED,
                self.PUNISH.value: BehavType.DEALT,
                self.PURCHASE.value: BehavType.DEALT,
                self.PURSUE.value: BehavType.MOVED,
                self.PUSH.value: BehavType.MOVED,
                self.PUT.value: BehavType.MOVED,
                self.PUZZLE.value: BehavType.THOUGHT,
                self.QUATE.value: BehavType.DEALT,
                self.QUIT.value: BehavType.DEALT,
                self.RAISE.value: BehavType.EXPRESSED,
                self.RANGE.value: BehavType.EXPRESSED,
                self.REACH.value: BehavType.DEALT,
                self.REACT.value: BehavType.EXPRESSED,
                self.READ.value: BehavType.DONE,
                self.REALIZE.value: BehavType.THOUGHT,
                self.REBEL.value: BehavType.DEALT,
                self.RECALL.value: BehavType.TALKED,
                self.RECEIVE.value: BehavType.DEALT,
                self.RECKON.value: BehavType.DEALT,
                self.RECOGNZE.value: BehavType.THOUGHT,
                self.RECOLLECT.value: BehavType.THOUGHT,
                self.RECOMMEND.value: BehavType.DEALT,
                self.RECOVER.value: BehavType.DEALT,
                self.REDUCE.value: BehavType.EXPRESSED,
                self.REFER.value: BehavType.DEALT,
                self.REFLECT.value: BehavType.EXPRESSED,
                self.REFORM.value: BehavType.DEALT,
                self.REFRESH.value: BehavType.FELT,
                self.REFUSE.value: BehavType.TALKED,
                self.REGARD.value: BehavType.VIEWED,
                self.REGRET.value: BehavType.THOUGHT,
                self.REJECT.value: BehavType.TALKED,
                self.RELATE.value: BehavType.EXPRESSED,
                self.RELAX.value: BehavType.EXPRESSED,
                self.RELAY.value: BehavType.DEALT,
                self.RELEASE.value: BehavType.DEALT,
                self.RELY.value: BehavType.THOUGHT,
                self.REMAIN.value: BehavType.EXPRESSED,
                self.REMARK.value: BehavType.THOUGHT,
                self.REMEMBER.value: BehavType.THOUGHT,
                self.REMIND.value: BehavType.THOUGHT,
                self.REMOVE.value: BehavType.DEALT,
                self.RENT.value: BehavType.DEALT,
                self.REPAIR.value: BehavType.DEALT,
                self.REPEAT.value: BehavType.EXPRESSED,
                self.REPORT.value: BehavType.TALKED,
                self.REPRESENT.value: BehavType.DEALT,
                self.REQUEST.value: BehavType.TALKED,
                self.REQUIRE.value: BehavType.DEALT,
                self.RESCUE.value: BehavType.DEALT,
                self.RESEMBLE.value: BehavType.EXPRESSED,
                self.RESERVE.value: BehavType.DEALT,
                self.RESIST.value: BehavType.DEALT,
                self.RESOLVE.value: BehavType.DEALT,
                self.RESPECT.value: BehavType.THOUGHT,
                self.RESPOND.value: BehavType.DEALT,
                self.REST.value: BehavType.DEALT,
                self.RESTORE.value: BehavType.DEALT,
                self.RESULT.value: BehavType.EXPRESSED,
                self.RETIRE.value: BehavType.DEALT,
                self.RETRICT.value: BehavType.DEALT,
                self.RETURN.value: BehavType.MOVED,
                self.REVEAL.value: BehavType.EXPRESSED,
                self.REVIEW.value: BehavType.THOUGHT,
                self.REWARD.value: BehavType.DEALT,
                self.RID.value: BehavType.DEALT,
                self.RIDE.value: BehavType.HANDLED,
                self.RING.value: BehavType.DONE,
                self.RISE.value: BehavType.MOVED,
                self.ROB.value: BehavType.DEALT,
                self.ROCK.value: BehavType.EXPRESSED,
                self.ROLL.value: BehavType.MOVED,
                self.ROW.value: BehavType.DEALT,
                self.RUB.value: BehavType.MOVED,
                self.RUIN.value: BehavType.EXPRESSED,
                self.RULE.value: BehavType.THOUGHT,
                self.RUN.value: BehavType.MOVED,
                self.RUSH.value: BehavType.FELT,
                self.SACRIFICE.value: BehavType.DEALT,
                self.SAD.value: BehavType.FELT,
                self.SAIL.value: BehavType.HANDLED,
                self.SATISFY.value: BehavType.EXPRESSED,
                self.SAVE.value: BehavType.DEALT,
                self.SAY.value: BehavType.TALKED,
                self.SCARE.value: BehavType.FELT,
                self.SCATTER.value: BehavType.EXPRESSED,
                self.SCOLD.value: BehavType.TALKED,
                self.SCRATCH.value: BehavType.MOVED,
                self.SCREAM.value: BehavType.TALKED,
                self.SEAL.value: BehavType.DEALT,
                self.SEARCH.value: BehavType.VIEWED,
                self.SEAT.value: BehavType.MOVED,
                self.SECURE.value: BehavType.DEALT,
                self.SEE.value: BehavType.VIEWED,
                self.SEEK.value: BehavType.VIEWED,
                self.SEEM.value: BehavType.THOUGHT,
                self.SEIZE.value: BehavType.MOVED,
                self.SELECT.value: BehavType.DEALT,
                self.SELL.value: BehavType.DEALT,
                self.SEND.value: BehavType.DEALT,
                self.SEPARATE.value: BehavType.DEALT,
                self.SERVE.value: BehavType.DEALT,
                self.SET.value: BehavType.DEALT,
                self.SETTLE.value: BehavType.DEALT,
                self.SHAKE.value: BehavType.MOVED,
                self.SHARE.value: BehavType.DEALT,
                self.SHIFT.value: BehavType.MOVED,
                self.SHINE.value: BehavType.EXPRESSED,
                self.SHOCK.value: BehavType.FELT,
                self.SHOOT.value: BehavType.HANDLED,
                self.SHOP.value: BehavType.DEALT,
                self.SHOUT.value: BehavType.TALKED,
                self.SHOW.value: BehavType.VIEWED,
                self.SHRUG.value: BehavType.MOVED,
                self.SHUT.value: BehavType.DEALT,
                self.SIGH.value: BehavType.TALKED,
                self.SIGN.value: BehavType.DEALT,
                self.SING.value: BehavType.TALKED,
                self.SINK.value: BehavType.EXPRESSED,
                self.SIT.value: BehavType.MOVED,
                self.SKATE.value: BehavType.MOVED,
                self.SKIP.value: BehavType.MOVED,
                self.SLEEP.value: BehavType.EXPRESSED,
                self.SLICE.value: BehavType.DEALT,
                self.SLIDE.value: BehavType.MOVED,
                self.SLIP.value: BehavType.MOVED,
                self.SLOBBER.value: BehavType.EXPRESSED,
                self.SMASH.value: BehavType.DONE,
                self.SMELL.value: BehavType.EXPRESSED,
                self.SMILE.value: BehavType.VIEWED,
                self.SMOKE.value: BehavType.DONE,
                self.SNAP.value: BehavType.DONE,
                self.SOLVE.value: BehavType.THOUGHT,
                self.SOUND.value: BehavType.DONE,
                self.SPARE.value: BehavType.DEALT,
                self.SPEAK.value: BehavType.TALKED,
                self.SPECIALIZE.value: BehavType.DEALT,
                self.SPEND.value: BehavType.DEALT,
                self.SPILL.value: BehavType.DEALT,
                self.SPIN.value: BehavType.DEALT,
                self.SPLIT.value: BehavType.DEALT,
                self.SPOIL.value: BehavType.EXPRESSED,
                self.SPREAD.value: BehavType.DEALT,
                self.STAND.value: BehavType.MOVED,
                self.STARE.value: BehavType.VIEWED,
                self.START.value: BehavType.DEALT,
                self.STARVE.value: BehavType.EXPRESSED,
                self.STAY.value: BehavType.EXPRESSED,
                self.STEAL.value: BehavType.DEALT,
                self.STICK.value: BehavType.DEALT,
                self.STIMULATE.value: BehavType.DEALT,
                self.STIR.value: BehavType.DEALT,
                self.STOP.value: BehavType.DEALT,
                self.STORE.value: BehavType.DEALT,
                self.STRAIN.value: BehavType.MOVED,
                self.STRESS.value: BehavType.EXPRESSED,
                self.STRETCH.value: BehavType.MOVED,
                self.STRIKE.value: BehavType.MOVED,
                self.STRUGGLE.value: BehavType.THOUGHT,
                self.STUDY.value: BehavType.DEALT,
                self.SUBMIT.value: BehavType.DEALT,
                self.SUBSCRIBE.value: BehavType.DEALT,
                self.SUCCEED.value: BehavType.DEALT,
                self.SUCK.value: BehavType.DONE,
                self.SUFFER.value: BehavType.FELT,
                self.SUGGEST.value: BehavType.TALKED,
                self.SUIT.value: BehavType.EXPRESSED,
                self.SUPPLY.value: BehavType.DEALT,
                self.SUPPOSE.value: BehavType.TALKED,
                self.SUPPORT.value: BehavType.DEALT,
                self.SURPRISE.value: BehavType.FELT,
                self.SURROUND.value: BehavType.EXPRESSED,
                self.SURVIVE.value: BehavType.EXPRESSED,
                self.SUSPECT.value: BehavType.THOUGHT,
                self.SUSPEND.value: BehavType.DEALT,
                self.SWEAR.value: BehavType.THOUGHT,
                self.SWEEP.value: BehavType.DEALT,
                self.SWIM.value: BehavType.MOVED,
                self.SWING.value: BehavType.MOVED,
                self.SWITCH.value: BehavType.HANDLED,
                self.SWORD.value: BehavType.MOVED,
                self.TAKE.value: BehavType.DEALT,
                self.TALK.value: BehavType.TALKED,
                self.TAP.value: BehavType.MOVED,
                self.TEACH.value: BehavType.DEALT,
                self.TEAR.value: BehavType.DEALT,
                self.TELL.value: BehavType.DIALOGUE,
                self.TEND.value: BehavType.EXPRESSED,
                self.TEST.value: BehavType.DONE,
                self.THANK.value: BehavType.THOUGHT,
                self.THINK.value: BehavType.THOUGHT,
                self.THREATEN.value: BehavType.FELT,
                self.THROW.value: BehavType.MOVED,
                self.TIE.value: BehavType.DEALT,
                self.TOSS.value: BehavType.DEALT,
                self.TOUCH.value: BehavType.MOVED,
                self.TRAIN.value: BehavType.DEALT,
                self.TRANSFER.value: BehavType.DEALT,
                self.TRANSFORM.value: BehavType.EXPRESSED,
                self.TRANSLATE.value: BehavType.DEALT,
                self.TRANSPORT.value: BehavType.DEALT,
                self.TRAVEL.value: BehavType.DEALT,
                self.TREAT.value: BehavType.DEALT,
                self.TRIP.value: BehavType.DEAL,
                self.TRUST.value: BehavType.THOUGHT,
                self.TRY.value: BehavType.DEALT,
                self.TURN.value: BehavType.MOVED,
                self.TWIST.value: BehavType.MOVED,
                self.TYPE.value: BehavType.DEALT,
                self.UNDERGO.value: BehavType.DEALT,
                self.UNDERLINE.value: BehavType.DEALT,
                self.UNDERSTAND.value: BehavType.THOUGHT,
                self.UNITE.value: BehavType.DEALT,
                self.UNLOCK.value: BehavType.HANDLED,
                self.UPSET.value: BehavType.DEALT,
                self.URGE.value: BehavType.THOUGHT,
                self.USE.value: BehavType.DONE,
                self.VANISH.value: BehavType.EXPRESSED,
                self.VARY.value: BehavType.EXPRESSED,
                self.VIEW.value: BehavType.VIEWED,
                self.VISIT.value: BehavType.MOVED,
                self.VOTE.value: BehavType.DEALT,
                self.WAIT.value: BehavType.EXPRESSED,
                self.WAKE.value: BehavType.EXPRESSED,
                self.WALK.value: BehavType.MOVED,
                self.WANT.value: BehavType.THOUGHT,
                self.WARM.value: BehavType.DEALT,
                self.WARN.value: BehavType.DEALT,
                self.WASTE.value: BehavType.EXPRESSED,
                self.WATCH.value: BehavType.VIEWED,
                self.WAVE.value: BehavType.EXPRESSED,
                self.WEAKEN.value: BehavType.EXPRESSED,
                self.WEAR.value: BehavType.VIEWED,
                self.WEIGH.value: BehavType.DEALT,
                self.WELCOME.value: BehavType.THOUGHT,
                self.WHIP.value: BehavType.EXPRESSED,
                self.WHISPER.value: BehavType.TALKED,
                self.WHISTLE.value: BehavType.TALKED,
                self.WIN.value: BehavType.DEALT,
                self.WIND.value: BehavType.EXPRESSED,
                self.WIPE.value: BehavType.DEALT,
                self.WISH.value: BehavType.THOUGHT,
                self.WITHDRAW.value: BehavType.DEALT,
                self.WONDER.value: BehavType.THOUGHT,
                self.WORK.value: BehavType.DEALT,
                self.WORRY.value: BehavType.THOUGHT,
                self.WOUND.value: BehavType.EXPRESSED,
                self.WRAP.value: BehavType.DEALT,
                self.WRITE.value: BehavType.DEALT,
                self.WRY.value: BehavType.TALKED,
                self.YAWN.value: BehavType.TALKED,
                self.YELL.value: BehavType.TALKED,
                }[self.value]

