############# garen expressions #################
image garen angry   = Composite((562, 1400), CHAR_OFFSET.GAREN, "garen_body", CHAR_OFFSET.GAREN, "images/characters/garen/face/angry.webp")
image garen sad     = Composite((562, 1400), CHAR_OFFSET.GAREN, "garen_body", CHAR_OFFSET.GAREN, "images/characters/garen/face/sad.webp")
image garen sassy   = Composite((562, 1400), CHAR_OFFSET.GAREN, "garen_body", CHAR_OFFSET.GAREN, "images/characters/garen/face/sassy.webp")
image garen scared  = Composite((562, 1400), CHAR_OFFSET.GAREN, "garen_body", CHAR_OFFSET.GAREN, "images/characters/garen/face/scared.webp")
image garen smile   = Composite((562, 1400), CHAR_OFFSET.GAREN, "garen_body", CHAR_OFFSET.GAREN, "images/characters/garen/face/smile.webp")
image garen think   = Composite((562, 1400), CHAR_OFFSET.GAREN, "garen_body", CHAR_OFFSET.GAREN, "images/characters/garen/face/think.webp")
image garen talk    = "garen"
###############################################
image garen = Composite((562, 1400), CHAR_OFFSET.GAREN, "garen_body")

image garen_body = "images/characters/garen/normal.webp"
init python:
    config.tag_layer["garen"] = "characters"