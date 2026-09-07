define ATTRIBUTE_RANGE = 15 # <- "raise your lowest attribute first" range

init -2 python:
########### derived stats (health, damage, armor n the like)
    def healthMaxCalc(dataObj):
        ResultValue = int(dataObj["base_health"] + max(dataObj["derived_Endurance"] * 5, 0))
        ResultValue = max(ResultValue, 1)
        return ResultValue

    def energyMaxCalc(dataObj):
        ResultValue = int(dataObj["base_energy"] + max(dataObj["derived_Willpower"] * 5, 0))
        ResultValue = max(ResultValue, 1)
        return ResultValue

    def manaMaxCalc(dataObj):
        ResultValue = int(dataObj["base_mana"] + max(dataObj["Mana_Power"] * 5, 0))
        ResultValue = max(ResultValue, 1)
        return ResultValue

    def damageCalc(dataObj):
        EquipmentValue = 0

        hand_1_item = dataObj["eqp_hand1"] if dataObj["eqp_hand1"] is not None else None
        hand_2_item = dataObj["eqp_hand2"] if dataObj["eqp_hand2"] is not None else None

        if hand_1_item:
            EquipmentValue += all_items[hand_1_item].get("Damage", 0)
        if hand_2_item:
            EquipmentValue += all_items[hand_2_item].get("Damage", 0)

        ResultValue = int(dataObj["base_damage"] + dataObj["derived_Strength"] * 5 + EquipmentValue)
        # safety
        ResultValue = max(ResultValue, 1)
        return ResultValue

    def armorCalc(dataObj):
        ResultValue = dataObj["base_armor"] + dataObj["derived_Endurance"] * 3
        for SlotID in EQP_SLOTS.ALL:
            if dataObj[SlotID] is not None:
                ItemID = dataObj[SlotID]
                ResultValue += all_items[ItemID].get("Armor", 0)
    
        ResultValue = max(ResultValue, 1)
        return(ResultValue)

    def magicResCalc(dataObj):
        ResultValue = dataObj["base_mres"] + dataObj["derived_Willpower"]
        for SlotID in EQP_SLOTS.ALL:
            if dataObj[SlotID] is not None:
                ItemID = dataObj[SlotID]
                ResultValue += all_items[ItemID].get("add_stat_mres", 0)
    
        ResultValue = max(ResultValue, 1)
        return(ResultValue)

    # attack rating == raw score to hit
    def AttackRatingCalc(dataObj):
        ResultValue = dataObj["base_att_rate"] + dataObj["derived_Agility"] * 2
    
        ResultValue = max(ResultValue, 1)
        return ResultValue

    # dodge rating == how hard enemy is to hit
    def DodgeRatingCalc(dataObj):
        ResultValue = dataObj["base_dodge_rate"] + dataObj["derived_Dexterity"] * 2
    
        ResultValue = max(ResultValue, 1)
        return ResultValue

    def CritChanceCalc(dataObj):
        ResultValue = dataObj["base_crit_chance"] + int(dataObj["derived_Luck"] * 2.5)
        for SlotID in EQP_SLOTS.ALL:
            if dataObj[SlotID] is not None:
                ItemID = dataObj[SlotID]
                ResultValue += all_items[ItemID].get("add_stat_crit_chance", 0)
    
        ResultValue = max(ResultValue, 1)
        return(ResultValue)

