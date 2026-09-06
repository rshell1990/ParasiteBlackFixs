############# cecilia expressions #################
image cecilia angry = Composite((587, 1223), CHAR_OFFSET.PRINCESS_CECILIA, "cecilia_body", CHAR_OFFSET.PRINCESS_CECILIA, "images/characters/cecilia/face/angry.webp")
image cecilia blush = Composite((587, 1223), CHAR_OFFSET.PRINCESS_CECILIA, "cecilia_body", CHAR_OFFSET.PRINCESS_CECILIA, "images/characters/cecilia/face/blush.webp")
image cecilia cry   = Composite((587, 1223), CHAR_OFFSET.PRINCESS_CECILIA, "cecilia_body", CHAR_OFFSET.PRINCESS_CECILIA, "images/characters/cecilia/face/cry.webp")
image cecilia happy = Composite((587, 1223), CHAR_OFFSET.PRINCESS_CECILIA, "cecilia_body", CHAR_OFFSET.PRINCESS_CECILIA, "images/characters/cecilia/face/happy.webp")
image cecilia laugh = Composite((587, 1223), CHAR_OFFSET.PRINCESS_CECILIA, "cecilia_body", CHAR_OFFSET.PRINCESS_CECILIA, "images/characters/cecilia/face/laugh.webp")
image cecilia lewd  = Composite((587, 1223), CHAR_OFFSET.PRINCESS_CECILIA, "cecilia_body", CHAR_OFFSET.PRINCESS_CECILIA, "images/characters/cecilia/face/lewd.webp")
image cecilia sad   = Composite((587, 1223), CHAR_OFFSET.PRINCESS_CECILIA, "cecilia_body", CHAR_OFFSET.PRINCESS_CECILIA, "images/characters/cecilia/face/sad.webp")
image cecilia scared    = Composite((587, 1223), CHAR_OFFSET.PRINCESS_CECILIA, "cecilia_body", CHAR_OFFSET.PRINCESS_CECILIA, "images/characters/cecilia/face/scared.webp")
image cecilia serious   = Composite((587, 1223), CHAR_OFFSET.PRINCESS_CECILIA, "cecilia_body", CHAR_OFFSET.PRINCESS_CECILIA, "images/characters/cecilia/face/serious.webp")
image cecilia shocked   = Composite((587, 1223), CHAR_OFFSET.PRINCESS_CECILIA, "cecilia_body", CHAR_OFFSET.PRINCESS_CECILIA, "images/characters/cecilia/face/shocked.webp")
###############################################
image cecilia = Composite((587, 1223), CHAR_OFFSET.PRINCESS_CECILIA, "cecilia_body")
image cecilia_body = ConditionSwitch(
    "worldChars['cecilia']['clothes'] == 'naked'",  "cecilia_naked",
    "True", "cecilia_normal",
)
image cecilia_normal = "images/characters/cecilia/normal.webp"
image cecilia_naked = "images/characters/cecilia/naked.webp"