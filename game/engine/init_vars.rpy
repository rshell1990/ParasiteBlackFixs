# Dummy dictionary used to store temporary variables
# keys unused anymore must be removed
default tmpvar = {}

default player_party = ["mc"]

default PlayerPos = WorldPosition("mc_house_bedroom")
default questObjs = dict()

default ShowDialogueHistoryButton = True
default ShowLevelUpFloatingText = True # turned off for prologue section

init -1 python:
    # XP needed to get to a level = (sum of previous lvl) * 350
    # values in parentheses mean, "how much do I need to get there from prev level"
    # lvl 1: 0
    # lvl 2: 350 =>  (1) *  350
    # lvl 3: 1050  (700) => (1 + 2) * 350
    # lvl 4: 2100 (1050) => (1 + 2 + 3) * 350
    # lvl 5: 3500 (1400) => (1 + 2 + 3 + 4) * 350
    # lvl 6: 5250 (1750)
    # lvl 7: 7350 (2100)
    store.allLvls = {}
    for i in range(1, 101):
        store.allLvls[i] = int(i * (1 + i) / 2 * 350)

init 1 python:
    # this is a very bad way to do this tbh
    def setInitVariables():
        store.PlayerPos = WorldPosition("mc_house_bedroom")
        WorldMapLocAdd("novaras_gates")
        SetGameDay(1)
        TimeSetTo(TIME_MORNING)
        AutoTimeFreeze(False)
        store.autoMoveQ = []
        store.curDialogue = None
        store.eventLabels = []
        store.questObjs = {x.__name__: x() for x in allQuests}
        store.questLogCurSel = None

        AutoAmb(True)
        AutoMus(True)

        store.dynamicAmbience = None
        store.dynamicMusic = None

        store.unlockedNotes = set()

        store.player_name = _("Caspian") # Default value
        store.player_party = ["mc"]
        store.PlayerCombatTeam = store.player_party

############ inventory and items-related 
        BuildAllItemContainers()
#########################################
        store.worldChars = {}

        for CharID in CharDefs:
            if not CharDefs[CharID]["IsMob"]:
                CreateWorldCharFromID(CharID)

        for tag in wLocs:
            wLocs[tag].setParentRef()
        return

    config.start_callbacks.append(setInitVariables)

default persistent.ShowAnnoyingPopup = True
