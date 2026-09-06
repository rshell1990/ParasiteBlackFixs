init python:
    @AppendToAllQuests
    class QstFromAnotherWorld(BaseQuest):
        GOALS = {0: QuestStage(_("Return Home"),                        hintTxt = _("I should head home. [regina_ref_cap!t] must've lost her mind over me missing...")),
            1: QuestStage(_("Go to Markus' house"),                     hintTxt = _("Regina was happy to see me in one piece. I should now go to Markus' place, so that we can move on with the whole Adventurers Guild thing...")),
            2: QuestStage(_("Follow Markus into the Valley of Death"),  hintTxt = _("Markus wants to try the... benefits of our otherworldly companions far beyond the city walls. I hope this won't backfire on us...")),
            3: QuestStage(_("Explore your new 'form'"),                 hintTxt = _("The beings inside us certainly know how to impress their hosts. We got stronger and faster, although our looks would be terrifying for a normal human being."))}
        
        TITLE = _("From another world")
        DESCRIPTION = _("I have survived my time in the Scouts... But at what cost? Something {i}strange{/i} has clearly happened to me and Markus.")

        def __init__(self):
            super().__init__()

            self.XpReward = 400
            self.LetVesDie = False
            self.IsMain = True

        def locationMod(self):
            btnMods = {}
            return LocButtonMod(directMods = btnMods)

        def onComplete(self):
            QstStart(EventNovarasMarkusTavernPostFaw)
            QstStart(EventSebastianGuardPostFawOneOff)

            BlockWaitGlobal(False)

            WorldMapLocAdd("valley_of_death")

            gui_parts["world_map"] = True

            CharSetVar("kiara", "default_look", "hooded")
            CharSetVar("kiara", "portrait", "images/characters/kiara/portrait_hooded.webp")

            CharSetClothes("kiara", "normal")

            CharAltFormUnlock("mc")
            CharAltFormUnlock("markus")

            CharMeet("lukkan", Silent = True)
            CharMeet("skallion", Silent = True)

            if self.LetVesDie:
                wLocs["ves_camp"].displayName = _("Desert camp")
                wLocs["ves_tent_int"].displayName = _("Desert camp tent")
            else:
                CharMeet("ves", Silent = True)
                QstStart(DialogueVes)
                QstStart(RomanceVes)

            QstStart(TravelMine)
            QstStart(EventJackalGirlEncounter)
            QstStart(VizuraCaravan)
            QstStart(EventFortressInn)
            QstStart(TravelNodesRandomizer)

            QstStart(EventNijahRescue)
            QstStart(ExploreLakeBalun)
            QstStart(PrimerBiteBark)
            QstStart(EventPartyBanter_Cities)
            QstStart(LukkanTavernEncounter)
            QstStart(PrimerQstProperReunion)            
            return