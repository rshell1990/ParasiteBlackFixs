init python:
    class BattleChar(object):
        def __init__(self, CharRef, CharID, BattleSide = 0, IsTransformed = False):
            self.CharRef = CharRef
            self.CharID = CharID
            self.BattleSide = BattleSide
            self.IsTransformed = IsTransformed
            self.SpriteTag = "battle_char_%s_%s_%s" % (BattleSide, CharID, id(self))
            self.StatusEffects = []
            self.IsAlive = True
            self.PositionSlotIndex = 0
            self.SpriteZorder = 0
            self.HudZorder = 0
            self.AudioChannelsFX = []
            self.AudioChannelVoice = None

            for AttributeName in [
                "Health", "HealthMax", "Energy", "EnergyMax", "Mana", "ManaMax",
                "Damage", "Armor", "MagicRes", "AttackRating", "DodgeRating", "CritChance"
            ]:
                setattr(self, AttributeName, CharRef.get(AttributeName, 0))

            self.Skills = []
            self.Skill_Attack = None
            self.Skill_Defend = None
            self.Skill_ExtraTransform = None
            self.Skill_ExtraUnTransform = None

    BattleCharClass = BattleChar
    # use this one if you wanna pass the string itself directly
    def Battle_AddLogEntry(Entry):
        BattleScene.LogEntries.append(Entry)
        return

    # use this one if you wanna automatically replace char names with corresp. colors or such
    def Battle_AddLogEntry_Autoformat(String = "",
            USER =                  None,
            TARGET =                None,
            PROTECTOR =             None,

            SKILL_NAME =            None,
            ITEM_NAME =             None,

            DAMAGE_AMOUNT =         None,
            BLEED_DAMAGE_AMOUNT =   None,
            BURN_DAMAGE_AMOUNT =    None,
            POISON_DAMAGE_AMOUNT =  None,

            ABSORB_AMOUNT =         None,
            HEALTH_RECOVERED =      None,
            ENERGY_RECOVERED =      None,
            MANA_STOLEN =           None,
            HEALTH_STOLEN =         None,
            
            SUM_OF_ALLIED_HP =      None,
            ):
        assert len(String) > 0, "Log entry must have string passed in"
        ResultString = String
        
        if USER is not None:
            assert "USER_NAME" in ResultString, "USER is not none for a log string but USER_NAME isnt in the string"
            user_name = USER.CharRef.get("name", "") if getattr(USER, "CharRef", None) else ""
            if USER.BattleSide == 0:
                ResultString = ResultString.replace("USER_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ALLY]}" + str(user_name) + "{/color}")
            else:
                ResultString = ResultString.replace("USER_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ENEMY]}" + str(user_name) + "{/color}")

        if TARGET is not None:
            assert "TARGET_NAME" in ResultString, "TARGET is not none for a log string but TARGET_NAME is not in the string"
            target_name = TARGET.CharRef.get("name", "") if getattr(TARGET, "CharRef", None) else ""
            if TARGET.BattleSide == 0:
                ResultString = ResultString.replace("TARGET_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ALLY]}" + str(target_name) + "{/color}")
            else:
                ResultString = ResultString.replace("TARGET_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ENEMY]}" + str(target_name) + "{/color}")
        
        if PROTECTOR is not None:
            assert "PROTECTOR_NAME" in ResultString, "PROTECTOR is not none for a log string but PROTECTOR_NAME is not in the string"
            protector_name = PROTECTOR.CharRef.get("name", "") if getattr(PROTECTOR, "CharRef", None) else ""
            if PROTECTOR.BattleSide == 0:
                ResultString = ResultString.replace("PROTECTOR_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ALLY]}" + str(protector_name) + "{/color}")
            else:
                ResultString = ResultString.replace("PROTECTOR_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ENEMY]}" + str(protector_name) + "{/color}")

        if SKILL_NAME is not None:
            ResultString = ResultString.replace("SKILL_NAME", "{color=[BATTLE_COLORS_LOG.NAME_SKILL]}" + str(SKILL_NAME) + "{/color}")

        if ITEM_NAME is not None:
            ResultString = ResultString.replace("ITEM_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ITEM]}" + str(ITEM_NAME) + "{/color}")

        if DAMAGE_AMOUNT is not None:
            ResultString = ResultString.replace("DAMAGE_AMOUNT", "{color=[BATTLE_COLORS_LOG.DAMAGE]}" + str(DAMAGE_AMOUNT) + "{/color}")

        if BLEED_DAMAGE_AMOUNT is not None:
            ResultString = ResultString.replace("BLEED_DAMAGE_AMOUNT", "{color=[BATTLE_COLORS_LOG.DAMAGE_BLEED]}" + str(BLEED_DAMAGE_AMOUNT) + "{/color}")
        if POISON_DAMAGE_AMOUNT is not None:
            ResultString = ResultString.replace("POISON_DAMAGE_AMOUNT", "{color=[BATTLE_COLORS_LOG.DAMAGE_POISON]}" + str(POISON_DAMAGE_AMOUNT) + "{/color}")
        if BURN_DAMAGE_AMOUNT is not None:
            ResultString = ResultString.replace("BURN_DAMAGE_AMOUNT", "{color=[BATTLE_COLORS_LOG.DAMAGE_BURN]}" + str(BURN_DAMAGE_AMOUNT) + "{/color}")

        if ABSORB_AMOUNT is not None:
            ResultString = ResultString.replace("ABSORB_AMOUNT", "{color=[BATTLE_COLORS_LOG.DAMAGE]}" + str(ABSORB_AMOUNT) + "{/color}")
        if HEALTH_RECOVERED is not None:
            ResultString = ResultString.replace("HEALTH_RECOVERED", "{color=[BATTLE_COLORS_LOG.RESTORE_HEALTH]}" + str(HEALTH_RECOVERED) + "{/color}")
        if ENERGY_RECOVERED is not None:
            ResultString = ResultString.replace("ENERGY_RECOVERED", "{color=[BATTLE_COLORS_LOG.RESTORE_ENERGY]}" + str(ENERGY_RECOVERED) + "{/color}")
        if MANA_STOLEN is not None:
            ResultString = ResultString.replace("MANA_STOLEN", "{color=[BATTLE_COLORS_LOG.RESTORE_ENERGY]}" + str(MANA_STOLEN) + "{/color}")
        if HEALTH_STOLEN is not None:
            ResultString = ResultString.replace("HEALTH_STOLEN", "{color=[BATTLE_COLORS_LOG.RESTORE_HEALTH]}" + str(HEALTH_STOLEN) + "{/color}")
        if SUM_OF_ALLIED_HP is not None:
            ResultString = ResultString.replace("SUM_OF_ALLIED_HP", "{color=[BATTLE_COLORS_LOG.RESTORE_HEALTH]}" + str(SUM_OF_ALLIED_HP) + "{/color}")

        BattleScene.LogEntries.append(ResultString)
        return