################# dramora expressions ##############
image dramora angry     = Composite((650, 1238), CHAR_OFFSET.DRAMORA, "dramora_body", CHAR_OFFSET.DRAMORA, "images/characters/dramora/face/angry.webp")
image dramora angry2    = Composite((650, 1238), CHAR_OFFSET.DRAMORA, "dramora_body", CHAR_OFFSET.DRAMORA, "images/characters/dramora/face/angry2.webp")
image dramora sassy     = Composite((650, 1238), CHAR_OFFSET.DRAMORA, "dramora_body", CHAR_OFFSET.DRAMORA, "images/characters/dramora/face/sassy.webp")
image dramora smile     = Composite((650, 1238), CHAR_OFFSET.DRAMORA, "dramora_body", CHAR_OFFSET.DRAMORA, "images/characters/dramora/face/smile.webp")
image dramora smile2    = Composite((650, 1238), CHAR_OFFSET.DRAMORA, "dramora_body", CHAR_OFFSET.DRAMORA, "images/characters/dramora/face/smile2.webp")
image dramora talk = "dramora"
##################################################
image dramora = Composite((650, 1238), CHAR_OFFSET.DRAMORA, "dramora_body")
image dramora_body = "images/characters/dramora/normal.webp"

init python:
    config.tag_layer["dramora"] = "characters"