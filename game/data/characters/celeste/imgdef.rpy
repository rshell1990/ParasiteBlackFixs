############# celeste expressions #############
image celeste angry = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/angry.webp")
image celeste blush = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/blush.webp")
image celeste happy = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/happy.webp")
image celeste laugh = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/laugh.webp")
image celeste lewd  = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/lewd.webp")
image celeste sad   = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/sad.webp")
image celeste think = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/think.webp")
############# celeste psycho expressions #######
image celeste p_fury    = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/p_fury.webp")
image celeste p_laugh   = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/p_laugh.webp")
image celeste p_laugh2  = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/p_laugh2.webp")
image celeste p_laugh3  = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/p_laugh3.webp")
image celeste p_lewd    = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/p_lewd.webp")
image celeste p_sad    = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body", CHAR_OFFSET.CELESTE, "images/characters/celeste/face/p_sad.webp")
image celeste talk = "celeste"
################################################
image celeste = Composite((1118, 1270), CHAR_OFFSET.CELESTE, "celeste_body")
image celeste_body = ConditionSwitch(
    "worldChars['celeste']['clothes'] == 'sword'", "images/characters/celeste/sword.webp",
    "worldChars['celeste']['clothes'] == 'naked'", "images/characters/celeste/naked.webp",
    "True", "images/characters/celeste/normal.webp",
)



