################# regina expressions #########
image regina angry      = Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_face_angry",    (0, 0), "regina_hood")
image regina angry_talk = "regina angry"
image regina fury       = Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_face_fury",     (0, 0), "regina_hood")
image regina happy      = Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_face_happy",    (0, 0), "regina_hood")
image regina smile      = "regina happy"
image regina smile_talk = "regina happy"
image regina laugh      = Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_face_laugh",    (0, 0), "regina_hood")
image regina lewd       = Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_face_lewd",     (0, 0), "regina_hood")
image regina lewd_talk  = "regina lewd"
image regina purple_eyes= Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_face_purple_eyes", (0, 0), "regina_hood")
image regina sad        = Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_face_sad",      (0, 0), "regina_hood")
image regina sad_talk   = "regina sad"
image regina scared     = Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_face_scared",   (0, 0), "regina_hood")
image regina shock      = Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_face_shock",    (0, 0), "regina_hood")
image regina shock_talk = "regina shock"
image regina shy        = Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_face_shy",      (0, 0), "regina_hood")
image regina shy_talk   = "regina shy"
image regina think      = Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_face_think",    (0, 0), "regina_hood")
image regina talk       = "regina"
###############################################
image regina = Composite((654, 1400), (0, 0), "regina_body", (0, 0), "regina_hood")
image regina_body = ConditionSwitch(
        "worldChars['regina']['clothes']=='naked'",     "images/characters/regina/naked.webp",
        "worldChars['regina']['clothes']=='towel'",     "images/characters/regina/towel.webp",
        "worldChars['regina']['clothes']=='robe'",      "images/characters/regina/robe.webp",
        "worldChars['regina']['clothes']=='witch'",     "images/characters/regina/witch.webp",
        "True",    "images/characters/regina/normal.webp",
)
image regina_face_angry = "images/characters/regina/face/angry.webp"
image regina_face_fury  = "images/characters/regina/face/fury.webp"
image regina_face_happy = "images/characters/regina/face/happy.webp"
image regina_face_laugh = "images/characters/regina/face/laugh.webp"
image regina_face_lewd  = "images/characters/regina/face/lewd.webp"
image regina_face_purple_eyes = "images/characters/regina/face/purple_eyes.webp"
image regina_face_sad   = "images/characters/regina/face/sad.webp"
image regina_face_scared= "images/characters/regina/face/scared.webp"
image regina_face_shock = "images/characters/regina/face/shock.webp"
image regina_face_shy   = "images/characters/regina/face/shy.webp"
image regina_face_think = "images/characters/regina/face/think.webp"

image regina_hood = ConditionSwitch(
        "worldChars['regina']['clothes'] == 'robe' and worldChars['regina']['hood'] == True", "images/characters/regina/hood.webp",
        "True", Null())