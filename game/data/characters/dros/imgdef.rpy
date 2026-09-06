################# dros expressions ###########
image dros angry    = Composite((682, 1352), CHAR_OFFSET.DROS, "dros_body", CHAR_OFFSET.DROS, "dros_face_angry")
image dros shock    = Composite((682, 1352), CHAR_OFFSET.DROS, "dros_body", CHAR_OFFSET.DROS, "dros_face_shock")
image dros smile    = Composite((682, 1352), CHAR_OFFSET.DROS, "dros_body", CHAR_OFFSET.DROS, "dros_face_smile")
image dros lewd     = Composite((682, 1352), CHAR_OFFSET.DROS, "dros_body", CHAR_OFFSET.DROS, "dros_face_lewd")
image dros sad      = Composite((682, 1352), CHAR_OFFSET.DROS, "dros_body", CHAR_OFFSET.DROS, "dros_face_sad")
image dros talk     = Composite((682, 1352), CHAR_OFFSET.DROS, "dros_body", CHAR_OFFSET.DROS, "dros_face_talk")
##############################################
image dros  = Composite((682, 1352), CHAR_OFFSET.DROS, "dros_body")

image dros_body = ConditionSwitch(
    "worldChars['dros']['Transformed'] == True",    "dros_body_transformed",
    "worldChars['dros']['Transformed'] == False",   "dros_body_normal")

image dros_body_normal = ConditionSwitch(
    "worldChars['dros']['clothes'] == 'dress'",     "images/characters/dros/dress.webp",
    "worldChars['dros']['clothes'] == 'ling'",      "images/characters/dros/dress.webp", # there's no ling
    "worldChars['dros']['clothes'] == 'naked'",     "images/characters/dros/naked.webp",
    "True",    "images/characters/dros/normal.webp",
)

image dros_body_transformed = ConditionSwitch(
    "worldChars['dros']['clothes'] == 'dress'",     "images/characters/dros/fem/dress.webp",
    "worldChars['dros']['clothes'] == 'ling'",      "images/characters/dros/fem/ling.webp",
    "worldChars['dros']['clothes'] == 'naked'",     "images/characters/dros/fem/naked.webp",
    "True",    "images/characters/dros/fem/normal.webp",
)


image dros_face_talk    = ConditionSwitch(
    "worldChars['dros']['Transformed'] == True",    Null(),
    "worldChars['dros']['Transformed'] == False",   Null())
image dros_face_angry   = ConditionSwitch(
    "worldChars['dros']['Transformed'] == True",    "images/characters/dros/fem/face/angry.webp",
    "worldChars['dros']['Transformed'] == False",   ConditionSwitch(
        "worldChars['dros']['clothes'] == 'dress'", "images/characters/dros/face/angry_m.webp",
        "worldChars['dros']['clothes'] != 'dress'", "images/characters/dros/face/angry.webp"))
image dros_face_smile   = ConditionSwitch(
    "worldChars['dros']['Transformed'] == True",    "images/characters/dros/fem/face/smile2.webp",
    "worldChars['dros']['Transformed'] == False",   ConditionSwitch(
        "worldChars['dros']['clothes'] == 'dress'", "images/characters/dros/face/happy_m.webp",
        "worldChars['dros']['clothes'] != 'dress'", "images/characters/dros/face/happy.webp"))
image dros_face_lewd    = ConditionSwitch(
    "worldChars['dros']['Transformed'] == True",    "images/characters/dros/fem/face/blush.webp",
    "worldChars['dros']['Transformed'] == False",   ConditionSwitch(
        "worldChars['dros']['clothes'] == 'dress'", "images/characters/dros/face/lewd_m.webp",
        "worldChars['dros']['clothes'] != 'dress'", "images/characters/dros/face/lewd.webp"))
image dros_face_sad     = ConditionSwitch(
    "worldChars['dros']['Transformed'] == True",    "images/characters/dros/fem/face/sad.webp",
    "worldChars['dros']['Transformed'] == False",   ConditionSwitch(
        "worldChars['dros']['clothes'] == 'dress'", "images/characters/dros/face/sad_m.webp",
        "worldChars['dros']['clothes'] != 'dress'", "images/characters/dros/face/sad.webp"))
image dros_face_shock   = ConditionSwitch(
    "worldChars['dros']['Transformed'] == True",    "images/characters/dros/fem/face/scared.webp",
    "worldChars['dros']['Transformed'] == False",   ConditionSwitch(
        "worldChars['dros']['clothes'] == 'dress'", "images/characters/dros/face/shock_m.webp",
        "worldChars['dros']['clothes'] != 'dress'", "images/characters/dros/face/shock.webp"))
