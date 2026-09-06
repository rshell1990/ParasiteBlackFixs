define LENIN = Character(_("Lenin"))
define SWEETIE = Character(_("Sweetie Fox"))
define SPECTER = Character(_("Biggie Smalls"))
define HAMUN_GUARD = Character(_("Hamun Guard"))

image lenin = "charph1"
image sweetie = "charph2"
image specter = "charph3"

label qst_TheDarkSpecterOfBiggieSmalls_intro:
    $ QstComplete(PrimerTheDarkSpecterOfBiggieSmalls)
    "While walking around Hamun, you are approached by a Hamun city guard:"
    show cg_guard at right_f with easeinright
    show mc at left with easeinleft
    HAMUN_GUARD @talk "You are summoned at once to speak to Garen Quiltshire."
    menu qst_TheDarkSpecterOfBiggieSmalls_intro_menu:
        "What now?":
            HAMUN_GUARD @talk "GO AT ONCE!"
            # loops back to menu
            jump qst_TheDarkSpecterOfBiggieSmalls_intro_menu

        "You're not my dad! You can't tell me what to do!":
            HAMUN_GUARD "HA! I have the lead developer on my side, fool!"
            jump qst_TheDarkSpecterOfBiggieSmalls_intro_menu

        "Tell the git I shall be there.":
            HAMUN_GUARD "ANOTHER WIN FOR CAPITALISM!"
            hide cg_guard with easeoutright
            hide mc with easeoutleft
            $ QstStart(QstTheDarkSpecterOfBiggieSmalls)
            $ QstSetProgress(QstTheDarkSpecterOfBiggieSmalls, 0)
            $ LocEnter()

label qst_TheDarkSpecterOfBiggieSmalls_garen2:
    show garen at right_f with easeinright
    show mc at left with easeinleft
    GAREN @talk "Have you reconsidered my offer?"
    menu qst_TheDarkSpecterOfBiggieSmalls_garen2_menu:
        "Give me one thousand coins or I report you myself." (Req_Barter = 8): # Available with Barter 8+.
            GAREN @angry "Damn you boy! I agree!"
            $ QstTheDarkSpecterOfBiggieSmalls().ChosenReward = 1000
            $ QstTheDarkSpecterOfBiggieSmalls().TakenQuest = 1
            jump qst_TheDarkSpecterOfBiggieSmalls_garenaftertakingquest

        "Nah, I can make more money just by growing tits, I have the perk you know!" if PlayerHasPerk("fem_charm"):
            GAREN @shock "You strike a hard bargain! Show me!"
            hide mc with dissolve
            show mcfem at left
            MC @smile "Like this?"
            GAREN @smile "Wonderful tits! You are right! I shall raise the bargain to one hundred coins!"
            hide mcfem with dissolve
            show mc at left
            $ QstTheDarkSpecterOfBiggieSmalls().ChosenReward = 100
            $ QstTheDarkSpecterOfBiggieSmalls().TakenQuest = 1
            jump qst_TheDarkSpecterOfBiggieSmalls_garenaftertakingquest

        "yes...":
            GAREN @talk "I see. Very well."
            $ QstTheDarkSpecterOfBiggieSmalls().ChosenReward = 1
            $ QstTheDarkSpecterOfBiggieSmalls().TakenQuest = 1
            jump qst_TheDarkSpecterOfBiggieSmalls_garenaftertakingquest

        "no":
            GAREN @angry "UNACCEPTABLE! THE DEVELOPER WILL NOT ALLOW IT!"
            GAREN @talk "Return when you have found sense!"
            $ QstTheDarkSpecterOfBiggieSmalls().TakenQuest = 2
            $ LocEnter()

label qst_TheDarkSpecterOfBiggieSmalls_garen1:
    show garen at right_f with easeinright
    show mc at left with easeinleft
    GAREN @smile "You have made it, good!"
    GAREN @think "I have been avoiding paying the IRS for years, and made the unfortunate decision of hiding some obscure records with an ancient deity mankind scarcely understood."
    GAREN @talk "The dark specter Biggie Smalls, a being who was sealed away after years of conflict with the wizard Tupac."
    GAREN @talk "Help me, and I shall reward you with a SINGLE coin!"
    menu qst_TheDarkSpecterOfBiggieSmalls_garen1_menu:
        "Yes.":
            # Accept quest. Reward = 1 gold.
            # Player accepted the quest
            $ QstTheDarkSpecterOfBiggieSmalls().ChosenReward = 1
            $ QstTheDarkSpecterOfBiggieSmalls().TakenQuest = 1
            jump qst_TheDarkSpecterOfBiggieSmalls_garenaftertakingquest

        "No.":
            GAREN @angry "UNACCEPTABLE! THE DEVELOPER WILL NOT ALLOW IT!"
            GAREN @talk "Return when you have found sense!"
            $ QstTheDarkSpecterOfBiggieSmalls().TakenQuest = 2  # Player declined the quest
            # IMPLEMENT: exit/re-enter dialogue without advancing.
            $ LocEnter()

