init python:
    notesLib["reginaButtplugFarmDis"] = Note(
        _("[regina_ref_cap!t] behaves strangely"),
        _("I bumped into [regina_ref_cap!t] as she was heading to the Farming District. She was unusually nervous."))

    @AppendToAllQuests
    class EventReginaButtplug(LogicModule):
        def onEnter(self):  
            if GetLocID() in [LocID for LocID in LocIDList_NovarasCityStreets if LocID not in ("novaras_dist_farm", "novaras_dist_house")]:
                if IsDaytime():
                    if self.progress == 0:
                        if QstDelayCheck(self):
                            if RngInt(1, 2) == 2:
                                return TriggeredEvent("regina_shopping_buttplug")

            elif GetLocID() == "novaras_blacksmith":
                if IsDaytime():
                    if self.progress == 1:
                        return TriggeredEvent("regina_buttplug_buy")
            
            elif GetLocID() == "mc_house_kitchen":
                if IsDaytime():
                    if self.progress == 2:
                        if QstDelayCheck(self):
                            # First time, 100% prob to happen
                            # Next occurrence: 25% prob
                            if self.nextEventOnDay == 0 or RngInt(1, 4) == 1:
                                return TriggeredEvent("regina_buttplug_cooking")
                else:
                    # Can only be checked once a day
                    self.nextEventOnDay = GetGameDay() + 1

label regina_shopping_buttplug:
    show mc at cleft
    with dissolve
    "While traversing my way through the city, to my surprise, I bumped into [regina_ref!t], looking unusually nervous."
    show regina at cright_f
    with easeinright
    show regina shock
    REGINA @shock_talk "Oh! [player_name!t]!"
    MC @talk "[regina_ref_cap!t]?"
    MC @talk "Are you going somewhere?"
    show regina lewd
    REGINA @lewd_talk "Oh, well ... I was just umm, doing some shopping is all."
    MC @talk "Shopping?"
    REGINA @smile_talk "Y-Yes, shopping."
    REGINA @talk "I'm just heading to pick up some new jewellery I ordered."
    REGINA @lewd_talk "It's become quite the gossip amongst women in the city."
    MC @talk "Oh? Would you like me to come with you to pick it up?"
    show regina shock
    REGINA @shock_talk "Ah! N-No need dear! I'll just see you later, have to run now!"
    "[regina_ref_cap!t] quickly hurried past me."
    REGINA @shock_talk "Byee!"
    hide regina with easeoutright
    MC "(Well that was strange ...)"
    BLACK "(From her scent, I believe she is heading towards the Farming District.)"
    MC "(The Farming District? For jewellery?)"
    MC "(Something feels off.)"

    $ QstSetProgress(EventReginaButtplug, 1)
    $ QstSetDelayVal(EventReginaButtplug, 0)
    $ NoteUnlock("reginaButtplugFarmDis")

    $ LocEnter()


#Scene 3 - scene auto plays once player enters the BLACKSMITHS after seeing Regina in the street
label regina_buttplug_buy:
    show regina at right_f
    show arlena smile at cright_f
    REGINA @talk "Is it ready?"
    ARLENA "Here's your new {i}package,{/i} I hope you enjoy."
    show mc at cleft with easeinleft
    REGINA @smile_talk "That's great, I-"
    #Regina sees MC
    show regina shock
    REGINA @shock_talk "[player_name!t]!"
    REGINA @shock_talk "W-What are you doing here?"
    MC @surprised "Why are {i}you{/i} here?"
    show regina lewd
    "Flustered, [regina_ref_cap!t] twirled her long back hair in her fingers, her fair blushed red."
    REGINA @lewd_talk "Just getting that jewellery I mentioned earlier."
    MC @talk "...{i}At the blacksmiths?{/i}"
    show regina smile
    REGINA @smile_talk "I-I should get going now! See you at home!"
    "With that, [regina_ref_cap!t] quickly scarpered off out of the blacksmiths." #Regina exit
    hide regina with easeoutright
    ARLENA "..."
    MC @talk "... Did she just buy-"
    ARLENA "My lips are sealed."
    'A smirking Arlena twirled around, humming to herself as she hurried off back upstairs.'
    hide arlena with easeoutright
    MC @surprised "Wait a minute! Arlena! ARLENA!"
    MC '(...)'

    $ QstSetProgress(EventReginaButtplug, 2)
    $ NoteLock("reginaButtplugFarmDis")

    $ LocEnter()


