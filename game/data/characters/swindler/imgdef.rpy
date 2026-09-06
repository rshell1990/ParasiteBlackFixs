############# swindler expressions ############
image swindler angry = Composite((483, 1298), CHAR_OFFSET.SWINDLER, "swindler_body", CHAR_OFFSET.SWINDLER, "images/characters/swindler/face/angry.webp")
image swindler happy = Composite((483, 1298), CHAR_OFFSET.SWINDLER, "swindler_body", CHAR_OFFSET.SWINDLER, "images/characters/swindler/face/happy.webp")
image swindler laugh = Composite((483, 1298), CHAR_OFFSET.SWINDLER, "swindler_body", CHAR_OFFSET.SWINDLER, "images/characters/swindler/face/laugh.webp")
image swindler sad   = Composite((483, 1298), CHAR_OFFSET.SWINDLER, "swindler_body", CHAR_OFFSET.SWINDLER, "images/characters/swindler/face/sad.webp")
image swindler scared= Composite((483, 1298), CHAR_OFFSET.SWINDLER, "swindler_body", CHAR_OFFSET.SWINDLER, "images/characters/swindler/face/scared.webp")
image swindler smug  = Composite((483, 1298), CHAR_OFFSET.SWINDLER, "swindler_body", CHAR_OFFSET.SWINDLER, "images/characters/swindler/face/smug.webp")
##############################################
image swindler = Composite((483, 1298), CHAR_OFFSET.SWINDLER, "swindler_body")
image swindler_body = ConditionSwitch(
    "worldChars['swindler']['pose'] == 'knife'",  "images/characters/swindler/knife.webp",
    "True", "images/characters/swindler/normal.webp",
)