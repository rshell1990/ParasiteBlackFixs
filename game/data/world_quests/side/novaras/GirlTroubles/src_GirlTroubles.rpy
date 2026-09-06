label qst_girl_troubles_about_rhuvan:
    DIVINE @talk "Yes? Do you have its hide?"
    menu:
        "Here." if PlayerItemQty('white_bear_hide') > 0: #If the player has Rhuvan bear hide in inventory
            $ QstLittleLies().divineGotRhuvanHide = True
            $ QstLittleLies().divineWantsRhuvansHide = False
            $ PlayerRemItem("white_bear_hide", 1)
            DIVINE @happy "Perfect!"
            DIVINE @happy "This should smooth any issues over with the council..."
            DIVINE @happy "Tell Mika the patch is hers, for now, at least."
            $ QstLittleLies().mikaGotFarmingPatch = True
            if QstGetProgress(QstLittleLies) == 3:
                $ QstSetProgress(QstLittleLies, 4)
            $ NoteLock("LittleLiesNote")
            $ LocEnter()
        "Not yet.":
            DIVINE @talk "Let me know if you have it."
            $ LocEnter()

label qst_girl_troubles_main_label:
    "Sister Divine raised an eyebrow."
    DIVINE @talk "Which one?"
    #Options appear here for quest related stuff to the girls 
    menu qst_girl_troubles_main_label_menu: 
        "Mika is refusing to let me train her to fight unless she gets her gardening patch on the rooftops." if (QstGetProgress(QstLittleLies) == 3 and QstLittleLies().askToGiveMikaTheFarmingPatch): #IF PLAYER AGREED TO HELP MIKA GET HER GARDENING PATCH
            DIVINE @angry "Urghh, that girl..."
            DIVINE @angry "I've told her {i}no{/i} dozens of times, but she continues to persist on the matter!"
            DIVINE @angry "The garden isn't just for her, it's for {i}everyone.{/i}"
            DIVINE @angry "Not to mention that if she leaves the tower, who exactly is supposed to tend to this farming patch in her absence?"
            MC @talk "Surely you can spare some small section of the garden for her?"
            DIVINE @talk "{i}*Sigh*{/i}"
            DIVINE @talk "Any such decisions would have to be reviewed and approved by other council members."
            DIVINE @talk "Things are...very stringent around here."
            menu qst_girl_troubles_main_label_menu_2:
                "Are all the mages as tightly controlled as the Mages of Palam?":
                    DIVINE @talk "All of the mages have strict rules and regulations on most matters, even who you marry."
                    MC @talk "Who you marry?"
                    DIVINE @talk "A mage can prove to be a powerful political asset for anyone; any binding unions need to seek the approval of the high council before they can get married."
                    MC @talk "I suppose that makes sense, though I imagine it leaves many a mage in an awkward position should they fall in love with the wrong person."
                    "Sister Divine sighed softly."
                    DIVINE @sad "{i}It does indeed...{/i}"
                    jump qst_girl_troubles_main_label_menu_2
                "Then how did you let things slip past with the girls?":
                    DIVINE @talk "With great risk, [player_name!t]... Great risk to my own station." #loops back to this menu
                    jump qst_girl_troubles_main_label_menu_2
                "Surely there must be a way?": #continues.
                    DIVINE @talk "{i}*Sigh*{/i}"
                    DIVINE @talk "I suppose I could {i}attempt{/i} to pull some strings once more, even if it was just to keep the patch for her temporarily."
                    DIVINE @talk "But ... What can you offer me in return?"
                    menu qst_girl_troubles_main_label_menu_3:
                        "Oh, we both know what I offer you in return...{i}*run your hand down her back.*{/i}" if QstIsActive(RomanceDivine):
                            "Sister Divine's breathing became heavy as she shivered to my touch."
                            DIVINE @shock "I..."
                            DIVINE @embar "Alright, fine!"
                            DIVINE @lewd "You better make good on that offer."
                            MC @lewd "Oh, don't worry, I plan on making it {i}unforgettable{/i} for you."
                            "Sister Divine let out another excited, trembling hot breath as she tried to keep herself composed."
                            DIVINE @lewd "I look forward to it ... Now tell Mika she has her farming patch, for now, at least."
                            $ QstLittleLies().mikaGotFarmingPatch = True
                            $ QstSetProgress(QstLittleLies, 4)
                            $ LocEnter()
                        "Would coin suffice?":
                            DIVINE @talk "Hmm ... I suppose coin would certainly soften the blow of any criticisms at the next council meeting."
                            DIVINE @talk "Say, [QstLittleLies().divinePersuasionCost] should suffice..."
                            menu qst_girl_troubles_main_label_menu_4:
                                "Here you go." (Req_Gold = QstLittleLies().divinePersuasionCost): #Pay 2500 coins - if the player has money in inventory
                                    $ PlayerRemItem("gold", QstLittleLies().divinePersuasionCost)
                                    DIVINE @happy "Very good. Tell Mika the patch she wants is hers, at least for now."
                                    $ QstLittleLies().divinePersuasionPaid = True
                                    $ QstSetProgress(QstLittleLies, 4)
                                    $ LocEnter()
                                "Make it two thousand at least; that amount of coin is nothing to be laughed at for most." (Req_Barter = 7) if (QstLittleLies().divinePersuasionCost != 2000): #Barter (high)
                                    $ QstLittleLies().divinePersuasionCost = 2000
                                    DIVINE @talk "Urgh, very well, I suppose I can make do with two thousand ... But not a coin less!" #Success variant, now only 2000 coins charged 
                                    jump qst_girl_troubles_main_label_menu_4
                                "I don't have that kind of coin on me right.":
                                    DIVINE @talk "I can't go to the council without some kind of offering to ease any questions."
                                    DIVINE @talk "Return when you have the coin..."
                                    $ LocEnter()
                        "What would you suggest?" if (not QstLittleLies().divineWantsRhuvansHide and GetPlayerLevel() >= 6):
                            DIVINE @talk "Well ... There is {i}one{/i} thing that I believe could persuade me."
                            MC @talk "Speak it?"
                            DIVINE @talk "A great white bear, exceptionally rare and particularly aggressive, known as a {i}rhuvan.{/i}"
                            DIVINE @talk "Their hide is exceptionally prized and could be used as a gift to carry favor with many a lord and such."
                            DIVINE @talk "Should you be able to slay one of them and bring me its hide, I could give Mika her gardening patch in return."
                            MC @think "Hm, I shall think on it."
                            $ QstLittleLies().divineWantsRhuvansHide = True
                            $ NoteUnlock("LittleLiesNote")
                            $ LocEnter()
        "I've made some progress with Mika" if QstGirlTroubles().mika_training_done and IsGoalVisible(QstGirlTroubles, 3):
            DIVINE @happy "Yes, I've {i}seen.{/i}"
            DIVINE @happy "She's come so much out of her shell since you've started helping her."
            MC @talk "She's ready to face whatever's out there."
            DIVINE @talk "Well... No one's truly ever {i}ready.{/i}"
            DIVINE @talk "But I think now her fate is in the hands of the gods to keep her safe."
            DIVINE @happy "Well done, [player_name!t], here's your reward..." #MIKA QUEST COMPLETE + 700 coins awarded 
            $ PlayerAddItem("gold", 700)
            $ GoalComplete(QstGirlTroubles, 3)
            $ QstComplete(QstGirlTroubles)
            $ LocEnter()

        "Mika has said she's willing to let me train her to fight, should you give her one of your more...{i}intimate{/i} lessons." if (QstGetProgress(QstLittleLies) == 3 and QstLittleLies().askToGoOutWithMika):
            DIVINE @talk "{i}Intimate?{/i}"
            "Suddenly realizing what Mika was asking for, Sister Divine panicked as she offered sheepish protest."
            DIVINE @shock "I- I never cross boundaries with any of the girls! I-I'm their-"
            MC @talk "Sister Divine, Mika told me everything."
            DIVINE @sad "... I see."
            DIVINE @sad "I - I understand this probably isn't something you approve of, but..."
            DIVINE @sad "Kindly keep this knowledge to yourself."
            DIVINE @sad "The girls ... Us Mages of Palam, it's a terribly lonely life."
            DIVINE @sad "The expectations to be these saint-like figures is crushing, especially for those who don't want it."
            DIVINE @sad "A life without love is terrible, and love to a Mage of Palam is a delicate, often impossible thing to keep."
            DIVINE @sad "But grown women still have needs ... So we find what we can of it amongst ourselves."
            MC @talk "You don't need to explain yourself to me, sister."
            MC @talk "I only mentioned it because Mika has asked me to persuade you to give her the same affection as you give the others."
            DIVINE @sad "I-"
            DIVINE @talk "I didn't quite realize she felt that way, I never intended to make her feel unwanted."
            DIVINE @embar "... Very well, tell Mika to meet me in the tower bathhouse tonight."
            DIVINE @embar "I shall make it up to her in full."
            $ QstLittleLies().mikaWillHaveHerDate = True
            $ QstSetProgress(QstLittleLies, 4)
            $ LocEnter()
        "Never mind for now...": #loops back
            DIVINE @talk "Very well then."
            jump divine_talk