############# attributes, this will likely be compressed  
    def StrengthCalc(dataObj):
        ResultValue = dataObj["Strength"]
        # in both story and combat, get gear bonus
        for SlotID in EQP_SLOTS.ALL:
            if dataObj[SlotID] is not None:
                ItemID = dataObj[SlotID]
                ResultValue += all_items[ItemID].get("add_attr_str", 0)

        # if in battle, use battle status eff properties
        if dataObj["BattleChar"] is not None:
            for StatusEff in dataObj["BattleChar"].StatusEffects:
                if StatusEff.AttrMod_StrengthMul is not None:
                    ResultValue *= StatusEff.AttrMod_StrengthMul
                if StatusEff.AttrMod_StrengthAdd is not None:
                    ResultValue += StatusEff.AttrMod_StrengthAdd
        # story mode, separate calc path
        else:
            if dataObj.CharID in StoryStatusEffects:
                for StatusEffID in StoryStatusEffects[dataObj.CharID]:
                    if "StrengthAdd" in StoryStatEffDefs[StatusEffID]:
                        ResultValue += StoryStatEffDefs[StatusEffID]["StrengthAdd"]

        ResultValue = math.ceil(max(ResultValue, 1))
        return(ResultValue)

    def EnduranceCalc(dataObj):
        VerboseLog_General = False
        ResultValue = dataObj["Endurance"]
        for SlotID in EQP_SLOTS.ALL:
            if dataObj[SlotID] is not None:
                ItemID = dataObj[SlotID]
                if ItemID in all_items:
                    ResultValue += all_items[ItemID].get("add_attr_end", 0)
                else:
                    if VerboseLog_General:
                        print("warning: EnduranceCalc tried to add endurance to char %s from item with id %s which was not found in all_items" % (dataObj["name"], ItemID))

        if dataObj["BattleChar"] is not None:
            for StatusEff in dataObj["BattleChar"].StatusEffects:
                if StatusEff.AttrMod_EnduranceMul is not None:
                    ResultValue *= StatusEff.AttrMod_EnduranceMul
                if StatusEff.AttrMod_EnduranceAdd is not None:
                    ResultValue += StatusEff.AttrMod_EnduranceAdd
        else:
            if dataObj.CharID in StoryStatusEffects:
                for StatusEffID in StoryStatusEffects[dataObj.CharID]:
                    if "EnduranceAdd" in StoryStatEffDefs[StatusEffID]:
                        ResultValue += StoryStatEffDefs[StatusEffID]["EnduranceAdd"]
    
        ResultValue = math.ceil(max(ResultValue, 1))
        return(ResultValue)

    def WillpowerCalc(dataObj):
        ResultValue = dataObj["Willpower"]
        for SlotID in EQP_SLOTS.ALL:
            if dataObj[SlotID] is not None:
                ItemID = dataObj[SlotID]
                ResultValue += all_items[ItemID].get("add_attr_will", 0)

        if dataObj["BattleChar"] is not None:
            for StatusEff in dataObj["BattleChar"].StatusEffects:
                if StatusEff.AttrMod_WillpowerMul is not None:
                    ResultValue *= StatusEff.AttrMod_WillpowerMul
                if StatusEff.AttrMod_WillpowerAdd is not None:
                    ResultValue += StatusEff.AttrMod_WillpowerAdd
    
        ResultValue = math.ceil(max(ResultValue, 1))
        return(ResultValue)

    def AgiCalc(dataObj):
        ResultValue = dataObj["Agility"]
        for SlotID in EQP_SLOTS.ALL:
            if dataObj[SlotID] is not None:
                ItemID = dataObj[SlotID]
                ResultValue += all_items[ItemID].get("add_attr_agi", 0)

        if dataObj["BattleChar"] is not None:
            for StatusEff in dataObj["BattleChar"].StatusEffects:
                if StatusEff.AttrMod_AgilityMul is not None:
                    ResultValue *= StatusEff.AttrMod_AgilityMul
                if StatusEff.AttrMod_AgilityAdd is not None:
                    ResultValue += StatusEff.AttrMod_AgilityAdd
    
        ResultValue = math.ceil(max(ResultValue, 1))
        return(ResultValue)

    def DexCalc(dataObj):
        ResultValue = dataObj["Dexterity"]
        for SlotID in EQP_SLOTS.ALL:
            if dataObj[SlotID] is not None:
                ItemID = dataObj[SlotID]
                ResultValue += all_items[ItemID].get("add_attr_dex", 0)
    
        if dataObj["BattleChar"] is not None:
            for StatusEff in dataObj["BattleChar"].StatusEffects:
                if StatusEff.AttrMod_DexterityMul is not None:
                    ResultValue *= StatusEff.AttrMod_DexterityMul
                if StatusEff.AttrMod_DexterityAdd is not None:
                    ResultValue += StatusEff.AttrMod_DexterityAdd
        else:
            if dataObj.CharID in StoryStatusEffects:
                for StatusEffID in StoryStatusEffects[dataObj.CharID]:
                    if "DexterityAdd" in StoryStatEffDefs[StatusEffID]:
                        ResultValue += StoryStatEffDefs[StatusEffID]["DexterityAdd"]

        ResultValue = math.ceil(max(ResultValue, 1))
        return(ResultValue)

    def LuckCalc(dataObj):
        ResultValue = dataObj["Luck"]
        for SlotID in EQP_SLOTS.ALL:
            if dataObj[SlotID] is not None:
                ItemID = dataObj[SlotID]
                ResultValue += all_items[ItemID].get("add_attr_luck", 0)
    
        if dataObj["BattleChar"] is not None:
            for StatusEff in dataObj["BattleChar"].StatusEffects:
                if StatusEff.AttrMod_LuckMul is not None:
                    ResultValue *= StatusEff.AttrMod_LuckMul
                if StatusEff.AttrMod_LuckAdd is not None:
                    ResultValue += StatusEff.AttrMod_LuckAdd

        ResultValue = math.ceil(max(ResultValue, 1))
        return(ResultValue) 

    def CharismaCalc(dataObj):
        ResultValue = dataObj["Charisma"]
        for SlotID in EQP_SLOTS.ALL:
            if dataObj[SlotID] is not None:
                ItemID = dataObj[SlotID]
                ResultValue += all_items[ItemID].get("add_attr_charisma", 0)
    
        if dataObj["BattleChar"] is not None:
            for StatusEff in dataObj["BattleChar"].StatusEffects:
                ResultValue *= getattr(StatusEff, "AttrMod_CharismaMul")

        ResultValue = math.ceil(max(ResultValue, 1))
        return(ResultValue) 

    def BarterCalc(dataObj):
        ResultValue = dataObj["Barter"]
        for SlotID in EQP_SLOTS.ALL:
            if dataObj[SlotID] is not None:
                ItemID = dataObj[SlotID]
                ResultValue += all_items[ItemID].get("add_attr_barter", 0)
    
        if dataObj["BattleChar"] is not None:
            for StatusEff in dataObj["BattleChar"].StatusEffects:
                ResultValue *= getattr(StatusEff, "AttrMod_BarterMul")

        ResultValue = math.ceil(max(ResultValue, 1))
        return(ResultValue) 

