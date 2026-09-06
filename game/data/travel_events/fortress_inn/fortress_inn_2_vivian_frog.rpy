#Fortress Inn variant 2 - 'The Dancing Frog'
label fortress_inn_vivian_firsttime:
    $ EventFortressInn().SeenFirstTimes[EventFortressInn().VariantID] = True
    show mc at left with easeinleft
    "Upon entering, a cheerful dark-haired woman made her way towards me with a frothing ale in hand."
    show vivian at center with dissolve
    VIVIAN @smile "Welcome... Welcome to {i}The Dancing Frog.{/i}"
    VIVIAN @talk "Call me Vivian. If you need anything, please ask."
    VIVIAN @talk "Moharius! We have new guests!"
    "The tavern owner nodded, wiping one of his cups clean. He said nothing, simply nodding."
    jump fortress_inn_vivian_talk_menu

label fortress_inn_vivian_talk:
    show vivian at center with dissolve
    VIVIAN @smile "How can I help?"
    menu fortress_inn_vivian_talk_menu:
        "I'd like to order something.":
            VIVIAN @smile "Drink or food, sir?"
            menu:
                "I'd like a drink, please." (Req_Gold = 20):
                    $ PlayerRemItem("gold", 20)
                    VIVIAN @smile "Ale, I presume?"
                    VIVIAN @smile "Or would you prefer some of our wine?"
                    MC @smile "Ale will do nicely."
                    VIVIAN @talk "Of course, sir."
                    "Vivian made her way to the bar before returning with a jug of ale topped with a thick white froth, which she carefully placed before me."
                    VIVIAN @smile "Please, enjoy."
                    $ EventFortressInn().GetDrink()
                    "I sipped the drink... It was a remarkably good ale."
                "I'd like some food, please." (Req_Gold = 40):
                    $ PlayerRemItem("gold", 40)
                    VIVIAN @smile "Of course, sir. We have roasted rabbit with vegetables as today's special."
                    MC @smile "I'll take that."
                    scene black with dissolve
                    $ TimeAdvBy(TIME_1H)
                    "Vivian left and returned a short while later with a steaming plate of well-cooked food."
                    $ EventFortressInn().GetFood()
                    $ LocFlush()
                    show vivian at center
                    with dissolve
                    VIVIAN @smile "Please, enjoy."
                    "She turned her attention to another table."
                "I've changed my mind.":
                    VIVIAN @talk "I'll come back shortly and give you some more time to decide."
            jump fortress_inn_vivian_talk_menu

        "How do places like this even survive?":
            VIVIAN @smile "What do you mean?"
            VIVIAN @smile "Merchants pass through. They want somewhere safe to rest, a comfortable bed, and food already prepared."
            VIVIAN @talk "With the number of bandits and Demorai stalking the roads these days, setting up camp is a risky venture."
            MC @think "But what stops those same bandits and Demorai from looting these places and burning them down?"
            VIVIAN @think "You ask a lot of questions, sir."
            MC @talk "I'm curious how 'safe' this place really is before I lay my head here."
            "Vivian laughed softly."
            VIVIAN @smile "I can assure you, sir, these inns aren't just safe because we have guards stationed nearby, {i}which we do.{/i}"
            VIVIAN @talk "They're also partially funded by the GTC."
            MC @think "What?"
            VIVIAN @talk "It's fairly straightforward. The GTC offers generous loans to inns like ours and rotates guards between them to help keep each one secure."
            VIVIAN @talk "{i}Sometimes{/i}, they don't even offer loans... They simply hand over ownership of an inn."
            MC @think "Generosity and the GTC aren't two things I'd ever expect to hear in the same sentence."
            VIVIAN @talk "They don't do it out of generosity. They do it because it's pragmatic, sir."
            VIVIAN @talk "If the roads aren't safe enough... If merchants no longer wish to travel them... Then the GTC loses far more coin than it spends investing in us."
            VIVIAN @smile "That's all there is to it."
            jump fortress_inn_vivian_talk_menu

        "How is the littlun?" (AppearIf = CharGetBirths("vivian") > 0):
            VIVIAN @angry "{i}*Ahem!*{/i}"
            "She gently kicked me beneath the table."
            MC @angry "Ow."
            VIVIAN @smile "The little one is fine."
            VIVIAN @angry "Her {i}father{/i} continues to be absent from her life."
            MC @surprised "I-"
            VIVIAN @sad "{i}*Sigh*{/i}"
            VIVIAN @talk "It's fine, please... I understand."
            "She paused."
            VIVIAN @talk "{i}What we have.{/i}"
            VIVIAN @talk "But if you're not going to be a steady figure in her life, I'd prefer you kept your distance until she's old enough."
            "Her words stung slightly, but given my travels and the path I was on, perhaps she was right."
            jump fortress_inn_vivian_talk_menu

        "Do you provide any... {i}'special services?'{/i}" (AppearIf = (EventFortressInn().ScheduledFuntime == False)):
            "Vivian didn't answer immediately. Instead, she studied me to make sure we meant the same thing."
            "Satisfied we did, she smiled coyly."
            VIVIAN @smile "... Yes, sir."
            VIVIAN @smile "I can provide you with some drinks and... {i}companionship{/i} this evening."
            VIVIAN @lewd "... For an additional fee."
            VIVIAN @talk "You'll have to get a room here, of course."
            VIVIAN @lewd "Are you... {i}interested in some evening entertainment, sir?{/i}"
            menu:
                "Yes.":
                    $ EventFortressInn().ScheduledFuntime = True
                    VIVIAN @smile "I shall stop by your room tonight with a bottle of wine then, sir."
                "No.":
                    VIVIAN @talk "Very well..."
            jump fortress_inn_vivian_talk_menu
        "I best get going...":
            VIVIAN @smile "Stay safe on the roads, sir."
            $ LocEnter()

