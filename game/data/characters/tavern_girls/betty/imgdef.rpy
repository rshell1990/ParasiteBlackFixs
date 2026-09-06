image betty angry  = Composite((900, 1544), CHAR_OFFSET.BETTY, "betty_body", CHAR_OFFSET.BETTY, "images/characters/betty/face/angry.webp")
image betty blush  = Composite((900, 1544), CHAR_OFFSET.BETTY, "betty_body", CHAR_OFFSET.BETTY, "images/characters/betty/face/blush.webp")
image betty cry    = Composite((900, 1544), CHAR_OFFSET.BETTY, "betty_body", CHAR_OFFSET.BETTY, "images/characters/betty/face/cry.webp")
image betty sad    = Composite((900, 1544), CHAR_OFFSET.BETTY, "betty_body", CHAR_OFFSET.BETTY, "images/characters/betty/face/sad.webp")
image betty scared = Composite((900, 1544), CHAR_OFFSET.BETTY, "betty_body", CHAR_OFFSET.BETTY, "images/characters/betty/face/scared.webp")
image betty think  = Composite((900, 1544), CHAR_OFFSET.BETTY, "betty_body", CHAR_OFFSET.BETTY, "images/characters/betty/face/think.webp")
image betty shock  = Composite((900, 1544), CHAR_OFFSET.BETTY, "betty_body", CHAR_OFFSET.BETTY, "images/characters/betty/face/shock.webp")
image betty happy  = Composite((900, 1544), CHAR_OFFSET.BETTY, "betty_body", CHAR_OFFSET.BETTY, "images/characters/betty/face/happy.webp")
image betty smile  = "betty happy"
image betty flirt  = "betty blush"
image betty lewd   = "betty blush"
image betty laugh  = Composite((900, 1544), CHAR_OFFSET.BETTY, "betty_body", CHAR_OFFSET.BETTY, "images/characters/betty/face/laugh.webp")
image betty lust   = Composite((900, 1544), CHAR_OFFSET.BETTY, "betty_body", CHAR_OFFSET.BETTY, "images/characters/betty/face/lust.webp")
image betty talk   = "betty happy"

#################################################

image betty = Composite((900, 1544), CHAR_OFFSET.BETTY, "betty_body")

image betty_body = ConditionSwitch(
    "worldChars['betty']['clothes'] == 'naked'", "betty_naked",
    "worldChars['betty']['clothes'] == 'normal_tray'", "betty_normal_tray",
    "True", "betty_normal")

image betty_normal = ConditionSwitch(
    "worldChars['betty']['preg'] == 0", "images/characters/betty/normal.webp",
    "worldChars['betty']['preg'] == 1", "images/characters/betty/preg/normal_1.webp",
    "worldChars['betty']['preg'] == 2", "images/characters/betty/preg/normal_2.webp",
    "worldChars['betty']['preg'] == 3", "images/characters/betty/preg/normal_3.webp",
    "worldChars['betty']['preg'] == 4", "images/characters/betty/preg/normal_4.webp")

image betty_normal_tray = ConditionSwitch(
    "worldChars['betty']['preg'] == 0", "images/characters/betty/normal_tray.webp",
    "worldChars['betty']['preg'] == 1", "images/characters/betty/preg/normal_tray_1.webp",
    "worldChars['betty']['preg'] == 2", "images/characters/betty/preg/normal_tray_2.webp",
    "worldChars['betty']['preg'] == 3", "images/characters/betty/preg/normal_tray_3.webp",
    "worldChars['betty']['preg'] == 4", "images/characters/betty/normal_tray.webp")

image betty_naked = ConditionSwitch(
    "worldChars['betty']['preg'] == 0", "images/characters/betty/naked.webp",
    "worldChars['betty']['preg'] == 1", "images/characters/betty/preg/naked_1.webp",
    "worldChars['betty']['preg'] == 2", "images/characters/betty/preg/naked_2.webp",
    "worldChars['betty']['preg'] == 3", "images/characters/betty/preg/naked_3.webp",
    "worldChars['betty']['preg'] == 4", "images/characters/betty/naked.webp")