#Scene 4 - MC home living room - player can find Regina cooking - This scene is repeatable - but a low to moderate chance of reoccuring
label regina_buttplug_cooking:
    show cg_regina_cooking_back at cleft
    with dissolve
    MC "(Looks like [regina_ref_cap!t] is busy cooking)."
    MC "({i}It doesn't seem like she's noticed me come in{/i})."
    MC "(Maybe I can ... ?)"
    menu:
        "Forget it.":
            "Deciding it was a bad idea, I pushed the thought from my mind."
            scene black with dissolve
            $ LocFlush()

        "Try and lift [regina_ref_cap!t]'s dress?":
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            scene regina_buttplug_1 with dissolve
            "While [regina_ref_cap!t] was distracted, I gently began to hike up her skirt more and more, revealing the black lace panties hugging against her butt beneath."
            "Wedged beneath, I could make out the outline of something beneath the panties themselves."
            "[regina_ref_cap!t] continued to hum away, and I contemplated just how much further I should push my luck ..."
            menu:
                "Stop now.":
                    MC "(I best not push my luck any further)."

                    $ AutoMus(True)
                    scene black with dissolve
                    $ LocFlush()

                "Gently tug down her panties.":
                    scene regina_buttplug_2 with dissolve
                    "Gently, I tugged and pulled down [regina_ref_cap!t]'s panties very slowly."
                    "Now fully visible, pressed between her ass was one of the jeweled toys."
                    "A bronze plug with a green emerald like gem in the center."
                    REGINA "... Are you enjoying the view back there?"
                    MC "[regina_ref_cap!t]! I-"
                    MC "How long have you known I've been stood here?!"
                    REGINA "Long enough."
                    REGINA "It's fine ... If you like what you see so much, why don't you touch it?"
                    MC "I ..."

                    menu:
                        'Step back.':
                            "Flustered, I quickly pulled back."
                            #Scene goes back to character models talking

                            $ AutoMus(True)
                            scene black with dissolve
                            $ LocFlush()

                            show regina lewd at cright_f
                            show mc surprised at cleft
                            with dissolve
                            REGINA @smile_talk "There's no point being shy now."
                            REGINA @lewd_talk "You've caught me red-handed."
                            MC @surprised "Y-Yes, but-"
                            MC @surprised "I don't know what came over me!"
                            "[regina_ref_cap!t] simply laughed."
                            show regina smile
                            REGINA @smile_talk "It's fine, you shouldn't be ashamed of such desires."

                        'Grab her ass.':
                            scene regina_buttplug_3 with dissolve
                            "Reaching out, I nervously pawed and squeezed at [regina_ref_cap!t]'s ass."
                            REGINA "Mhhff..."
                            REGINA "See? There's nothing to worry about ..."
                            MC "Should we really be-"
                            REGINA "Mmhh, You have such strong hands now dear!"
                            "I pulled back, heart racing." #scene goes back to character models talking 

                            $ AutoMus(True)
                            scene black with dissolve
                            $ LocFlush()

                            show mc surprised at cleft
                            show regina smile at cright_f
                            with dissolve
                            REGINA @smile_talk "There's no need to be embarrassed!"
                            REGINA @smile_talk "You shouldn't feel ashamed of such desires."

                            $ UnlockGalSceneAndGrantXp("regina","buttplug")

                    "There was something strange with her expression, a part of me wondered why she was so ... easy about all this."
                    "But I remembered she had always been unusual when it came to affection with me."
                    "Ever since I was young, she had been overly-affectionate, and remarkably candid when it came to the topic of sex."
                    MC @surprised "I ... think I should go."
                    REGINA @smile_talk "Be safe, dear!"

                    hide mc
                    hide regina
                    with dissolve

    $ QstSetDelay(EventReginaButtplug, 2)
    $ LocEnterQ()
