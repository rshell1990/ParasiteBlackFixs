init python:
    @RegisterBattleSkill("Madness")
    class BattleSkill_Madness(BattleSkill):
        DisplayName = _("Madness")
        Icon = "images/battle_skill_icons/no_icon.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 40

        DurationByLevel = {1: 1, 2: 2, 3: 2, 4: 3}
        ErraticChanceByLevel = {1: 0.45, 2: 0.55, 3: 0.70, 4: 0.85}

        def CanExecute(self):
            if not super(BattleSkill_Madness, self).CanExecute():
                return False
            return True

        def Execute(self, Target):
            Caster = self.Owner_BattleChar
            Duration = self.DurationByLevel[self.Level]
            ErraticChance = self.ErraticChanceByLevel[self.Level]

            # Generic object initialization
            StatusObj = renpy.python.RevertableObject()

            # Core Status Identity
            StatusObj.StatusEffectID = "madness"
            StatusObj.DisplayName = _("Madness")
            StatusObj.EffectType = BATTLE_STATUS_EFFECT_TYPE.DEBUFF
            StatusObj.Icon = "images/battle_status_icons/no_icon.webp"
            StatusObj.Duration = Duration
            StatusObj.ErraticChance = ErraticChance

            # Engine Tick Attributes required by Battle_ApplyStatusEffect
            StatusObj.TickOn_Enemy = getattr(store, "BATTLE_STATUS_EFFECT_TICK", object())
            StatusObj.TickOn_Ally = getattr(store, "BATTLE_STATUS_EFFECT_TICK", object())
            StatusObj.TickOn = None

            # Apply status using engine handler
            EffectHandler = BattleEffect_ApplyStatusOnEnemy(StatusEffect = StatusObj)
            EffectHandler.ApplyEffect(Target)
            return

        def GetDesc(self, DescLevel = 1):
            Turns = self.DurationByLevel[DescLevel]
            Chance = round(self.ErraticChanceByLevel[DescLevel] * 100)
            return tra(_("Drives an enemy into madness for %s turn(s). While afflicted, the target has a %s%% chance on their turn to act erratically, attacking allies or harming themselves.")) % (Turns, Chance)