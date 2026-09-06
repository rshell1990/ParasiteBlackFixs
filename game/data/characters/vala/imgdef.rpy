########### vala expressions ###############
image vala angry = Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_face_angry",   CHAR_OFFSET.VALA, "vala_glasses")
image vala blush = Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_face_blush",   CHAR_OFFSET.VALA, "vala_glasses")
image vala cry =   Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_face_cry",     CHAR_OFFSET.VALA, "vala_glasses")
image vala embar = Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_face_embar",   CHAR_OFFSET.VALA, "vala_glasses")
image vala laugh = Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_face_laugh",   CHAR_OFFSET.VALA, "vala_glasses")
image vala sad =   Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_face_sad",     CHAR_OFFSET.VALA, "vala_glasses")
image vala scared =Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_face_scared",  CHAR_OFFSET.VALA, "vala_glasses")
image vala shock = Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_face_shock",   CHAR_OFFSET.VALA, "vala_glasses")
image vala smile = Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_face_smile",   CHAR_OFFSET.VALA, "vala_glasses")
image vala surp =  Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_face_surp",    CHAR_OFFSET.VALA, "vala_glasses")
image vala think = Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_face_think",   CHAR_OFFSET.VALA, "vala_glasses")
image vala talk = "vala" # ph
##########################################
image vala = Composite((566, 1246), CHAR_OFFSET.VALA, "vala_body", CHAR_OFFSET.VALA, "vala_glasses")
image vala_body = ConditionSwitch(
        "worldChars['vala']['clothes'] == 'normal_ash'","images/characters/vala/normal_ash.webp",
        "worldChars['vala']['clothes'] == 'naked'",     "images/characters/vala/naked.webp",
        "True",    "images/characters/vala/normal.webp",
)
image vala_glasses = ConditionSwitch(
        "worldChars['vala']['glasses'] == 'on'", "images/characters/vala/glasses.webp",
        "worldChars['vala']['glasses'] == 'off'", Null())

####################
## face conditionals (for ash)
image vala_face_angry = ConditionSwitch("worldChars['vala']['clothes'] == 'normal_ash'", "images/characters/vala/face_ash/angry.webp", "True", "images/characters/vala/face/angry.webp")
image vala_face_blush = ConditionSwitch("worldChars['vala']['clothes'] == 'normal_ash'", "images/characters/vala/face_ash/blush.webp", "True", "images/characters/vala/face/blush.webp")
image vala_face_cry =   ConditionSwitch("worldChars['vala']['clothes'] == 'normal_ash'", "images/characters/vala/face_ash/cry.webp",   "True", "images/characters/vala/face/cry.webp")
image vala_face_embar = ConditionSwitch("worldChars['vala']['clothes'] == 'normal_ash'", "images/characters/vala/face_ash/embar.webp", "True", "images/characters/vala/face/embar.webp")
image vala_face_laugh = ConditionSwitch("worldChars['vala']['clothes'] == 'normal_ash'", "images/characters/vala/face_ash/laugh.webp", "True", "images/characters/vala/face/laugh.webp")
image vala_face_sad =   ConditionSwitch("worldChars['vala']['clothes'] == 'normal_ash'", "images/characters/vala/face_ash/sad.webp",   "True", "images/characters/vala/face/sad.webp")
image vala_face_scared =ConditionSwitch("worldChars['vala']['clothes'] == 'normal_ash'", "images/characters/vala/face_ash/scared.webp","True", "images/characters/vala/face/scared.webp")
image vala_face_shock = ConditionSwitch("worldChars['vala']['clothes'] == 'normal_ash'", "images/characters/vala/face_ash/shock.webp", "True", "images/characters/vala/face/shock.webp")
image vala_face_smile = ConditionSwitch("worldChars['vala']['clothes'] == 'normal_ash'", "images/characters/vala/face_ash/smile.webp", "True", "images/characters/vala/face/smile.webp")
image vala_face_surp =  ConditionSwitch("worldChars['vala']['clothes'] == 'normal_ash'", "images/characters/vala/face_ash/surp.webp",  "True", "images/characters/vala/face/surp.webp")
image vala_face_think = ConditionSwitch("worldChars['vala']['clothes'] == 'normal_ash'", "images/characters/vala/face_ash/think.webp", "True", "images/characters/vala/face/think.webp")