label fortress_inn_moharius_talk:
    show cg_moharius at center with dissolve
    MOHARIUS @talk "Can I help you?"
    menu fortress_inn_moharius_talk_menu:
        "I'd like a room for the night, please." (AppearIf = (EventFortressInn().BoughtKey == False)):
            MOHARIUS @talk "Two hundred coins."
            menu:
                "{i}*Pay the coin*{/i}" (Req_Gold = 200):
                    $ PlayerRemItem("gold", 200)
                    $ EventFortressInn().BoughtKey = True
                    "Carefully, he placed a small, faded iron key into my palm."
                    MOHARIUS @talk "Furthest room on the right."
                    MOHARIUS @talk "We hope you enjoy your stay with us."
                    $ LocEnter()
                "On second thought...":
                    MOHARIUS @talk "Let me know if you want a room."
                    MOHARIUS @talk "Otherwise, Vivian can sort you out with food and drinks, sir."
                    jump fortress_inn_moharius_talk_menu
        "Nothing for now.":
            MOHARIUS @talk "Come see me if you need accommodation for the evening, sir."
            $ LocEnter()

label fortress_inn_vivian_night:
#If the player bought a room and requested Vivian's services
    $ TimeAdvBy(TIME_05H)
    $ LocSet("fortress_inn_room")
    "... That night, there was a gentle knock at my door."
    $ PlaySound(audio.door_knock)
    $ Pause(0.5)
    $ LocFlush()
    show mc at right_f
    with dissolve
    show vivian at cleft with easeinleft
    "As I turned to open it, Vivian carefully stepped into the room, her hips swaying with a slightly exaggerated, playful rhythm."
    VIVIAN @smile "Sir..."
    VIVIAN @smile "Before we begin, there is the matter of my fee."
    MC @think "Go on?"
    VIVIAN @smile "Three hundred for my mouth, five hundred and fifty for my womanhood..."
    VIVIAN @smile "And seven fifty for my..."
    "She paused, letting the word linger."
    VIVIAN @lewd "{i}Rear.{/i}"
    menu:
        "I want your mouth." (Req_Gold = 300):
            $ PlayerRemItem("gold", 300)
            label replay_vivian_bj:
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            VIVIAN @smile "Good choice."
            "Vivian stripped herself naked, letting her clothes slip from her body and fall to the floor."
            VIVIAN @smile "Now then, let me show you my..."
            "She licked her lips enticingly."
            VIVIAN @lewd "{i}Trick.{/i}"
            $ PlaySexFx(audio.ves69_150, 1)
            if CharIsVisiblyPreg("vivian"):
                scene vivian_bj_preg_1
            else:
                scene vivian_bj_nopreg_1
            with dissolve
            $ Pause()
            "... Ten minutes later."
            MC "Ahh! Gods!"
            MC "Where did you learn-"
            "I could only groan in appreciation as Vivian, lying on her back, took me deeper without choking, better than any harlot."
            "Her throat opened to receive me, and as my hand fondled her breast, only soft moans escaped her lips."
            VIVIAN "{i}*Slurp!*{/i} Mmfghh... Lhikhee mhyee thrickhh? {i}*Slurp!*{/i}"
            MC "Ahh! Gods, girl! Don't you need to breathe?!"
            "Vivian didn't answer. She simply continued to dutifully service me, her tongue dancing greedily as she worked."
            "As polite as she was, she certainly knew how to be very 'un-lady-like' when it suited her."
            if CharIsVisiblyPreg("vivian"):
                scene vivian_bj_preg_2
            else:
                scene vivian_bj_nopreg_2
            with dissolve
            $ Pause()
            "Vivian took everything I gave her, and before long I found myself moving faster."
            "She didn't protest. The wet, lewd sounds only grew louder as she obediently continued."
            MC "Ohhh, fuck!"
            MC "V-Vivian!"
            "Her tongue continued to work relentlessly, and I knew I wouldn't be able to last much longer."
            "Vivian's skills were impeccable. For a brief, bemused moment, I wondered if she could teach some of the girls I knew how to perform this little act."
            MC "Ahh...!"
            MC "G-Girl... I'm close."
            "Vivian only moaned softly as I pinched and tugged at one of her nipples."
            VIVIAN "Mmmfghhh...!"
            "She trembled briefly, her breathing growing heavier."
            "Did she just... cum?"
            "If she had, she suppressed any obvious reaction."
            "I laughed. How 'lady-like' of her to remain so dignified."
            "By now, my aching balls were ready to burst."
            "Huffing and puffing, I grunted as I reached my climax."
            $ ReduceInfectionFromSex("vivian")
            if CharIsVisiblyPreg("vivian"):
                $ UnlockGalFlag("vivian", "bj", "var_preg")
            else:
                $ UnlockGalFlag("vivian", "bj", "var_nopreg")
            $ UnlockGalSceneAndGrantXp("vivian", "bj")
            $ PlaySexFx(audio.ves69_finish)
            if CharIsVisiblyPreg("vivian"):
                scene vivian_bj_preg_cum
            else:
                scene vivian_bj_nopreg_cum
            with flash
            $ Pause()
            "For the briefest moment, some of my seed spilled from the corner of her mouth, making her squirm."
            "It seemed even the disciplined Vivian struggled with such quantity."
            "Still, she composed herself before I finally pulled away."
            "She gasped for air, slowly rising to her feet as she wiped her mouth with her arm."
            VIVIAN @shock "Fucking Malakai's balls!"
            VIVIAN @smile "How long were you storing that up?"
            MC @smile "Oh, so you {i}can{/i} drop the lady act when you feel like it."
            "Vivian playfully stuck out her tongue as she gathered her clothes from the floor."
            VIVIAN @smile "Sweet dreams... Sir."
            $ StopReplay()
            scene black with dissolve
            "She didn't linger, quietly closing the door behind her as I dropped onto the bed and sighed contentedly."
        "I want your womanhood." (Req_Gold = 550):
            $ PlayerRemItem("gold", 550)
            label replay_vivian_missionary_vag:
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            "Vivian smirked as she let her clothes slip from her body and fall to the floor, her naked form glistening in the candlelight."
            VIVIAN @smile "Of course you do."
            VIVIAN @smile "Now, take your clothes off and join me on the bed."
            scene black with dissolve
            "A few minutes later..."
            $ PlaySexFx(audio.nijah_miss_1, 1)
            if CharIsVisiblyPreg("vivian"):
                scene vivian_missionary_preg_vag_1
            else:
                scene vivian_missionary_nopreg_vag_1
            with dissolve
            $ Pause()
            VIVIAN "H-Hold my throat!"
            VIVIAN "Ahh! Y-Yes! Like that!"
            "Pinned to the bed beneath my hand at her throat, Vivian squirmed excitedly as I rubbed my cock against the wet, glistening mound of her womanhood."
            MC "For all your uptightness... You seem to enjoy being thrown around."
            "Vivian could only squirm beneath my grip."
            VIVIAN "A good lady knows how to separate her public appearance from her private life."
            VIVIAN "... Now stop teasing me, {i}sir.{/i}"
            VIVIAN "And give me that big cock already!"
            $ PlaySexFx(audio.nijah_miss_2, 1)
            if CharIsVisiblyPreg("vivian"):
                scene vivian_missionary_preg_vag_2
            else:
                scene vivian_missionary_nopreg_vag_2
            with dissolve
            $ Pause()
            "I obliged, pushing my member into Vivian's warmth as she groaned happily."
            "I sank into her inch by inch, drawing back slowly before thrusting into her again."
            VIVIAN "M-Mmmfghh!"
            VIVIAN "Squeeze my throat harder!"
            "I gently tightened my fingertips around her throat as I continued to fuck her."
            "Vivian only tightened around me further, her womanhood soaking as she wheezed softly for air."
            VIVIAN "Y-Yes..."
            VIVIAN "Harder! Give it to me harder!"
            $ PlaySexFx(audio.nijah_miss_3, 1)
            if CharIsVisiblyPreg("vivian"):
                scene vivian_missionary_preg_vag_3
            else:
                scene vivian_missionary_nopreg_vag_3
            with dissolve
            $ Pause()
            "I began to move faster, slamming my cock into Vivian's soaking hole as her eyes watered and slowly rolled back."
            "She choked and wheezed, all while her tight, eager hole eagerly took me."
            VIVIAN "Y-Yheshh!"
            MC "Hrghh! Fuck! Girl!"
            "I continued to pound away for some time."
            "The bedframe rhythmically struck the wall as Vivian's choked moans grew louder."
            "Sweat glistened on her skin as my balls began to ache, desperate to unload into her welcoming pussy."
            MC "I'm close!"
            "Vivian trembled beneath my hand, managing to rasp out,"
            VIVIAN "{i}C-Cum...{/i}"
            "Slamming balls deep into her, I couldn't hold back any longer."
            
            if not QstIsActive(PregFortressInnVivian):
                $ QstStart(PregFortressInnVivian)
            $ PregRoll("vivian")
            $ PlaySexFx(audio.nijah_miss_finish)
            $ ReduceInfectionFromSex("vivian")
            if CharIsVisiblyPreg("vivian"):
                $ UnlockGalFlag("vivian", "missionary", "var_preg_vag")
            else:
                $ UnlockGalFlag("vivian", "missionary", "var_nopreg_vag")
            $ UnlockGalSceneAndGrantXp("vivian", "missionary")
            
            if CharIsVisiblyPreg("vivian"):
                scene vivian_missionary_preg_vag_cum
            else:
                scene vivian_missionary_nopreg_vag_cum
            with flash
            $ Pause()
            MC "HRGHHH!!"
            "As I emptied myself into her, Vivian gasped and twitched."
            "Her body trembled as her eyes rolled back."
            "She let out a whimpering, squealing moan as drool trickled from her lips onto my hand."
            "As I released my grip, she drew in a sharp breath, the faint red marks around her neck still visible as my cum seeped from her."
            VIVIAN @talk "{i}*Huff*{/i} Gods... You really... {i}*Huff*{/i}"
            VIVIAN @smile "Took it all out on me, didn't you?"
            MC @smile "You're the one who wanted it rough."
            $ StopReplay()
            scene black with dissolve
            "Vivian carefully rubbed at her neck as she bent to collect her clothes from the floor."
            VIVIAN @smile "See you in the morning... Sir."
            "Vivian left my room with her clothes still in hand."
        "I want your rear." (Req_Gold = 750):
            $ PlayerRemItem("gold", 750)
            label replay_vivian_missionary_anal:
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            VIVIAN @talk "{i}*Sigh*{/i}"
            VIVIAN @talk "Give me a moment to... prepare myself."
            VIVIAN @smile "... And take off your clothes and get ready for my return."
            scene black with dissolve
            "... Ten minutes later."
            $ PlaySexFx(audio.nijah_miss_1, 1)
            if CharIsVisiblyPreg("vivian"):
                scene vivian_missionary_preg_anal_1
            else:
                scene vivian_missionary_nopreg_anal_1
            with dissolve
            $ Pause()
            "Pinned to the bed, my hand gently squeezed at her throat as the head of my cock teasingly rubbed against her womanhood,"
            "prodding at her lubed-up asshole in anticipation as she squirmed beneath me."
            VIVIAN "Mmfghh...!"
            VIVIAN "E-Eager, aren't we?"
            MC "You're the one who asked for it rough."
            "Vivian simply smiled defiantly, and as my cock continued to tease and prod at her lubed-up ass,"
            "with one sharp push, the head of my cock spread her hole and forced its way a couple of inches into her rear."
            $ PlaySexFx(audio.nijah_miss_2, 1)
            if CharIsVisiblyPreg("vivian"):
                scene vivian_missionary_preg_anal_2
            else:
                scene vivian_missionary_nopreg_anal_2
            with dissolve
            $ Pause()
            VIVIAN "{i}*Gasp!*{/i}"
            "Slowly, I began to move in and out of her ass."
            "The insane tightness of her rear squeezed around me."
            MC "Gods, girl, your ass feels like it was built to take cock!"
            "As my hand lightly flexed around her throat, she struggled not to laugh."
            VIVIAN "I can— Ahh! Assure you— Mmfghh!"
            VIVIAN "This is the result of hard work and training!"
            VIVIAN "Oooh! Go on..."
            VIVIAN "Faster, sir... Mmfghh!"
            VIVIAN "Fuck my ass faster!"
            $ PlaySexFx(audio.nijah_miss_3, 1)
            if CharIsVisiblyPreg("vivian"):
                scene vivian_missionary_preg_anal_3
            else:
                scene vivian_missionary_nopreg_anal_3
            with dissolve
            $ Pause()
            "Vivian groaned as I began to slam my cock into her rear."
            "The bedframe rocked with each thrust, striking the wall with a loud {i}*THUD*{/i}."
            VIVIAN "Y-Yes...!"
            VIVIAN "Mmmfghhh!"
            MC "Didn't think you'd be— {i}*Huff*{/i} So into this!"
            VIVIAN "It's more— Mmfghh!"
            VIVIAN "T-The feeling that I shouldn't be doing it!"
            "As my balls slapped against her, I knew I wouldn't be able to last much longer."
            MC "I'm close!"
            VIVIAN "Do it! F-Finish inside me!"
            $ PlaySexFx(audio.nijah_miss_finish)
            $ ReduceInfectionFromSex("vivian")

            if CharIsVisiblyPreg("vivian"):
                $ UnlockGalFlag("vivian", "missionary", "var_preg_anal")
            else:
                $ UnlockGalFlag("vivian", "missionary", "var_nopreg_anal")
            $ UnlockGalSceneAndGrantXp("vivian", "missionary")

            if CharIsVisiblyPreg("vivian"):
                scene vivian_missionary_preg_anal_cum
            else:
                scene vivian_missionary_nopreg_anal_cum
            with flash
            $ Pause()
            "Burying my cock deep in her ass, I grunted, flooding her rear with my thick load."
            VIVIAN "FUCK!"
            "I couldn't help but laugh at hearing her caught so off guard."
            "Finally, fully spent, I slowly withdrew my cock."
            "Like a cork being pulled from a wine bottle, my cock slipped free as my cum spilled from her stretched ring."
            VIVIAN "Damn it!"
            $ StopReplay()
            scene black with dissolve
            "Vivian rose to her feet, her legs trembling slightly as the seed continued to run down her leg onto the floor."
            VIVIAN @think "There's going to be so much clean-up tomorrow..."
            MC @smile "That's your first thought after letting me plough your ass?"
            VIVIAN @talk "No, my first thought is..."
            VIVIAN @talk "{i}I need a bath.{/i}"
            "Vivian scooped her clothes from the floor into a bundle."
            VIVIAN @talk "Goodnight, sir."
            VIVIAN @smile "{i}Do stop by again soon.{/i}"
            "She winked before closing the door behind her."
        "On second thought, I find myself too tired...":
            $ AutoMus(False)
            stop music fadeout 0.1
            $ PlaySound(audio.scratch_stop)
            "Vivian blinked for a moment, caught off guard before quickly recomposing herself."
            VIVIAN @talk "Of course, sir."
            VIVIAN @talk "I will let you rest in peace."
            hide vivian with dissolve
            scene black with dissolve
    $ AutoMus(True)
    return


