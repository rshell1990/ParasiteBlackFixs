############### lady tarbeck expressions ##############
image lady_tarbeck angry = Composite((730, 1478), CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_body", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_face_angry", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_mask")
image lady_tarbeck blush = Composite((730, 1478), CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_body", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_face_blush", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_mask")
image lady_tarbeck lust  = Composite((730, 1478), CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_body", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_face_lust",CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_mask")
image lady_tarbeck blush2  = "lady_tarbeck lust"
image lady_tarbeck cry   = Composite((730, 1478), CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_body", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_face_cry",   CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_mask")
image lady_tarbeck happy = Composite((730, 1478), CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_body", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_face_happy", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_mask")
image lady_tarbeck laugh = Composite((730, 1478), CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_body", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_face_laugh", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_mask")
image lady_tarbeck smile = "lady_tarbeck laugh"
image lady_tarbeck sad   = Composite((730, 1478), CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_body", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_face_sad",   CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_mask")
image lady_tarbeck scared= Composite((730, 1478), CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_body", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_face_scared",CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_mask")
image lady_tarbeck think = Composite((730, 1478), CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_body", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_face_think", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_mask")
image lady_tarbeck shock = Composite((730, 1478), CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_body", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_face_shock", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_mask")
image lady_tarbeck talk  = "lady_tarbeck"

image lady_tarbeck      = Composite((730, 1478), CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_body", CHAR_OFFSET.LADY_TARBECK, "lady_tarbeck_mask")
#### branches into 3 diff. body variants
image lady_tarbeck_body = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'bimbo'",    "lady_tarbeck_body_bimbo",
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "lady_tarbeck_body_darkmage",
    "True",  "lady_tarbeck_body_normal"
)
#### there body variants
image lady_tarbeck_body_normal = ConditionSwitch(
    "worldChars['lady_tarbeck']['clothes'] == 'naked'",    "lady_tarbeck_body_normal_naked",
    "worldChars['lady_tarbeck']['clothes'] == 'ling'",    "lady_tarbeck_body_normal_ling",
    "True",  "lady_tarbeck_body_normal_normal"
)
image lady_tarbeck_body_darkmage = ConditionSwitch(
    "worldChars['lady_tarbeck']['clothes'] == 'naked'",    "lady_tarbeck_body_darkmage_naked",
    "worldChars['lady_tarbeck']['clothes'] == 'ling'",    "lady_tarbeck_body_darkmage_ling",
    "True",  "lady_tarbeck_body_darkmage_normal"
)
image lady_tarbeck_body_bimbo = ConditionSwitch(
    "worldChars['lady_tarbeck']['clothes'] == 'naked'",    "lady_tarbeck_body_bimbo_naked",
    "True",  "lady_tarbeck_body_bimbo_normal"
)
#### specific body defs
## normal
image lady_tarbeck_body_normal_normal = ConditionSwitch(
    "worldChars['lady_tarbeck']['preg'] == 0", "images/characters/lady_tarbeck/normal.webp",
    "worldChars['lady_tarbeck']['preg'] == 1", "images/characters/lady_tarbeck/preg/normal_1.webp",
    "worldChars['lady_tarbeck']['preg'] == 2", "images/characters/lady_tarbeck/preg/normal_2.webp",
    "worldChars['lady_tarbeck']['preg'] == 3", "images/characters/lady_tarbeck/preg/normal_3.webp",
    "worldChars['lady_tarbeck']['preg'] == 4", "images/characters/lady_tarbeck/preg/normal_4.webp")
image lady_tarbeck_body_normal_naked = ConditionSwitch(
    "worldChars['lady_tarbeck']['preg'] == 0", "images/characters/lady_tarbeck/naked.webp",
    "worldChars['lady_tarbeck']['preg'] == 1", "images/characters/lady_tarbeck/preg/naked_1.webp",
    "worldChars['lady_tarbeck']['preg'] == 2", "images/characters/lady_tarbeck/preg/naked_2.webp",
    "worldChars['lady_tarbeck']['preg'] == 3", "images/characters/lady_tarbeck/preg/naked_3.webp",
    "worldChars['lady_tarbeck']['preg'] == 4", "images/characters/lady_tarbeck/naked.webp")
image lady_tarbeck_body_normal_ling = ConditionSwitch(
    "worldChars['lady_tarbeck']['preg'] == 0", "images/characters/lady_tarbeck/ling.webp",
    "worldChars['lady_tarbeck']['preg'] == 1", "images/characters/lady_tarbeck/preg/ling_1.webp",
    "worldChars['lady_tarbeck']['preg'] == 2", "images/characters/lady_tarbeck/preg/ling_2.webp",
    "worldChars['lady_tarbeck']['preg'] == 3", "images/characters/lady_tarbeck/preg/ling_3.webp",
    "worldChars['lady_tarbeck']['preg'] == 4", "images/characters/lady_tarbeck/ling.webp")
## darkmage
image lady_tarbeck_body_darkmage_normal = ConditionSwitch(
    "worldChars['lady_tarbeck']['preg'] == 0", "images/characters/lady_tarbeck/darkmage/normal.webp",
    "worldChars['lady_tarbeck']['preg'] == 1", "images/characters/lady_tarbeck/darkmage/preg/normal_1.webp",
    "worldChars['lady_tarbeck']['preg'] == 2", "images/characters/lady_tarbeck/darkmage/preg/normal_2.webp",
    "worldChars['lady_tarbeck']['preg'] == 3", "images/characters/lady_tarbeck/darkmage/preg/normal_3.webp",
    "worldChars['lady_tarbeck']['preg'] == 4", "images/characters/lady_tarbeck/darkmage/preg/normal_4.webp")

image lady_tarbeck_body_darkmage_naked = ConditionSwitch(
    "worldChars['lady_tarbeck']['preg'] == 0", "images/characters/lady_tarbeck/darkmage/naked.webp",
    "worldChars['lady_tarbeck']['preg'] == 1", "images/characters/lady_tarbeck/darkmage/preg/naked_1.webp",
    "worldChars['lady_tarbeck']['preg'] == 2", "images/characters/lady_tarbeck/darkmage/preg/naked_2.webp",
    "worldChars['lady_tarbeck']['preg'] == 3", "images/characters/lady_tarbeck/darkmage/preg/naked_3.webp",
    "worldChars['lady_tarbeck']['preg'] == 4", "images/characters/lady_tarbeck/darkmage/naked.webp")

image lady_tarbeck_body_darkmage_ling = ConditionSwitch(
    "worldChars['lady_tarbeck']['preg'] == 0", "images/characters/lady_tarbeck/darkmage/ling.webp",
    "worldChars['lady_tarbeck']['preg'] == 1", "images/characters/lady_tarbeck/darkmage/preg/ling_1.webp",
    "worldChars['lady_tarbeck']['preg'] == 2", "images/characters/lady_tarbeck/darkmage/preg/ling_2.webp",
    "worldChars['lady_tarbeck']['preg'] == 3", "images/characters/lady_tarbeck/darkmage/preg/ling_3.webp",
    "worldChars['lady_tarbeck']['preg'] == 4", "images/characters/lady_tarbeck/darkmage/ling.webp")
## bimbo
image lady_tarbeck_body_bimbo_normal = ConditionSwitch(
    "worldChars['lady_tarbeck']['preg'] == 0", "images/characters/lady_tarbeck/bimbo/normal.webp",
    "worldChars['lady_tarbeck']['preg'] == 1", "images/characters/lady_tarbeck/bimbo/preg/normal_1.webp",
    "worldChars['lady_tarbeck']['preg'] == 2", "images/characters/lady_tarbeck/bimbo/preg/normal_2.webp",
    "worldChars['lady_tarbeck']['preg'] == 3", "images/characters/lady_tarbeck/bimbo/preg/normal_3.webp",
    "worldChars['lady_tarbeck']['preg'] == 4", "images/characters/lady_tarbeck/bimbo/preg/normal_4.webp")

image lady_tarbeck_body_bimbo_naked = ConditionSwitch(
    "worldChars['lady_tarbeck']['preg'] == 0", "images/characters/lady_tarbeck/bimbo/naked.webp",
    "worldChars['lady_tarbeck']['preg'] == 1", "images/characters/lady_tarbeck/bimbo/preg/naked_1.webp",
    "worldChars['lady_tarbeck']['preg'] == 2", "images/characters/lady_tarbeck/bimbo/preg/naked_2.webp",
    "worldChars['lady_tarbeck']['preg'] == 3", "images/characters/lady_tarbeck/bimbo/preg/naked_3.webp",
    "worldChars['lady_tarbeck']['preg'] == 4", "images/characters/lady_tarbeck/bimbo/naked.webp")


###### faces, switch based on which variant used
image lady_tarbeck_face_angry = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "images/characters/lady_tarbeck/darkmage/face/angry.webp",
    "worldChars['lady_tarbeck']['variant'] == 'bimbo'", "images/characters/lady_tarbeck/bimbo/face/angry.webp",
    "True", "images/characters/lady_tarbeck/face/angry.webp"
)
image lady_tarbeck_face_blush = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "images/characters/lady_tarbeck/darkmage/face/blush.webp",
    "worldChars['lady_tarbeck']['variant'] == 'bimbo'", "images/characters/lady_tarbeck/bimbo/face/blush.webp",
    "True", "images/characters/lady_tarbeck/face/blush.webp"
)
image lady_tarbeck_face_cry = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "images/characters/lady_tarbeck/darkmage/face/cry.webp",
    "worldChars['lady_tarbeck']['variant'] == 'bimbo'", "images/characters/lady_tarbeck/bimbo/face/cry.webp",
    "True", "images/characters/lady_tarbeck/face/cry.webp"
)
image lady_tarbeck_face_happy = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "images/characters/lady_tarbeck/darkmage/face/happy.webp",
    "worldChars['lady_tarbeck']['variant'] == 'bimbo'", "images/characters/lady_tarbeck/bimbo/face/happy.webp",
    "True", "images/characters/lady_tarbeck/face/happy.webp"
)
image lady_tarbeck_face_laugh = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "images/characters/lady_tarbeck/darkmage/face/laugh.webp",
    "worldChars['lady_tarbeck']['variant'] == 'bimbo'", "images/characters/lady_tarbeck/bimbo/face/laugh.webp",
    "True", "images/characters/lady_tarbeck/face/laugh.webp"
)
image lady_tarbeck_face_lust = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "images/characters/lady_tarbeck/darkmage/face/lust.webp",
    "worldChars['lady_tarbeck']['variant'] == 'bimbo'", "images/characters/lady_tarbeck/bimbo/face/lust.webp",
    "True", "images/characters/lady_tarbeck/face/lust.webp"
)
image lady_tarbeck_face_sad = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "images/characters/lady_tarbeck/darkmage/face/sad.webp",
    "worldChars['lady_tarbeck']['variant'] == 'bimbo'", "images/characters/lady_tarbeck/bimbo/face/sad.webp",
    "True", "images/characters/lady_tarbeck/face/sad.webp"
)
image lady_tarbeck_face_scared = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "images/characters/lady_tarbeck/darkmage/face/scared.webp",
    "worldChars['lady_tarbeck']['variant'] == 'bimbo'", "images/characters/lady_tarbeck/bimbo/face/scared.webp",
    "True", "images/characters/lady_tarbeck/face/scared.webp"
)
image lady_tarbeck_face_shock = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "images/characters/lady_tarbeck/darkmage/face/shock.webp",
    "worldChars['lady_tarbeck']['variant'] == 'bimbo'", "images/characters/lady_tarbeck/bimbo/face/shock.webp",
    "True", "images/characters/lady_tarbeck/face/shock.webp"
)
image lady_tarbeck_face_think = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "images/characters/lady_tarbeck/darkmage/face/think.webp",
    "worldChars['lady_tarbeck']['variant'] == 'bimbo'", "images/characters/lady_tarbeck/bimbo/face/think.webp",
    "True", "images/characters/lady_tarbeck/face/think.webp"
)
#### mask present on all variants but is a sprite only for darkmage
image lady_tarbeck_mask = ConditionSwitch(
    "worldChars['lady_tarbeck']['variant'] == 'darkmage'", "lady_tarbeck_mask_switch",
    "True", Null()
)

image lady_tarbeck_mask_switch = ConditionSwitch(
    "worldChars['lady_tarbeck']['darkmage_mask'] == 'True'", "images/characters/lady_tarbeck/darkmage/mask.webp",
    "True", Null()
)