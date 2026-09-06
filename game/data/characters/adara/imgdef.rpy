############# adara expressions #################
image adara angry   = Composite((692, 1402), CHAR_OFFSET.ADARA, "adara_body", CHAR_OFFSET.ADARA, "adara_face_angry",  CHAR_OFFSET.ADARA, "adara_blush")
image adara cry     = Composite((692, 1402), CHAR_OFFSET.ADARA, "adara_body", CHAR_OFFSET.ADARA, "adara_face_cry",    CHAR_OFFSET.ADARA, "adara_blush")
image adara joy     = Composite((692, 1402), CHAR_OFFSET.ADARA, "adara_body", CHAR_OFFSET.ADARA, "adara_face_joy",    CHAR_OFFSET.ADARA, "adara_blush")
image adara lewd    = Composite((692, 1402), CHAR_OFFSET.ADARA, "adara_body", CHAR_OFFSET.ADARA, "adara_face_lewd",   CHAR_OFFSET.ADARA, "adara_blush")
image adara sad     = Composite((692, 1402), CHAR_OFFSET.ADARA, "adara_body", CHAR_OFFSET.ADARA, "adara_face_sad",    CHAR_OFFSET.ADARA, "adara_blush")
image adara shame   = Composite((692, 1402), CHAR_OFFSET.ADARA, "adara_body", CHAR_OFFSET.ADARA, "adara_face_shame",  CHAR_OFFSET.ADARA, "adara_blush")
image adara shock   = Composite((692, 1402), CHAR_OFFSET.ADARA, "adara_body", CHAR_OFFSET.ADARA, "adara_face_shock",  CHAR_OFFSET.ADARA, "adara_blush")
image adara smile   = Composite((692, 1402), CHAR_OFFSET.ADARA, "adara_body", CHAR_OFFSET.ADARA, "adara_face_smile",  CHAR_OFFSET.ADARA, "adara_blush")
image adara talk    = "adara"
###############################################
image adara = Composite((692, 1402), CHAR_OFFSET.ADARA, "adara_body")

image adara_body = ConditionSwitch(
    "worldChars['adara']['clothes'] == 'naked'",        "adara_naked",
    "worldChars['adara']['clothes'] == 'normal_ash'",   "adara_normal_ash",
    "worldChars['adara']['clothes'] == 'ling'",         "adara_ling",
    "True",       "adara_normal",
    )

image adara_normal = ConditionSwitch(
        "worldChars['adara']['preg'] == 0", "images/characters/adara/normal.webp",
        "worldChars['adara']['preg'] == 1", "images/characters/adara/preg/normal_1.webp",
        "worldChars['adara']['preg'] == 2", "images/characters/adara/preg/normal_2.webp",
        "worldChars['adara']['preg'] == 3", "images/characters/adara/preg/normal_3.webp",
        "worldChars['adara']['preg'] == 4", "images/characters/adara/normal.webp")

image adara_naked = ConditionSwitch(
        "worldChars['adara']['preg'] == 0", "images/characters/adara/naked.webp",
        "worldChars['adara']['preg'] == 1", "images/characters/adara/preg/naked_1.webp",
        "worldChars['adara']['preg'] == 2", "images/characters/adara/preg/naked_2.webp",
        "worldChars['adara']['preg'] == 3", "images/characters/adara/preg/naked_3.webp",
        "worldChars['adara']['preg'] == 4", "images/characters/adara/naked.webp")

image adara_ling = ConditionSwitch(
        "worldChars['adara']['preg'] == 0", "images/characters/adara/ling.webp",
        "worldChars['adara']['preg'] == 1", "images/characters/adara/preg/ling_1.webp",
        "worldChars['adara']['preg'] == 2", "images/characters/adara/preg/ling_2.webp",
        "worldChars['adara']['preg'] == 3", "images/characters/adara/preg/ling_3.webp",
        "worldChars['adara']['preg'] == 4", "images/characters/adara/ling.webp")

image adara_normal_ash = "images/characters/adara/normal_ash.webp"

image adara_blush = ConditionSwitch(
    "worldChars['adara']['blush'] == True", "images/characters/adara/face/blush.webp",
    "worldChars['adara']['blush'] == False", Null())

################### cg during coming storm quest
image cg_adara_on_top = Movie(start_image = "images/cgs/adara_on_top/cg_adara_on_top_start.webp",
                                play = "images/cgs/adara_on_top/cg_adara_on_top.webm")
image cg_adara_kissing = Movie(start_image = "images/cgs/adara_kissing/cg_adara_kissing_start.webp",
                                play = "images/cgs/adara_kissing/cg_adara_kissing.webm")
################### cg during hamun sleep
image cg_adara_on_top_nude = Movie(start_image = "images/cgs/adara_on_top/cg_adara_on_top_nude_start.webp",
                                play = "images/cgs/adara_on_top/cg_adara_on_top_nude.webm")
image cg_adara_kissing_nude = Movie(start_image = "images/cgs/adara_kissing/cg_adara_kissing_nude_start.webp",
                                play = "images/cgs/adara_kissing/cg_adara_kissing_nude.webm")

################ face expressions conditionals (for ash variant)
image adara_face_angry =ConditionSwitch("worldChars['adara']['clothes'] == 'normal_ash'", "images/characters/adara/face_ash/angry.webp", "True", "images/characters/adara/face/angry.webp")
image adara_face_cry =  ConditionSwitch("worldChars['adara']['clothes'] == 'normal_ash'", "images/characters/adara/face_ash/cry.webp",   "True", "images/characters/adara/face/cry.webp")
image adara_face_joy =  ConditionSwitch("worldChars['adara']['clothes'] == 'normal_ash'", "images/characters/adara/face_ash/joy.webp",   "True", "images/characters/adara/face/joy.webp")
image adara_face_lewd = ConditionSwitch("worldChars['adara']['clothes'] == 'normal_ash'", "images/characters/adara/face_ash/lewd.webp",  "True", "images/characters/adara/face/lewd.webp")
image adara_face_sad =  ConditionSwitch("worldChars['adara']['clothes'] == 'normal_ash'", "images/characters/adara/face_ash/sad.webp",   "True", "images/characters/adara/face/sad.webp")
image adara_face_shame =ConditionSwitch("worldChars['adara']['clothes'] == 'normal_ash'", "images/characters/adara/face_ash/shame.webp", "True", "images/characters/adara/face/shame.webp")
image adara_face_shock =ConditionSwitch("worldChars['adara']['clothes'] == 'normal_ash'", "images/characters/adara/face_ash/shock.webp", "True", "images/characters/adara/face/shock.webp")
image adara_face_smile =ConditionSwitch("worldChars['adara']['clothes'] == 'normal_ash'", "images/characters/adara/face_ash/smile.webp", "True", "images/characters/adara/face/smile.webp")