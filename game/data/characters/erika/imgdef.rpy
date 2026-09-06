################# erika expressions ##############
image erika angry       = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/angry.webp", CHAR_OFFSET.ERIKA, "erika_hat")
image erika drunk       = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/drunk.webp", CHAR_OFFSET.ERIKA, "erika_hat")
image erika serious     = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/serious.webp", CHAR_OFFSET.ERIKA, "erika_hat")
image erika think       = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/think.webp", CHAR_OFFSET.ERIKA, "erika_hat")
image erika lewd        = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/lewd.webp",  CHAR_OFFSET.ERIKA, "erika_hat")
image erika sad         = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/sad.webp",   CHAR_OFFSET.ERIKA, "erika_hat")
image erika surp        = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/shock.webp", CHAR_OFFSET.ERIKA, "erika_hat")
image erika smile       = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/laugh.webp", CHAR_OFFSET.ERIKA, "erika_hat")
image erika angry_talk  = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/angry.webp", CHAR_OFFSET.ERIKA, "erika_hat")
image erika lewd_talk   = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/lewd.webp",  CHAR_OFFSET.ERIKA, "erika_hat")
image erika sad_talk    = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/sad.webp",   CHAR_OFFSET.ERIKA, "erika_hat")
image erika surp_talk   = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/shock.webp", CHAR_OFFSET.ERIKA, "erika_hat")
image erika smile_talk  = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "images/characters/erika/face/laugh.webp", CHAR_OFFSET.ERIKA, "erika_hat")
image erika talk        = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body")
##################################################
# layers are body -> face -> hat
image erika = Composite((637, 1350), CHAR_OFFSET.ERIKA, "erika_body", CHAR_OFFSET.ERIKA, "erika_hat")

image erika_body = ConditionSwitch(
    "worldChars['erika']['clothes']=='naked'",  "images/characters/erika/naked.webp",
    "True", "images/characters/erika/dress.webp",
)

image erika_hat = ConditionSwitch("worldChars['erika']['clothes']=='normal'", "images/characters/erika/face/hat.webp", "True", Null())
