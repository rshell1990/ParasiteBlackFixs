############# gavkat expressions #################
image gavkat angry = Composite((488, 917), CHAR_OFFSET.GAVKAT, "gavkat_body", CHAR_OFFSET.GAVKAT, "images/characters/gavkat/face/angry.webp")
image gavkat think = Composite((488, 917), CHAR_OFFSET.GAVKAT, "gavkat_body", CHAR_OFFSET.GAVKAT, "images/characters/gavkat/face/think.webp")
image gavkat smile = Composite((488, 917), CHAR_OFFSET.GAVKAT, "gavkat_body", CHAR_OFFSET.GAVKAT, "images/characters/gavkat/face/smile.webp")

image gavkat       = Composite((488, 917), CHAR_OFFSET.GAVKAT, "gavkat_body")
image gavkat talk  = "gavkat"

image gavkat_body = "images/characters/gavkat/normal.webp"
init python:
    config.tag_layer["gavkat"] = "characters"