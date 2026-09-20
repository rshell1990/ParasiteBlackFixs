init python:
    @RegisterBattleItemAction("PotionHeal")
    class BattleItemAction_PotionHeal(BattleSkill):
        ValidTargets = BATTLE_TARGETS.SELF
        SpendTurn = False

        def __init__(self, Owner_BattleChar = None, ItemID = None):
            super().__init__(Owner_BattleChar = Owner_BattleChar)            
            self.ItemID = ItemID
            self.ItemName = all_items[self.ItemID]["name"]
            self.RestoreBaseAmount = all_items[self.ItemID]["on_use_battle_arg1"]

        def Execute(self, Target):
            Battle_ScheduledItemUse(
                SourceAction = self,
                UseTarget = self.Owner_BattleChar,
                SoundUse_CustomList = soundLib["usePotion"],
                GenericLogLine = False,
                Effects_OnTarget = [BattleEffect_RestoreHealth(RestoreValue = self.RestoreBaseAmount)])
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                ITEM_NAME = all_items[self.ItemID]["name"],
                HEALTH_RECOVERED = Battle_GetHealthRecoveredModifiedAndClamped(self.Owner_BattleChar, self.RestoreBaseAmount),
                String = tra(_("USER_NAME drinks ITEM_NAME, restoring HEALTH_RECOVERED health!")))
            return

        def CanExecute(self):
            return (True if self.Owner_BattleChar.Health < self.Owner_BattleChar.HealthMax else False)

        def GetDesc(self):
            Result = []
            AmountThatWillPotentiallyBeRecovered = round(Battle_GetHealthRecoveryMod(self.Owner_BattleChar) * self.RestoreBaseAmount)

            # single val
            if AmountThatWillPotentiallyBeRecovered == self.RestoreBaseAmount:
                Result.append(Item_BonusColor + tra(_("Restores health on use: %s")) % self.RestoreBaseAmount + "{/color}")

            # double val
            else:
                Result.append(Item_BonusColor + tra(_("Restores health on use: %s (Base %s)")) % (AmountThatWillPotentiallyBeRecovered, self.RestoreBaseAmount) + "{/color}")

            return "".join(Result)
######################################################################
    @RegisterBattleItemAction("PotionEther")
    class BattleItemAction_PotionEther(BattleSkill):
        ValidTargets = BATTLE_TARGETS.SELF
        SpendTurn = False

        def __init__(self, Owner_BattleChar = None, ItemID = None):
            super().__init__(Owner_BattleChar = Owner_BattleChar)            
            self.ItemID = ItemID
            self.ItemName = all_items[self.ItemID]["name"]
            self.RestoreBaseAmount = all_items[self.ItemID]["on_use_battle_arg1"]

        def Execute(self, Target):
            Battle_ScheduledItemUse(
                SourceAction = self,
                UseTarget = self.Owner_BattleChar,
                SoundUse_CustomList = soundLib["usePotion"],
                GenericLogLine = False,
                Effects_OnTarget = [BattleEffect_RestoreEnergyOrMana(RestoreValue = self.RestoreBaseAmount)])
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                ITEM_NAME = all_items[self.ItemID]["name"],
                RESTORED_AMOUNT = self.RestoreBaseAmount,
                String = tra(_("USER_NAME drinks ITEM_NAME, restoring RESTORED_AMOUNT Magic/Stamina!")))
            return

        def CanExecute(self):
            resource = "Mana" if self.Owner_BattleChar.CharRef.get("is_mage", False) else "Energy"
            return getattr(self.Owner_BattleChar, resource) < getattr(self.Owner_BattleChar, resource + "Max")

        def GetDesc(self):
            Result = []
            return Item_BonusColor + tra(_("Restores Magic/Stamina on use: %s")) % self.RestoreBaseAmount + "{/color}"
