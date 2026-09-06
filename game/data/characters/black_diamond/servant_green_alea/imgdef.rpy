############### alea expressions ###############
image alea grump =  Composite((650, 1288), CHAR_OFFSET.ALEA, "alea_body", CHAR_OFFSET.ALEA, "images/characters/alea/face/face_grump.webp", CHAR_OFFSET.ALEA, "alea_mask")
image alea huh =    Composite((650, 1288), CHAR_OFFSET.ALEA, "alea_body", CHAR_OFFSET.ALEA, "images/characters/alea/face/face_huh.webp",   CHAR_OFFSET.ALEA, "alea_mask")
image alea lewd =   Composite((650, 1288), CHAR_OFFSET.ALEA, "alea_body", CHAR_OFFSET.ALEA, "images/characters/alea/face/face_lewd.webp",  CHAR_OFFSET.ALEA, "alea_mask")
image alea sad =    Composite((650, 1288), CHAR_OFFSET.ALEA, "alea_body", CHAR_OFFSET.ALEA, "images/characters/alea/face/face_sad.webp",   CHAR_OFFSET.ALEA, "alea_mask")
image alea shock =  Composite((650, 1288), CHAR_OFFSET.ALEA, "alea_body", CHAR_OFFSET.ALEA, "images/characters/alea/face/face_shock.webp", CHAR_OFFSET.ALEA, "alea_mask")
image alea smile =  Composite((650, 1288), CHAR_OFFSET.ALEA, "alea_body", CHAR_OFFSET.ALEA, "images/characters/alea/face/face_smile.webp", CHAR_OFFSET.ALEA, "alea_mask")
image alea smile2 = Composite((650, 1288), CHAR_OFFSET.ALEA, "alea_body", CHAR_OFFSET.ALEA, "images/characters/alea/face/face_smile2.webp",CHAR_OFFSET.ALEA, "alea_mask")
image alea talk =   Composite((650, 1288), CHAR_OFFSET.ALEA, "alea_body", CHAR_OFFSET.ALEA, "alea_animtalk", CHAR_OFFSET.ALEA, "alea_mask")
################################################
# layers as body -> face -> mask 
image alea = Composite((650, 1288), CHAR_OFFSET.ALEA, "alea_body", CHAR_OFFSET.ALEA, "alea_animblink", CHAR_OFFSET.ALEA, "alea_mask")
image alea_body = ConditionSwitch(
    "worldChars['alea']['clothes'] == 'naked'",  "images/characters/alea/naked.webp",
    "worldChars['alea']['clothes'] == 'topl'",   "images/characters/alea/topless.webp",
    "worldChars['alea']['clothes'] == 'topl_d'", "images/characters/alea/topless_drinks.webp",
    "True", "images/characters/alea/base.webp",
)

image alea_mask = ConditionSwitch("worldChars['alea']['mask'] == True", "images/characters/alea/face/face_mask.webp", "True", Null())

# stubs
image alea_animblink:
    Null()
image alea_animtalk:
    Null()
