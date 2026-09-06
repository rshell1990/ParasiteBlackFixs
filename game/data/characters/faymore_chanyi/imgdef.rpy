################# chanyi expressions ##############
image chanyi embar  = Composite((668, 1340), CHAR_OFFSET.CHANYI, "chanyi_body", CHAR_OFFSET.CHANYI, "images/characters/chanyi/face/embar.webp")
image chanyi happy  = Composite((668, 1340), CHAR_OFFSET.CHANYI, "chanyi_body", CHAR_OFFSET.CHANYI, "images/characters/chanyi/face/happy.webp")
image chanyi laugh  = Composite((668, 1340), CHAR_OFFSET.CHANYI, "chanyi_body", CHAR_OFFSET.CHANYI, "images/characters/chanyi/face/laugh.webp")
image chanyi smile  = "chanyi laugh"
image chanyi lewd   = Composite((668, 1340), CHAR_OFFSET.CHANYI, "chanyi_body", CHAR_OFFSET.CHANYI, "images/characters/chanyi/face/lewd.webp")
image chanyi sad    = Composite((668, 1340), CHAR_OFFSET.CHANYI, "chanyi_body", CHAR_OFFSET.CHANYI, "images/characters/chanyi/face/sad.webp")
image chanyi scared = Composite((668, 1340), CHAR_OFFSET.CHANYI, "chanyi_body", CHAR_OFFSET.CHANYI, "images/characters/chanyi/face/scared.webp") 
image chanyi think  = Composite((668, 1340), CHAR_OFFSET.CHANYI, "chanyi_body", CHAR_OFFSET.CHANYI, "images/characters/chanyi/face/think.webp")
image chanyi angry  = "chanyi"
image chanyi serious= "chanyi"
image chanyi shock  = "chanyi"
image chanyi talk   = "chanyi"

##################################################
# layers are body -> face
image chanyi = Composite((668, 1340), CHAR_OFFSET.CHANYI, "chanyi_body")
image chanyi_body = ConditionSwitch(
    "worldChars['chanyi']['clothes']=='naked'",  "chanyi_naked",
    "worldChars['chanyi']['clothes']=='ling'",   "chanyi_ling",
    "True",  "chanyi_dress",
)

image chanyi_ling = ConditionSwitch(
    "worldChars['chanyi']['preg'] == 0", "images/characters/chanyi/ling.webp",
    "worldChars['chanyi']['preg'] == 1", "images/characters/chanyi/preg/ling_1.webp",
    "worldChars['chanyi']['preg'] == 2", "images/characters/chanyi/preg/ling_2.webp",
    "worldChars['chanyi']['preg'] == 3", "images/characters/chanyi/preg/ling_3.webp",
    "worldChars['chanyi']['preg'] == 4", "images/characters/chanyi/ling.webp",
)

image chanyi_naked = ConditionSwitch(
    "worldChars['chanyi']['preg'] == 0", "images/characters/chanyi/naked.webp",
    "worldChars['chanyi']['preg'] == 1", "images/characters/chanyi/preg/naked_1.webp",
    "worldChars['chanyi']['preg'] == 2", "images/characters/chanyi/preg/naked_2.webp",
    "worldChars['chanyi']['preg'] == 3", "images/characters/chanyi/preg/naked_3.webp",
    "worldChars['chanyi']['preg'] == 4", "images/characters/chanyi/naked.webp",
)

image chanyi_dress = ConditionSwitch(
    "worldChars['chanyi']['preg'] == 0", "images/characters/chanyi/dress.webp",
    "worldChars['chanyi']['preg'] == 1", "images/characters/chanyi/preg/dress_1.webp",
    "worldChars['chanyi']['preg'] == 2", "images/characters/chanyi/preg/dress_2.webp",
    "worldChars['chanyi']['preg'] == 3", "images/characters/chanyi/preg/dress_3.webp",
    "worldChars['chanyi']['preg'] == 4", "images/characters/chanyi/preg/dress_4.webp",
)
