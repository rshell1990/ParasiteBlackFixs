################### red lizard expressions #########
image lizard_red angry  = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_red_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/red/face/angry.webp")
image lizard_red happy  = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_red_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/red/face/happy.webp")
image lizard_red lewd   = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_red_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/red/face/lewd.webp")
image lizard_red sad    = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_red_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/red/face/sad.webp")
image lizard_red scared = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_red_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/red/face/scared.webp")
image lizard_red shock  = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_red_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/red/face/shock.webp")
#####################################################
image lizard_red = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_red_body")
image lizard_red_body = ConditionSwitch(
    "worldChars['lizard_red']['hair'] == 'normal'", "lizard_red_hair",
    "worldChars['lizard_red']['hair'] == 'bald'", "lizard_red_bald")

image lizard_red_bald = ConditionSwitch(
    "worldChars['lizard_red']['preg'] == 0", "images/characters/lizard_girls/red/bald.webp",
    "worldChars['lizard_red']['preg'] == 1", "images/characters/lizard_girls/red/preg/bald_1.webp",
    "worldChars['lizard_red']['preg'] == 2", "images/characters/lizard_girls/red/preg/bald_2.webp",
    "worldChars['lizard_red']['preg'] == 3", "images/characters/lizard_girls/red/preg/bald_3.webp",
    "worldChars['lizard_red']['preg'] == 4", "images/characters/lizard_girls/red/preg/bald_4.webp")
image lizard_red_hair = ConditionSwitch(
    "worldChars['lizard_red']['preg'] == 0", "images/characters/lizard_girls/red/hair.webp",
    "worldChars['lizard_red']['preg'] == 1", "images/characters/lizard_girls/red/preg/hair_1.webp",
    "worldChars['lizard_red']['preg'] == 2", "images/characters/lizard_girls/red/preg/hair_2.webp",
    "worldChars['lizard_red']['preg'] == 3", "images/characters/lizard_girls/red/preg/hair_3.webp",
    "worldChars['lizard_red']['preg'] == 4", "images/characters/lizard_girls/red/preg/hair_4.webp")