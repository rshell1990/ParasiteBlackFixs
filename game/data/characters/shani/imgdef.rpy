################## shani expressions #############
image shani angry   = Composite((521, 1242), CHAR_OFFSET.SHANI, "shani_body", CHAR_OFFSET.SHANI, "face_shani_angry")
image shani cry     = Composite((521, 1242), CHAR_OFFSET.SHANI, "shani_body", CHAR_OFFSET.SHANI, "face_shani_cry")
image shani embar   = Composite((521, 1242), CHAR_OFFSET.SHANI, "shani_body", CHAR_OFFSET.SHANI, "face_shani_embar")
image shani laugh   = Composite((521, 1242), CHAR_OFFSET.SHANI, "shani_body", CHAR_OFFSET.SHANI, "face_shani_laugh")
image shani lewd    = Composite((521, 1242), CHAR_OFFSET.SHANI, "shani_body", CHAR_OFFSET.SHANI, "face_shani_lewd")
image shani sad     = Composite((521, 1242), CHAR_OFFSET.SHANI, "shani_body", CHAR_OFFSET.SHANI, "face_shani_sad")
image shani scared  = Composite((521, 1242), CHAR_OFFSET.SHANI, "shani_body", CHAR_OFFSET.SHANI, "face_shani_scared")
image shani shock   = Composite((521, 1242), CHAR_OFFSET.SHANI, "shani_body", CHAR_OFFSET.SHANI, "face_shani_shock")
image shani smile   = Composite((521, 1242), CHAR_OFFSET.SHANI, "shani_body", CHAR_OFFSET.SHANI, "face_shani_smile")
image shani think   = Composite((521, 1242), CHAR_OFFSET.SHANI, "shani_body", CHAR_OFFSET.SHANI, "face_shani_think")
image shani talk    = "shani"
image shani angry_talk = "shani"
########
image shani = Composite((521, 1242), CHAR_OFFSET.SHANI, "shani_body")

image shani_body = ConditionSwitch(
    "worldChars['shani']['clothes'] == 'normal_ash'",   "images/characters/shani/normal_ash.webp",
    "worldChars['shani']['clothes'] == 'naked'",        "shani_naked",
    "True",       "shani_clothed",
)

image shani_clothed = ConditionSwitch(
    "worldChars['shani']['pose'] == 'normal'",  "images/characters/shani/normal.webp",
    "worldChars['shani']['pose'] == 'alt'",     "images/characters/shani/normal_pose2.webp")

image shani_naked = ConditionSwitch(
    "worldChars['shani']['pose'] == 'normal'",  "images/characters/shani/naked.webp",
    "worldChars['shani']['pose'] == 'alt'",     "images/characters/shani/naked_pose2.webp")

##############
## face conditionals (for ashes)
image face_shani_angry = ConditionSwitch("worldChars['shani']['clothes'] == 'normal_ash'", "images/characters/shani/face_ash/angry.webp",   "True", "images/characters/shani/face/angry.webp")
image face_shani_cry =   ConditionSwitch("worldChars['shani']['clothes'] == 'normal_ash'", "images/characters/shani/face_ash/cry.webp",     "True", "images/characters/shani/face/cry.webp")
image face_shani_embar = ConditionSwitch("worldChars['shani']['clothes'] == 'normal_ash'", "images/characters/shani/face_ash/embar.webp",   "True", "images/characters/shani/face/embar.webp")
image face_shani_laugh = ConditionSwitch("worldChars['shani']['clothes'] == 'normal_ash'", "images/characters/shani/face_ash/laugh.webp",   "True", "images/characters/shani/face/laugh.webp")
image face_shani_lewd =  ConditionSwitch("worldChars['shani']['clothes'] == 'normal_ash'", "images/characters/shani/face_ash/lewd.webp",    "True", "images/characters/shani/face/lewd.webp")
image face_shani_sad =   ConditionSwitch("worldChars['shani']['clothes'] == 'normal_ash'", "images/characters/shani/face_ash/sad.webp",     "True", "images/characters/shani/face/sad.webp")
image face_shani_scared =ConditionSwitch("worldChars['shani']['clothes'] == 'normal_ash'", "images/characters/shani/face_ash/scared.webp",  "True", "images/characters/shani/face/scared.webp")
image face_shani_shock = ConditionSwitch("worldChars['shani']['clothes'] == 'normal_ash'", "images/characters/shani/face_ash/shock.webp",   "True", "images/characters/shani/face/shock.webp")
image face_shani_smile = ConditionSwitch("worldChars['shani']['clothes'] == 'normal_ash'", "images/characters/shani/face_ash/smile.webp",   "True", "images/characters/shani/face/smile.webp")
image face_shani_think = ConditionSwitch("worldChars['shani']['clothes'] == 'normal_ash'", "images/characters/shani/face_ash/think.webp",   "True", "images/characters/shani/face/think.webp")