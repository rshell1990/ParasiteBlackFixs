############# phoah expressions #################
image phoah angry   = Composite((989, 1400), CHAR_OFFSET.PHOAH, "phoah_body", CHAR_OFFSET.PHOAH, "images/characters/phoah/face/angry.webp")
image phoah blush   = Composite((989, 1400), CHAR_OFFSET.PHOAH, "phoah_body", CHAR_OFFSET.PHOAH, "images/characters/phoah/face/blush.webp")
image phoah happy   = Composite((989, 1400), CHAR_OFFSET.PHOAH, "phoah_body", CHAR_OFFSET.PHOAH, "images/characters/phoah/face/happy.webp")
image phoah laugh   = Composite((989, 1400), CHAR_OFFSET.PHOAH, "phoah_body", CHAR_OFFSET.PHOAH, "images/characters/phoah/face/laugh.webp")
image phoah sad     = Composite((989, 1400), CHAR_OFFSET.PHOAH, "phoah_body", CHAR_OFFSET.PHOAH, "images/characters/phoah/face/sad.webp")
image phoah scared  = Composite((989, 1400), CHAR_OFFSET.PHOAH, "phoah_body", CHAR_OFFSET.PHOAH, "images/characters/phoah/face/scared.webp")
image phoah shock   = Composite((989, 1400), CHAR_OFFSET.PHOAH, "phoah_body", CHAR_OFFSET.PHOAH, "images/characters/phoah/face/scared.webp")
image phoah think   = Composite((989, 1400), CHAR_OFFSET.PHOAH, "phoah_body", CHAR_OFFSET.PHOAH, "images/characters/phoah/face/think.webp")
image phoah talk = "phoah" # stub
###############################################
image phoah = Composite((989, 1400), CHAR_OFFSET.PHOAH, "phoah_body")
image phoah_body = ConditionSwitch(
    "worldChars['phoah']['clothes'] == 'naked'", "phoah_naked",
    "True", "phoah_normal",
)

image phoah_normal = ConditionSwitch(
    "worldChars['phoah']['wings'] == False", "images/characters/phoah/normal.webp",
    "worldChars['phoah']['wings'] == True", "images/characters/phoah/normal_wings.webp")

image phoah_naked = ConditionSwitch(
    "worldChars['phoah']['wings'] == False", "images/characters/phoah/naked.webp",
    "worldChars['phoah']['wings'] == True", "images/characters/phoah/naked_wings.webp")