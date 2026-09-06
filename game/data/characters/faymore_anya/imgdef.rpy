################# anya expressions ##############
image anya think = Composite((477, 1340), CHAR_OFFSET.ANYA, "anya_body", CHAR_OFFSET.ANYA, "images/characters/anya/face/think.webp")
image anya shock = Composite((477, 1340), CHAR_OFFSET.ANYA, "anya_body", CHAR_OFFSET.ANYA, "images/characters/anya/face/shock.webp")
image anya scared= Composite((477, 1340), CHAR_OFFSET.ANYA, "anya_body", CHAR_OFFSET.ANYA, "images/characters/anya/face/scared.webp")
image anya sad   = Composite((477, 1340), CHAR_OFFSET.ANYA, "anya_body", CHAR_OFFSET.ANYA, "images/characters/anya/face/sad.webp")
image anya cry   = "anya sad"
image anya crying   = "anya sad"
image anya lewd  = Composite((477, 1340), CHAR_OFFSET.ANYA, "anya_body", CHAR_OFFSET.ANYA, "images/characters/anya/face/lewd.webp")
image anya flirt  = "anya lewd"
image anya laugh = Composite((477, 1340), CHAR_OFFSET.ANYA, "anya_body", CHAR_OFFSET.ANYA, "images/characters/anya/face/laugh.webp")
image anya smile = "anya laugh"
image anya happy = Composite((477, 1340), CHAR_OFFSET.ANYA, "anya_body", CHAR_OFFSET.ANYA, "images/characters/anya/face/happy.webp")
image anya emb = Composite((477, 1340), CHAR_OFFSET.ANYA, "anya_body", CHAR_OFFSET.ANYA, "images/characters/anya/face/embar.webp")
image anya angry = Composite((477, 1340), CHAR_OFFSET.ANYA, "anya_body", CHAR_OFFSET.ANYA, "images/characters/anya/face/angry.webp")

image anya blush = "anya"
image anya talk  = "anya"

##################################################
# layers are body -> face
image anya = Composite((477, 1340), CHAR_OFFSET.ANYA, "anya_body")
image anya_body = ConditionSwitch(
    "worldChars['anya']['clothes']=='naked'",  "anya_naked",
    "worldChars['anya']['clothes']=='ling'",   "anya_ling",
    "True",  "anya_dress",
)

image anya_ling = ConditionSwitch(
    "worldChars['chanyi']['preg'] == 0", "images/characters/anya/ling.webp",
    "worldChars['chanyi']['preg'] == 1", "images/characters/anya/preg/ling_1.webp",
    "worldChars['chanyi']['preg'] == 2", "images/characters/anya/preg/ling_2.webp",
    "worldChars['chanyi']['preg'] == 3", "images/characters/anya/preg/ling_3.webp",
    "worldChars['chanyi']['preg'] == 4", "images/characters/anya/ling.webp",
)

image anya_naked = ConditionSwitch(
    "worldChars['chanyi']['preg'] == 0", "images/characters/anya/naked.webp",
    "worldChars['chanyi']['preg'] == 1", "images/characters/anya/preg/naked_1.webp",
    "worldChars['chanyi']['preg'] == 2", "images/characters/anya/preg/naked_2.webp",
    "worldChars['chanyi']['preg'] == 3", "images/characters/anya/preg/naked_3.webp",
    "worldChars['chanyi']['preg'] == 4", "images/characters/anya/naked.webp"
)

image anya_dress = ConditionSwitch(
    "worldChars['chanyi']['preg'] == 0", "images/characters/anya/dress.webp",
    "worldChars['chanyi']['preg'] == 1", "images/characters/anya/preg/dress_1.webp",
    "worldChars['chanyi']['preg'] == 2", "images/characters/anya/preg/dress_2.webp",
    "worldChars['chanyi']['preg'] == 3", "images/characters/anya/preg/dress_3.webp",
    "worldChars['chanyi']['preg'] == 4", "images/characters/anya/preg/dress_4.webp"
)