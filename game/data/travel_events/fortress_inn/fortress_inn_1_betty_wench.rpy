label fortress_inn_betty_firsttime:
    $ EventFortressInn().SeenFirstTimes[EventFortressInn().VariantID] = True
    show mc at left with easeinleft
    "Upon entering, a busty blonde woman carrying two ales smiled as she placed them on the table."
    show betty at center with dissolve
    BETTY @happy "Welcome, lovelies!"
    BETTY @happy "Welcome to {i}The Naughty Wench.{/i} I trusted your travels had been long and hard?"
    "She smiled and winked."
    BETTY @blush "My name's Betty. Come, come take a seat. Let me and ma' husband fetch you somethin'!"
    BRYHER @talk "Don't forget to offer 'em a room!"
    BETTY @angry "I WAS ABOUT TO, DEAR!"
    BETTY @happy "Never mind me husband, Bryher. Just let me or my husband know if you wanted anything."
    BETTY @happy "What could I do for you, love?"
    jump fortress_inn_betty_talk_menu

label fortress_inn_betty_talk:
    show betty at center with dissolve
    BETTY @happy "What could I do for you, love?"
    menu fortress_inn_betty_talk_menu:
        "I'd like to order something.":
            BETTY @happy "Sure! What would you like?"
            menu:
                "I'd like a drink, please." (Req_Gold = 15):
                    $ PlayerRemItem("gold", 15)
                    BETTY @happy "Coming right up!"
                    "Betty hurried to the bar before returning with a jug of ale topped with a thick white froth."
                    BETTY @happy "Hope that quenched your thirst!"
                    $ EventFortressInn().GetDrink()
                    "Upon sipping the drink, I sighed, already feeling remarkably better."
                "I'd like some food, please." (Req_Gold = 25):
                    $ PlayerRemItem("gold", 25)
                    BETTY @happy "We've got just the thing for you!"
                    BETTY @happy "Roasted boar and onion!"
                    scene black with dissolve
                    $ TimeAdvBy(TIME_1H)
                    "Betty sauntered off and returned about thirty minutes later with my steaming meal."
                    $ EventFortressInn().GetFood()
                    $ LocFlush()
                    show betty at center
                    with dissolve
                    BETTY @blush "Enjoy, darling!"
                    "She wandered off to another table."
                "I've changed my mind.":
                    BETTY @talk "Call me over when you wanted to order something, love."
            jump fortress_inn_betty_talk_menu

        "Heard any rumors around these parts?":
            BETTY @happy "Rumors?"
            $ tmpvar = RngInt(1, 4)
            if tmpvar == 1:
                BETTY @talk "Rumor had it strange things were happening on the Orasmore Isles."
                BETTY @shock "People were saying the lands were cursed!"
            elif tmpvar == 2:
                BETTY @talk "There'd been talk of some scaly monster going toe to toe with Zanarak on the city walls!"
                BETTY @think "Sounded to me like a bunch of drunkards imagining things."
            elif tmpvar == 3:
                BETTY @talk "They said the GTC and the merchant lords' trade war was getting more and more volatile by the day."
                BETTY @angry "Greedy bastards... How much coin did they bloody need?"
            elif tmpvar == 4:
                BETTY @sad "Rumor had it there were orcs hiding up north in Angmurus."
                BETTY @scared "Didn't know what was scarier... them or the Demorai."
                if CharInParty("ves"):
                    VES @talk "..."
                    BETTY @scared "FUCKING HELLS!"
                    VES @angry "I am not scary!"
                    VES @angry "I am very lovable!"
                    BETTY @talk "W-Whatever you say, uhh... love."
                    BETTY @talk "I guessed adventuring parties were a lot more open now than when I lived in the capital!"
            jump fortress_inn_betty_talk_menu

        "How is the littlun?" (AppearIf = CharGetBirths("betty") > 0):
            BETTY @talk "Loves their milk and sucking on my tits."
            "Betty's eyes fluttered as she looked at me alluringly."
            BETTY @lust "{i}Reminded me of his father...{/i}"
            jump fortress_inn_betty_talk_menu

        "Do you provide any... {i}'special services?'{/i}" (AppearIf = (EventFortressInn().ScheduledFuntime == False)):
            "Betty blinked at the request before a small, alluring smile appeared on her lips."
            "She inched closer, speaking in a hushed tone while glancing back at her husband. He looked at her and nodded."
            BETTY @blush "Well, sir... We did provide an evening {i}nightcap and some... companionship.{/i}"
            BETTY @blush "{i}For an extra fee.{/i}"
            "Her hands carefully brushed against me."
            BETTY @talk "You'd have to get a room here... But was that something you'd like?"
            menu:
                "Yes.":
                    BETTY @happy "Then I'd make arrangements to swing by your room this evening."
                    $ EventFortressInn().ScheduledFuntime = True
                "No.":
                    "Betty pulled away."
                    BETTY @talk "Well, if you changed your mind."
                    BETTY @talk "You knew where to find me."
            jump fortress_inn_betty_talk_menu
        "I best get going...":
            BETTY @happy "Safe travels!"
            $ LocEnter()