label qst_TheDarkSpecterOfBiggieSmalls_garenreturn:
    show garen at right_f with easeinright
    show mc at left with easeinleft
    GAREN @angry "What are you doing here? Go and do what you gotta do!"
return
label qst_TheDarkSpecterOfBiggieSmalls_garenaftertakingquest:
    GAREN @talk "To summon Biggie, you must first battle Vladimir Lenin to win the sword and mantle of 'Russianest Russian ever.' You may find him hanging out at the library."
    GAREN @talk "You must also take this, and give Sweetie Fox this feline creature! It is the only way!"
    $ PlayerAddItem("qst_feline")
    GAREN @talk "You may find her at the brothel ONLY at night!"
    GAREN @talk "Go now! Hurry!"
    GAREN @talk "Complete your tasks and return."
    hide garen at right_f with easeoutright
    hide mc at left with easeoutleft
    $ QstTheDarkSpecterOfBiggieSmalls().TakenQuest = 1
    $ GoalComplete(QstTheDarkSpecterOfBiggieSmalls, 0)
    $ GoalShow(QstTheDarkSpecterOfBiggieSmalls, 1)
    $ GoalShow(QstTheDarkSpecterOfBiggieSmalls, 2)
    $ LocEnter()

label qst_TheDarkSpecterOfBiggieSmalls_lenin:
    $ QstTheDarkSpecterOfBiggieSmalls().LeninFound = True
    show mc at left with easeinleft
    show lenin at right_f
    LENIN "STALINNNNNNN!?! WHAT HAVE YOU DONE?!"
    LENIN "AND WHY AM I HERE?!"
    LENIN "Oh bother... Just die already!"
    hide mc with dissolve
    # Battle against Lenin's ghost + support thugs using real enemy templates.
    $ StartBattle(BattleData(BackgroundImage = "pbat_hamun_street", CharIDList_Right = ["lenin", "lenins_thug1", "lenins_thug2"]))
    if LastBattleOutcome != "victory":
        return
    show mc at left
    show lenin at right_f
    LENIN "Shit..."
    LENIN "I am defeated!"
    LENIN "I crown you now an honorary Russian! Take this blade to defeat Biggie!"
    $ QstTheDarkSpecterOfBiggieSmalls().LeninDefeated = True
    $ PlayerAddItem("trotskys_bane")
    $ QstSetProgress(QstTheDarkSpecterOfBiggieSmalls, 1)
    $ LocSet("hamun_library")
    $ LocEnter()
label qst_TheDarkSpecterOfBiggieSmalls_sweetie2:
    show mc at cleft
    show sweetie at right_f
    SWEETIE "May I help you champion?"
    menu Qst_TheDarkSpecterOfBiggieSmalls_Sweetie_menu2:
        "I do not have it.": # Only available if the player does NOT have the Feline.
            SWEETIE "Return when you do!"
            $ QstTheDarkSpecterOfBiggieSmalls().SweetieDelivered = False
            $ LocSet("hamun_brothel")
            $ LocEnter()
label qst_TheDarkSpecterOfBiggieSmalls_sweetie1:
    show mc at cleft
    show sweetie at right_f
    SWEETIE "May I help you champion?"
    menu Qst_TheDarkSpecterOfBiggieSmalls_Sweetie_menu1:
        "Here, take this.": # Only available if the player has the Feline quest item.
            if not PlayerHasItem("qst_feline"):
                SWEETIE "Return when you do!"
            $ PlayerRemItem("qst_feline")
            $ QstTheDarkSpecterOfBiggieSmalls().SweetieDelivered = True
            $ LocSet("hamun_brothel")
            $ LocEnter()
            # Remove the Feline from inventory here.
            SWEETIE "I thank you brave knight, wanna see my tits?"
            menu Qst_TheDarkSpecterOfBiggieSmalls_menu4:
                "Yes.":
                    SWEETIE "Here you go."
                    SWEETIE "Hope you enjoyed the view."
                    jump qst_TheDarkSpecterOfBiggieSmalls_sweetie3
                "No.":
                    SWEETIE "Well that's gay, but okay."
                    jump qst_TheDarkSpecterOfBiggieSmalls_sweetie3
