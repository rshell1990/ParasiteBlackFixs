# Functions listed here can be used manually via console or GUI/code hooks
init python:
    def is_debug_permitted():
        """Returns True if debug/developer mode is enabled."""
        return bool(config.developer)

    def DEBUG_CompleteAllRealQuests():
        if not is_debug_permitted():
            return
        for quest in GetAllGameQuests():
            QstStart(quest)
            QstComplete(quest)

    def DEBUG_SetAllStatsTo(value=10):
        if not is_debug_permitted():
            return
        char_ids = ["mc", "markus", "kiara", "myu", "elena", "jana", "ves"]
        stat_ids = ["Strength", "Agility", "Dexterity", "Willpower", "Endurance", "Luck", "Charisma", "Barter"]
        
        for char_id in char_ids:
            if char_id in worldChars:
                for stat_id in stat_ids:
                    if stat_id in worldChars[char_id]:
                        worldChars[char_id][stat_id] = value

    def DEBUG_AddAllPerks():
        if not is_debug_permitted():
            return
        for perk_id in Lib_Perks:
            PlayerAddPerk(perk_id, Soft=True)

    def register_debug_weapons():
        # Gate registration behind debug mode or DLC presence
        if not (is_debug_permitted() or renpy.has_label("dlc_weapons_label")):
            return

        static_item_defs["irridian_armor"] = {
            "name": _("Irridian armor"),
            "plural": _("Irridian armor"),
            "desc": _("Get Hurt By No One, Forever."),
            "add_stat_def": 99999,
            "icon": "images/items/armor/irridian_armor.webp",
            "eqp_slots": EQP_SLOTS.CHEST,
            "value_per_unit": 99999,
            "can_lose": False,
            "shop_category": "armor",
            "sort_order": 40,
        }
        static_item_defs["irridian_blade"] = {
            "name": _("Irridian blade"),
            "plural": _("Irridian blade"),
            "desc": _("Kill All Enemies, Instantly."),
            "Damage": 99999,
            "add_attr_str": 99999,
            "icon": "images/items/weapons/irridian_blade.webp",
            "eqp_slots": EQP_SLOTS.HANDS,
            "value_per_unit": 99999,
            "can_lose": False,
            "shop_category": "weapon",
            "sort_order": 30,
        }
        static_item_defs["irridian_shield"] = {
            "name": _("Irridian shield"),
            "plural": _("Irridian shields"),
            "desc": _("Can't Be Hurt, Forever"),
            "add_stat_crit_chance": 99999,
            "add_attr_end": 99999,
            "add_attr_agi": 99999,
            "icon": "images/items/armor/irridian_shield.webp",
            "eqp_slots": EQP_SLOTS.HANDS,
            "value_per_unit": 99999,
            "can_lose": False,
            "shop_category": "weapon",
            "sort_order": 30,
        }
        static_item_defs["irridian_amulet"] = {
            "name": _("Irridian amulet"),
            "plural": _("Irridian amulets"),
            "desc": _("Be Affected By No One, Forever."),
            "icon": "images/items/jewelry/irridian_amulet.webp",
            "eqp_slots": EQP_SLOTS.NECK,
            "value_per_unit": 99999,
            "can_lose": False,
            "shop_category": "jewelry",
            "sex_infection_loss_modifier": 99999,
            "add_stat_mres": 99999,
            "add_attr_int": 99999,
            "add_attr_wis": 99999,
            "add_attr_barter": 99999,
            "add_attr_luck": 99999,
            "add_attr_mp": 99999,
            "add_attr_mpr": 99999,
            "sort_order": 50,
        }

    # Execute initial registration check
    register_debug_weapons()


# Ren'Py Script Label
label debug_weapons_label:
    $ register_debug_weapons()
    return