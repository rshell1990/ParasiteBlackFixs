############### lady bargore expressions ##############
image lady_bargore angry = Composite((567, 1400), CHAR_OFFSET.LADY_BARGORE, "lady_bargore_body", CHAR_OFFSET.LADY_BARGORE, "images/characters/lady_bargore/face/angry.webp")
image lady_bargore embar = Composite((567, 1400), CHAR_OFFSET.LADY_BARGORE, "lady_bargore_body", CHAR_OFFSET.LADY_BARGORE, "images/characters/lady_bargore/face/embar.webp")
image lady_bargore happy = Composite((567, 1400), CHAR_OFFSET.LADY_BARGORE, "lady_bargore_body", CHAR_OFFSET.LADY_BARGORE, "images/characters/lady_bargore/face/happy.webp")
image lady_bargore smile = "lady_bargore happy"
image lady_bargore blush = "lady_bargore happy"
image lady_bargore laugh = Composite((567, 1400), CHAR_OFFSET.LADY_BARGORE, "lady_bargore_body", CHAR_OFFSET.LADY_BARGORE, "images/characters/lady_bargore/face/laugh.webp")
image lady_bargore lewd  = Composite((567, 1400), CHAR_OFFSET.LADY_BARGORE, "lady_bargore_body", CHAR_OFFSET.LADY_BARGORE, "images/characters/lady_bargore/face/lewd.webp")
image lady_bargore sad   = Composite((567, 1400), CHAR_OFFSET.LADY_BARGORE, "lady_bargore_body", CHAR_OFFSET.LADY_BARGORE, "images/characters/lady_bargore/face/sad.webp")
image lady_bargore scared= Composite((567, 1400), CHAR_OFFSET.LADY_BARGORE, "lady_bargore_body", CHAR_OFFSET.LADY_BARGORE, "images/characters/lady_bargore/face/scared.webp")
image lady_bargore surp  = Composite((567, 1400), CHAR_OFFSET.LADY_BARGORE, "lady_bargore_body", CHAR_OFFSET.LADY_BARGORE, "images/characters/lady_bargore/face/surp.webp")
image lady_bargore shock = "lady_bargore surp"
image lady_bargore think = Composite((567, 1400), CHAR_OFFSET.LADY_BARGORE, "lady_bargore_body", CHAR_OFFSET.LADY_BARGORE, "images/characters/lady_bargore/face/think.webp")
image lady_bargore talk  = "lady_bargore"
#################################################
image lady_bargore = Composite((567, 1400), CHAR_OFFSET.LADY_BARGORE, "lady_bargore_body")

image lady_bargore_body = ConditionSwitch(
    "worldChars['lady_bargore']['clothes'] == 'naked'", "lady_bargore_naked",
    "True",  "lady_bargore_normal",
)
image lady_bargore_normal = ConditionSwitch(
        "worldChars['lady_belamore']['preg'] == 0", "images/characters/lady_bargore/normal.webp",
        "worldChars['lady_belamore']['preg'] == 1", "images/characters/lady_bargore/preg/normal1.webp",
        "worldChars['lady_belamore']['preg'] == 2", "images/characters/lady_bargore/preg/normal2.webp",
        "worldChars['lady_belamore']['preg'] == 3", "images/characters/lady_bargore/preg/normal3.webp",
        "worldChars['lady_belamore']['preg'] == 4", "images/characters/lady_bargore/preg/normal4.webp")
image lady_bargore_naked = ConditionSwitch(
        "worldChars['lady_belamore']['preg'] == 0", "images/characters/lady_bargore/naked.webp",
        "worldChars['lady_belamore']['preg'] == 1", "images/characters/lady_bargore/preg/naked1.webp",
        "worldChars['lady_belamore']['preg'] == 2", "images/characters/lady_bargore/preg/naked2.webp",
        "worldChars['lady_belamore']['preg'] == 3", "images/characters/lady_bargore/preg/naked3.webp",
        "worldChars['lady_belamore']['preg'] == 4", "images/characters/lady_bargore/naked.webp")