######################################################################
    @RegisterBattleItemAction("PotionElixer")
    class BattleItemAction_PotionElixer(BattleSkill):
        ValidTargets = BATTLE_TARGETS.SELF
        SpendTurn = False

        def __init__(self, Owner_BattleChar = None, ItemID = None):
            super().__init__(Owner_BattleChar = Owner_BattleChar)            
            self.ItemID = ItemID
            self.ItemName = all_items[self.ItemID]["name"]
            self.RestoreBaseAmount = all_items[self.ItemID]["on_use_battle_arg1"]

        def Execute(self, Target):
            Battle_ScheduledItemUse(
                SourceAction = self,
                UseTarget = self.Owner_BattleChar,
                SoundUse_CustomList = soundLib["usePotion"],
                GenericLogLine = False,
                Effects_OnTarget = [
                    BattleEffect_RestoreHealth(RestoreValue = self.RestoreBaseAmount),
                    BattleEffect_RestoreEnergyOrMana(RestoreValue = self.RestoreBaseAmount),
                ])
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                ITEM_NAME = all_items[self.ItemID]["name"],
                RESTORED_AMOUNT = self.RestoreBaseAmount,
                String = tra(_("USER_NAME drinks ITEM_NAME, restoring RESTORED_AMOUNT HP and Magic/Stamina!")))
            return

        def CanExecute(self):
            resource = "Mana" if self.Owner_BattleChar.CharRef.get("is_mage", False) else "Energy"
            return (
                self.Owner_BattleChar.Health < self.Owner_BattleChar.HealthMax
                or getattr(self.Owner_BattleChar, resource) < getattr(self.Owner_BattleChar, resource + "Max")
            )

        def GetDesc(self):
            Result = []
            return Item_BonusColor + tra(_("Restores HP and Magic/Stamina on use: %s")) % self.RestoreBaseAmount + "{/color}"
        ######################################################################
    @RegisterBattleItemAction("PotionRevive")
    class BattleItemAction_PotionRevive(BattleSkill):
        ValidTargets = BATTLE_TARGETS.ALLY_NOT_SELF
        AllowDeadTargets = True
        SpendTurn = False

        def __init__(self, Owner_BattleChar = None, ItemID = None):
            super().__init__(Owner_BattleChar = Owner_BattleChar)            
            self.ItemID = ItemID
            self.ItemName = all_items[self.ItemID]["name"]
            self.RestoreBaseAmount = all_items[self.ItemID]["on_use_battle_arg1"]

        def Execute(self, Target):
            Target.IsAlive = True
            Battle_RunCharAnim(Target, "idle")
            Battle_ScheduledItemUse(
                SourceAction = self,
                UseTarget = Target,
                SoundUse_CustomList = soundLib["usePotion"],
                GenericLogLine = False,
                Effects_OnTarget = [BattleEffect_RestoreHealth(RestoreValue = self.RestoreBaseAmount)])
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                TARGET = Target,
                ITEM_NAME = all_items[self.ItemID]["name"],
                HEALTH_RECOVERED = Battle_GetHealthRecoveredModifiedAndClamped(Target, self.RestoreBaseAmount),
                String = tra(_("USER_NAME uses ITEM_NAME on TARGET_NAME, restoring HEALTH_RECOVERED health!")))
            return

        def CanExecute(self):
            return any(not BattleChar.IsAlive for BattleChar in BattleScene.BattleChars[self.Owner_BattleChar.BattleSide] if BattleChar != self.Owner_BattleChar)

        def GetDesc(self):
            return Item_BonusColor + tra(_("Revives a fallen ally with %s health.")) % self.RestoreBaseAmount + "{/color}"
