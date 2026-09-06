########### WARNING THERES ALOT OF DUPE CODE IN THERE
########### WARNING THERES ALOT OF COPIED CODE IN THERE
########### WARNING THERES ALOT OF SAME CODE IN THERE

screen inventory(charID = "mc"):
    on "show" action SetVariable("block_wait_dynamic", True)
    on "hide" action SetVariable("block_wait_dynamic", False)
    tag ingame_menu
    modal True

    default Char_ID = charID # identifier of sel. char
    default char_index = player_party.index(Char_ID) # index of player_party list
    default SelItemID = None

    default CurrentPage = 0

    default stat_attr_tab = "stats" # swaps between stat/attribute sections of char side    

    default PartyInvXGrid = 7
    default PartyInvYGrid = 6

    use close_outside("inventory")
    use outer_frame():
        hbox: ### contains two sides: party inv & char sheet
            xalign 0.5
            vbox: #### here party inv section begins
                if GetPartySize() > 1:
                    label STR_UI.PARTY_INV:
                        xalign 0.5
                else:
                    label STR_UI.YOUR_INV:
                        xalign 0.5
                xsize 760
                frame:
                    ysize 670
                    grid PartyInvXGrid PartyInvYGrid:
                        xfill True
                        allow_underfull True
                        xalign 0.5
                        # ItemID wraps 0-x, x-y, dep. on page
                        for ItemID in sorted(player_inv, key = lambda x: all_items[x]["sort_order"])[CurrentPage * (PartyInvXGrid * PartyInvYGrid):CurrentPage * (PartyInvXGrid * PartyInvYGrid) + (PartyInvXGrid * PartyInvYGrid)]:
                            fixed:
                                fit_first True
                                if SelItemID == ItemID:
                                    add "images/gui/inventory_slots/slot_under.webp":
                                        size gui.inventory_stored_item_size
                                        matrixcolor TintMatrix((82, 55, 47))

                                imagebutton:
                                    idle  Transform(all_items[ItemID]["icon"], size = gui.inventory_stored_item_size, matrixcolor = IdentityMatrix())
                                    hover Transform(all_items[ItemID]["icon"], size = gui.inventory_stored_item_size, matrixcolor = BrightnessMatrix(0.2))
                                    if SelItemID != ItemID:
                                        if ItemCanBeUsed(ItemID) or ItemCanBeDropped(ItemID) or GetCharEquippableQty(char_index, ItemID):
                                            action SetLocalVariable("SelItemID", ItemID)
                                        else:
                                            action NullAction()
                                    else:
                                        action SetLocalVariable("SelItemID", None)

                                    hovered TooltipSetUI(GetItemDesc(ItemID, player_inv[ItemID]))
                                    unhovered TooltipClearUI()
                                for party_Char_ID in player_party:
                                    for slot_ID in EQP_SLOTS.ALL:
                                        if worldChars[party_Char_ID][slot_ID] == ItemID:
                                            if party_Char_ID == Char_ID:
                                                add "images/gui/inventory_slots/slot_select.webp":
                                                    size gui.inventory_stored_item_size
                                                    matrixcolor TintMatrix((220, 120, 110))
                                            else:
                                                add "images/gui/inventory_slots/slot_select.webp":
                                                    size gui.inventory_stored_item_size
                                                    matrixcolor TintMatrix((200, 100, 90)) * OpacityMatrix(0.45)
                                                
                                        
                                if player_inv[ItemID] > 1:
                                    text str(player_inv[ItemID]):
                                        align (0.95, 1.0)
                fixed:
                    xalign 0.5
                    xfill True
                    if int(len(list(player_inv.keys())) / (PartyInvXGrid * PartyInvYGrid)) > 0:
                        textbutton _("<< Prev. page"):
                            action If(CurrentPage > 0, 
                                    true = SetLocalVariable("CurrentPage", CurrentPage - 1))
                            xalign 0.0
                    hbox:
                        xalign 0.5
                        textbutton _("(d) Drop"):
                            if SelItemID is not None:
                                if not all_items[SelItemID]["cannot_lose"]:
                                    action [SetLocalVariable("SelItemID", None), Show("drop_item", ItemID = SelItemID)]
                            keysym "K_d"
                        textbutton _("Use"):
                            if SelItemID is not None:
                                if all_items[SelItemID]["on_use_story"] is not None:
                                    action [SetLocalVariable("SelItemID", None), Function(UseItemStory, Char_ID, SelItemID)]
                    if int(len(list(player_inv.keys())) / (PartyInvXGrid * PartyInvYGrid)) > 0:
                        textbutton _("Next page >>"):
                            action If(CurrentPage < int((len(list(player_inv.keys())) - 1) / (PartyInvXGrid * PartyInvYGrid)), 
                                    true = SetLocalVariable("CurrentPage", CurrentPage + 1))
                            xalign 1.0
                        
                        
            null width 5
            vbox: #### char section
                xalign 0.5
                xsize 620
                # char switch buttons, name
                fixed:
                    xalign 0.5
                    xfill True
                    ysize 50
                    textbutton "<<":
                        xalign 0.12
                        if GetPartySize() > 1:
                            if char_index > 0:
                                action [SetLocalVariable("Char_ID", player_party[char_index - 1]), SetLocalVariable("char_index", char_index - 1), TooltipClearUI()]
                        keysym "K_z"
                        hovered TooltipSetUI(tra(_("Prev. character")) + " (z)")
                        unhovered TooltipClearUI()
                    label "%s" % worldChars[Char_ID]["name"]:
                        align (0.5, 0.5)
                    textbutton ">>":
                        xalign 0.88
                        if GetPartySize() > 1:
                            if char_index + 1 < GetPartySize():
                                action [SetLocalVariable("Char_ID", player_party[char_index + 1]), SetLocalVariable("char_index", char_index + 1), TooltipClearUI()]
                        keysym "K_c"
                        hovered TooltipSetUI(tra(_("Next character")) + " (c)")
                        unhovered TooltipClearUI()
                        
                # xp bar
                hbox:
                    xalign 0.5
                    frame:
                        background Null()
                        xsize 150
                        ysize 50
                        text tra(_("Level %s")) % GetCharLevelFromID(Char_ID) xalign 0.9
                    bar:
                        style "bar_teal_256"
                        xalign 0.5
                        yalign 0.5
                        ysize 30
                        value getCurrentXpPercentageToReachNextLevel(Char_ID)
                        range 1.00
                    frame:
                        background Null()
                        xsize 150
                        ysize 50
                        text "%s/%s" % (getCurrentXpInLevel(Char_ID), getXpInLevelToReachNext(Char_ID)):
                            xalign 0.5
                # eqp slots -> portrait -> eqp slots
                hbox:
                    xalign 0.5
                    spacing 5
                    vbox:
                        for slot_ID in ["eqp_chest", "eqp_ring1", "eqp_hand1"]:
                            use equipment_slot(char_index, SelItemID, slot_ID)
                    vbox:
                        imagebutton:
                            align (0.5, 0.5)
                            idle Transform(worldChars[Char_ID]["portrait"], matrixcolor = IdentityMatrix())
                            hover Transform(worldChars[Char_ID]["portrait"], matrixcolor = BrightnessMatrix(0.15))
                            if Char_ID != "mc":
                                if PlayerCanSpeakToPartyChars():
                                    keyboard_focus True
                                    action [Hide("inventory", transition = Dissolve(0.15)), Function(PartyTalkToChar, Char_ID)]
                                    hovered TooltipSetUI(tra(_("Talk to %s")) % tra(worldChars[Char_ID]["name"]))
                                else:
                                    keyboard_focus False
                                    action NullAction()
                                    hovered TooltipSetUI(tra(_("You cannot talk to %s right now")) % tra(worldChars[Char_ID]["name"]))
                                unhovered TooltipClearUI()
                            else:
                                keyboard_focus False
    
                    vbox:
                        for slot_ID in ["eqp_neck", "eqp_ring2", "eqp_hand2"]:
                            use equipment_slot(char_index, SelItemID, slot_ID)
                null height 5
                # hp/ep numbers & bars
                hbox:
                    xalign 0.5
                    frame:
                        background Null()
                        xsize 100
                        ysize 50
                        if StoryCharIsPoisoned(Char_ID):
                            text "%s/%s\n{size=-5}Poison (%sh){/size}" % (worldChars[Char_ID]["Health"], worldChars[Char_ID]["HealthMax"], StoryStatusEffects[Char_ID]["Poison"]):
                                color "#af1414"
                                align (0.5, 0.5)
                        else:
                            text "%s/%s" % (worldChars[Char_ID]["Health"], worldChars[Char_ID]["HealthMax"]):
                                color "#af1414"
                                align (0.5, 0.5)
                    vbox:
                        align (0.5, 0.5)
                        # health bar, curr/max
                        bar:
                            if StoryCharIsPoisoned(Char_ID):
                                style "bar_brgreen_256"
                            else:
                                style "bar_red_256"
                            xalign 0.5
                            value AnimatedValue(worldChars[Char_ID]["Health"], worldChars[Char_ID]["HealthMax"], delay = 0.15)
                        # EP OR mana bar, curr/max
                        bar: 
                            xalign 0.5
                            if worldChars[Char_ID]["is_mage"]:
                                style "bar_blue_256"
                                value AnimatedValue(worldChars[Char_ID]["Mana"], worldChars[Char_ID]["ManaMax"], delay = 0.15)
                            else:
                                style "bar_green_256"
                                value AnimatedValue(worldChars[Char_ID]["Energy"], worldChars[Char_ID]["EnergyMax"], delay = 0.15)
                    # EP OR mana values
                    frame:
                        background Null()
                        xsize 100
                        ysize 50
                        if worldChars[Char_ID]["is_mage"]:
                            text "%s/%s" % (worldChars[Char_ID]["Mana"], worldChars[Char_ID]["ManaMax"]):
                                color "#2219aa"
                                align (0.5, 0.5)    
                        else:
                            text "%s/%s" % (worldChars[Char_ID]["Energy"], worldChars[Char_ID]["EnergyMax"]):
                                color "#22880e"
                                align (0.5, 0.5)    
                null height 10
                # buttons to swap between stats/attr tabs
                hbox:
                    xalign 0.5
                    spacing 10
                    textbutton _("Attributes"):
                        if stat_attr_tab != "attr":
                            action SetLocalVariable("stat_attr_tab", "attr")
                    textbutton _("Battle Stats"):
                        if stat_attr_tab != "stats":
                            action SetLocalVariable("stat_attr_tab", "stats")
                null height 15
                # derived stats tab of char side
                if stat_attr_tab == "stats":
                    hbox:
                        xalign 0.5
                        xsize 500
                        vbox:
                            use attribute_box(worldChars[Char_ID], "Damage")
                            use attribute_box(worldChars[Char_ID], "Armor")
                            use attribute_box(worldChars[Char_ID], "MagicRes")
                        vbox:
                            use attribute_box(worldChars[Char_ID], "AttackRating")
                            use attribute_box(worldChars[Char_ID], "DodgeRating")
                            use attribute_box(worldChars[Char_ID], "CritChance")
                # attributes tab of char side
                else:
                    hbox:
                        xalign 0.5
                        xsize 500
                        vbox:
                            use attribute_box(worldChars[Char_ID], "Strength")
                            use attribute_box(worldChars[Char_ID], "Endurance")
                            if worldChars[Char_ID]["is_mage"]:
                                use attribute_box(worldChars[Char_ID], "Mana_Power")
                            else:
                                use attribute_box(worldChars[Char_ID], "Willpower")
                            use attribute_box(worldChars[Char_ID], "Luck")
                        vbox:
                            use attribute_box(worldChars[Char_ID], "Agility")
                            use attribute_box(worldChars[Char_ID], "Dexterity")
                            if Char_ID == "mc":
                                use attribute_box(worldChars[Char_ID], "Charisma")
                                use attribute_box(worldChars[Char_ID], "Barter")

