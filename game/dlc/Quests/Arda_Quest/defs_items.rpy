init python:
    static_item_defs["champion_armor"] = {
        "name": _("Champion armor"),
        "plural": _("Champion armor"),
        "desc": _("Stunning armor radiating power... Simply looking at it gives a sense of something holy."),
        "Armor": 200,
        "icon": "images/items/armor/champion_armor.webp",
        "eqp_slots": EQP_SLOTS.CHEST,
        "value_per_unit": 35000,
        "can_lose": False,
        "cant_sell_msg": _("For some reason... I cannot bring myself to part with it..."),
        "shop_category": "armor",
        "sort_order": 40,
    }
    static_item_defs["star_bringer"] = {
        "name": _("Star Bringer"),
        "plural": _("Star Bringer"),
        "desc": _("A perfect blade. The new gods' magecraft is etched into the very soul of the sword itself..."),
        "Damage": 50,
        "icon": "images/items/weapons/star_bringer.webp",
        "eqp_slots": EQP_SLOTS.HANDS,
        "value_per_unit": 50000,
        "can_lose": False,
        "cant_sell_msg": _("For some reason... I cannot bring myself to part with it..."),
        "shop_category": "weapon",
        "sort_order": 30,
    }