################### drax expressions #########
image drax angry = Composite((682, 1352), CHAR_OFFSET.DRAX, "drax", CHAR_OFFSET.DRAX, "drax_face_angry")
image drax happy = Composite((682, 1352), CHAR_OFFSET.DRAX, "drax", CHAR_OFFSET.DRAX, "drax_face_happy")
image drax laugh = Composite((682, 1352), CHAR_OFFSET.DRAX, "drax", CHAR_OFFSET.DRAX, "drax_face_laugh")
image drax sad =   Composite((682, 1352), CHAR_OFFSET.DRAX, "drax", CHAR_OFFSET.DRAX, "drax_face_sad")
image drax think = Composite((682, 1352), CHAR_OFFSET.DRAX, "drax", CHAR_OFFSET.DRAX, "drax_face_think")
#############################################
image drax = Composite((682, 1352), CHAR_OFFSET.DRAX, "drax_body")
image drax_body = ConditionSwitch(
    "worldChars['drax']['clothes'] == 'normal_ash'",    "images/characters/drax/normal_ash.webp",
    "True",        "images/characters/drax/normal.webp",
)

#######################
## expression conditionals (for ashed)
image drax_face_angry = ConditionSwitch("worldChars['drax']['clothes'] == 'normal_ash'", "images/characters/drax/face_ash/angry.webp", "True", "images/characters/drax/face/angry.webp")
image drax_face_happy = ConditionSwitch("worldChars['drax']['clothes'] == 'normal_ash'", "images/characters/drax/face_ash/happy.webp", "True", "images/characters/drax/face/happy.webp")
image drax_face_laugh = ConditionSwitch("worldChars['drax']['clothes'] == 'normal_ash'", "images/characters/drax/face_ash/laugh.webp", "True", "images/characters/drax/face/laugh.webp")
image drax_face_sad =   ConditionSwitch("worldChars['drax']['clothes'] == 'normal_ash'", "images/characters/drax/face_ash/sad.webp",   "True", "images/characters/drax/face/sad.webp")
image drax_face_think = ConditionSwitch("worldChars['drax']['clothes'] == 'normal_ash'", "images/characters/drax/face_ash/think.webp", "True", "images/characters/drax/face/think.webp")