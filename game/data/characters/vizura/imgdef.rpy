################### vizura expressions #########
image vizura talk   = Composite((488, 917), CHAR_OFFSET.VIZURA, "vizura_body")
image vizura angry  = Composite((488, 917), CHAR_OFFSET.VIZURA, "vizura_body", CHAR_OFFSET.VIZURA, "images/characters/vizura/face/angry.webp")
image vizura cry    = Composite((488, 917), CHAR_OFFSET.VIZURA, "vizura_body", CHAR_OFFSET.VIZURA, "images/characters/vizura/face/cry.webp")
image vizura happy  = Composite((488, 917), CHAR_OFFSET.VIZURA, "vizura_body", CHAR_OFFSET.VIZURA, "images/characters/vizura/face/happy.webp")
image vizura laugh  = Composite((488, 917), CHAR_OFFSET.VIZURA, "vizura_body", CHAR_OFFSET.VIZURA, "images/characters/vizura/face/laugh.webp")
image vizura lewd   = Composite((488, 917), CHAR_OFFSET.VIZURA, "vizura_body", CHAR_OFFSET.VIZURA, "images/characters/vizura/face/lewd.webp")
image vizura sad    = Composite((488, 917), CHAR_OFFSET.VIZURA, "vizura_body", CHAR_OFFSET.VIZURA, "images/characters/vizura/face/sad.webp")
image vizura scared = Composite((488, 917), CHAR_OFFSET.VIZURA, "vizura_body", CHAR_OFFSET.VIZURA, "images/characters/vizura/face/scared.webp")
image vizura surp   = Composite((488, 917), CHAR_OFFSET.VIZURA, "vizura_body", CHAR_OFFSET.VIZURA, "images/characters/vizura/face/surp.webp")
image vizura think  = Composite((488, 917), CHAR_OFFSET.VIZURA, "vizura_body", CHAR_OFFSET.VIZURA, "images/characters/vizura/face/think.webp")
#####################################################
image vizura = Composite((488, 917), CHAR_OFFSET.VIZURA, "vizura_body")
image vizura_body = ConditionSwitch(
    "worldChars['vizura']['clothes'] == 'naked'",   "vizura_naked",
    "True",  "vizura_normal",
)

image vizura_normal = ConditionSwitch(
    "worldChars['vizura']['preg'] == 0", "images/characters/vizura/normal.webp",
    "worldChars['vizura']['preg'] == 1", "images/characters/vizura/preg/normal_1.webp",
    "worldChars['vizura']['preg'] == 2", "images/characters/vizura/preg/normal_2.webp",
    "worldChars['vizura']['preg'] == 3", "images/characters/vizura/preg/normal_3.webp",
    "worldChars['vizura']['preg'] == 4", "images/characters/vizura/preg/baby.webp")

image vizura_naked = ConditionSwitch(
    "worldChars['vizura']['preg'] == 0", "images/characters/vizura/naked.webp",
    "worldChars['vizura']['preg'] == 1", "images/characters/vizura/preg/naked_1.webp",
    "worldChars['vizura']['preg'] == 2", "images/characters/vizura/preg/naked_2.webp",
    "worldChars['vizura']['preg'] == 3", "images/characters/vizura/preg/naked_3.webp",
    "worldChars['vizura']['preg'] == 4", "images/characters/vizura/naked.webp") # she ditches the baby along with ehr clothes!