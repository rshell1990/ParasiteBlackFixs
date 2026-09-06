screen characters():
    # toggle waiting availability
    on "show" action SetVariable("block_wait_dynamic", True)
    on "hide" action SetVariable("block_wait_dynamic", False)

    tag ingame_menu

    modal True

    default Char_ID = "mc"
    # all the on-level-up-changes are done to char itself
    # on revert, leave, or tab change - a stored copy overwrites a worldchar[id]
    default CharCopy = copy.deepcopy(worldChars["mc"])

    default tab_page = "sheet" # "sheet", "skills", "perks", "AltFormSkills". sheet is where you distr. attributes, rest is self-explan
    on "hide" action SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy))

    use close_outside("characters", do_return = False)#(False if renpy.get_screen("say") or renpy.get_screen("choice") else True))

    use outer_frame:
        vbox:
            xalign 0.5
            fixed:
                xalign 0.5
                xsize 420
                ysize 45
                if GetPartySize() > 1:
                    textbutton "<<":
                        align (0.0, 0.5)
                        if player_party.index(Char_ID) > 0:
                            action [SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy)),
                                    SetLocalVariable("CharCopy", copy.deepcopy(worldChars[player_party[player_party.index(Char_ID) - 1]])), 
                                    SetLocalVariable("Char_ID", player_party[player_party.index(Char_ID) - 1]),
                                    If(player_party[player_party.index(Char_ID) - 1] != "mc" and tab_page == "perks", true = SetLocalVariable("tab_page", "sheet")),
                                    If(worldChars[player_party[player_party.index(Char_ID) - 1]]["HasAltForm"] == False and tab_page == "AltFormSkills", true = SetLocalVariable("tab_page", "sheet"))]
                label "%s" % worldChars[Char_ID]["name"] align (0.5, 0.5)
                if GetPartySize() > 1:
                    textbutton ">>":
                        align (1.0, 0.5)
                        if player_party.index(Char_ID) + 1 < GetPartySize():
                            action [SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy)),
                                    SetLocalVariable("CharCopy", copy.deepcopy(worldChars[player_party[player_party.index(Char_ID) + 1]])), 
                                    SetLocalVariable("Char_ID", player_party[player_party.index(Char_ID) + 1]),
                                    If(player_party[player_party.index(Char_ID) + 1] != "mc" and tab_page == "perks", true = SetLocalVariable("tab_page", "sheet")),
                                    If(worldChars[player_party[player_party.index(Char_ID) + 1]]["HasAltForm"] == False and tab_page == "AltFormSkills", true = SetLocalVariable("tab_page", "sheet"))]
            null height 5
            hbox:
                xsize 1400
                xalign 0.5
                #spacing 100
                #### char sheet tab btn
                if worldChars[Char_ID]["lvlPoints"] > 0:
                    textbutton tra(_("Character sheet (%s)")) % worldChars[Char_ID]["lvlPoints"]:
                        selected tab_page == "sheet"
                        style "button_tab"
                        action [SetLocalVariable("tab_page", "sheet"), 
                                SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy)),
                                ]
                else:
                    textbutton _("Character sheet"):
                        selected tab_page == "sheet"
                        style "button_tab"
                        action [SetLocalVariable("tab_page", "sheet"), 
                                SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy)),
                                ]

                #### skills tab btn
                if worldChars[Char_ID]["skillPoints"] > 0:
                    textbutton tra(Lib_BattleSkillTrees[worldChars[Char_ID]["BattleClass"]]["skills_string"]) + " (%s)" % worldChars[Char_ID]["skillPoints"]:
                        selected tab_page == "skills"
                        style "button_tab" 
                        action [SetLocalVariable("tab_page", "skills"), 
                                SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy)),]
                else:
                    textbutton tra(Lib_BattleSkillTrees[worldChars[Char_ID]["BattleClass"]]["skills_string"]):
                        selected tab_page == "skills"
                        style "button_tab" 
                        action [SetLocalVariable("tab_page", "skills"),
                                SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy)),]
                
                #### extra (para) skills tab btn
                if worldChars[Char_ID]["HasAltForm"] == True:
                    if worldChars[Char_ID]["AltForm_Unlocked"]:
                        if worldChars[Char_ID]["AltForm_SkillPoints"] > 0:
                            textbutton tra(Lib_BattleSkillTrees[worldChars[Char_ID]["AltForm_BattleClass"]]["skills_string"]) + " (%s)" % worldChars[Char_ID]["AltForm_SkillPoints"]:
                                selected tab_page == "AltFormSkills"
                                style "button_tab" 
                                action [SetLocalVariable("tab_page", "AltFormSkills"), 
                                        SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy)),
                                        ]
                        else:
                            textbutton tra(Lib_BattleSkillTrees[worldChars[Char_ID]["AltForm_BattleClass"]]["skills_string"]):
                                selected tab_page == "AltFormSkills"
                                style "button_tab"
                                action [SetLocalVariable("tab_page", "AltFormSkills"), 
                                        SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy)),
                                        ]
                #### perks tab btn
                if Char_ID == "mc":
                    if len(GetNextPerkBunch()) > 0 or len(worldChars["mc"]["perks"]) > 0:
                        if len(GetNextPerkBunch()) > 0:
                            textbutton _("Perks (New)"):
                                selected tab_page == "perks"
                                style "button_tab"
                                action [SetLocalVariable("tab_page", "perks"),
                                        SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy)),
                                        ]
                                
                        else:
                            textbutton _("Perks"):
                                selected tab_page == "perks"
                                style "button_tab"
                                action [SetLocalVariable("tab_page", "perks"),
                                        SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy)),
                                        ]
                
            null height 10
