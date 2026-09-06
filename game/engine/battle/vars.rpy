default BattleScene = None              # global, if not none -> player is in battle
default LastBattleOutcome = None        # "victory", "defeat", "retreat"
default LastCombatTeam = None           # global for the team-selection screen: will re-select your last party composition

default Playthrough_FoughtEnemyTeams = []       # a list of ["brute", "scout"], ["scout", "scout"], if you encounter same combo another time, you dont get xp

default persistent.BattlePref_AutoLootAll = False               # show loot screen at all
default persistent.BattlePref_FastLoop = False                  # speed up all anims to near instant
default persistent.BattlePref_AutoFillPlayerCombatTeam = True   # dont show team selection unless necessary
default persistent.BattlePref_AutoBattleByDefault = False       # left side will be ai controlled on start
default persistent.Battle_AutoSelectActorAndTargetForAI = True  # by default, AI selection will bop around

