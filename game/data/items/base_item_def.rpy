init -1 python:
    # every static item definition extends this dict
    static_item_defs = {}
    # used to define which enemy drops what,
    # actual entries are placed near specific battle mob definitions
    LootDropData = {}

    
    # every item updates a copy of this dict, you can also use it like a reference list
    base_item = {
        "name":"!name missing",
        "desc":"!missing a description",
        "template_ID":None,
        "plural":None, 
        "icon":"images/gui/inventory_slots/missing_icon.webp",
        # for legit slots look up 'python in EQP_SLOTS'
        # should be like EQP_SLOTS.HANDS
        "eqp_slots":None,
        # price in gold coins per unit
        "value_per_unit":0,
        # "quest item", cannot be lost by ingame means (trade, drop)
        "cannot_lose":False, 

        # callables to happen if player "uses" an item in story mode
        # format is [[], []] which is [callable, args], [callable, args]
        # for an example see healing potion
        "on_use_story":None, 
        # callables to happen if player "uses" an item in battle
        # format is "battle action ID", the id is defined in a decorator call RegisterBattleItemAction
        "on_use_battle":None,
        # this is used by battle actions, example is "how many hp to restore"
        "on_use_battle_arg1":None,

        # a LIST of IDs of status effects to apply on battle start
        # at the time of making this its designed for Faymore armor/blade
        "battle_perma_effects":None,

        # if this flag is true, in story mode it will GetDesc from battle action
        "show_battle_desc_in_story_mode":False,

        # ai-only flag, "this item heals if used"
        "AI_heal":False,
        # ai-only flag, "this item restores EP if used"
        "AI_restore_energy":False,

        # flat increase to damage if equipped
        "Damage":0,
        # flat increase to armor if equipped
        "Armor":0,

        # float, multiplies infection loss on sex, for example see divine_gift_amulet
        "sex_infection_loss_modifier":0.0, 

        # flat increase to corresp. derived stat
        "add_stat_mres":0,
        "add_stat_crit_chance":0,

        # flat change (inc/decr) to corresp. attribute if equipped
        "add_attr_dex":0,
        "add_attr_str":0,
        "add_attr_end":0,
        "add_attr_barter":0,
        "add_attr_agi":0,
        "add_attr_luck":0,
        "add_attr_will":0,

        # item category is for shop type based sell/discounts
        # if None the item wont be bought by any shop
        "shop_category":None,

        "sort_order":999, # <- less means show earlier in containers
    }

    static_item_defs["gold"] = {
        "name":_("Gold"),
        "plural":_("Gold"),
        "desc":_("The universal language."),
        "icon":"images/items/gold.webp",
        "value_per_unit":1,
        "sort_order":0,
    }