##################### shay expressions #############
image shay talk     = Composite((503, 1377), CHAR_OFFSET.SHAY, "shay_body", CHAR_OFFSET.SHAY, "shay_animtalk")
image shay angry    = Composite((503, 1377), CHAR_OFFSET.SHAY, "shay_body", CHAR_OFFSET.SHAY, "images/characters/shay/face/angry.webp")
image shay shock    = Composite((503, 1377), CHAR_OFFSET.SHAY, "shay_body", CHAR_OFFSET.SHAY, "images/characters/shay/face/shock.webp")
image shay shy      = Composite((503, 1377), CHAR_OFFSET.SHAY, "shay_body", CHAR_OFFSET.SHAY, "images/characters/shay/face/shy.webp")
image shay smile    = Composite((503, 1377), CHAR_OFFSET.SHAY, "shay_body", CHAR_OFFSET.SHAY, "images/characters/shay/face/smile.webp")
image shay smile2   = Composite((503, 1377), CHAR_OFFSET.SHAY, "shay_body", CHAR_OFFSET.SHAY, "images/characters/shay/face/smile2.webp")
image shay think    = Composite((503, 1377), CHAR_OFFSET.SHAY, "shay_body", CHAR_OFFSET.SHAY, "images/characters/shay/face/think.webp")
image shay what     = Composite((503, 1377), CHAR_OFFSET.SHAY, "shay_body", CHAR_OFFSET.SHAY, "images/characters/shay/face/what.webp")
#######################################################
image shay = Composite((503, 1377), CHAR_OFFSET.SHAY, "shay_body")
image shay_body = ConditionSwitch(
    "worldChars['shani']['clothes'] == 'ling'",  "shay_ling",
    "worldChars['shani']['clothes'] == 'naked'", "shay_naked",
    "True",                                      "shay_normal",
)

image shay_ling = ConditionSwitch(
    "worldChars['shay']['preg'] == 0", "images/characters/shay/ling.webp",
    "worldChars['shay']['preg'] == 1", "images/characters/shay/preg/ling1.webp",
    "worldChars['shay']['preg'] == 2", "images/characters/shay/preg/ling2.webp",
    "worldChars['shay']['preg'] == 3", "images/characters/shay/preg/ling3.webp",
    "worldChars['shay']['preg'] == 4", "images/characters/shay/ling.webp"
)
image shay_naked = ConditionSwitch(
    "worldChars['shay']['preg'] == 0", "images/characters/shay/naked.webp",
    "worldChars['shay']['preg'] == 1", "images/characters/shay/preg/naked1.webp",
    "worldChars['shay']['preg'] == 2", "images/characters/shay/preg/naked2.webp",
    "worldChars['shay']['preg'] == 3", "images/characters/shay/preg/naked3.webp",
    "worldChars['shay']['preg'] == 4", "images/characters/shay/naked.webp"
)
image shay_normal = ConditionSwitch(
    "worldChars['shay']['preg'] == 0", "images/characters/shay/normal.webp",
    "worldChars['shay']['preg'] == 1", "images/characters/shay/preg/normal1.webp",
    "worldChars['shay']['preg'] == 2", "images/characters/shay/preg/normal2.webp",
    "worldChars['shay']['preg'] == 3", "images/characters/shay/preg/normal3.webp",
    "worldChars['shay']['preg'] == 4", "images/characters/shay/normal.webp"
)

image shay_animtalk:
    Null()
image shay_animblink:
    Null()
