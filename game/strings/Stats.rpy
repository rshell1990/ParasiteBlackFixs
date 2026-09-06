init -1 python in STR_STAT:
    # attributes #
    STRENGTH = _("Strength")
    STRENGTH_DESC = _("Affects raw physical damage.")
    ENDURANCE = _("Endurance")
    ENDURANCE_DESC = _("Affects maximum hitpoints and physical resistance.")
    
    WILLPOWER = _("Willpower")
    WILLPOWER_DESC = _("Affects the size of a character's energy pool and their magic resistance.")
    MANAPWR = _("Mana Power")
    MANAPWR_DESC = _("Affects the size of a character's mana pool and their magic resistance.")

    AGILITY = _("Agility")
    AGILITY_DESC = _("Affects attack rating, thus increasing the character's chance to hit an enemy.")
    DEXTERITY = _("Dexterity")
    DEXTERITY_DESC = _("Affects dodge rating, raising the chance to dodge a blow.")

    LUCK = _("Luck")
    LUCK_DESC = _("Affects chance to land a critical strike.")
    
    CHARISMA = _("Charisma")
    CHARISMA_DESC = _("Unlocks dialogue options, allowing you to charm your way around (or into) various situations.")
    BARTER = _("Barter")
    BARTER_DESC = _("Affects trade-related dialogue.")

    # derived stats #
    HEALTH = _("Health")
    HEALTH_DESC = _("Health governs how much damage this character can take.")
    ENERGY = _("Energy")
    ENERGY_DESC = _("Energy allows a character to execute skills.")
    MANA = _("Mana")
    MANA_DESC = _("Mana allows a character to cast spells.")

    DAMAGE = _("Damage")
    DAMAGE_DESC = _("Base damage this character does with their attacks and skills.\nThe actual damage is rolled between 75% and 125% of this value.")
    ARMOR = _("Armor")
    ARMOR_DESC = _("Armor is a flat damage reduction applied in combat.")
    MRES = _("Magic res.")
    MRES_DESC = _("Magic resistance is a flat damage reduction against damaging spells.\nNote: this stat does not affect anything, since there's no spells in the game yet.")
    ATTRATE = _("Attack Rating")
    ATTRATE_DESC = _("Attack rating governs the character's ability to land a strike.")
    DODGERATE = _("Dodge Rating")
    DODGERATE_DESC = _("Dodge rating governs the character's ability to avoid an incoming blow.")
    CRITCHANCE = _("Crit Chance")
    CRITCHANCE_DESC = _("Critical strike chance is a %-chance to land a more powerful blow.")

init python:
    GUI_STAT_NAME_MAP = {
        "Health":STR_STAT.HEALTH,
        "Health_desc":STR_STAT.HEALTH_DESC,
        
        "Mana":STR_STAT.MANA,
        "Mana_desc":STR_STAT.MANA_DESC,

        "Energy":STR_STAT.ENERGY,
        "Energy_desc":STR_STAT.ENERGY_DESC,

        "Damage":STR_STAT.DAMAGE,
        "Damage_desc":STR_STAT.DAMAGE_DESC,

        "Armor":STR_STAT.ARMOR,
        "Armor_desc":STR_STAT.ARMOR_DESC,

        "MagicRes":STR_STAT.MRES,
        "MagicRes_desc":STR_STAT.MRES_DESC,

        "AttackRating":STR_STAT.ATTRATE,
        "AttackRating_desc":STR_STAT.ATTRATE_DESC,

        "DodgeRating":STR_STAT.DODGERATE,
        "DodgeRating_desc":STR_STAT.DODGERATE_DESC,

        "CritChance":STR_STAT.CRITCHANCE,
        "CritChance_desc":STR_STAT.CRITCHANCE_DESC,

        "Strength":STR_STAT.STRENGTH,
        "derived_Strength":STR_STAT.STRENGTH,
        "Strength_desc":STR_STAT.STRENGTH_DESC,
        "derived_Strength_desc":STR_STAT.STRENGTH_DESC,

        "Endurance":STR_STAT.ENDURANCE,
        "derived_Endurance":STR_STAT.ENDURANCE,
        "Endurance_desc":STR_STAT.ENDURANCE_DESC,
        "derived_Endurance_desc":STR_STAT.ENDURANCE_DESC,

        "Mana_Power":STR_STAT.MANAPWR,
        "Mana_Power_desc":STR_STAT.MANAPWR_DESC,

        "Willpower":STR_STAT.WILLPOWER,
        "Willpower_desc":STR_STAT.WILLPOWER_DESC,

        "Luck":STR_STAT.LUCK,
        "Luck_desc":STR_STAT.LUCK_DESC,

        "Agility":STR_STAT.AGILITY,
        "derived_Agility":STR_STAT.AGILITY,
        "Agility_desc":STR_STAT.AGILITY_DESC,
        "derived_Agility_desc":STR_STAT.AGILITY_DESC,

        "Dexterity":STR_STAT.DEXTERITY,
        "derived_Dexterity":STR_STAT.DEXTERITY,
        "Dexterity_desc":STR_STAT.DEXTERITY_DESC,
        "derived_Dexterity_desc":STR_STAT.DEXTERITY_DESC,

        "Charisma":STR_STAT.CHARISMA,
        "Charisma_desc":STR_STAT.CHARISMA_DESC,

        "Barter":STR_STAT.BARTER,
        "derived_Barter":STR_STAT.BARTER,
        "Barter_desc":STR_STAT.BARTER_DESC,
        "derived_Barter_desc":STR_STAT.BARTER_DESC,
    }
