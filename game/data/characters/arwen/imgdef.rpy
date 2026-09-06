############# arwen expressions ###############
image arwen angry = Composite((695, 1400), CHAR_OFFSET.ARWEN, "arwen_body", CHAR_OFFSET.ARWEN, "images/characters/arwen/face/angry.webp")
image arwen blush = Composite((695, 1400), CHAR_OFFSET.ARWEN, "arwen_body", CHAR_OFFSET.ARWEN, "images/characters/arwen/face/blush.webp")
image arwen happy = Composite((695, 1400), CHAR_OFFSET.ARWEN, "arwen_body", CHAR_OFFSET.ARWEN, "images/characters/arwen/face/happy.webp")
image arwen laugh = Composite((695, 1400), CHAR_OFFSET.ARWEN, "arwen_body", CHAR_OFFSET.ARWEN, "images/characters/arwen/face/laugh.webp")
image arwen sad =   Composite((695, 1400), CHAR_OFFSET.ARWEN, "arwen_body", CHAR_OFFSET.ARWEN, "images/characters/arwen/face/sad.webp")
image arwen scared =Composite((695, 1400), CHAR_OFFSET.ARWEN, "arwen_body", CHAR_OFFSET.ARWEN, "images/characters/arwen/face/scared.webp")
image arwen think = Composite((695, 1400), CHAR_OFFSET.ARWEN, "arwen_body", CHAR_OFFSET.ARWEN, "images/characters/arwen/face/think.webp")
image arwen talk =  Composite((695, 1400), CHAR_OFFSET.ARWEN, "arwen_body", CHAR_OFFSET.ARWEN, "arwen_animtalk")
################################################
image arwen = Composite((695, 1400), CHAR_OFFSET.ARWEN, "arwen_body", CHAR_OFFSET.ARWEN, "arwen_animblink")

image arwen_body = ConditionSwitch(
    "worldChars['arwen']['clothes'] == 'celeste'",  "images/characters/arwen/celeste.webp",
    "worldChars['arwen']['clothes'] == 'naked'",    "images/characters/arwen/naked.webp",
    "True",   "images/characters/arwen/base.webp",
)

# stubs
image arwen_animblink:
    Null()
image arwen_animtalk:
    Null()
