init python:
    def Battle_DealDamage(TargetBattleChar, Value, IgnoreArmor = False, PierceInvincibility = False, IsCrit = False, FloatingTextKind = 0):
        # cancel on godmode
        if Battle_HasStatusEffect(TargetBattleChar, "godmode"):
            if not PierceInvincibility:    
                Battle_AddLogEntry_Autoformat(
                    TARGET = TargetBattleChar, 
                    String = tra(_("TARGET_NAME did not suffer any damage because of the invincibility!")))
                return

        Battle_RunCharAnim(TargetBattleChar, "hit")
        Battle_PlayCharSkinSound("Char_BeenHit", TargetBattleChar, Chance = 0.15, Voice = True)

        # ignore armor calc
        if IgnoreArmor:
            DamageValue = Value
        else:
            DamageValue = Battle_GetArmorDamageReduction(Value, TargetBattleChar)

        # under willpower ya cant go below 1hp
        if Battle_HasStatusEffect(TargetBattleChar, "willpower"):
            TargetBattleChar.Health = max(TargetBattleChar.Health - DamageValue, 1)
        else:
            TargetBattleChar.Health = max(TargetBattleChar.Health - DamageValue, 0)

        # changes floating text kind
        if IsCrit:
            Battle_QueueFloatingTextOnChar(TargetBattleChar, DamageValue, Kind = 2)
        else:
            Battle_QueueFloatingTextOnChar(TargetBattleChar, DamageValue, Kind = FloatingTextKind)

        # process all battle death-related stuff
        if TargetBattleChar.Health == 0:
            Battle_LoopStep(0.15)

            if BattleScene.SelectedLeft == TargetBattleChar:
                BattleScene.SelectedLeft = None
            if BattleScene.SelectedRight == TargetBattleChar:
                BattleScene.SelectedRight = None

            Battle_PlayCharSkinSound("Char_Die", TargetBattleChar, Voice = True)

            Battle_AddLogEntry_Autoformat(
                TARGET = TargetBattleChar,
                String = tra(_("TARGET_NAME {color=[BATTLE_COLORS_LOG.BATTLE_STATUS]}is defeated!{/color}")))

            TooltipClear()

            TargetBattleChar.IsAlive = False
            RemainingAliveAlliesOfDead = Battle_GetAliveCharsOnSide(TargetBattleChar.BattleSide)

            # delete protect status eff
            for Char in RemainingAliveAlliesOfDead:
                for StatusEffect in reversed(Char.StatusEffects):
                    if StatusEffect.StatusEffectID == "protect":
                        if StatusEffect.ProtectedBy == TargetBattleChar:
                            Char.StatusEffects.remove(StatusEffect)

            # auto-select alive char
            if len(RemainingAliveAlliesOfDead) > 0:
                if TargetBattleChar.BattleSide == 0:
                    Battle_SelectLeftChar(RemainingAliveAlliesOfDead.pop())
                elif TargetBattleChar.BattleSide == 1:
                    Battle_SelectRightChar(RemainingAliveAlliesOfDead.pop())

            renpy.with_statement(Dissolve(0.0))
            renpy.hide(TargetBattleChar.SpriteTag)
            if persistent.BattlePref_FastLoop:
                renpy.with_statement(Dissolve(0.05))
            else:
                renpy.with_statement(Dissolve(0.5))

            ### achievement
            if TargetBattleChar.BattleSide == 1:
                store._total_enemies_killed += 1
            if store._total_enemies_killed > 100 and can_unlock_achievement("BLOODTHIRSTY_ARENT_WE"):
                unlock_achievement("BLOODTHIRSTY_ARENT_WE")
        return
    
    def Battle_GetArmorDamageReduction(Value, Target):
        return round(Value * (1 - (0.99 * (1 - math.exp(-0.023 * Target.Armor )))))
    
    def Battle_BCharDamageRoll(AttackingBattleChar, Mod = 1.0):
        DamageTuple = Battle_GetBattleCharDamageSpread(AttackingBattleChar, Mod = Mod)
        return random.randint(DamageTuple[0], DamageTuple[1])
    
    def Battle_GetBattleCharDamageSpread(Char, Mod = 1.0):
        MinVal = int(Char.Damage * 0.75 * Mod)
        MaxVal = int(Char.Damage * 1.25 * Mod)
        return (MinVal, MaxVal)
    def Battle_GetPBCharDamageSpread(PBChar, Mod = 1.0):
        MinVal = int(PBChar["Damage"] * 0.75 * Mod)
        MaxVal = int(PBChar["Damage"] * 1.25 * Mod)
        return (MinVal, MaxVal)

    ## for ui
    def Battle_GetBCharDmgTupleAsText(BattleChar, Mod = 1.0):
        SpreadTup = Battle_GetBattleCharDamageSpread(BattleChar, Mod)
        return f"{SpreadTup[0]}-{SpreadTup[1]}"
    def Battle_GetPBCharDmgTupleAsText(PBCharID, Mod = 1.0):
        SpreadTup = Battle_GetPBCharDamageSpread(worldChars[PBCharID], Mod)
        return f"{SpreadTup[0]}-{SpreadTup[1]}"