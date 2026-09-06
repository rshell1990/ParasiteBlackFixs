############### nyx expressions ##############
image nyx angry     = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_angry")
image nyx arrogant  = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_arrogant")
image nyx blush     = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_blush")
image nyx crying    = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_crying")
image nyx disg      = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_disg")
image nyx drunk     = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_drunk")
image nyx drunk_sad = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_drunk_sad")
image nyx furious   = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_furious")
image nyx laugh     = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_laugh")
image nyx sad       = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_sad")
image nyx scared    = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_scared")
image nyx shock     = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_shock")
image nyx smile     = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_smile")
image nyx think     = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body", CHAR_OFFSET.NYX, "nyx_face_think")
image nyx talk = "nyx"
##############################################
image nyx = Composite((645, 1340), CHAR_OFFSET.NYX, "nyx_body")
image nyx_body = ConditionSwitch( # EVERY PREG VARIATION IS MISSING
    "worldChars['nyx']['clothes'] == 'naked'",      "images/characters/nyx/naked.webp",
    "worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/normal_ash.webp",
    "worldChars['nyx']['clothes'] == 'slave'",      "images/characters/nyx/slave.webp",
    "worldChars['nyx']['clothes'] == 'robe'",       "images/characters/nyx/robe.webp",
    "worldChars['nyx']['clothes'] == 'robe_mug'",   "images/characters/nyx/robe_mug.webp",
    "worldChars['nyx']['clothes'] == 'lingerie'",   "images/characters/nyx/ling.webp",
    "True",     "images/characters/nyx/normal.webp",
)


############################
## expression conditionals (for ashed)
image nyx_face_angry    = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/angry.webp",      "True", "images/characters/nyx/face/angry.webp")
image nyx_face_arrogant = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/arrogant.webp",   "True", "images/characters/nyx/face/arrogant.webp")
image nyx_face_blush    = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/blush.webp",      "True", "images/characters/nyx/face/blush.webp")
image nyx_face_crying   = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/crying.webp",     "True", "images/characters/nyx/face/crying.webp")
image nyx_face_disg     = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/disg.webp",       "True", "images/characters/nyx/face/disg.webp")
image nyx_face_drunk    = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/drunk.webp",      "True", "images/characters/nyx/face/drunk.webp")
image nyx_face_drunk_sad= ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/drunk_sad.webp",  "True", "images/characters/nyx/face/drunk_sad.webp")
image nyx_face_furious  = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/furious.webp",    "True", "images/characters/nyx/face/furious.webp")
image nyx_face_laugh    = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/laugh.webp",      "True", "images/characters/nyx/face/laugh.webp")
image nyx_face_sad      = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/sad.webp",        "True", "images/characters/nyx/face/sad.webp")
image nyx_face_scared   = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/scared.webp",     "True", "images/characters/nyx/face/scared.webp")
image nyx_face_shock    = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/shock.webp",      "True", "images/characters/nyx/face/shock.webp")
image nyx_face_smile    = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/smile.webp",      "True", "images/characters/nyx/face/smile.webp")
image nyx_face_think    = ConditionSwitch("worldChars['nyx']['clothes'] == 'normal_ash'", "images/characters/nyx/face_ash/think.webp",      "True", "images/characters/nyx/face/think.webp")


image cg_nyx_halfnaked:
    offset CHAR_OFFSET.NYX
    "cg_nyx_halfnaked_base"