################# charsheet tab. attributes & increasing of, derived stats (damage, armor), portrait, hp/ep, xp to next level
            if tab_page == "sheet":
                vbox:
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
                                    # mc-only attributes
                                    if AttributeID in ["Charisma", "Barter"] and Char_ID != "mc":
                                        continue
                                    hbox:
                                        spacing 5    
                                        # subtract point button
                                        if worldChars[Char_ID][AttributeID] > CharCopy[AttributeID]:                                    
                                            textbutton "<<":
                                                xsize 50
                                                action [SetDict(worldChars[Char_ID], AttributeID, worldChars[Char_ID][AttributeID] - 1), 
                                                    SetDict(worldChars[Char_ID], "lvlPoints", worldChars[Char_ID]["lvlPoints"] + 1),
                                                    Function(LowerHighestAttributeIfNecessary, Char_ID, AttributeID),
                                                    Function(CharHeal, Char_ID), 
                                                    Function(CharRestoreEnergy, Char_ID),
                                                    ]
                                        else:
                                            null width 50
                                        # attribute bar w/current value
                                        use attribute_box(worldChars[Char_ID], AttributeID)
                                        # add point button
                                        if worldChars[Char_ID]["lvlPoints"] > 0:
                                            textbutton ">>":
                                                xsize 50
                                                if CanRaiseAttribute(Char_ID, AttributeID):
                                                    action [SetDict(worldChars[Char_ID], AttributeID, worldChars[Char_ID][AttributeID] + 1),
                                                        SetDict(worldChars[Char_ID], "lvlPoints", worldChars[Char_ID]["lvlPoints"] - 1),
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
                                if worldChars[Char_ID]["lvlPoints"] > 0 or worldChars[Char_ID] != CharCopy:
                                    text tra(_("Points to spend: %s")) % worldChars[Char_ID]["lvlPoints"] xalign 0.5 color "#fd7b5b" at eye_catching_flash
                                    hbox:
                                        xalign 0.5
                                        textbutton _("Revert"):
                                            if worldChars[Char_ID] != CharCopy:
                                                action SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy))
                                        textbutton _("Confirm"):
                                            if worldChars[Char_ID] != CharCopy:
                                                action SetLocalVariable("CharCopy", copy.deepcopy(worldChars[Char_ID]))
                                                at eye_catching_flash
                        ############# char xp, portrait, hp/ep
                        frame:
                            xsize 450
                            background Null() # layout
                            vbox:
                                null height 30
                                xalign 0.5
                                # xp bar
                                vbox:
                                    xalign 0.5
                                    text tra(_("Level %s")) % GetCharLevelFromID(Char_ID) xalign 0.5
                                    bar:
                                        style "bar_teal_256"
                                        xalign 0.5
                                        yalign 0.5
                                        ysize 30
                                        value getCurrentXpPercentageToReachNextLevel(Char_ID)
                                        range 1.00
                                    text "%s/%s" % (getCurrentXpInLevel(Char_ID), getXpInLevelToReachNext(Char_ID)):
                                        xalign 0.5
                                    text tra(_("Total experience: %s")) % worldChars[Char_ID]["experience"] xalign 0.5

                                # portrait
                                imagebutton:
                                    align (0.5, 0.5)
                                    idle Transform(worldChars[Char_ID]["portrait"], matrixcolor = IdentityMatrix())
                                    hover Transform(worldChars[Char_ID]["portrait"], matrixcolor = BrightnessMatrix(0.15))
                                    if Char_ID != "mc":
                                        if PlayerCanSpeakToPartyChars():
                                            keyboard_focus True
                                            action [Hide("characters", transition = Dissolve(0.15)), Function(PartyTalkToChar, Char_ID)]
                                            hovered TooltipSetUI(tra(_("Talk to %s")) % tra(worldChars[Char_ID]["name"]))
                                        else:
                                            keyboard_focus False
                                            action NullAction()
                                            hovered TooltipSetUI(tra(_("You cannot talk to %s right now")) % tra(worldChars[Char_ID]["name"]))
                                        unhovered TooltipClearUI()
                                    else:
                                        keyboard_focus False

                                    
                                null height 5
                                
                                # hp/ep bars
                                vbox:
                                    align (0.5, 0.5)
                                    # health bar, curr/max
                                    bar:
                                        if StoryCharIsPoisoned(Char_ID):
                                            style "bar_brgreen_256"
                                        else:
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
                                    if StoryCharIsPoisoned(Char_ID):
                                        text tra("Hitpoints: %s/%s\n{size=-5}Poison (%sh){/size}") % (worldChars[Char_ID]["Health"], worldChars[Char_ID]["HealthMax"], StoryStatusEffects[Char_ID]["Poison"]):
                                            color "#af1414"
                                            align (0.5, 0.5)    
                                    else:
                                        text tra("Hitpoints: %s/%s") % (worldChars[Char_ID]["Health"], worldChars[Char_ID]["HealthMax"]):
                                            color "#af1414"
                                            align (0.5, 0.5)    
                                    # EP OR mana values
                                    if worldChars[Char_ID]["is_mage"]:
                                        text tra("Mana: %s/%s") % (worldChars[Char_ID]["Mana"], worldChars[Char_ID]["ManaMax"]):
                                            color "#2219aa"
                                            align (0.5, 0.5)    
                                    else:
                                        text tra("Energy: %s/%s") % (worldChars[Char_ID]["Energy"], worldChars[Char_ID]["EnergyMax"]):
                                            color "#22880e"
                                            align (0.5, 0.5)    
                vbox:
                    xalign 0.5
                    null height 10
                    if worldChars[Char_ID]["lvlPoints"] > 0:
                        text "{i}" + tra(_("You have attribute points to distribute to this character.")) + "{/i}" size 20 at eye_catching_flash color "#fd7b5b" xalign 0.5
                    if worldChars[Char_ID]["skillPoints"] > 0 or (worldChars[Char_ID]["HasAltForm"] and worldChars[Char_ID]["AltForm_SkillPoints"] > 0):
                        text "{i}" + tra(_("You have skill points to distribute to this character.")) + "{/i}" size 20 at eye_catching_flash color "#fd7b5b" xalign 0.5
                    if Char_ID == "mc" and len(GetNextPerkBunch()) > 0:
                        text "{i}" + tra(_("You have perk points to distribute to this character.")) + "{/i}" size 20 at eye_catching_flash color "#fd7b5b" xalign 0.5


