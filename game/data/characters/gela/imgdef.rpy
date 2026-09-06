################### gela expressions #########
image gela angry = Composite((514, 1358), CHAR_OFFSET.GELA, "gela_body", CHAR_OFFSET.GELA, "images/characters/gela/face/angry.webp")
image gela horny = Composite((514, 1358), CHAR_OFFSET.GELA, "gela_body", CHAR_OFFSET.GELA, "images/characters/gela/face/horny.webp")
image gela sad   = Composite((514, 1358), CHAR_OFFSET.GELA, "gela_body", CHAR_OFFSET.GELA, "images/characters/gela/face/sad.webp")
#############################################
image gela talk = "gela"
image gela = Composite((514, 1358), CHAR_OFFSET.GELA, "gela_body")
image gela_body = ConditionSwitch(
    "worldChars['gela']['clothes'] == 'blades'", "images/characters/gela/blades.webp",
    "True",                                      "images/characters/gela/normal.webp")
