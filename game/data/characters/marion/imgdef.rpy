############# marion expressions #################
image marion angry  = Composite((690, 1360), CHAR_OFFSET.MARION, "marion_body", CHAR_OFFSET.MARION, "images/characters/marion/face/angry.webp")
image marion bitelip= Composite((690, 1360), CHAR_OFFSET.MARION, "marion_body", CHAR_OFFSET.MARION, "images/characters/marion/face/bitelip.webp")
image marion blush  = Composite((690, 1360), CHAR_OFFSET.MARION, "marion_body", CHAR_OFFSET.MARION, "images/characters/marion/face/blush.webp")
image marion cry    = Composite((690, 1360), CHAR_OFFSET.MARION, "marion_body", CHAR_OFFSET.MARION, "images/characters/marion/face/cry.webp")
image marion fury   = Composite((690, 1360), CHAR_OFFSET.MARION, "marion_body", CHAR_OFFSET.MARION, "images/characters/marion/face/fury.webp")
image marion laugh  = Composite((690, 1360), CHAR_OFFSET.MARION, "marion_body", CHAR_OFFSET.MARION, "images/characters/marion/face/laugh.webp")
image marion sad    = Composite((690, 1360), CHAR_OFFSET.MARION, "marion_body", CHAR_OFFSET.MARION, "images/characters/marion/face/sad.webp")
image marion smile  = Composite((690, 1360), CHAR_OFFSET.MARION, "marion_body", CHAR_OFFSET.MARION, "images/characters/marion/face/smile.webp")
image marion think  = Composite((690, 1360), CHAR_OFFSET.MARION, "marion_body", CHAR_OFFSET.MARION, "images/characters/marion/face/think.webp")
image marion talk = "marion" # stub
###############################################
image marion = Composite((690, 1360), CHAR_OFFSET.MARION, "marion_body")
image marion_body = ConditionSwitch(
    "worldChars['marion']['clothes'] == 'naked'",   "marion_naked",
    "worldChars['marion']['clothes'] == 'ling'",    "marion_ling",
    "True",  "marion_normal",
)

image marion_normal = ConditionSwitch(
    "worldChars['marion']['preg'] == 0", "images/characters/marion/normal.webp",
    "worldChars['marion']['preg'] == 1", "images/characters/marion/preg/normal_1.webp",
    "worldChars['marion']['preg'] == 2", "images/characters/marion/preg/normal_2.webp",
    "worldChars['marion']['preg'] == 3", "images/characters/marion/preg/normal_3.webp",
    "worldChars['marion']['preg'] == 4", "images/characters/marion/preg/normal_3.webp")

image marion_naked = ConditionSwitch(
    "worldChars['marion']['preg'] == 0", "images/characters/marion/naked.webp",
    "worldChars['marion']['preg'] == 1", "images/characters/marion/preg/naked_1.webp",
    "worldChars['marion']['preg'] == 2", "images/characters/marion/preg/naked_2.webp",
    "worldChars['marion']['preg'] == 3", "images/characters/marion/preg/naked_3.webp",
    "worldChars['marion']['preg'] == 4", "images/characters/marion/preg/naked_3.webp")

image marion_ling = ConditionSwitch(
    "worldChars['marion']['preg'] == 0", "images/characters/marion/ling.webp",
    "worldChars['marion']['preg'] == 1", "images/characters/marion/preg/ling_1.webp",
    "worldChars['marion']['preg'] == 2", "images/characters/marion/preg/ling_2.webp",
    "worldChars['marion']['preg'] == 3", "images/characters/marion/preg/ling_3.webp",
    "worldChars['marion']['preg'] == 4", "images/characters/marion/preg/ling_3.webp")