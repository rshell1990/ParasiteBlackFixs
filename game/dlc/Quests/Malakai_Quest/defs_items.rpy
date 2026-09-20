init python:
    static_item_defs["void_armor"] = {
        "name":_("Void armor"),
        "plural":_("Void armor"),
        "desc":_("Powerful, beautifully crafted armor reeking of old god magecraft... Whatever being made this, did so to give it to their champion..."),
        "Armor":13,
        "grants_skill":"Summon2",
        "icon":"dlc/Quests/Malakai_Quest/Malakai/PB_Icon_DarkArmor_Chest.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 35000,
        "cannot_lose": True, #'For some reason... I cannot bring myself to part with it...'
        "shop_category":"armor",
        "sort_order":40,
    }
    static_item_defs["shadowreach"] = {
        "name":_("Shadowreach"),
        "plural":_("Shadowreach"),
        "desc":_("A beautifully crafted blade resonating with the magecraft of the old gods... One can simply feel the power resonating through it by looking at it."),
        "Damage":50,
        "battle_perma_effects":["shadowreach_stealhpstrike"],
        "icon":"dlc/Quests/Malakai_Quest/Malakai/PB_Icon_DarkArmor_Sword.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":50000,
        "cannot_lose": True, #'For some reason... I cannot bring myself to part with it...'
        "shop_category":"weapon",
        "sort_order":30,
    }
