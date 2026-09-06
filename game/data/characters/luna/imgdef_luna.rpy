############# luna expressions #################
image luna angry    = Composite((675, 1238), CHAR_OFFSET.LUNA, "luna_body", CHAR_OFFSET.LUNA, "images/characters/luna/face/angry.webp")
image luna cry      = Composite((675, 1238), CHAR_OFFSET.LUNA, "luna_body", CHAR_OFFSET.LUNA, "images/characters/luna/face/cry.webp")
image luna lookaway = Composite((675, 1238), CHAR_OFFSET.LUNA, "luna_body", CHAR_OFFSET.LUNA, "images/characters/luna/face/lookaway.webp")
image luna sad      = Composite((675, 1238), CHAR_OFFSET.LUNA, "luna_body", CHAR_OFFSET.LUNA, "images/characters/luna/face/sad.webp")
image luna sad2     = Composite((675, 1238), CHAR_OFFSET.LUNA, "luna_body", CHAR_OFFSET.LUNA, "images/characters/luna/face/sad2.webp")
image luna sassy    = Composite((675, 1238), CHAR_OFFSET.LUNA, "luna_body", CHAR_OFFSET.LUNA, "images/characters/luna/face/sassy.webp")
image luna scary    = Composite((675, 1238), CHAR_OFFSET.LUNA, "luna_body", CHAR_OFFSET.LUNA, "images/characters/luna/face/scary.webp")
image luna smile    = Composite((675, 1238), CHAR_OFFSET.LUNA, "luna_body", CHAR_OFFSET.LUNA, "images/characters/luna/face/smile.webp")
image luna talk = "luna"
###############################################
image luna = Composite((675, 1238), CHAR_OFFSET.LUNA, "luna_body")
image luna_body = ConditionSwitch(
    "worldChars['luna']['clothes'] == 'naked'",     "luna_naked",
    "worldChars['luna']['clothes'] == 'ling'",      "luna_ling",
    "True",    "luna_normal",
)

image luna_normal = ConditionSwitch(
    "worldChars['luna']['preg'] == 0", "images/characters/luna/normal.webp",
    "worldChars['luna']['preg'] == 1", "images/characters/luna/preg/normal_1.webp",
    "worldChars['luna']['preg'] == 2", "images/characters/luna/preg/normal_2.webp",
    "worldChars['luna']['preg'] == 3", "images/characters/luna/preg/normal_3.webp",
    "worldChars['luna']['preg'] == 4", "images/characters/luna/preg/normal_baby.webp")

image luna_naked = ConditionSwitch(
    "worldChars['luna']['preg'] == 0", "images/characters/luna/naked.webp",
    "worldChars['luna']['preg'] == 1", "images/characters/luna/preg/naked_1.webp",
    "worldChars['luna']['preg'] == 2", "images/characters/luna/preg/naked_2.webp",
    "worldChars['luna']['preg'] == 3", "images/characters/luna/preg/naked_3.webp",
    "worldChars['luna']['preg'] == 4", "images/characters/luna/naked.webp")

image luna_ling = ConditionSwitch(
    "worldChars['luna']['preg'] == 0", "images/characters/luna/ling.webp",
    "worldChars['luna']['preg'] == 1", "images/characters/luna/preg/ling_1.webp",
    "worldChars['luna']['preg'] == 2", "images/characters/luna/preg/ling_2.webp",
    "worldChars['luna']['preg'] == 3", "images/characters/luna/preg/ling_3.webp",
    "worldChars['luna']['preg'] == 4", "images/characters/luna/ling.webp")