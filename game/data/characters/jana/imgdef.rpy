################### jana expressions #########
image jana angry =  Composite((570, 1319), (0, 0), "jana_body", (0, 0), "images/characters/jana/face/angry.webp")
image jana blush =  Composite((570, 1319), (0, 0), "jana_body", (0, 0), "images/characters/jana/face/blush.webp")
image jana cry =    Composite((570, 1319), (0, 0), "jana_body", (0, 0), "images/characters/jana/face/cry.webp")
image jana laugh =  Composite((570, 1319), (0, 0), "jana_body", (0, 0), "images/characters/jana/face/laugh.webp")
image jana sad =    Composite((570, 1319), (0, 0), "jana_body", (0, 0), "images/characters/jana/face/sad.webp")
image jana scared = Composite((570, 1319), (0, 0), "jana_body", (0, 0), "images/characters/jana/face/scared.webp")
image jana smile =  Composite((570, 1319), (0, 0), "jana_body", (0, 0), "images/characters/jana/face/smile.webp")
image jana smug =   Composite((570, 1319), (0, 0), "jana_body", (0, 0), "images/characters/jana/face/smug.webp")
image jana think =  Composite((570, 1319), (0, 0), "jana_body", (0, 0), "images/characters/jana/face/think.webp")
#####################################################
image jana = Composite((570, 1319), (0, 0), "jana_body")

image jana_body = ConditionSwitch(
    "worldChars['jana']['clothes'] == 'naked'", "jana_naked",
    "worldChars['jana']['clothes'] == 'dress'", "jana_lingerie",
    "True", "jana_normal",
)
image jana_normal = ConditionSwitch(
    "worldChars['jana']['preg'] == 0", "images/characters/jana/base_uniform.webp",
    "worldChars['jana']['preg'] == 1", "images/characters/jana/preg/uniform_preg1.webp",
    "worldChars['jana']['preg'] == 2", "images/characters/jana/preg/uniform_preg2.webp",
    "worldChars['jana']['preg'] == 3", "images/characters/jana/preg/uniform_preg3.webp",
    "worldChars['jana']['preg'] == 4", "images/characters/jana/base_uniform.webp")
image jana_naked = ConditionSwitch(
    "worldChars['jana']['preg'] == 0", "images/characters/jana/base_nude.webp",
    "worldChars['jana']['preg'] == 1", "images/characters/jana/preg/nude_preg1.webp",
    "worldChars['jana']['preg'] == 2", "images/characters/jana/preg/nude_preg2.webp",
    "worldChars['jana']['preg'] == 3", "images/characters/jana/preg/nude_preg3.webp",
    "worldChars['jana']['preg'] == 4", "images/characters/jana/base_nude.webp")
image jana_lingerie = ConditionSwitch(
    "worldChars['jana']['preg'] == 0", "images/characters/jana/base_dress.webp",
    "worldChars['jana']['preg'] == 1", "images/characters/jana/preg/dress_preg1.webp",
    "worldChars['jana']['preg'] == 2", "images/characters/jana/preg/dress_preg2.webp",
    "worldChars['jana']['preg'] == 3", "images/characters/jana/preg/dress_preg3.webp",
    "worldChars['jana']['preg'] == 4", "images/characters/jana/base_dress.webp")