############################
####### vivian
label fortress_inn_vivian_impreg:
#### #Vivian impreg (first/rep)
    $ PregFortressInnVivian().ShareImpregNews = False
    show mc at cleft with easeinleft
    show vivian at cright_f with easeinright
    VIVIAN @talk "... We need to talk, {i}sir.{/i}"
    "My eyes drifted down towards her belly as I almost instinctively sensed the change."
    MC @surprised "Are you-"
    if PregFortressInnVivian().NumImpregs == 1:
        VIVIAN @talk "Yes, and it's yours."
        MC @talk "... Do you need coin or anything from me?"
        VIVIAN @talk "No."
        MC @surprised "What?"
        VIVIAN @sad "Just... I'd prefer if you weren't in and out of her life."
        VIVIAN @sad "You're with the Adventurers' Guild. You're hardly the settling-down type."
        VIVIAN @sad "I don't mind you passing by to see how the littlun is doing, but please..."
        VIVIAN @talk "I'll tell her that her father is a brave adventurer, but I'm not making promises about when you'll be back."
        VIVIAN @talk "If you want to get to know your daughter."
    else:
        #Repeat variant
        VIVIAN @talk "Yes... {i}Again.{/i}"
        VIVIAN @angry "Have you considered {i}not{/i} finishing inside me so often?"
        MC @talk "Have you considered not begging me to?"
        VIVIAN @talk "Hmph... Point taken."
        VIVIAN @talk "Nothing has changed. The same rules apply."
        VIVIAN @talk "If you want to know this little one as well."
    #Both continued
    VIVIAN @talk "{i}If you're still alive by then.{/i}"
    VIVIAN @talk "Come back when she's old enough."
    hide vivian with easeoutleft
    "With that, Vivian turned to tend to the other tables."
    show mc at center with ease
    MC @sad "(As depressing as her words were... Perhaps there was some truth in them.)"
    MC "(Still, hopefully there was a future for me in her life.)"
    MC "(... Presuming this infernal war didn't kill me first.)"
    $ LocEnter()
   
#### # After giving birth
label fortress_inn_vivian_postbirth:
    $ PregFortressInnVivian().DoBabyScene = False
    show mc at cleft with easeinleft
    show vivian at cright_f with easeinright
    VIVIAN @smile "Welcome..."
    "In her arms, wrapped in cloth, Vivian cradled a small crying baby."
    VIVIAN @smile "I'll be with you in a moment, sir, once I've fed her."
    VIVIAN @smile "... By the way, what did you think of the name-"
    $ PregFortressInnVivian().BabyName = renpy.input(_("What shall we call her?"), default = _("Kara"))
    VIVIAN @smile "Hm, I'll think on it."
    VIVIAN @talk "Enjoy the rest of your time here, sir."
    $ LocEnter()
