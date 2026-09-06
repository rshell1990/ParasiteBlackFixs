################### green lizard expressions #########
image lizard_green angry    = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_green_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/green/face/angry.webp")
image lizard_green happy    = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_green_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/green/face/happy.webp")
image lizard_green lewd     = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_green_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/green/face/lewd.webp")
image lizard_green sad      = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_green_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/green/face/sad.webp")
image lizard_green scared   = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_green_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/green/face/scared.webp")
image lizard_green shock    = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_green_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/green/face/shock.webp")
#####################################################
image lizard_green = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_green_body")
image lizard_green_body = ConditionSwitch(
    "worldChars['lizard_green']['hair'] == 'normal'",   "lizard_green_hair",
    "worldChars['lizard_green']['hair'] == 'bald'",     "lizard_green_bald")

image lizard_green_bald = ConditionSwitch(
    "worldChars['lizard_green']['preg'] == 0", "images/characters/lizard_girls/green/bald.webp",
    "worldChars['lizard_green']['preg'] == 1", "images/characters/lizard_girls/green/preg/bald_1.webp",
    "worldChars['lizard_green']['preg'] == 2", "images/characters/lizard_girls/green/preg/bald_2.webp",
    "worldChars['lizard_green']['preg'] == 3", "images/characters/lizard_girls/green/preg/bald_3.webp",
    "worldChars['lizard_green']['preg'] == 4", "images/characters/lizard_girls/green/preg/bald_4.webp")
image lizard_green_hair = ConditionSwitch(
    "worldChars['lizard_green']['preg'] == 0", "images/characters/lizard_girls/green/hair.webp",
    "worldChars['lizard_green']['preg'] == 1", "images/characters/lizard_girls/green/preg/hair_1.webp",
    "worldChars['lizard_green']['preg'] == 2", "images/characters/lizard_girls/green/preg/hair_2.webp",
    "worldChars['lizard_green']['preg'] == 3", "images/characters/lizard_girls/green/preg/hair_3.webp",
    "worldChars['lizard_green']['preg'] == 4", "images/characters/lizard_girls/green/preg/hair_4.webp")