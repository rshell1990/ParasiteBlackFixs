############### alysha expressions ##############
image alysha talk =     Composite((450, 1216), (0, 0), "alysha_body", CHAR_OFFSET.ALYSHA, "alysha_animtalk")
image alysha crying =   Composite((450, 1216), (0, 0), "alysha_body", CHAR_OFFSET.ALYSHA, ConditionSwitch("worldChars['alysha']['clothes'] == 'slave'", "images/characters/alysha/face/slave_crying.webp", "True", "images/characters/alysha/face/free_crying.webp"))
image alysha sad =      Composite((450, 1216), (0, 0), "alysha_body", CHAR_OFFSET.ALYSHA, "images/characters/alysha/face/slave_sad.webp")
image alysha shock =    Composite((450, 1216), (0, 0), "alysha_body", CHAR_OFFSET.ALYSHA, ConditionSwitch("worldChars['alysha']['clothes'] == 'slave'", "images/characters/alysha/face/slave_shock.webp", "True", "images/characters/alysha/face/free_shock.webp"))
image alysha smile =    Composite((450, 1216), (0, 0), "alysha_body", CHAR_OFFSET.ALYSHA, "images/characters/alysha/face/free_smile.webp")
##############################################

image alysha:
    "alysha_body"

image alysha_body = Composite(
    (450, 1216),
    CHAR_OFFSET.ALYSHA, ConditionSwitch(
        "worldChars['alysha']['clothes'] == 'slave'", "images/characters/alysha/slave.webp",
        "True", "images/characters/alysha/free.webp")
)

image alysha_animtalk:
    Null()
image alysha_animblink:
    Null()

################## alysha warrior expressions ###############
image alysha_warrior angry =    Composite((505, 1270), (0, 0), "alysha_warrior_body", (0, 80), "images/characters/alysha/warrior/face/angry.webp")
image alysha_warrior cry =      Composite((505, 1270), (0, 0), "alysha_warrior_body", (0, 80), "images/characters/alysha/warrior/face/cry.webp")
image alysha_warrior laugh =    Composite((505, 1270), (0, 0), "alysha_warrior_body", (0, 80), "images/characters/alysha/warrior/face/laugh.webp")
image alysha_warrior lewd =     Composite((505, 1270), (0, 0), "alysha_warrior_body", (0, 80), "images/characters/alysha/warrior/face/lewd.webp")
image alysha_warrior sad =      Composite((505, 1270), (0, 0), "alysha_warrior_body", (0, 80), "images/characters/alysha/warrior/face/sad.webp")
image alysha_warrior scared =   Composite((505, 1270), (0, 0), "alysha_warrior_body", (0, 80), "images/characters/alysha/warrior/face/scared.webp")
image alysha_warrior shock =    Composite((505, 1270), (0, 0), "alysha_warrior_body", (0, 80), "images/characters/alysha/warrior/face/shock.webp")
image alysha_warrior smile =    Composite((505, 1270), (0, 0), "alysha_warrior_body", (0, 80), "images/characters/alysha/warrior/face/smile.webp")
image alysha_warrior think =    Composite((505, 1270), (0, 0), "alysha_warrior_body", (0, 80), "images/characters/alysha/warrior/face/think.webp")
image alysha_warrior talk =     "alysha_warrior"

image alysha_warrior:
    "alysha_warrior_body"

image alysha_warrior_body:
    "images/characters/alysha/warrior/normal.webp"
    yoffset 80

image cg_alysha_war_no_hand:
    "images/characters/alysha/warrior/cgs/cg_alysha_war_no_hand_base.webp"
    yoffset 80
image cg_alysha_war_no_hand2:
    "images/characters/alysha/warrior/cgs/cg_alysha_war_no_hand2_base.webp"
    yoffset 80