default _enable_achievements = True

init python:
    achievement.steam_position = "bottom right"

    achievement.register("DEEP_POCKETS")
    achievement.register("ALL_THAT_GLITTERS")
    achievement.register("A_KINGS_RANSOM")
    achievement.register("MAKING_A_NAME_FOR_YOURSELF")
    achievement.register("YOU_GET_AROUND")
    achievement.register("STUD")
    achievement.register("DESERT_LORD")
    achievement.register("A_WARRIOR_NEEDS_HIS_ALLIES")
    achievement.register("A_HERO_IN_THE_MAKING")
    achievement.register("YOU_ARE_GOING_PLACES")
    achievement.register("BLOODTHIRSTY_ARENT_WE")
    achievement.register("LOOK_MOM_I_MADE_A_THING")
    achievement.register("A_FAIR_EXCHANGE")
    achievement.register("A_STICKY_TYRANT")
    achievement.register("YOUVE_BEEN_BUSY")

    achievement.register("LOOK_AT_YOU_DETECTIVE")
    achievement.register("THE_SECOND_SIEGE_OF_NOVARAS")

    # beast of novaras quest
    achievement.register("A_BEAST_OR_SAVIOR")

    def can_unlock_achievement(name):
        global _enable_achievements
        if _enable_achievements and not achievement.has(name):
            return True
        else:
            return False
    
    def unlock_achievement(name):
        achievement.grant(name)
        achievement.sync()
        return

default _total_earned_gold = 0
default _total_cummed_characters = []
default _total_node_enter = 0
default _total_enemies_killed = 0
default _total_gold_spent_on_merchant = 0
