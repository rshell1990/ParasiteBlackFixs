################### mrs winward expressions #########
image mrs_winward angry = Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "images/characters/winward_mrs/face/angry.webp", CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
image mrs_winward blush = Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "images/characters/winward_mrs/face/blush.webp", CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
image mrs_winward cry   = Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "images/characters/winward_mrs/face/cry.webp",   CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
image mrs_winward embarr= Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "images/characters/winward_mrs/face/embarr.webp",CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
image mrs_winward happy = Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "images/characters/winward_mrs/face/happy.webp", CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
image mrs_winward laugh = Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "images/characters/winward_mrs/face/laugh.webp", CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
image mrs_winward lewd  = Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "images/characters/winward_mrs/face/lewd.webp",  CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
image mrs_winward sad   = Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "images/characters/winward_mrs/face/sad.webp",   CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
image mrs_winward scared= Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "images/characters/winward_mrs/face/scared.webp",CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
image mrs_winward shock = Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "images/characters/winward_mrs/face/shock.webp", CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
image mrs_winward think = Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "images/characters/winward_mrs/face/think.webp", CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
#####################################################
image mrs_winward = Composite((780, 1400), CHAR_OFFSET.MRS_WINWARD, "mrs_winward_body", CHAR_OFFSET.MRS_WINWARD, "mrs_winward_funeral_veil")
image mrs_winward_body = ConditionSwitch(
    "worldChars['mrs_winward']['clothes'] == 'naked'",  "mrs_winward_naked",
    "worldChars['mrs_winward']['clothes'] == 'cowl'",   "mrs_winward_cowl",
    "worldChars['mrs_winward']['clothes'] == 'funeral'","mrs_winward_funeral",
    "True", "mrs_winward_normal",
)
image mrs_winward_normal = ConditionSwitch(
    "worldChars['mrs_winward']['preg'] == 0", "images/characters/winward_mrs/normal.webp",
    "worldChars['mrs_winward']['preg'] == 1", "images/characters/winward_mrs/preg/normal_1.webp",
    "worldChars['mrs_winward']['preg'] == 2", "images/characters/winward_mrs/preg/normal_2.webp",
    "worldChars['mrs_winward']['preg'] == 3", "images/characters/winward_mrs/preg/normal_3.webp",
    "worldChars['mrs_winward']['preg'] == 4", "images/characters/winward_mrs/holding_baby.webp")
image mrs_winward_naked = ConditionSwitch(
    "worldChars['mrs_winward']['preg'] == 0", "images/characters/winward_mrs/naked.webp",
    "worldChars['mrs_winward']['preg'] == 1", "images/characters/winward_mrs/preg/naked_1.webp",
    "worldChars['mrs_winward']['preg'] == 2", "images/characters/winward_mrs/preg/naked_2.webp",
    "worldChars['mrs_winward']['preg'] == 3", "images/characters/winward_mrs/preg/naked_3.webp",
    "worldChars['mrs_winward']['preg'] == 4", "images/characters/winward_mrs/holding_baby.webp")
image mrs_winward_cowl = ConditionSwitch(
    "worldChars['mrs_winward']['preg'] == 0", "images/characters/winward_mrs/cowl.webp",
    "worldChars['mrs_winward']['preg'] == 1", "images/characters/winward_mrs/preg/cowl_1.webp",
    "worldChars['mrs_winward']['preg'] == 2", "images/characters/winward_mrs/preg/cowl_2.webp",
    "worldChars['mrs_winward']['preg'] == 3", "images/characters/winward_mrs/preg/cowl_3.webp",
    "worldChars['mrs_winward']['preg'] == 4", "images/characters/winward_mrs/holding_baby.webp")
image mrs_winward_funeral = ConditionSwitch(
    "worldChars['mrs_winward']['preg'] == 0", "images/characters/winward_mrs/funeral.webp",
    "worldChars['mrs_winward']['preg'] == 1", "images/characters/winward_mrs/funeral.webp",
    "worldChars['mrs_winward']['preg'] == 2", "images/characters/winward_mrs/funeral.webp",
    "worldChars['mrs_winward']['preg'] == 3", "images/characters/winward_mrs/funeral.webp",
    "worldChars['mrs_winward']['preg'] == 4", "images/characters/winward_mrs/funeral.webp")
image mrs_winward_funeral_veil = ConditionSwitch(
    "worldChars['mrs_winward']['clothes'] == 'funeral'", "images/characters/winward_mrs/funeral_veil.webp",
    "True", Null())

# this is for graveyard location only
image mrs_winward_funeral_baked = Composite(
    (780, 1400),
    (0, 0), "images/characters/winward_mrs/funeral.webp",
    (0, 0), "images/characters/winward_mrs/funeral_veil.webp")