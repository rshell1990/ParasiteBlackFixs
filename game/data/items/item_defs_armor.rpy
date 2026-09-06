init python:    
############## armor ##########
    static_item_defs["leather_armor"] = {
        "name":_("Leather armor"),
        "plural":_("Leather armors"),
        "desc":_("An armor set made from boiled leather. It wouldn't help much against a heavy slash, but it's better protection than none at all."),
        "Armor":6,
        "icon":"images/items/armor/armor_leather.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit":200,
        "shop_category":"armor",

        "sort_order":40,
    }

    static_item_defs["scout_armor"] = {
        "name":_("Scout armor"),
        "plural":_("Scout armors"),
        "desc":_("An armor of the Alderian scouts. A lightweight design made from sturdy leather reinforced with crudely-forged armor plates."),
        "Armor":5,
        "icon":"images/items/armor/armor_scout.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit":220,
        "cannot_lose":True,
        "shop_category":"armor",

        "sort_order":40,
    }

    static_item_defs["father_armor_item"] = {
        "name":_("Plate armor"),
        "plural":_("Plate armors"),
        "desc":_("A heavy armor set, a gift from my father. Quite cumbersome, it offers decent protection."),
        "Armor":10,
        "icon":"images/items/armor/armor_metal.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit":1200,
        "shop_category":"armor",

        "sort_order":40,
    }

    static_item_defs["reinforced_leather_armor"] = {
        "name":_("Reinforced leather armor"),
        "plural":_("Reinforced leather armors"),
        "desc":_("Leather armor, reinforced and sturdier than usual, a favorite of rogues and bandits."),
        "Armor": 7,
        "icon":"images/items/armor/armor_reinf_leather.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit":625,
        "shop_category":"armor",

        "sort_order":40,
    }

    static_item_defs["chainmail"] = {
        "name":_("Chainmail"),
        "plural":_("Chainmails"),
        "desc":_("Armor consisting of many interlocking small metal rings."),
        "Armor":8,
        "icon":"images/items/armor/armor_chainmail.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 825,
        "shop_category":"armor",

        "sort_order":40,
    }

    static_item_defs["bronze_armor"] = {
        "name":_("Bronze armor"),
        "plural":_("Bronze armors"),
        "desc":_("Metal armor formed from bronze, often worn by lower ranked adventures on a budget."),
        "Armor":10,
        "icon":"images/items/armor/armor_bronze.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 3200,
        "shop_category":"armor",

        "sort_order":40,
    }

    static_item_defs["iron_armor"] = {
        "name":_("Iron armor"),
        "plural":_("Iron armors"),
        "desc":_("Armor forged in iron, sturdy stuff."),
        "Armor":12,
        "icon":"images/items/armor/armor_iron.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 5564,
        "shop_category":"armor",

        "sort_order":40,
    }

    static_item_defs["steel_armor"] = {
        "name":_("Steel armor"),
        "plural":_("Steel armors"),
        "desc":_("The finest armor {i}publicly{/i} available."),
        "Armor":14,
        "icon":"images/items/armor/armor_steel.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 11232,
        "shop_category":"armor",

        "sort_order":40,
    }

    static_item_defs["syaxian_armor"] = {
        "name":_("Syaxian armor"),
        "plural":_("Syaxian armors"),
        "desc":_("The old Armor worn by the Alderian army, some of the greatest armor ever created."),
        "Armor":17,
        "icon":"images/items/armor/armor_syax.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 20579,
        "shop_category":"armor",

        "sort_order":40,
    }

### erika
    static_item_defs["inquisitor_uniform"] = {
        "name":_("Inquisitor uniform"),
        "plural":_("Inquisitor uniforms"),
        "desc":_("A standard inquisitor uniform. Reinforced leather with some ornate decorating. It provides decent enough protection and allows the inquisitor to stay nimble in battle."),
        "Armor": 7,
        "icon":"images/items/armor/armor_inquisitor_uniform.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit":725,
        "shop_category":"armor",

        "sort_order":40,
    }

### ves
    static_item_defs["orc_tribal_wear"] = {
        "name":_("Orc tribal wear"),
        "plural":_("Orc tribal wear"),
        "desc":_("A mixture of leathers, bones and cloths, light and agile, but provide little protection for the wearer."),
        "Armor": 4,
        "icon":"images/items/armor/orc_tribal_wear.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit":250,
        "shop_category":"armor",

        "sort_order":40,
    }

### kiara
    static_item_defs["duskshroud_raiment"] = {
        "name":_("Duskshroud Raiment"),
        "plural":_("Duskshroud Raiments"),
        "desc":_("A stylish, well-crafted set of robes and clothes designed to blend in with the dark, agile, but provides minimal protection."),
        "Armor": 2,
        "add_attr_dex":1,
        "icon":"images/items/armor/duskshroud_raiment.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit":300,
        "shop_category":"armor",

        "sort_order":40,
    }

### hamun crafts
    static_item_defs["bronlite_armor"] = {
        "name":_("Bronlite armor"),
        "plural":_("Bronlite armors"),
        "desc":_("A special type of bronze armor, treated to be weaker, but considerably lighter and supposedly, thanks to the strange enchantments applied, makes the wearer faster."),
        "Armor":5,
        "add_attr_dex":3,
        "icon":"images/items/armor/armor_bronlite.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 4200,
        "shop_category":"armor",

        "sort_order":40,
    }

    static_item_defs["reinf_desert_robes"] = {
        "name":_("Reinforced desert robes"),
        "plural":_("Reinforced desert robes"),
        "desc":_("A favorite of desert bandits, taking light robes with pieces of miscellaneous metals applied through elaborate braces beneath, the armor provides minimal protection but allows the user to strike quickly."),
        "Armor":4,
        "add_attr_dex":1,
        "icon":"images/items/armor/reinf_desert_robes.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 1250,
        "shop_category":"armor",

        "sort_order":40,
    }

### sypha armor
    static_item_defs["xeriya_armor"] = {
        "name":_("Order of Xeriya armor"),
        "plural":_("Order of Xeriya armors"),
        "desc":_("A strangely crafted Demorai armor, it appears to be enchanted, and is both strong and versatile for speed."),
        "Armor":7,
        "add_attr_dex":1,
        "add_attr_agi":1,
        "icon":"images/items/armor/xeriya_armor.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 2850,
        "shop_category":"armor",

        "sort_order":40,
    }

### dreamhouse reward
    static_item_defs["faymore_armor"] = {
        "name":_("Faymore armor"),
        "plural":_("Faymore armor"),
        "desc":_("The Faymore family armor, worn by Strigon Faymore, wearing it gives a sense that the darkness of the world recedes every so slightly…"),
        # Every round, heals 10% of current HP for the wearer
        "battle_perma_effects":["FaymoreArmorRegenWearer"],
        "Armor":12,
        "icon":"images/items/armor/faymore_armor.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 7500,
        "shop_category":"armor",
        "sort_order":40,
    }

