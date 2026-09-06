init python:
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

        # calc orig hp %
        OrigHealthFactor = Char["Health"] / Char["HealthMax"]
        # equip item
        Char[slot_ID] = ItemID
        # scale hp to that orig factor
        Char["Health"] = min(max(math.ceil(Char["HealthMax"] * OrigHealthFactor), 1), Char["HealthMax"])

        # this is important for inv screens
        if SetMTTToItemDesc:
            TooltipSet(GetItemDesc(ItemID))
        return

    def UnequipItem_CharIndex(char_index, slot_ID):
        Char = worldChars[player_party[char_index]]
        UnequipItem(Char, slot_ID)
        return

    def UnequipItem_CharID(Char_ID, slot_ID):
        Char = worldChars[Char_ID]
        UnequipItem(Char, slot_ID)
        return

    def UnequipItem(Char, Slot_ID):
        # calc orig hp %
        OrigHealthFactor = Char["Health"] / Char["HealthMax"]
        # unequip item
        Char[Slot_ID] = None
        # scale hp to that orig factor
        Char["Health"] = min(max(int(Char["HealthMax"] * OrigHealthFactor), 1), Char["HealthMax"])

        TooltipClear()
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
                        worldChars[char_ID][slot_ID] = None

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
                    worldChars[char_slotID[i][0]][char_slotID[i][1]] = None