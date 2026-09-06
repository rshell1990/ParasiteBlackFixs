############### ingrid expressions ##############
image ingrid angry  = Composite((654, 1399), CHAR_OFFSET.INGRID, "ingrid_body", CHAR_OFFSET.INGRID, "images/characters/ingrid/face/angry.webp", CHAR_OFFSET.INGRID, "ingrid_mask")
image ingrid blush  = Composite((654, 1399), CHAR_OFFSET.INGRID, "ingrid_body", CHAR_OFFSET.INGRID, "images/characters/ingrid/face/blush.webp", CHAR_OFFSET.INGRID, "ingrid_mask")
image ingrid cry    = Composite((654, 1399), CHAR_OFFSET.INGRID, "ingrid_body", CHAR_OFFSET.INGRID, "images/characters/ingrid/face/cry.webp",   CHAR_OFFSET.INGRID, "ingrid_mask")
image ingrid laugh  = Composite((654, 1399), CHAR_OFFSET.INGRID, "ingrid_body", CHAR_OFFSET.INGRID, "images/characters/ingrid/face/laugh.webp", CHAR_OFFSET.INGRID, "ingrid_mask")
image ingrid sad    = Composite((654, 1399), CHAR_OFFSET.INGRID, "ingrid_body", CHAR_OFFSET.INGRID, "images/characters/ingrid/face/sad.webp",   CHAR_OFFSET.INGRID, "ingrid_mask")
image ingrid scared = Composite((654, 1399), CHAR_OFFSET.INGRID, "ingrid_body", CHAR_OFFSET.INGRID, "images/characters/ingrid/face/scared.webp",CHAR_OFFSET.INGRID, "ingrid_mask")
image ingrid smile  = Composite((654, 1399), CHAR_OFFSET.INGRID, "ingrid_body", CHAR_OFFSET.INGRID, "images/characters/ingrid/face/smile.webp", CHAR_OFFSET.INGRID, "ingrid_mask")
image ingrid think  = Composite((654, 1399), CHAR_OFFSET.INGRID, "ingrid_body", CHAR_OFFSET.INGRID, "images/characters/ingrid/face/think.webp", CHAR_OFFSET.INGRID, "ingrid_mask")
image ingrid talk  = "ingrid"
#################################################
image ingrid =       Composite((654, 1399), CHAR_OFFSET.INGRID, "ingrid_body", CHAR_OFFSET.INGRID, "ingrid_mask")

image ingrid_body = ConditionSwitch(
    "worldChars['ingrid']['clothes'] == 'naked'",  "ingrid_naked",
    "worldChars['ingrid']['clothes'] == 'ling'",   "ingrid_ling",
    "True",  "ingrid_normal",
    )

image ingrid_mask = ConditionSwitch(
    "worldChars['ingrid']['mask'] == True", "images/characters/ingrid/mask.webp",
    "True", Null(),
)

image ingrid_normal = ConditionSwitch(
        "worldChars['ingrid']['preg'] == 0", "images/characters/ingrid/normal.webp",
        "worldChars['ingrid']['preg'] == 1", "images/characters/ingrid/preg/normal_1.webp",
        "worldChars['ingrid']['preg'] == 2", "images/characters/ingrid/preg/normal_2.webp",
        "worldChars['ingrid']['preg'] == 3", "images/characters/ingrid/preg/normal_3.webp",
        "worldChars['ingrid']['preg'] == 4", "images/characters/ingrid/normal.webp")
image ingrid_ling = ConditionSwitch(
        "worldChars['ingrid']['preg'] == 0", "images/characters/ingrid/ling.webp",
        "worldChars['ingrid']['preg'] == 1", "images/characters/ingrid/preg/ling_1.webp",
        "worldChars['ingrid']['preg'] == 2", "images/characters/ingrid/preg/ling_2.webp",
        "worldChars['ingrid']['preg'] == 3", "images/characters/ingrid/preg/ling_3.webp",
        "worldChars['ingrid']['preg'] == 4", "images/characters/ingrid/ling.webp")
image ingrid_naked = ConditionSwitch(
        "worldChars['ingrid']['preg'] == 0", "images/characters/ingrid/naked.webp",
        "worldChars['ingrid']['preg'] == 1", "images/characters/ingrid/preg/naked_1.webp",
        "worldChars['ingrid']['preg'] == 2", "images/characters/ingrid/preg/naked_2.webp",
        "worldChars['ingrid']['preg'] == 3", "images/characters/ingrid/preg/naked_3.webp",
        "worldChars['ingrid']['preg'] == 4", "images/characters/ingrid/naked.webp")