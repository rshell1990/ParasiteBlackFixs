screen StartCharacterMenu():
    tag ingame_menu

    modal True

    default Char_ID = "mc"
    # all the on-level-up-changes are done to char itself
    # on revert, leave, tab change - a stored copy overwrites a worldchar[id]
    default CharCopy = copy.deepcopy(worldChars["mc"])

    default Input = None

    default AttributePoints = 0

    use outer_frame:
        vbox:
            null height 15
            label _("Character creation") xalign 0.5
            xalign 0.5
            null height 20
################# charsheet tab. attributes & increasing of, derived stats (damage, armor), portrait, hp/ep, xp to next level
            hbox:
                xalign 0.5
                ############## char attributes
                frame:
                    xalign 0.5
                    xsize 450
                    background Null() # layout purposes
                    vbox:
                        xalign 0.5
                        label _("Attributes") xalign 0.5
                        null height 10
                        for AttributeID in ["Strength", "Endurance", "Willpower", "Agility", "Dexterity", "Luck", "Charisma", "Barter"]:
                            hbox:
                                spacing 5    
                                # subtract point button
                                textbutton "<<":
                                    xsize 50
                                    if worldChars[Char_ID][AttributeID] > 1:
                                        if CanReduceAttribute(Char_ID, AttributeID):
                                            action [SetDict(worldChars[Char_ID], AttributeID, worldChars[Char_ID][AttributeID] - 1),
                                                    SetLocalVariable("AttributePoints", AttributePoints + 1),
                                                    Function(CharHeal, Char_ID), 
                                                    Function(CharRestoreEnergy, Char_ID)]
                                        else:
                                            hovered TooltipSetUI(_("Lower your highest attribute to reduce this one further."))
                                            unhovered TooltipClearUI()
                                            text_color "#ad4040"
                                            action NullAction()
                                # attribute bar w/current value
                                use attribute_box(worldChars[Char_ID], AttributeID)

                                # add attr button
                                if AttributePoints > 0:
                                    textbutton ">>":
                                        xsize 50
                                        if CanRaiseAttribute(Char_ID, AttributeID):
                                            action [SetDict(worldChars[Char_ID], AttributeID, worldChars[Char_ID][AttributeID] + 1),
                                                SetLocalVariable("AttributePoints", AttributePoints - 1),
                                                Function(CharHeal, Char_ID), 
                                                Function(CharRestoreEnergy, Char_ID)]
                                        else:
                                            hovered TooltipSetUI(_("Raise the lowest attribute to develop this one further."))
                                            unhovered TooltipClearUI()
                                            text_color "#ad4040"
                                            action NullAction()
                                else:
                                    null width 50

                ########### char derived stats (dmg, att rating), points distr.
                frame:
                    xsize 450
                    background Null() # layout
                    vbox:
                        xalign 0.5
                        label _("Battle stats") xalign 0.5
                        
                        null height 10
                        for AttributeID in ["Damage", "Armor", "MagicRes", "AttackRating", "DodgeRating", "CritChance"]:
                            use attribute_box(worldChars[Char_ID], AttributeID, XSize = 280)
                        
                        null height 50
                        if AttributePoints > 0:
                            text tra(_("Points to spend: %s")) % AttributePoints xalign 0.5

                ############# char xp, portrait, hp/ep
                frame:
                    xsize 450
                    background Null() # layout
                    vbox:
                        null height 30
                        xalign 0.5

                        ### name input
                        vbox:
                            xsize 400
                            ysize 100
                            xalign 0.5
                            if Input == "Name":    
                                input:
                                    xalign 0.5
                                    exclude '~1234567890=!@#$%^&*()_+/][\\//.,><";:|?' # -`
                                    length 20
                                    value VariableInputValue("player_name")
                                textbutton _("Confirm") action SetLocalVariable("Input", None) xalign 0.5 keysym config.keymap["input_enter"]
                            else:
                                text "%s" % worldChars[Char_ID]["name"] xalign 0.5
                                textbutton _("Change name") action SetLocalVariable("Input","Name") xalign 0.5

                        null height 15
                        # portrait
                        add Transform(worldChars[Char_ID]["portrait"]) align (0.5, 0.5)
                        null height 5
                        
                        # hp/ep bars
                        vbox:
                            align (0.5, 0.5)
                            # health bar, curr/max
                            bar:
                                style "bar_red_256"
                                xalign 0.5
                                value worldChars[Char_ID]["Health"]
                                range worldChars[Char_ID]["HealthMax"]
                            # EP OR mana bar, curr/max
                            bar: 
                                xalign 0.5
                                if worldChars[Char_ID]["is_mage"]:
                                    style "bar_blue_256"
                                    value worldChars[Char_ID]["Mana"]
                                    range worldChars[Char_ID]["ManaMax"]
                                else:
                                    style "bar_green_256"
                                    value worldChars[Char_ID]["Energy"]
                                    range worldChars[Char_ID]["EnergyMax"]
                        
                        # HP/EP values
                        vbox:
                            xalign 0.5
                            # HP value
                            text tra(_("Hitpoints: %s/%s")) % (worldChars[Char_ID]["Health"], worldChars[Char_ID]["HealthMax"]):
                                color "#af1414"
                                align (0.5, 0.5)    
                            # EP OR mana values
                            if worldChars[Char_ID]["is_mage"]:
                                text tra(_("Mana: %s/%s")) % (worldChars[Char_ID]["Mana"], worldChars[Char_ID]["ManaMax"]):
                                    color "#2219aa"
                                    align (0.5, 0.5)    
                            else:
                                text tra(_("Energy: %s/%s")) % (worldChars[Char_ID]["Energy"], worldChars[Char_ID]["EnergyMax"]):
                                    color "#22880e"
                                    align (0.5, 0.5)
            hbox:
                xalign 0.5
                spacing 10
                textbutton _("Revert"):
                    if worldChars[Char_ID] != CharCopy:
                        action [SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy)), SetLocalVariable("AttributePoints", 0)]
                textbutton _("Confirm"):
                    if AttributePoints == 0:
                        action Show("confirm", message = _("Begin the game with this character?"), 
                                                yes_action = [Hide("confirm"), Return()],
                                                no_action = Hide("confirm"),
                                                transition = Dissolve(0.25))
                        default_focus True