############### nijah expressions #################
image nijah angry = Composite((760, 1400), CHAR_OFFSET.NIJAH, "nijah_body", CHAR_OFFSET.NIJAH, "images/characters/nijah/face/angry.webp")
image nijah cry   = Composite((760, 1400), CHAR_OFFSET.NIJAH, "nijah_body", CHAR_OFFSET.NIJAH, "images/characters/nijah/face/cry.webp")
image nijah happy = Composite((760, 1400), CHAR_OFFSET.NIJAH, "nijah_body", CHAR_OFFSET.NIJAH, "images/characters/nijah/face/happy.webp")
image nijah smile = Composite((760, 1400), CHAR_OFFSET.NIJAH, "nijah_body", CHAR_OFFSET.NIJAH, "images/characters/nijah/face/laugh.webp")
image nijah lewd  = Composite((760, 1400), CHAR_OFFSET.NIJAH, "nijah_body", CHAR_OFFSET.NIJAH, "images/characters/nijah/face/lewd.webp")
image nijah sad   = Composite((760, 1400), CHAR_OFFSET.NIJAH, "nijah_body", CHAR_OFFSET.NIJAH, "images/characters/nijah/face/sad.webp")
image nijah scared= Composite((760, 1400), CHAR_OFFSET.NIJAH, "nijah_body", CHAR_OFFSET.NIJAH, "images/characters/nijah/face/scared.webp")
image nijah shock = Composite((760, 1400), CHAR_OFFSET.NIJAH, "nijah_body", CHAR_OFFSET.NIJAH, "images/characters/nijah/face/shock.webp")
image nijah shy   = Composite((760, 1400), CHAR_OFFSET.NIJAH, "nijah_body", CHAR_OFFSET.NIJAH, "images/characters/nijah/face/shy.webp")
##################################################
image nijah = Composite((760, 1400), CHAR_OFFSET.NIJAH, "nijah_body")
image nijah talk = "nijah"

image nijah_body = ConditionSwitch(
        "worldChars['nijah']['pose'] == 1", "nijah_body_pose1",
        "worldChars['nijah']['pose'] == 2", "nijah_body_pose2")
image nijah_body_pose1 = ConditionSwitch(
        "worldChars['nijah']['clothes'] == 'naked'", "nijah_body_naked_pose1",
        "worldChars['nijah']['clothes'] == 'jewelry'", "nijah_body_jewelry_pose1",
        "True", "nijah_body_robe_pose1",
)
image nijah_body_pose2 = ConditionSwitch(
        "worldChars['nijah']['clothes'] == 'naked'", "nijah_body_naked_pose2",
        "worldChars['nijah']['clothes'] == 'jewelry'", "nijah_body_jewelry_pose2",
        "True", "nijah_body_robe_pose2",
)

image nijah_body_robe_pose1 = ConditionSwitch(
        "worldChars['nijah']['preg'] == 0", "images/characters/nijah/robe_pose1.webp",
        "worldChars['nijah']['preg'] == 1", "images/characters/nijah/preg/robe_pose1_1.webp",
        "worldChars['nijah']['preg'] == 2", "images/characters/nijah/preg/robe_pose1_2.webp",
        "worldChars['nijah']['preg'] == 3", "images/characters/nijah/preg/robe_pose1_3.webp",
        "worldChars['nijah']['preg'] == 4", "images/characters/nijah/robe_pose1.webp")
image nijah_body_naked_pose1 = ConditionSwitch(
        "worldChars['nijah']['preg'] == 0", "images/characters/nijah/naked_pose1.webp",
        "worldChars['nijah']['preg'] == 1", "images/characters/nijah/preg/naked_pose1_1.webp",
        "worldChars['nijah']['preg'] == 2", "images/characters/nijah/preg/naked_pose1_2.webp",
        "worldChars['nijah']['preg'] == 3", "images/characters/nijah/preg/naked_pose1_3.webp",
        "worldChars['nijah']['preg'] == 4", "images/characters/nijah/naked_pose1.webp")

image nijah_body_jewelry_pose1 = ConditionSwitch(
        "worldChars['nijah']['preg'] == 0", "images/characters/nijah/jewel_pose1.webp",
        "worldChars['nijah']['preg'] == 1", "images/characters/nijah/preg/jewel_pose1_1.webp",
        "worldChars['nijah']['preg'] == 2", "images/characters/nijah/preg/jewel_pose1_2.webp",
        "worldChars['nijah']['preg'] == 3", "images/characters/nijah/preg/jewel_pose1_3.webp",
        "worldChars['nijah']['preg'] == 4", "images/characters/nijah/jewel_pose1.webp")
       
image nijah_body_robe_pose2 = ConditionSwitch(
        "worldChars['nijah']['preg'] == 0", "images/characters/nijah/robe_pose2.webp",
        "worldChars['nijah']['preg'] == 1", "images/characters/nijah/preg/robe_pose2_1.webp",
        "worldChars['nijah']['preg'] == 2", "images/characters/nijah/preg/robe_pose2_2.webp",
        "worldChars['nijah']['preg'] == 3", "images/characters/nijah/preg/robe_pose2_3.webp",
        "worldChars['nijah']['preg'] == 4", "images/characters/nijah/robe_pose2.webp")

image nijah_body_naked_pose2 = ConditionSwitch(
        "worldChars['nijah']['preg'] == 0", "images/characters/nijah/naked_pose2.webp",
        "worldChars['nijah']['preg'] == 1", "images/characters/nijah/preg/naked_pose2_1.webp",
        "worldChars['nijah']['preg'] == 2", "images/characters/nijah/preg/naked_pose2_2.webp",
        "worldChars['nijah']['preg'] == 3", "images/characters/nijah/preg/naked_pose2_3.webp",
        "worldChars['nijah']['preg'] == 4", "images/characters/nijah/naked_pose2.webp")
image nijah_body_jewelry_pose2 = ConditionSwitch(
        "worldChars['nijah']['preg'] == 0", "images/characters/nijah/jewel_pose2.webp",
        "worldChars['nijah']['preg'] == 1", "images/characters/nijah/preg/jewel_pose2_1.webp",
        "worldChars['nijah']['preg'] == 2", "images/characters/nijah/preg/jewel_pose2_2.webp",
        "worldChars['nijah']['preg'] == 3", "images/characters/nijah/preg/jewel_pose2_3.webp",
        "worldChars['nijah']['preg'] == 4", "images/characters/nijah/jewel_pose2.webp")

image nijah_baby = "images/characters/nijah/holding_baby_clothes.webp"