############### sophira expressions ############ 667 1400
image sophira cry   = Composite((667, 1400), (0, 0), "sophira_body", (0, 0), "images/characters/sophira/face/cry.webp")
image sophira fury  = Composite((667, 1400), (0, 0), "sophira_body", (0, 0), "images/characters/sophira/face/fury.webp")
image sophira happy = Composite((667, 1400), (0, 0), "sophira_body", (0, 0), "images/characters/sophira/face/happy.webp")
image sophira laugh = Composite((667, 1400), (0, 0), "sophira_body", (0, 0), "images/characters/sophira/face/laugh.webp")
image sophira lewd  = Composite((667, 1400), (0, 0), "sophira_body", (0, 0), "images/characters/sophira/face/lewd.webp")
image sophira sad   = Composite((667, 1400), (0, 0), "sophira_body", (0, 0), "images/characters/sophira/face/sad.webp")
image sophira shock = Composite((667, 1400), (0, 0), "sophira_body", (0, 0), "images/characters/sophira/face/shock.webp")
image sophira shy   = Composite((667, 1400), (0, 0), "sophira_body", (0, 0), "images/characters/sophira/face/shy.webp")
image sophira think = Composite((667, 1400), (0, 0), "sophira_body", (0, 0), "images/characters/sophira/face/think.webp")
image sophira talk  = "sophira"
#############################################
image sophira = Composite((667, 1400), (0, 0), "sophira_body")
image sophira_body = ConditionSwitch(
    "worldChars['sophira']['clothes'] == 'naked'",  "sophira_naked",
    "worldChars['sophira']['clothes'] == 'ling'",   "sophira_ling",
    "True", "sophira_normal",
)

image sophira_normal = ConditionSwitch(
    "worldChars['sophira']['preg'] == 0", "images/characters/sophira/dress.webp",
    "worldChars['sophira']['preg'] == 1", "images/characters/sophira/preg/dress_preg_1.webp",
    "worldChars['sophira']['preg'] == 2", "images/characters/sophira/preg/dress_preg_2.webp",
    "worldChars['sophira']['preg'] == 3", "images/characters/sophira/preg/dress_preg_3.webp",
    "True", "images/characters/sophira/dress.webp")

image sophira_naked = ConditionSwitch(
    "worldChars['sophira']['preg'] == 0", "images/characters/sophira/naked.webp",
    "worldChars['sophira']['preg'] == 1", "images/characters/sophira/naked.webp",
    "worldChars['sophira']['preg'] == 2", "images/characters/sophira/naked.webp",
    "worldChars['sophira']['preg'] == 3", "images/characters/sophira/naked.webp",
    "True", "images/characters/sophira/naked.webp")

image sophira_ling = ConditionSwitch(
    "worldChars['sophira']['preg'] == 0", "images/characters/sophira/ling.webp",
    "worldChars['sophira']['preg'] == 1", "images/characters/sophira/preg/ling_preg_1.webp",
    "worldChars['sophira']['preg'] == 2", "images/characters/sophira/preg/ling_preg_2.webp",
    "worldChars['sophira']['preg'] == 3", "images/characters/sophira/preg/ling_preg_3.webp",
    "True", "images/characters/sophira/ling.webp")