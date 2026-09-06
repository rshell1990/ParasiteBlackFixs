init python:    
############## weapons #########
    static_item_defs["nyx_gift_sword"] = {
        "name":_("Alderian officer sword"),
        "plural":_("Alderian officer swords"),
        "desc":_("A high-quality sword issued to high-ranking Alderian officers.\nCaptain Nyx sure knew what I need the most out there."),
        "Damage":12,
        "add_stat_crit_chance":5,
        "icon":"images/items/weapons/sword_alderian.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":400,
        "shop_category":"weapon",

        "sort_order":30,
    }
    static_item_defs["scout_sword"] = {
        "name":_("Scout sword"),
        "plural":_("Scout swords"),
        "desc":_("A rather crude but well-balanced one-handed sword of the Scouts Corp."),
        "Damage":8,
        "icon":"images/items/weapons/sword_scout.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":150,
        "cannot_lose":True,
        "shop_category":"weapon",

        "sort_order":30,
    }
    static_item_defs["scout_sword_rusty"] = {
        "name":_("Rusty scout sword"),
        "plural":_("Rusty scout swords"),
        "desc":_("A barely-usable sword of the Scouts Corp. It is heavily damaged by rust and there are dents all over the blade."),
        "Damage":4,
        "icon":"images/items/weapons/sword_scout_rusty.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":25,
        "shop_category":"weapon",

        "sort_order":30,
    }
    static_item_defs["goblin_cleaver"] = {
        "name":_("Goblin cleaver"),
        "plural":_("Goblin cleavers"),
        "desc":_("A heavy, crude sword."),
        "Damage":15,
        "add_attr_dex":1,
        "icon":"images/items/weapons/sword_goblin.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":350,
        "shop_category":"weapon",

        "sort_order":30,
    }
    static_item_defs["sword_2h"] = {
        "name":_("Two-handed steel sword"),
        "plural":_("Two-handed steel sword"),
        "desc":_("A long and heavy sword, clearly designed to be wielded with both hands."),
        "Damage":25,
        "icon":"images/items/weapons/sword_2h.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":8120,
        "shop_category":"weapon",

        "sort_order":30,
    }
    static_item_defs["tarek_blade"] = {
        "name":_("Tarek's blade"),
        "plural":_("Tarek's blades"),
        "desc":_("A cruel and vicious blade designed to prolong suffering..."),
        "icon":"images/items/weapons/tarek_blade.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "Damage":14,
        "add_attr_str":1,
        "add_attr_end":1,
        "shop_category":"weapon",
        "value_per_unit": 450,

        "sort_order":30,
    }
    static_item_defs["bronze_sword"] = {
        "name":_("Bronze sword"),
        "plural":_("Bronze swords"),
        "desc":_("A bronze blade"),
        "Damage":17,
        "icon":"images/items/weapons/sword_bronze.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":1300,
        "shop_category":"weapon",

        "sort_order":30,
    }
    static_item_defs["iron_sword"] = {
        "name":_("Iron sword"),
        "plural":_("Iron swords"),
        "desc":_("A blade forged in iron"),
        "Damage":19,
        "icon":"images/items/weapons/sword_iron.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":4550,
        "shop_category":"weapon",

        "sort_order":30,
    }
    static_item_defs["steel_sword"] = {
        "name":_("Steel sword"),
        "plural":_("Steel swords"),
        "desc":_("A steel blade... finely crafted"),
        "Damage":21,
        "add_attr_dex":1,
        "icon":"images/items/weapons/sword_steel.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":10140,
        "shop_category":"weapon",

        "sort_order":30,
    }
    static_item_defs["syaxian_sword"] = {
        "name":_("Syaxian sword"),
        "plural":_("Syaxian swords"),
        "desc":_("A syaxian blade... One of the finest swords ever produced"),
        "Damage":27,
        "add_attr_dex":2,
        "icon":"images/items/weapons/sword_syax.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":17461,
        "shop_category":"weapon",

        "sort_order":30,
    }
    static_item_defs["debug_killer"] = {
        "name":_("(dev) killer sword"),
        "plural":_("(dev) killer swords"),
        "desc":_("debug them into ash"),
        "Damage":27000,
        "icon":"images/items/weapons/sword_syax.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":17461,
        "shop_category":"weapon",

        "sort_order":30,
    }
