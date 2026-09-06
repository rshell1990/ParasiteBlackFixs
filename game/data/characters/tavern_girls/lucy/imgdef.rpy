image lucy angry  = Composite((692, 1546), CHAR_OFFSET.LUCY, "lucy_body", CHAR_OFFSET.LUCY, "images/characters/lucy/face/angry.webp")
image lucy blush  = Composite((692, 1546), CHAR_OFFSET.LUCY, "lucy_body", CHAR_OFFSET.LUCY, "images/characters/lucy/face/blush.webp")
image lucy cry    = Composite((692, 1546), CHAR_OFFSET.LUCY, "lucy_body", CHAR_OFFSET.LUCY, "images/characters/lucy/face/cry.webp")
image lucy sad    = Composite((692, 1546), CHAR_OFFSET.LUCY, "lucy_body", CHAR_OFFSET.LUCY, "images/characters/lucy/face/sad.webp")
image lucy scared = Composite((692, 1546), CHAR_OFFSET.LUCY, "lucy_body", CHAR_OFFSET.LUCY, "images/characters/lucy/face/scared.webp")
image lucy think  = Composite((692, 1546), CHAR_OFFSET.LUCY, "lucy_body", CHAR_OFFSET.LUCY, "images/characters/lucy/face/think.webp")
image lucy shock  = Composite((692, 1546), CHAR_OFFSET.LUCY, "lucy_body", CHAR_OFFSET.LUCY, "images/characters/lucy/face/shock.webp")
image lucy surprised = "lucy shock"
image lucy emb    = "lucy blush"
image lucy happy  = Composite((692, 1546), CHAR_OFFSET.LUCY, "lucy_body", CHAR_OFFSET.LUCY, "images/characters/lucy/face/happy.webp")
image lucy smile  = "lucy happy"
image lucy laugh  = Composite((692, 1546), CHAR_OFFSET.LUCY, "lucy_body", CHAR_OFFSET.LUCY, "images/characters/lucy/face/laugh.webp")
image lucy lust   = Composite((692, 1546), CHAR_OFFSET.LUCY, "lucy_body", CHAR_OFFSET.LUCY, "images/characters/lucy/face/lust.webp")
image lucy talk   = "lucy happy"

#################################################

image lucy = Composite((692, 1546), CHAR_OFFSET.LUCY, "lucy_body")

image lucy_body = ConditionSwitch(
    "worldChars['lucy']['clothes'] == 'naked'", "lucy_naked",
    "True", "lucy_normal")

image lucy_normal = ConditionSwitch(
    "worldChars['lucy']['preg'] == 0", "images/characters/lucy/normal.webp",
    "worldChars['lucy']['preg'] == 1", "images/characters/lucy/preg/normal_1.webp",
    "worldChars['lucy']['preg'] == 2", "images/characters/lucy/preg/normal_2.webp",
    "worldChars['lucy']['preg'] == 3", "images/characters/lucy/preg/normal_3.webp",
    "worldChars['lucy']['preg'] == 4", "images/characters/lucy/preg/normal_4.webp")

image lucy_naked = ConditionSwitch(
    "worldChars['lucy']['preg'] == 0", "images/characters/lucy/naked.webp",
    "worldChars['lucy']['preg'] == 1", "images/characters/lucy/preg/naked_1.webp",
    "worldChars['lucy']['preg'] == 2", "images/characters/lucy/preg/naked_2.webp",
    "worldChars['lucy']['preg'] == 3", "images/characters/lucy/preg/naked_3.webp",
    "worldChars['lucy']['preg'] == 4", "images/characters/lucy/naked.webp")