init python:
    GUI_ATTRIBUTE_ICON_MAP = {
        "Damage":"images/gui/stat_icons/attack.webp",
        "Armor":"images/gui/stat_icons/armor.webp",
        "AttackRating":"images/gui/stat_icons/attack_rating.webp",
        "CritChance":"images/gui/stat_icons/crit_chance.webp",
        "DodgeRating":"images/gui/stat_icons/dodge.webp",
        "Energy":"images/gui/stat_icons/energy.webp",
        "Health":"images/gui/stat_icons/health.webp",
        "MagicRes":"images/gui/stat_icons/magic_res.webp",
        "Mana":"images/gui/stat_icons/mana.webp",
    }

screen attribute_box(CharObj, AttrID, XSize = 220, Icon = False):
    hbox:
        xsize XSize
        if Icon:
            add GUI_ATTRIBUTE_ICON_MAP[AttrID] size (40, 40) align (0.5, 0.5)
        frame:
            textbutton tra(GUI_STAT_NAME_MAP[AttrID]):
                style "button_sneaky"
                hovered TooltipSetUI(tra(GUI_STAT_NAME_MAP[AttrID + "_desc"]))
                keyboard_focus False
                unhovered TooltipClearUI()
                action NullAction()
                xfill True
            xfill True

        frame:
            xalign 1.0
            xminimum 60
            xpadding 15
            # show item-modified attribute value in Parentheses if necessary like 4 (6)
            if "derived_" + AttrID in CharObj and CharObj["derived_" + AttrID] != CharObj[AttrID]:
                hbox:
                    text str(CharObj[AttrID]):
                        xalign 0.5
                    text " "
                    text "%s%s%s" % ("(", CharObj["derived_" + AttrID], ")"):
                        xalign 0.5
                    
            else:
                text str(CharObj[AttrID]):
                    xalign 0.5

