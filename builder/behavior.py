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
    REPIRT = auto()
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

def behavior_str_of(behavior: Behavior) -> str:
    return {
            Behavior.ACT: "行動する",
            Behavior.ACCEPT: "受け取る",
            Behavior.ACQUIRE: "入手する",
            Behavior.ADD: "追加する",
            Behavior.ADHERE: "付く",
            Behavior.ADVISE: "助言する",
            Behavior.AGREE: "賛成する",
            Behavior.AIM: "向ける",
            Behavior.ANGRY: "怒る",
            Behavior.ANSWER: "答える",
            Behavior.APPEAR: "現れる",
            Behavior.APPLY: "申し込む",
            Behavior.ARRIVE: "到着する",
            Behavior.ASK: "尋ねる",
            Behavior.ATTACK: "攻撃する",
            Behavior.BE: "いる",
            Behavior.BECOME: "なる",
            Behavior.BEGIN: "始まる",
            Behavior.BELIEVE: "信じる",
            Behavior.BET: "賭ける",
            Behavior.BIND: "縛る",
            Behavior.BORROW: "借りる",
            Behavior.BREAK: "壊す",
            Behavior.BREATHE: "息をする",
            Behavior.BROW: "眉を顰める",
            Behavior.BUILD: "建てる",
            Behavior.BURN: "焼く",
            Behavior.BURST: "弾ける",
            Behavior.BURY: "葬る",
            Behavior.BUY: "買う",
            Behavior.CALCULATE: "計算する",
            Behavior.CALL: "呼ぶ",
            Behavior.CARE: "治療する",
            Behavior.CARRY: "運ぶ",
            Behavior.CATCH: "捕まえる",
            Behavior.CHANGE: "変える",
            Behavior.CHARM: "魅了する",
            Behavior.CHECK: "確認する",
            Behavior.CHEER: "応援する",
            Behavior.CHOOSE: "選ぶ",
            Behavior.CLEAN: "掃除する",
            Behavior.CLICK: "クリックする",
            Behavior.CLIMB: "登る",
            Behavior.CLOSE: "閉じる",
            Behavior.CLOTHE: "服を着せる",
            Behavior.COACH: "指導する",
            Behavior.COME: "来る",
            Behavior.COMMAND: "命じる",
            Behavior.COMPARE: "比べる",
            Behavior.COMPLETE: "完了する",
            Behavior.CONFESS: "告白する",
            behavior.CONFUSE: "混乱する",
            Behavior.CONTACT: "連絡する",
            Behavior.CONTINUE: "続ける",
            Behavior.COOPERATE: "協力する",
            Behavior.COUGH: "咳をする",
            Behavior.COOK: "料理する",
            Behavior.CREATE: "作る:",
            Behavior.CRY: "叫ぶ",
            Behavior.CUT: "切る",
            Behavior.DANCE: "踊る",
            Behavior.DEAL: "扱う",
            Behavior.DEFINE: "定義する",
            Behavior.DIE: "死ぬ",
            Behavior.DIG: "掘る",
            Behavior.DISAPPEAR: "消える",
            Behavior.DISAPPROVE: "不賛成",
            Behavior.DISLIKE: "嫌い",
            Behavior.DISPEL: "晴らす",
            Behavior.DISPLAY: "表示する",
            Behavior.DIVE: "飛び込む",
            Behavior.DO: "行う",
            Behavior.DOUBT: "疑う",
            Behavior.DRAW: "描く",
            Behavior.DREAM: "夢を見る",
            Behavior.DRESS: "着飾る",
            Behavior.DRINK: "飲む",
            Behavior.DRIVE: "運転する",
            Behavior.DROP: "落ちる",
            Behavior.DRY: "乾く",
            Behavior.EARN: "稼ぐ",
            Behavior.EAT: "食べる",
            Behavior.EDUCATE: "教育する",
            Behavior.EMAIL: "メールする",
            Behavior.EMPLOY: "雇う",
            Behavior.ENGAGE: "婚約する",
            Behavior.ENJOY: "楽しむ",
            Behavior.ENTER: "入る",
            Behavior.ENVY: "恨む",
            Behavior.EQUIP: "装備する",
            Behavior.ESCAPE: "逃げる",
            Behavior.EXCHANGE: "交換する",
            Behavior.EXAMINE: "試験する",
            Behavior.EXCITE: "興奮する",
            Behavior.EXPLAIN: "説明する",
            Behavior.EXPLORE: "探検する",
            Behavior.FACE: "顔を合わせる",
            Behavior.FAIL: "失敗する",
            Behavior.FALL: "落下する",
            Behavior.FEEL: "感じる",
            Behavior.FIND: "見つける",
            Behavior.FINISH: "終わる",
            Behavior.FEEL: "感じる",
            Behavior.FIB: "嘘をつく",
            Behavior.FIGHT: "戦う",
            Behavior.FILL: "満たす",
            Behavior.FIND: "見つける",
            Behavior.FIRE: "火を点ける",
            Behavior.FIREJOB: "首にする",
            Behavior.FLASH: "輝く",
            Behavior.FLOAT: "浮かぶ",
            Behavior.FLY: "飛ぶ",
            Behavior.FOLLOW: "ついていく",
            Behavior.FORGET: "忘れる",
            Behavior.FORGIVE: "許す",
            Behavior.FREEZE: "凍る",
            Behavior.FRY: "揚げる",
            Behavior.GATHER: "集める",
            Behavior.GAZE: "見つめる",
            Behavior.GET: "手に入れる",
            Behavior.GIVE: "与える",
            Behavior.GLAD: "嬉しい",
            Behavior.GO: "行く",
            Behavior.GRADUATE: "卒業する",
            Behavior.GREET: "挨拶する",
            Behavior.GROWL: "唸る",
            Behavior.GUARD: "守る",
            Behavior.GUESS: "思う",
            Behavior.GUIDE: "案内する",
            Behavior.HAND: "手を握る",
            Behavior.HANDLE: "操作する",
            Behavior.HANG: "掛ける",
            Behavior.HAPPEN: "起こる",
            Behavior.HAPPY: "幸せ",
            Behavior.HATE: "嫌う",
            Behavior.HAVE: "持つ",
            Behavior.HEAL: "癒やす",
            Behavior.HEAR: "聞く",
            Behavior.HELP: "助ける",
            Behavior.HIDE: "隠す",
            Behavior.HIRE: "雇う",
            Behavior.HIT: "打つ",
            Behavior.HOLD: "握る",
            Behavior.HOPE: "希望する",
            Behavior.HUG: "抱く",
            Behavior.HUNT: "狩る",
            Behavior.HURRY: "急ぐ",
            Behavior.HURT: "傷つける",
            Behavior.IGNORE: "無視する",
            Behavior.IMAGINE: "想像する",
            Behavior.INJURE: "負傷する",
            Behavior.INSTRUMENT: "楽器",
            Behavior.INTRODUCE: "紹介する",
            Behavior.INVEST: "投資する",
            Behavior.INVESTIGATE: "捜査する",
            Behavior.INVITE: "招く",
            Behavior.JOG: "ジョギングする",
            Behavior.JOIN: "加わる",
            Behavior.JUDGE: "審判する",
            Behavior.JUMP: "ジャンプする",
            Behavior.KEEP: "保つ",
            Behavior.KEYBOARD: "キィを打つ",
            Behavior.KICK: "蹴る",
            Behavior.KILL: "殺す",
            Behavior.KISS: "キスする",
            Behavior.KNIT: "編む",
            Behavior.KNOCK: "ノックする",
            Behavior.KNOW: "知る",
            Behavior.LAUGH: "笑う",
            Behavior.LAY: "横たえる",
            Behavior.LEARN: "学ぶ",
            Behavior.LEAVE: "残る",
            Behavior.LET: "させる",
            Behavior.LIE: "横たわる",
            Behavior.LIFE: "暮らす",
            Behavior.LIGHT: "明かりを点ける",
            Behavior.LISTEN: "聞く",
            Behavior.LIVE: "生きる",
            Behavior.LOOK: "見る",
            Behavior.LOOKDOWN: "俯く",
            Behavior.LOCK: "鍵を掛ける",
            Behavior.LOSE: "失う",
            Behavior.LOVE: "愛する",
            Behavior.MAKE: "作る",
            Behavior.MAKEUP: "化粧する",
            Behavior.MANAGE: "管理する",
            Behavior.MANUFACTURE: "製作する",
            behavior.MAON: "呻く",
            Behavior.MARK: "印をつける",
            Behavior.MARRY: "結婚する",
            Behavior.MASTER: "習得する",
            Behavior.MEASURE: "測る",
            Behavior.MEET: "会う",
            Behavior.MELT: "溶ける",
            Behavior.MEAN: "意味する",
            Behavior.MEMO: "メモする",
            Behavior.MISS: "ミスする",
            Behavior.MIX: "混ぜる",
            Behavior.MODIFY: "修正する",
            Behavior.MOVE: "移動する",
            Behavior.MUST: "しなければならない",
            Behavior.NEED: "必要とする",
            Behavior.NONE: "なし",
            Behavior.NOTICE: "気づく",
            Behavior.OBTAIN: "手に入れる",
            Behavior.OCCUR: "発生する",
            Behavior.OPEN: "開く",
            Behavior.OPPOSE: "反対する",
            Behavior.OVERCOME: "打開する",
            Behavior.OVERFLOW: "溢れる",
            Behavior.OVERLOOK: "見落とす",
            Behavior.OWN: "所有する",
            Behavior.PACK: "パックする",
            Behavior.PAINT: "塗る",
            Behavior.PASS: "通る",
            Behavior.PAUSE: "休止する",
            Behavior.PAY: "支払う",
            Behavior.PERFORM: "演じる",
            Behavior.PHONE: "電話する",
            Behavior.PLACE: "設置する",
            Behavior.PLAY: "遊ぶ",
            Behavior.PLUNGE: "突っ込む",
            Behavior.PRAY: "祈る",
            Behavior.PRACTICE: "練習する",
            Behavior.PRESS: "押す",
            Behavior.PRINT: "印刷する",
            Behavior.PROMISE: "約束する",
            Behavior.PUBLISH: "出版する",
            Behavior.PULL: "引く",
            Behavior.PUNCH: "殴る",
            Behavior.PUSH: "押す",
            Behavior.PUT: "置く",
            Behavior.PUZZLE: "困らせる",
            Behavior.REACH: "届く",
            Behavior.REACT: "反応する",
            Behavior.READ: "読む",
            Behavior.REALIZE: "認識する",
            Behavior.RECEIVE: "受け取る",
            Behavior.RECOMMEND: "勧める",
            Behavior.REFLECT: "反射する",
            Behavior.REFRESH: "リフレッシュする",
            Behavior.REGARD: "見做す",
            Behavior.REGRET: "後悔する",
            Behavior.RELEASE: "離す",
            Behavior.REMEMBER: "思い出す",
            Behavior.RENT: "貸す",
            Behavior.REPLY: "返事",
            Behavior.RESCUE: "救助する",
            Behavior.REST: "休む",
            Behavior.RETURN: "戻る",
            Behavior.REVIEW: "見直す",
            Behavior.RIDE: "乗る",
            Behavior.RING: "鳴る",
            Behavior.RISE: "上がる",
            Behavior.ROB: "奪う",
            Behavior.ROCK: "揺らす",
            Behavior.ROLL: "転がる",
            Behavior.RUB: "擦る",
            Behavior.RUN: "走る",
            Behavior.SACRIFICE: "犠牲になる",
            Behavior.SAD: "悲しむ",
            Behavior.SAVE: "保存する",
            Behavior.SAY: "言う",
            Behavior.SCARE: "怯える",
            Behavior.SCRATCH: "引っ掻く",
            Behavior.SCREAM: "悲鳴を上げる",
            Behavior.SEARCH: "探す",
            Behavior.SEAT: "座らせる",
            Behavior.SEE: "見る",
            Behavior.SEEK: "捜索する",
            Behavior.SEEM: "思える",
            Behavior.SELECT: "選択する",
            Behavior.SELL: "売る",
            Behavior.SEND: "送る",
            Behavior.SEPARATE: "散らばる",
            Behavior.SET: "セットする",
            Behavior.SHAKE: "振る",
            Behavior.SHARE: "分ける",
            Behavior.SHINE: "輝く",
            Behavior.SHOCK: "ショックを受ける",
            Behavior.SHOOT: "撃つ",
            Behavior.SHOW: "見せる",
            Behavior.SIGH: "嘆息する",
            Behavior.SIGN: "サインする",
            Behavior.SING: "歌う",
            Behavior.SINK: "沈む",
            Behavior.SIT: "座る",
            Behavior.SKATE: "スケートする",
            Behavior.SLEEP: "眠る",
            Behavior.SLICE: "スライスする",
            Behavior.SLIDE: "ずれる",
            Behavior.SLIP: "滑る",
            Behavior.SLOBBER: "垂らす",
            Behavior.SMELL: "匂う",
            Behavior.SMILE: "微笑する",
            Behavior.SMOKE: "煙草を吸う",
            Behavior.SOLVE: "解決する",
            Behavior.SOUND: "音が鳴る",
            Behavior.SPEAK: "声を出す",
            Behavior.SPEND: "費やす",
            Behavior.SPILL: "零す",
            Behavior.SPIN: "紡ぐ",
            Behavior.SPLIT: "裂ける",
            Behavior.SPREAD: "広まる",
            Behavior.SQUEEZE: "搾る",
            Behavior.STAND: "立つ",
            Behavior.STARE: "凝視する",
            Behavior.START: "開始する",
            Behavior.STAY: "留まる",
            Behavior.STEAL: "盗む",
            Behavior.STICK: "刺す",
            Behavior.STOP: "止まる",
            Behavior.STORE: "収める",
            Behavior.STUDY: "勉強する",
            Behavior.SUCCEED: "成功する",
            Behavior.SUGGEST: "提案する",
            Behavior.SUPPLY: "供給する",
            Behavior.SUPPORT: "サポートする",
            Behavior.SUPPOSE: "想定する",
            Behavior.SURPRISE: "驚かす",
            Behavior.SURROUND: "囲む",
            Behavior.SURVIVE: "生き残る",
            Behavior.SWEAR: "誓う",
            Behavior.SWEEP: "掃く",
            Behavior.SWIM: "泳ぐ",
            Behavior.SWING: "振る",
            Behavior.SWORD: "剣を振るう",
            Behavior.TAKE: "連れて行く",
            Behavior.TALK: "話す",
            Behavior.TAP: "軽く叩く",
            Behavior.TEACH: "教える",
            Behavior.TELL: "台詞",
            Behavior.TEST: "テスト",
            Behavior.THANK: "感謝する",
            Behavior.THINK: "考える",
            Behavior.THROW: "投げる",
            Behavior.TIE: "結ぶ",
            Behavior.TOSS: "トスする",
            Behavior.TOUCH: "触れる",
            Behavior.TRAIN: "鍛える",
            Behavior.TRANSFER: "転移する",
            Behavior.TRANSFORM: "変形する",
            Behavior.TRAVEL: "旅行する",
            Behavior.TRIP: "旅に出る",
            Behavior.TRUST: "信頼する",
            Behavior.TRY: "挑戦する",
            Behavior.TURN: "向きを変える",
            Behavior.TWIST: "捻る",
            Behavior.UNDERSTAND: "理解する",
            Behavior.UNITE: "合わせる",
            Behavior.UNLOCK: "鍵を開ける",
            Behavior.USE: "使う",
            Behavior.VANISH: "消える",
            Behavior.VISIT: "訪れる",
            Behavior.WAIT: "待つ",
            Behavior.WAKE: "目覚める",
            Behavior.WALK: "歩く",
            Behavior.WANT: "したい",
            Behavior.WARM: "温める",
            Behavior.WASTE: "無駄にする",
            Behavior.WATCH: "視聴する",
            Behavior.WAVE: "波打つ",
            Behavior.WEAR: "着る",
            Behavior.WEIGH: "測る",
            Behavior.WELCOME: "歓迎する",
            Behavior.WHISPER: "囁く",
            Behavior.WIN: "勝つ",
            Behavior.WIND: "風に当てる",
            Behavior.WIPE: "拭く",
            Behavior.WISH: "願う",
            Behavior.WONDER: "不思議に思う",
            Behavior.WORK: "仕事する",
            Behavior.WORRY: "心配する",
            Behavior.WRY: "苦笑する",
            Behavior.WRITE: "書く",
            Behavior.YELL: "喚く",
            }[behavior]