######################################################################
    @RegisterBattleItemAction("GoblinBomb")
    class BattleItemAction_GoblinBomb(BattleSkill):
        SpendTurn = False
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        DamageAmt = 100

        def __init__(self, Owner_PBCharID = None, Owner_BattleChar = None, ItemID = None):
            super().__init__(Owner_BattleChar = Owner_BattleChar, Owner_PBCharID = Owner_PBCharID)

            self.ItemID = ItemID
            self.ItemName = all_items[self.ItemID]["name"]

        def Execute(self, Target):
            Battle_ScheduledItemUse(
                CharSkinAnimToPlay = "attack",
                SourceAction = self,
                UseTarget = Target,
                SoundUse_CustomList = ["audio/battle/swordSwing/hSword-01.ogg", "audio/battle/swordSwing/hSword-02.ogg", "audio/battle/swordSwing/hSword-03.ogg", "audio/battle/swordSwing/hSword-04.ogg", "audio/battle/swordSwing/hSword-05.ogg"],
                SoundImpact_CustomList = ["audio/battle/explosion/explosion1.ogg", "audio/battle/explosion/explosion2.ogg", "audio/battle/explosion/explosion3.ogg"],
                TargetVFXID = self.Owner_BattleChar.BattleSkin.BasicAttackImpactImageID,
                GenericLogLine = False,
                Effects_OnTarget = [BattleEffect_DealDamageFlat(DamageValue = self.DamageAmt)])

            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                TARGET = Target,
                DAMAGE_AMOUNT = Battle_GetArmorDamageReduction(round(self.DamageAmt * Battle_GetIncomingDamageMod(Target)), Target),
                ITEM_NAME = self.ItemName,
                String = tra(_("USER_NAME throws ITEM_NAME at TARGET_NAME, dealing DAMAGE_AMOUNT damage!")))
            return
    
        def GetDesc(self):
            Result = []

            Result.append(Item_MalusColor + tra(_("Throw to deal damage to a single enemy: %s")) % self.DamageAmt + "{/color}")

            return "".join(Result)
    @RegisterBattleItemAction("GoblinScrapnelBomb")
    class BattleItemAction_GoblinScrapnelBomb(BattleSkill):
        SpendTurn = False
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        DamageAmt = 75

        def __init__(self, Owner_PBCharID = None, Owner_BattleChar = None, ItemID = None):
            super().__init__(Owner_BattleChar = Owner_BattleChar, Owner_PBCharID = Owner_PBCharID)

            self.ItemID = ItemID
            self.ItemName = all_items[self.ItemID]["name"]

        def Execute(self, Target):
            Battle_ScheduledItemUse(
                CharSkinAnimToPlay = "attack",
                SourceAction = self,
                UseTarget = self.ValidTargets,
                SoundUse_CustomList = ["audio/battle/swordSwing/hSword-01.ogg", "audio/battle/swordSwing/hSword-02.ogg", "audio/battle/swordSwing/hSword-03.ogg", "audio/battle/swordSwing/hSword-04.ogg", "audio/battle/swordSwing/hSword-05.ogg"],
                SoundImpact_CustomList = ["audio/battle/explosion/explosion1.ogg", "audio/battle/explosion/explosion2.ogg", "audio/battle/explosion/explosion3.ogg"],
                TargetVFXID = self.Owner_BattleChar.BattleSkin.BasicAttackImpactImageID,
                GenericLogLine = False,
                Effects_OnTarget = [BattleEffect_DealDamageFlat(DamageValue = self.DamageAmt)])

            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                DAMAGE_AMOUNT = Battle_GetArmorDamageReduction(round(self.DamageAmt * Battle_GetIncomingDamageMod(Target)), Target),
                ITEM_NAME = self.ItemName,
                String = tra(_("USER_NAME throws ITEM_NAME at All Enemies, dealing DAMAGE_AMOUNT damage!")))
            return
    
        def GetDesc(self):
            Result = []

            Result.append(Item_MalusColor + tra(_("Throw to deal damage to all enemies: %s")) % self.DamageAmt + "{/color}")

            return "".join(Result)
######################################################################
    @RegisterBattleItemAction("BattleFoodHeal")
    class BattleItemAction_BattleFoodHeal(BattleSkill):
        ValidTargets = BATTLE_TARGETS.SELF
        SpendTurn = False
        
        def __init__(self, Owner_BattleChar = None, ItemID = None):
            super().__init__(Owner_BattleChar = Owner_BattleChar)

            self.ItemID = ItemID
            self.ItemName = all_items[self.ItemID]["name"]

            self.RestoreBaseAmount = all_items[self.ItemID]["on_use_battle_arg1"]

        def Execute(self, Target):
            Battle_ScheduledItemUse(
                SourceAction = self,
                UseTarget = self.Owner_BattleChar,
                SoundUse_CustomList = soundLib["chew"],
                GenericLogLine = False,
                Effects_OnTarget = [BattleEffect_RestoreHealth(RestoreValue = self.RestoreBaseAmount)])
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                ITEM_NAME = self.ItemName,
                HEALTH_RECOVERED = Battle_GetHealthRecoveredModifiedAndClamped(self.Owner_BattleChar, self.RestoreBaseAmount),
                String = tra(_("USER_NAME eats ITEM_NAME, restoring HEALTH_RECOVERED health!")))
            return

        def CanExecute(self):
            return (True if self.Owner_BattleChar.Health < self.Owner_BattleChar.HealthMax else False)
    
        def GetDesc(self):
            Result = []
            AmountThatWillPotentiallyBeRecovered = round(Battle_GetHealthRecoveryMod(self.Owner_BattleChar) * self.RestoreBaseAmount)

            # single val
            if AmountThatWillPotentiallyBeRecovered == self.RestoreBaseAmount:
                Result.append(Item_BonusColor + tra(_("Restores health on use: %s")) % self.RestoreBaseAmount + "{/color}")

            # double val
            else:
                Result.append(Item_BonusColor + tra(_("Restores health on use: %s (Base %s)")) % (AmountThatWillPotentiallyBeRecovered, self.RestoreBaseAmount) + "{/color}")

            return "".join(Result)