screen equipment_slot(char_index, SelItemID, slot_ID):
    fixed:
        fit_first True
        add "images/gui/inventory_slots/%s.webp" % slot_ID:
            size gui.general_icon_size
        imagebutton:
            if worldChars[player_party[char_index]][slot_ID] is not None:
                idle Transform(all_items[worldChars[player_party[char_index]][slot_ID]]["icon"], matrixcolor = IdentityMatrix(), fit = "contain")
                hover Transform(all_items[worldChars[player_party[char_index]][slot_ID]]["icon"], matrixcolor = BrightnessMatrix(0.2), fit = "contain")

                hovered TooltipSetUI(GetItemDesc(worldChars[player_party[char_index]][slot_ID], 1))
                unhovered TooltipClearUI()
                action NullAction()

                if SelItemID is None:
                    action Function(UnequipItem_CharIndex, char_index, slot_ID)
            else:
                idle Transform("images/gui/blank.webp", matrixcolor = IdentityMatrix(), fit = "contain")
                hover Transform("images/gui/blank.webp", matrixcolor = BrightnessMatrix(0.2), fit = "contain")

            if SelItemID is not None:
                if CanEquip(char_index, SelItemID, slot_ID):
                    # i have no idea how or why code below works without issue -- tmm
                    if GetCharEquippableQty(char_index, SelItemID) > 1:
                        action Function(EquipItem, char_index, SelItemID, slot_ID)
                    if GetCharEquippableQty(char_index, SelItemID) == 1:
                        action Function(EquipItem, char_index, SelItemID, slot_ID), SetScreenVariable("SelItemID", None)
                    if GetEquippedQty(SelItemID) == player_inv[SelItemID] - 1:
                        action Function(EquipItem, char_index, SelItemID, slot_ID), SetScreenVariable("SelItemID", None)

        # "can equip into this slot" indicator
        if SelItemID is not None:
            if CanEquip(char_index, SelItemID, slot_ID):
                add Transform("images/gui/inventory_slots/slot_select.webp", fit = "contain")

