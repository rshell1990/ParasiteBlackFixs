################ fawha expressions ###############
image fawha angry =     Composite((650, 1288), CHAR_OFFSET.FAWHA, "fawha_body", CHAR_OFFSET.FAWHA, "images/characters/fawha/face/face_angry.webp",  CHAR_OFFSET.FAWHA, "fawha_mask")
image fawha lewd =      Composite((650, 1288), CHAR_OFFSET.FAWHA, "fawha_body", CHAR_OFFSET.FAWHA, "images/characters/fawha/face/face_lewd.webp",   CHAR_OFFSET.FAWHA, "fawha_mask")
image fawha sad =       Composite((650, 1288), CHAR_OFFSET.FAWHA, "fawha_body", CHAR_OFFSET.FAWHA, "images/characters/fawha/face/face_sad.webp",    CHAR_OFFSET.FAWHA, "fawha_mask")
image fawha sad2 =      Composite((650, 1288), CHAR_OFFSET.FAWHA, "fawha_body", CHAR_OFFSET.FAWHA, "images/characters/fawha/face/face_angry.webp",  CHAR_OFFSET.FAWHA, "fawha_mask")
image fawha smile =     Composite((650, 1288), CHAR_OFFSET.FAWHA, "fawha_body", CHAR_OFFSET.FAWHA, "images/characters/fawha/face/face_smile.webp",  CHAR_OFFSET.FAWHA, "fawha_mask")
image fawha smile2 =    Composite((650, 1288), CHAR_OFFSET.FAWHA, "fawha_body", CHAR_OFFSET.FAWHA, "images/characters/fawha/face/face_smile2.webp", CHAR_OFFSET.FAWHA, "fawha_mask")
image fawha something = Composite((650, 1288), CHAR_OFFSET.FAWHA, "fawha_body", CHAR_OFFSET.FAWHA, "images/characters/fawha/face/face_something.webp", CHAR_OFFSET.FAWHA, "fawha_mask")
image fawha talk =      Composite((650, 1288), CHAR_OFFSET.FAWHA, "fawha_body", CHAR_OFFSET.FAWHA, "fawha_animtalk", CHAR_OFFSET.FAWHA, "fawha_mask")
##################################################
# layers as body -> face -> mask 
image fawha = Composite((650, 1288), CHAR_OFFSET.FAWHA, "fawha_body", CHAR_OFFSET.FAWHA, "fawha_animblink", CHAR_OFFSET.FAWHA, "fawha_mask")
image fawha_body = ConditionSwitch(
    "worldChars['fawha']['clothes'] == 'naked'",  "images/characters/fawha/naked.webp",
    "worldChars['fawha']['clothes'] == 'topl'",   "images/characters/fawha/topless.webp",
    "worldChars['fawha']['clothes'] == 'topl_d'", "images/characters/fawha/topless_drinks.webp",
    "True", "images/characters/fawha/base.webp",
)
image fawha_mask = ConditionSwitch("worldChars['fawha']['mask'] == True", "images/characters/fawha/face/face_mask.webp", "True", Null())

# stubs
image fawha_animblink:
    Null()
image fawha_animtalk:
    Null()
