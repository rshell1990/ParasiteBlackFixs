label evscr_nijah_rescue_1:
    menu:
        MC 'Sounds like sure trouble... Should I?'
        "Investigate the sounds.":
            scene black with dissolve
            'I turned sharply as I made my way through a series of dark and fetid alleyways, chasing the sounds.'
            'Stumbling over dislodged cobblestones and piles of rubbish, I finally came across a woman, terrified and cowering.'
            'Her face was shrouded by rags as the men surrounded her brandishing their blades.'
            'The largest amongst them, a fat, repulsive bearded thug, towered over her.'
            THUG @talk "Stupid fucking whore."
            THUG @talk 'You still owe us gold, girl!'
            'The frightened, muffled voice pleaded back.'
            UNKNOWN @talk 'Please! Need time!'
            THUG @talk 'No more time, you pay NOW!'
            $ LocFlush()
            show mc at left
            show cg_bandit at cright_f
            with dissolve
            'From the shadows I emerged, and the men turned to face me.'
            THUG @talk 'Who are you?'
            THUG @talk 'Stay out of this, this does nor a concern you.'
            'Looking around, I could see dozens of eyes watching from every open crevice and window.'
            MC '(Damn... I better be careful here, it’s too risky to transform)'
            MC '(If I fight them, I’ll have to do it in my normal form)'
            $ choicemenu = ['a']
            call evscr_nijah_rescue_1_thugsmenu from _call_evscr_nijah_rescue_1_thugsmenu
            return
        'Ignore it.':
            # makes it a revisitable clickable icon
            $ QstSetProgress(EventNijahRescue, 1)
            $ LocEnterQ()

label evscr_nijah_rescue_1_thugsmenu:
    menu:
        "You'll be leaving now... or else." if 'a' in choicemenu:
            # 1.) Continued (Fail)
            THUG @talk 'Bah! There are three of us and only one of you!'
            THUG @talk 'You’ll have to do better than that!'
            $ choicemenu.remove("a")
            jump evscr_nijah_rescue_1_thugsmenu

        '{image=[ICON.SWORDS]} I am death incarnate, come to claim you wretches.':
            THUG @talk 'Kill him, you fools!'
            $ AutoMus(False)
            $ PlayMusic("audio/music/31_Encounter.ogg")
            $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys", CharIDList_Right = ["e_bandit", "e_thug", "e_bandit"], CanTransform = False))
            $ AutoMus(True)
            'As their lifeless bodies littered the alleyway, the blood flowed freely into the cracks of the cobblestone.'
            'I sighed with relief, wiping the sweat from my brow but quickly realised I couldn’t stay here long or else I risked drawing the ire of the guards.'
            return

        'Whats going on here?':
            THUG @talk 'This is not your business, stranger!'
            THUG @talk 'This woman owes us money and she will pay it!'
            MC @talk 'How much is her debt?'
            THUG @talk 'Two hundred coins now... the rest later.'
            menu:
                "I shall cover her debt." (Req_Gold = 200):
                    $ PlayerRemItem("gold", 200)
                    THUG @talk 'Hmm...'
                    THUG @talk 'You have bought yourself some time, {i}for now,{/i} girl...'
                    THUG @talk 'Pleasure doing business with you, stranger, heh...'
                    return

                "{image=[ICON.SWORDS]} Actually, I'd rather just kill you all than part with a single coin.":
                    THUG @talk 'Men! Draw your blades!'
                    $ AutoMus(False)
                    $ PlayMusic("audio/music/31_Encounter.ogg")
                    $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys", CharIDList_Right = ["e_bandit", "e_thug", "e_bandit"], CanTransform = False))
                    $ AutoMus(True)
                    return

                '{image=[ICON.DEATH]} Hm, I see this is not my concern, I will be taking my leave.':
                    THUG @talk 'A wise decision...'
                    #Screen fade to black
                    scene black with dissolve
                    if CharGetVar("nijah", "prologueMet"):
                        MC '(As I left the alley, I could hear the strangely familiar voice pleading behind me for mercy.)'
                    else:
                        MC '(As I left the alley, I could hear a female voice pleading behind me for mercy.)'
                    MC '(I wondered if I could, or should, have done something different there.)'
                    MC "(But, it's best to leave Ramonians to handle their own affairs.)"
                    $ EventNijahRescue().investigateFlag = False
                    $ QstFail(EventNijahRescue)
                    $ LocEnter()