# just exchange items, as in a chest
screen container(container_dict, ContainerName = _("Container"), DoReturn = False, DoReturnOnTakeAll = False, HideOnTakeAll = False):
    tag ingame_menu
    modal True

    default CurrentPageLeft = 0
    default CurrentPageRight = 0

    use close_outside("container", do_return = DoReturn)
    use outer_frame():
        hbox:
            xalign 0.5
            vbox:
                if GetPartySize() > 1:
                    label STR_UI.PARTY_INV:
                        xalign 0.5
                else:
                    label STR_UI.YOUR_INV:
                        xalign 0.5
                xsize 720
                frame:
                    xalign 0.5
                    ysize 700
                    grid 6 6:
                        xalign 0.5
                        spacing 3
                        ysize 660
                        xfill True
                        allow_underfull True

                        for ItemID in sorted(player_inv, key = lambda x: all_items[x]["sort_order"])[CurrentPageLeft * 36:CurrentPageLeft * 36 + 36]:
                            fixed:
                                fit_first True
                                if all_items[ItemID]["cannot_lose"]:
                                    add "images/gui/inventory_slots/slot_under.webp":
                                        size gui.inventory_stored_item_size
                                        matrixcolor TintMatrix((70, 0, 0))

                                imagebutton:
                                    idle Transform(all_items[ItemID]["icon"], size = gui.inventory_stored_item_size, matrixcolor = IdentityMatrix())
                                    hover Transform(all_items[ItemID]["icon"], size = gui.inventory_stored_item_size, matrixcolor = BrightnessMatrix(0.2))
                                    if all_items[ItemID]["cannot_lose"]:
                                        action NullAction()
                                    else:
                                        if player_inv[ItemID] <= 2:
                                            action Function(TransferItem, player_inv, ItemID, container_dict, FromPlayer = True)
                                        else:
                                            action Show("transfer_item", ItemID = ItemID, from_container = player_inv, to_container = container_dict, FromPlayer = True)
                                    hovered TooltipSetUI(GetItemDesc(ItemID, player_inv[ItemID]))
                                    unhovered TooltipClearUI()

                                for Char_ID in player_party:
                                    for slot_ID in EQP_SLOTS.ALL:
                                        if worldChars[Char_ID][slot_ID] == ItemID:
                                            add "images/gui/inventory_slots/slot_select.webp":
                                                size gui.inventory_stored_item_size
                                                matrixcolor TintMatrix((212, 115, 87))
                                if player_inv[ItemID] > 1:
                                    text str(player_inv[ItemID]):
                                        align (0.95, 1.0)
                if int(len(list(player_inv.keys())) / 36) > 0:
                    hbox:
                        xalign 0.5
                        textbutton _("<< Prev. page"):
                            action If(CurrentPageLeft > 0, 
                                true = SetLocalVariable("CurrentPageLeft", CurrentPageLeft - 1))
                            xalign 0.5
                        null width 50
                        textbutton _("Next page >>"):
                            action If(CurrentPageLeft < int((len(list(player_inv.keys())) - 1) / 36),
                                true = SetLocalVariable("CurrentPageLeft", CurrentPageLeft + 1))
                            xalign 0.5

            vbox:
                xsize 720
                label ContainerName:
                    xalign 0.5
                frame:
                    xalign 0.5
                    ysize 700
                    grid 6 6:
                        xalign 0.5
                        spacing 3
                        ysize 660
                        xfill True
                        allow_underfull True
                        for ItemID in sorted(container_dict, key = lambda x: all_items[x]["sort_order"])[CurrentPageRight * 36:CurrentPageRight * 36 + 36]:
                            fixed:
                                fit_first True
                                imagebutton:
                                    idle Transform(all_items[ItemID]["icon"], size = gui.inventory_stored_item_size, matrixcolor = IdentityMatrix())
                                    hover Transform(all_items[ItemID]["icon"], size = gui.inventory_stored_item_size, matrixcolor = BrightnessMatrix(0.2))
                                    if container_dict[ItemID] <= 2:
                                        action Function(TransferItem, container_dict, ItemID, player_inv)
                                    else:
                                        action Show("transfer_item", ItemID = ItemID, from_container = container_dict, to_container = player_inv)
                                    hovered TooltipSetUI(GetItemDesc(ItemID, container_dict[ItemID]))
                                    unhovered TooltipClearUI()
                                if container_dict[ItemID] > 1:
                                    text str(container_dict[ItemID]):
                                        align (0.95, 1.0)
                fixed:
                    xalign 0.5
                    xfill True
                    if int(len(list(container_dict.keys())) / 36) > 0:
                        textbutton _("<< Prev. page"):
                            action If(CurrentPageRight > 0, 
                                true = SetLocalVariable("CurrentPageRight", CurrentPageRight - 1))
                            xalign 0.0

                    textbutton _("(r) Take all"):
                        xalign 0.5
                        if container_dict:
                            if DoReturnOnTakeAll == True:
                                action [Function(TakeAllItems, container_dict), Return()]
                            else:
                                if HideOnTakeAll == True:
                                    action [Function(TakeAllItems, container_dict), Hide("container", transition = Dissolve(0.15))]
                                else:
                                    action Function(TakeAllItems, container_dict)
                        keysym "K_r"

                    if int(len(list(container_dict.keys())) / 36) > 0:
                        textbutton _("Next page >>"):
                            action If(CurrentPageRight < int((len(list(container_dict.keys())) - 1) / 36), 
                                true = SetLocalVariable("CurrentPageRight", CurrentPageRight + 1))
                            xalign 1.0

