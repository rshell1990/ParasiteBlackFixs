init python:
    @AppendToAllQuests
    class QstReginaPackage(BaseQuest):
        GOALS = {
            0: QuestStage(_("Visit the blacksmith"), 
                trackTag = "btn_novaras_blacksmith", 
                hintTxt = _("I can find the smithy of Novaras in the Farmlands district to the north.")),
            1: QuestStage(_("Collect bronze scraps for Drax (5)"), 
                hintTxt = _("I have to collect some bronze scraps off Demorai scout parties lurking at the Valley of Death. They won't just hand it over, that's for sure."), 
                trackTag = "btn_novaras_blacksmith"),
            2: QuestStage(_("Pickup the package"), 
                hintTxt=_("Drax will need some time to construct whatever it is [regina_ref!t] needs. It'll take a day."), 
                trackTag = "btn_novaras_blacksmith"),
            3: QuestStage(_("Give the package to Regina"), 
                trackTag = "btn_mc_house"),
            }
        TITLE = _("Regina's Package")
        DESCRIPTION = _("[regina_ref_cap!t] has asked me to collect a package for her from the blacksmith, I wonder what it could be?")

        def __init__(self):
            super().__init__()
    
            self.XpReward = 300

        def onComplete(self):
            # Enable dildo event
            QstStart(EventReginaDildo)
            EventReginaDildo().dildoEvent = True
            CharMeet("arlena", Silent = True)
            return

        def onEnter(self):  
            if GetLocID() == "novaras_blacksmith":
                if IsDaytime():
                    if self.progress == 0:
                        return TriggeredEvent("reginaPackage_intro")

        def onPreSleepMcHouse(self):
            if self.progress >= 4 and GetLocID() == "mc_house_bedroom":
                if RngInt(1, 4) == 1:
                    return TriggeredEvent("reginaPackage_dildo")

        def extraDialogue(self):
            if self.progress == 1:
                if PlayerItemQty("bronze_scraps") < 5:
                    yield ("drax_root", DNode(_("I don't have enough bronze yet..."), "reginaPackage_noBronze"))
                else:
                    yield ("drax_root", DNode(_("Here is the bronze scrap you wanted."),"drax_bronzeDeliver1"))

            if self.progress == 2 and self.delayCheck():
                yield ("drax_root", DNode(_("Is [regina_ref!t]’s gift ready?"), "drax_getGift", order = 5))
            if self.progress == 3:
                yield ("regina_root", DNode(_("I’ve got that thing you wanted from the Blacksmiths."),"regina_deliverPackage", order = 5))

label reginaPackage_noBronze:
    DRAX "That's unfortunate."
    DRAX "You can scrap some off these demorai lurkers outside the city walls."
    return

label reginaPackage_intro:
    call blacksmithscene1 from _call_blacksmithscene1
    $ QstStart(QstDaughterOfMetal)
    $ QstSetProgress(QstReginaPackage, 1)
    $ QstStart(DialogueDrax)
    $ QstStart(DemoraiHuntButton)
    return

label drax_getGift:
    MC @talk 'Is [regina_ref!t]’s gift ready?'
    DRAX 'Here you go, even packaged it up nicely for you.'
    $ PlayerAddItem("qst_regina_package")
    $ QstSetProgress(QstReginaPackage, 3)
    MC @talk 'Thanks, Drax.'
    DRAX 'Anything else you need now?'
    return

label drax_bronzeDeliver1:
    $ DialogueDrax().AgreedToBringMoreBronze = True
    $ PlayerRemItem("bronze_scraps", 5)
    $ PlayerAddItem("gold", 100)
    jump qstReginaPackage_DraxCollectedBronze

label regina_deliverPackage:
    REGINA @talk 'Oh! Good to hear!'
    MC @talk 'Here you go.'
    $ PlayerRemItem("qst_regina_package")
    #EN. PLAYER LOSES THE BOXED GIFT ITEM.'
    REGINA @talk 'Thank you, dear.'
    'Planting a soft kiss on my cheek, [regina_ref!t] smiled.'
    $ CharChangeRel("regina", 1)
    REGINA @talk 'Here, for the next time you and Markus go out drinking.'
    $ PlayerAddItem("gold", 10)
    MC @talk '[regina_ref_cap!t]! I can’t accept—'
    REGINA @talk 'I insist.'
    REGINA @talk 'Now if you don’t mind, I’ve a few errands to run.'
    MC @talk 'See you later, [regina_ref!t].'
    REGINA @talk 'Bye now! '

    $ QstComplete(QstReginaPackage)
    # this was swapped out to locset due to new locenter now triggering events
    $ LocSet("mc_house_kitchen")
    $ LocEnter()
