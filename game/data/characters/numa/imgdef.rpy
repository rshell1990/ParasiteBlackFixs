############### numa expressions ##########
image numa angry    = Composite((678, 1250), CHAR_OFFSET.NUMA, "numa_body", CHAR_OFFSET.NUMA, "images/characters/numa/face/angry.webp")
image numa blush    = Composite((678, 1250), CHAR_OFFSET.NUMA, "numa_body", CHAR_OFFSET.NUMA, "images/characters/numa/face/blush.webp")
image numa laugh    = Composite((678, 1250), CHAR_OFFSET.NUMA, "numa_body", CHAR_OFFSET.NUMA, "images/characters/numa/face/laugh.webp")
image numa sad      = Composite((678, 1250), CHAR_OFFSET.NUMA, "numa_body", CHAR_OFFSET.NUMA, "images/characters/numa/face/sad.webp")
image numa scared   = Composite((678, 1250), CHAR_OFFSET.NUMA, "numa_body", CHAR_OFFSET.NUMA, "images/characters/numa/face/scared.webp")
image numa shock    = Composite((678, 1250), CHAR_OFFSET.NUMA, "numa_body", CHAR_OFFSET.NUMA, "images/characters/numa/face/shock.webp")
image numa surprised = "numa shock"
image numa smile    = Composite((678, 1250), CHAR_OFFSET.NUMA, "numa_body", CHAR_OFFSET.NUMA, "images/characters/numa/face/smile.webp")
image numa think    = Composite((678, 1250), CHAR_OFFSET.NUMA, "numa_body", CHAR_OFFSET.NUMA, "images/characters/numa/face/think.webp")
image numa serious  = "numa think"
image numa talk     = "numa"
############################################
image numa = Composite((678, 1250), CHAR_OFFSET.NUMA, "numa_body")
image numa_body = ConditionSwitch(
    "worldChars['numa']['clothes'] == 'naked'", "images/characters/numa/naked.webp",
    "True", "images/characters/numa/normal.webp",
)