screen trade(TradeLMClass):
    tag ingame_menu
    modal True

    default CurrentPageLeft = 0
    default CurrentPageRight = 0

    default ShopLM = TradeLMClass()

    use close_outside("trade", do_return = True)
    use outer_frame():
        hbox:
            xalign 0.5
            vbox:
                xsize 720
                if GetPartySize() > 1:
                    label STR_UI.PARTY_INV:
                        xalign 0.5
                else:
                    label STR_UI.YOUR_INV:
                        xalign 0.5
                frame:
                    xalign 0.5
                    ysize 700
                    grid 6 6:
                        xalign 0.5
                        spacing 3
                        ysize 690
                        xfill True
                        allow_underfull True
                        for ItemID in sorted(player_inv, key = lambda x: all_items[x]["sort_order"])[CurrentPageLeft * 36:CurrentPageLeft * 36 + 36]:
                            fixed:
                                fit_first True
                                if not UI_CanSell(ShopLM, ItemID):
                                    add "images/gui/inventory_slots/slot_under.webp":
                                        size gui.inventory_stored_item_size
                                        matrixcolor TintMatrix((70, 0, 0))
                                imagebutton:
                                    idle    Transform(all_items[ItemID]["icon"], size = gui.inventory_stored_item_size, matrixcolor = IdentityMatrix())
                                    hover   Transform(all_items[ItemID]["icon"], size = gui.inventory_stored_item_size, matrixcolor = BrightnessMatrix(0.2))
                                    if UI_CanSell(ShopLM, ItemID):
                                        if GetMaxToSell(ItemID, ShopLM) <= 2:
                                            action Function(UI_SellItem, ShopLM, ItemID)
                                        else:
                                            action Show("sell_item_stack", ItemID = ItemID, ShopLM = ShopLM)
                                    else:
                                        action NullAction()

                                    hovered TooltipSetUI(GetItemDesc(ItemID, player_inv[ItemID], ShopLM = ShopLM, sell = True))
                                    unhovered TooltipClearUI()
                                for Char_ID in player_party:
                                    for slot_ID in EQP_SLOTS.ALL:
                                        if worldChars[Char_ID][slot_ID] == ItemID:
                                            add "images/gui/inventory_slots/slot_select.webp":
                                                size gui.inventory_stored_item_size
                                                matrixcolor TintMatrix((212, 115, 87))
                                if player_inv[ItemID] > 1:
                                    text str(player_inv[ItemID]):
                                        align (0.95, 1.0)
                if int(len(list(player_inv.keys())) / 36) > 0:
                    hbox:
                        xalign 0.5
                        textbutton _("<< Prev. page"):
                            action If(CurrentPageLeft > 0,
                                true = SetLocalVariable("CurrentPageLeft", CurrentPageLeft - 1))
                            xalign 0.5
                        null width 50
                        textbutton _("Next page >>"):
                            action If(CurrentPageLeft < int((len(list(player_inv.keys())) - 1) / 36),
                                true = SetLocalVariable("CurrentPageLeft", CurrentPageLeft + 1))
                            xalign 0.5

            vbox:
                xsize 720
                label _("Merchant Inventory"):
                    xalign 0.5
                frame:
                    xalign 0.5
                    
                    ysize 700
                    grid 6 6:
                        xalign 0.5
                        spacing 3
                        xfill True
                        ysize 660
                        allow_underfull True

                        for ItemID in sorted(ShopLM.Items, key = lambda x: all_items[x]["sort_order"])[CurrentPageRight * 36:CurrentPageRight * 36 + 36]:
                            fixed:
                                fit_first True
                                if not UI_CanBuy(ItemID, ShopLM):
                                    add "images/gui/inventory_slots/slot_under.webp":
                                        size gui.inventory_stored_item_size
                                        matrixcolor TintMatrix((70, 0, 0))
                                imagebutton:
                                    idle Transform(all_items[ItemID]["icon"], size = gui.inventory_stored_item_size, matrixcolor = IdentityMatrix())
                                    hover Transform(all_items[ItemID]["icon"], size = gui.inventory_stored_item_size, matrixcolor = BrightnessMatrix(0.2))
                                    if UI_CanBuy(ItemID, ShopLM):
                                        if GetMaxToBuy(ItemID, ShopLM) <= 2:
                                            action Function(UI_BuyItem, ShopLM, ItemID)
                                        else:
                                            action Show("buy_item_stack", ItemID = ItemID, ShopLM = ShopLM)
                                    else:
                                        action NullAction()
                                    hovered TooltipSetUI(GetItemDesc(ItemID, ShopLM.Items[ItemID], ShopLM = ShopLM))
                                    unhovered TooltipClearUI()
                                if ShopLM.Items[ItemID] > 1:
                                    text str(ShopLM.Items[ItemID]):
                                        align (0.95, 1.0)
                if int(len(list(ShopLM.Items.keys())) / 36) > 0:
                    hbox:
                        xalign 0.5
                        textbutton _("<< Prev. page"):
                            action If(CurrentPageRight > 0, 
                                true = SetLocalVariable("CurrentPageRight", CurrentPageRight - 1))
                            xalign 0.5
                        null width 50
                        textbutton _("Next page >>"):
                            action If(CurrentPageRight < int((len(list(ShopLM.Items.keys())) - 1) / 36), 
                                true = SetLocalVariable("CurrentPageRight", CurrentPageRight + 1))
                            xalign 0.5