#### Speaking to Bryher
label fortress_inn_bryher_talk:
    show cg_bryher at center with dissolve
    BRYHER "Interested in drinks or food? Speak to the wife."
    BRYHER "If you wanted a room, let me know."
    menu fortress_inn_bryher_talk_menu:
        "I'd like a room for the night, please."  (AppearIf = (EventFortressInn().BoughtKey == False)):
            BRYHER @talk "One hundred and fifty coins."
            menu:
                "{i}*Pay the coin*{/i}" (Req_Gold = 150):
                    $ PlayerRemItem("gold", 150)
                    $ EventFortressInn().BoughtKey = True
                    "He handed me a small iron key."
                    BRYHER @talk "Rooms were upstairs on the far left."
                    $ LocEnter()
                "On second thought...":
                    "The man turned away and resumed cleaning the cups."
                    jump fortress_inn_bryher_talk_menu
        "Nothing for now.":
            BRYHER @talk "Then why were you wasting my time?"
            $ LocEnter()

#### If the player told Betty they were interested in her 'night services', this triggered upon entering the player's room.
label fortress_inn_betty_night:
    $ TimeAdvBy(TIME_05H)
    $ LocSet("fortress_inn_room")
    "... Later that night."
    $ PlaySound(audio.door_knock)
    $ Pause(0.5)
    $ LocFlush()
    show mc at right_f
    with dissolve
    show betty at cleft with easeinleft
    BETTY @happy "Sorry I'm late. Had to wait till all the other guests were asleep."
    "Betty's eyes wandered over my body."
    BETTY @blush "Fucking hells, looks like I got lucky tonight."
    BETTY @blush "You're a lot tastier looking than the usual fucks who want this."
    MC @think "Is your husband asleep?"
    BETTY @happy "Don't worry about him, love. He knows we've gotta make coin where we can."
    BETTY @happy "He won't bother us tonight."
    MC @think "How much?"
    BETTY @happy "Two hundred for my mouth. Three-fifty for my womanhood..."
    "She paused."
    BETTY "Five hundred for me arse, because I hate not being able to walk properly in the morning."
    menu:
        "I want your mouth." (Req_Gold = 200):
            $ PlayerRemItem("gold", 200)
            label replay_betty_bj:
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            BETTY @happy "Is this you trying to say I'm too chatty?"
            BETTY @lust "Or that you're wondering what else this mouth can do?"
            MC @smile "Show me what it can do."
            BETTY @lust "...Get yer kit off."
            $ PlaySexFx(audio.adara_hj_loop, 1)
            scene betty_bj_1
            with dissolve
            $ Pause()
            "The two of us stripped down as Betty pushed me onto the bed."
            "Wrapping her huge, warm tits around me, Betty smiled as she began to massage my cock."
            BETTY "You should know, no man's lasted very long when I do this."
            "As she pushed her tits together and squeezed my cock between her breasts,"
            "I could feel my cock throb with excitement."
            scene betty_bj_2
            with dissolve
            $ Pause()
            MC "I should've guessed you'd be so— {i}*Huff*{/i}"
            MC "Talented..."
            BETTY "The gods blessed me with huge tits, and I make good use of that blessing."
            BETTY "Backache aside, these fucking milkers earned me more tips than any smile or witty comment, I can assure you of that!"
            "Betty licked her lips as she looked down at my cock."
            BETTY "You ready for the main event, love?"
            MC "Stop teasing and put those fat lips on my cock already."
            BETTY "Fuckin' man after me own heart."
            $ PlaySexFx(audio.adara_hj_loop_x2, 1)
            scene betty_bj_3
            with dissolve
            $ Pause()
            "Betty's soft, wet lips wrapped around the head of my member as she began to suckle on it."
            "Her head dipped in a steady rhythm as she suckled on my member, taking me a little deeper while continuing to massage me with her soft, pillowy tits."
            BETTY "{i}*Slurp!* *Slurp!*{/i} Mmfghh..."
            BETTY "Shuchh ahhh— {i}*Slurp!*{/i} bhighh chockhh..."
            BETTY "Mmmfghh..."
            "Betty's tongue danced around the tip, circling the head as she giggled teasingly to herself."
            MC "Ahh!"
            MC "Your huge tits were made to be wrapped around my cock."
            "Betty didn't answer. Instead, she simply moved her head faster."
            "Taking me deeper as I groaned."
            $ PlaySexFx(audio.adara_hj_loop_x3, 1)
            scene betty_bj_4
            with dissolve
            $ Pause()
            "Her tongue thrashed around furiously as she squeezed her tits together even tighter."
            MC "{i}*Huff*{/i} Betty... Ahh...!"
            MC "Gods, did your husband teach you how to do this?!"
            "Betty could only laugh with my cock still stuffed in her mouth."
            "Somehow, I took that to be a {i}no.{/i}"
            "Her lips continued to glide over my cock, dragging me towards the edge before pulling back just enough."
            MC "{i}*Huff*{/i} This is torture, wench!"
            MC "Push me over the damn edge already!"
            BETTY "{i}*Slurp!* Mmfghh...!{/i}"
            BETTY "Whishh ghranthhdd! {i}*Slurp!*{/i}"
            "Finally, she thrust her head forward, and my aching, heavy balls could take no more as I grunted,"
            "flooding her mouth with my load."
            $ ReduceInfectionFromSex("betty")
            $ UnlockGalSceneAndGrantXp("betty", "bj")
            $ PlaySexFx(audio.adara_hj_finish)
            scene betty_bj_cum
            with flash
            $ Pause()
            MC "HRGHHHH!"
            "Betty's eyes widened as she squealed slightly at the rush pouring into her mouth."
            "Much of it spilled down and glazed her tits before she pulled away with a *PLOP*."
            "She licked her lips, smiled, and stood back up."
            BETTY "Mmm... Tasty."
            BETTY "Glad to be of service, hun."
            BETTY "{i}Sweet dreams, fufu...{/i}"
            $ StopReplay()
            scene black with dissolve
            "Grabbing her clothes from the floor, Betty blew me a kiss before quietly closing the door behind her."
            "Sweet dreams indeed..."
        "I want your pussy." (Req_Gold = 350):
            $ PlayerRemItem("gold", 350)
            label replay_betty_missionary_vag:
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            BETTY @happy "Take off your clothes, love."
            scene black with dissolve
            "As the two of us stripped down, Betty's eyes widened, her mouth hanging agape as she stared at my cock."
            BETTY @shock "Fucking hells... What a cock!"
            "She giggled nervously, smiling alluringly as she moved towards the bed."
            BETTY @blush "Come on, I can't wait to feel what that thing can do..."
            $ PlaySexFx(audio.nijah_miss_1, 1)
            if CharIsVisiblyPreg("betty"):
                scene betty_missionary_preg_vag_1
            else:
                scene betty_missionary_nopreg_vag_1
            with dissolve
            $ Pause()
            "Betty lay down on the bed and spread her legs expectantly for me."
            BETTY "Come on, don't keep me waiting."
            "As I rubbed my cock against her glistening womanhood, she let out a shuddering moan."
            BETTY "Bet you make all the girls squeal with that huge cock."
            MC "Are you ready for it?"
            BETTY "Shove that fat prick in, handsome."
            "I wasted no time, pushing my cock into her tight warmth as Betty cooed happily."
            $ PlaySexFx(audio.nijah_miss_2, 1)
            if CharIsVisiblyPreg("betty"):
                scene betty_missionary_preg_vag_2
            else:
                scene betty_missionary_nopreg_vag_2
            with dissolve
            $ Pause()
            BETTY "MMMMFGHHH...!"
            BETTY "You're stretching me out so— Ahh! Much!"
            "Her wet cunt squeezed effortlessly around me."
            "Wet squelching sounds filled the room as I fucked her."
            MC "Does your husband— Ahh! Fill you like this?"
            BETTY "Course not! Mmfghh..."
            BETTY "That's why we're— Oooh! Happy with this little arrangement!"
            BETTY "All the fort inns like ours— Ahh! Got someone selling their ass!"
            BETTY "Too much money from travelling merchants and adventurers to pass up!"
            BETTY "We can't afford no— Ahh! Fucking hells! Yes!"
            BETTY "Mhmm, no slutty barmaid, so... Oooh!"
            BETTY "He turns a blind eye to my ass being on the line!"
            BETTY "Oooh! Fuck! Harder! Fuck my little pussy harder!"
            $ PlaySexFx(audio.nijah_miss_3, 1)
            if CharIsVisiblyPreg("betty"):
                scene betty_missionary_preg_vag_3
            else:
                scene betty_missionary_nopreg_vag_3
            with dissolve
            $ Pause()
            "I slammed my cock harder into Betty as she continued to moan."
            "Her huge tits rocked with each thrust as she laughed, squeezing me with her tight hole."
            BETTY "Oooooh!"
            BETTY "That's it! Mmfghh! Give it to me!"
            "She squeezed and fondled her own tits, playing with her nipples as her moans grew louder."
            BETTY "G-Give it to me! Don't stop!"
            "From the volume of her moans and the bed rocking beneath us, there was little doubt her husband and the other guests had heard something."
            "... It was hard to worry about that, though, especially while buried balls deep in Betty."
            MC "Hrghh! I'm close, you wench!"
            BETTY "Ahh! F-Fuck!"
            BETTY "Come on, love! I can feel how full those balls are slapping against me!"
            BETTY "Dump it all into me!"
            "As I slammed my cock into her, Betty gasped as she felt my heavy balls empty into her puffy pussy."
            if not QstIsActive(PregFortressInnBetty):
                $ QstStart(PregFortressInnBetty)
            $ PregRoll("betty")
            $ PlaySexFx(audio.nijah_miss_finish)
            $ ReduceInfectionFromSex("betty")
            if CharIsVisiblyPreg("betty"):
                $ UnlockGalFlag("betty", "missionary", "var_preg_vag")
            else:
                $ UnlockGalFlag("betty", "missionary", "var_nopreg_vag")
            $ UnlockGalSceneAndGrantXp("betty", "missionary")
            if CharIsVisiblyPreg("betty"):
                scene betty_missionary_preg_vag_cum
            else:
                scene betty_missionary_nopreg_vag_cum
            with flash
            $ Pause()
            MC "HRGHHHHH...!!"
            BETTY "{i}*GASPS!*{/i}"
            BETTY "Gods! I'm gonna be walking around with your cum dripping out of me for WEEKS!"
            BETTY "You part horse or somethin'?"
            "I laughed as Betty climbed back to her feet and grabbed her dress from the floor."
            MC @think "Where are you going?"
            BETTY @happy "Back to bed, love, before hubby wakes up."
            "She chuckled, giving me a kiss on the cheek before slipping out of the room."
            $ StopReplay()
            scene black with dissolve
            SHYAHTAN "(... Good for breeding.)"
            MC "(You say that about everyone.)"
            SHYAHTAN "(Her ample breasts should suckle many of our young.)"
        "I want your ass." (Req_Gold = 500):
            $ PlayerRemItem("gold", 500)
            label replay_betty_missionary_anal:
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            BETTY @think "What is it with men trying to shove their cock into places they don't belong?"
            MC @think "Is that a no?"
            "Betty grinned, giving her own ass a playful slap."
            BETTY @happy "It ain't my first pick, but I can take you in me arse."
            "As the two of us stripped naked, Betty's eyes settled on the hard member in front of her."
            BETTY @shock "Fitting that back there is going to be..."
            BETTY @happy "A bit of a challenge."
            MC @smile "Are you up for a challenge?"
            BETTY @happy "Sure... Just let me grab some lube first."
            "Betty scurried off to fetch something before hurrying back to my room."
            BETTY @happy "All prepped and ready for you, love."
            $ PlaySexFx(audio.nijah_miss_1, 1)
            if CharIsVisiblyPreg("betty"):
                scene betty_missionary_preg_anal_1
            else:
                scene betty_missionary_nopreg_anal_1
            with dissolve
            $ Pause()
            "Betty giggled as she climbed onto the bed and spread her legs expectantly."
            BETTY "Come on, don't keep me waiting."
            "As I teasingly rubbed my cock against her lubed-up hole, her pussy glistened with excitement."
            MC "I haven't been able to keep my eyes off your ass since I walked in."
            BETTY "And here you are, about to stretch it and fuck it silly."
            BETTY "Funny how life goes, eh?"
            MC "Are you ready for this?"
            BETTY "No..."
            BETTY "But I bet your fat prick's gonna make me cum anyway."
            "As I pushed against her tight little hole, she tensed for a moment before relaxing. Her hole spread around the head of my cock as I eased a few inches inside."
            $ PlaySexFx(audio.nijah_miss_2, 1)
            if CharIsVisiblyPreg("betty"):
                scene betty_missionary_preg_anal_2
            else:
                scene betty_missionary_nopreg_anal_2
            with dissolve
            $ Pause()
            BETTY "{i}*Gasp!*{/i}"
            BETTY "Gods... You're really— {i}*Huff*{/i} REALLY stretching me!"
            MC "Need a minute?"
            BETTY "J-Just go slow... Ahh! Ease me butt into it, alright?"
            "I did as Betty asked, slowly pounding her fat rear and letting her grow accustomed to the feeling of my cock inside her ass before carefully pushing deeper."
            BETTY "Mmfghh..."
            BETTY "Is... Is my arse still good?"
            "For the briefest moment, Betty's cheeks flushed red as she shyly looked away."
            BETTY "W-Wouldn't you rather be fucking some younger lass's rear than mine?"
            BETTY "Me husband hardly wants it from me anymore."
            BETTY "Just quickies and maybe a blowjob once a month."
            MC "Then your husband's a fool."
            MC "I'd fuck this tight ass every night and dump a load in it if I could."
            "I felt Betty tighten around me at my words."
            BETTY "Y-Yes... Ahh...!"
            BETTY "H-Harder..."
            BETTY "I'm ready for you to give it to me proper now!"
            $ PlaySexFx(audio.nijah_miss_3, 1)
            if CharIsVisiblyPreg("betty"):
                scene betty_missionary_preg_anal_3
            else:
                scene betty_missionary_nopreg_anal_3
            with dissolve
            $ Pause()
            "Not wanting to leave a girl wanting, I began to slam my cock into her tight hole."
            "Betty groaned as her tight hole squeezed and stretched around me."
            BETTY "F-Fuckkkk...!"
            BETTY "It's burning! Ahh! My fucking ass is b-burning!"
            MC "Should I—"
            BETTY "Don't you fuckin' dare!"
            BETTY "After— Ahh! Sweet-talking me and fucking this hole!"
            BETTY "Don't you dare stop till you've left me feelin' like I'm young, dumb and full of cum again!"
            MC "You've got a way with words."
            BETTY "A dick in my arse tends to bring out the poet in me!"
            "I laughed as Betty's asshole continued to squeeze around me, trying to wring my cock dry."
            "As I continued to pound away, my balls slapped against her while her huge tits bounced and the bedframe slammed against the wall."
            "{i}*Thud* *Thud* *Thud!*{/i}"
            "I wondered if her husband could hear me fucking his wife's ass."
            BETTY "Ahhh...! You— {i}*Huff*{/i} big-dicked bastard!"
            BETTY "Ooooooh!"
            BETTY "I-I'm close... I'm close, ya hear?!"
            BETTY "Can't believe you're gonna make me cum from my ass!"
            BETTY "{i}F-Fuckin' hells...{/i}"
            "Betty's ass tightened around me as increasingly vulgar thoughts tumbled from her mouth."
            BETTY "I don't want to— Ahh! Walk straight for a week!"
            BETTY "S-Stretch my arse out! I want my husband to know, when he sees me wobbling, you've ruined my shitter!"
            BETTY "Don't s-stop! Don't—"
            "Betty's eyes rolled back as her body convulsed and trembled."
            "Her tight ass squeezed around my cock as her body went into spasms."
            "All Betty could mutter between breathless moans was, 'Oh gods!' as she came."
            "I continued to plough away for some time as hot little moans escaped her lips and she let me have my way with her."
            "Eventually, as my balls felt heavy and my cock ached to finish,"
            "I forced my cock to the hilt, grunting as my balls slapped against her and unloaded into the tight ass of the married wench."
            $ PlaySexFx(audio.nijah_miss_finish)
            $ ReduceInfectionFromSex("betty")
            if CharIsVisiblyPreg("betty"):
                $ UnlockGalFlag("betty", "missionary", "var_preg_anal")
            else:
                $ UnlockGalFlag("betty", "missionary", "var_nopreg_anal")
            $ UnlockGalSceneAndGrantXp("betty", "missionary")
            if CharIsVisiblyPreg("betty"):
                scene betty_missionary_preg_anal_cum
            else:
                scene betty_missionary_nopreg_anal_cum
            with flash
            $ Pause()
            MC "HRGHHHH...!"
            "By now, Betty had been thoroughly fucked senseless."
            "As I filled her ass, she could only coo and moan softly."
            "Satisfied I'd pumped her ass full of my seed, I slowly withdrew my cock, watching as the cum seeped back out."
            $ StopReplay()
            scene black with dissolve
            "After about an hour, Betty's shaky legs finally steadied as she rose to her feet and made her way back towards her room."
            "Not even bothering to dress, I watched the curvy wench wander back to her husband's side, my cum still seeping down her legs."
            "She blew me a kiss before disappearing."
        "Actually, my coin pouch is a little short...":
            $ AutoMus(False)
            stop music fadeout 0.1
            $ PlaySound(audio.scratch_stop)
            BETTY @sad "Sorry, love, ain't runnin' a charity here."
            BETTY @sad "Call me back when you can afford yer evenin' {i}entertainment.{/i}"
            hide betty with dissolve
            "Without another word, Betty turned and left."
            scene black with dissolve
    $ AutoMus(True)
    return