#################  skills tab. three stubs for off def supp trees
            if tab_page == "skills":
                vbox:
                    xalign 0.5
                    hbox:
                        xalign 0.5
                        spacing 10
                        for SkillTabLabel, SkillTabID in zip([_("Offence"), _("Defence"), _("Support")], ["offence", "defence", "support"]):
                            vbox:
                                label SkillTabLabel xalign 0.5
                                frame:
                                    ysize 550
                                    xsize 440
                                    use SkillTab(Char_ID, SkillTabID, CharClassID = worldChars[Char_ID]["BattleClass"])
                    vbox:
                        null height 10
                        xalign 0.5
                        if worldChars[Char_ID]["skillPoints"] > 0:
                            text tra(_("Points to spend: %s")) % worldChars[Char_ID]["skillPoints"] xalign 0.5 color "#fd7b5b" at eye_catching_flash
                        else:
                            text ""
                        hbox:
                            xalign 0.5
                            spacing 10

                            textbutton _("Revert"):
                                if worldChars[Char_ID] != CharCopy:
                                    action SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy))

                            textbutton _("Confirm"):
                                if worldChars[Char_ID] != CharCopy:
                                    action SetLocalVariable("CharCopy", copy.deepcopy(worldChars[Char_ID]))
                                    at eye_catching_flash

                        null height 30

