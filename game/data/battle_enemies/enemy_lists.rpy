init python:
    # these are for random-ish encounters
    dynamic_enemy_lists["novaras_patrol_bandits"] = [
        [{"e_bandit":2}, {"e_thug":3}, {"e_bandit":2}],
        [{"e_bandit":2}, {"e_bandit":2}, {"e_bandit":2}],
    ]
    dynamic_enemy_lists["lake_balun_slimelarks"] = [
        [{"e_slimelark":3}, {"e_slimelark":4}],
        [{"e_slimelark":2}, {"e_slimelark":2}, {"e_slimelark":3}]
    ]
    dynamic_enemy_lists["valley_demorai_hunt"] = [
        [{"e_demorai_brute":2}, {"e_demorai_scout":3}],
        [{"e_demorai_scout":2}, {"e_demorai_scout":2}, {"e_demorai_scout":2}],
        [{"e_demorai_scout":2}, {"e_demorai_scout":2}, {"e_demorai_scout":2}, {"e_demorai_scout":1}]
    ]
    def GetEnemyList(ID):
        return renpy.random.choice(dynamic_enemy_lists[ID])