############ markus expressions (MARKUS PROLOGUE AND MARKUS FEM EXPRESSIONS ARE SEPARATE, SCROLL DOWN) ###############
image markus angry  = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_angry")
image markus cry    = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_cry")
image markus drunk  = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_drunk")
image markus fury   = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_fury")
image markus joy    = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_joy")
image markus lewd   = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_lewd")
image markus sad    = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_sad")
image markus scared = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_scared")
image markus shock  = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_shock")
image markus smile  = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_smile")
image markus smug   = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_smug")
image markus think  = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body", CHAR_OFFSET.MARKUS, "markus_face_think")
image markus talk   = "markus"
########################################
image markus = Composite((609, 1442), CHAR_OFFSET.MARKUS, "markus_body")

image markus_body = ConditionSwitch(
    "worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/normal_ash.webp",
    # warning scout in here is just a bug fix for saves
    "worldChars['markus']['clothes'] == 'scout'", "images/characters/markus/normal.webp",
    "worldChars['markus']['clothes'] == 'naked'", "images/characters/markus/naked.webp",
    "worldChars['markus']['clothes'] == 'towel'",       "images/characters/markus/towel.webp",
    "worldChars['markus']['clothes'] == 'wet'",         "images/characters/markus/wet.webp",
    "worldChars['markus']['clothes'] == 'towel_wet'",   "images/characters/markus/towel_wet.webp",
    "True",                                         "images/characters/markus/normal.webp",
)

####################
# expression conditionals (for ash)
image markus_face_angry = ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/angry.webp", "True", "images/characters/markus/face/angry.webp")
image markus_face_cry   = ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/cry.webp",   "True", "images/characters/markus/face/cry.webp")
image markus_face_drunk = ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/drunk.webp", "True", "images/characters/markus/face/drunk.webp")
image markus_face_fury  = ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/fury.webp",  "True", "images/characters/markus/face/fury.webp")
image markus_face_joy   = ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/joy.webp",   "True", "images/characters/markus/face/joy.webp")
image markus_face_lewd  = ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/lewd.webp",  "True", "images/characters/markus/face/lewd.webp")
image markus_face_sad   = ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/sad.webp",   "True", "images/characters/markus/face/sad.webp")
image markus_face_scared= ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/scared.webp","True", "images/characters/markus/face/scared.webp")
image markus_face_shock = ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/shock.webp", "True", "images/characters/markus/face/shock.webp")
image markus_face_smile = ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/smile.webp", "True", "images/characters/markus/face/smile.webp")
image markus_face_smug  = ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/smug.webp",  "True", "images/characters/markus/face/smug.webp")
image markus_face_think = ConditionSwitch("worldChars['markus']['clothes'] == 'normal_ash'", "images/characters/markus/face_ash/think.webp", "True", "images/characters/markus/face/think.webp")

image markus_transformed:
    Transform("images/characters/markus/markus_transformed.webp", zoom = 1.1)
    offset CHAR_OFFSET.MARKUS_TRAN

