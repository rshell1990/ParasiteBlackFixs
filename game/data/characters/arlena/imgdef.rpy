############# arlena expressions #################
image arlena angry =    Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body", CHAR_OFFSET.ARLENA, "arlena_face_angry")
image arlena blush =    Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body", CHAR_OFFSET.ARLENA, "arlena_face_blush")
image arlena blush_2 =  Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body", CHAR_OFFSET.ARLENA, "arlena_face_blush_2")
image arlena cry =      Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body", CHAR_OFFSET.ARLENA, "arlena_face_cry")
image arlena laugh =    Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body", CHAR_OFFSET.ARLENA, "arlena_face_laugh")
image arlena sad =      Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body", CHAR_OFFSET.ARLENA, "arlena_face_sad")
image arlena scared =   Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body", CHAR_OFFSET.ARLENA, "arlena_face_scared")
image arlena shock =    Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body", CHAR_OFFSET.ARLENA, "arlena_face_shock")
image arlena smile =    Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body", CHAR_OFFSET.ARLENA, "arlena_face_smile")
image arlena smug =     Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body", CHAR_OFFSET.ARLENA, "arlena_face_smug")
image arlena think =    Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body", CHAR_OFFSET.ARLENA, "arlena_face_think")
image arlena talk = "arlena"

image arlena = Composite((556, 1288), CHAR_OFFSET.ARLENA, "arlena_body")

image arlena_body = ConditionSwitch(
    "worldChars['arlena']['clothes'] == 'naked'",       "arlena_naked",
    "worldChars['arlena']['clothes'] == 'normal_ash'",  "arlena_normal_ash",
    "worldChars['arlena']['clothes'] == 'apron'",       "arlena_apron",
    "True",      "arlena_normal",
)

image arlena_normal = ConditionSwitch(
        "worldChars['arlena']['preg'] == 0", "images/characters/arlena/normal.webp",
        "worldChars['arlena']['preg'] == 1", "images/characters/arlena/preg/normal_1.webp",
        "worldChars['arlena']['preg'] == 2", "images/characters/arlena/preg/normal_2.webp",
        "worldChars['arlena']['preg'] == 3", "images/characters/arlena/preg/normal_3.webp",
        "worldChars['arlena']['preg'] == 4", "images/characters/arlena/normal.webp")

image arlena_normal_ash = "images/characters/arlena/normal_ash.webp"

image arlena_naked = ConditionSwitch(
        "worldChars['arlena']['preg'] == 0", "images/characters/arlena/naked.webp",
        "worldChars['arlena']['preg'] == 1", "images/characters/arlena/preg/naked_1.webp",
        "worldChars['arlena']['preg'] == 2", "images/characters/arlena/preg/naked_2.webp",
        "worldChars['arlena']['preg'] == 3", "images/characters/arlena/preg/naked_3.webp",
        "worldChars['arlena']['preg'] == 4", "images/characters/arlena/naked.webp")

image arlena_apron = ConditionSwitch(
        "worldChars['arlena']['preg'] == 0", "images/characters/arlena/apron.webp",
        "worldChars['arlena']['preg'] == 1", "images/characters/arlena/preg/apron_1.webp",
        "worldChars['arlena']['preg'] == 2", "images/characters/arlena/preg/apron_2.webp",
        "worldChars['arlena']['preg'] == 3", "images/characters/arlena/preg/apron_3.webp",
        "worldChars['arlena']['preg'] == 4", "images/characters/arlena/apron.webp")

### expression images (for ash variants)
image arlena_face_angry =   ConditionSwitch("worldChars['arlena']['clothes'] == 'normal_ash'", "images/characters/arlena/face_ash/angry.webp",      "True", "images/characters/arlena/face/angry.webp")
image arlena_face_blush =   ConditionSwitch("worldChars['arlena']['clothes'] == 'normal_ash'", "images/characters/arlena/face_ash/blush.webp",      "True", "images/characters/arlena/face/blush.webp")
image arlena_face_blush_2 = ConditionSwitch("worldChars['arlena']['clothes'] == 'normal_ash'", "images/characters/arlena/face_ash/blush_2.webp",    "True", "images/characters/arlena/face/blush_2.webp")
image arlena_face_cry =     ConditionSwitch("worldChars['arlena']['clothes'] == 'normal_ash'", "images/characters/arlena/face_ash/cry.webp",        "True", "images/characters/arlena/face/cry.webp")
image arlena_face_laugh =   ConditionSwitch("worldChars['arlena']['clothes'] == 'normal_ash'", "images/characters/arlena/face_ash/laugh.webp",      "True", "images/characters/arlena/face/laugh.webp")
image arlena_face_sad =     ConditionSwitch("worldChars['arlena']['clothes'] == 'normal_ash'", "images/characters/arlena/face_ash/sad.webp",        "True", "images/characters/arlena/face/sad.webp")
image arlena_face_scared =  ConditionSwitch("worldChars['arlena']['clothes'] == 'normal_ash'", "images/characters/arlena/face_ash/scared.webp",     "True", "images/characters/arlena/face/scared.webp")
image arlena_face_shock =   ConditionSwitch("worldChars['arlena']['clothes'] == 'normal_ash'", "images/characters/arlena/face_ash/shock.webp",      "True", "images/characters/arlena/face/shock.webp")
image arlena_face_smile =   ConditionSwitch("worldChars['arlena']['clothes'] == 'normal_ash'", "images/characters/arlena/face_ash/smile.webp",      "True", "images/characters/arlena/face/smile.webp")
image arlena_face_smug =    ConditionSwitch("worldChars['arlena']['clothes'] == 'normal_ash'", "images/characters/arlena/face_ash/smug.webp",       "True", "images/characters/arlena/face/smug.webp")
image arlena_face_think =   ConditionSwitch("worldChars['arlena']['clothes'] == 'normal_ash'", "images/characters/arlena/face_ash/think.webp",      "True", "images/characters/arlena/face/think.webp")