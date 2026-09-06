################# serafina expressions #########
image serafina angry  = Composite((382, 1420), CHAR_OFFSET.SERAFINA, "serafina_body", CHAR_OFFSET.SERAFINA, "images/characters/serafina/face/angry.webp", CHAR_OFFSET.SERAFINA, "serafina_hat")
image serafina embar  = Composite((382, 1420), CHAR_OFFSET.SERAFINA, "serafina_body", CHAR_OFFSET.SERAFINA, "images/characters/serafina/face/embar.webp", CHAR_OFFSET.SERAFINA, "serafina_hat")
image serafina happy  = Composite((382, 1420), CHAR_OFFSET.SERAFINA, "serafina_body", CHAR_OFFSET.SERAFINA, "images/characters/serafina/face/happy.webp", CHAR_OFFSET.SERAFINA, "serafina_hat")
image serafina laugh  = Composite((382, 1420), CHAR_OFFSET.SERAFINA, "serafina_body", CHAR_OFFSET.SERAFINA, "images/characters/serafina/face/laugh.webp", CHAR_OFFSET.SERAFINA, "serafina_hat")
image serafina smile  = "serafina laugh"
image serafina lewd   = Composite((382, 1420), CHAR_OFFSET.SERAFINA, "serafina_body", CHAR_OFFSET.SERAFINA, "images/characters/serafina/face/lewd.webp",  CHAR_OFFSET.SERAFINA, "serafina_hat")
image serafina sad    = Composite((382, 1420), CHAR_OFFSET.SERAFINA, "serafina_body", CHAR_OFFSET.SERAFINA, "images/characters/serafina/face/sad.webp",   CHAR_OFFSET.SERAFINA, "serafina_hat")
image serafina scared = Composite((382, 1420), CHAR_OFFSET.SERAFINA, "serafina_body", CHAR_OFFSET.SERAFINA, "images/characters/serafina/face/scared.webp",CHAR_OFFSET.SERAFINA, "serafina_hat")
image serafina shock  = "serafina scared"
image serafina surpr  = Composite((382, 1420), CHAR_OFFSET.SERAFINA, "serafina_body", CHAR_OFFSET.SERAFINA, "images/characters/serafina/face/surpr.webp", CHAR_OFFSET.SERAFINA, "serafina_hat")
image serafina surprised  = "serafina surpr"
image serafina think  = Composite((382, 1420), CHAR_OFFSET.SERAFINA, "serafina_body", CHAR_OFFSET.SERAFINA, "images/characters/serafina/face/think.webp", CHAR_OFFSET.SERAFINA, "serafina_hat")
image serafina talk   = "serafina"
image serafina        = Composite((382, 1420), CHAR_OFFSET.SERAFINA, "serafina_body", CHAR_OFFSET.SERAFINA, "serafina_hat")

###############################################

image serafina_body   = ConditionSwitch(
    "worldChars['serafina']['clothes'] == 'naked'", "serafina_naked",
    "worldChars['serafina']['clothes'] == 'mage'",  "serafina_mage",
    "worldChars['serafina']['clothes'] == 'inq'",   "serafina_inq",
    "True", "serafina_normal"
)

image serafina_normal = ConditionSwitch(
    "worldChars['serafina']['preg'] == 0", "images/characters/serafina/normal.webp",
    "worldChars['serafina']['preg'] == 1", "images/characters/serafina/preg/normal_1.webp",
    "worldChars['serafina']['preg'] == 2", "images/characters/serafina/preg/normal_2.webp",
    "worldChars['serafina']['preg'] == 3", "images/characters/serafina/preg/normal_3.webp",
    "worldChars['serafina']['preg'] == 4", "images/characters/serafina/normal.webp"
)
image serafina_naked  = ConditionSwitch(
    "worldChars['serafina']['preg'] == 0", "images/characters/serafina/naked.webp",
    "worldChars['serafina']['preg'] == 1", "images/characters/serafina/preg/naked_1.webp",
    "worldChars['serafina']['preg'] == 2", "images/characters/serafina/preg/naked_2.webp",
    "worldChars['serafina']['preg'] == 3", "images/characters/serafina/preg/naked_3.webp",
    "worldChars['serafina']['preg'] == 4", "images/characters/serafina/naked.webp"
)
image serafina_inq    = ConditionSwitch(
    "worldChars['serafina']['preg'] == 0", "images/characters/serafina/inq.webp",
    "worldChars['serafina']['preg'] == 1", "images/characters/serafina/preg/inq_1.webp",
    "worldChars['serafina']['preg'] == 2", "images/characters/serafina/preg/inq_2.webp",
    "worldChars['serafina']['preg'] == 3", "images/characters/serafina/preg/inq_3.webp",
    "worldChars['serafina']['preg'] == 4", "images/characters/serafina/inq.webp"
)
image serafina_mage   = ConditionSwitch(
    "worldChars['serafina']['preg'] == 0", "images/characters/serafina/mage.webp",
    "worldChars['serafina']['preg'] == 1", "images/characters/serafina/preg/mage_1.webp",
    "worldChars['serafina']['preg'] == 2", "images/characters/serafina/preg/mage_2.webp",
    "worldChars['serafina']['preg'] == 3", "images/characters/serafina/preg/mage_3.webp",
    "worldChars['serafina']['preg'] == 4", "images/characters/serafina/mage.webp"
)

# 2x nested condswitch dont fear the reaper
image serafina_hat = ConditionSwitch("worldChars['serafina']['clothes'] == 'inq'", ConditionSwitch("worldChars['serafina']['hat'] == True", "images/characters/serafina/hat.webp", "True", Null()), "True", Null())
