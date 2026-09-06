init python:
    def PlayerAddItem(ItemID, Amount = 1, Silent = False, using_cheat = False):
        # checks
        Assert(ItemID in static_item_defs, "Item ID %s not found in static_item defs" % ItemID)
        Assert(ItemID in all_items, "Item ID %s not found in all_items" % ItemID)
        Assert(Amount > 0, "wtf? called playeradditem with less than 1 item count")

        # add item
        AddItemTo(player_inv, ItemID, Amount)

        # achievement
        if ItemID == "gold":
            # achievmeent
            if not using_cheat:
                store._total_earned_gold += Amount
                if store._total_earned_gold > 10000 and can_unlock_achievement("DEEP_POCKETS"):
                    unlock_achievement("DEEP_POCKETS")
                if store._total_earned_gold > 50000 and can_unlock_achievement("ALL_THAT_GLITTERS"):
                    unlock_achievement("ALL_THAT_GLITTERS")
                if store._total_earned_gold > 100000 and can_unlock_achievement("A_KINGS_RANSOM"):
                    unlock_achievement("A_KINGS_RANSOM")

        # notif
        if not Silent:
            notify_text = []
            ItemDict = all_items[ItemID]
            notify_text.append(tra(_("Acquired")))
            if Amount == 1:
                notify_text.append(tra(ItemDict["name"]))
            else:
                notify_text.append("x%s" % Amount)
                if ItemDict["plural"] is not None:
                    notify_text.append(tra(ItemDict["plural"]))
                else:
                    notify_text.append(tra(ItemDict["name"]))

            AddNotif(" ".join(notify_text), Kind = ("gold_handle" if ItemID == "gold" else "item_add"))
        return

    def PlayerRemItem(ItemID, Amount = 1, Silent = False, MuteSfx = False):
        if _in_replay:
            return
        # checks
        if Amount <= 0:
            return
        Assert(ItemID in static_item_defs, "Item ID %s not found in static_item defs" % ItemID)
        Assert(ItemID in all_items, "Item ID %s not found in all_items" % ItemID)

        # rem item
        RemItemFrom(player_inv, ItemID, Amount, FromPlayer = True)

        if MuteSfx == False:
            # sound
            if ItemID == "gold":
                # gold sound
                renpy.music.play(renpy.random.choice(soundLib["item_handle_coins"]), channel = "sound", loop = False, relative_volume = 0.85)
            else:
                # generic item sound
                renpy.music.play(renpy.random.choice(soundLib["item_handle_generic"]), channel = "sound", loop = False, relative_volume = 0.85)

        # notif
        if not Silent:
            notify_text = []
            ItemDict = all_items[ItemID]
            notify_text.append(tra(_("Lost")))
            if Amount == 1:
                notify_text.append(tra(ItemDict["name"]))
            else:
                notify_text.append("x%s" % Amount)
                if ItemDict["plural"] is not None:
                    notify_text.append(tra(ItemDict["plural"]))
                else:
                    notify_text.append(tra(ItemDict["name"]))
            
            AddNotif(" ".join(notify_text), Kind = "item_rem")
        return

    def PlayerItemQty(ItemID):
        return GetItemQty(player_inv, ItemID)
    def PlayerHasItem(ItemID):
        return PlayerItemQty(ItemID) > 0

#################################################
# this is where you add all new containers 
    def BuildAllItemContainers():
        VerboseLog_General = False

        store.AllContainers = {}

################ shops list
        for QstObj in GetAllQuests():
            if isinstance(QstObj, BaseShopLM):
                store.AllContainers[QstObj.__class__.__name__] = QstObj.Items

#################################################
################ containers (like chests & bookshelves)
        ContainerIDList = [
            "player_inv",
            "chest_mc_house",
            "bookshelf_library_novaras",
            "bookshelf_library_hamun",
            "bookshelf_comingstorm_special",
        ]

        for ContainerID in ContainerIDList:
            if not hasattr(store, ContainerID):
                if VerboseLog_General:
                    print("Adding container: %s" % ContainerID)
                setattr(store, ContainerID, {})
            store.AllContainers[ContainerID] = getattr(store, ContainerID)
#################################################
################ recipe containers (transient-ish, for crafters)
        RecipeContainersList = [
            "DraxCraftRecipesAndIngredientsContainer",
            "HamunSmithyCraftRecipesAndIngredientsContainer"
        ]

        for RecipeContainerID in RecipeContainersList:
            if not hasattr(store, RecipeContainerID):
                if VerboseLog_General:
                    print("Adding recipe container: %s" % RecipeContainerID)
                setattr(store, RecipeContainerID, {})
            store.AllContainers[RecipeContainerID] = getattr(store, RecipeContainerID)
        return

    def TakeAllItems(container, Silent = False): # by UI only
        for ItemID in list(container):
            TransferItem(from_container = container, ItemID = ItemID, to_container = player_inv, Amount = container[ItemID], Silent = Silent)
        return

    # by UI and by end-battle autoloot
    def TransferItem(from_container, ItemID, to_container, Amount = 1, FromPlayer = False, ShopLM = None, sell = False, Silent = True):
        from_container[ItemID] -= Amount
        if from_container[ItemID] == 0:
            from_container.pop(ItemID)
        if FromPlayer:
            UnequipIfMissing(ItemID)

        if ItemID in to_container:
            to_container[ItemID] += Amount
        else:
            to_container[ItemID] = Amount

        if ShopLM is not None:
            if sell:
                TransferItem(to_container, "gold", from_container, GetShopSellToPrice(ItemID, ShopLM) * Amount)
            else:
                TransferItem(to_container, "gold", from_container, GetShopBuyPrice(ItemID, ShopLM) * Amount)

        # clears tooltip (like under cursor) if it was last item
        if ItemID not in from_container:
            TooltipClear()

        if to_container == player_inv:
            ItemAcquiredQuestCall(ItemID, Amount)
        if from_container == player_inv:
            ItemLostQuestCall(ItemID, Amount)

        if not Silent:
            notify_text = []
            if Amount == 1:
                notify_text.append(tra(_("Acquired")))
                notify_text.append(tra(all_items[ItemID]["name"]))
            else:
                notify_text.append(tra(_("Acquired")))
                notify_text.append("x%s" % Amount)
                notify_text.append(tra(all_items[ItemID]["plural"]))

            if ItemID == "gold":
                AddNotif(" ".join(notify_text), Kind = "gold_handle")
            else:
                AddNotif(" ".join(notify_text), Kind = "item_add")
        return

    def GetItemQty(Container, ItemID):
        Result = (Container[ItemID] if ItemID in Container else 0)
        return Result

    def RemItemFrom(Container, ItemID, Amount = 1, FromPlayer = False):
        Assert(ItemID in static_item_defs, "Item ID %s not found in static_item defs" % ItemID)
        Assert(ItemID in all_items, "Item ID %s not found in all_items" % ItemID)
        if ItemID not in Container:
            return
        Container[ItemID] -= Amount
        if Container[ItemID] <= 0:
            Container.pop(ItemID)
        if FromPlayer:
            ItemLostQuestCall(ItemID, Amount)
            UnequipIfMissing(ItemID)
        return

    def AddItemTo(Container, ItemID, Amount = 1):
        Assert(ItemID in static_item_defs, "Item ID %s not found in static_item defs" % ItemID)
        Assert(ItemID in all_items, "Item ID %s not found in all_items" % ItemID)
        if ItemID in Container:
            Container[ItemID] += Amount
        else:
            Container[ItemID] = Amount
        # do quest trigger hook
        if Container == player_inv:
            ItemAcquiredQuestCall(ItemID, Amount)
        return