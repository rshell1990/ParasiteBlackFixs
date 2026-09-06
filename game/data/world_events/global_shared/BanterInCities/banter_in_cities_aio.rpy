default SeenBanterLabels_NovarasCity = set()
default SeenBanterLabels_HamunCity = set()

init python:
    # all "map event" banter labels
    BanterLabels_NovarasCity = {
        "travelmodebanter_city_novaras_mc_markus_1",
        "travelmodebanter_city_novaras_mc_markus_2",
        "travelmodebanter_city_novaras_mc_markus_3_nijah",
        "travelmodebanter_city_novaras_mc_markus_4_elena",
    }
    # all "camp event" banter labels
    BanterLabels_HamunCity = {
        "travelmodebanter_city_hamun_mc_ves_1",
        "travelmodebanter_city_hamun_mc_ves_2",
        "travelmodebanter_city_hamun_mc_ves_3_romance",
    }

    LocIDList_HamunCityStreets = [
        "hamun_dist_arena",
        "hamun_dist_merch_lord",
        "hamun_dist_docks",
        ]

    # all this does is fires appropriate events via onenter
    @AppendToAllQuests
    class EventPartyBanter_Cities(LogicModule):
        def __init__(self):
            super().__init__()

            # lowerr priority so it doesnt interrupt other events
            self.priority = -666

        def onEnter(self):  
            if LastBanterDay is not None:
                if GetGameDay() - 5 < LastBanterDay:
                    return
            if RngInt(1, 60) != 1:
                return

            City = ""
            if GetLocID() in LocIDList_NovarasCityStreets:
                City = "Novaras"
            elif GetLocID() in LocIDList_HamunCityStreets:
                City = "Hamun"
            else:
                return
        
            ### past that point, we're guaranteed to be in either hamun/novaras

            AllSeeableBanterLabels = []

            # novaras banter
            if City == "Novaras":
                for BanterLabel in store.BanterLabels_NovarasCity:
                    if BanterLabel not in SeenBanterLabels_NovarasCity:
                        if self.CheckConditions(BanterLabel):
                            AllSeeableBanterLabels.append(BanterLabel)
            # hamun banter
            elif City == "Hamun":
                for BanterLabel in store.BanterLabels_HamunCity:
                    if BanterLabel not in SeenBanterLabels_HamunCity:
                        if self.CheckConditions(BanterLabel):
                            AllSeeableBanterLabels.append(BanterLabel)

            if len(AllSeeableBanterLabels) == 0:
                return
            TargetBanterLabel = renpy.random.choice(AllSeeableBanterLabels)
            store.LastBanterDay = GetGameDay()
            if City == "Novaras":
                store.SeenBanterLabels_NovarasCity.add(TargetBanterLabel)
            elif City == "Hamun":
                store.SeenBanterLabels_HamunCity.add(TargetBanterLabel)
            return TriggeredEvent(TargetBanterLabel)
            
        def CheckConditions(self, BanterLabel):
            if BanterLabel == "travelmodebanter_city_novaras_mc_markus_1":
                if CharInParty("markus"):
                    return True
            elif BanterLabel == "travelmodebanter_city_novaras_mc_markus_2":
                if CharInParty("markus"):
                    return True
            elif BanterLabel == "travelmodebanter_city_novaras_mc_markus_3_nijah":
                if CharInParty("markus"):
                    if QstIsComplete(EventNijahRescue):
                        return True
            elif BanterLabel == "travelmodebanter_city_novaras_mc_markus_4_elena":
                if CharInParty("markus"):
                    if CharIsLover("elena"):
                        return True

            elif BanterLabel == "travelmodebanter_city_hamun_mc_ves_1":
                if CharInParty("ves"):
                    return True
            elif BanterLabel == "travelmodebanter_city_hamun_mc_ves_2":
                if CharInParty("ves"):
                    return True
            elif BanterLabel == "travelmodebanter_city_hamun_mc_ves_3_romance":
                if CharInParty("ves"):
                    if CharIsLover("ves"):
                        return True

            return False

