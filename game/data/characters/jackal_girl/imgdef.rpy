################### jackal girl expressions #########
image jackal_girl angry = Composite((667, 1390), CHAR_OFFSET.JACKAL_GIRL, "jackal_girl_body", CHAR_OFFSET.JACKAL_GIRL, "images/characters/jackal_girl/face/angry.webp")
image jackal_girl blush = Composite((667, 1390), CHAR_OFFSET.JACKAL_GIRL, "jackal_girl_body", CHAR_OFFSET.JACKAL_GIRL, "images/characters/jackal_girl/face/blush.webp")
image jackal_girl cry   = Composite((667, 1390), CHAR_OFFSET.JACKAL_GIRL, "jackal_girl_body", CHAR_OFFSET.JACKAL_GIRL, "images/characters/jackal_girl/face/cry.webp")
image jackal_girl happy = Composite((667, 1390), CHAR_OFFSET.JACKAL_GIRL, "jackal_girl_body", CHAR_OFFSET.JACKAL_GIRL, "images/characters/jackal_girl/face/happy.webp")
image jackal_girl laugh = Composite((667, 1390), CHAR_OFFSET.JACKAL_GIRL, "jackal_girl_body", CHAR_OFFSET.JACKAL_GIRL, "images/characters/jackal_girl/face/laugh.webp")
image jackal_girl lewd  = Composite((667, 1390), CHAR_OFFSET.JACKAL_GIRL, "jackal_girl_body", CHAR_OFFSET.JACKAL_GIRL, "images/characters/jackal_girl/face/lewd.webp")
image jackal_girl sad   = Composite((667, 1390), CHAR_OFFSET.JACKAL_GIRL, "jackal_girl_body", CHAR_OFFSET.JACKAL_GIRL, "images/characters/jackal_girl/face/sad.webp")
image jackal_girl scared= Composite((667, 1390), CHAR_OFFSET.JACKAL_GIRL, "jackal_girl_body", CHAR_OFFSET.JACKAL_GIRL, "images/characters/jackal_girl/face/scared.webp")
image jackal_girl surp  = Composite((667, 1390), CHAR_OFFSET.JACKAL_GIRL, "jackal_girl_body", CHAR_OFFSET.JACKAL_GIRL, "images/characters/jackal_girl/face/surp.webp")
image jackal_girl think = Composite((667, 1390), CHAR_OFFSET.JACKAL_GIRL, "jackal_girl_body", CHAR_OFFSET.JACKAL_GIRL, "images/characters/jackal_girl/face/think.webp")
image jackal_girl talk = "jackal_girl"
#####################################################
image jackal_girl = Composite((667, 1390), CHAR_OFFSET.JACKAL_GIRL, "jackal_girl_body")

image jackal_girl_body = ConditionSwitch(
    "worldChars['jackal_girl']['clothes'] == 'naked'",  "jackal_girl_body_naked",
    "True", "jackal_girl_body_normal",
)

image jackal_girl_body_naked = ConditionSwitch(
    "worldChars['jackal_girl']['preg'] == 0", "images/characters/jackal_girl/naked.webp",
    "worldChars['jackal_girl']['preg'] == 1", "images/characters/jackal_girl/preg/naked_1.webp",
    "worldChars['jackal_girl']['preg'] == 2", "images/characters/jackal_girl/preg/naked_2.webp",
    "worldChars['jackal_girl']['preg'] == 3", "images/characters/jackal_girl/preg/naked_3.webp",
    "worldChars['jackal_girl']['preg'] == 4", "images/characters/jackal_girl/naked.webp")

image jackal_girl_body_normal  = ConditionSwitch(
    "worldChars['jackal_girl']['preg'] == 0", "images/characters/jackal_girl/normal.webp",
    "worldChars['jackal_girl']['preg'] == 1", "images/characters/jackal_girl/preg/normal_1.webp",
    "worldChars['jackal_girl']['preg'] == 2", "images/characters/jackal_girl/preg/normal_2.webp",
    "worldChars['jackal_girl']['preg'] == 3", "images/characters/jackal_girl/preg/normal_3.webp",
    "worldChars['jackal_girl']['preg'] == 4", "images/characters/jackal_girl/normal.webp")
