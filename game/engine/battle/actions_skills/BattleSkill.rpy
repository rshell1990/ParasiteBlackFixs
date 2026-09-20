init -1 python:
    class BattleSkill:
        Owner_PBCharID      = None
        Owner_BattleChar    = None

        Level = 1
        Level_Max = 1

        DisplayName = ""
        Icon = "images/battle_skill_icons/no_icon.webp"

        SpendTurn = True
        AutoSelectNextInPartyOnExecute = True
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 0
        Cost_Mana = 0
        Cost_Infection = 0         # mc only
        Cost_PercHealthCurr = 0.0  # % of current hp, 0.5 == 50%
        Cost_PercHealthMax = 0.0   # % of max hp

        OncePerTurn = True
        UsedThisTurn = False

        AITags = set()
        AIBaseWeight = 1.0

        ShowHitChance = True       # for 100% hit stuff, disable this

        def __init__(self, Owner_BattleChar=None, Owner_PBCharID=None, ToLevel=1):
            assert Owner_BattleChar is not None or Owner_PBCharID is not None, "Skill must have either pbchar or battle char owner"
            self.Owner_PBCharID = Owner_PBCharID
            self.Owner_BattleChar = Owner_BattleChar
            self.Level = ToLevel

        def OwnerCharCanPaySkillCost(self):
            # energy cost
            if self.Cost_Energy > 0:
                if self.Owner_BattleChar.Energy < self.Cost_Energy:
                    return False

            # mana cost
            if self.Cost_Mana > 0:
                if self.Owner_BattleChar.Mana < self.Cost_Mana:
                    return False

            # current hp % cost
            if self.Cost_PercHealthCurr > 0.0:
                if self.Owner_BattleChar.Health <= 1:
                    return False

            # max hp % cost
            if self.Cost_PercHealthMax > 0.0:
                IntHpCostValue = int(self.Owner_BattleChar.HealthMax * self.Cost_PercHealthMax)
                if self.Owner_BattleChar.Health <= IntHpCostValue:
                    return False

            # infection cost
            if self.Cost_Infection > 0:
                # only test for player-controlled mc
                if self.Owner_BattleChar.BattleSide == 0 and hasattr(store, "InfectionModule"):
                    inf_mod = store.InfectionModule()
                    if (inf_mod.MaxValue - inf_mod.CurrentValue) <= self.Cost_Infection:
                        return False

            return True

        # extra test to check if skill can be executed
        def CanExecute(self):
            if self.OncePerTurn and self.UsedThisTurn:
                return False
            return self.OwnerCharCanPaySkillCost()

        # fires right before execution to drain resources
        def DrainCosts(self):
            if self.Cost_Energy > 0:
                self.Owner_BattleChar.Energy -= self.Cost_Energy
            if self.Cost_Mana > 0:
                self.Owner_BattleChar.Mana -= self.Cost_Mana
            if self.Cost_Infection > 0 and self.Owner_BattleChar.BattleSide == 0:
                if hasattr(store, "InfectionModule"):
                    store.InfectionModule().CurrentValue += self.Cost_Infection
            if self.Cost_PercHealthCurr > 0.0:
                new_hp = int(self.Owner_BattleChar.Health * (1.0 - self.Cost_PercHealthCurr))
                self.Owner_BattleChar.Health = max(1, min(new_hp, self.Owner_BattleChar.HealthMax))
            if self.Cost_PercHealthMax > 0.0:
                new_hp = self.Owner_BattleChar.Health - int(self.Owner_BattleChar.HealthMax * self.Cost_PercHealthMax)
                self.Owner_BattleChar.Health = max(1, min(new_hp, self.Owner_BattleChar.HealthMax))

        # actual logic
        def Execute(self, Target):
            pass

        # description text
        def GetDesc(self, DescLevel=1):
            return "No desc"

    # for ui
    def Battle_FormatDescVal(Value, Percentage = False, Parentheses = False):
        TextValue = str(Value)
        if Percentage:
            TextValue += "%"
        if Parentheses:
            TextValue = "(" + TextValue + ")"
        return "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}%s{/color}" % TextValue

    def GetSkillDesc(SkillObj):
        if SkillObj is None:
            return ""
        GetDesc = getattr(SkillObj, "GetDesc", None)
        if GetDesc is None:
            return str(getattr(SkillObj, "DisplayName", ""))
        return GetDesc()

    def Battle_GetUnmetCostAsString(SkillObj):
        ResultStrings = []
        
        # energy cost
        if SkillObj.Cost_Energy > 0 and SkillObj.Owner_BattleChar.Energy < SkillObj.Cost_Energy:
            ResultStrings.append(_("Not enough energy!"))

        # mana cost
        if SkillObj.Cost_Mana > 0 and SkillObj.Owner_BattleChar.Mana < SkillObj.Cost_Mana:
            ResultStrings.append(_("Not enough mana!"))

        # current hp % cost
        if SkillObj.Cost_PercHealthCurr > 0.0 and SkillObj.Owner_BattleChar.Health <= 1:
            ResultStrings.append(_("Not enough health!"))

        # max hp % cost
        if SkillObj.Cost_PercHealthMax > 0.0:
            IntHpCostValue = int(SkillObj.Owner_BattleChar.HealthMax * SkillObj.Cost_PercHealthMax)
            if SkillObj.Owner_BattleChar.Health <= IntHpCostValue:
                ResultStrings.append(_("Not enough health!"))

        # infection cost
        if SkillObj.Cost_Infection > 0 and SkillObj.Owner_BattleChar.BattleSide == 0:
            if hasattr(store, "InfectionModule"):
                inf_mod = store.InfectionModule()
                if (inf_mod.MaxValue - inf_mod.CurrentValue) <= SkillObj.Cost_Infection:
                    ResultStrings.append(_("Cannot afford the infection hit!"))

        FormattedStrings = []
        for String in ResultStrings:
            FormattedStrings.append("{size=+6}{color=[BATTLE_COLORS.REQ_MISSING]}" + String + "{/color}{/size}\n")

        return "".join(FormattedStrings)