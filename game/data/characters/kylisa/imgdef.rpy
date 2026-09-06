################# kylisa expressions ##############
image kylisa talk   = Composite((695, 1400), (0, 0), "kylisa_body", (0, 0), "kylisa_animtalk", (0, 0), "kylisa_hood")
image kylisa angry  = Composite((695, 1400), (0, 0), "kylisa_body", (0, 0), "images/characters/kylisa/face/angry.webp", (0, 0), "kylisa_hood")
image kylisa blush  = Composite((695, 1400), (0, 0), "kylisa_body", (0, 0), "images/characters/kylisa/face/blush.webp", (0, 0), "kylisa_hood")
image kylisa happy  = Composite((695, 1400), (0, 0), "kylisa_body", (0, 0), "images/characters/kylisa/face/happy.webp", (0, 0), "kylisa_hood")
image kylisa sad    = Composite((695, 1400), (0, 0), "kylisa_body", (0, 0), "images/characters/kylisa/face/sad.webp",   (0, 0), "kylisa_hood")
image kylisa scared = Composite((695, 1400), (0, 0), "kylisa_body", (0, 0), "images/characters/kylisa/face/scared.webp",(0, 0), "kylisa_hood")
image kylisa smile  = Composite((695, 1400), (0, 0), "kylisa_body", (0, 0), "images/characters/kylisa/face/smile.webp", (0, 0), "kylisa_hood")
image kylisa think  = Composite((695, 1400), (0, 0), "kylisa_body", (0, 0), "images/characters/kylisa/face/think.webp", (0, 0), "kylisa_hood")
#####################################################
image kylisa = Composite((695, 1400), (0, 0), "kylisa_body", (0, 0), "kylisa_hood")
image kylisa_body = ConditionSwitch(
    "worldChars['kylisa']['clothes'] == 'normal_nostaff'", "images/characters/kylisa/base_nostaff.webp",
    "worldChars['kylisa']['clothes'] == 'naked'",   "images/characters/kylisa/base_naked.webp",
    "worldChars['kylisa']['clothes'] == 'ling'",    "images/characters/kylisa/base_ling.webp",
    "True",  "images/characters/kylisa/base_staff.webp",
)

image kylisa_hood = ConditionSwitch(
    "worldChars['kylisa']['hood'] == False", Null(),
    "worldChars['kylisa']['hood'] == True",  "images/characters/kylisa/face/hood.webp"
)

#animblink
image kylisa_animblink:
    Null()

#animtalk
image kylisa_animtalk:
    Null()
