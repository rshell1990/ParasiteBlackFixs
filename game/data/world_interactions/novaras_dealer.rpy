init python:
    @AppendToAllQuests
    class ShopNovarasDealer(BaseShopLM):
        def __init__(self):
            super().__init__()
            self.WillNotBuyCategories = GetAllItemShopCats() - {"weapon", "illegal"}

        def onStart(self):
            AddItemTo(self.Items, "gold", 500)
            self.onMidnight()
            return

        # restock 
        def onMidnight(self):
            super().SimulateTradingItems(self, 
                TargetGold = 1500,
                TargetStockValue = 1500,
                RestockItemsPool = {
                    "potion_heal_minor":{
                        "restock_if_below":8,
                        "daily_amt":5.0},
                    "potion_antidote":{
                        "restock_if_below":4, 
                        "daily_amt":2.0},
                    "raza_seed":{
                        "restock_if_below":8,
                        "daily_amt":4.0},
                },
            )
            return

    @AppendToAllQuests
    # this only handles the repeated interactions (shopping)
    class NovarasDealer(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_mage":
                if not IsDaytime():
                    btnMods["btn_novaras_mage_dist_dealer"] = BtnJumpLabel(_("Find the dealer"), "novaras_dealer_mage_dist_rep")
            return LocButtonMod(directMods = btnMods)

        def onStart(self):
            QstStart(ShopNovarasDealer)
            return
        
label novaras_dealer_mage_dist_rep:
    
    show cg_dealer at center with dissolve
    DEALER "Hello again."
    DEALER "Interested in doing some business?"
    menu:
        "Show me what you've got.":
            DEALER "Take a look..."
            call screen trade(ShopNovarasDealer)
        "I'm good.":
            DEALER "Should you change your mind..."
    DEALER "You know where to find me."
    $ LocEnter()
