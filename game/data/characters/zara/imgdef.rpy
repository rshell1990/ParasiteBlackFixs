################# zara expressions ##############
image zara angry    = Composite((695, 1400), CHAR_OFFSET.ZARA, "zara_body", CHAR_OFFSET.ZARA, "images/characters/zara/face/angry.webp")
image zara angry_blush = Composite((695, 1400), CHAR_OFFSET.ZARA, "zara_body", CHAR_OFFSET.ZARA, "images/characters/zara/face/angry_blush.webp")
image zara blush    = Composite((695, 1400), CHAR_OFFSET.ZARA, "zara_body", CHAR_OFFSET.ZARA, "images/characters/zara/face/blush.webp")
image zara cry_blush= Composite((695, 1400), CHAR_OFFSET.ZARA, "zara_body", CHAR_OFFSET.ZARA, "images/characters/zara/face/cry_blush.webp")
image zara laugh    = Composite((695, 1400), CHAR_OFFSET.ZARA, "zara_body", CHAR_OFFSET.ZARA, "images/characters/zara/face/laugh.webp")
image zara shock    = Composite((695, 1400), CHAR_OFFSET.ZARA, "zara_body", CHAR_OFFSET.ZARA, "images/characters/zara/face/shock.webp")
image zara lewd     = Composite((695, 1400), CHAR_OFFSET.ZARA, "zara_body", CHAR_OFFSET.ZARA, "images/characters/zara/face/lewd.webp")
image zara sad      = Composite((695, 1400), CHAR_OFFSET.ZARA, "zara_body", CHAR_OFFSET.ZARA, "images/characters/zara/face/sad.webp")
image zara smile    = Composite((695, 1400), CHAR_OFFSET.ZARA, "zara_body", CHAR_OFFSET.ZARA, "images/characters/zara/face/smile.webp")
image zara think    = Composite((695, 1400), CHAR_OFFSET.ZARA, "zara_body", CHAR_OFFSET.ZARA, "images/characters/zara/face/think.webp")
image zara talk = "zara" # ph
##################################################
image zara = Composite((695, 1400), CHAR_OFFSET.ZARA, "zara_body")
image zara_body = ConditionSwitch(
    "worldChars['zara']['clothes'] == 'naked'", "images/characters/zara/naked.webp",
    "worldChars['zara']['clothes'] == 'ling'", "images/characters/zara/ling.webp",
    "worldChars['zara']['clothes'] == 'dress'", "images/characters/zara/dress.webp",
    "True", "images/characters/zara/normal.webp",
)
