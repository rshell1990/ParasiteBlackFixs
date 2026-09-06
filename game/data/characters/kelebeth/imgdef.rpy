################### kelebeth expressions #########
image kelebeth angry    = Composite((755, 1249), CHAR_OFFSET.KELEBETH, "kelebeth_body", CHAR_OFFSET.KELEBETH, "images/characters/kelebeth/face/angry.webp")
image kelebeth blush    = Composite((755, 1249), CHAR_OFFSET.KELEBETH, "kelebeth_body", CHAR_OFFSET.KELEBETH, "images/characters/kelebeth/face/blush.webp")
image kelebeth laugh    = Composite((755, 1249), CHAR_OFFSET.KELEBETH, "kelebeth_body", CHAR_OFFSET.KELEBETH, "images/characters/kelebeth/face/laugh.webp")
image kelebeth sad      = Composite((755, 1249), CHAR_OFFSET.KELEBETH, "kelebeth_body", CHAR_OFFSET.KELEBETH, "images/characters/kelebeth/face/sad.webp")
image kelebeth scared   = Composite((755, 1249), CHAR_OFFSET.KELEBETH, "kelebeth_body", CHAR_OFFSET.KELEBETH, "images/characters/kelebeth/face/scared.webp")
image kelebeth think    = Composite((755, 1249), CHAR_OFFSET.KELEBETH, "kelebeth_body", CHAR_OFFSET.KELEBETH, "images/characters/kelebeth/face/think.webp")
#####################################################
image kelebeth          = Composite((755, 1249), CHAR_OFFSET.KELEBETH, "kelebeth_body")

image kelebeth_body = ConditionSwitch(
    "worldChars['kelebeth']['clothes'] == 'naked'",  "kelebeth_naked", 
    "True",  "kelebeth_naked")

image kelebeth_naked = ConditionSwitch(
        "worldChars['kelebeth']['preg'] == 0", "images/characters/kelebeth/naked.webp",
        "worldChars['kelebeth']['preg'] == 1", "images/characters/kelebeth/preg/naked_1.webp",
        "worldChars['kelebeth']['preg'] == 2", "images/characters/kelebeth/preg/naked_2.webp",
        "worldChars['kelebeth']['preg'] == 3", "images/characters/kelebeth/preg/naked_3.webp",
        "worldChars['kelebeth']['preg'] == 4", "images/characters/kelebeth/naked.webp")

image cg_kelebeth_kneel:
    "cg_kelebeth_kneel_base"
    offset (0, 330)

init python:
    config.tag_layer["cg_kelebeth_kneel"] = "characters"