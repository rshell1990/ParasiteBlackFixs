init 1 python:
    BuildItemDicts()

init -1 python:
    def BuildItemDict(ItemID):
        NewItem = base_item.copy()
        NewItem.update(static_item_defs[ItemID])
        NewItem["template_ID"] = ItemID # store template ID coz why not
        return NewItem

    def BuildItemDicts():
        store.all_items = {}
        for ItemID in static_item_defs:
            store.all_items[ItemID] = BuildItemDict(ItemID)
        return

    def UseItemStory(char_ID, ItemID):
        for CallableAndArgs in all_items[ItemID]["on_use_story"]:
            func = CallableAndArgs[0]
            # Convert string name to function reference if passed as string
            if isinstance(func, str):
                func = getattr(store, func, None)
                
            if callable(func):
                if len(CallableAndArgs) > 1:
                    func(ItemID, char_ID, CallableAndArgs[1])
                else:
                    func(ItemID, char_ID)
        return
    def UseSkillBook(char_id, item_id):
        # 1. Fetch the target skill key string (e.g., "Summon")
        skill_id = all_items[item_id].get("teaches_skill")
        if not skill_id:
            return

        char_data = worldChars[char_id]

        # 2. Assign skill directly to CharSkills
        if "CharSkills" not in char_data or char_data["CharSkills"] is None:
            char_data["CharSkills"] = {}

        char_data["CharSkills"][skill_id] = 1

        # 3. Consume the item
        RemItemFrom(player_inv, item_id, 1, FromPlayer=True)

        # 4. Refresh Ren'Py UI state
        renpy.restart_interaction()
    def ItemHealUserStory(ItemID, char_ID, raw_heal_value):
        missing_hp = worldChars[char_ID]["HealthMax"] - worldChars[char_ID]["Health"]
        if missing_hp == 0:
            return
        CharHeal(char_ID, Value = raw_heal_value)
        RemItemFrom(player_inv, ItemID, 1, FromPlayer = True)
        renpy.music.play(renpy.random.choice(soundLib["usePotion"]), channel = "sound", loop = False, relative_volume = 0.75)
        TooltipClear()
        return

    def ItemRaiseAttStory(ItemID, char_ID, AttributeAndValue):
        AttributeToRaise = AttributeAndValue[0]
        ValueToRaiseBy = AttributeAndValue[1]
        AddCharAttr(worldChars["mc"], AttributeToRaise, ValueToRaiseBy)
        RemItemFrom(player_inv, ItemID, 1, FromPlayer = True)
        AddNotif(tra(_("%s raised by %s!")) % (tra(GUI_STAT_NAME_MAP[AttributeToRaise]), ValueToRaiseBy), Kind = "attr_raised")
        TooltipClear()
        return

    def ItemClearInfectionStory(ItemID, char_ID):
        InfChangeBy(-666)
        RemItemFrom(player_inv, ItemID, 1, FromPlayer = True)
        TooltipClear()
        return

    def ItemLearnSkill(ItemID, char_ID, skill_key):
        target_char = worldChars.get(char_ID, worldChars["mc"])
        
        # Method 1: Check if the character object has a dedicated method (e.g., AddSkill)
        if hasattr(target_char, "AddSkill"):
            target_char.AddSkill(skill_key)
            AddNotif(tra(_("Learned new skill: %s!")) % tra(skill_key), Kind = "attr_raised")
            RemItemFrom(player_inv, ItemID, 1, FromPlayer = True)
        
        # Method 2: Check for direct attribute (list or set)
        elif hasattr(target_char, "skills"):
            if skill_key not in target_char.skills:
                target_char.skills.append(skill_key)
                AddNotif(tra(_("Learned new skill: %s!")) % tra(skill_key), Kind = "attr_raised")
                RemItemFrom(player_inv, ItemID, 1, FromPlayer = True)
            else:
                AddNotif(tra(_("You already know %s.")) % tra(skill_key))

        elif hasattr(target_char, "Skills"):
            if skill_key not in target_char.Skills:
                target_char.Skills.append(skill_key)
                AddNotif(tra(_("Learned new skill: %s!")) % tra(skill_key), Kind = "attr_raised")
                RemItemFrom(player_inv, ItemID, 1, FromPlayer = True)
            else:
                AddNotif(tra(_("You already know %s.")) % tra(skill_key))
                
        # Method 3: Fallback if character attributes are accessed like dict keys
        elif "Skills" in target_char:
            if skill_key not in target_char["Skills"]:
                target_char["Skills"].append(skill_key)
                AddNotif(tra(_("Learned new skill: %s!")) % tra(skill_key), Kind = "attr_raised")
                RemItemFrom(player_inv, ItemID, 1, FromPlayer = True)
            else:
                AddNotif(tra(_("You already know %s.")) % tra(skill_key))
        else:
            AddNotif(tra(_("Learned new skill: %s!")) % tra(skill_key), Kind = "attr_raised")
            RemItemFrom(player_inv, ItemID, 1, FromPlayer = True)
            
        TooltipClear()
        return

