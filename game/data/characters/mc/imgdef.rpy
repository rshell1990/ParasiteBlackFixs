########### mc expressions post-prologue (PROLOGUE AND FEM EXPRESSIONS ARE SEPARATE, SCROLL DOWN) ############
image mc angry  = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, ConditionSwitch("worldChars['mc']['default_look'] == 'father_armor_ash'", "images/characters/mc/face/angry_ash.webp", "True", "images/characters/mc/face/angry.webp"))
image mc angry2 = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/angry2.webp")
image mc bitelip= Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/bitelip.webp")
image mc cry    = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/cry.webp")
image mc embarr = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/embarr.webp")
image mc lewd   = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/lewd.webp")
image mc sad    = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/sad.webp")
image mc drunk  = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/drunk.webp")
image mc scared = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, ConditionSwitch("worldChars['mc']['default_look'] == 'father_armor_ash'", "images/characters/mc/face/scared_ash.webp", "True", "images/characters/mc/face/scared.webp"))
image mc serious= Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/serious.webp")
image mc smile  = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/smile.webp")
image mc laugh  = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/smile.webp")
image mc smile2 = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/smile2.webp")
image mc surprised = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, ConditionSwitch("worldChars['mc']['default_look'] == 'father_armor_ash'", "images/characters/mc/face/surprised_ash.webp", "True", "images/characters/mc/face/surprised.webp"))
image mc shock = "mc surprised"
image mc think = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body", CHAR_OFFSET.MC, "images/characters/mc/face/think.webp")
image mc talk = "mc"
###################################
image mc = Composite((573, 1400), CHAR_OFFSET.MC, "mc_body")

image mc_body = ConditionSwitch(
    "worldChars['mc']['clothes'] == 'naked'",       "images/characters/mc/naked.webp",
    "worldChars['mc']['clothes'] == 'towel'",       "images/characters/mc/towel.webp",
    "worldChars['mc']['clothes'] == 'wet'",         "images/characters/mc/wet.webp",
    "worldChars['mc']['clothes'] == 'towel_wet'",   "images/characters/mc/towel_wet.webp",
    "worldChars['mc']['clothes'] == 'pants'",       "mc_default_pants",
    "worldChars['mc']['clothes'] == 'suit'",        "images/characters/mc/suit.webp",
    "worldChars['mc']['clothes'] == 'mug'",         "images/characters/mc/mug.webp",
    "True",                                         "mc_default_clothes", # aka normal
)
image mc_default_clothes = ConditionSwitch(
    "worldChars['mc']['default_look'] == 'father_armor'",       "images/characters/mc/father_armor.webp",
    "worldChars['mc']['default_look'] == 'father_armor_ash'",   "images/characters/mc/father_armor_ash.webp",
    "True",             "images/characters/mc/normal.webp", # aka normal
)
image mc_default_pants = ConditionSwitch(
    "worldChars['mc']['default_look'] == 'father_armor'",   "images/characters/mc/pants_f_arm.webp",
    "True",         "images/characters/mc/pants_norm.webp", # aka normal
)
image mc_transformed:
    Transform("images/characters/mc/mc_transformed.webp", zoom = 1.1)
    offset CHAR_OFFSET.MC_TRAN

########################### prologue only
######### mc prologue expressions ###########
image mcprologue talk   = Composite((512, 1410), CHAR_OFFSET.MC_PROL, "mcprologue_body") # effectively null
image mcprologue angry  = Composite((512, 1410), CHAR_OFFSET.MC_PROL, "mcprologue_body", CHAR_OFFSET.MC_PROL, "images/characters/mc/prologue/face/face_angry.webp")
image mcprologue sad    = Composite((512, 1410), CHAR_OFFSET.MC_PROL, "mcprologue_body", CHAR_OFFSET.MC_PROL, "images/characters/mc/prologue/face/face_sad.webp")
image mcprologue shy    = Composite((512, 1410), CHAR_OFFSET.MC_PROL, "mcprologue_body", CHAR_OFFSET.MC_PROL, "images/characters/mc/prologue/face/face_shy.webp")
image mcprologue smile  = Composite((512, 1410), CHAR_OFFSET.MC_PROL, "mcprologue_body", CHAR_OFFSET.MC_PROL, "images/characters/mc/prologue/face/face_smile.webp")
image mcprologue think  = Composite((512, 1410), CHAR_OFFSET.MC_PROL, "mcprologue_body", CHAR_OFFSET.MC_PROL, "images/characters/mc/prologue/face/face_thinking.webp")
image mcprologue scared = Composite((512, 1410), CHAR_OFFSET.MC_PROL, "mcprologue_body", CHAR_OFFSET.MC_PROL, "images/characters/mc/prologue/face/face_scared.webp")
#################################
image mcprologue = Composite((512, 1410), CHAR_OFFSET.MC_PROL, "mcprologue_body")

image mcprologue_body = ConditionSwitch(
    "worldChars['mc']['clothes'] == 'scout'",   "images/characters/mc/prologue/mc_p_gear_sw.webp",
    "True",  "images/characters/mc/prologue/mc_p.webp",
)



######### mc female expressions ##############
image mcfem angry   = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body", CHAR_OFFSET.MC_FEM, "images/characters/mc_fem/face/angry.webp")
image mcfem annoy   = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body", CHAR_OFFSET.MC_FEM, "images/characters/mc_fem/face/annoy.webp")
image mcfem cry     = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body", CHAR_OFFSET.MC_FEM, "images/characters/mc_fem/face/cry.webp")
image mcfem laugh   = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body", CHAR_OFFSET.MC_FEM, "images/characters/mc_fem/face/laugh.webp")
image mcfem lewd    = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body", CHAR_OFFSET.MC_FEM, "images/characters/mc_fem/face/lewd.webp")
image mcfem lewd_smile = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body", CHAR_OFFSET.MC_FEM, "images/characters/mc_fem/face/lewd_smile.webp")
image mcfem sad     = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body", CHAR_OFFSET.MC_FEM, "images/characters/mc_fem/face/sad.webp")
image mcfem shock   = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body", CHAR_OFFSET.MC_FEM, "images/characters/mc_fem/face/shock.webp")
image mcfem shy     = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body", CHAR_OFFSET.MC_FEM, "images/characters/mc_fem/face/shy.webp")
image mcfem smile   = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body", CHAR_OFFSET.MC_FEM, "images/characters/mc_fem/face/smile.webp")
image mcfem think   = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body", CHAR_OFFSET.MC_FEM, "images/characters/mc_fem/face/think.webp")
#############################################
image mcfem = Composite((695, 1400), CHAR_OFFSET.MC_FEM, "mcfem_body")

image mcfem_body = ConditionSwitch(
    "mc_female_outfit == 'normal'",     "mcfem_clothed",
    "mc_female_outfit == 'ling'",       "images/characters/mc_fem/ling.webp",
    "mc_female_outfit == 'naked'",      "images/characters/mc_fem/naked.webp",
    "mc_female_outfit == 'slave'",      "images/characters/mc_fem/slave.webp",
    "mc_female_outfit == 'wet'",        "images/characters/mc_fem/wet.webp",
    "mc_female_outfit == 'towel_wet'",  "images/characters/mc_fem/towel_wet.webp",
    "mc_female_outfit == 'towel'",      "images/characters/mc_fem/towel.webp",
)
image mcfem_clothed = ConditionSwitch(
    "worldChars['mc']['default_look'] == 'normal'", "images/characters/mc_fem/armor_1.webp",
    "worldChars['mc']['default_look'] == 'father_armor'", "images/characters/mc_fem/armor_2.webp")