######### attribute set/add
    def SetCharAttr(dataObj, att_name, value):
        if att_name not in dataObj:
            raise Exception("SetCharAttr: Attribute (%s) does not exist in %s" % (att_name, dataObj))
        dataObj[att_name] = value
        return

    def AddCharAttr(CharOrID, att_name, value, TrackDirect = True): # tracked attribute increases will be recorded for auto-recalculation
        if isinstance(CharOrID, str):
            # assumes if its a string, its an id, therefore a world char
            dataObj = worldChars[CharOrID]
        elif isinstance(CharOrID, PBCharacter):
            # everything else must be a char
            dataObj = CharOrID
        if att_name not in dataObj:
            raise Exception("AddCharAttr: Attribute (%s) does not exist in %s" % (att_name, dataObj))
        dataObj[att_name] += value
        if TrackDirect:
            dataObj["directly_added_attribute_points"] += 1
        return

######## check if can raise attribute over x of any other
    def CanRaiseAttribute(Char_ID, OrigAttrID):
        if Char_ID == "mc":
            AttributesToCheck = ["Strength", "Endurance", "Willpower", "Agility", "Dexterity", "Luck", "Charisma", "Barter"]
        else:
            # non-mc chars shouldnt worry bout charisma or barter for allocation
            AttributesToCheck = ["Strength", "Endurance", "Willpower", "Agility", "Dexterity", "Luck"]
        Char = worldChars[Char_ID]
        AttributesToCheck.remove(OrigAttrID)
        for AttributeID in AttributesToCheck:
            ThisAttrValue = Char[AttributeID]
            if ThisAttrValue + ATTRIBUTE_RANGE <= Char[OrigAttrID]:
                return False
        return True

    
