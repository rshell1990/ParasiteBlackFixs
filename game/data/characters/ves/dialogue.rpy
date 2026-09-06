init python:
    CharIDPartyDialogueLabelMap["ves"] = "ves_party_talk"

    @AppendToAllQuests
    class DialogueVes(LogicModule):
        def __init__(self):
            super().__init__()

            self.outHunting = False # she hunts every other day


        def locationMod(self):
            btnMods = {}
            if self.progress > 0:
                if GetLocID() == "ves_tent_int":
                    if IsDaytime():
                        if not self.outHunting:
                            btnMods["talkVes"] = BtnJumpLabel(_("Talk to Ves"), "ves_dial_talk")
            return LocButtonMod(directMods = btnMods)

        def onMidnight(self):
            if self.outHunting:
                self.outHunting = False
            else:
                if RngInt(1,3): # 33% chance to go hunt
                    self.outHunting = True

        def extraDialogue(self):
            yield ("ves_root", DNode(_("Been out hunting?"), "ves_dial_beenout"))
            yield ("ves_root", DNode(_("Seen anything of interest out here?"), "ves_dial_seenanything"))
            yield ("ves_root", DNode(_("I should go."), "ves_dial_bye", nextNode = "DNodeExit", order = -100))

            yield ("ves_party_root", DNode(_("Let's move on."), "ves_party_bye", nextNode = "DNodeExit", order = -100))

        def onEnter(self):  
            if GetLocID() == "ves_tent_int":
                if self.progress == 0:
                    return TriggeredEvent("ves_firstmeet")
                else:
                    if self.outHunting:
                        return TriggeredEvent("ves_isOutHunting")

label ves_party_talk:
    show ves at center with dissolve
    VES "Yes, [player_name!t]?"
    call processDialogue("ves_party_root") from _call_processDialogue_69
    $ LocEnter()

label ves_party_bye:
    VES "Sure, human."
    $ LocEnter()

#################################
label ves_isOutHunting:
    MC "(Ves must be out hunting.)"
    MC "(I might be able to catch her tomorrow.)"
    $ LocSet("ves_camp")
    $ LocEnterQ()

label ves_firstmeet:
    $ QstSetProgress(DialogueVes, 1)
    $ AutoMus(False)
    $ PlayMusic("audio/music/29_Orcs_Eyes.ogg")
    show ves:
        xcenter 0.3
    with dissolve
    'Opening the flap of her tent, I stepped inside to find Ves sitting cross legged on the floor, inspecting her axes before sharpening them with a vicious-looking rock.'
    'Looking around the tent which flapped with each gust of wind, I observed that she had done a remarkable job to have survived as long as she had out here in these harsh lands.'
    'Sprawled across the floor were a mixture of fur rugs made from the hides of animals from her many hunts and cloth she had found and hung decoratively.'
    'Here and there were various pieces of equipment and intricate looking items she had fashioned out here in this small corner of the desert.'
    'There was a small wooden tub, presumably for washing in but I couldn’t even begin to guess where she managed to find enough water to get close to filling it in these barren lands.'
    'Her bed was comprised of a cluster of blue quilts and pillows that seemed almost out of place in the desert, had she stolen them?'
    'The bedframe itself was notably made with some craftsmanship, further raising my suspicions on the matter, but I decided not to pry too much into her affairs.'
    'Here and there were jars filled with either water or small dead animals in some preservative substance, scorpions, beetles and such...'
    'Presumably kept as small rations of food for when the dried-out meat on the lines outside was running low.'
    'As she tested the sharpness of her axe with her thumb, she looked up coolly at me.'
    VES @talk 'What do you want, human?'
    call processDialogue("ves_root") from _call_processDialogue_33
    $ AutoMus(True)
    $ LocEnter()

label ves_dial_talk:
    show ves with dissolve:
        xcenter 0.3
    VES @talk "What is it, human?"
    call processDialogue("ves_root") from _call_processDialogue_34
    $ LocEnter()

label ves_dial_beenout:
    VES @talk 'Not yet, but I will be soon.'
    VES @talk 'Can’t risk supplies getting too low.'
    return

label ves_dial_seenanything:
    VES @talk 'Just your usual small parties of Demorai moving through the sands.'
    VES @talk 'Oh, and some Skorn... Not much else.'
    VES @talk 'Though I did find a strange temple out here once...'
    'I raised an eyebrow'
    MC @talk 'A temple?'
    VES @talk 'Just some ruinous thing... Southeast of here.'
    MC @talk 'Hm, I see...'
    return

label ves_dial_bye:
    VES @talk 'Very well.'
    VES @talk 'As you are, human.'
    return
