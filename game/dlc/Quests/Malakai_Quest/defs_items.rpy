init python:
    ### TheDarkSpecterOfBiggieSmalls reward
    static_item_defs["void_armor"] = {
        "name":_("Void armor"),
        "plural":_("Void armor"),
        "desc":_("Powerful, beautifully crafted armor reeking of old god magecraft... Whatever being made this, did so to give it to their champion..."),
        "Armor":200,
        "icon":"images/items/armor/void_armor.webp",
        "eqp_slots":EQP_SLOTS.CHEST,
        "value_per_unit": 35000,
        "can_lose": False, #'For some reason... I cannot bring myself to part with it...'
        "shop_category":"armor",
        "sort_order":40,
    }
    static_item_defs["shadowreach"] = {
        "name":_("Shadowreach"),
        "plural":_("Shadowreach"),
        "desc":_("A beautifully crafted blade resonating with the magecraft of the old gods... One can simply feel the power resonating through it by looking at it."),
        "Damage":50,
        "icon":"images/items/weapons/shadowreach.webp",
        "eqp_slots":EQP_SLOTS.HANDS,
        "value_per_unit":50000,
        "can_lose": False, #'For some reason... I cannot bring myself to part with it...'
        "shop_category":"weapon",
        "sort_order":30,
    }
    #IMPLEMENTATION: Grant Void Armor and Shadowreach, complete 'Sweet dreams...', and award 250 XP. Both reward items are permanently unsellable.
#Armor - 'Void Armor' - Armor description: Powerful, beautifully crafted armor reeking of old god magecraft... Whatever being made this, did so to give it to their champion... Value: 35000 (The armor cannot be sold - if player tries in a shop circling over it simply reads 'For some reason... I cannot bring myself to part with it...')
#Sword - 'Shadowreach' - Weapon description: A beautifully crafted blade resonating with the magecraft of the old gods... One can simply feel the power resonating through it by looking at it. Value 50000 (Cannot be sold, same as above)
