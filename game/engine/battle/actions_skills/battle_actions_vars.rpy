# opens up libs for skill and item actions
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
            # Inject the class into the global store so pickle can resolve it on load
            setattr(renpy.store, Class.__name__, Class)
            return Class
        return Decorate

# an enum without enums :^)
init -2 python in BATTLE_TARGETS:
    _constant = True
    SELF = 0
    ANY_ALLY = 1
    ALLY_NOT_SELF = 2
    ANY_ENEMY = 3
    ALL_ENEMIES = 4
    ALL_ALLIES = 5
    ALL_ALLIES_NOT_SELF = 7
    EVERYONE = 6

init python:
    # THIS IS CALLED ACTION BC IT CAN EITHER BE "USE ITEM" OR "USE SKILL"
    class ScheduledAction:
        def __init__(self, ActionInstance, Target):
            self.ActionInstance = ActionInstance
            self.Target = Target
    
        def __repr__(self):
            return "%s, target %s" % (getattr(self.ActionInstance, "DisplayName", "some action"), self.Target.CharRef["name"])

