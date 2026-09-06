################### blue lizard expressions #########
image lizard_blue angry = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_blue_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/blue/face/angry.webp")
image lizard_blue happy = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_blue_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/blue/face/happy.webp")
image lizard_blue lewd  = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_blue_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/blue/face/lewd.webp")
image lizard_blue sad   = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_blue_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/blue/face/sad.webp")
image lizard_blue scared= Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_blue_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/blue/face/scared.webp")
image lizard_blue shock = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_blue_body", CHAR_OFFSET.LIZARD, "images/characters/lizard_girls/blue/face/shock.webp")
#####################################################
image lizard_blue = Composite((695, 1400), CHAR_OFFSET.LIZARD, "lizard_blue_body")
image lizard_blue_body = ConditionSwitch(
    "worldChars['lizard_blue']['hair'] == 'normal'",    "lizard_blue_hair",
    "worldChars['lizard_blue']['hair'] == 'bald'",      "lizard_blue_bald")

image lizard_blue_bald = ConditionSwitch(
    "worldChars['lizard_blue']['preg'] == 0", "images/characters/lizard_girls/blue/bald.webp",
    "worldChars['lizard_blue']['preg'] == 1", "images/characters/lizard_girls/blue/preg/bald_1.webp",
    "worldChars['lizard_blue']['preg'] == 2", "images/characters/lizard_girls/blue/preg/bald_2.webp",
    "worldChars['lizard_blue']['preg'] == 3", "images/characters/lizard_girls/blue/preg/bald_3.webp",
    "worldChars['lizard_blue']['preg'] == 4", "images/characters/lizard_girls/blue/preg/bald_4.webp")
image lizard_blue_hair = ConditionSwitch(
    "worldChars['lizard_blue']['preg'] == 0", "images/characters/lizard_girls/blue/hair.webp",
    "worldChars['lizard_blue']['preg'] == 1", "images/characters/lizard_girls/blue/preg/hair_1.webp",
    "worldChars['lizard_blue']['preg'] == 2", "images/characters/lizard_girls/blue/preg/hair_2.webp",
    "worldChars['lizard_blue']['preg'] == 3", "images/characters/lizard_girls/blue/preg/hair_3.webp",
    "worldChars['lizard_blue']['preg'] == 4", "images/characters/lizard_girls/blue/preg/hair_4.webp")