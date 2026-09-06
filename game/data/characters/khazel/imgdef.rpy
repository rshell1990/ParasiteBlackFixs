############## khazel expressions ################
image khazel talk   = Composite((834, 1400), CHAR_OFFSET.KHAZEL, "khazel_body", CHAR_OFFSET.KHAZEL, "khazel_animtalk")
image khazel angry  = Composite((834, 1400), CHAR_OFFSET.KHAZEL, "khazel_body", CHAR_OFFSET.KHAZEL, "images/characters/khazel/face/angry.webp")
image khazel blush  = Composite((834, 1400), CHAR_OFFSET.KHAZEL, "khazel_body", CHAR_OFFSET.KHAZEL, "images/characters/khazel/face/blush.webp")
image khazel fury   = Composite((834, 1400), CHAR_OFFSET.KHAZEL, "khazel_body", CHAR_OFFSET.KHAZEL, "images/characters/khazel/face/fury.webp")
image khazel happy  = Composite((834, 1400), CHAR_OFFSET.KHAZEL, "khazel_body", CHAR_OFFSET.KHAZEL, "images/characters/khazel/face/happy.webp")
image khazel laugh  = Composite((834, 1400), CHAR_OFFSET.KHAZEL, "khazel_body", CHAR_OFFSET.KHAZEL, "images/characters/khazel/face/laugh.webp")
image khazel sad    = Composite((834, 1400), CHAR_OFFSET.KHAZEL, "khazel_body", CHAR_OFFSET.KHAZEL, "images/characters/khazel/face/sad.webp")
image khazel shock  = Composite((834, 1400), CHAR_OFFSET.KHAZEL, "khazel_body", CHAR_OFFSET.KHAZEL, "images/characters/khazel/face/shock.webp")
image khazel think  = Composite((834, 1400), CHAR_OFFSET.KHAZEL, "khazel_body", CHAR_OFFSET.KHAZEL, "images/characters/khazel/face/think.webp")
#################################################
image khazel = Composite((834, 1400), CHAR_OFFSET.KHAZEL, "khazel_body")

image khazel_body = ConditionSwitch(
    "True", "images/characters/khazel/normal.webp",
)

image khazel_animtalk:
    Null()