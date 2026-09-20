init -1 python:
    class BATTLE_COLORS:
        REQ_MISSING = "#ff6b6b"
        REQ_SATISF = "#7bd88f"
        SKILLDESC_GREEN = "#7bd88f"

    class BATTLE_COLORS_LOG:
        BATTLE_STATUS = "#d7c7a1"
        NAME_ALLY = "#8bd5ff"
        NAME_ENEMY = "#ff8b8b"
        NAME_SKILL = "#f4d35e"
        NAME_ITEM = "#b8e986"
        DAMAGE = "#ff6b6b"
        DAMAGE_BLEED = "#c0392b"
        DAMAGE_POISON = "#8e44ad"
        DAMAGE_BURN = "#e67e22"
        CRITICAL = "#ffd166"
        MISS = "#9aa0a6"
        RESTORE_HEALTH = "#7bd88f"
        RESTORE_ENERGY = "#63c5da"
default BattleScene = None              # Global reference; non-None indicates an active combat session
default LastBattleOutcome = None        # Stores "victory", "defeat", or "retreat"
default LastCombatTeam = None           # Remembers last party composition for party selection UI

default Playthrough_FoughtEnemyTeams = []       # Tracks defeated enemy configurations to prevent duplicate XP gains

default persistent.BattlePref_AutoLootAll = False               # Automatically loot all items without showing loot screen
default persistent.BattlePref_FastLoop = False                  # Speed up battle animations to near-instantaneous
default persistent.BattlePref_AutoFillPlayerCombatTeam = True   # Skip team selection UI when possible
default persistent.BattlePref_AutoBattleByDefault = False       # Set player side (Side 0) to AI control on battle start
default persistent.BattlePref_AutoSelectActorAndTargetForAI = True  # Enable visual target indicator bopping during AI action selection