#############################################################################

    def ItemCanBeDropped(ItemID):
        if all_items[ItemID]["cannot_lose"]:
            return False
        else:
            return True

    def ItemCanBeUsed(ItemID):
        if all_items[ItemID]["on_use_story"] is None:
            return False
        else:
            return True

    def GetItemValue(ItemID):
        if "value_per_unit" in all_items[ItemID]:
            return all_items[ItemID]["value_per_unit"]
        else:
            return 0

    def GetItemDesc(ItemID, Amount = 1, ShopLM = None, sell = False, BattleChar = None): # by UI only
        ### order of strings appended -> order of strings displayed
        item_dict = all_items[ItemID]
        item_value = item_dict["value_per_unit"] # < gets base price

        ShopNotInterestedFlag = False
        ShopCannotAffordFlag = False

        if ShopLM:
            if sell:
                if IsItemExcludedFromShop(ShopLM, ItemID):
                    ShopNotInterestedFlag = True
                else:
                    item_value = GetShopSellToPrice(ItemID, ShopLM)
                    if GetItemQty(ShopLM.Items, "gold") < item_value:
                        ShopCannotAffordFlag = True
            else:
                item_value = GetShopBuyPrice(ItemID, ShopLM)

        text_strings = []
        if Amount == 1:
            text_strings.append("{size=30}" + tra(item_dict["name"]) + "{/size}")
        else:
            if item_dict["plural"] is not None:
                text_strings.append("{size=30}" + tra(item_dict["plural"]) + " x" + str(Amount) + "{/size}")
            else:
                text_strings.append("{size=30}" + tra(item_dict["name"]) + " x" + str(Amount) + "{/size}")

        text_strings.append("{size=27}{color=#c2c2c2}" + tra(item_dict["desc"]) + "{/size}{/color}")

        BonusColor = Item_BonusColor
        MalusColor = Item_MalusColor

