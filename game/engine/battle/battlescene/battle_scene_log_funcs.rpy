init python:
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
            
            SUM_OF_ALLIED_HP =      None,
            ):
        Assert(len(String) > 0, "Log entry must have string passed in")
        ResultString = String
        if USER is not None:
            Assert("USER_NAME" in ResultString, "USER is not none for a log string but USER_NAME isnt in the string")
            if USER.BattleSide == 0:
                ResultString = ResultString.replace("USER_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ALLY]}" + tra(USER.CharRef["name"]) + "{/color}")
            else:
                ResultString = ResultString.replace("USER_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ENEMY]}" + tra(USER.CharRef["name"]) + "{/color}")

        if TARGET is not None:
            Assert("TARGET_NAME" in ResultString, "TARGET is not none for a log string but TARGET_NAME is not in the string")
            if TARGET.BattleSide == 0:
                ResultString = ResultString.replace("TARGET_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ALLY]}" + tra(TARGET.CharRef["name"]) + "{/color}")
            else:
                ResultString = ResultString.replace("TARGET_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ENEMY]}" + tra(TARGET.CharRef["name"]) + "{/color}")
        
        if PROTECTOR is not None:
            Assert("PROTECTOR_NAME" in ResultString, "PROTECTOR is not none for a log string but PROTECTOR_NAME is not in the string")
            if PROTECTOR.BattleSide == 0:
                ResultString = ResultString.replace("PROTECTOR", "{color=[BATTLE_COLORS_LOG.NAME_ALLY]}" + tra(PROTECTOR.CharRef["name"]) + "{/color}")
            else:
                ResultString = ResultString.replace("PROTECTOR", "{color=[BATTLE_COLORS_LOG.NAME_ENEMY]}" + tra(PROTECTOR.CharRef["name"]) + "{/color}")

        if SKILL_NAME is not None:
            ResultString = ResultString.replace("SKILL_NAME", "{color=[BATTLE_COLORS_LOG.NAME_SKILL]}" + tra(SKILL_NAME) + "{/color}")

        if ITEM_NAME is not None:
            ResultString = ResultString.replace("ITEM_NAME", "{color=[BATTLE_COLORS_LOG.NAME_ITEM]}" + tra(ITEM_NAME) + "{/color}")

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
        if SUM_OF_ALLIED_HP is not None:
            ResultString = ResultString.replace("SUM_OF_ALLIED_HP", "{color=[BATTLE_COLORS_LOG.RESTORE_HEALTH]}" + str(SUM_OF_ALLIED_HP) + "{/color}")

        BattleScene.LogEntries.append(ResultString)
        return

