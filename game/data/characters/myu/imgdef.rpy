############# myu expressions ############
image myu talk  = Composite((930, 1400), CHAR_OFFSET.MYU, "myu_body", CHAR_OFFSET.MYU, "myu_animtalk")
image myu angry = Composite((930, 1400), CHAR_OFFSET.MYU, "myu_body", CHAR_OFFSET.MYU, "images/characters/myu/face/angry.webp")
image myu blush = Composite((930, 1400), CHAR_OFFSET.MYU, "myu_body", CHAR_OFFSET.MYU, "images/characters/myu/face/blush.webp")
image myu joy   = Composite((930, 1400), CHAR_OFFSET.MYU, "myu_body", CHAR_OFFSET.MYU, "images/characters/myu/face/joy.webp")
image myu laugh = Composite((930, 1400), CHAR_OFFSET.MYU, "myu_body", CHAR_OFFSET.MYU, "images/characters/myu/face/laugh.webp")
image myu sad   = Composite((930, 1400), CHAR_OFFSET.MYU, "myu_body", CHAR_OFFSET.MYU, "images/characters/myu/face/sad.webp")
image myu scared= Composite((930, 1400), CHAR_OFFSET.MYU, "myu_body", CHAR_OFFSET.MYU, "images/characters/myu/face/scared.webp")
image myu smile = Composite((930, 1400), CHAR_OFFSET.MYU, "myu_body", CHAR_OFFSET.MYU, "images/characters/myu/face/smile.webp")
image myu think = Composite((930, 1400), CHAR_OFFSET.MYU, "myu_body", CHAR_OFFSET.MYU, "images/characters/myu/face/think.webp")
##############################################
image myu = Composite((930, 1400), CHAR_OFFSET.MYU, "myu_body")
image myu_body = ConditionSwitch(
    "worldChars['myu']['preg'] == 0", "images/characters/myu/normal.webp",
    "worldChars['myu']['preg'] == 1", "images/characters/myu/preg1.webp",
    "worldChars['myu']['preg'] == 2", "images/characters/myu/preg2.webp",
    "worldChars['myu']['preg'] == 3", "images/characters/myu/preg3.webp",
    "worldChars['myu']['preg'] == 4", "images/characters/myu/normal.webp")
image myu_animtalk:
    Null()

image cg_myu_monster:
    "cg_myu_monster_base"
    offset CHAR_OFFSET.MYU

image cg_myu_monster_blood:
    "cg_myu_monster_blood_base"
    offset CHAR_OFFSET.MYU

image cg_myu_baby:
    "cg_myu_baby_base"
    offset CHAR_OFFSET.MYU

image cg_myu_bimbo:
    "cg_myu_bimbo_base"
    offset CHAR_OFFSET.MYU
image cg_myu_bimbo_blush:
    "cg_myu_bimbo_blush_base"
    offset CHAR_OFFSET.MYU
