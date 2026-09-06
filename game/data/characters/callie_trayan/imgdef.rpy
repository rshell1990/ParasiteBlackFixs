############# callie expressions #################
image callie talk =     Composite((695, 1400), CHAR_OFFSET.CALLIE, "callie_body", CHAR_OFFSET.CALLIE, "callie_talk")
image callie angry =    Composite((695, 1400), CHAR_OFFSET.CALLIE, "callie_body", CHAR_OFFSET.CALLIE, "images/characters/callie/face/angry.webp")
image callie blush =    Composite((695, 1400), CHAR_OFFSET.CALLIE, "callie_body", CHAR_OFFSET.CALLIE, "images/characters/callie/face/blush.webp")
image callie happy =    Composite((695, 1400), CHAR_OFFSET.CALLIE, "callie_body", CHAR_OFFSET.CALLIE, "images/characters/callie/face/happy.webp")
image callie laugh =    Composite((695, 1400), CHAR_OFFSET.CALLIE, "callie_body", CHAR_OFFSET.CALLIE, "images/characters/callie/face/laugh.webp")
image callie lewd =     Composite((695, 1400), CHAR_OFFSET.CALLIE, "callie_body", CHAR_OFFSET.CALLIE, "images/characters/callie/face/lewd.webp")
image callie sad =      Composite((695, 1400), CHAR_OFFSET.CALLIE, "callie_body", CHAR_OFFSET.CALLIE, "images/characters/callie/face/sad.webp")
###############################################
image callie = Composite((695, 1400), CHAR_OFFSET.CALLIE, "callie_body")
image callie_body = ConditionSwitch(
    "worldChars['callie']['clothes'] == 'naked'", "images/characters/callie/naked.webp",
    "worldChars['callie']['clothes'] == 'ling'", "images/characters/callie/ling.webp",
    "True", "images/characters/callie/normal.webp",
)
# stub
image callie_talk = Null()

############# trayan expressions #################
image trayan talk =     Composite((695, 1400), CHAR_OFFSET.TRAYAN, "trayan_body", CHAR_OFFSET.TRAYAN, "trayan_talk")
image trayan angry =    Composite((695, 1400), CHAR_OFFSET.TRAYAN, "trayan_body", CHAR_OFFSET.TRAYAN, "images/characters/trayan/face/angry.webp")
image trayan blush =    Composite((695, 1400), CHAR_OFFSET.TRAYAN, "trayan_body", CHAR_OFFSET.TRAYAN, "images/characters/trayan/face/blush.webp")
image trayan horny =    Composite((695, 1400), CHAR_OFFSET.TRAYAN, "trayan_body", CHAR_OFFSET.TRAYAN, "images/characters/trayan/face/horny.webp")
image trayan sad =      Composite((695, 1400), CHAR_OFFSET.TRAYAN, "trayan_body", CHAR_OFFSET.TRAYAN, "images/characters/trayan/face/sad.webp")
image trayan smile =    Composite((695, 1400), CHAR_OFFSET.TRAYAN, "trayan_body", CHAR_OFFSET.TRAYAN, "images/characters/trayan/face/smile.webp")
image trayan smile2 =   Composite((695, 1400), CHAR_OFFSET.TRAYAN, "trayan_body", CHAR_OFFSET.TRAYAN, "images/characters/trayan/face/smile_2.webp")
###############################################
image trayan = Composite((695, 1400), CHAR_OFFSET.TRAYAN, "trayan_body")
image trayan_body = ConditionSwitch(
    "worldChars['trayan']['clothes'] == 'naked'", "images/characters/trayan/naked.webp",
    "worldChars['trayan']['clothes'] == 'ling'", "images/characters/trayan/ling.webp",
    "True", "images/characters/trayan/normal.webp",
)
# stub
image trayan_talk = Null()