screen transfer_item(ItemID, from_container, to_container = None, FromPlayer = False):
    modal True

    default transfer_amount_max = from_container[ItemID]
    default transfer_amount = max(1, int(transfer_amount_max/2))
    key "w" action SetLocalVariable("transfer_amount", transfer_amount_max)
    key "s" action SetLocalVariable("transfer_amount", 1)
    key "a" action SetLocalVariable("transfer_amount", max(1, min(transfer_amount - 1, transfer_amount_max)))
    key "d" action SetLocalVariable("transfer_amount", max(1, min(transfer_amount + 1, transfer_amount_max)))
    on "show" action TooltipClearUI()

    #add "images/gui/unsorted/black_under.webp"
    use outer_frame(800, 465, padd_top = 30):
        vbox:
            ypos 0.1
            xalign 0.5
            spacing 10
            text all_items[ItemID]["name"]:
                text_align .5
                xalign 0.5
            text tra(_("Transfer %s?")) % transfer_amount:
                    text_align .5
                    xalign 0.5
            add "images/gui/unsorted/splitter_line.webp":
                xalign 0.5
                xsize 0.75
                ysize 20
            bar:
                xalign 0.5
                value ScreenVariableValue("transfer_amount", transfer_amount_max - 1, style = "slider", offset = 1, step = 1)
                range transfer_amount_max
                xsize 600
            hbox:
                xalign 0.5
                spacing 5
                textbutton _("Confirm (e)"):
                    style "confirm_button"
                    keysym ["K_RETURN", "e"]
                    action Function(TransferItem, from_container, ItemID, to_container, transfer_amount, FromPlayer), Hide("transfer_item")
                textbutton _("Cancel (t)"):
                    style "confirm_button"
                    action Hide("transfer_item")
                    keysym config.keymap["gui_rest_menu"]
            if FromPlayer:
                if GetEquippedQty(ItemID) > player_inv[ItemID] - transfer_amount:
                    text tra(_("Transfering will unequip %s.")) % (abs(player_inv[ItemID] - GetEquippedQty(ItemID) - transfer_amount)):
                        text_align .5
                        xalign 0.5

