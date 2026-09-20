init python:
    import math
    import random

    def Battle_QueueFloatingTextOnChar(BattleChar, Value, Kind = 0):
        BattleSceneObj = getattr(store, "BattleScene", None)
        if BattleSceneObj is None:
            return
        if not hasattr(BattleSceneObj, "FloatingTextQueue"):
            BattleSceneObj.FloatingTextQueue = []
        BattleSceneObj.FloatingTextQueue.append((BattleChar, Value, Kind))

    def Battle_DealDamage(TargetBattleChar, Value, IgnoreArmor = False, PierceInvincibility = False, IsCrit = False, FloatingTextKind = 0):
        if not TargetBattleChar:
            return

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

        current_hp = getattr(TargetBattleChar, "Health", 0)

        # under willpower ya cant go below 1hp
        if Battle_HasStatusEffect(TargetBattleChar, "willpower"):
            TargetBattleChar.Health = max(current_hp - DamageValue, 1)
        else:
            TargetBattleChar.Health = max(current_hp - DamageValue, 0)

        # changes floating text kind
        if IsCrit:
            Battle_QueueFloatingTextOnChar(TargetBattleChar, DamageValue, Kind = 2)
        else:
            Battle_QueueFloatingTextOnChar(TargetBattleChar, DamageValue, Kind = FloatingTextKind)

        # process all battle death-related stuff
        if getattr(TargetBattleChar, "Health", 0) == 0:
            Battle_LoopStep(0.15)

            battle_scene = getattr(store, "BattleScene", None)
            if battle_scene:
                if getattr(battle_scene, "SelectedLeft", None) == TargetBattleChar:
                    battle_scene.SelectedLeft = None
                if getattr(battle_scene, "SelectedRight", None) == TargetBattleChar:
                    battle_scene.SelectedRight = None

            Battle_PlayCharSkinSound("Char_Die", TargetBattleChar, Voice = True)

            Battle_AddLogEntry_Autoformat(
                TARGET = TargetBattleChar,
                String = tra(_("TARGET_NAME {color=[BATTLE_COLORS_LOG.BATTLE_STATUS]}is defeated!{/color}")))

            if hasattr(store, "TooltipClearUI"):
                TooltipClearUI()

            TargetBattleChar.IsAlive = False
            target_side = getattr(TargetBattleChar, "BattleSide", 0)
            RemainingAliveAlliesOfDead = Battle_GetAliveCharsOnSide(target_side)

            # delete protect status eff
            for Char in RemainingAliveAlliesOfDead:
                for StatusEffect in reversed(getattr(Char, "StatusEffects", [])):
                    if getattr(StatusEffect, "StatusEffectID", None) == "protect":
                        if getattr(StatusEffect, "ProtectedBy", None) == TargetBattleChar:
                            Char.StatusEffects.remove(StatusEffect)

            # auto-select alive char
            if len(RemainingAliveAlliesOfDead) > 0:
                next_char = RemainingAliveAlliesOfDead.pop()
                if target_side == 0:
                    Battle_SelectLeftChar(next_char)
                elif target_side == 1:
                    Battle_SelectRightChar(next_char)

            sprite_tag = getattr(TargetBattleChar, "SpriteTag", None)
            renpy.with_statement(Dissolve(0.0))
            if sprite_tag:
                renpy.hide(sprite_tag)

            fast_loop = getattr(persistent, "BattlePref_FastLoop", False)
            if fast_loop:
                renpy.with_statement(Dissolve(0.05))
            else:
                renpy.with_statement(Dissolve(0.5))

            ### achievement
            if target_side == 1:
                store._total_enemies_killed = getattr(store, "_total_enemies_killed", 0) + 1
            
            total_killed = getattr(store, "_total_enemies_killed", 0)
            can_unlock = getattr(store, "can_unlock_achievement", None)
            do_unlock = getattr(store, "unlock_achievement", None)
            
            if total_killed > 100 and can_unlock and can_unlock("BLOODTHIRSTY_ARENT_WE"):
                if do_unlock:
                    do_unlock("BLOODTHIRSTY_ARENT_WE")
        return
    
    def Battle_GetArmorDamageReduction(Value, Target):
        armor = getattr(Target, "Armor", 0) if Target else 0
        return round(Value * (1 - (0.99 * (1 - math.exp(-0.023 * armor)))))

    def Battle_GetIncomingDamageMod(Target):
        DamageMod = 1.0
        for StatusEffect in getattr(Target, "StatusEffects", []):
            DamageMod *= getattr(StatusEffect, "DamageReceived_Mod", getattr(StatusEffect, "DamageRecieved_Mod", 1.0))
        return DamageMod
    
    def Battle_BCharDamageRoll(AttackingBattleChar, Mod = 1.0):
        DamageTuple = Battle_GetBattleCharDamageSpread(AttackingBattleChar, Mod = Mod)
        return random.randint(DamageTuple[0], DamageTuple[1])
    
    def Battle_GetBattleCharDamageSpread(Char, Mod = 1.0):
        base_dmg = getattr(Char, "Damage", 0) if Char else 0
        MinVal = int(base_dmg * 0.75 * Mod)
        MaxVal = int(base_dmg * 1.25 * Mod)
        return (MinVal, MaxVal)

    def Battle_GetPBCharDamageSpread(PBChar, Mod = 1.0):
        base_dmg = PBChar.get("Damage", 0) if isinstance(PBChar, dict) else 0
        MinVal = int(base_dmg * 0.75 * Mod)
        MaxVal = int(base_dmg * 1.25 * Mod)
        return (MinVal, MaxVal)

    ## for ui
    def Battle_GetBCharDmgTupleAsText(BattleChar, Mod = 1.0):
        SpreadTup = Battle_GetBattleCharDamageSpread(BattleChar, Mod)
        return f"{SpreadTup[0]}-{SpreadTup[1]}"

    def Battle_GetPBCharDmgTupleAsText(PBCharID, Mod = 1.0):
        world_chars = getattr(store, "worldChars", {})
        pb_char = world_chars.get(PBCharID, {})
        SpreadTup = Battle_GetPBCharDamageSpread(pb_char, Mod)
        return f"{SpreadTup[0]}-{SpreadTup[1]}"