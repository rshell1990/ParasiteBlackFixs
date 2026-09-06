screen choice(items):
    zorder -1

    default enabled = True
    default hint = ""

    # toggle waiting availability
    on "show" action [Hide("say"), SetVariable("block_wait_dynamic", True)]
    on "hide" action SetVariable("block_wait_dynamic", False)

    frame:
        background Frame("images/gui/story/textbox.webp", Borders(50,115,50,250), tile = False)
        anchor (0.5, 1.0)
        pos (0.5, 1.0)
        xsize 1250
        yminimum 324
        if gui_parts["access_buttons"]:
            bottom_padding 75
        else:
            bottom_padding 30
        if _history_list:
            top_padding 80
        else:
            top_padding 100
        vbox:
            anchor (0.5, 1.0)
            pos (0.5, 1.0)
            spacing 10
            if _history_list:
                # find first non-notif entry (or try to)
                if _history_list[-1].what.startswith("NOTIF_"):
                    
                    if FindIndexOfFirstNonNotifEntryInHistory() is not None:
                        vbox:
                            # oh god
                            if _history_list[FindIndexOfFirstNonNotifEntryInHistory()].who:
                                label _history_list[FindIndexOfFirstNonNotifEntryInHistory()].who:
                                    style "choice_label"
                                    yalign 0.5
                                    xoffset -10
                            else:
                                null height 15
                            text _history_list[FindIndexOfFirstNonNotifEntryInHistory()].what:
                                style "choice_dialogue"
                                xsize 1100
                                xoffset 10    
                else:
                    vbox:
                        if _history_list[-1].who:
                            label _history_list[-1].who:
                                style "choice_label"
                                yalign 0.5
                                xoffset -10
                        else:
                            null height 15
                        text _history_list[-1].what:
                            style "choice_dialogue"
                            xsize 1100
                            xoffset 10
            vbox:
                if _history_list:
                    if _history_list[-1].who:
                        yminimum 125
                    else:
                        yminimum 150
                anchor  (0.5, 1.0)
                pos     (0.5, 1.0)

                $ SkippedAmt = 0

                for idx, i in enumerate(items):
                    if i.kwargs.get("AppearIf") == False:
                        $ SkippedAmt += 1
                        continue

                    $ hint = ""
                    $ enabled = i.kwargs.get("enabled")
                    $ Req_Gold = i.kwargs.get("Req_Gold", 0)
                    $ Req_Charm = i.kwargs.get("Req_Charm", 0)
                    $ Req_Barter = i.kwargs.get("Req_Barter", 0)
                    $ Req_Strength = i.kwargs.get("Req_Strength", 0)
                    $ Req_Agi = i.kwargs.get("Req_Agi", 0)
                    $ Req_Dex = i.kwargs.get("Req_Dex", 0)
                    $ AddLeft = "" # will add stuff like Charisma icon and required value.
                    $ Req_Perk = i.kwargs.get("Req_Perk", None)
                    

                    if Req_Charm > 0:
                        $ AddLeft = "{image=[ICON.DRAMA]} " + tra(_("Charisma %s: ")) % Req_Charm
                        if worldChars["mc"]["derived_Charisma"] < Req_Charm:
                            $ enabled = False
                            $ hint = "\n{size=-5}(" + tra(_("You are not charming enough")) + "){/size}"

                    if Req_Agi > 0:
                        $ AddLeft = tra(_("Agility %s: ")) % Req_Agi
                        if worldChars["mc"]["derived_Agility"] < Req_Agi:
                            $ enabled = False
                            $ hint = "\n{size=-5}(" + tra(_("You are not agile enough")) + "){/size}"
                    
                    if Req_Dex > 0:
                        $ AddLeft = tra(_("Dexterity %s: ")) % Req_Dex
                        if worldChars["mc"]["derived_Dexterity"] < Req_Dex:
                            $ enabled = False
                            $ hint = "\n{size=-5}(" + tra(_("You are not dextrous enough")) + "){/size}"
                    
                    if Req_Barter > 0:
                        $ AddLeft = "{image=[ICON.BARTER]} " + tra(_("Barter %s: ")) % Req_Barter
                        if worldChars["mc"]["derived_Barter"] < Req_Barter:
                            $ enabled = False
                            $ hint = "\n{size=-5}(" + tra(_("Your barter skill is not high enough")) + "){/size}"

                    if Req_Strength > 0:
                        $ AddLeft = tra(_("Strength %s: ")) % Req_Strength
                        if worldChars["mc"]["derived_Strength"] < Req_Strength:
                            $ enabled = False
                            $ hint = "\n{size=-5}(" + tra(_("You are not strong enough")) + "){/size}"
                    
                    if Req_Perk is not None:
                        if Req_Perk == "terrifying":
                            $ AddLeft = "{image=[ICON.INTIMIDATE]}"
                        elif Req_Perk == "perception_warp":
                            $ AddLeft = "{image=[ICON.BRAIN]}"
                        elif Req_Perk == "fem_charm":
                            $ AddLeft = "{image=[ICON.LIPS]}"
                        elif Req_Perk == "chameleon":
                            $ AddLeft = "{image=[ICON.CHAMELEON]}"

                        if not PlayerHasPerk(Req_Perk):
                            $ enabled = False
                            $ hint = "\n{size=-5}(" + tra(_("You lack the required perk: ")) + tra(Lib_Perks[Req_Perk]["name"]) + "){/size}"

                    # disable an option when gold is needed & display amount
                    if Req_Gold > 0 and PlayerItemQty("gold") < Req_Gold:
                        $ enabled = False
                        $ hint = "\n{size=-5}(" + tra(_("You need %s gold")) % Req_Gold + "){/size}"

                    # if player can pay, note how much gold will be paid
                    if Req_Gold > 0 and PlayerItemQty("gold") >= Req_Gold:
                        $ hint = "\n{size=-5}(" + tra(_("You will pay %s gold")) % Req_Gold + "){/size}"

                    hbox:
                        xsize 1100
                        xalign 0.5
                        xoffset -20
                        $ numKey = "%d" % (idx + 1 - SkippedAmt)
                        label "%s" % str(idx + 1 - SkippedAmt):
                            style "choice_label"
                            anchor (0.33335, 0.5)
                            pos (0.5,0.5)
                        textbutton AddLeft + " " + tra(i.caption) + hint:
                            if i.chosen:
                                style "choice_button_seen"
                            else:
                                style "choice_button"
                            yminimum 35
                            xalign 0.5
                            text_xalign 0.5
                            xsize 1050
                            keysym numKey
                            sensitive enabled
                            action [i.action, Function(AddChoiceToHistory, i, _history_list)]

init python:
    def FindIndexOfFirstNonNotifEntryInHistory():
        # assumes history is not empty
        for ReverseIndex, Entry in enumerate(reversed(_history_list)):
            if not Entry.what.startswith("NOTIF_"):
                return len(_history_list) - 1 - ReverseIndex
        return None