default seenWMapLocTags = set() # set of wmap-friendly loc tags player can see on map
# be aware that there are more libs enabled by other code. for example, skill lib
init -3 python:
    vfxLibLights = {}
    skinLib = {}
    skillTreeLib = {}
    skillTreeLibObj = {}
    soundLib = {}
    dynamic_enemy_lists = {} # used in dynamically-defined combat
    lewdsGalleryLib = {}
    wLocs = {} # 'world locations'
    CharDefs = {}
    notesLib = {}
    CharIDPartyDialogueLabelMap = {}
    Lib_BattleSkillTrees = {}