############### lady belamore expressions ##############
image lady_belamore angry = Composite((491, 1400), CHAR_OFFSET.LADY_BELAMORE, "lady_belamore_body", CHAR_OFFSET.LADY_BELAMORE, "images/characters/lady_belamore/face/angry.webp")
image lady_belamore embar = Composite((491, 1400), CHAR_OFFSET.LADY_BELAMORE, "lady_belamore_body", CHAR_OFFSET.LADY_BELAMORE, "images/characters/lady_belamore/face/embar.webp")
image lady_belamore emb   = "lady_belamore embar"
image lady_belamore happy = Composite((491, 1400), CHAR_OFFSET.LADY_BELAMORE, "lady_belamore_body", CHAR_OFFSET.LADY_BELAMORE, "images/characters/lady_belamore/face/happy.webp")
image lady_belamore smile = "lady_belamore happy"
image lady_belamore laugh = Composite((491, 1400), CHAR_OFFSET.LADY_BELAMORE, "lady_belamore_body", CHAR_OFFSET.LADY_BELAMORE, "images/characters/lady_belamore/face/laugh.webp")
image lady_belamore lewd  = Composite((491, 1400), CHAR_OFFSET.LADY_BELAMORE, "lady_belamore_body", CHAR_OFFSET.LADY_BELAMORE, "images/characters/lady_belamore/face/lewd.webp")
image lady_belamore sad   = Composite((491, 1400), CHAR_OFFSET.LADY_BELAMORE, "lady_belamore_body", CHAR_OFFSET.LADY_BELAMORE, "images/characters/lady_belamore/face/sad.webp")
image lady_belamore scared= Composite((491, 1400), CHAR_OFFSET.LADY_BELAMORE, "lady_belamore_body", CHAR_OFFSET.LADY_BELAMORE, "images/characters/lady_belamore/face/scared.webp")
image lady_belamore surp  = Composite((491, 1400), CHAR_OFFSET.LADY_BELAMORE, "lady_belamore_body", CHAR_OFFSET.LADY_BELAMORE, "images/characters/lady_belamore/face/surp.webp")
image lady_belamore shock = "lady_belamore surp"
image lady_belamore think = Composite((491, 1400), CHAR_OFFSET.LADY_BELAMORE, "lady_belamore_body", CHAR_OFFSET.LADY_BELAMORE, "images/characters/lady_belamore/face/think.webp")
image lady_belamore serious = "lady_belamore think"
image lady_belamore talk  = "lady_belamore"
#################################################
image lady_belamore = Composite((491, 1400), CHAR_OFFSET.LADY_BELAMORE, "lady_belamore_body")

image lady_belamore_body = ConditionSwitch(
    "worldChars['lady_belamore']['clothes'] == 'naked'", "lady_belamore_naked",
    "True",  "lady_belamore_normal",
)
image lady_belamore_normal = ConditionSwitch(
        "worldChars['lady_belamore']['preg'] == 0", "images/characters/lady_belamore/normal.webp",
        "worldChars['lady_belamore']['preg'] == 1", "images/characters/lady_belamore/preg/normal1.webp",
        "worldChars['lady_belamore']['preg'] == 2", "images/characters/lady_belamore/preg/normal2.webp",
        "worldChars['lady_belamore']['preg'] == 3", "images/characters/lady_belamore/preg/normal3.webp",
        "worldChars['lady_belamore']['preg'] == 4", "images/characters/lady_belamore/preg/normal4.webp")
image lady_belamore_naked = ConditionSwitch(
        "worldChars['lady_belamore']['preg'] == 0", "images/characters/lady_belamore/naked.webp",
        "worldChars['lady_belamore']['preg'] == 1", "images/characters/lady_belamore/preg/naked1.webp",
        "worldChars['lady_belamore']['preg'] == 2", "images/characters/lady_belamore/preg/naked2.webp",
        "worldChars['lady_belamore']['preg'] == 3", "images/characters/lady_belamore/preg/naked3.webp",
        "worldChars['lady_belamore']['preg'] == 4", "images/characters/lady_belamore/naked.webp")