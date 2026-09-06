############# sypha expressions ############
image sypha talk    = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "sypha_animtalk")
image sypha angry   = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/angry.webp")
image sypha blush   = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/blush.webp")
image sypha cry     = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/cry.webp")
image sypha disgust = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/disgust.webp")
image sypha embarr  = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/embarr.webp")
image sypha fury    = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/fury.webp")
image sypha happy   = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/happy.webp")
image sypha joy_tears = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/joy_tears.webp")
image sypha laugh   = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/laugh.webp")
image sypha mad     = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/mad.webp")
image sypha perv    = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/perv.webp")
image sypha sad     = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/sad.webp")
image sypha scared  = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/scared.webp")
image sypha shock   = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/shock.webp")
image sypha smug    = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/smug.webp")
image sypha think   = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body", CHAR_OFFSET.SYPHA, "images/characters/sypha/face/think.webp")
##############################################
image sypha = Composite((588, 1400), CHAR_OFFSET.SYPHA, "sypha_body")
image sypha_body = ConditionSwitch(
    "worldChars['sypha']['clothes'] == 'normal_2'",     "images/characters/sypha/normal_2.webp",
    "worldChars['sypha']['clothes'] == 'naked'",        "images/characters/sypha/naked.webp",
    "worldChars['sypha']['clothes'] == 'armour'",       "images/characters/sypha/armour.webp",
    "worldChars['sypha']['clothes'] == 'armour_helm'",  "images/characters/sypha/armour_helm.webp",
    "worldChars['sypha']['clothes'] == 'ling'",         "images/characters/sypha/ling.webp",
    "worldChars['sypha']['clothes'] == 'ling_chain'",   "images/characters/sypha/ling_chain.webp",
    "worldChars['sypha']['clothes'] == 'wet'",          "images/characters/sypha/wet.webp",
    "worldChars['sypha']['clothes'] == 'towel_wet'",    "images/characters/sypha/towel_wet.webp",
    "worldChars['sypha']['clothes'] == 'towel'",        "images/characters/sypha/towel.webp",
    "worldChars['sypha']['clothes'] == 'dress'",        "images/characters/sypha/dress.webp",
    "True",       "images/characters/sypha/normal.webp",
)

image sypha_animtalk:
    Null()