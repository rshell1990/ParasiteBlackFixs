init python:
    def UI_CanCraft(Recipe):
        for IngredientID, IngredientQty in Recipe["Ingredients"].items():
            if PlayerItemQty(IngredientID) < IngredientQty:
                return False
        return True

    def CraftItem(Recipe):
        PlayerAddItem(Recipe["ItemID"])
        for IngredientID, IngredientQty in Recipe["Ingredients"].items():
            PlayerRemItem(IngredientID, IngredientQty, Silent = True)
        ### achievement
        if can_unlock_achievement("LOOK_MOM_I_MADE_A_THING"):
            unlock_achievement("LOOK_MOM_I_MADE_A_THING")
        return

    def UpdateCraftRecipesAndIngredientsContainer(SmithyID = None):
        # wow oink oink
        Assert(SmithyID == "drax" or SmithyID == "hamun_smithy", "Smithy id fucked!")
        if SmithyID == "drax":
            RecipesList = DraxCraftRecipes
            SmithyCraftContainer = DraxCraftRecipesAndIngredientsContainer

        elif SmithyID == "hamun_smithy":
            RecipesList = HamunSmithyCraftRecipes
            SmithyCraftContainer = HamunSmithyCraftRecipesAndIngredientsContainer

        for RecipeID in RecipesList:
            RecipeData = AllCraftRecipes[RecipeID]
            if GetItemQty(SmithyCraftContainer, RecipeData["ItemID"]) == 0:
                AddItemTo(SmithyCraftContainer, RecipeData["ItemID"])
            for IngredientID in RecipeData["Ingredients"]:
                if GetItemQty(SmithyCraftContainer, IngredientID) == 0:
                    AddItemTo(SmithyCraftContainer, IngredientID)

screen SmithyCrafting(SmithyID = None):
    tag ingame_menu
    modal True

    use close_outside("SmithyCrafting", do_return = True)
    use outer_frame():
        vbox:
            spacing 10
            xalign 0.5
            label _("Select a recipe") xalign 0.5
            frame:
                xsize 1400
                ysize 710
                vpgrid:
                    cols 3
                    allow_underfull True
                    mousewheel True
                    scrollbars "vertical"
                    spacing 10

                    if SmithyID == "drax":
                        for RecipeID in sorted(list(DraxCraftRecipes)):
                            use SmithyCraftingRecipeEntry(AllCraftRecipes[RecipeID])
                    elif SmithyID == "hamun_smithy":
                        for RecipeID in sorted(list(HamunSmithyCraftRecipes)):
                            use SmithyCraftingRecipeEntry(AllCraftRecipes[RecipeID])

screen SmithyCraftingRecipeEntry(Recipe):
    button:
        idle_background Transform(Frame("images/gui/frames/paper.webp", Borders(0, 0, 0, 0)))
        hover_background Transform(Frame("images/gui/frames/paper.webp", Borders(0, 0, 0, 0)), matrixcolor = BrightnessMatrix(0.15))
        padding (6, 8)
        xalign 0.5

        xsize 445
        vbox:
            null height 15
            #spacing 10
            # item icon n name
            hbox:
                spacing 5
                xalign 0.5
                imagebutton:
                    idle Transform(all_items[Recipe["ItemID"]]["icon"], size = gui.general_icon_size, matrixcolor = IdentityMatrix())
                    hover Transform(all_items[Recipe["ItemID"]]["icon"], size = gui.general_icon_size, matrixcolor = BrightnessMatrix(0.2))
                    action NullAction()
                    hovered TooltipSetUI(GetItemDesc(Recipe["ItemID"]))
                    unhovered TooltipClearUI()
                text all_items[Recipe["ItemID"]]["name"] yalign 0.5 color "#171616"
            # ingredientos
            frame:
                background Null()
                xalign 0.5
                xfill True
                ysize 310
                vbox:
                    yalign 0.25
                    xalign 0.5
                    for IngredientID in Recipe["Ingredients"]:
                        hbox:
                            imagebutton:
                                idle Transform(all_items[IngredientID]["icon"], size = (64, 64), matrixcolor = IdentityMatrix())
                                hover Transform(all_items[IngredientID]["icon"], size = (64, 64), matrixcolor = BrightnessMatrix(0.2))
                                action NullAction()
                                hovered TooltipSetUI(GetItemDesc(IngredientID))
                                unhovered TooltipClearUI()
                            if PlayerItemQty(IngredientID) < Recipe["Ingredients"][IngredientID]:
                                text "{color=#57040b}%sx %s (%s){/color}" % (Recipe["Ingredients"][IngredientID], tra(all_items[IngredientID]["name"]), GetItemQty(player_inv, IngredientID)) yalign 0.5 color "#171616"
                            else:
                                text "%sx %s (%s)" % (Recipe["Ingredients"][IngredientID], tra(all_items[IngredientID]["name"]), GetItemQty(player_inv, IngredientID)) yalign 0.5 color "#171616"

        action If(UI_CanCraft(Recipe), true = [Function(CraftItem, Recipe), Return()], false = NullAction())
