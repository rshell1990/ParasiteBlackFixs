init -1 python:
    def DEBUG_AddAllCompanions():
        Chars = []
        for CharID in worldChars:
            if worldChars[CharID]["IsCompanion"] == True:
                Chars.append(CharID)

        for CharID in Chars:
            PartyAddChar(CharID, Silent = True)
        return
    
    def DEBUG_RemAllCompanions():
        Chars = []
        for CharID in worldChars:
            if worldChars[CharID]["IsCompanion"] == True:
                Chars.append(CharID)

        for CharID in Chars:
            if CharInParty(CharID):
                PartyRemChar(CharID, Silent = True)
        return
    
    def DEBUG_AddOneToAllClassSkills():
        CharsWithClass = [CharID for CharID in worldChars if worldChars[CharID]["BattleClass"] is not None]
        for CharID in CharsWithClass:
            WorldChar = worldChars[CharID]

            for SkillBranch in ["offence", "defence", "support"]:
                for SkillID in Lib_BattleSkillTrees[WorldChar["BattleClass"]][SkillBranch]:
                    # add skill id if its not there (also add level)
                    if SkillID not in WorldChar["CharSkills"]:
                        WorldChar["CharSkills"][SkillID] = 1
                    else:
                        SkillObj = SkillLib[SkillID](Owner_PBCharID = CharID)
                        WorldChar["CharSkills"][SkillID] = 1
                        if WorldChar["CharSkills"][SkillID] < SkillObj.Level_Max:
                            WorldChar["CharSkills"][SkillID] += 1

                if WorldChar["AltForm_BattleClass"] is not None:
                    for SkillID in Lib_BattleSkillTrees[WorldChar["AltForm_BattleClass"]][SkillBranch]:
                        
                        # add skill id if its not there (also add level)
                        if SkillID not in WorldChar["AltForm_CharSkills"]:
                            
                            WorldChar["AltForm_CharSkills"][SkillID] = 1
                        else:
                            
                            SkillObj = SkillLib[SkillID](Owner_PBCharID = CharID)
                            WorldChar["AltForm_CharSkills"][SkillID] = 1
                            if WorldChar["AltForm_CharSkills"][SkillID] < SkillObj.Level_Max:
                                
                                WorldChar["AltForm_CharSkills"][SkillID] += 1