screen buy_item_stack(ItemID, ShopLM):
    modal True

    
    default transfer_amount_max = GetMaxToBuy(ItemID, ShopLM)
    default transfer_amount = max(1, int(transfer_amount_max/2))
    key "w" action SetLocalVariable("transfer_amount", transfer_amount_max)
    key "s" action SetLocalVariable("transfer_amount", 1)
    key "a" action SetLocalVariable("transfer_amount", max(1, min(transfer_amount - 1, transfer_amount_max)))
    key "d" action SetLocalVariable("transfer_amount", max(1, min(transfer_amount + 1, transfer_amount_max)))
    on "show" action TooltipClearUI()

    #add "images/gui/unsorted/black_under.webp"
    use outer_frame(800, 465, padd_top = 30):
        vbox:
            ypos 0.1
            xalign 0.5
            spacing 10
            text all_items[ItemID]["name"]:
                text_align .5
                xalign 0.5
            text tra(_("Buy %s?")) % transfer_amount:
                    text_align .5
                    xalign 0.5
            add "images/gui/unsorted/splitter_line.webp":
                xalign 0.5
                xsize 0.75
                ysize 20
            bar:
                xalign 0.5
                value ScreenVariableValue("transfer_amount", transfer_amount_max - 1, style = "slider", offset = 1, step = 1)
                range transfer_amount_max
                xsize 600
            text tra(_("Total value: %s")) % (GetShopBuyPrice(ItemID, ShopLM) * transfer_amount):
                xalign 0.5
                text_align .5
            hbox:
                xalign 0.5
                spacing 5
                textbutton _("Confirm (e)"):
                    style "confirm_button"
                    keysym ["K_RETURN", "K_e"]
                    action Function(UI_BuyItem, ShopLM, ItemID, transfer_amount), Hide("buy_item_stack")
                textbutton _("Cancel (t)"):
                    style "confirm_button"
                    action Hide("buy_item_stack")
                    keysym config.keymap['gui_rest_menu']