######## story/battle desc
        if IsPlayerInBattle() and BattleScene.PostBattleFlag == False:
            # in battle only care for items that are displayed
            action_key = item_dict.get("on_use_battle")
            if action_key is not None:
                if action_key in ItemActionLib:
                    text_strings.append(ItemActionLib[action_key](Owner_BattleChar = BattleChar, ItemID = ItemID).GetDesc())
                else:
                    text_strings.append("{color=#ff5555}Missing action handler: " + str(action_key) + "{/color}")
        else:
            if item_dict["on_use_story"] is not None:
                for Entry in item_dict["on_use_story"]:
                    if Entry[0] == ItemHealUserStory:
                        text_strings.append(BonusColor + tra(_("Restores health on use: %s")) % Entry[1] + "{/color}")
                    elif Entry[0] == ItemLearnSkill:
                        text_strings.append(BonusColor + tra(_("Teaches skill on use: %s")) % tra(Entry[1]) + "{/color}")
                    elif Entry[0] == ItemRaiseAttStory:
                        text_strings.append(BonusColor + "%s +%s %s" % (tra(GUI_STAT_NAME_MAP[Entry[1][0]]), Entry[1][1], tra(_("(Permanent)"))) + "{/color}")
                    elif Entry[0] == ItemClearInfectionStory:
                        text_strings.append(BonusColor + tra(_("Will reduce your infection level to zero.")) +  "{/color}")
                    elif Entry[0] == ItemRazaEffectUser:
                        text_strings.append(BonusColor + "%s +%s %s" % (tra(GUI_STAT_NAME_MAP["Strength"]), 1, tra(_("(6 hours)"))) + "{/color}")
                        text_strings.append(BonusColor + "%s +%s %s" % (tra(GUI_STAT_NAME_MAP["Endurance"]), 1, tra(_("(6 hours)"))) + "{/color}")
                        text_strings.append(MalusColor + "%s %s %s" % (tra(GUI_STAT_NAME_MAP["Dexterity"]), -2, tra(_("(6 hours)"))) + "{/color}")
                        text_strings.append(MalusColor + "%s: %s %s / %s (%s %s)" % (tra(_("Poison")), 10, tra(_("damage")), tra(_("hour")), 6, tra(_("hours"))) + "{/color}")
                    elif Entry[0] == ItemStrangeMeatPoisonUser:
                        text_strings.append(BonusColor + tra(_("Restores health on use: %s")) % 10 + "{/color}")
                        text_strings.append(MalusColor + "%s: %s / %s (%s %s)" % (tra(_("Poison")), 10, tra(_("hour")), 24, tra(_("hours"))) + "{/color}")
                    elif Entry[0] == ItemAntidoteStory:
                        text_strings.append(BonusColor + tra(_("Cures poisoning")) + "{/color}")
            else:
                if item_dict["show_battle_desc_in_story_mode"] == True:
                    text_strings.append(tra(_("In battle:")))
                    action_key = item_dict.get("on_use_battle")
                    if action_key in ItemActionLib:
                        ItemActionInstance = ItemActionLib[action_key](ItemID = ItemID, Owner_PBCharID = "mc")
                        text_strings.append(ItemActionInstance.GetDesc())
                    else:
                        text_strings.append("{color=#ff5555}Missing action handler: " + str(action_key) + "{/color}")
                if "battle_perma_effects" in item_dict:
                    if item_dict["battle_perma_effects"]:
                        for EffID in item_dict["battle_perma_effects"]:
                            if EffID == "FaymoreArmorRegenWearer":
                                Str = tra(_("In battle, heals 10% of current HP for the wearer every turn"))
                                text_strings.append(BonusColor + Str + "{/color}")
                            elif EffID == "FaymoreBladeRegenParty":
                                Str = tra(_("In battle, heals 5% of current HP for the party every turn"))
                                text_strings.append(BonusColor + Str + "{/color}")

################## attributes
        for AddAttribute, AttributeID in [
            ("add_attr_barter", "Barter"),
            ("add_attr_dex",    "Dexterity"),
            ("add_attr_str",    "Strength"),
            ("add_attr_luck",   "Luck"),
            ("add_attr_end",    "Endurance"),
            ("add_attr_agi",    "Agility")]:
            if item_dict[AddAttribute] != 0:
                if item_dict[AddAttribute] > 0:
                    text_strings.append(BonusColor + "%s: %s" % (tra(GUI_STAT_NAME_MAP[AttributeID]), item_dict[AddAttribute]) + "{/color}")
                else:
                    text_strings.append(MalusColor + "%s: %s" % (tra(GUI_STAT_NAME_MAP[AttributeID]), item_dict[AddAttribute]) + "{/color}")

################# derived stats
### damage
        if item_dict["Damage"] != 0:
            text_strings.append(BonusColor + tra(_("Damage: %s")) % item_dict["Damage"] + "{/color}")
### armor
        if item_dict["Armor"] != 0:
            text_strings.append(BonusColor + tra(_("Armor: %s")) % item_dict["Armor"] + "{/color}")

