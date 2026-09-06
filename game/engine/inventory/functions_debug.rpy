init python:
    # manual utility
    def DEBUG_CheckItemCats():
        ExistingCats = {}
        for ItemID, ItemData in static_item_defs.items():
            if ItemID == "gold":
                continue
            if ItemID.startswith("qst_"):
                continue
            if "shop_category" not in ItemData:
                print("Item missing cat: %s" % (ItemID))
            else:
                if ItemData["shop_category"] not in ExistingCats:
                    ExistingCats[ItemData["shop_category"]] = 1
                else:
                    ExistingCats[ItemData["shop_category"]] += 1

        print("All items by cats:")
        for Entry, Val in ExistingCats.items():
            print("%s: %s" % (Entry, Val))
        return ""

    def DEBUG_PlayerAddAllItems(Amount = 1): # dev only
        for ItemID in all_items:
            AddItemTo(player_inv, ItemID, Amount)
        return

    def DEBUG_PlayerRemoveAllItems(): # dev only (actually used by DarkPassenger quest)
        for ItemID in list(player_inv):
            RemItemFrom(player_inv, ItemID, Amount = player_inv[ItemID], FromPlayer = True)
        return
