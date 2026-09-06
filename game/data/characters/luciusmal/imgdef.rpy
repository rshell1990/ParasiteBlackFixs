############ luciusmal expressions ##############
image luciusmal angry   = Composite((875, 1479), (0, 0), "luciusmal_body", (0, 0), "images/characters/luciusmal/face/angry.webp")
image luciusmal devious = Composite((875, 1479), (0, 0), "luciusmal_body", (0, 0), "images/characters/luciusmal/face/devious.webp")
image luciusmal laugh   = Composite((875, 1479), (0, 0), "luciusmal_body", (0, 0), "images/characters/luciusmal/face/laugh.webp")
image luciusmal sad     = Composite((875, 1479), (0, 0), "luciusmal_body", (0, 0), "images/characters/luciusmal/face/sad.webp")
image luciusmal scared  = Composite((875, 1479), (0, 0), "luciusmal_body", (0, 0), "images/characters/luciusmal/face/scared.webp")
image luciusmal smile   = Composite((875, 1479), (0, 0), "luciusmal_body", (0, 0), "images/characters/luciusmal/face/smile.webp")
image luciusmal think   = Composite((875, 1479), (0, 0), "luciusmal_body", (0, 0), "images/characters/luciusmal/face/think.webp")
image luciusmal talk = "luciusmal"
##################################################
image luciusmal = Composite((875, 1479), (0, 0), "luciusmal_body")
image luciusmal_body = ConditionSwitch(
    "worldChars['luciusmal']['pose'] == 'base_1'", "images/characters/luciusmal/base_1.webp",
    "worldChars['luciusmal']['pose'] == 'base_2'", "images/characters/luciusmal/base_2.webp")