##############################
##### Betty pregnancy content
label fortress_inn_betty_impreg:
    $ PregFortressInnBetty().ShareImpregNews = False
    show mc at cleft with easeinleft
    "As I entered through the doors of {i}The Naughty Wench,{/i}"
    show betty at cright_f with easeinright
    "Betty made her way towards me with a huge grin."
    "To my surprise, my eyes weren't drawn to her huge tits for once..."
    "{i}But to her heavily pregnant belly.{/i}"
    MC @surprised "B-Betty! You're-"
    if PregFortressInnBetty().NumImpregs == 1:
        # First time
        BETTY @happy "Pregnant!"
        BETTY @happy "My husband's over the moon that we've got a littlun on the way again, ain't ya?!"
    else:
        # Repeat variant
        BETTY @happy "Pregnant again!"
        BETTY @happy "Aren't me and my husband blessed?"
    # Both continued
    BRYHER "... Hmph."
    "Betty inched closer."
    BETTY @talk "{i}Now listen, lover boy, before you get any ideas.{/i}"
    BETTY @talk "{i}This ain't the first time I've been knocked up, and it probably ain't gonna be the last.{/i}"
    BETTY @talk "{i}Just keep playing dumb, and no matter how many little 'accidents' we have, I'll let you fill my belly and womb with as much cum as you want.{/i}"
    BETTY @talk "{i}... Just keep your mouth shut.{/i}"
    BETTY @lust "{i}Daddy.{/i}"
    hide betty with easeoutleft
    "With that, Betty sauntered off towards another table."
    show mc at center with ease
    MC @think "(Is it definitely-)"
    SHYAHTAN "(Yes, it is ours.)"
    SHYAHTAN "(And she yearns to carry more of our seed.)"
    MC @smile "(Good to know...)"
    MC @smile "(A pair of ass and tits like that is wasted on her husband.)"
    $ LocEnter()