#################  extra skills tab for mc & markus & elena & kiara
            if tab_page == "AltFormSkills":
                vbox:
                    xalign 0.5
                    hbox:
                        xalign 0.5
                        spacing 10
                        for SkillTabLabel, SkillTabID in zip([_("Offence"), _("Defence"), _("Support")], ["offence", "defence", "support"]):
                            vbox:
                                label SkillTabLabel xalign 0.5
                                frame:
                                    ysize 550
                                    xsize 440
                                    use SkillTab(Char_ID, SkillTabID, CharClassID = worldChars[Char_ID]["AltForm_BattleClass"])
                    vbox:
                        null height 10
                        xalign 0.5
                        if worldChars[Char_ID]["AltForm_SkillPoints"] > 0:
                            text tra(_("Points to spend: %s")) % worldChars[Char_ID]["AltForm_SkillPoints"] xalign 0.5 color "#fd7b5b" at eye_catching_flash
                        else:
                            text ""
                        hbox:
                            xalign 0.5
                            spacing 10

                            textbutton _("Revert"):
                                if worldChars[Char_ID] != CharCopy:
                                    action SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy))

                            textbutton _("Confirm"):
                                if worldChars[Char_ID] != CharCopy:
                                    action SetLocalVariable("CharCopy", copy.deepcopy(worldChars[Char_ID]))
                                    at eye_catching_flash
                        null height 30

#################  perks tab
            if tab_page == "perks":
                hbox:
                    xalign 0.5
                    spacing 40
                    vbox:
                        xsize 1100
                        ## perks list/menu
                        if len(GetNextPerkBunch()) > 0:
                            label _("Choose new perk"):
                                xalign 0.5
                            null height 10
                            frame:
                                xfill True
                                ysize 630
                                vbox:
                                    xfill True
                                    spacing 5
                                    for PerkID, PerkData in GetNextPerkBunch().items():
                                        button:
                                            frame:
                                                xfill True
                                                background Null()
                                                vbox:
                                                    xfill True
                                                    null height 5
                                                    label PerkData["name"] xalign 0.5
                                                    text PerkData["desc"]
                                                    text PerkData["desc_2"] color "#8d918e"
                                                    null height 10
                                            action Function(PlayerAddPerk, PerkID)
                        else:
                            label _("Your perks"):
                                xalign 0.5
                            null height 10
                            frame:
                                xfill True
                                ysize 630
                                viewport:
                                    #xsize 1100
                                    xfill True
                                    ysize 630
                                    scrollbars "vertical"
                                    mousewheel True
                                    draggable True
                                    vbox:
                                        xfill True
                                        spacing 10
                                        for Perk_ID in worldChars["mc"]["perks"]:
                                            vbox:
                                                xfill True
                                                label Lib_Perks[Perk_ID]["name"] xalign 0.5
                                                text Lib_Perks[Perk_ID]["desc"]
                                                text Lib_Perks[Perk_ID]["desc_2"] color "#8d918e"

                    ## char portrait/hp/ep
                    vbox:
                        xalign 0.5
                        null height 75
                        # portrait
                        add Transform(worldChars[Char_ID]["portrait"]) align (0.5, 0.5)
                        null height 5

                        # hp/ep bars
                        vbox:
                            align (0.5, 0.5)
                            # health bar, curr/max
                            bar:
                                if StoryCharIsPoisoned(Char_ID):
                                    style "bar_brgreen_256"
                                else:
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
                            if StoryCharIsPoisoned(Char_ID):
                                text tra("Hitpoints: %s/%s\n%s") % (worldChars[Char_ID]["Health"], worldChars[Char_ID]["HealthMax"], _("Poisoned!")):
                                    color "#af1414"
                                    align (0.5, 0.5)    
                            else:
                                text tra("Hitpoints: %s/%s") % (worldChars[Char_ID]["Health"], worldChars[Char_ID]["HealthMax"]):
                                    color "#af1414"
                                    align (0.5, 0.5)    
                            # EP OR mana values
                            if worldChars[Char_ID]["is_mage"]:
                                text tra("Mana: %s/%s") % (worldChars[Char_ID]["Mana"], worldChars[Char_ID]["ManaMax"]):
                                    color "#2219aa"
                                    align (0.5, 0.5)    
                            else:
                                text tra("Energy: %s/%s") % (worldChars[Char_ID]["Energy"], worldChars[Char_ID]["EnergyMax"]):
                                    color "#22880e"
                                    align (0.5, 0.5)

                        null height 30
                        hbox:
                            xalign 0.5
                            spacing 10
                            textbutton _("Revert"):
                                if worldChars[Char_ID] != CharCopy:
                                    action SetDict(worldChars, Char_ID, copy.deepcopy(CharCopy))

                            textbutton _("Confirm"):
                                if worldChars[Char_ID] != CharCopy:
                                    action SetLocalVariable("CharCopy", copy.deepcopy(worldChars[Char_ID]))
                                    at eye_catching_flash