init python:
    def Travel_RollPartyBanter_Map():
        
        LegitBanterLabels = TravelModeBanter_Map_GetAllSeeableBanterLabels()
        if len(LegitBanterLabels) == 0:
            return

        LocFlush(dissolve)
        Pause(0.75)
        BanterLabel = renpy.random.choice(LegitBanterLabels)
        SeenBanterLabels_Map.add(BanterLabel)

        store.LastBanterDay = GetGameDay()

        renpy.call(BanterLabel)
        return

#####################################################################################################################################################
### banter during city travel
# MARKUS and MC - Novaras 1 (in city) 
label travelmodebanter_city_novaras_mc_markus_1:
    show mc at cright with easeinleft
    show markus at cleft with easeinleft
    MARKUS @talk "I have a curious question for you, friend."
    show mc at blurin, cright_f
    MC @think "What is it?"
    MARKUS @talk "If we could go back, and you could choose between the power we have now... or the life of safety and comfort in the castle that we always dreamed of—what would you pick?"
    menu:
        "I'd choose the life we always wanted.":
            MARKUS @talk "A part of me would too..."
            MARKUS @talk "Still, it feels good knowing I don't have to sleep with a knife under my pillow every night."
        "I'd choose the power we have now.":
            MARKUS @think "Even though we're always neck-deep in danger?"
            menu:
                "Maybe... but we're more free than anyone else in Alderay.":
                    MARKUS @talk "Hmm... I see."
                    MARKUS @talk "Let's just hope our freedom doesn't come at the cost of choosing where to die."
                "We have the power to save the realm.":
                    MARKUS @talk "Heh, maybe. I'd be content just saving our own hides."
                "Aren't you enjoying all the women and coin?":
                    MARKUS @smile "What man wouldn't?"
                    MARKUS @talk "Still... I don't enjoy living like every day could be my last."
            MARKUS @talk "Anyway, that's all I had to ask. Let's keep moving."
    hide markus with easeoutright
    show mc at blurin, cright
    hide mc with easeoutright
    $ LocEnter()

# MARKUS and MC - Novaras 2 (in city)
label travelmodebanter_city_novaras_mc_markus_2:
    show mc at cright with easeinleft
    show markus at cleft with easeinleft
    MARKUS @smug "Sooo... you and Adara—"
    show mc at blurin, cright_f
    MC @talk "It's hard to say. Especially given our... 'gifts'."
    MARKUS @think "I don't get you."
    MARKUS @talk "You spent years with that treacherous witch, and the whole time, you and Adara were making eyes at each other."
    MC @surprised "W-We were not!"
    MARKUS @smile "You can hide many things from me. Your feelings for her aren't one of them."
    show mc at blurin, shake, cright
    MC @angry "Tsch!"
    MARKUS @smile "I'm simply saying, you would be a fool to let that girl go."
    MC @talk "Advice noted."
    hide mc with easeoutright
    show markus at center with easeinleft
    $ LocEnter()

# MARKUS and MC - Novaras 3 (in city) (If player rescued Nijah)
label travelmodebanter_city_novaras_mc_markus_3_nijah:
    show mc at cright with easeinleft
    show markus at cleft with easeinleft
    MARKUS @talk "So, you and the Ramonian girl."
    show mc at blurin, cright_f
    MC @angry "Don't start."
    MARKUS @shock "Hey, I'm not judging. She's quite beautiful."
    MC @think "Why do I sense a 'but' coming?"
    MARKUS @talk "But it's illegal for Alderian citizens to marry Ramonian refugees, you know."
    MC @think "Do I need a marriage certificate for every girl I bed now?"
    MARKUS @talk "No, but... if this war ends—"
    MC "When it ends."
    MARKUS @talk "—when it ends, she'll be expected to return to Ramon."
    show mc at blurin, cright
    MC "..."
    MARKUS @talk "Don't fall in love with her if you can help it, [player_name!t]... You're only going to get hurt."
    hide markus with easeoutright
    hide mc with easeoutright
    $ LocEnter()

