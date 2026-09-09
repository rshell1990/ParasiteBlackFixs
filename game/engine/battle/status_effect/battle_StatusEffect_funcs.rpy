init python:
    def Battle_ApplyStatusEffect(TargetChar = None, StatusEffect = None, CastOnEnemy = False):
        if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
            if Battle_HasStatusEffect(TargetChar, "immunity"):
                Battle_AddLogEntry_Autoformat(
                    TARGET = TargetChar,
                    SKILL_NAME = StatusEffect.EffectName,
                    String = tra(_("SKILL_NAME cannot be applied to TARGET_NAME because TARGET_NAME is immune to debuffs!")))
                return
        if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
            if Battle_HasStatusEffect(TargetChar, "curse"):
                Battle_AddLogEntry_Autoformat(
                    TARGET = TargetChar,
                    SKILL_NAME = StatusEffect.EffectName,
                    String = tra(_("SKILL_NAME cannot be applied to TARGET_NAME because TARGET_NAME is cursed!")))
                return

        if CastOnEnemy == True:
            StatusEffect.TickOn = StatusEffect.TickOn_Enemy
        else:
            StatusEffect.TickOn = StatusEffect.TickOn_Ally

        StatusEffect.Owner_BattleChar = TargetChar

        # if a char is about to 'protect' another char, remove char's 'protect' from another char if present
        if getattr(StatusEffect, "StatusEffectID", None) == "protect":
            if StatusEffect.AllowMultiple == False:
                AliveSideChars = Battle_GetAliveCharsOnSide(StatusEffect.Owner_BattleChar.BattleSide)
                AliveSideChars.remove(TargetChar)
                for BattleChar in AliveSideChars:
                    for PresentAllyStatusEffect in reversed(BattleChar.StatusEffects):
                        if PresentAllyStatusEffect.StatusEffectID == "protect":
                            if PresentAllyStatusEffect.ProtectedBy == StatusEffect.ProtectedBy:
                                BattleChar.StatusEffects.remove(PresentAllyStatusEffect)

        # case 1, effect with this stacking id present, do stacking
        for PresentStatusEffect in reversed(TargetChar.StatusEffects):
            if getattr(PresentStatusEffect, "StatusEffectID", None) == getattr(StatusEffect, "StatusEffectID", None):
                # stacking just add duration
                if PresentStatusEffect.StackingMethod == BATTLE_STATUS_EFFECT_STACKING.ADDITIVE:
                    PresentStatusEffect.Duration += StatusEffect.Duration
                # stacking replaces
                elif PresentStatusEffect.StackingMethod == BATTLE_STATUS_EFFECT_STACKING.REPLACE:
                    # better wins in case of same ID
                    if hasattr(StatusEffect, "IsBetterThanAnotherEffect"):
                        if StatusEffect.IsBetterThanAnotherEffect(PresentStatusEffect):
                            TargetChar.StatusEffects.remove(PresentStatusEffect)
                            TargetChar.StatusEffects.append(StatusEffect)
                    else:
                        TargetChar.StatusEffects.remove(PresentStatusEffect)
                        TargetChar.StatusEffects.append(StatusEffect)
                elif PresentStatusEffect.StackingMethod == BATTLE_STATUS_EFFECT_STACKING.ADD_AS_NEW:
                    StatusEffect.StatusEffectID += str(id(StatusEffect))
                    TargetChar.StatusEffects.append(StatusEffect)
                return
    
        # case 2, effect with this stacking id is not present, add
        TargetChar.StatusEffects.append(StatusEffect)
        return

    def Battle_RemoveAllDebuffs(TargetChar):
        for StatusEffect in reversed(TargetChar.StatusEffects):
            if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                TargetChar.StatusEffects.remove(StatusEffect)
        return

    def Battle_RemoveAllBuffs(TargetChar):
        for StatusEffect in reversed(TargetChar.StatusEffects):
            if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                TargetChar.StatusEffects.remove(StatusEffect)
        return

    def Battle_RemoveStatusEffect(TargetChar, EffectID):
        for StatusEffect in reversed(TargetChar.StatusEffects):
            if StatusEffect.StatusEffectID == EffectID:
                TargetChar.StatusEffects.remove(StatusEffect)
        return

    def GetStatusEffectDesc(StatusEffect):
        TextLines = []

        # Safely extract EffectName with a fallback string
        effect_name = getattr(StatusEffect, "EffectName", "Status Effect")
        TextLines.append(tra(effect_name))

        # Safely call GetDesc if available
        if hasattr(StatusEffect, "GetDesc"):
            desc = StatusEffect.GetDesc()
            if desc:
                TextLines.append("\n" + desc)

        # Safely check SourceName
        source_name = getattr(StatusEffect, "SourceName", None)
        if source_name is not None:
            TextLines.append("\n" + tra(_("Source:")) + " " + tra(source_name))

        # Safely check StatusEffectID for Developer mode
        if config.developer:
            effect_id = getattr(StatusEffect, "StatusEffectID", StatusEffect.__class__.__name__)
            TextLines.append("\n{color=#949494}(DEV) Status effect ID: %s{/color}" % effect_id)

        return "".join(TextLines)

    def Battle_TickStatusEffectDuration(ActingSide, AtEnd=True):
        # Handle both integer side indices and character lists
        if isinstance(ActingSide, int):
            left_party = getattr(BattleScene, "CharList_Left", getattr(BattleScene, "Party_Left", []))
            right_party = getattr(BattleScene, "CharList_Right", getattr(BattleScene, "Party_Right", []))
            char_list = left_party if ActingSide == 0 else right_party
        else:
            char_list = ActingSide

        for BattleChar in char_list:
            for StatusEffect in list(BattleChar.StatusEffects):
                # Check permanence safely
                if getattr(StatusEffect, "IsPermanent", getattr(StatusEffect, "Permanent", False)):
                    continue

                # Check tick timing safely (0 = End, 1 = Start)
                tick_timing = getattr(StatusEffect, "TickOn", 0)
                target_timing = 0 if AtEnd else 1

                if tick_timing == target_timing:
                    if hasattr(StatusEffect, "TickDuration"):
                        StatusEffect.TickDuration(AtEnd=AtEnd)

    def Battle_PlacePermaStatusEffects():
        for Side in range(2):
            AllSideChars = Battle_GetAliveCharsOnSide(Side)
            for BattleChar in AllSideChars:
                for SlotID in EQP_SLOTS.ALL:
                    if BattleChar.CharRef[SlotID] is not None:
                        ItemID = BattleChar.CharRef[SlotID]
                        Assert(ItemID in all_items, "wtf? item id %s not found in all_items" % ItemID)
                        ItemDef = all_items[ItemID]
                        if "battle_perma_effects" in ItemDef:
                            if ItemDef["battle_perma_effects"] is not None:
                                EffIDs = ItemDef["battle_perma_effects"]
                                for EffID in EffIDs:
                                    if EffID == "FaymoreBladeRegenParty":
                                        BladeStatEffID = "health_regen_curr_perma_faymore_blade"
                                        for Char in AllSideChars:
                                            if not Battle_HasStatusEffect(Char, BladeStatEffID):
                                                Battle_ApplyStatusEffect(
                                                    TargetChar = Char, 
                                                    StatusEffect = BattleStatusEff_RegenHealthCurrPermanent(
                                                        RestoreVal = 0.05,
                                                        SourceName = tra(_("Faymore blade")),
                                                        StatusEffectID = BladeStatEffID,
                                                    )
                                                )
                                    elif EffID == "FaymoreArmorRegenWearer":
                                        Battle_ApplyStatusEffect(
                                            TargetChar = BattleChar, 
                                            StatusEffect = BattleStatusEff_RegenHealthCurrPermanent(
                                                RestoreVal = 0.1, 
                                                SourceName = tra(_("Faymore armor")), 
                                                StatusEffectID = "health_regen_curr_perma_faymore_armor",
                                            )
                                        )


    def Battle_StatusEffect_OnTurnStart(Side = 0):
        for BattleChar in Battle_GetAliveCharsOnSide(Side):
            for StatusEffect in reversed(BattleChar.StatusEffects):
                if hasattr(StatusEffect, "OnTurnStart"):
                    # you can get killed during this for loop hence isalive check
                    # ^ im not sure that sentence makes sense? 
                    # but the check is necessary bc crashes otherwise
                    if BattleChar.IsAlive:
                        StatusEffect.OnTurnStart()
                        Battle_LoopStep(0.2)

    def Battle_GetIncomingDamageMod(BattleChar):
        DamageMod_In = 1.0
        for StatusEffect in BattleChar.StatusEffects:
            DamageMod_In *= getattr(StatusEffect, "DamageRecieved_Mod", 1.0)
        return round(max(DamageMod_In, 0.1), 1)

    def Battle_GetOutgoingDamageMod(BattleChar):
        DamageMod_Out = 1.0
        for StatusEffect in BattleChar.StatusEffects:
            DamageMod_Out *= getattr(StatusEffect, "DamageDealt_Mod", 1.0)
        return DamageMod_Out

    def Battle_HasStatusEffect(BattleChar, EffectID):
        ####Checks if a character has a specific status effect, safely handling custom effect state objects.
        if not hasattr(BattleChar, "StatusEffects") or not BattleChar.StatusEffects:
            return False

        for StatusEffect in BattleChar.StatusEffects:
            # Safely check StatusEffectID, ID, or class/type name
            effect_id = getattr(StatusEffect, "StatusEffectID", getattr(StatusEffect, "ID", None))
            
            if effect_id == EffectID:
                return True
            # Fallback check if EffectID matches the class name directly
            elif StatusEffect.__class__.__name__ == EffectID:
                return True

        return False

    def Battle_GetStatusEffect(BattleChar, EffectID):
        for StatusEffect in BattleChar.StatusEffects:
            if getattr(StatusEffect, "StatusEffectID", None) == EffectID:
                return StatusEffect

    def Battle_HasAnyDebuff(BattleChar):
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                return True
        return False

    def Battle_HasAnyBuff(BattleChar):
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                return True
        return False