screen sell_item_stack(ItemID, ShopLM):
    modal True

    
    default transfer_amount_max = GetMaxToSell(ItemID, ShopLM)
    default transfer_amount = max(1, int(transfer_amount_max/2))
    key "w" action SetLocalVariable("transfer_amount", transfer_amount_max)
    key "s" action SetLocalVariable("transfer_amount", 1)
    key "a" action SetLocalVariable("transfer_amount", max(1, min(transfer_amount - 1, transfer_amount_max)))
    key "d" action SetLocalVariable("transfer_amount", max(1, min(transfer_amount + 1, transfer_amount_max)))
    on "show" action TooltipClearUI()

    #add "images/gui/unsorted/black_under.webp"
    use outer_frame(800, 465, padd_top = 30):
        vbox:
            ypos 0.1
            xalign 0.5
            spacing 10
            text all_items[ItemID]["name"]:
                text_align .5
                xalign 0.5
            text tra(_("Sell %s?")) % transfer_amount:
                    text_align .5
                    xalign 0.5
            add "images/gui/unsorted/splitter_line.webp":
                xalign 0.5
                xsize 0.75
                ysize 20
            bar:
                xalign 0.5
                value ScreenVariableValue("transfer_amount", transfer_amount_max - 1, style = "slider", offset = 1, step = 1)
                range transfer_amount_max
                xsize 600
            text tra(_("Total value: %s")) % (GetShopSellToPrice(ItemID, ShopLM) * transfer_amount):
                xalign 0.5
                text_align .5
            hbox:
                xalign 0.5
                spacing 5
                textbutton _("Confirm (e)"):
                    style "confirm_button"
                    keysym ["K_RETURN", "K_e"]
                    action Function(UI_SellItem, ShopLM, ItemID, transfer_amount), Hide("sell_item_stack")
                textbutton _("Cancel (t)"):
                    style "confirm_button"
                    action Hide("sell_item_stack")
                    keysym config.keymap['gui_rest_menu']
            if GetEquippedQty(ItemID) > player_inv[ItemID] - transfer_amount:
                text tra(_("Selling will unequip %s.")) % (abs(player_inv[ItemID] - GetEquippedQty(ItemID) - transfer_amount)):
                    text_align .5
                    xalign 0.5

screen drop_item(ItemID):
    modal True

    default transfer_amount = max(1, int(player_inv[ItemID]/2))
    default transfer_amount_max = player_inv[ItemID]
    key "w" action SetLocalVariable("transfer_amount", transfer_amount_max)
    key "s" action SetLocalVariable("transfer_amount", 1)
    key "a" action SetLocalVariable("transfer_amount", max(1, min(transfer_amount - 1, transfer_amount_max)))
    key "d" action SetLocalVariable("transfer_amount", max(1, min(transfer_amount + 1, transfer_amount_max)))
    on "show" action TooltipClearUI()

    #add "images/gui/unsorted/black_under.webp"
    use outer_frame(800, 465, padd_top = 30, padd_bot = 30):
        vbox:
            yalign 0.5
            xalign 0.5
            spacing 10
            text all_items[ItemID]["name"]:
                text_align .5
                xalign 0.5
            text tra(_("Drop %s?")) % transfer_amount:
                text_align .5
                xalign 0.5
            add "images/gui/unsorted/splitter_line.webp":
                xalign 0.5
                xsize 0.75
                ysize 20
            if player_inv[ItemID] > 1:
                bar:
                    xalign 0.5
                    value ScreenVariableValue("transfer_amount", transfer_amount_max - 1, style = "slider", offset = 1, step = 1)
                    range transfer_amount_max
                    xsize 600
            text _("Dropped items cannot be recovered!"):
                text_align .5
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 5
                textbutton _("Confirm (e)"):
                    style "confirm_button"
                    keysym ["K_RETURN", "K_e"]
                    action Function(RemItemFrom, player_inv, ItemID, transfer_amount, FromPlayer = True), Hide("drop_item")
                textbutton _("Cancel (t)"):
                    style "confirm_button"
                    action Hide("drop_item")
                    keysym "K_t"
            if GetEquippedQty(ItemID) > player_inv[ItemID] - transfer_amount:
                text tra(_("Dropping will unequip %s.")) % (abs(player_inv[ItemID] - GetEquippedQty(ItemID) - transfer_amount)):
                    text_align .5
                    xalign 0.5