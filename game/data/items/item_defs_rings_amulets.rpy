init python:
############## amulets ##########
    static_item_defs["divine_gift_amulet"] = {
        "name":_("Amplifier Amulet"),
        "plural":_("Amplifier Amulets"),
        "desc":_("A gift from Sister Divine.\nIncreases the amount of parasite infection you lose when having sex."),
        "icon":"images/items/jewelry/divine_amulet.webp",
        "eqp_slots":EQP_SLOTS.NECK,
        "value_per_unit":450,
        "sex_infection_loss_modifier":1.25,
        "shop_category":"jewelry",

        "sort_order":50,
    }
    static_item_defs["arlena_gift_amulet"] = {
        "name":_("Heart Amulet"),
        "plural":_("Heart Amulets"),
        "desc":_("A gift from Arlena."),
        "icon":"images/items/jewelry/arlena_amulet.webp",
        "eqp_slots":EQP_SLOTS.NECK,
        "value_per_unit":1000,
        "shop_category":"jewelry",

        "sort_order":50,
    }
    static_item_defs["amulet_protection"] = {
        "name":_("Protection Amulet"),
        "plural":_("Protection Amulets"),
        "desc":_("An amulet."),
        "Armor":5,
        "icon":"images/items/jewelry/amulet1.webp",
        "eqp_slots":EQP_SLOTS.NECK,
        "value_per_unit":150,
        "shop_category":"jewelry",

        "sort_order":50,
    }

## erika
    static_item_defs["ring_inquisitor"] = {
        "name":_("Inquisitor ring of divine protection"),
        "plural":_("Inquisitor rings of divine protection"),
        "desc":_("A small, blessed ring, all inquisitors are given them in the hopes it can help repel any dark magecraft thrown their way."),
        "icon":"images/items/jewelry/ring_inquisitor.webp",
        "eqp_slots":EQP_SLOTS.RINGS,
        "value_per_unit":300,
        "add_stat_mres":5,
        "shop_category":"jewelry",

        "sort_order":50,
    }
    static_item_defs["dros_gift"] = {
        "name":_("A ruby ring"),
        "plural":_("A ruby ring"),
        "desc":_("A gift from that one peculiar elf I know."),
        "add_attr_barter":1,
        "icon":"images/items/jewelry/dros_gift.webp",
        "eqp_slots":EQP_SLOTS.RINGS,
        "value_per_unit":350,
        "shop_category":"jewelry",

        "sort_order":50,
    }

    # UNUSED (you cant get it anywhere)
    static_item_defs["infernium_ring"] = {
        "name":_("Infernium ring"),
        "plural":_("Infernium rings"),
        "desc":_("A ring forged from a pact with a demon, increasing the users strength at the cost of their endurance."),
        "icon":"images/items/jewelry/ring_inferno.webp",

        "add_attr_str":2,
        "add_attr_end":-1,

        "eqp_slots":EQP_SLOTS.RINGS,
        "value_per_unit":300,
        "shop_category":"jewelry",

        "sort_order":50,
    }

    # UNUSED (you cant get it anywhere)
    static_item_defs["elven_house_insignia_ring"] = {
        "name":_("Elven house insignia ring"),
        "plural":_("Elven house insignia rings"),
        "desc":_("A ring representing one of the many elven lords houses, common amongst elves"),
        "icon":"images/items/jewelry/ring_elven.webp",

        "add_attr_agi":1,

        "eqp_slots":EQP_SLOTS.RINGS,
        "value_per_unit":75,
        "shop_category":"jewelry",

        "sort_order":50,
    }

    
    static_item_defs["orc_tribal_necklace"] = {
        "name":_("Orc tribal necklace"),
        "plural":_("Orc tribal necklaces"),
        "desc":_("A necklace made of small bones with insignias carved into them, it radiates a strange energy."),
        "icon":"images/items/jewelry/necklace_orc.webp",

        "eqp_slots":EQP_SLOTS.NECK,

        "add_attr_will":1,
        "value_per_unit":150,
        "shop_category":"jewelry",

        "sort_order":50,
    }

## kiara
    static_item_defs["shadow_ring"] = {
        "name":_("Shadow ring"),
        "plural":_("Shadow rings"),
        "desc":_("A simple ring that emits a strange, dark aura..."),
        "icon":"images/items/jewelry/shadow_ring.webp",
        "eqp_slots":EQP_SLOTS.RINGS,
        "value_per_unit":350,
        "add_attr_agi":2,
        "shop_category":"jewelry",

        "sort_order":50,
    }
### hamun craft
    static_item_defs["ring_of_wealth"] = {
        "name":_("Ring of Wealth"),
        "plural":_("Rings of Wealth"),
        "desc":_("Popular amongst merchant lords. These special blessed rings are said to help with business."),
        "icon":"images/items/jewelry/ring_of_wealth.webp",
        "eqp_slots":EQP_SLOTS.RINGS,
        "value_per_unit":3200,
        "add_attr_barter":2,
        "shop_category":"jewelry",

        "sort_order":50,
    }

### beast of novaras sypha locket
    static_item_defs["lovers_locket"] = {
        "name":_("Half-Heart locket"),
        "plural":_("Half-Heart lockets"),
        "desc":_("Half of a heart-shaped locket, a common gift for lovers in Ramon... Sypha has the other half."),
        "icon":"images/items/jewelry/lovers_locket.webp",
        "eqp_slots":EQP_SLOTS.NECK,
        "value_per_unit":250,
        "shop_category":"jewelry",

        "sort_order":50,
    }