init python:
    ### TheDarkSpecterOfBiggieSmalls reward
    static_item_defs["gooner_armor"] = {
        "name":_("Gooner armor"),
        "plural":_("Gooner armor"),
        "desc":_("This armor smells stale, depressed, and faintly of dried jizz"),
        "Armor":200,
        "icon":"images/items/armor/faymore_armor.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 0,
        "shop_category":"armor",
        "sort_order":40,
    }
    static_item_defs["qst_feline"] = {
        "name":_("Feline"),
        "desc":_("A feline statue that was given to me by Garen to give to Sweetie at the Brothel"), 
        "cannot_lose":False,
        "icon":"images/items/quest/qst_strange_totem.webp",
        "sort_order":20,
        "value_per_unit":9999,
    }
    static_item_defs["qst_dodgy_tax_receipts"] = {
        "name":_("dodgy tax receipts"),
        "desc":_("Garen's receipts showing how often he has defrauded the government over the years"), 
        "cannot_lose":True,
        "icon":"images/items/quest/qst_bloody_scroll.webp",
        "sort_order":20,
        "value_per_unit":99999,
    }
    static_item_defs["trotskys_bane"] = {
        "name":_("Trotsky's Bane"),
        "plural":_("Trotsky's Banes"),
        "desc":_("A powerful blade forged in the image of Leon Trotsky, said to grant its wielder the ability to inspire rebellion, weapon of the Russianest Russian."),
        "Damage":50,
        "icon":"images/items/weapons/faymore_blade.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":7000,
        "shop_category":"weapon",
        "sort_order":30,
    }