##########################
########## After giving birth
label fortress_inn_betty_postbirth:
    $ PregFortressInnBetty().DoBabyScene = False
    show mc at cleft with easeinleft
    BETTY @happy "Ahh! Look who's here!"
    show betty at cright_f with easeinright
    BETTY @happy "Your papa and mama's {i}special friend!{/i}"
    "Betty grinned as she walked over, the baby cradled in her arms."
    BETTY @happy "{i}How strange...{/i}"
    BETTY @lust "{i}He looks so much more like you than my husband!{/i}"
    "She glanced over at her husband, who willingly chose to ignore the comment."
    "Was he in denial, or simply a willing cuckold? I wasn't sure, nor did I think it wise to ask."
    MC @smile "How strange indeed."
    MC @smile "... It's a boy?"
    BETTY @happy "'Tis indeed. Any ideas for a name?"
    $ PregFortressInnBetty().BabyName = renpy.input(_("What shall we call him?"), default = _("Karnesh"))
    BETTY @happy "That's a lovely name."
    BETTY @happy "Anyway, looks like it's feeding time for this littlun!"
    "Betty winked."
    BETTY @happy "Call me over if you need anything..."
    BETTY @lust "{i}Any...thing.{/i}"
    "I watched her hips sway as she sauntered away."
    SHYAHTAN "(We should consider breeding her again soon...)"
    $ LocEnter()