label qst_TheDarkSpecterOfBiggieSmalls_sweetie3:
    SWEETIE "Here sir knight, take this armor and use it to defeat Biggie."
    # Add armor: "Gooner Armor".
    $ PlayerAddItem("gooner_armor")
    MC @smile "THANK YOU!"
    $ GoalComplete(QstTheDarkSpecterOfBiggieSmalls, 2)
    $ LocSet("hamun_brothel")
    $ LocEnter()
label qst_TheDarkSpecterOfBiggieSmalls_garen3:
    $ QstSetProgress(QstTheDarkSpecterOfBiggieSmalls, 3)
    show garen at right_f
    show mc at left
    GAREN @talk "You have returned! And I see you have completed my tasks! I can summon Biggie to battle whenever you are ready!"
    menu Qst_TheDarkSpecterOfBiggieSmalls_menu5:
        "Summon him.":
            GAREN @talk "Excellent!"
            hide garen with easeoutright
            jump qst_TheDarkSpecterOfBiggieSmalls_BiggieSummon
        "Do not.":
            GAREN @talk "Well... I guess I'll just stand here and wait then?"
            $ LocSet("hamun_hookah_bar")
            $ LocEnter()
label qst_TheDarkSpecterOfBiggieSmalls_BiggieSummon:
    "The tavern suddenly tore itself apart as the great specter appeared."
    SPECTER "YOU DARE SUMMON THE NOTORIOUS?"
    SPECTER "FIGHT ME!"
    $ StartBattle(BattleData(BackgroundImage = "pbat_hamun_street", CharIDList_Right = ["BiggieSmalls"]))
    if LastBattleOutcome == "victory":
        jump qst_TheDarkSpecterOfBiggieSmalls_biggie_victory
    else:
        jump qst_TheDarkSpecterOfBiggieSmalls_biggie_defeat
label qst_TheDarkSpecterOfBiggieSmalls_biggie_defeat:
    "You failed to defeat Biggie. Retry?"
    # show yes/no menu
    menu Qst_TheDarkSpecterOfBiggieSmalls_biggie_defeat_menu:
        "Yes!":
            jump qst_TheDarkSpecterOfBiggieSmalls_BiggieSummon
        "No!":
            hide mc with dissolve
            $ LocSet("hamun_hookah_bar")
            $ LocEnter()

label qst_TheDarkSpecterOfBiggieSmalls_biggie_victory:
    show specter at right_f
    show mc at left
    SPECTER "You have defeated me, I will now return your records so you can continue defrauding the governments."
    $ QstTheDarkSpecterOfBiggieSmalls().BiggieDefeated = True
    $ PlayerAddItem("qst_dodgy_tax_receipts")
    $ GoalShow(QstTheDarkSpecterOfBiggieSmalls, 4)
    SPECTER "Here, enjoy this free bitch as well."
    show nijah at cright_f
    MC "Nijah! What are you doing here?!"
    SPECTER "REMEMBER G, WITH GREAT POWER, COMES GREAT BITCHES."
    hide specter
    $ QstTheDarkSpecterOfBiggieSmalls().BiggieSummoned = True
    $ GoalComplete(QstTheDarkSpecterOfBiggieSmalls, 3)
    NIJAH "I have come to ride your cock like a mindless fuck doll!"
    menu Qst_TheDarkSpecterOfBiggieSmalls_menu6:
        # Implement using the existing Nijah remake cowgirl scene assets up on the drive.
        "Yessss!": 
            image qst_biggie_nijah_cowgirl_loop = Movie(
            start_image = "images/sexy_scenes/nijah/house_cowgirl/nopreg/start_image.webp",
            play = "images/sexy_scenes/nijah/house_cowgirl/nopreg/loop.webm")
            image qst_biggie_nijah_cowgirl_finish = "images/sexy_scenes/nijah/house_cowgirl/nopreg/finish.webp"
            scene qst_biggie_nijah_cowgirl_loop with dissolve
            $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg",1)
            $ Pause()
            NIJAH "YES! SO GOOD!"
            NIJAH "YOU TRULY ARE THE PLAYER!"
            NIJAH "HUZZAH!"
            scene qst_biggie_nijah_cowgirl_loop with dissolve
            $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg",1)
            $ Pause()
            NIJAH "DID I LEAVE THE OVEN ON?"
            NIJAH "DON'T FORGET TO WATCH THE BIG LEBOWSKI WHEN YOU CAN MY LOVE!"
            scene qst_biggie_nijah_cowgirl_finish with dissolve
            NIJAH "AH! WE ARE MAKING A BABY! EXCELLENT!"
            NIJAH "THE DECLINING BIRTH RATE COMMITTEE WILL BE PLEASED!"
            $ ReduceInfectionFromSex("nijah", 0.1)
            $ LocSet("hamun_hookah_bar")
            $ LocEnter()
        "Not this time!":
            NIJAH "Speak to Garen if you want to fuck sometime!"
            hide nijah with easeoutright
            hide mc with easeoutleft
            $ LocSet("hamun_hookah_bar")
            $ LocEnter()
