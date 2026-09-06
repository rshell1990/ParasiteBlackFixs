################# mika expressions ##############
image mika angry = Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body", CHAR_OFFSET.MIKA, "images/characters/mika/face/angry.webp")
image mika think = Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body", CHAR_OFFSET.MIKA, "images/characters/mika/face/think.webp")
image mika drunk = Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body", CHAR_OFFSET.MIKA, "images/characters/mika/face/drunk.webp")
image mika blush = Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body", CHAR_OFFSET.MIKA, "images/characters/mika/face/blush.webp")
image mika cry   = Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body", CHAR_OFFSET.MIKA, "images/characters/mika/face/cry.webp")
image mika laugh = Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body", CHAR_OFFSET.MIKA, "images/characters/mika/face/laugh.webp")
image mika lewd  = Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body", CHAR_OFFSET.MIKA, "images/characters/mika/face/lewd.webp")
image mika sad   = Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body", CHAR_OFFSET.MIKA, "images/characters/mika/face/sad.webp")
image mika scared= Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body", CHAR_OFFSET.MIKA, "images/characters/mika/face/scared.webp")
image mika shock = Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body", CHAR_OFFSET.MIKA, "images/characters/mika/face/shock.webp")
image mika smile = Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body", CHAR_OFFSET.MIKA, "images/characters/mika/face/smile.webp")
image mika talk = "mika"
##################################################
image mika = Composite((601, 1400), CHAR_OFFSET.MIKA, "mika_body")

image mika_body = ConditionSwitch(
    "worldChars['mika']['clothes'] == 'boner'", "images/characters/mika/boner.webp",
    "worldChars['mika']['clothes'] == 'naked'", "mika_body_naked",
    "worldChars['mika']['clothes'] == 'ling1'", "images/characters/mika/ling_1.webp",
    "worldChars['mika']['clothes'] == 'ling2'", "images/characters/mika/ling_2.webp",
    "worldChars['mika']['clothes'] == 'dress'", "mika_body_dress",
    "worldChars['mika']['clothes'] == 'towel'", "images/characters/mika/towel.webp",
    "worldChars['mika']['clothes'] == 'towel_water'", "images/characters/mika/towel_water.webp",
    "worldChars['mika']['clothes'] == 'towel_wet'", "images/characters/mika/towel_wet.webp",
    "worldChars['mika']['clothes'] == 'water'", "images/characters/mika/water.webp",
    "worldChars['mika']['clothes'] == 'wet'", "images/characters/mika/wet.webp",
    "worldChars['mika']['clothes'] == 'bare_tits'", "images/characters/mika/bare_tits.webp",
    "True", "mika_body_dress",
)

image mika_body_naked = ConditionSwitch(
    "worldChars['mika']['preg'] == 0", "images/characters/mika/naked.webp",
    "worldChars['mika']['preg'] == 1", "images/characters/mika/preg/naked_1.webp",
    "worldChars['mika']['preg'] == 2", "images/characters/mika/preg/naked_2.webp",
    "worldChars['mika']['preg'] == 3", "images/characters/mika/preg/naked_3.webp",
    "worldChars['mika']['preg'] == 4", "images/characters/mika/naked.webp")
image mika_body_dress = ConditionSwitch(
    "worldChars['mika']['preg'] == 0", "images/characters/mika/dress.webp",
    "worldChars['mika']['preg'] == 1", "images/characters/mika/preg/dress_1.webp",
    "worldChars['mika']['preg'] == 2", "images/characters/mika/preg/dress_2.webp",
    "worldChars['mika']['preg'] == 3", "images/characters/mika/preg/dress_3.webp",
    "worldChars['mika']['preg'] == 4", "images/characters/mika/preg/dress_4.webp")


image cg_mika_baby = Composite((601, 1400), CHAR_OFFSET.MIKA, "images/characters/mika/cgs/cg_mika_baby_base.webp")