def behav_type_of(behavior: Behavior) -> BehavType:
    return {
            Behavior.ACT: BehavType.DONE,
            Behavior.ACCEPT: BehavType.DEALT,
            Behavior.ACQUIRE: BehavType.DEALT,
            Behavior.ADD: BehavType.DEALT,
            Behavior.ADHERE: BehavType.DEALT,
            Behavior.ADVISE: BehavType.TALKED,
            Behavior.AGREE: BehavType.THOUGHT,
            Behavior.AIM: BehavType.DEALT,
            Behavior.ANGRY: BehavType.FELT,
            Behavior.APPEAR: BehavType.VIEWED,
            Behavior.APPLY: BehavType.DEALT,
            Behavior.ARRIVE: BehavType.MOVED,
            Behavior.ASK: BehavType.TALKED,
            Behavior.ATTACK: BehavType.DONE,
            Behavior.BAKE: BehavType.COOKED,
            Behavior.BE: BehavType.EXPRESSED,
            Behavior.BECOME: BehavType.EXPRESSED,
            Behavior.BEG: BehavType.DEALT,
            Behavior.BEGIN: BehavType.DONE,
            Behavior.BELIEVE: BehavType.THOUGHT,
            Behavior.BET: BehavType.DEALT,
            Behavior.BIND: BehavType.DEALT,
            Behavior.BORROW: BehavType.DEALT,
            Behavior.BREAK: BehavType.DONE,
            Behavior.BREATHE: BehavType.DONE,
            Behavior.BROW: BehavType.EXPRESSED,
            Behavior.BUILD: BehavType.DEALT,
            Behavior.BURN: BehavType.EXPRESSED,
            Behavior.BURST: BehavType.EXPRESSED,
            Behavior.BUY: BehavType.DEALT,
            Behavior.CALCULATE: BehavType.DEALT,
            Behavior.CALL: BehavType.DEALT,
            Behavior.CARE: BehavType.DEALT,
            Behavior.CARRY: BehavType.DEALT,
            Behavior.CATCH: BehavType.DEALT,
            Behavior.CHANGE: BehavType.EXPRESSED,
            Behavior.CHARM: BehavType.EXPRESSED,
            Behavior.CHECK: BehavType.DEALT,
            Behavior.CHEER: BehavType.DEALT,
            Behavior.CHOOSE: BehavType.DEALT,
            Behavior.CLEAN: BehavType.DEALT,
            Behavior.CLICK: BehavType.HANDLED,
            Behavior.CLIMB: BehavType.MOVED,
            Behavior.CLOSE: BehavType.DEALT,
            Behavior.CLOTHE: BehavType.DEALT,
            Behavior.COACH: BehavType.DEALT,
            Behavior.COME: BehavType.MOVED,
            Behavior.COMMAND: BehavType.DEALT,
            Behavior.COMPARE: BehavType.DEALT,
            Behavior.COMPLETE: BehavType.HANDLED,
            Behavior.CONFESS: BehavType.TALKED,
            Behavior.CONFUSE: BehavType.FELT,
            Behavior.CONTACT: BehavType.TALKED,
            Behavior.CONTINUE: BehavType.DONE,
            Behavior.COOPERATE: BehavType.DEALT,
            Behavior.COOK: BehavType.COOKED,
            Behavior.COUGH: BehavType.FELT,
            Behavior.CREATE: BehavType.DEALT,
            Behavior.CRY: BehavType.FELT,
            Behavior.CUT: BehavType.DEALT,
            Behavior.DANCE: BehavType.DEALT,
            Behavior.DEAL: BehavType.DEALT,
            Behavior.DECIDE: BehavType.THOUGHT,
            Behavior.DEFEAT: BehavType.DONE,
            Behavior.DEFINE: BehavType.DEALT,
            Behavior.DESTROY: BehavType.DONE,
            Behavior.DIE: BehavType.DONE,
            Behavior.DIG: BehavType.DEALT,
            Behavior.DISAPPEAR: BehavType.VIEWED,
            Behavior.DISAPPROVE: BehavType.THOUGHT,
            Behavior.DISLIKE: BehavType.THOUGHT,
            Behavior.DISPEL: BehavType.DEALT,
            Behavior.DISPLAY: BehavType.VIEWED,
            Behavior.DIVE: BehavType.MOVED,
            Behavior.DO: BehavType.DONE,
            Behavior.DOUBT: BehavType.THOUGHT,
            Behavior.DRAG: BehavType.DEALT,
            Behavior.DRAW: BehavType.DONE,
            Behavior.DREAM: BehavType.THOUGHT,
            Behavior.DRESS: BehavType.DEALT,
            Behavior.DRINK: BehavType.DEALT,
            Behavior.DRIVE: BehavType.HANDLED,
            Behavior.DROP: BehavType.DONE,
            Behavior.DRY: BehavType.DEALT,
            Behavior.EARN: BehavType.DEALT,
            Behavior.EAT: BehavType.DEALT,
            Behavior.EDUCATE: BehavType.DEALT,
            Behavior.EMAIL: BehavType.TALKED,
            Behavior.EMPLOY: BehavType.DEALT,
            Behavior.ENGAGE: BehavType.DEALT,
            Behavior.ENTER: BehavType.MOVED,
            Behavior.ENJOY: BehavType.FELT,
            Behavior.ENVY: BehavType.THOUGHT,
            Behavior.EQUIP: BehavType.DEALT,
            Behavior.ESCAPE: BehavType.MOVED,
            Behavior.EXCHANGE: BehavType.DEALT,
            Behavior.EXAMINE: BehavType.DEALT,
            Behavior.EXCITE: BehavType.FELT,
            Behavior.EXIST: BehavType.MOVED,
            Behavior.EXPECT: BehavType.THOUGHT,
            Behavior.EXPLAIN: BehavType.TALKED,
            Behavior.EXPLORE: BehavType.MOVED,
            Behavior.EXPRESS: BehavType.EXPRESSED,
            Behavior.FACE: BehavType.EXPRESSED,
            Behavior.FALL: BehavType.DONE,
            Behavior.FEEL: BehavType.FELT,
            Behavior.FIB: BehavType.TALKED,
            Behavior.FIGHT: BehavType.DONE,
            Behavior.FILL: BehavType.DEALT,
            Behavior.FIND: BehavType.DEALT,
            Behavior.FINISH: BehavType.DONE,
            Behavior.FIRE: BehavType.DONE,
            Behavior.FIREJOB: BehavType.DEALT,
            Behavior.FLASH: BehavType.EXPRESSED,
            Behavior.FLEE: BehavType.MOVED,
            Behavior.FLOAT: BehavType.MOVED,
            Behavior.FLY: BehavType.MOVED,
            Behavior.FOCUS: BehavType.EXPRESSED,
            Behavior.FOLD: BehavType.DONE,
            Behavior.FOLLOW: BehavType.MOVED,
            Behavior.FORGET: BehavType.THOUGHT,
            Behavior.FORGIVE: BehavType.THOUGHT,
            Behavior.FORM: BehavType.DEALT,
            Behavior.FREEZE: BehavType.EXPRESSED,
            Behavior.FRY: BehavType.COOKED,
            Behavior.GATHER: BehavType.DEALT,
            Behavior.GAZE: BehavType.EXPRESSED,
            Behavior.GET: BehavType.DEALT,
            Behavior.GIVE: BehavType.DEALT,
            Behavior.GLAD: BehavType.FELT,
            Behavior.GO: BehavType.MOVED,
            Behavior.GRADUATE: BehavType.DEALT,
            Behavior.GREET: BehavType.TALKED,
            Behavior.GUARD: BehavType.DONE,
            Behavior.GROWL: BehavType.TALKED,
            Behavior.GUESS: BehavType.THOUGHT,
            Behavior.GUIDE: BehavType.DEALT,
            Behavior.HAND: BehavType.DEALT,
            Behavior.HANDLE: BehavType.HANDLED,
            Behavior.HANG: BehavType.DEALT,
            Behavior.HAPPEN: BehavType.EXPRESSED,
            Behavior.HAPPY: BehavType.FELT,
            Behavior.HATE: BehavType.THOUGHT,
            Behavior.HAVE: BehavType.DONE,
            Behavior.HEAL: BehavType.DEALT,
            Behavior.HEAR: BehavType.TALKED,
            Behavior.HELP: BehavType.DEALT,
            Behavior.HIDE: BehavType.DEALT,
            Behavior.HIRE: BehavType.DEALT,
            Behavior.HIT: BehavType.DONE,
            Behavior.HOLD: BehavType.DONE,
            Behavior.HOPE: BehavType.THOUGHT,
            Behavior.HUG: BehavType.DONE,
            Behavior.HUNT: BehavType.DEALT,
            Behavior.HURRY: BehavType.FELT,
            Behavior.HURT: BehavType.DEALT,
            Behavior.IGNORE: BehavType.THOUGHT,
            Behavior.IMAGINE: BehavType.THOUGHT,
            Behavior.INJURE: BehavType.DEALT,
            Behavior.INSTRUMENT: BehavType.DEALT,
            Behavior.INVEST: BehavType.DEALT,
            Behavior.INVESTIGATE: BehavType.DEALT,
            Behavior.INVITE: BehavType.DEALT,
            Behavior.INTRODUCE: BehavType.TALKED,
            Behavior.JOG: BehavType.MOVED,
            Behavior.JOIN: BehavType.THOUGHT,
            Behavior.JUMP: BehavType.DONE,
            Behavior.KEEP: BehavType.EXPRESSED,
            Behavior.KEYBOARD: BehavType.HANDLED,
            Behavior.KICK: BehavType.DONE,
            Behavior.KILL: BehavType.DONE,
            Behavior.KISS: BehavType.DONE,
            Behavior.KNIT: BehavType.DEALT,
            Behavior.KNOCK: BehavType.DEALT,
            Behavior.KNOW: BehavType.THOUGHT,
            Behavior.LAUGH: BehavType.TALKED,
            Behavior.LAY: BehavType.DONE,
            Behavior.LEARN: BehavType.THOUGHT,
            Behavior.LEAVE: BehavType.DEALT,
            Behavior.LET: BehavType.DEALT,
            Behavior.LIE: BehavType.DONE,
            Behavior.LIFE: BehavType.DONE,
            Behavior.LIGHT: BehavType.HANDLED,
            Behavior.LIKE: BehavType.THOUGHT,
            Behavior.LISTEN: BehavType.TALKED,
            Behavior.LIVE: BehavType.DONE,
            Behavior.LOOK: BehavType.VIEWED,
            Behavior.LOOKDOWN: BehavType.VIEWED,
            Behavior.LOCK: BehavType.HANDLED,
            Behavior.LOSE: BehavType.DEALT,
            Behavior.LOVE: BehavType.THOUGHT,
            Behavior.MAKE: BehavType.DONE,
            Behavior.MAKEUP: BehavType.DEALT,
            Behavior.MANAGE: BehavType.DEALT,
            Behavior.MANUFACTURE: BehavType.DEALT,
            Behavior.MAON: BehavType.TALKED,
            Behavior.MARK: BehavType.DEALT,
            Behavior.MARRY: BehavType.DEALT,
            Behavior.MASTER: BehavType.DONE,
            Behavior.MEAN: BehavType.THOUGHT,
            Behavior.MEASURE: BehavType.DEALT,
            Behavior.MEET: BehavType.DEALT,
            Behavior.MELT: BehavType.DONE,
            Behavior.MEMO: BehavType.DEALT,
            Behavior.MISS: BehavType.DONE,
            Behavior.MODIFY: BehavType.DEALT,
            Behavior.MOVE: BehavType.MOVED,
            Behavior.MUST: BehavType.THOUGHT,
            Behavior.NEED: BehavType.THOUGHT,
            Behavior.NONE: BehavType.DONE,
            Behavior.NOTICE: BehavType.THOUGHT,
            Behavior.OBTAIN: BehavType.DEALT,
            Behavior.OCCUR: BehavType.DONE,
            Behavior.OPEN: BehavType.DEALT,
            Behavior.OPERATE: BehavType.HANDLED,
            Behavior.OPPOSE: BehavType.THOUGHT,
            Behavior.ORGANIZE: BehavType.DEALT,
            Behavior.OVERCOME: BehavType.DEALT,
            Behavior.OVERFLOW: BehavType.EXPRESSED,
            Behavior.OVERLOOK: BehavType.VIEWED,
            Behavior.OWN: BehavType.DEALT,
            Behavior.PACK: BehavType.DEALT,
            Behavior.PAINT: BehavType.DEALT,
            Behavior.PASS: BehavType.MOVED,
            Behavior.PAT: BehavType.DONE,
            Behavior.PAUSE: BehavType.DONE,
            Behavior.PAY: BehavType.DEALT,
            Behavior.PERFORM: BehavType.MOVED,
            Behavior.PHONE: BehavType.TALKED,
            Behavior.PICK: BehavType.DEALT,
            Behavior.PLACE: BehavType.DONE,
            Behavior.PLAY: BehavType.DONE,
            Behavior.PLUNGE: BehavType.DONE,
            Behavior.PRACTICE: BehavType.DONE,
            Behavior.PRAY: BehavType.THOUGHT,
            Behavior.PRESS: BehavType.HANDLED,
            Behavior.PRINT: BehavType.DEALT,
            Behavior.PROMISE: BehavType.THOUGHT,
            Behavior.PROTECT: BehavType.DONE,
            Behavior.PUBLISH: BehavType.DEALT,
            Behavior.PULL: BehavType.DONE,
            Behavior.PUNCH: BehavType.DONE,
            Behavior.PUSH: BehavType.DONE,
            Behavior.PUT: BehavType.DONE,
            Behavior.PUZZLE: BehavType.THOUGHT,
            Behavior.REACH: BehavType.MOVED,
            Behavior.REACT: BehavType.FELT,
            Behavior.READ: BehavType.DEALT,
            Behavior.REALIZE: BehavType.FELT,
            Behavior.RECEIVE: BehavType.DEALT,
            Behavior.RECOMMEND: BehavType.THOUGHT,
            Behavior.REFLECT: BehavType.DEALT,
            Behavior.REFRESH: BehavType.FELT,
            Behavior.REGARD: BehavType.THOUGHT,
            Behavior.REGRET: BehavType.THOUGHT,
            Behavior.REMEMBER: BehavType.THOUGHT,
            Behavior.RENT: BehavType.DEALT,
            Behavior.REPLY: BehavType.TALKED,
            Behavior.RESCUE: BehavType.DEALT,
            Behavior.REST: BehavType.DONE,
            Behavior.RETURN: BehavType.MOVED,
            Behavior.REVIEW: BehavType.DEALT,
            Behavior.RIDE: BehavType.HANDLED,
            Behavior.RING: BehavType.DONE,
            Behavior.RISE: BehavType.MOVED,
            Behavior.ROB: BehavType.DEALT,
            Behavior.ROCK: BehavType.DEALT,
            Behavior.ROLL: BehavType.DEALT,
            Behavior.RUB: BehavType.DEALT,
            Behavior.RUN: BehavType.MOVED,
            Behavior.SACRIFICE: BehavType.THOUGHT,
            Behavior.SAD: BehavType.FELT,
            Behavior.SAVE: BehavType.DEALT,
            Behavior.SAY: BehavType.TALKED,
            Behavior.SCARE: BehavType.FELT,
            Behavior.SCRATCH: BehavType.DONE,
            Behavior.SCREAM: BehavType.TALKED,
            Behavior.SEARCH: BehavType.DEALT,
            Behavior.SEAT: BehavType.MOVED,
            Behavior.SEE: BehavType.VIEWED,
            Behavior.SEEK: BehavType.DEALT,
            Behavior.SEEM: BehavType.THOUGHT,
            Behavior.SELECT: BehavType.THOUGHT,
            Behavior.SELL: BehavType.DEALT,
            Behavior.SEND: BehavType.DEALT,
            Behavior.SEPARATE: BehavType.DEALT,
            Behavior.SHARE: BehavType.DEALT,
            Behavior.SHAKE: BehavType.DONE,
            Behavior.SET: BehavType.HANDLED,
            Behavior.SHINE: BehavType.EXPRESSED,
            Behavior.SHOCK: BehavType.FELT,
            Behavior.SHOOT: BehavType.HANDLED,
            Behavior.SHOUT: BehavType.TALKED,
            Behavior.SHOW: BehavType.VIEWED,
            Behavior.SIGH: BehavType.DONE,
            Behavior.SIGN: BehavType.DEALT,
            Behavior.SING: BehavType.DONE,
            Behavior.SINK: BehavType.EXPRESSED,
            Behavior.SIT: BehavType.MOVED,
            Behavior.SKATE: BehavType.DONE,
            Behavior.SLEEP: BehavType.DONE,
            Behavior.SLICE: BehavType.DEALT,
            Behavior.SLIDE: BehavType.DEALT,
            Behavior.SLIP: BehavType.DONE,
            Behavior.SLOBBER: BehavType.DONE,
            Behavior.SMELL: BehavType.DEALT,
            Behavior.SMILE: BehavType.EXPRESSED,
            Behavior.SMOKE: BehavType.DONE,
            Behavior.SOLVE: BehavType.DEALT,
            Behavior.SOUND: BehavType.HANDLED,
            Behavior.SPEAK: BehavType.EXPRESSED,
            Behavior.SPEND: BehavType.DEALT,
            Behavior.SPILL: BehavType.EXPRESSED,
            Behavior.SPIN: BehavType.DONE,
            Behavior.SPLIT: BehavType.DEALT,
            Behavior.SPREAD: BehavType.EXPRESSED,
            Behavior.SQUEEZE: BehavType.DEALT,
            Behavior.STAND: BehavType.MOVED,
            Behavior.STARE: BehavType.VIEWED,
            Behavior.START: BehavType.HANDLED,
            Behavior.STAY: BehavType.DONE,
            Behavior.STEAL: BehavType.DEALT,
            Behavior.STICK: BehavType.DONE,
            Behavior.STOP: BehavType.HANDLED,
            Behavior.STORE: BehavType.DEALT,
            Behavior.STUDY: BehavType.DONE,
            Behavior.SUCCEED: BehavType.THOUGHT,
            Behavior.SUGGEST: BehavType.THOUGHT,
            Behavior.SUPPLY: BehavType.DEALT,
            Behavior.SUPPORT: BehavType.DEALT,
            Behavior.SUPPOSE: BehavType.THOUGHT,
            Behavior.SURPRISE: BehavType.FELT,
            Behavior.SURROUND: BehavType.MOVED,
            Behavior.SURVIVE: BehavType.DONE,
            Behavior.SWEAR: BehavType.THOUGHT,
            Behavior.SWEEP: BehavType.DONE,
            Behavior.SWIM: BehavType.DONE,
            Behavior.SWING: BehavType.DONE,
            Behavior.SWORD: BehavType.DONE,
            Behavior.TAKE: BehavType.DEALT,
            Behavior.TALK: BehavType.TALKED,
            Behavior.TAP: BehavType.DONE,
            Behavior.TEACH: BehavType.DEALT,
            Behavior.TELL: BehavType.DIALOGUE,
            Behavior.TEST: BehavType.DONE,
            Behavior.THANK: BehavType.THOUGHT,
            Behavior.THINK: BehavType.THOUGHT,
            Behavior.THROW: BehavType.DEALT,
            Behavior.TIE: BehavType.DONE,
            Behavior.TOSS: BehavType.DEALT,
            Behavior.TOUCH: BehavType.DONE,
            Behavior.TRAIN: BehavType.DEALT,
            Behavior.TRANSFER: BehavType.DEALT,
            Behavior.TRANSFORM: BehavType.DONE,
            Behavior.TRAVEL: BehavType.MOVED,
            Behavior.TREAT: BehavType.DEALT,
            Behavior.TRIP: BehavType.MOVED,
            Behavior.TRUST: BehavType.THOUGHT,
            Behavior.TRY: BehavType.THOUGHT,
            Behavior.TURN: BehavType.MOVED,
            Behavior.TWIST: BehavType.MOVED,
            Behavior.UNDERSTAND: BehavType.THOUGHT,
            Behavior.UNITE: BehavType.EXPRESSED,
            Behavior.UNLOCK: BehavType.HANDLED,
            Behavior.USE: BehavType.DEALT,
            Behavior.VANISH: BehavType.EXPRESSED,
            Behavior.VIEW: BehavType.VIEWED,
            Behavior.VISIT: BehavType.MOVED,
            Behavior.WAIT: BehavType.THOUGHT,
            Behavior.WAKE: BehavType.DONE,
            Behavior.WALK: BehavType.MOVED,
            Behavior.WANT: BehavType.THOUGHT,
            Behavior.WARM: BehavType.DEALT,
            Behavior.WASTE: BehavType.THOUGHT,
            Behavior.WATCH: BehavType.VIEWED,
            Behavior.WAVE: BehavType.DONE,
            Behavior.WEAR: BehavType.DEALT,
            Behavior.WEIGH: BehavType.DEALT,
            Behavior.WELCOME: BehavType.THOUGHT,
            Behavior.WHISPER: BehavType.TALKED,
            Behavior.WIN: BehavType.THOUGHT,
            Behavior.WIND: BehavType.EXPRESSED,
            Behavior.WIPE: BehavType.DONE,
            Behavior.WISH: BehavType.THOUGHT,
            Behavior.WONDER: BehavType.THOUGHT,
            Behavior.WORK: BehavType.DONE,
            Behavior.WORRY: BehavType.THOUGHT,
            Behavior.WRITE: BehavType.DONE,
            Behavior.WRY: BehavType.TALKED,
            Behavior.YELL: BehavType.TALKED,
            }[behavior]
