init python:
    static_item_defs["potion_heal_minor"] = {
        "name":_("Minor Health Potion"),
        "plural":_("Minor Health Potions"),
        "desc":_("The blood-red healing concotion slushes around inside."),
        "icon":"images/items/consum/potion_red1.webp",
        "value_per_unit":30,
        "on_use_battle":"PotionHeal",
        "on_use_battle_arg1":30,
        "on_use_story":[[ItemHealUserStory, 30]],
        "AI_heal": True,
        "shop_category":"magecraft",

        "sort_order":10,
    }

    static_item_defs["potion_heal_regular"] = {
        "name":_("Regular Health Potion"),
        "plural":_("Regular Health Potions"),
        "desc":_("The blood-red healing concotion slushes around inside."),
        "icon":"images/items/consum/potion_red5.webp",
        "value_per_unit":50,
        "on_use_battle":"PotionHeal",
        "on_use_battle_arg1":50,
        "on_use_story":[[ItemHealUserStory, 50]],
        "AI_heal": True,
        "shop_category":"magecraft",

        "sort_order":10,
    }

    static_item_defs["potion_heal_large"] = {
        "name":_("Large Health Potion"),
        "plural":_("Large Health Potions"),
        "desc":_("The blood-red healing concotion slushes around inside."),
        "icon":"images/items/consum/potion_red3.webp",
        "value_per_unit":70,
        "on_use_battle":"PotionHeal",
        "on_use_battle_arg1":70,
        "on_use_story":[[ItemHealUserStory, 70]],
        "AI_heal": True,
        "shop_category":"magecraft",

        "sort_order":10,
    }

    static_item_defs["potion_heal_vlarge"] = {
        "name":_("Very Large Health Potion"),
        "plural":_("Very Large Health Potions"),
        "desc":_("The blood-red healing concotion slushes around inside."),
        "icon":"images/items/consum/potion_red4.webp",
        "value_per_unit":200,
        "on_use_battle":"PotionHeal",
        "on_use_battle_arg1":110,
        "on_use_story":[[ItemHealUserStory, 110]],
        "AI_heal": True,
        "shop_category":"magecraft",

        "sort_order":10,
    }

    static_item_defs["goblin_bomb"] = {
        "name":         _("Goblin bomb"),
        "plural":       _("Goblin bombs"),
        "desc":         _("Ka-booms!"),
        "icon":         "images/items/consum/goblin_bomb.webp",
        "value_per_unit":150,
        "on_use_battle":"GoblinBomb",
        "show_battle_desc_in_story_mode":True,
        "shop_category":"magecraft",

        "sort_order":10,
    }

    static_item_defs["grapes"] = {
        "name":_("Bunch of grapes"),
        "plural":_("Bunch of grapes"),
        "desc":_("Usually encountered in a form of wine these days,\nthis fruit is deliciously refreshing."),
        "icon":"images/items/consum/grapes.webp",
        "value_per_unit":75,
        "on_use_battle":"BattleFoodHeal",
        "on_use_battle_arg1":5,
        "on_use_story":[[ItemHealUserStory, 5]],
        "AI_heal": True,
        "shop_category":"food",

        "sort_order":10,
    }

    static_item_defs["goblin_stims"] = {
        "name":_("Goblin Stimulants"),
        "plural":_("Goblin Stimulants"),
        "desc":_("These goblin alchemists sure know how to make your blood boil..."),
        "icon":"images/items/consum/goblin_stims.webp",
        "value_per_unit":100,
        "on_use_battle":"GoblinStims",
        "show_battle_desc_in_story_mode":True,
        "AI_restore_energy": True,
        "shop_category":"magecraft",
        
        "sort_order":10,
    }

    static_item_defs["elena_gift_book"] = {
        "name":_("The dreams of Ashara - A love story"),
        "plural":_("The dreams of Ashara - A love story"),
        "desc":_("A gift from Elena. Will raise your charisma if used."),
        "icon":"images/items/consum/elena_gift_book.webp",
        "value_per_unit":250,
        "on_use_story":[[ItemRaiseAttStory, ("Charisma", 1)]],
        "shop_category":"book",

        "sort_order":10,
    }

    static_item_defs["myu_gift_jar"] = {
        "name":_("A small slime jar"),
        "plural":_("A small slime jar"),
        "desc":_("A gift from Myu."),
        "icon":"images/items/consum/myu_gift_jar.webp",
        "value_per_unit":350,
        "on_use_story":[[ItemClearInfectionStory]],
        "shop_category":"magecraft",

        "sort_order":10,
    }

    
    
    static_item_defs["ramonian_twister"] = {
        "name":_("Ramonian Twister"),
        "plural":_("Ramonian Twisters"),
        "desc":_("Yummy!"),
        "icon":"images/items/consum/shavuha.webp",
        "value_per_unit":80,
        "on_use_battle":"BattleFoodHeal",
        "on_use_battle_arg1":100,
        "on_use_story":[[ItemHealUserStory, 100]],
        "AI_heal": True,
        "shop_category":"food",

        "sort_order":10,
    }

    static_item_defs["raza_seed"] = {
        "name":_("Raza seed"),
        "plural":_("Raza seeds"),
        "desc":_("Raza infused into chewable seeds... Highly addictive, but often eaten and consumed for immediate pain relief."),
        "icon":"images/items/consum/raza_seed.webp",
        "on_use_battle":"RazaSeed",
        "on_use_story":[[ItemRazaEffectUser]],
        "value_per_unit": 12,
        "shop_category":"illegal",

        "sort_order":10,
        }

    static_item_defs["strange_meat"] = {
        "name":_("Strange meat"),
        "plural":_("Strange meats"),
        "desc":_("A strange meat with an odd smell..."),
        "on_use_battle":"StrangeMeat",
        "on_use_story":[[ItemStrangeMeatPoisonUser]],
        "icon":"images/items/consum/strange_meat.webp",
        "value_per_unit":2,
        "shop_category":"food",

        "sort_order":10,
        }

    static_item_defs["potion_antidote"] = {
        "name":_("Antidote"),
        "plural":_("Antidote"),
        "desc":_("A dark, sour liquid."),
        "icon":"images/items/consum/antidote.webp",
        "value_per_unit":80,
        "on_use_battle":"PotionAntidote",
        "on_use_story":[[ItemAntidoteStory]],
        "AI_heal": True,
        "shop_category":"magecraft",

        "sort_order":10,
        }
    static_item_defs["potion_lowrevival"] = {
        "name":_("LowRevival"),
        "plural":_("LowRevival"),
        "desc":_("A small golden, creamy liquid in a bottle."),
        "icon":"images/items/consum/revival.webp",
        "value_per_unit":140,
        "on_use_battle":"PotionRevival",
        "AI_heal": True,
        "shop_category":"magecraft",

        "sort_order":10,
    }
    static_item_defs["potion_medrevival"] = {
        "name":_("MedRevival"),
        "plural":_("MedRevival"),
        "desc":_("A refined golden, creamy liquid in a bottle."),
        "icon":"images/items/consum/medrevival.webp",
        "value_per_unit":500,
        "on_use_battle":"PotionMedRevival",
        "AI_heal": True,
        "shop_category":"magecraft",

        "sort_order":10,
    }
    static_item_defs["potion_highrevival"] = {
        "name":_("HighRevival"),
        "plural":_("HighRevival"),
        "desc":_("An ultra refined golden, creamy liquid in a bottle."),
        "icon":"images/items/consum/highrevival.webp",
        "value_per_unit":999,
        "on_use_battle":"PotionHighRevival",
        "AI_heal": True,
        "shop_category":"magecraft",

        "sort_order":10,
    }