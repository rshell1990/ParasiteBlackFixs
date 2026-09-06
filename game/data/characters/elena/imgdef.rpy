############### elena expressions ############
image elena angry   = Composite((850, 1340), CHAR_OFFSET.ELENA, "elena_body", CHAR_OFFSET.ELENA, "images/characters/elena/face/face_angry.webp")
image elena grumpy  = Composite((850, 1340), CHAR_OFFSET.ELENA, "elena_body", CHAR_OFFSET.ELENA, "images/characters/elena/face/face_grumpy.webp")
image elena lewd    = Composite((850, 1340), CHAR_OFFSET.ELENA, "elena_body", CHAR_OFFSET.ELENA, "images/characters/elena/face/face_lewd.webp")
image elena sad     = Composite((850, 1340), CHAR_OFFSET.ELENA, "elena_body", CHAR_OFFSET.ELENA, "images/characters/elena/face/face_sad.webp")
image elena shock   = Composite((850, 1340), CHAR_OFFSET.ELENA, "elena_body", CHAR_OFFSET.ELENA, "images/characters/elena/face/face_shock.webp")
image elena smile   = Composite((850, 1340), CHAR_OFFSET.ELENA, "elena_body", CHAR_OFFSET.ELENA, "images/characters/elena/face/face_smile.webp")
image elena cry     = Composite((850, 1340), CHAR_OFFSET.ELENA, "elena_body", CHAR_OFFSET.ELENA, "images/characters/elena/face/face_crying.webp")
image elena talk    = Composite((850, 1340), CHAR_OFFSET.ELENA, "elena_body", CHAR_OFFSET.ELENA, "elena_animtalk")
#############################################
image elena = Composite((850, 1340), CHAR_OFFSET.ELENA, "elena_body")

image elena_body = ConditionSwitch(
        "worldChars['elena']['clothes'] == 'naked'",    "elena_naked",
        "worldChars['elena']['clothes'] == 'ling'",     "elena_ling",
        "worldChars['elena']['clothes'] == 'rags'",     "elena_rags",
        "worldChars['elena']['clothes'] == 'apron'",    "images/characters/elena/apron.webp",
        "True",   "images/characters/elena/base.webp",
)

image elena_ling = ConditionSwitch(
        "worldChars['elena']['preg'] == 0", "images/characters/elena/lingerie.webp",
        "worldChars['elena']['preg'] == 1", "images/characters/elena/preg/lingerie_preg1.webp",
        "worldChars['elena']['preg'] == 2", "images/characters/elena/preg/lingerie_preg2.webp",
        "worldChars['elena']['preg'] == 3", "images/characters/elena/preg/lingerie_preg3.webp")

image elena_naked = ConditionSwitch(
        "worldChars['elena']['preg'] == 0", "images/characters/elena/naked.webp",
        "worldChars['elena']['preg'] == 1", "images/characters/elena/preg/naked_preg1.webp",
        "worldChars['elena']['preg'] == 2", "images/characters/elena/preg/naked_preg2.webp",
        "worldChars['elena']['preg'] == 3", "images/characters/elena/preg/naked_preg3.webp")

image elena_rags = ConditionSwitch(
        "worldChars['elena']['preg'] == 0", "images/characters/elena/rags.webp",
        "worldChars['elena']['preg'] == 1", "images/characters/elena/preg/rags_preg1.webp",
        "worldChars['elena']['preg'] == 2", "images/characters/elena/preg/rags_preg2.webp",
        "worldChars['elena']['preg'] == 3", "images/characters/elena/preg/rags_preg3.webp")
image elena_animtalk = Null()

########## wolf form
image elena_w =       Composite((1500, 959), (0, 500), "elena_w_body")

image elena_w angry = Composite((1500, 959), (0, 500), "elena_w_body", (0, 500), "images/characters/elena/wolf/face_angry.webp")
image elena_w bark =  Composite((1500, 959), (0, 500), "elena_w_body", (0, 500), "elena_animbark")

image elena_w_body = "images/characters/elena/wolf/base.webp"

# talking
image elena_animbark:
        "images/characters/elena/wolf/face_bark2.webp"
        0.2
        Null()