################# rania expressions #########
image rania angry   = Composite((596, 1399), CHAR_OFFSET.RANIA, "rania_body", CHAR_OFFSET.RANIA, "images/characters/rania/face/angry.webp")
image rania blush   = Composite((596, 1399), CHAR_OFFSET.RANIA, "rania_body", CHAR_OFFSET.RANIA, "images/characters/rania/face/blush.webp")
image rania cry     = Composite((596, 1399), CHAR_OFFSET.RANIA, "rania_body", CHAR_OFFSET.RANIA, "images/characters/rania/face/cry.webp")
image rania happy   = Composite((596, 1399), CHAR_OFFSET.RANIA, "rania_body", CHAR_OFFSET.RANIA, "images/characters/rania/face/happy.webp")
image rania smile   = "rania happy"
image rania laugh   = Composite((596, 1399), CHAR_OFFSET.RANIA, "rania_body", CHAR_OFFSET.RANIA, "images/characters/rania/face/laugh.webp")
image rania sad     = Composite((596, 1399), CHAR_OFFSET.RANIA, "rania_body", CHAR_OFFSET.RANIA, "images/characters/rania/face/sad.webp")
image rania scared  = Composite((596, 1399), CHAR_OFFSET.RANIA, "rania_body", CHAR_OFFSET.RANIA, "images/characters/rania/face/scared.webp")
image rania shock   = Composite((596, 1399), CHAR_OFFSET.RANIA, "rania_body", CHAR_OFFSET.RANIA, "images/characters/rania/face/shock.webp")
image rania smug    = Composite((596, 1399), CHAR_OFFSET.RANIA, "rania_body", CHAR_OFFSET.RANIA, "images/characters/rania/face/smug.webp")
image rania think   = Composite((596, 1399), CHAR_OFFSET.RANIA, "rania_body", CHAR_OFFSET.RANIA, "images/characters/rania/face/think.webp")
image rania talk    = "rania"
###############################################
image rania = Composite((596, 1399), CHAR_OFFSET.RANIA, "rania_body")

image rania_body = ConditionSwitch(
    "True", "images/characters/rania/normal.webp")
