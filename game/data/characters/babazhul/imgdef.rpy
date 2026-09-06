########## babazhul expressions #############
image babazhul talk = Composite(
    (1920, 1080),
    (0, 0),     "cg_nov_witch_cond",
    (0, 0),     "babazhul_talk_cond",
    (0, -1),    "babazhul_blink_cond")
#########################################

image babazhul_blink_cond = ConditionSwitch(
    "worldChars['babazhul']['lit'] == 'yes'", "babazhul_animblink_l",
    "worldChars['babazhul']['lit'] == 'no'",  "babazhul_animblink")

image babazhul_talk_cond = ConditionSwitch(
    "worldChars['babazhul']['lit'] == 'yes'", "babazhul_animtalk_l",
    "worldChars['babazhul']['lit'] == 'no'",  "babazhul_animtalk")

image cg_nov_witch_cond = ConditionSwitch(
    "worldChars['babazhul']['lit'] == 'yes'", "cg_nov_witch_glow",
    "worldChars['babazhul']['lit'] == 'no'",  "cg_nov_witch")

image babazhul = Composite(
    (1920, 1080),
    (0, 0), "cg_nov_witch_cond",
    (0, 0), "babazhul_blink_cond")

#animblink
image babazhul_animblink_l:
    Null()
    2.5
    "images/characters/babazhul/face/l_eyes_closed.webp"
    0.35
    repeat

#animblink
image babazhul_animblink:
    Null()
    2.5
    "images/characters/babazhul/face/eyes_closed.webp"
    0.35
    repeat

#animtalk
image babazhul_animtalk:
    Null()
    0.1
    "images/characters/babazhul/face/mouth_open1.webp"
    0.2
    "images/characters/babazhul/face/mouth_open2.webp"
    0.2
    "images/characters/babazhul/face/mouth_open1.webp"
    0.2
    Null()
    0.2
    "images/characters/babazhul/face/mouth_open1.webp"
    0.2
    Null()
    0.6
    "images/characters/babazhul/face/mouth_open1.webp"
    0.2
    "images/characters/babazhul/face/mouth_open2.webp"
    0.2
    "images/characters/babazhul/face/mouth_open1.webp"
    0.2
    Null()
    0.2
    "images/characters/babazhul/face/mouth_open1.webp"
    0.2
    Null()

#animtalk
image babazhul_animtalk_l:
    Null()
    0.1
    "images/characters/babazhul/face/l_mouth_open1.webp"
    0.2
    "images/characters/babazhul/face/l_mouth_open2.webp"
    0.2
    "images/characters/babazhul/face/l_mouth_open1.webp"
    0.2
    Null()
    0.2
    "images/characters/babazhul/face/l_mouth_open1.webp"
    0.2
    Null()
    0.6
    "images/characters/babazhul/face/l_mouth_open1.webp"
    0.2
    "images/characters/babazhul/face/l_mouth_open2.webp"
    0.2
    "images/characters/babazhul/face/l_mouth_open1.webp"
    0.2
    Null()
    0.2
    "images/characters/babazhul/face/l_mouth_open1.webp"
    0.2
    Null()
