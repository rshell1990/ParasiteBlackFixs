init python:
    config.tag_layer["cg_mib"] = "characters"
    config.tag_layer["cg_mage"] = "characters"
    config.tag_layer["cg_scout"] = "characters"
    config.tag_layer["cg_black_scout"] = "characters"
    config.tag_layer["cg_guard_base"] = "characters"
    config.tag_layer["cg_guard"] = "characters"
    config.tag_layer["cg_guard_rot"] = "characters"
    config.tag_layer["cg_bandit_dark"] = "characters"
    config.tag_layer["cg_random_boy"] = "characters"

    config.tag_layer["cg_demorai_brute_highrez"] = "characters"

    config.tag_layer["cg_bandit"] = "characters"
    config.tag_layer["bandit1"] = "characters"
    config.tag_layer["bandit2"] = "characters"
    config.tag_layer["bandit3"] = "characters"

    config.tag_layer["cg_dark_mage"] = "characters"
    config.tag_layer["cg_raider"] = "characters"
    
    config.tag_layer["cg_dealer"] = "characters"

    config.tag_layer["cg_man_silh"] = "characters"
    
    config.tag_layer["cg_silver_knight"] = "characters"
    config.tag_layer["cg_guard_hamun"] = "characters"
    config.tag_layer["cg_tarbeck_watcher"] = "characters"

    config.tag_layer["cg_zanarak_char"] = "characters"

    config.tag_layer["cg_zofn"] = "characters"
    config.tag_layer["cg_zarpod"] = "characters"

    config.tag_layer["cg_merl_sage"] = "characters"

    config.tag_layer["cg_theface"] = "characters"

    config.tag_layer["cg_gtc_goon"] = "characters"
    config.tag_layer["cg_gtc_goon2"] = "characters"

    config.tag_layer["theface_humanoid"] = "characters"

    config.tag_layer["cg_virgo"] = "characters"
    config.tag_layer["cg_babyface"] = "characters"
    config.tag_layer["cg_gator"] = "characters"

    config.tag_layer["cg_assassin"] = "characters"

    config.tag_layer["cg_bryher"] = "characters"
    config.tag_layer["cg_johan"] = "characters"
    config.tag_layer["cg_moharius"] = "characters"

    config.tag_layer["cg_lazzarian"] = "characters"

image cg_bryher:
    "cg_bryher_base"
    offset (0, 80)
image cg_johan:
    "cg_johan_base"
    offset (0, 80)
image cg_lazzarian:
    "cg_lazzarian_base"
    offset (0, 80)
image cg_moharius:
    "cg_moharius_base"
    offset (0, 80)

image cg_gtc_goon:
    "cg_gtc_goon_base"
    offset (0, 80)
image cg_gtc_goon2:
    "cg_gtc_goon2_base"
    offset (0, 60)

image cg_man_silh:
    "mc_p"
    yoffset 90
    matrixcolor BrightnessMatrix(-1.0)

image cg_guard:
    "cg_guard_base"
    offset CHAR_OFFSET.CG_GUARD

image cg_guard_rot:
    "cg_guard_rot_base"
    offset CHAR_OFFSET.CG_GUARD_ROT

image cg_zarpod:
    "cg_zarpod_base"
    offset CHAR_OFFSET.ZARPOD

image cg_merl_sage:
    "cg_merl_sage_base"
    offset (0, 0)

image cg_zofn:
    "cg_zofn_base"
    offset (0, 55)

image cg_tarbeck_watcher:
    "cg_tarbeck_watcher_base"
    offset (0, -90)

image cg_guard_hamun:
    "cg_guard_hamun_base"
    offset (0, -10)

image cg_theface:
    "cg_theface_base"
    offset (0, 0)

image theface_humanoid:
    "images/characters/the_face_humanoid/normal.webp"
    offset (0, 180)

image theface_humanoid smile = Composite((582, 1273), (0, 180), "images/characters/the_face_humanoid/normal.webp", (0, 180), "images/characters/the_face_humanoid/face/smile.webp")
image theface_humanoid think = Composite((582, 1273), (0, 180), "images/characters/the_face_humanoid/normal.webp", (0, 180), "images/characters/the_face_humanoid/face/think.webp")

image cg_virgo:
    "cg_virgo_base"
    offset (0, 100)
image cg_gator:
    "cg_gator_base"

image cg_babyface:
    "cg_babyface_base"

image cg_bandit2:
    "cg_bandit"
image cg_bandit3:
    "cg_bandit"
image cg_bandit4:
    "cg_bandit"

image cg_lazarian:
    offset (30, 60)
    "cg_lazarian_base"