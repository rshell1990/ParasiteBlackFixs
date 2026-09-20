# Constants namespace for combat targeting rules
init -2 python in BATTLE_TARGETS:
    _constant = True
    SELF = 0
    ANY_ALLY = 1
    ALLY_NOT_SELF = 2
    ANY_ENEMY = 3
    ALL_ENEMIES = 4
    ALL_ALLIES = 5
    ALL_ALLIES_NOT_SELF = 6
    EVERYONE = 7

# Dynamic skill and item registries
init -1 python:
    SkillLib = {}
    def RegisterBattleSkill(SkillID):
        def Decorate(Class):
            SkillLib[SkillID] = Class
            Class.SkillID = SkillID
            return Class
        return Decorate

    ItemActionLib = {}
    def RegisterBattleItemAction(ActionID):
        def Decorate(Class):
            ItemActionLib[ActionID] = Class
            Class.ActionID = ActionID
            return Class
        return Decorate

init python:
    class ScheduledAction:
        def __init__(self, ActionInstance, Target):
            self.ActionInstance = ActionInstance
            self.Target = Target
    
        def __repr__(self):
            action_name = getattr(self.ActionInstance, "DisplayName", "Unknown Action")
            
            if isinstance(self.Target, list):
                target_str = f"{len(self.Target)} Targets"
            elif hasattr(self.Target, "CharRef") and isinstance(self.Target.CharRef, dict):
                target_str = self.Target.CharRef.get("name", "Unknown Character")
            else:
                target_str = str(self.Target)
                
            return f"{action_name}, target {target_str}"