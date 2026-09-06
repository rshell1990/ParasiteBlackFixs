############### giselra expressions ##############
image giselra angry = Composite((654, 1399), CHAR_OFFSET.GISELRA, "giselra_body", CHAR_OFFSET.GISELRA, "images/characters/giselra/face/angry.webp")
image giselra shock = Composite((654, 1399), CHAR_OFFSET.GISELRA, "giselra_body", CHAR_OFFSET.GISELRA, "images/characters/giselra/face/shock.webp")
image giselra shy   = Composite((654, 1399), CHAR_OFFSET.GISELRA, "giselra_body", CHAR_OFFSET.GISELRA, "images/characters/giselra/face/shy.webp")
image giselra smile = Composite((654, 1399), CHAR_OFFSET.GISELRA, "giselra_body", CHAR_OFFSET.GISELRA, "images/characters/giselra/face/smile.webp")
image giselra think = Composite((654, 1399), CHAR_OFFSET.GISELRA, "giselra_body", CHAR_OFFSET.GISELRA, "images/characters/giselra/face/think.webp")
image giselra talk  = "giselra"
#################################################
image giselra = Composite((654, 1399), CHAR_OFFSET.GISELRA, "giselra_body")

image giselra_body = ConditionSwitch(
    "worldChars['giselra']['clothes'] == 'naked'", "giselra_naked",
    "worldChars['giselra']['clothes'] == 'ling'",  "giselra_ling",
    "True",  "giselra_normal",
    )
image giselra_normal = ConditionSwitch(
        "worldChars['giselra']['preg'] == 0", "images/characters/giselra/normal.webp",
        "worldChars['giselra']['preg'] == 1", "images/characters/giselra/preg/normal_1.webp",
        "worldChars['giselra']['preg'] == 2", "images/characters/giselra/preg/normal_2.webp",
        "worldChars['giselra']['preg'] == 3", "images/characters/giselra/preg/normal_3.webp",
        "worldChars['giselra']['preg'] == 4", "images/characters/giselra/normal.webp")
image giselra_ling = ConditionSwitch(
        "worldChars['giselra']['preg'] == 0", "images/characters/giselra/ling.webp",
        "worldChars['giselra']['preg'] == 1", "images/characters/giselra/preg/ling_1.webp",
        "worldChars['giselra']['preg'] == 2", "images/characters/giselra/preg/ling_2.webp",
        "worldChars['giselra']['preg'] == 3", "images/characters/giselra/preg/ling_3.webp",
        "worldChars['giselra']['preg'] == 4", "images/characters/giselra/ling.webp")
image giselra_naked = ConditionSwitch(
        "worldChars['giselra']['preg'] == 0", "images/characters/giselra/naked.webp",
        "worldChars['giselra']['preg'] == 1", "images/characters/giselra/preg/naked_1.webp",
        "worldChars['giselra']['preg'] == 2", "images/characters/giselra/preg/naked_2.webp",
        "worldChars['giselra']['preg'] == 3", "images/characters/giselra/preg/naked_3.webp",
        "worldChars['giselra']['preg'] == 4", "images/characters/giselra/naked.webp")