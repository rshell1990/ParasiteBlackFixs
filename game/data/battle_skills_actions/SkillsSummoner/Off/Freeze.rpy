init python:

    BaseStatusClass = getattr(store, "BattleStatusEffect", renpy.python.RevertableObject)

    class FreezeStatusEffect(BaseStatusClass):
        def __init__(self, target=None, duration=1):
            if hasattr(super(FreezeStatusEffect, self), "__init__"):
                super(FreezeStatusEffect, self).__init__()

            self.ID = "freeze"
            self.StatusEffectID = "freeze"
            self.DisplayName = _("Frozen")
            self.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
            self.Icon = "images/battle_status_icons/freeze.webp"
            self.IsPermanent = False
            self.Owner = target

            self.Duration = int(duration)
            self.MaxDuration = int(duration)
            self._ticked_this_turn = False

        def StepTurn(self):
            """Executes once per side turn round."""
            if self._ticked_this_turn:
                return
            self._ticked_this_turn = True

            self.Duration -= 1

            if self.Duration > 0:
                if hasattr(store, "Battle_ShowFloatingText") and self.Owner:
                    Battle_ShowFloatingText(self.Owner, _("Frozen!"))
            else:
                self.RemoveSelf()

        def OnTurnStart(self):
            # Reset tick guard at start of turn
            self._ticked_this_turn = False
            self.StepTurn()

        def OnTurnEnd(self):
            self._ticked_this_turn = False

        def TickDuration(self, *args, **kwargs):
            # Fallback tick pass for MainLoop execution
            self.StepTurn()

        def RemoveSelf(self):
            owner = getattr(self, "Owner", None)

            # 1. Clear status directly from Owner
            if owner and hasattr(owner, "StatusEffects"):
                owner.StatusEffects = [s for s in owner.StatusEffects if getattr(s, "ID", None) != "freeze"]

            # 2. Clear status from all active battle characters
            if hasattr(store, "BattleScene") and store.BattleScene:
                for char in store.BattleScene.BattleChars[0] + store.BattleScene.BattleChars[1]:
                    if hasattr(char, "StatusEffects"):
                        char.StatusEffects = [s for s in char.StatusEffects if getattr(s, "ID", None) != "freeze"]
                        if owner is None or char == owner:
                            owner = char

            if hasattr(store, "Battle_ShowFloatingText") and owner:
                Battle_ShowFloatingText(owner, _("Thawed!"))

            if hasattr(renpy, "restart_interaction"):
                renpy.restart_interaction()


    @RegisterBattleSkill("Freeze")
    class BattleSkill_Freeze(BattleSkill):
        DisplayName = _("Freeze")
        Icon = "images/battle_skill_icons/freeze.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 35

        DurationByLevel = {1: 1, 2: 1, 3: 2, 4: 3}
        FreezeChanceByLevel = {1: 0.50, 2: 0.70, 3: 0.85, 4: 1.00}

        def CanExecute(self):
            if not super(BattleSkill_Freeze, self).CanExecute():
                return False
            return True

        def Execute(self, Target):
            Caster = self.Owner_BattleChar
            TargetDuration = self.DurationByLevel[self.Level]
            ProcChance = self.FreezeChanceByLevel[self.Level]

            if renpy.random.random() <= ProcChance:
                # Clear existing freeze effects on target
                if hasattr(Target, "StatusEffects") and isinstance(Target.StatusEffects, list):
                    Target.StatusEffects = [s for s in Target.StatusEffects if getattr(s, "ID", None) != "freeze"]

                # Instantiate and attach directly to target
                StatusObj = FreezeStatusEffect(target=Target, duration=TargetDuration)
                Target.StatusEffects.append(StatusObj)

                if hasattr(store, "Battle_ShowFloatingText"):
                    Battle_ShowFloatingText(Target, _("Frozen!"))
            else:
                if hasattr(store, "Battle_ShowFloatingText"):
                    Battle_ShowFloatingText(Target, _("Resisted!"))
            return

        def GetDesc(self, DescLevel = 1):
            Turns = self.DurationByLevel[DescLevel]
            Chance = round(self.FreezeChanceByLevel[DescLevel] * 100)
            return tra(_("Attempts to freeze an enemy (%s%% chance) for %s turn(s). While frozen, the target cannot act.")) % (Chance, Turns)