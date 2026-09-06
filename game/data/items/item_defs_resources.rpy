init python:
    static_item_defs["bronze_scraps"] = {
        "name":_("Bronze scraps"),
        "plural":_("Bronze scraps"),
        "desc":_("A blacksmith might find some use for this."),
        "icon":"images/items/res/bronze_scraps.webp",
        "value_per_unit":15,
        "shop_category":"crafting",

        "sort_order":60,
    }
    static_item_defs["gems"] = {
        "name":_("Gems"),
        "plural":_("Gems"),
        "desc":_("Gems are truly outrageous.\nThey are truly, truly, truly... outrageous."),
        "icon":"images/items/res/pink_gems.webp",
        "value_per_unit":50,
        "shop_category":"crafting",

        "sort_order":60,
    }
    static_item_defs["raw_gems"] = {
        "name":_("Raw gems"),
        "plural":_("Raw gems"),
        "desc":_("Uncut, these are totally unremarkable."),
        "icon":"images/items/res/raw_gems.webp",
        "value_per_unit":25,
        "shop_category":"crafting",

        "sort_order":60,
    }
    static_item_defs["slimelark_remains"] = {
        "name":_("Slimelark remains"),
        "plural":_("Slimelark remains"),
        "desc":_("Not as tough now in that bottle huh, slime?"),
        "icon":"images/items/res/slimelark_remains.webp",
        "value_per_unit":25,
        "shop_category":"crafting",

        "sort_order":60,
    }
    static_item_defs["red_meat"] = {
        "name":_("Red meat"),
        "plural":_("Red meat"),
        "desc":_("Suspiciously appetizing."),
        "icon":"images/items/res/red_meat.webp",
        "value_per_unit":30,
        "shop_category":"food",

        "sort_order":60,
    }
    static_item_defs["darkmage_design_notes"] = {
        "name":_("Dark Mage design notes"),
        "plural":_("Dark Mage design notes"),
        "desc":_("These... schemes might yield some coin if I can find a buyer."),
        "icon":"images/items/res/darkmage_design_notes.webp",
        "value_per_unit":80,
        "shop_category":"magecraft",

        "sort_order":60,
    }

    static_item_defs["animal_hide"] = {
        "name":_("Animal hide"),
        "plural":_("Animal hides"),
        "desc":_("A tanner might be able to turn this into some leather."),
        "icon":"images/items/res/animal_hide.webp",
        "value_per_unit":25,
        "shop_category":"crafting",

        "sort_order":60,
    }
    static_item_defs["white_bear_hide"] = {
        "name":_("White bear hide"),
        "plural":_("White bear hides"),
        "desc":_("It must be useful for something..."),
        "icon":"images/items/res/white_animal_hide.webp",
        "value_per_unit":100,
        "shop_category":"crafting",

        "sort_order":60,
    }
    static_item_defs["iron_ore"] = {
        "name":_("Iron ore"),
        "plural":_("Iron ore"),
        "desc":_("A blacksmith might find some use for this."),
        "icon":"images/items/res/iron_ore.webp",
        "value_per_unit":35,
        "shop_category":"crafting",

        "sort_order":60,
    }
    static_item_defs["copper_ore"] = {
        "name":_("Copper ore"),
        "plural":_("Copper ore"),
        "desc":_("A blacksmith could turn these seemingly useless rocks into bronze."),
        "icon":"images/items/res/copper_ore.webp",
        "value_per_unit":35,
        "shop_category":"crafting",

        "sort_order":60,
    }
    static_item_defs["leather"] = {
        "name":_("Leather"),
        "plural":_("Leather"),
        "desc":_("A blacksmith might find some use for this."),
        "icon":"images/items/res/leather.webp",
        "value_per_unit":25,
        "shop_category":"crafting",

        "sort_order":60,
    }
   
    static_item_defs["syax_ore"] = {
        "name":_("Syax ore"),
        "plural":_("Syax ore"),
        "desc":_("A blacksmith might find some use for this."),
        "icon":"images/items/res/syax_ore.webp",
        "value_per_unit":45,
        "shop_category":"crafting",

        "sort_order":60,
    }

    static_item_defs["cow_hide"] = {
        "name":_("Cow hide"),
        "plural":_("Cow hides"),
        "desc":_("Moo!"),
        "icon":"images/items/res/cowhide.webp",
        "value_per_unit":120,
        "shop_category":"crafting",

        "sort_order":60,
    }

    # used for crafting, supposed to be rewarded by some later quests
    static_item_defs["royal_decree"] = {
        "name":_("Royal Decree"),
        "plural":_("Royal Decrees"),
        "desc":_("A piece of paper documenting the individual's incredible service to the empire."),
        "icon":"images/items/res/royal_decree.webp",
        "value_per_unit":0,
        "cannot_lose":True,
        "shop_category":"crafting",

        "sort_order":60,
    }

    ####################################################################################
    #All pickaxes should be purchasable by the blacksmith
    static_item_defs["bronze_pickaxe"] = {
        "name":_("Bronze pickaxe"),
        "plural":_("Bronze pickaxes"),
        "desc":_("A pickaxe specially designed for mining copper ore, it radiates some light magecraft property to prevent rusting."),
        "icon":"images/items/res/pick_bronze.webp",
        "value_per_unit":850,
        "shop_category":"crafting",

        "sort_order":59,
    }
    static_item_defs["iron_pickaxe"] = {
        "name":_("Iron pickaxe"),
        "plural":_("Iron pickaxes"),
        "desc":_("A sturdy pickaxe designed for mining iron ore, it radiates some light magecraft property to prevent rusting."),
        "icon":"images/items/res/pick_iron.webp",
        "value_per_unit":2250,
        "shop_category":"crafting",

        "sort_order":59,
    }
    static_item_defs["syax_pickaxe"] = {
        "name":_("Syax pickaxe"),
        "plural":_("Syax pickaxes"),
        "desc":_("A sturdy pickaxe designed for mining syax ore... It has the royal insignia etched onto the handle."),
        "icon":"images/items/res/pick_syax.webp",
        "value_per_unit":4500,
        "shop_category":"crafting",

        "sort_order":59,
    }
    static_item_defs["spaceship_crystal"] = {
        "name":_("Strange crystal"),
        "plural":_("Strange crystals"),
        "desc":_("This item was recovered from the ruins of a strange ship... It emanates a strange aura unlike anything I've ever seen."),
        "icon":"images/items/res/spaceship_crystal.webp",
        "value_per_unit":2000,
        "shop_category":"magecraft",

        "sort_order":60,
    }
    ############## runes
    static_item_defs["rune_of_quickness"] = {
        "name":_("Rune of Quickness"),
        "plural":_("Runes of Quickness"),
        "desc":_("A runestone with some kind of insignia marking, it emits some form of magecraft energy - this one seems focused on increasing one's speed."),
        "icon":"images/items/res/rune_of_quickness.webp",
        "value_per_unit":750,
        "shop_category":"magecraft",

        "sort_order":60,
    }
    static_item_defs["rune_of_power"] = {
        "name":_("Rune of Power"),
        "plural":_("Runes of Power"),
        "desc":_("A runestone with some kind of insignia marking, it emits some form of magecraft energy - this one seems focused on giving one more raw, physical power."),
        "icon":"images/items/res/rune_of_power.webp",
        "value_per_unit":750,
        "shop_category":"magecraft",

        "sort_order":60,
    }
    static_item_defs["rune_of_defence"] = {
        "name":_("Rune of Defence"),
        "plural":_("Runes of Defence"),
        "desc":_("A runestone with some kind of insignia marking, it emits some form of magecraft energy - this one seems focused on helping one with defending themselves from attacks."),
        "icon":"images/items/res/rune_of_defence.webp",
        "value_per_unit":850,
        "shop_category":"magecraft",

        "sort_order":60,
    }