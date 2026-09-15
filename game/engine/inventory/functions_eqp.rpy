init -2 python:
    # silently fails if no item or cant eqp
    def PlayerPartyCharEquipItem(CharID, ItemID, DirectSlotID = None):
        VerboseLog_General = False
        if PlayerItemQty(ItemID) < 1:
            if VerboseLog_General:
                print("soft error: tried PlayerPartyCharEquipItem with itemID %s but item was not found in player inventory" % ItemID)
            return
        if not CharInParty(CharID):
            if VerboseLog_General:
                print("soft error: tried PlayerPartyCharEquipItem with charID %s but char was not found in player party" % CharID)
            return
        # set forced slot if present
        if DirectSlotID is not None:
            TargetSlot = DirectSlotID
        # find slot
        else:
            Slots = all_items[ItemID]["eqp_slots"]
            FoundSlot = False
            for SlotID in Slots:
                if worldChars[CharID][SlotID] == None:
                    TargetSlot = SlotID
                    FoundSlot = True
            # if did not find free slot, we'll just force-equip into first slot
            if FoundSlot == False:
                TargetSlot = Slots[0]
        # unequip if theres shit in target slot
        UnequipItem_CharID(CharID, TargetSlot)
        # eqp item
        EquipItem(player_party.index(CharID), ItemID, TargetSlot, SetMTTToItemDesc = False)
        return

    def CanEquip(char_index, ItemID, slot_ID):
        if worldChars[player_party[char_index]][slot_ID] is not ItemID:
            if GetEquippedQty(ItemID) < player_inv[ItemID]:
                if all_items[ItemID]["eqp_slots"] is not None:
                    slots = all_items[ItemID]["eqp_slots"]
                    if slot_ID in slots:
                        return True
        return False

    def GetCharEquippableQty(char_index, ItemID):
        return_val = 0

        if GetEquippedQty(ItemID) == player_inv[ItemID]:
            return return_val

        for slot_ID in EQP_SLOTS.ALL:
            if CanEquip(char_index, ItemID, slot_ID):
                return_val += 1

        return return_val

    def EquipItem(char_index, ItemID, slot_ID, SetMTTToItemDesc = True):
        Char = worldChars[player_party[char_index]]

        OrigHealthFactor = Char["Health"] / Char["HealthMax"]
        Char[slot_ID] = ItemID

        item_def = all_items.get(ItemID, {})
        if "grants_skill" in item_def:
            skill = item_def["grants_skill"]
            
            # 1. Update CharSkills dict
            if "CharSkills" in Char:
                Char["CharSkills"][skill] = Char["CharSkills"].get(skill, 0) + 1

            # 2. Update learned_skills as a dictionary (SkillID: Level)
            if "learned_skills" in Char:
                if not isinstance(Char["learned_skills"], dict):
                    Char["learned_skills"] = {}
                Char["learned_skills"][skill] = Char["learned_skills"].get(skill, 0) + 1

        Char["Health"] = min(max(math.ceil(Char["HealthMax"] * OrigHealthFactor), 1), Char["HealthMax"])

        if SetMTTToItemDesc:
            TooltipSet(GetItemDesc(ItemID))
        renpy.restart_interaction()
        return

    def UnequipItem(Char, Slot_ID):
        ItemID = Char.get(Slot_ID)

        if ItemID and ItemID in all_items:
            item_def = all_items[ItemID]
            if "grants_skill" in item_def:
                skill = item_def["grants_skill"]
                
                # 1. Cleanup CharSkills
                if "CharSkills" in Char and skill in Char["CharSkills"]:
                    Char["CharSkills"][skill] -= 1
                    if Char["CharSkills"][skill] <= 0:
                        del Char["CharSkills"][skill]
                
                # 2. Cleanup learned_skills dict
                if "learned_skills" in Char and isinstance(Char["learned_skills"], dict):
                    if skill in Char["learned_skills"]:
                        Char["learned_skills"][skill] -= 1
                        if Char["learned_skills"][skill] <= 0:
                            del Char["learned_skills"][skill]

        OrigHealthFactor = Char["Health"] / Char["HealthMax"]
        Char[Slot_ID] = None
        Char["Health"] = min(max(int(Char["HealthMax"] * OrigHealthFactor), 1), Char["HealthMax"])

        TooltipClear()
        renpy.restart_interaction()
        return

    def UnequipItem_CharID(Char_ID, slot_ID):
        Char = worldChars[Char_ID]
        UnequipItem(Char, slot_ID)
        return

    def UnequipItem_CharIndex(char_index, slot_ID):
        Char = worldChars[player_party[char_index]]
        UnequipItem(Char, slot_ID)
        return

    def GetEquippedQty(ItemID):
        equipped_qty = 0 # assumes 1 per slot
        for char_ID in player_party:
            for slot_ID in EQP_SLOTS.ALL:
                if worldChars[char_ID][slot_ID] == ItemID:
                    equipped_qty += 1
        return equipped_qty

    def UnequipIfMissing(ItemID):
        # case 1, no equipped items left in inv: strip ALL party eqp slots
        if ItemID not in player_inv:
            for char_ID in player_party:
                for slot_ID in EQP_SLOTS.ALL:
                    if worldChars[char_ID][slot_ID] == ItemID:
                        UnequipItem(worldChars[char_ID], slot_ID)

        # case 2, SOME eqp. items left in inv: strip SOME party eqp slots at random
        else:
            equipped_qty = GetEquippedQty(ItemID)
            if equipped_qty > player_inv[ItemID]:
                amount_to_strip = equipped_qty - player_inv[ItemID]
                char_slotID = []
                for char_ID in player_party:
                    for slot_ID in EQP_SLOTS.ALL:
                        if worldChars[char_ID][slot_ID] == ItemID:
                            char_slotID.append((char_ID, slot_ID))
                for i in range(0, amount_to_strip):
                    UnequipItem(worldChars[char_slotID[i][0]], char_slotID[i][1])