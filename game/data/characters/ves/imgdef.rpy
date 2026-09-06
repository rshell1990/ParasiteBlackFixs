################# ves expressions ###############
image ves smile_talk    = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/laugh.webp", CHAR_OFFSET.VES, "ves_animtalk", CHAR_OFFSET.VES, "ves_hood")
image ves angry_talk    = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/angry.webp", CHAR_OFFSET.VES, "ves_animtalk", CHAR_OFFSET.VES, "ves_hood")
image ves friendly_talk = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/happy.webp", CHAR_OFFSET.VES, "ves_animtalk", CHAR_OFFSET.VES, "ves_hood")
image ves lewd_talk     = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/blush.webp", CHAR_OFFSET.VES, "ves_animtalk", CHAR_OFFSET.VES, "ves_hood")
image ves blush_talk    = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/blush.webp", CHAR_OFFSET.VES, "ves_animtalk", CHAR_OFFSET.VES, "ves_hood")
image ves sad_talk      = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/sad.webp",   CHAR_OFFSET.VES, "ves_animtalk", CHAR_OFFSET.VES, "ves_hood")
image ves think_talk    = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/sad.webp",   CHAR_OFFSET.VES, "ves_animtalk", CHAR_OFFSET.VES, "ves_hood")
image ves surp_talk     = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/shock.webp", CHAR_OFFSET.VES, "ves_animtalk", CHAR_OFFSET.VES, "ves_hood")
image ves talk          = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "ves_animtalk", CHAR_OFFSET.VES, "ves_hood")
image ves smile         = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/laugh.webp", CHAR_OFFSET.VES, "ves_hood")
image ves angry         = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/angry.webp", CHAR_OFFSET.VES, "ves_hood")
image ves friendly      = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/happy.webp", CHAR_OFFSET.VES, "ves_hood")
image ves lewd          = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/blush.webp", CHAR_OFFSET.VES, "ves_hood")
image ves blush         = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/blush.webp", CHAR_OFFSET.VES, "ves_hood")
image ves sad           = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/sad.webp",   CHAR_OFFSET.VES, "ves_hood")
image ves think         = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/sad.webp",   CHAR_OFFSET.VES, "ves_hood")
image ves surprised     = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "images/characters/ves/face/shock.webp", CHAR_OFFSET.VES, "ves_hood")
image ves shock         = "ves surprised"
################################################
image ves = Composite((810, 1400), CHAR_OFFSET.VES, "ves_body", CHAR_OFFSET.VES, "ves_hood")
image ves_body = ConditionSwitch(
    "worldChars['ves']['clothes'] == 'naked'",  "images/characters/ves/naked.webp",
    "worldChars['ves']['clothes'] == 'ling'",   "images/characters/ves/ling.webp",
    "worldChars['ves']['clothes'] == 'dom'",    "images/characters/ves/dom.webp",
    "worldChars['ves']['clothes'] == 'dress'",  "images/characters/ves/dress.webp",
    "worldChars['ves']['clothes'] == 'maid'",   "images/characters/ves/maid.webp",
    "True", "images/characters/ves/armor.webp",
)
image ves_hood = ConditionSwitch(
    # INVERSE: normal is hood, rest is not!
    "worldChars['ves']['clothes'] == 'normal'", "images/characters/ves/hood.webp", 
    "True", Null())
image ves_animtalk = Null()

image cg_ves_maid_kneel:
    "cg_ves_maid_kneel_base"
    offset (0, 310)
image cg_ves_maid_leash:
    "cg_ves_maid_leash_base"
    offset (0, 60)