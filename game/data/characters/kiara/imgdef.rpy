############### kiara expressions ###############
image kiara angry =     Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_angry",      CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara blush =     Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_blush",      CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara cry =       Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_cry",        CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara happy =     Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_happy",      CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara smile =     Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_happy",      CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara happy_tears=Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA,"kiara_face_happy_tears", CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara laugh =     Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_laugh",      CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara sad =       Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_sad",        CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara scared =    Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_scared",     CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara shock =     Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_scared",     CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara serious =   Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_serious",    CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara shy =       Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_shy",        CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara think =     Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_face_think",      CHAR_OFFSET.KIARA, "kiara_body_layer_top")
image kiara talk =      "kiara"
##########################################

image kiara = Composite((755, 1249), CHAR_OFFSET.KIARA, "kiara_body_root",  CHAR_OFFSET.KIARA, "kiara_body_layer_top")

# 'root' because she has two bodies
image kiara_body_root = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'",         "kiara_body_human",
        "worldChars['kiara']['story_form'] == 'demorai'",       "kiara_body_demorai"
)

image kiara_body_human = ConditionSwitch(
        "worldChars['kiara']['clothes'] == 'naked'",    "images/characters/kiara/naked.webp",
        "worldChars['kiara']['clothes'] == 'plain'",    "images/characters/kiara/normal.webp",
        "worldChars['kiara']['clothes'] == 'towel'",    "images/characters/kiara/towel.webp",

        "worldChars['kiara']['clothes'] == 'dom'",      "images/characters/kiara/dom.webp",
        "worldChars['kiara']['clothes'] == 'dress'",    "images/characters/kiara/dress.webp",
        "worldChars['kiara']['clothes'] == 'maid'",     "images/characters/kiara/maid.webp",

        # normal will fallback through here
        "True",                                         "kiara_body_human_variants"
)

# will choose between scout and duskshroud
image kiara_body_human_variants = ConditionSwitch(
        "worldChars['kiara']['default_look'] == 'scout'",  "images/characters/kiara/scout.webp",
        "worldChars['kiara']['default_look'] == 'hooded'", "images/characters/kiara/hooded.webp"
)

image kiara_body_demorai = ConditionSwitch(
        "worldChars['kiara']['clothes'] == 'naked'", "images/characters/kiara/demorai/naked.webp",
        "True",                                      "images/characters/kiara/demorai/normal.webp"
)
###############################################
# this also splits between two bodies
image kiara_body_layer_top = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'",         "kiara_body_layer_top_human",
        "worldChars['kiara']['story_form'] == 'demorai'",       "kiara_body_layer_top_demorai",
)

# the hood clothes piece' overlay
image kiara_body_layer_top_human = ConditionSwitch(
        "worldChars['kiara']['clothes'] == 'dom'",      "images/characters/kiara/dom_mask.webp",
        "worldChars['kiara']['clothes'] == 'dress'",    "images/characters/kiara/mask.webp",
        "worldChars['kiara']['clothes'] == 'maid'",     "images/characters/kiara/tiara.webp",
        "worldChars['kiara']['clothes'] == 'normal' and worldChars['kiara']['default_look'] == 'hooded'", "images/characters/kiara/hooded_hood.webp",
        "True", Null()
)

# the hood clothes piece' overlay
image kiara_body_layer_top_demorai = ConditionSwitch(
        "True", Null()
)

##############################################
###### faces for two forms
image kiara_face_angry = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/angry.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/angry.webp")
image kiara_face_blush = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/blush.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/happy.webp")
image kiara_face_cry = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/cry.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/cry.webp")
image kiara_face_happy = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/happy.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/happy.webp")
image kiara_face_smile = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/happy.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/happy.webp")
image kiara_face_happy_tears = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/happy_tears.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/happy.webp")
image kiara_face_laugh = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/laugh.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/laugh.webp")
image kiara_face_sad = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/sad.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/sad.webp")
image kiara_face_scared = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/scared.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/scared.webp")
image kiara_face_shock = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/scared.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/shock.webp")
image kiara_face_serious = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/serious.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/think.webp")
image kiara_face_shy = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/shy.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/sad.webp")
image kiara_face_think = ConditionSwitch(
        "worldChars['kiara']['story_form'] == 'human'", "images/characters/kiara/face/think.webp",
        "worldChars['kiara']['story_form'] == 'demorai'", "images/characters/kiara/demorai/face/think.webp")

image cg_kiara_maid_kneel:
        "cg_kiara_maid_kneel_base"
        offset (0, 310)

image cg_kiara_maid_leash:
        "cg_kiara_maid_leash_base"
        offset (0, 60)