## erika
    static_item_defs["sword_inquisitor"] = {
        "name":_("Inquisitor blade"),
        "plural":_("Inquisitor blades"),
        "desc":_("A standard inquisitor blade. While not the best blades, their infused magecraft casting allows them to act as a conduit without being damaged."),
        "Damage":9,
        "icon":"images/items/weapons/sword_inquisitor.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":800,
        "shop_category":"weapon",

        "sort_order":30,
    }

## ves
    static_item_defs["orc_tribal_axe"] = {
        "name":_("Orc tribal axe"),
        "plural":_("Orc tribal axes"),
        "desc":_("A typical axe commonly used by orcs."),
        "Damage":5,
        "add_stat_crit_chance":4,
        "icon":"images/items/weapons/orc_tribal_axe.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":850,
        "shop_category":"weapon",

        "sort_order":30,
    }
    static_item_defs["ves_family_axe"] = {
        "name":_("Ves family axe"),
        "plural":_("Ves family axes"),
        "desc":_("Weathered down and rusting, this old axe seems to have belonged to Ves' father... It's not very sharp, but you sense something emitting deep from it."),
        "Damage":1,
        "add_attr_luck":1,
        "icon":"images/items/weapons/ves_family_axe.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":150,
        "shop_category":"weapon",

        "sort_order":30,
    }
## kiara
    static_item_defs["corrupted_blade"] = {
        "name":_("Corrupted blade"),
        "plural":_("Corrupted blades"),
        "desc":_("A strange, short blade that appears to have been corrupted by Demorai magecraft."),
        "Damage":5,
        "add_attr_dex":1,
        "icon":"images/items/weapons/corrupted_blade.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":400,
        "shop_category":"weapon",

        "sort_order":30,
    }

### hamun crafts
    static_item_defs["bronlite_dagger"] = {
        "name":_("Bronlite dagger"),
        "plural":_("Bronlite daggers"),
        "desc":_("A special type of bronze dagger, treated to be weaker, but considerably lighter and supposedly, thanks to the strange enchantments applied, makes the wearer faster."),
        "Damage":3,
        "add_attr_dex":1,
        "add_attr_agi":2,
        "icon":"images/items/weapons/dagger_bronlite.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":1550,
        "shop_category":"weapon",

        "sort_order":30,
    }
    static_item_defs["bronlite_sword"] = {
        "name":_("Bronlite sword"),
        "plural":_("Bronlite swords"),
        "desc":_("A special type of bronze sword, treated to be weaker, but considerably lighter and supposedly, thanks to the strange enchantments applied, makes the wearer faster."),
        "Damage":7,
        "add_attr_agi":2,
        "icon":"images/items/weapons/sword_bronlite.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":2600,
        "shop_category":"weapon",

        "sort_order":30,
    }
### sypha weapon
    static_item_defs["xeriya_spear"] = {
        "name":_("Spear of Xeriya"),
        "plural":_("Spears of Xeriya"),
        "desc":_("A uniquely crafted spear, it appears to be enchanted, I cannot tell what kind of metal it is..."),
        "Damage":12,
        "add_attr_luck":3,
        "add_attr_agi":1,
        "icon":"images/items/weapons/xeriya_spear.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":2400,
        "shop_category":"weapon",

        "sort_order":30,
    }

### faymore reward
    static_item_defs["faymore_blade"] = {
        "name":_("Faymore blade"),
        "plural":_("Faymore blades"),
        "desc":_("The Faymore family blade, once wielded by Strigon Faymore, a noble knight famous for his valor… It resonates power."),
        "Damage":18,
        # Every round heals 5% of current HP for the party
        "battle_perma_effects":["FaymoreBladeRegenParty"],
        "icon":"images/items/weapons/faymore_blade.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":5500,
        "shop_category":"weapon",
        

        "sort_order":30,
    }
