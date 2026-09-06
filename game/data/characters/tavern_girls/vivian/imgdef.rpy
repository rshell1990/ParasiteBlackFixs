############### Vivian expressions ##############
image vivian angry = Composite((654, 1399), CHAR_OFFSET.VIVIAN, "vivian_body", CHAR_OFFSET.VIVIAN, "images/characters/vivian/face/angry.webp")
image vivian blush = Composite((654, 1399), CHAR_OFFSET.VIVIAN, "vivian_body", CHAR_OFFSET.VIVIAN, "images/characters/vivian/face/blush.webp")
image vivian cry   = Composite((654, 1399), CHAR_OFFSET.VIVIAN, "vivian_body", CHAR_OFFSET.VIVIAN, "images/characters/vivian/face/cry.webp")
image vivian sad   = Composite((654, 1399), CHAR_OFFSET.VIVIAN, "vivian_body", CHAR_OFFSET.VIVIAN, "images/characters/vivian/face/sad.webp")
image vivian scared= Composite((654, 1399), CHAR_OFFSET.VIVIAN, "vivian_body", CHAR_OFFSET.VIVIAN, "images/characters/vivian/face/scared.webp")
image vivian think = Composite((654, 1399), CHAR_OFFSET.VIVIAN, "vivian_body", CHAR_OFFSET.VIVIAN, "images/characters/vivian/face/think.webp")
image vivian happy = Composite((654, 1399), CHAR_OFFSET.VIVIAN, "vivian_body", CHAR_OFFSET.VIVIAN, "images/characters/vivian/face/happy.webp")
image vivian smile = "vivian happy"
image vivian shock = Composite((654, 1399), CHAR_OFFSET.VIVIAN, "vivian_body", CHAR_OFFSET.VIVIAN, "images/characters/vivian/face/shock.webp")
image vivian laugh = Composite((654, 1399), CHAR_OFFSET.VIVIAN, "vivian_body", CHAR_OFFSET.VIVIAN, "images/characters/vivian/face/laugh.webp")
image vivian lewd  = Composite((654, 1399), CHAR_OFFSET.VIVIAN, "vivian_body", CHAR_OFFSET.VIVIAN, "images/characters/vivian/face/lewd.webp")
image vivian talk  = "vivian happy"

#################################################
image vivian      = Composite((654, 1399), CHAR_OFFSET.VIVIAN, "vivian_body")
image vivian_body = ConditionSwitch(
    "worldChars['vivian']['clothes'] == 'naked'",  "vivian_naked",
    "worldChars['vivian']['clothes'] == 'ling'",   "vivian_ling",
    "worldChars['vivian']['clothes'] == 'normal_mug'","vivian_normal_mug",
    "True",  "vivian_normal")

image vivian_naked = ConditionSwitch(
    "worldChars['vivian']['preg'] == 0", "images/characters/vivian/naked.webp",
    "worldChars['vivian']['preg'] == 1", "images/characters/vivian/preg/naked_1.webp",
    "worldChars['vivian']['preg'] == 2", "images/characters/vivian/preg/naked_2.webp",
    "worldChars['vivian']['preg'] == 3", "images/characters/vivian/preg/naked_3.webp",
    "worldChars['vivian']['preg'] == 4", "images/characters/vivian/naked.webp")
image vivian_ling = ConditionSwitch(
    "worldChars['vivian']['preg'] == 0", "images/characters/vivian/ling.webp",
    "worldChars['vivian']['preg'] == 1", "images/characters/vivian/preg/naked_1.webp",
    "worldChars['vivian']['preg'] == 2", "images/characters/vivian/preg/naked_2.webp",
    "worldChars['vivian']['preg'] == 3", "images/characters/vivian/preg/naked_3.webp",
    "worldChars['vivian']['preg'] == 4", "images/characters/vivian/ling.webp")
image vivian_normal_mug = ConditionSwitch(
    "worldChars['vivian']['preg'] == 0", "images/characters/vivian/normal_mug.webp",
    "worldChars['vivian']['preg'] == 1", "images/characters/vivian/preg/normal_mug_1.webp",
    "worldChars['vivian']['preg'] == 2", "images/characters/vivian/preg/normal_mug_2.webp",
    "worldChars['vivian']['preg'] == 3", "images/characters/vivian/preg/normal_mug_3.webp",
    "worldChars['vivian']['preg'] == 4", "images/characters/vivian/normal_mug.webp")
image vivian_normal = ConditionSwitch(
    "worldChars['vivian']['preg'] == 0", "images/characters/vivian/normal.webp",
    "worldChars['vivian']['preg'] == 1", "images/characters/vivian/preg/normal_1.webp",
    "worldChars['vivian']['preg'] == 2", "images/characters/vivian/preg/normal_2.webp",
    "worldChars['vivian']['preg'] == 3", "images/characters/vivian/preg/normal_3.webp",
    "worldChars['vivian']['preg'] == 4", "images/characters/vivian/preg/normal_4.webp")