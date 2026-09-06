init python:
    @AppendToAllQuests
    class ShopNovarasLibrary(BaseShopLM):
        def __init__(self):
            super().__init__()
            self.WillNotBuyCategories   = GetAllItemShopCats() - {"book"}
            self.WillNotBuyItemIDs      = {"book_dragonwars", "book_darkmages", "book_newheart", "book_mageguide"}

        def onStart(self):
            AddItemTo(self.Items, "gold", RngInt(300, 600))
            self.onMidnight() # 1st restock is manual

        # daily restock, 
        def onMidnight(self):
            super().SimulateTradingItems(self, 
                TargetGold = 500,
                TargetStockValue = 500,
            )

    @AppendToAllQuests
    class DialogueVala(LogicModule):
        def __init__(self):
            super().__init__()

            self.unlocked_bookshelf = False # ask vala first

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_library_int":
                if IsDaytime():
                    btnMods["vala_talk_btn"] = BtnJumpLabel(_("Talk to Vala"), "nov_vala_obj_talk")
                if self.unlocked_bookshelf:
                    btnMods["library_bookshelves"] = BtnShowScreen(_("Bookshelves"), "container", bookshelf_library_novaras, HideOnTakeAll = True)
            return LocButtonMod(directMods = btnMods)

        def onEnter(self):  
            if self.progress == 0:
                if GetLocID() == "novaras_library_int":
                    if IsDaytime():
                        return TriggeredEvent("vala_firstmeet")

        def extraDialogue(self):
            yield ("vala_root", DNode(_("I have books to trade."), "nov_vala_books_trade"))
            if not self.unlocked_bookshelf:
                yield ("vala_root", DNode(_("I would like to read a book."), "book_selection"))
            yield ("vala_root", DNode(_("Nothing for now."), "dialogue_nothing", nextNode = "DNodeExit", order = -100))

        def AddBooks(self):
            for book_ID in ["book_dragonwars", "book_newheart", "book_mageguide", "book_darkmages"]:
                AddItemTo(bookshelf_library_novaras, book_ID)

        def onStart(self):
            QstStart(ShopNovarasLibrary)

label nov_vala_obj_talk:
    show vala at center_f with dissolve
    VALA "Hi there! Need anything?"
    call processDialogue("vala_root") from _call_processDialogue_2
    $ LocEnter()

### vala firstmeet
label vala_firstmeet:
    $ QstSetProgress(DialogueVala, 1)
    call nov_vala_scr_firstmeet from _call_nov_vala_scr_firstmeet
    $ LocEnter()

label book_selection:
    VALA "Sure, pick any book you see around and have a read!"
    $ DialogueVala().unlocked_bookshelf = True
    $ DialogueVala().AddBooks()
    $ LocEnter()

label nov_vala_books_trade:
    VALA "Of course! Show me what you got."
    call screen trade(ShopNovarasLibrary)
    VALA "Anything else?"
    return