# MARKUS and MC - Novaras 4 (in city) (If player romanced Elena)
label travelmodebanter_city_novaras_mc_markus_4_elena:
    show markus at cright with easeinleft
    show mc at cleft with easeinleft
    show markus at blurin, cright_f
    MARKUS @talk "Looks like our resident wolf girl's got her eye on you."
    MC @smile "What makes you say that?"
    MARKUS @smile "You mean besides the puppy eyes and tail wagging every time you look away?"
    MC @smile "I'll have to tease her about that."
    MC @think "Honestly, I thought you'd disapprove."
    MARKUS @smile "If she makes you happy, I'm happy."
    MARKUS @think "...Though I've just got one question."
    MC @think "What's that?"
    MARKUS @smug "Does she... *howl*?"
    MC @lewd "I'll let your imagination do the work."
    hide mc with easeoutright
    MARKUS @joy "Ha!"
    $ LocEnter()

# VES and MC - While in Hamun root - 1
label travelmodebanter_city_hamun_mc_ves_1:
    show ves at cright with easeinleft
    show mc at cleft with easeinleft
    show ves at blurin, cright_f
    VES @talk "..."
    MC @smile "You look like you want to say something."
    VES @talk "Are all human settlements this... big?"
    MC @smile "I suppose. Not what you're used to?"
    VES @talk "We travel light. Stay in one place too long, the Greater Trading Company finds us."
    MC @think "So no stone buildings?"
    VES @talk "Old stories say we once built such things... but those days are gone."
    MC @sad "Does seeing this upset you?"
    VES @talk "No. It inspires me."
    show ves at blurin, cright
    VES @talk "One day, when my people are free... we'll build our cities too."
    VES @smile "And maybe I'll show you around one of them."
    hide ves with easeoutright
    show mc at center with ease
    MC @smile "I'd like that."
    $ LocEnter()


# VES and MC - While in Hamun root - 2
label travelmodebanter_city_hamun_mc_ves_2:
    show ves at cright with easeinleft
    show mc at cleft with easeinleft
    show ves at blurin, cright_f
    VES @talk "{i}*Sniff*{/i}"
    MC @think "...Smell something?"
    VES @talk "Fresh bread. That scent... it's calling to me."
    MC @talk "It's just a bakery."
    "She whimpered quietly."
    MC @smile "Want to stop by?"
    show ves at shake
    VES @angry "No! Orcs live off the land—we hunt, not bake!"
    show ves at blurin, cright
    "A pause. More sniffing."
    show ves at blurin, cright_f
    VES @blush "...P-Perhaps we could {i}sample{/i} it."
    VES @blush "Something for my people to learn, maybe."
    MC @smile "Sounds like a plan."
    hide mc with easeoutright
    show ves at blurin, cright
    hide ves with easeoutright
    $ LocEnter()

# Ves and MC - While wandering around Hamun - 3 (romance)
label travelmodebanter_city_hamun_mc_ves_3_romance:
    show ves at cright with easeinleft
    show mc at cleft with easeinleft
    show ves at blurin, cright_f
    VES @blush "..."
    MC @smile "You know you can talk whenever you want, right?"
    MC @smile "You don't have to keep staring awkwardly."
    show ves at shake
    VES @angry "I AM NOT AWKWARD!"
    VES @blush "You... simply look nice today."
    MC @smile "Hm?"
    show ves at shake
    VES @angry "YOU LOOK GOOD TODAY!"
    show mc at shake
    MC @angry "THANKS!"
    VES @blush "...A-Anyway, enough distractions!"
    VES @blush "Let's keep moving!"
    show ves at blurin, cright
    hide ves with easeoutright
    show mc at center with ease
    MC @smile "As you command."
    hide mc with easeoutright
    $ LocEnter()