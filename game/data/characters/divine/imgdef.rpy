################### sister divine expressions #########
image divine angry  = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/angry.webp")
image divine cry    = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/cry.webp")
image divine embar  = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/embar.webp")
image divine fury   = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/fury.webp")
image divine happy  = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/happy.webp")
image divine laugh  = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/laugh.webp")
image divine srs    = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/srs.webp")
image divine lewd   = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/lewd.webp")
image divine sad    = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/sad.webp")
image divine scared = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/scared.webp")
image divine shock  = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/shock.webp")
image divine think  = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body", CHAR_OFFSET.DIVINE, "images/characters/divine/face/think.webp")
image divine talk = "divine"
#####################################################
image divine = Composite((675, 1461), CHAR_OFFSET.DIVINE, "divine_body")
# ph
image divine_body = ConditionSwitch(
        "worldChars['divine']['clothes'] == 'naked'", "divine_naked",
        "worldChars['divine']['clothes'] == 'water'", "divine_water",
        "worldChars['divine']['clothes'] == 'wet'", "divine_wet",
        "worldChars['divine']['clothes'] == 'towel'", "divine_towel",
        "worldChars['divine']['clothes'] == 'towel_wet'", "divine_towel_wet",
        "worldChars['divine']['clothes'] == 'towel_water'", "divine_towel_water",
        "worldChars['divine']['clothes'] == 'ling'", "divine_lingerie",
        "True", "divine_normal",
)

image divine_normal = ConditionSwitch(
        "worldChars['divine']['preg'] == 0", "images/characters/divine/dress.webp",
        "worldChars['divine']['preg'] == 1", "images/characters/divine/preg/dress_1.webp",
        "worldChars['divine']['preg'] == 2", "images/characters/divine/preg/dress_2.webp",
        "worldChars['divine']['preg'] == 3", "images/characters/divine/preg/dress_3.webp",
        "worldChars['divine']['preg'] == 4", "images/characters/divine/baby.webp")
image divine_naked = ConditionSwitch(
        "worldChars['divine']['preg'] == 0", "images/characters/divine/naked.webp",
        "worldChars['divine']['preg'] == 1", "images/characters/divine/preg/naked_1.webp",
        "worldChars['divine']['preg'] == 2", "images/characters/divine/preg/naked_2.webp",
        "worldChars['divine']['preg'] == 3", "images/characters/divine/preg/naked_3.webp",
        "worldChars['divine']['preg'] == 4", "images/characters/divine/baby.webp")
image divine_lingerie = ConditionSwitch(
        "worldChars['divine']['preg'] == 0", "images/characters/divine/ling.webp",
        "worldChars['divine']['preg'] == 1", "images/characters/divine/preg/ling_1.webp",
        "worldChars['divine']['preg'] == 2", "images/characters/divine/preg/ling_2.webp",
        "worldChars['divine']['preg'] == 3", "images/characters/divine/preg/ling_3.webp",
        "worldChars['divine']['preg'] == 4", "images/characters/divine/baby.webp")
image divine_water = ConditionSwitch(
        "worldChars['divine']['preg'] == 0", "images/characters/divine/water.webp",
        "worldChars['divine']['preg'] == 1", "images/characters/divine/preg/water_1.webp",
        "worldChars['divine']['preg'] == 2", "images/characters/divine/preg/water_2.webp",
        "worldChars['divine']['preg'] == 3", "images/characters/divine/preg/water_3.webp",
        "worldChars['divine']['preg'] == 4", "images/characters/divine/baby.webp")
image divine_wet = ConditionSwitch(
        "worldChars['divine']['preg'] == 0", "images/characters/divine/wet.webp",
        "worldChars['divine']['preg'] == 1", "images/characters/divine/preg/wet_1.webp",
        "worldChars['divine']['preg'] == 2", "images/characters/divine/preg/wet_2.webp",
        "worldChars['divine']['preg'] == 3", "images/characters/divine/preg/wet_3.webp",
        "worldChars['divine']['preg'] == 4", "images/characters/divine/baby.webp")
image divine_towel = ConditionSwitch(
        "worldChars['divine']['preg'] == 0", "images/characters/divine/towel.webp",
        "worldChars['divine']['preg'] == 1", "images/characters/divine/preg/towel_1.webp",
        "worldChars['divine']['preg'] == 2", "images/characters/divine/preg/towel_2.webp",
        "worldChars['divine']['preg'] == 3", "images/characters/divine/preg/towel_3.webp",
        "worldChars['divine']['preg'] == 4", "images/characters/divine/baby.webp")
image divine_towel_wet = ConditionSwitch(
        "worldChars['divine']['preg'] == 0", "images/characters/divine/towel_wet.webp",
        "worldChars['divine']['preg'] == 1", "images/characters/divine/preg/towel_wet_1.webp",
        "worldChars['divine']['preg'] == 2", "images/characters/divine/preg/towel_wet_2.webp",
        "worldChars['divine']['preg'] == 3", "images/characters/divine/preg/towel_wet_3.webp",
        "worldChars['divine']['preg'] == 4", "images/characters/divine/baby.webp")
image divine_towel_water = ConditionSwitch(
        "worldChars['divine']['preg'] == 0", "images/characters/divine/towel_water.webp",
        "worldChars['divine']['preg'] == 1", "images/characters/divine/preg/towel_water_1.webp",
        "worldChars['divine']['preg'] == 2", "images/characters/divine/preg/towel_water_2.webp",
        "worldChars['divine']['preg'] == 3", "images/characters/divine/preg/towel_water_3.webp",
        "worldChars['divine']['preg'] == 4", "images/characters/divine/baby.webp")