## same but goes other way, for char creation
    def CanReduceAttribute(Char_ID, OrigAttrID):
        # first get a list of all attrs
        if Char_ID == "mc":
            AttributesToCheck = ["Strength", "Endurance", "Willpower", "Agility", "Dexterity", "Luck", "Charisma", "Barter"]
        else:
            # non-mc chars shouldnt worry bout charisma or barter for allocation
            AttributesToCheck = ["Strength", "Endurance", "Willpower", "Agility", "Dexterity", "Luck"]
        Char = worldChars[Char_ID]
        # delete the attribute we're checking for from the list
        AttributesToCheck.remove(OrigAttrID)
        # go over the list, compare all attributes to the orig one
        for AttributeID in AttributesToCheck:
            ThisAttrValue = Char[AttributeID]
            if ThisAttrValue - ATTRIBUTE_RANGE > Char[OrigAttrID]:
                return False
        return True

    def LowerHighestAttributeIfNecessary(CharID, OrigAttrID):
        if CharID == "mc":
            AttributesToCheck = ["Strength", "Endurance", "Willpower", "Agility", "Dexterity", "Luck", "Charisma", "Barter"]
        else:
            # non-mc chars shouldnt worry bout charisma or barter for allocation
            AttributesToCheck = ["Strength", "Endurance", "Willpower", "Agility", "Dexterity", "Luck"]

        Char = worldChars[CharID]
        AttributesToCheck.remove(OrigAttrID)

        MarkedForReduction = []
        for AttributeID in AttributesToCheck:
            CheckAttrValue = Char[AttributeID]
            if Char[OrigAttrID] + ATTRIBUTE_RANGE < CheckAttrValue:
                MarkedForReduction.append(AttributeID)
            
        for AttrID in MarkedForReduction:
            Char[AttrID] -= 1
            Char["lvlPoints"] += 1

        return


###### this allocates free attr points based on rng and "auto_attr_allocation" weight map
    def AutoAllocateAttributes(dataObj):
        auto_attr_allocation = dataObj["auto_attr_allocation"] if dataObj["auto_attr_allocation"] is not None else "equal"
        # TL;DR if "auto_attr_allocation" is defined, use weighted random
        # else boost randomly from battle-relevant attributes
        weights = sorted(list(attr_allocation_weights[auto_attr_allocation].keys()))
        weight_sum = sum(weights)
        if weight_sum != 100:
            raise Exception("Weight sum of class %s does not equal 100 (it's %s)" % (auto_attr_allocation, weight_sum))
        while dataObj["lvlPoints"] > 0:
            rng = RngInt(1, 100)
            for weight in weights:
                if rng <= weight:
                    target_weight = weight
                    break
                rng -= weight            
            attribute_to_raise = random.choice(attr_allocation_weights[auto_attr_allocation][target_weight])
            AddCharAttr(dataObj, attribute_to_raise, 1, TrackDirect = False)
            dataObj["lvlPoints"] -= 1
        return

    attr_allocation_weights = {}
    # okay its not actually even coz keys need 2be different SO WHAT
    attr_allocation_weights["equal"] = {
        20:["Strength"],
        18:["Endurance"],
        17:["Agility"],
        16:["Dexterity"],
        15:["Willpower"],
        14:["Luck"],
    }
    attr_allocation_weights["fighter"] = {
        50:["Strength", "Endurance"],
        35:["Agility", "Dexterity", "Willpower"],
        15:["Luck"]
    }
    attr_allocation_weights["tank"] = {
        45:["Endurance"],
        30:["Strength", "Willpower"],
        25:["Agility", "Dexterity"]
    }
    attr_allocation_weights["hulk"] = {
        40:["Strength"],
        35:["Endurance", "Willpower", "Agility"],
        25:["Dexterity", "Luck"]
    }
    attr_allocation_weights["rogue"] = {
        50:["Agility", "Dexterity"],
        30:["Strength", "Luck"],
        20:["Willpower", "Endurance"]
    }
    attr_allocation_weights["summoner"] = {
        50:["Agility", "Dexterity"],
        30:["Strength", "Luck"],
        20:["Willpower", "Endurance"]
    }
    attr_allocation_weights["necromancer"] = {
        50:["Agility", "Dexterity"],
        30:["Strength", "Luck"],
        20:["Willpower", "Endurance"]
    }
    ### descriptions last updated 23/09/2023
    # "Strength":     5, # +5 melee damage per point
    # "Endurance":    5, # +5 hp per point OVER 5, its value also equals phys damage resistance (armor)

    # "Willpower":    5, # +5 max energy per point OVER 5
    # "mana_power":   5, # +5 max mana per point, UNUSED

    # "Agility":      5, # value equals attack rating (which affects to-hit chance)
    # "Dexterity":    5, # value equals dodge rating (which is tested against attack rating)

    # "Luck":         5, # to-crit, flat % value

    # these are narrative-only
    # "Charisma":        5, # unlocks charisma-based choices
    # "Barter":       5, # the higher barter skill, the lower shop prices + some unique dialogue options 