######################################################################
    @RegisterBattleItemAction("GoblinStims")
    class BattleItemAction_GoblinStims(BattleSkill):
        ValidTargets = BATTLE_TARGETS.SELF
        SpendTurn = False
        RestoreBaseAmount = 20

        def __init__(self, Owner_PBCharID = None, Owner_BattleChar = None, ItemID = None):
            super().__init__(Owner_BattleChar = Owner_BattleChar, Owner_PBCharID = Owner_PBCharID)

            self.ItemID = ItemID
            self.ItemName = all_items[self.ItemID]["name"]

        def Execute(self, Target):
            Battle_ScheduledItemUse(
                SourceAction = self,
                UseTarget = self.Owner_BattleChar,
                SoundUse_CustomList = soundLib["usePotion"],
                GenericLogLine = False,
                Effects_OnTarget = [BattleEffect_RestoreEnergy(RestoreValue = 20)])
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                ITEM_NAME = self.ItemName,
                ENERGY_RECOVERED = Battle_GetEnergyRecoveredModifiedAndClamped(self.Owner_BattleChar, 20),
                String = tra(_("USER_NAME uses ITEM_NAME, restoring ENERGY_RECOVERED energy!")))
            return
        
        def CanExecute(self):
            return (True if self.Owner_BattleChar.Energy < self.Owner_BattleChar.EnergyMax else False)
    
        def GetDesc(self):
            Result = []
            if self.Owner_BattleChar is not None:
                AmountThatWillPotentiallyBeRecovered = round(Battle_GetEnergyRecoveryMod(self.Owner_BattleChar) * self.RestoreBaseAmount)
            else:
                AmountThatWillPotentiallyBeRecovered = self.RestoreBaseAmount

            # single val
            if AmountThatWillPotentiallyBeRecovered == self.RestoreBaseAmount:
                Result.append(Item_BonusColor + tra(_("Restores energy on use: %s")) % self.RestoreBaseAmount + "{/color}")

            # double val
            else:
                Result.append(Item_BonusColor + tra(_("Restores energy on use: %s (Base %s)")) % (AmountThatWillPotentiallyBeRecovered, self.RestoreBaseAmount) + "{/color}")

            return "".join(Result)

######################################################################
    @RegisterBattleItemAction("RazaSeed")
    class BattleItemAction_RazaSeed(BattleSkill):
        ValidTargets = BATTLE_TARGETS.SELF
        SpendTurn = False
        PoisonHours = 6

        def __init__(self, Owner_BattleChar = None, ItemID = None):
            super().__init__(Owner_BattleChar = Owner_BattleChar)

            self.ItemID = ItemID
            self.ItemName = all_items[self.ItemID]["name"]

        def Execute(self, Target):
            Battle_ScheduledItemUse(
                SourceAction = self,
                UseTarget = self.Owner_BattleChar,
                SoundUse_CustomList = soundLib["chew"],
                GenericLogLine = False,
                Effects_OnTarget = [BattleEffect_ApplyStatusOnAlly(StatusEffect = BattleStatusEff_RazaSeed())])
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                ITEM_NAME = self.ItemName,
                String = tra(_("USER_NAME eats a ITEM_NAME!")))
            if self.Owner_BattleChar not in BattleScene.PostBattleGlobalPoison:
                BattleScene.PostBattleGlobalPoison[self.Owner_BattleChar] = self.PoisonHours
            else:
                if BattleScene.PostBattleGlobalPoison[self.Owner_BattleChar] < self.PoisonHours:
                    BattleScene.PostBattleGlobalPoison[self.Owner_BattleChar] = self.PoisonHours
            return

        def GetDesc(self):
            Result = []

            Result.append(Item_BonusColor + "%s +%s %s" % (tra(GUI_STAT_NAME_MAP["Strength"]), 1, tra(_("(6 hours)"))) + "{/color}")
            Result.append("\n")
            Result.append(Item_BonusColor + "%s +%s %s" % (tra(GUI_STAT_NAME_MAP["Endurance"]), 1, tra(_("(6 hours)"))) + "{/color}")
            Result.append("\n")
            Result.append(Item_MalusColor + "%s %s %s" % (tra(GUI_STAT_NAME_MAP["Dexterity"]), -2, tra(_("(6 hours)"))) + "{/color}")
            Result.append("\n")
            Result.append(Item_MalusColor + "%s: %s %s / %s (%s %s)" % (tra(_("Poison")), 10, tra(_("damage")), tra(_("hour")), self.PoisonHours, tra(_("hours"))) + "{/color}")


            return "".join(Result)

