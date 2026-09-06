################### carina expressions #########
image carina angry = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/angry.webp")
image carina happy = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/happy.webp")
image carina horny = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/horny.webp")
image carina laugh = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/laugh.webp")
# smile is copy of laugh
image carina smile  = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/laugh.webp")
image carina lewd   = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/lewd.webp")
image carina sad    = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/sad.webp")
image carina serious = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/serious.webp")
# think is copy of serious
image carina think  = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/serious.webp")
image carina shock  = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/shock.webp")
# surprised is copy of shock
image carina surprised = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/shock.webp")
# scared is copy of shock
image carina scared = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/shock.webp")
image carina smug   = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body", CHAR_OFFSET.CARINA, "images/characters/carina/face/smug.webp")
image carina talk = "carina"
#####################################################
image carina = Composite((792, 1478), CHAR_OFFSET.CARINA, "carina_body")

image carina_body = ConditionSwitch(
        "worldChars['carina']['clothes'] == 'naked'",   "carina_naked",
        "worldChars['carina']['clothes'] == 'ling'",    "carina_ling",
        "True",  "carina_normal",
)

image carina_normal = ConditionSwitch(
                "worldChars['carina']['preg'] == 0", "images/characters/carina/normal.webp",
                "worldChars['carina']['preg'] == 1", "images/characters/carina/preg/normal_1.webp",
                "worldChars['carina']['preg'] == 2", "images/characters/carina/preg/normal_2.webp",
                "worldChars['carina']['preg'] == 3", "images/characters/carina/preg/normal_3.webp",
                "worldChars['carina']['preg'] == 4", "images/characters/carina/normal.webp")
image carina_naked = ConditionSwitch(
                "worldChars['carina']['preg'] == 0", "images/characters/carina/naked.webp",
                "worldChars['carina']['preg'] == 1", "images/characters/carina/preg/naked_1.webp",
                "worldChars['carina']['preg'] == 2", "images/characters/carina/preg/naked_2.webp",
                "worldChars['carina']['preg'] == 3", "images/characters/carina/preg/naked_3.webp",
                "worldChars['carina']['preg'] == 4", "images/characters/carina/naked.webp")
image carina_ling = ConditionSwitch(
                "worldChars['carina']['preg'] == 0", "images/characters/carina/ling.webp",
                "worldChars['carina']['preg'] == 1", "images/characters/carina/preg/ling_1.webp",
                "worldChars['carina']['preg'] == 2", "images/characters/carina/preg/ling_2.webp",
                "worldChars['carina']['preg'] == 3", "images/characters/carina/preg/ling_3.webp",
                "worldChars['carina']['preg'] == 4", "images/characters/carina/ling.webp")
