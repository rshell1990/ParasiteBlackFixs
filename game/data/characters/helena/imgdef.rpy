################ helena expressions ##################
image helena talk =  Composite((500, 1148), (0, 0), "helena_body", (0, 0), "helena_animtalk")
image helena smile = Composite((500, 1148), (0, 0), "helena_body", (0, 0), "images/characters/helena/face/face_smile.webp")
image helena joy =   Composite((500, 1148), (0, 0), "helena_body", (0, 0), "images/characters/helena/face/face_joy.webp")
image helena angry = Composite((500, 1148), (0, 0), "helena_body", (0, 0), "images/characters/helena/face/face_angry.webp")
image helena lewd =  Composite((500, 1148), (0, 0), "helena_body", (0, 0), "images/characters/helena/face/face_lewd.webp")
image helena lewd2 = Composite((500, 1148), (0, 0), "helena_body", (0, 0), "images/characters/helena/face/face_lewd2.webp")
image helena sad =   Composite((500, 1148), (0, 0), "helena_body", (0, 0), "images/characters/helena/face/face_sad.webp")
image helena shock = Composite((500, 1148), (0, 0), "helena_body", (0, 0), "images/characters/helena/face/face_shock.webp")
#####################################################
image helena = Composite((500, 1148), (0, 0), "helena_body")

image helena_body = ConditionSwitch(
    "worldChars['helena']['clothes'] == 'ling'", "images/characters/helena/lingerie.webp",
    "worldChars['helena']['clothes'] == 'naked'", "images/characters/helena/naked.webp",
    "True", "images/characters/helena/base.webp",
)
# animblink
image helena_animblink:
    Null()

# animtalk
image helena_animtalk:
    Null()