label qst_TheDarkSpecterOfBiggieSmalls_garen4:
    show garen at right_f
    show mc at left
    GAREN @talk "You have done as I ask!"
    if not PlayerHasItem("qst_dodgy_tax_receipts"):
        GAREN @talk "Bring me the dodgy tax receipts first, then we can settle this."
        $ LocSet("hamun_hookah_bar")
        $ LocEnter()
    $ PlayerRemItem("qst_dodgy_tax_receipts")
    GAREN @talk "Now the government will never know I defrauded them to fund my crippling Warhammer addiction!"
    GAREN @talk "Here is your reward!"
    if QstTheDarkSpecterOfBiggieSmalls().ChosenReward == 1:
        $ PlayerAddItem("gold", 1)
    elif QstTheDarkSpecterOfBiggieSmalls().ChosenReward == 100:
        $ PlayerAddItem("gold", 100)
    elif QstTheDarkSpecterOfBiggieSmalls().ChosenReward == 1000:
        $ PlayerAddItem("gold", 1000)
    $ GoalComplete(QstTheDarkSpecterOfBiggieSmalls, 4)
    $ QstTheDarkSpecterOfBiggieSmalls().rewardClaimed = True
    $ QstTheDarkSpecterOfBiggieSmalls().GarenRewardClaimed = True
    $ QstComplete(QstTheDarkSpecterOfBiggieSmalls)
    $ LocSet("hamun_hookah_bar")
    $ LocEnter()
label qst_TheDarkSpecterOfBiggieSmalls_garen_postquest:
    show mc at left with easeinleft
    show garen at right_f with easeinright
    GAREN @talk "Yes?"
    menu qst_TheDarkSpecterOfBiggieSmalls_garen_postquest_menu:
        "Summon the wench.":
            GAREN @talk "Of course!"
            hide garen with easeoutright
            show nijah at right_f with easeinright
            label sandwich_choice:
                if renpy.random.choice([True, False]):
                    # SUCCESS:
                    NIJAH "Wanna fuck?"
                    menu qst_TheDarkSpecterOfBiggieSmalls_garen_postquest_sex_menu:
                        "Yes!":
                            image qst_biggie_nijah_cowgirl_loop = Movie(
                            start_image = "images/sexy_scenes/nijah/house_cowgirl/nopreg/start_image.webp",
                            play = "images/sexy_scenes/nijah/house_cowgirl/nopreg/loop.webm")
                            image qst_biggie_nijah_cowgirl_finish = "images/sexy_scenes/nijah/house_cowgirl/nopreg/finish.webp"
                            scene qst_biggie_nijah_cowgirl_loop with dissolve
                            scene qst_biggie_nijah_cowgirl_loop with dissolve
                            $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg",1)
                            $ Pause()
                            NIJAH "YES! SO GOOD!"
                            NIJAH "YOU TRULY ARE THE PLAYER!"
                            NIJAH "HUZZAH!"
                            scene qst_biggie_nijah_cowgirl_loop with dissolve
                            $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg",1)
                            $ Pause()
                            NIJAH "DID I LEAVE THE OVEN ON?"
                            NIJAH "DON'T FORGET TO WATCH THE BIG LEBOWSKI WHEN YOU CAN MY LOVE!"
                            scene qst_biggie_nijah_cowgirl_finish with dissolve
                            NIJAH "AH! WE ARE MAKING A BABY! EXCELLENT!"
                            NIJAH "THE DECLINING BIRTH RATE COMMITTEE WILL BE PLEASED!"
                            NIJAH "HUZZAH!"
                            NIJAH "Yay!"
                            $ ReduceInfectionFromSex("nijah", 0.1)
                            $ LocSet("hamun_hookah_bar")
                            $ LocEnter()
                        "No!":
                            NIJAH "Then I am leaving!"
                            hide nijah with easeoutright
                            $ LocSet("hamun_hookah_bar")
                            $ LocEnter()
                else:
                    GAREN @talk "You've had enough ass for one night!"
                    hide garen with easeoutright
                    hide mc with easeoutleft
                    $ LocSet("hamun_hookah_bar")
                    $ LocEnter()
                    # Return to root menu
        "That is all!":
            GAREN @smile "Farewell then!"
            hide garen with easeoutright
            hide mc with easeoutleft
            $ LocSet("hamun_hookah_bar")
            $ LocEnter()