###########################################
###### markus female expressions (markus fem expressions) ##########
image markus_fem talk   = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body")
image markus_fem angry  = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body", CHAR_OFFSET.MARKUS_FEM, "images/characters/markus/fem/face/angry.webp",   CHAR_OFFSET.MARKUS_FEM, "markus_fem_body_layer_top")
image markus_fem blush  = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body", CHAR_OFFSET.MARKUS_FEM, "images/characters/markus/fem/face/blush.webp",   CHAR_OFFSET.MARKUS_FEM, "markus_fem_body_layer_top")
image markus_fem drunk  = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body", CHAR_OFFSET.MARKUS_FEM, "images/characters/markus/fem/face/drunk.webp",   CHAR_OFFSET.MARKUS_FEM, "markus_fem_body_layer_top")
image markus_fem drunk_blush = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body", CHAR_OFFSET.MARKUS_FEM, "images/characters/markus/fem/face/drunk_blush.webp", CHAR_OFFSET.MARKUS_FEM, "markus_fem_body_layer_top")
image markus_fem happy  = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body", CHAR_OFFSET.MARKUS_FEM, "images/characters/markus/fem/face/happy.webp",   CHAR_OFFSET.MARKUS_FEM, "markus_fem_body_layer_top")
image markus_fem laugh  = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body", CHAR_OFFSET.MARKUS_FEM, "images/characters/markus/fem/face/laugh.webp",   CHAR_OFFSET.MARKUS_FEM, "markus_fem_body_layer_top")
image markus_fem lewd   = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body", CHAR_OFFSET.MARKUS_FEM, "images/characters/markus/fem/face/lewd.webp",    CHAR_OFFSET.MARKUS_FEM, "markus_fem_body_layer_top")
image markus_fem sad    = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body", CHAR_OFFSET.MARKUS_FEM, "images/characters/markus/fem/face/sad.webp",     CHAR_OFFSET.MARKUS_FEM, "markus_fem_body_layer_top")
image markus_fem surp   = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body", CHAR_OFFSET.MARKUS_FEM, "images/characters/markus/fem/face/surp.webp",    CHAR_OFFSET.MARKUS_FEM, "markus_fem_body_layer_top")
image markus_fem think  = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body", CHAR_OFFSET.MARKUS_FEM, "images/characters/markus/fem/face/think.webp",   CHAR_OFFSET.MARKUS_FEM, "markus_fem_body_layer_top")
########################################
image markus_fem = Composite((542, 1403), CHAR_OFFSET.MARKUS_FEM, "markus_fem_body", CHAR_OFFSET.MARKUS_FEM, "markus_fem_body_layer_top")
image markus_fem_body = ConditionSwitch(
    "worldChars['markus']['clothes'] == 'naked'",       "images/characters/markus/fem/naked.webp",
    "worldChars['markus']['clothes'] == 'towel'",       "images/characters/markus/fem/towel.webp",
    "worldChars['markus']['clothes'] == 'wet'",         "images/characters/markus/fem/wet.webp",
    "worldChars['markus']['clothes'] == 'towel_wet'",   "images/characters/markus/fem/towel_wet.webp",
    "worldChars['markus']['clothes'] == 'dress'",       "images/characters/markus/fem/dress.webp",
    "worldChars['markus']['clothes'] == 'maid'",        "images/characters/markus/fem/maid.webp",
    "worldChars['markus']['clothes'] == 'dom'",         "images/characters/markus/fem/dom.webp",
    "True",                                             "images/characters/markus/fem/normal.webp")

image markus_fem_body_layer_top = ConditionSwitch(
    "worldChars['markus']['clothes'] == 'maid'",        "images/characters/markus/fem/tiara.webp",
    "True",                                             Null(),
    )
image cg_markus_fem_maid_kneel:
    "cg_markus_fem_maid_kneel_base"
    offset (0, 310)
image cg_markus_fem_maid_leash:
    "cg_markus_fem_maid_leash_base"
    offset (0, 60)

################################### prologue only
###### markus prologue expressions #######
image markusprologue angry = Composite((678, 1400), CHAR_OFFSET.MARKUS_PROL, "markusprologue_body", CHAR_OFFSET.MARKUS_PROL, "images/characters/markus/prologue/face/angry.webp")
image markusprologue confused = Composite((678, 1400), CHAR_OFFSET.MARKUS_PROL, "markusprologue_body", CHAR_OFFSET.MARKUS_PROL, "images/characters/markus/prologue/face/thinking.webp")
image markusprologue sad    = Composite((678, 1400), CHAR_OFFSET.MARKUS_PROL, "markusprologue_body", CHAR_OFFSET.MARKUS_PROL, "images/characters/markus/prologue/face/sad.webp")
image markusprologue shock  = Composite((678, 1400), CHAR_OFFSET.MARKUS_PROL, "markusprologue_body", CHAR_OFFSET.MARKUS_PROL, "images/characters/markus/prologue/face/scared.webp")
image markusprologue smile  = Composite((678, 1400), CHAR_OFFSET.MARKUS_PROL, "markusprologue_body", CHAR_OFFSET.MARKUS_PROL, "images/characters/markus/prologue/face/happy.webp")
image markusprologue blush  = Composite((678, 1400), CHAR_OFFSET.MARKUS_PROL, "markusprologue_body", CHAR_OFFSET.MARKUS_PROL, "images/characters/markus/prologue/face/blushing.webp")
image markusprologue talk   = Composite((678, 1400), CHAR_OFFSET.MARKUS_PROL, "markusprologue_body") # effectively null
############################################
image markusprologue = Composite((678, 1400), CHAR_OFFSET.MARKUS_PROL, "markusprologue_body")

image markusprologue_body = ConditionSwitch(
        "worldChars['markus']['clothes'] == 'scout'",       "images/characters/markus/prologue/scout.webp",
        "worldChars['markus']['clothes'] == 'normal_p2'",   "images/characters/markus/prologue/norm_p2.webp",
        "worldChars['markus']['clothes'] == 'scout_p2'",    "images/characters/markus/prologue/scout_p2.webp",
        "True", "images/characters/markus/prologue/norm.webp")