################# esme expressions ##############
image esme angry    = Composite((580, 1161), CHAR_OFFSET.ESME, "esme_body", CHAR_OFFSET.ESME, "images/characters/esme/face/angry.webp",     CHAR_OFFSET.ESME, "esme_body_layer_top")
image esme cry      = Composite((580, 1161), CHAR_OFFSET.ESME, "esme_body", CHAR_OFFSET.ESME, "images/characters/esme/face/crying.webp",    CHAR_OFFSET.ESME, "esme_body_layer_top")
image esme happy    = Composite((580, 1161), CHAR_OFFSET.ESME, "esme_body", CHAR_OFFSET.ESME, "images/characters/esme/face/happy.webp",     CHAR_OFFSET.ESME, "esme_body_layer_top")
# smile is copy of happy
image esme smile    = Composite((580, 1161), CHAR_OFFSET.ESME, "esme_body", CHAR_OFFSET.ESME, "images/characters/esme/face/happy.webp",     CHAR_OFFSET.ESME, "esme_body_layer_top")
image esme laugh    = Composite((580, 1161), CHAR_OFFSET.ESME, "esme_body", CHAR_OFFSET.ESME, "images/characters/esme/face/laugh.webp",     CHAR_OFFSET.ESME, "esme_body_layer_top")
image esme lewd     = Composite((580, 1161), CHAR_OFFSET.ESME, "esme_body", CHAR_OFFSET.ESME, "images/characters/esme/face/lewd.webp",      CHAR_OFFSET.ESME, "esme_body_layer_top")
image esme sad      = Composite((580, 1161), CHAR_OFFSET.ESME, "esme_body", CHAR_OFFSET.ESME, "images/characters/esme/face/sad.webp",       CHAR_OFFSET.ESME, "esme_body_layer_top")
image esme scared   = Composite((580, 1161), CHAR_OFFSET.ESME, "esme_body", CHAR_OFFSET.ESME, "images/characters/esme/face/scared.webp",    CHAR_OFFSET.ESME, "esme_body_layer_top")
image esme shock    = Composite((580, 1161), CHAR_OFFSET.ESME, "esme_body", CHAR_OFFSET.ESME, "images/characters/esme/face/shocked.webp",   CHAR_OFFSET.ESME, "esme_body_layer_top")
image esme shocked  = "esme shock"
image esme talk     = "esme"
##################################################
image esme = Composite((580, 1161), CHAR_OFFSET.ESME, "esme_body", CHAR_OFFSET.ESME, "esme_body_layer_top")
image esme_body = ConditionSwitch(
    "worldChars['esme']['clothes'] == 'naked'",     "images/characters/esme/naked.webp",
    "worldChars['esme']['clothes'] == 'in_gold'",   "images/characters/esme/in_gold.webp",
    "worldChars['esme']['clothes'] == 'dom'",       "images/characters/esme/dom.webp",
    "worldChars['esme']['clothes'] == 'dress'",     "images/characters/esme/dress.webp",
    "worldChars['esme']['clothes'] == 'maid'",      "images/characters/esme/maid.webp",    
    "True",   "images/characters/esme/in_gold.webp",
)

image esme_body_layer_top = ConditionSwitch(
    "worldChars['esme']['clothes'] == 'dress'",     "images/characters/esme/mask.webp",
    "True",     Null(),
)

image cg_esme_maid_kneel:
    "cg_esme_maid_kneel_base"
    offset (0, 310)

image cg_esme_maid_leash:
    "cg_esme_maid_leash_base"
    offset (0, 60)