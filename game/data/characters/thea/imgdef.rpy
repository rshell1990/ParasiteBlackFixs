############## thea expressions ##############
image thea talk     = Composite((624, 1384), (0, 0), "thea_body", (0, 0), "thea_animtalk")
image thea angry    = Composite((624, 1384), (0, 0), "thea_body", (0, 0), "images/characters/thea/face/face_angry.webp")
image thea blush    = Composite((624, 1384), (0, 0), "thea_body", (0, 0), "images/characters/thea/face/face_blush.webp")
image thea disgust  = Composite((624, 1384), (0, 0), "thea_body", (0, 0), "images/characters/thea/face/face_disgust.webp")
image thea sad      = Composite((624, 1384), (0, 0), "thea_body", (0, 0), "images/characters/thea/face/face_sad.webp")
image thea smile    = Composite((624, 1384), (0, 0), "thea_body", (0, 0), "images/characters/thea/face/face_smile.webp")
image thea smile2   = Composite((624, 1384), (0, 0), "thea_body", (0, 0), "images/characters/thea/face/face_smile2.webp")
image thea scared   = Composite((624, 1384), (0, 0), "thea_body", (0, 0), "images/characters/thea/face/face_what.webp")
#################################################
image thea = Composite((624, 1384), (0, 0), "thea_body")
image thea_body = ConditionSwitch(
    "worldChars['thea']['clothes'] == 'naked'",  "images/characters/thea/naked.webp",
    "worldChars['thea']['clothes'] == 'ling'",   "images/characters/thea/ling.webp",
    "worldChars['thea']['clothes'] == 'gown'",   "images/characters/thea/gown.webp",
    "True", "images/characters/thea/base.webp",
)

image thea_animtalk:
    Null()
image thea_animblink:
    Null()
