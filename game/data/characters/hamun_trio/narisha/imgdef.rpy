############### lady narisha expressions ##############
image lady_narisha angry = Composite((504, 1400), CHAR_OFFSET.LADY_NARISHA, "lady_narisha_body", CHAR_OFFSET.LADY_NARISHA, "images/characters/lady_narisha/face/angry.webp")
image lady_narisha embar = Composite((504, 1400), CHAR_OFFSET.LADY_NARISHA, "lady_narisha_body", CHAR_OFFSET.LADY_NARISHA, "images/characters/lady_narisha/face/embar.webp")
image lady_narisha happy = Composite((504, 1400), CHAR_OFFSET.LADY_NARISHA, "lady_narisha_body", CHAR_OFFSET.LADY_NARISHA, "images/characters/lady_narisha/face/happy.webp")
image lady_narisha smile = "lady_narisha happy"
image lady_narisha laugh = Composite((504, 1400), CHAR_OFFSET.LADY_NARISHA, "lady_narisha_body", CHAR_OFFSET.LADY_NARISHA, "images/characters/lady_narisha/face/laugh.webp")
image lady_narisha lewd  = Composite((504, 1400), CHAR_OFFSET.LADY_NARISHA, "lady_narisha_body", CHAR_OFFSET.LADY_NARISHA, "images/characters/lady_narisha/face/lewd.webp")
image lady_narisha sad   = Composite((504, 1400), CHAR_OFFSET.LADY_NARISHA, "lady_narisha_body", CHAR_OFFSET.LADY_NARISHA, "images/characters/lady_narisha/face/sad.webp")
image lady_narisha scared= Composite((504, 1400), CHAR_OFFSET.LADY_NARISHA, "lady_narisha_body", CHAR_OFFSET.LADY_NARISHA, "images/characters/lady_narisha/face/scared.webp")
image lady_narisha surp  = Composite((504, 1400), CHAR_OFFSET.LADY_NARISHA, "lady_narisha_body", CHAR_OFFSET.LADY_NARISHA, "images/characters/lady_narisha/face/surp.webp")
image lady_narisha shock = "lady_narisha surp"
image lady_narisha think = Composite((504, 1400), CHAR_OFFSET.LADY_NARISHA, "lady_narisha_body", CHAR_OFFSET.LADY_NARISHA, "images/characters/lady_narisha/face/think.webp")
image lady_narisha talk  = "lady_narisha"
#################################################
image lady_narisha = Composite((504, 1400), CHAR_OFFSET.LADY_NARISHA, "lady_narisha_body")

image lady_narisha_body = ConditionSwitch(
    "worldChars['lady_narisha']['clothes'] == 'naked'", "lady_narisha_naked",
    "True",  "lady_narisha_normal",
)
image lady_narisha_normal = ConditionSwitch(
        "worldChars['lady_belamore']['preg'] == 0", "images/characters/lady_narisha/normal.webp",
        "worldChars['lady_belamore']['preg'] == 1", "images/characters/lady_narisha/preg/normal1.webp",
        "worldChars['lady_belamore']['preg'] == 2", "images/characters/lady_narisha/preg/normal2.webp",
        "worldChars['lady_belamore']['preg'] == 3", "images/characters/lady_narisha/preg/normal3.webp",
        "worldChars['lady_belamore']['preg'] == 4", "images/characters/lady_narisha/preg/normal4.webp")
image lady_narisha_naked = ConditionSwitch(
        "worldChars['lady_belamore']['preg'] == 0", "images/characters/lady_narisha/naked.webp",
        "worldChars['lady_belamore']['preg'] == 1", "images/characters/lady_narisha/preg/naked1.webp",
        "worldChars['lady_belamore']['preg'] == 2", "images/characters/lady_narisha/preg/naked2.webp",
        "worldChars['lady_belamore']['preg'] == 3", "images/characters/lady_narisha/preg/naked3.webp",
        "worldChars['lady_belamore']['preg'] == 4", "images/characters/lady_narisha/naked.webp")