######################################################################
    @RegisterBattleItemAction("StrangeMeat")
    class BattleItemAction_StrangeMeat(BattleSkill):
        ValidTargets = BATTLE_TARGETS.SELF
        RestoreAmt = 10
        PoisonHours = 24
        SpendTurn = False

        def __init__(self, Owner_BattleChar = None, ItemID = None):
            super().__init__(Owner_BattleChar = Owner_BattleChar)
            self.ItemID = ItemID
            self.ItemName = all_items[self.ItemID]["name"]

        def Execute(self, Target):
            Battle_ScheduledItemUse(
                SourceAction = self,
                UseTarget = self.Owner_BattleChar,
                SoundUse_CustomList = soundLib["chew"],
                GenericLogLine = False,
                Effects_OnTarget = [BattleEffect_RestoreHealth(RestoreValue = self.RestoreAmt)])
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                ITEM_NAME = self.ItemName,
                HEALTH_RECOVERED = Battle_GetHealthRecoveredModifiedAndClamped(self.Owner_BattleChar, self.RestoreAmt),
                String = tra(_("USER_NAME eats a ITEM_NAME, restoring HEALTH_RECOVERED health!")))
            if self.Owner_BattleChar not in BattleScene.PostBattleGlobalPoison:
                BattleScene.PostBattleGlobalPoison[self.Owner_BattleChar] = self.PoisonHours
            else:
                if BattleScene.PostBattleGlobalPoison[self.Owner_BattleChar] < self.PoisonHours:
                    BattleScene.PostBattleGlobalPoison[self.Owner_BattleChar] = self.PoisonHours
            return

        def CanExecute(self):
            return (True if self.Owner_BattleChar.Health < self.Owner_BattleChar.HealthMax else False)

        def GetDesc(self):
            Result = []

            Result.append(Item_BonusColor + tra(_("Restores health on use: %s") % self.RestoreAmt) + "{/color}")
            #Result.append("\n")
            Result.append(Item_MalusColor + "%s: %s / %s (%s %s)" % (tra(_("Poison")), self.RestoreAmt, tra(_("hour")), self.PoisonHours, tra(_("hours"))) + "{/color}")
                        
            return "".join(Result)

########################################################
    @RegisterBattleItemAction("PotionAntidote")
    class BattleItemAction_PotionAntidote(BattleSkill):
        ValidTargets = BATTLE_TARGETS.SELF
        SpendTurn = False

        def __init__(self, Owner_BattleChar = None, ItemID = None):
            super().__init__(Owner_BattleChar = Owner_BattleChar)
            self.ItemID = ItemID
            self.ItemName = all_items[self.ItemID]["name"]

        def Execute(self, Target):
            Battle_ScheduledItemUse(
                SourceAction = self,
                UseTarget = self.Owner_BattleChar,
                SoundUse_CustomList = soundLib["usePotion"],
                GenericLogLine = False,
                Effects_OnTarget = [BattleEffect_Antidote(self.Owner_BattleChar.CharID)])
            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                ITEM_NAME = all_items[self.ItemID]["name"],
                HEALTH_RECOVERED = Battle_GetHealthRecoveredModifiedAndClamped(self.Owner_BattleChar, 30),
                String = tra(_("USER_NAME drinks ITEM_NAME, restoring HEALTH_RECOVERED health!")))
            return

        def CanExecute(self):
            # we can antidote if
            # theres any poison dots on us
            if len([Effect.StatusEffectID for Effect in self.Owner_BattleChar.StatusEffects if Effect.StatusEffectID.startswith("poisondot")]) > 0:
                return True
            # our story char is poisoned
            if StoryCharIsPoisoned(self.Owner_BattleChar.CharID):
                return True
            # we used some item that will have us be poisoned post-battle
            if self.Owner_BattleChar in BattleScene.PostBattleGlobalPoison:
                return True

        def GetDesc(self):
            Result = []
            Result.append(Item_BonusColor + tra(_("Cures poisoning")) + "{/color}")
            return "".join(Result)