### mres
        if item_dict["add_stat_mres"] != 0:
            text_strings.append(BonusColor + tra(_("Magic res.: %s")) % item_dict["add_stat_mres"] + "{/color}")

### crit chance
        if item_dict["add_stat_crit_chance"] != 0:
            text_strings.append(BonusColor + tra(_("Critical chance: %s%%")) % item_dict["add_stat_crit_chance"] + "{/color}")

################################
        if item_dict["cannot_lose"]:
            text_strings.append("{color=#ffc4c4}" + tra(_("Cannot transfer")) + "{/color}")
        else:
            if ShopNotInterestedFlag and ItemID != "gold":
                text_strings.append("{size=27}{color=#c2c2c2}" + tra(_("{i}They are not interested in that item.{/i}")) + "{/size}{/color}")
            elif ShopCannotAffordFlag:
                text_strings.append("{size=27}{color=#c2c2c2}" + tra(_("{i}They cannot afford to buy that item from you.{/i}")) + "{/size}{/color}")
            else:
                if Amount == 1:
                    text_strings.append("{color=#fff7cc}" + tra(_("Value: %s")) % str(item_value) + "{/color}")
                else:
                    text_strings.append("{color=#fff7cc}" + tra(_("Value: %s (%s)")) % (str(item_value), str(item_value * Amount)) + "{/color}")

        if DEV_VARIABLES["HOVER_ITEM_IDS_AND_ORIG_VALUE"]:
            text_strings.append(tra(_("{color=#949494}(DEV) ItemID: %s{/color}")) % ItemID)
            if ShopLM:
                text_strings.append(tra(_("{color=#949494}(DEV) original item value: %s (%s){/color}")) % (str(item_dict["value_per_unit"]), str(item_dict["value_per_unit"] * Amount)))

        return "\n".join(text_strings)

########### for quests!
    def ItemAcquiredQuestCall(ItemID, Amount):
        for qstObj in GetAllActiveQuests():
            if hasattr(qstObj, "onItemAcquired"):
                qstObj.onItemAcquired(ItemID, Amount)
    
    def ItemLostQuestCall(ItemID, Amount):
        for qstObj in GetAllActiveQuests():
            if hasattr(qstObj, "onItemLost"):
                qstObj.onItemLost(ItemID, Amount)

init -2 python:
    def GetCharacterGrantedSkills(char_id):
        skills_list = []
        
        if "worldChars" not in globals() or char_id not in worldChars:
            return skills_list
            
        char_data = worldChars[char_id]

        # 1. Fetch learned/tome skills
        char_skills = getattr(char_data, "CharSkills", None)
        if char_skills is None and isinstance(char_data, dict):
            char_skills = char_data.get("CharSkills", {})
            
        if isinstance(char_skills, dict):
            for skill_id in char_skills.keys():
                if skill_id:
                    skills_list.append(str(skill_id).lower())

        # 2. Extract item keys across all slot attributes/dicts
        equipped_items = []
        slots = ["armor", "weapon", "accessory", "acc1", "acc2", "offhand", "head", "chest", "legs", "body"]
        
        for slot in slots:
            item = getattr(char_data, slot, None)
            if item is None and isinstance(char_data, dict):
                item = char_data.get(slot)
                
            if item:
                item_id = getattr(item, "id", getattr(item, "item_id", item))
                if isinstance(item_id, str):
                    equipped_items.append(item_id)

        # 3. Read skill grants from item definitions
        item_db = {}
        if "static_item_defs" in globals():
            item_db.update(static_item_defs)
        if "all_items" in globals():
            item_db.update(all_items)

        for item_id in equipped_items:
            if item_id in item_db:
                item_data = item_db[item_id]
                granted = item_data.get("grants_skill") or item_data.get("teaches_skill") or item_data.get("skill_key")
                if granted:
                    skill_key = str(granted).lower()
                    if skill_key not in skills_list:
                        skills_list.append(skill_key)

        return skills_list