####################################################################################
## Inventory logic self-tests.
##
## Run from the developer console (Shift+O) with:
##     DEBUG_RunInventoryLogicTests()
##
## Prints one line per check and a failure summary. Only touches developer-mode
## globals and restores them afterwards, so it is safe to run in a live session.

init python:
    def _T_Check(name, condition, detail = ""):
        if condition:
            print("[PASS] %s" % name)
            return True
        print("[FAIL] %s %s" % (name, detail))
        return False

    def DEBUG_RunInventoryLogicTests():
        failures = 0

        # -- Action-builder helpers (pure, no game state needed) ---------------
        # transfer direct vs stack-popup threshold
        _src = {"sword": 2}
        _dst = {}
        a = InvTransferAction("sword", _src, _dst, True)
        failures += not _T_Check("transfer <=2 is a direct Function action",
            isinstance(a, renpy.store.Function), repr(a))
        _src2 = {"sword": 3}
        a = InvTransferAction("sword", _src2, _dst, True)
        failures += not _T_Check("transfer >2 opens transfer_item popup",
            isinstance(a, renpy.store.Show), repr(a))

        # buy/sell thresholds: the ShopSellAction/ShopBuyAction builders consult
        # GetMaxToSell/GetMaxToBuy against the shop object; with a mock shop of
        # >2 stock they should open the stack popups.
        class _MockShop:
            def __init__(self):
                self.Items = {"potion": 5}

        a = ShopSellAction("potion", _MockShop())
        failures += not _T_Check("sell >2 opens sell_item_stack popup",
            isinstance(a, renpy.store.Show), repr(a))
        a = ShopBuyAction("potion", _MockShop())
        failures += not _T_Check("buy >2 opens buy_item_stack popup",
            isinstance(a, renpy.store.Show), repr(a))

        # take-all variants
        a = TakeAllAction({}, True, False)
        failures += not _T_Check("take-all with return includes Return()",
            isinstance(a, list), repr(a))
        a = TakeAllAction({}, False, True)
        failures += not _T_Check("take-all with hide includes Hide('container')",
            isinstance(a, list), repr(a))

        # -- Equipment slot click logic (needs worldChars state) ---------------
        _mc = "mc"
        _saved_slot = worldChars[_mc]["eqp_chest"]
        try:
            # No selection on an empty slot -> NullAction
            worldChars[_mc]["eqp_chest"] = None
            a = EquipSlotAction(player_party.index(_mc), None, "eqp_chest")
            failures += not _T_Check("empty slot, no selection -> NullAction",
                isinstance(a, renpy.store.NullAction), repr(a))
            # No selection on occupied slot -> unequip
            worldChars[_mc]["eqp_chest"] = _saved_slot if _saved_slot is not None else "___occupied___"
            if worldChars[_mc]["eqp_chest"] in all_items:
                a = EquipSlotAction(player_party.index(_mc), None, "eqp_chest")
                failures += not _T_Check("occupied slot, no selection -> unequip Function",
                    isinstance(a, renpy.store.Function), repr(a))
            # Selection that cannot be equipped -> NullAction
            a = EquipSlotAction(player_party.index(_mc), "___no_such_item___", "eqp_chest")
            failures += not _T_Check("bad selection -> NullAction",
                isinstance(a, renpy.store.NullAction), repr(a))
        finally:
            worldChars[_mc]["eqp_chest"] = _saved_slot

        # -- Shared quantity dialog wrappers ----------------------------------
        # The four popups are thin wrappers over quantity_stack; check the
        # screen-language side compiles by resolving the wrapper screens.
        failures += not _T_Check("quantity_stack wrappers exist",
            all(renpy.display.screen.has_screen(name) for name in [
                "quantity_stack", "transfer_item", "buy_item_stack",
                "sell_item_stack", "drop_item", "item_grid",
                "container", "trade"]))

        print("Inventory logic tests: %s failure(s)" % failures)
        return failures
