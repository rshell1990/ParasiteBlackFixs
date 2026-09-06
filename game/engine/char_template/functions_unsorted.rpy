init -2 python:
################### relationship
    def CharChangeRel(Char_ID, changeValue, Silent = False):
        dataObj = store.worldChars[Char_ID]
        newValue = max(min(dataObj["relation"] + changeValue, 9), -10)
        dataObj["relation"] = newValue
        if not Silent:
            if worldChars[Char_ID]["relstatus"] == "rel_lover":
                if -10 < newValue < 10:
                    if changeValue > 0:
                        AddNotif(tra(_("Relationship with ")) + tra(dataObj["name"]) + tra(_(" improved by ")) + str(changeValue), Kind = "char_rel_increase")
                    if changeValue < 0:
                        AddNotif(tra(_("Relationship with ")) + tra(dataObj["name"]) + tra(_(" lowered by ")) + str(changeValue), Kind = "char_rel_decrease")
                else:
                    if changeValue > 0:
                        AddNotif(tra(_("Relationship with ")) + tra(dataObj["name"]) + tra(_(" improved, but remained unchanged.")), Kind = "char_rel_increase_unchanged")
                    if changeValue < 0:
                        AddNotif(tra(_("Relationship with ")) + tra(dataObj["name"]) + tra(_(" lowered, but remained unchanged.")), Kind = "char_rel_decrease_unchanged")
    # alt name for script
    def CharAddRel(CharID, AddValue, Silent = False):
        CharChangeRel(CharID, AddValue, Silent)
    
    def CharGetRel(CharID):
        return worldChars[CharID]["relation"]

###################### altform
    def CharAltFormUnlock(CharID):
        store.worldChars[CharID]["AltForm_Unlocked"] = True
        return
    def CharAltFormLock(CharID):
        store.worldChars[CharID]["AltForm_Unlocked"] = False
        return
    def CharSetBattleSkinID(CharID, SkinID):
        store.worldChars[CharID]["BattleSkin"] = SkinID
        return

    # set any variable on a char to a new value. do not abuse it in weird ways
    def CharSetVar(CharID, Field, Value):
        if _in_replay:
            return
        VerboseLog_General = False
        Assert(Field in worldChars[CharID].props, "Field '%s' not found in .props for char '%s'" % (Field, CharID))
        if VerboseLog_General:
            print("DEBUG: For char '%s' setting field '%s' to '%s' (CharSetVar)" % (CharID, Field, Value))
        store.worldChars[CharID][Field] = Value
        return
    # get any var on a world char
    def CharGetVar(CharID, Field):
        return worldChars[CharID][Field]
    # get char name (imprtant bc tl)
    def CharGetName(CharID):
        return tra(worldChars[CharID]["name"])

    def CharHasVar(CharID, Field):
        return Field in worldChars[CharID]

    # sets "clothes" variable on a char to any value you pass in
    def CharSetClothes(CharID, Value):
        store.worldChars[CharID]["clothes"] = Value
        return

    # returns the current value of "clothes" variable on a char
    def CharGetClothes(CharID):
        return worldChars[CharID]["clothes"]
    
    # sets char portrait (rel/battle) to *image path*. MIGHT WORK with file name or renpy image tag
    def CharSetPortrait(CharID, ImagePath):
        store.worldChars[CharID]["portrait"] = ImagePath
        return
    # sets char "name" variable
    def CharSetName(CharID, NewName):
        store.worldChars[CharID]["name"] = NewName


############## internals
    def BuildCharTemplate(CharID = None, ExtraData = None, **ModifyValues):
        if CharID is None:
            raise Exception("CharID not defined")
        ReturnDict = copy.deepcopy(store.baseCharTemplate)

        for Key, Val in ModifyValues.items():
            if Key not in ReturnDict:
                raise Exception("ModifyValues: Invalid property: %s" % Key)
            ReturnDict[Key] = copy.deepcopy(Val)

        if ExtraData is not None:
            for Key, Val in ExtraData.items():
                if Key in ReturnDict:
                    raise Exception("Key %s is defined as an ExtraData for charID %s, but the key is present on baseCharTemplate." % (Key, CharID))

            ReturnDict.update(copy.deepcopy(ExtraData))

        return ReturnDict

    # Add skill to the char or upgrade a skill already added
    def CharAddOrRaiseSkill(CharID, SkillID, SkillInstance,  CharClassID, SkillTabID, AltFormSkill = False):
        Assert(SkillID in SkillLib, "Skill ID %s not found in skillLib" % SkillID)
        WorldChar = worldChars[CharID]
        if AltFormSkill:
            # add the skill if its not there
            if SkillID not in WorldChar["AltForm_CharSkills"]:
                WorldChar["AltForm_CharSkills"][SkillID] = 0
        else:
            # add the skill if its not there
            if SkillID not in WorldChar["CharSkills"]:
                WorldChar["CharSkills"][SkillID] = 0

        if AltFormSkill:
            if WorldChar["AltForm_CharSkills"][SkillID] < SkillInstance.Level_Max:
                WorldChar["AltForm_CharSkills"][SkillID] += 1
        else:
            if WorldChar["CharSkills"][SkillID] < SkillInstance.Level_Max:
                WorldChar["CharSkills"][SkillID] += 1

        SkillInstance.Level += 1

        if AltFormSkill:
            WorldChar["AltForm_SkillPoints"] -= 1
        else:
            WorldChar["skillPoints"] -= 1

        TooltipSet(Text(GetSkillDesc(SkillInstance) + GetSkillReq(CharID, CharClassID, SkillTabID, SkillID, SkillInstance, AltFormSkill = AltFormSkill)))

        return