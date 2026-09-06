label qst_BigTroubleLHamun_khazah_approach_hideout:
    if IsGoalVisible(QstBigTroubleLH, 3):
        MC "(I have already talked to the Khazah.)"
        MC "(I can now tell Marbella about their offer...)"
        $ LocEnterQ()
    # Khazah route
    # The player approaches the Khazah hideout and is stopped by a Khazah guard
    play sound "audio/cfx/door_knock.ogg"
    "I knocked on the wooden door."
    play sound "audio/cfx/doorthud.ogg"
    show cg_bandit at center with dissolve
    KHAZAH "What do you want?"
    menu:
        "I have an offer for the Khazah.":
            pass
        "Nothing.":
            KHAZAH "Then leave and stop wasting my time!"
            $ LocEnter()
    "The guard's eyes looked me up and down for a moment."
    KHAZAH "What kind of offer?"
    MC @serious "The kind only your boss should hear."
    KHAZAH "... Hmm."
    KHAZAH "You are either very brave, or very stupid."
    KHAZAH "... Fine."
    "Opening the door, the guard stepped aside."
    KHAZAH "Watch yourself."
    scene black with dissolve
    $ LocSet("hamun_khazah_hideout")
    $ LocFlush(dissolve)
    show mc at cright_f with easeinright
    KHAZAH "Who are you?"
    MC @talk "I'm here to speak to whoever's in charge."
    KHAZAH "Ha! Are you now?"
    KHAZAH "I should—"
    KHAZAH_LEADER "Step back, Azan."
    KHAZAH "But he's—"
    KHAZAH_LEADER "Don't you recognize {i}The Beast of Novaras?{/i}"
    "The Khazah guard's eyes widened in panic."
    show cg_bandit at cleft with easeinleft
    KHAZAH_LEADER "If he wanted to try and kill us,"
    KHAZAH_LEADER "I am afraid there is little we could do to stop him."
    MC @talk "Your Alderian is almost perfect."
    KHAZAH_LEADER "Your words are kind."
    KHAZAH_LEADER "Now tell me, what brings the saviour of Hamun here?"
    MC @talk "Lord Zanzibat wishes you dead."
    KHAZAH_LEADER "That is... to be expected."
    KHAZAH_LEADER "We have found much resistance to our presence in this city."
    MC @talk "I'm here to see if you can give me a counteroffer."
    KHAZAH_LEADER "To kill Lord Zanzibat?"
    KHAZAH_LEADER "I'm afraid that would paint too big of a target on all of our backs."
    MC @serious "Lord Zanzibat, in return for me wiping you all out, has offered to provide protection to a dwarf in this city named Marbella."
    MC @serious "She runs {i}The Crooked Shaft and Co.,{/i} and the Greater Trading Company is trying to push her out."
    KHAZAH_LEADER "... And Lord Zanzibat offered her protection in return for our murder?"
    MC @talk "Protection and twenty percent of the profits."
    KHAZAH_LEADER "HA!"
    KHAZAH_LEADER "The desert fox is indeed as greedy as they say he is."
    MC @think "And what can you offer me instead?"
    KHAZAH_LEADER "Hmm... She is a miner, you say?"
    KHAZAH_LEADER "A supply of gems would serve us better than a direct cut of profits... They could be sold elsewhere, somewhere like Newyark onwards toward Synmaria."
    MC @think "Just some gems?"
    KHAZAH_LEADER "Mmm... Not quite."
    KHAZAH_LEADER "Khazah leadership has made it clear: a woman's role in the Khazah is limited."
    KHAZAH_LEADER "If she wants our protection, she would need to be willing to service the men here."
    MC @surprised "What?!"
    KHAZAH_LEADER "I do not make the rules."
    KHAZAH_LEADER "If a woman was found here and she wasn't willing to service the men, it would be seen that I am elevating her rank."
    KHAZAH_LEADER "{i}Then it would be {b}*my*{/b} head on a pike.{/i}"
    MC @serious "I see."
    KHAZAH_LEADER "Come back with her answer, should you wish."
    $ GoalShow(QstBigTroubleLH, 3)
    $ QstBigTroubleLH().TalkedToKhazahOffer = True
    KHAZAH_LEADER "Until then..."
    "He offered a curt bow, taking a few steps back."
    KHAZAH_LEADER "I have other business to attend to."
    MC "(Hmm...)"
    MC "(Something tells me Marbella isn't going to like this offer.)"
    MC @think "(But maybe it is the safest bet?)"
    $ LocEnter()

label qst_BigTroubleLHamun_marbella_khazah_offer:
    MARBELLA @angry "... Who the fuck are the Khazah?"
    MARBELLA @shock "Wait, aren't they one of those gangs trying to muscle into Hamun from the capital?"
    MARBELLA @angry "You can't be bloody serious!"
    MC @talk "They're asking for only a ten percent cut... You're not going to get a better offer than that."
    MARBELLA @think "... What's the catch?"
    MC @think "..."
    MARBELLA @angry "What's the bloody catch, mate?"
    MC @serious "They want you to... Uh... work for them some nights."
    MARBELLA @think "Work for—"
    MARBELLA @think "Doing what?"
    MC @talk "..."
    MARBELLA @shock "...WHAT?!"
    MARBELLA @angry "HAVE YOU LOST YOUR MIND?!"
    MARBELLA @sad "Gods... You can't be serious!"
    MARBELLA @sad "My reputation would be ruined if people found out I was some gang's whore!"
    MARBELLA @sad "There... There has to be another way."
    MARBELLA @sad "{i}... Right?{/i}"
    menu:
        "No, Marbella, this is the only way.":
            # Gang route lock in
            MARBELLA @sad "... I—"
            MARBELLA @sad "I need some time to think about this, please?"
            scene black with dissolve
            "I turned to leave a dejected Marbella alone, no doubt torn over the offer."
            MC "(I should come back tomorrow for her answer...)"
            $ LocSet("hamun_dist_docks")
            $ LocFlush(dissolve)
            
            $ GoalComplete(QstBigTroubleLH, 1)
            if IsGoalVisible(QstBigTroubleLH, 2):
                $ GoalHide(QstBigTroubleLH, 2, Silent = True)
            $ GoalComplete(QstBigTroubleLH, 3, Silent = True)
            $ GoalShow(QstBigTroubleLH, 1000)

            $ QstBigTroubleLH().Kind = "gang"
            $ HouseLockHamunKhazahHideout().State = "operating"
            $ QstBigTroubleLH().Gang_ComeBackNextDay = True
            $ LocEnter()

        "You're right, there has to be another way... I'll keep looking.":
            MARBELLA @think "Thank the gods..."
            jump qst_BigTroubleLHamun_return_to_marbella_options

label qst_BigTroubleLHamun_marbella_gang_closed:
    MC "(I should let Marbella think on that offer the Khazahs gave.)"
    $ LocEnterQ()

#################################################################
#Route 3 - GANG-WHORE ROUTE - prostitution/swinging route 
# (Marbella will start working at a gang hideout during 
# SOME evenings as their whore - every other evening of the week)
#################################################################
# Gang whore route 1 - The Crooked Shaft and Mining Co (the player returns the next day)
label qst_BigTroubleLHamun_marbella_khazah_return_after_offer:
    show marbella at cleft
    show mc at cright_f with easeinright
    "As I entered the Crooked Shaft, a nervous Marbella looked up from her desk."
    show marbella at center with ease
    "She moved closer, uncertain and sheepish."
    $ GoalComplete(QstBigTroubleLH, 1000)
    MARBELLA @sad "... Can the Khazah really keep me safe?"
    MC @talk "Yes, I believe so."
    MARBELLA @sad "... Fuck me, I can't believe I'm agreeing to this."
    MARBELLA @angry "Fine. Tell those fucks I'm ready."
    $ GoalShow(QstBigTroubleLH, 1010)
    $ LocEnter()

############################################################################################################################################################
#Gang whore route - 2 - Khazah hideout 
#The player speaks to the Khazah leader
label qst_BigTroubleLHamun_marbella_khazah_talk_to_leader_marbella_agreed:
    $ QstBigTroubleLH().Gang_TalkedToLeaderAboutRivals = True
    KHAZAH_LEADER "This is good news."
    KHAZAH_LEADER "Now there is just the matter of securing our foothold in the city."
    MC @serious "She's agreed to her end of the deal. You need to keep yours."
    KHAZAH_LEADER "And we shall."
    KHAZAH_LEADER "But there are a few petty rivals we must deal with first."
    MC @think "'Petty rivals?'"
    KHAZAH_LEADER "The Khazah are keen to expand. Where there is expansion, there is always opposition."
    KHAZAH_LEADER "Just a few small groups attacking our couriers."
    KHAZAH_LEADER "They think we are easy prey because we are young blood in this city."
    KHAZAH_LEADER "{i}They are mistaken.{/i}"
    MC @serious "How long do you think it will take to deal with them?"
    KHAZAH_LEADER "A few weeks..."
    KHAZAH_LEADER "Unless..."
    KHAZAH_LEADER "I could pay you to deal with this little problem for us."
    MC @talk "How much?"
    KHAZAH_LEADER "Would fifteen hundred coins suffice?"
    menu qst_BigTroubleLHamun_marbella_khazah_talk_to_leader_marbella_agreed_menu:
        "Deal.":
            KHAZAH_LEADER "Good."
            $ GoalComplete(QstBigTroubleLH, 1010)
            KHAZAH_LEADER "They tend to linger around this part of the city."
            KHAZAH_LEADER "Look for them at night."
            KHAZAH_LEADER "Good hunting..."
            $ GoalShow(QstBigTroubleLH, 1020)
            $ LocEnter()
        "You're hiring 'The Beast of Novaras,' remember? Two thousand at least." (AppearIf = (QstBigTroubleLH().Gang_DealWithRivalsPay == 1500), Req_Barter = 15): #Barter check 15
            $ QstBigTroubleLH().Gang_DealWithRivalsPay = 2000
            $ GoalComplete(QstBigTroubleLH, 1010)
            KHAZAH_LEADER "Fine. Two thousand it is."
            KHAZAH_LEADER "Just bring me their heads."
            $ GoalShow(QstBigTroubleLH, 1020)
            $ LocEnter()
        "I'll need to think on it.":
            KHAZAH_LEADER "Very well. Let me know if you change your mind."
            $ LocEnter()

#Ends conversation, upon re-speaking, 
# the Khazah leader will say "Have you changed your mind?" - same menu prompts
label qst_BigTroubleLHamun_marbella_khazah_talk_to_leader_marbella_agreed_rep:
    KHAZAH_LEADER "Have you changed your mind?"
    jump qst_BigTroubleLHamun_marbella_khazah_talk_to_leader_marbella_agreed_menu


screen HamunFindKhazahRivals():
    if not block_wait_global and not block_wait_dynamic and wLocs[GetLocID()].CanWait:
        if IsGoalVisible(QstBigTroubleLH, 1020):
            if not IsDaytime():
                fixed:
                    fit_first True
                    align (0.18, 0.81)
                    text tra(_("Gangs slain: %s/3")) % QstBigTroubleLH().Gang_SlainRivalGangs:
                        xalign 0.5
                        yoffset -40
                    add "images/gui/buttons_loc/underlay.webp":
                        xalign 0.5
                    imagebutton:
                        idle "images/gui/buttons_loc/fight.webp"
                        hovered TooltipSetUI(_("Patrol"))
                        unhovered TooltipClearUI()
                        focus_mask "images/gui/buttons_loc/underlay.webp"
                        xalign 0.5
                        action [TooltipClearUI(), Hide("HamunFindKhazahRivals"), Jump("qst_BigTroubleLHamun_marbella_khazah_hunt_rivals_btn")]


label qst_BigTroubleLHamun_marbella_khazah_hunt_rivals_btn:
    MC "(I can scout the streets to try and find the rival gangs.)"
    menu:
        "DEBUG: auto-complete" (AppearIf = config.developer):
            $ GoalComplete(QstBigTroubleLH, 1020)
            $ GoalShow(QstBigTroubleLH, 1030)
            $ QstBigTroubleLH().Gang_SlainRivalGangs = 3
            $ LocEnterQ()
        "{image=[ICON.CLOCK]} Look for rival gangs":
            scene black with dissolve
            $ TimeAdvBy(TIME_2H)
            jump qst_BigTroubleLHamun_marbella_khazah_hunt_rivals_try
        "Move on":
            show screen HamunFindKhazahRivals()
            $ LocEnterQ()
#########################################################################################################################################################
# Gang whore route - 3 - Hamun map (EXT)
# Much like the dark knight quest, an icon appears at night that is clickable '0/3 gangs slain'
# Fail variant
label qst_BigTroubleLHamun_marbella_khazah_hunt_rivals_try:
    if RngInt(1, 2) == 1:
        # to 1
        if QstBigTroubleLH().Gang_SlainRivalGangs == 0:
            $ LocFlush()
            with dissolve
            show cg_bandit at cleft
            show mc at cright_f
            "Making my way down one of the many alleyways, a group of men surrounded me."
            GANG_MEMBER "Heard you were looking for us."
            GANG_MEMBER "Take it those Khazah fools sent you to kill us?"
            menu:
                "Leave the city before I skin you all alive." (Req_Perk = "terrifying"):
                    GANG_MEMBER "... Fuck me, you really mean it, don't you?"
                    GANG_MEMBER "You're that damn monster from the arena!"
                    MC @angry "Will you leave, or not?"
                    GANG_MEMBER "We're going, we're going!"
                    GANG_MEMBER "Tell those fucks to leave us alone."
                "You should leave the city while you still can... The Khazah won't stop until you're all dead if you stay." (Req_Charm = 19):
                    GANG_MEMBER "... Fuck."
                    GANG_MEMBER "Alright, alright!"
                    GANG_MEMBER "This bit of turf isn't worth losing our lives over."
                    GANG_MEMBER "Tell the Khazah it's theirs, damn it."
                "I don't suppose I can talk you out of what you're about to try and do?":
                    GANG_MEMBER "Nope!"
                    MC @angry "Let's make this quick. I've got more of you fools to kill."
                    GANG_MEMBER "BOYS!"
                    $ AutoMus(False)
                    $ PlayMusicRandom("mus_battle_generic")
                    $ StartBattle(BattleData("pbat_hamun_street_night", CharIDList_Right = [{"e_bandit":9}, {"e_bandit":9}, {"e_bandit":9}]))
                    $ LocFlush(dissolve)
                    "I severed the head of the last one, watching it roll across the sand as his body slumped to the ground with a loud thud."
                    $ AutoMus(True)
                    MC @talk "Hmph..."
            $ QstBigTroubleLH().Gang_SlainRivalGangs += 1
            MC "(One down, two to go.)"
            show screen NovarasPatrolScreen()
            $ LocEnter()
        # to 2
        elif QstBigTroubleLH().Gang_SlainRivalGangs == 1:
            $ LocFlush()
            with dissolve
            show cg_raider at cleft
            show mc at cright_f
            "While wandering the same wretched alleyways, a shrouded figure approached me."
            GANG_MEMBER "Ahh, the Khazah's newest bitch, I see."
            GANG_MEMBER "Sent here to kill us, right?"
            MC @talk "Is there a reason you're talking instead of just trying to kill me?"
            GANG_MEMBER "I'm waiting to hear one reason why we shouldn't..."
            menu:
                "Don't fight the Khazah. Join them." (Req_Barter = 18):
                    GANG_MEMBER "What?"
                    MC @talk "There are dozens of gangs like you out there."
                    MC @talk "How long do you think you can hold out against the merchant lords and rival gangs?"
                    MC @think "At least if you join the Khazah, you might stand a chance."
                    GANG_MEMBER "... You think they'd let us join?"
                    MC @talk "Right now, the Khazah are fresh blood in the city. They need more muscle."
                    MC @talk "Now is the best time to join them — not when they're big enough not to need you."
                    GANG_MEMBER "... Boys, come on. Let's go."
                    GANG_MEMBER "Let's see if those Khazah fucks are really open to the idea."
                "You can still walk away from this...":
                    GANG_MEMBER "And give up everything we've worked for?"
                    GANG_MEMBER "Fuck that!"
                    MC @angry "Hard way it is!"
                    $ AutoMus(False)
                    $ PlayMusicRandom("mus_battle_generic")
                    $ StartBattle(BattleData("pbat_hamun_street_night", CharIDList_Right = [{"e_bandit":10}, {"e_raider":10}, {"e_bandit":10}]))
                    $ LocFlush(dissolve)
                    "I split open the head of the last of them with my blade."
                    "He dropped to the sand as I sheathed it."
                    $ AutoMus(True)
            $ QstBigTroubleLH().Gang_SlainRivalGangs += 1
            MC "(Two down, one to go.)"
            show screen NovarasPatrolScreen()
            $ LocEnter()
        # to 3
        elif QstBigTroubleLH().Gang_SlainRivalGangs == 2:
            $ LocFlush()
            with dissolve
            show cg_bandit at cleft
            show mc at cright_f
            "Springing from the shadows, daggers ready, the gang's leader spoke in a husky voice."
            GANG_MEMBER "Coin or your life!"
            MC @smile "Well, you've made this next part easy."
            MC @smile "The Khazah send their regards..."
            GANG_MEMBER "FUCK! All of you! Kill this cunt!"
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData("pbat_hamun_street_night", CharIDList_Right = [{"e_bandit":11}, {"e_thug":11}, {"e_thug":11}]))
            $ LocFlush(dissolve)
            "My blade pierced the last one's chest."
            "He stumbled backward, gurgling as blood pooled through his clothes."
            "Shakily, he reached for the wound, staring in shock."
            "As he fell lifelessly to the ground, I sheathed my blade."
            $ AutoMus(True)
            $ QstBigTroubleLH().Gang_SlainRivalGangs += 1
            $ GoalComplete(QstBigTroubleLH, 1020)
            MC "(That should be all of them.)"
            MC "(Time to head back to the Khazah, I suppose.)"
            $ GoalShow(QstBigTroubleLH, 1030)
            $ LocEnter()
    else:
        $ LocFlush(dissolve)
        "I found no sign of the gangs the Khazah wanted dead."
        "Perhaps I'd have better luck next time..."
        show screen NovarasPatrolScreen()
        $ LocEnter()

############################################################################################################################################
#Gang whore route 4 - Khazah hideout 
#Player selects the Khazah leader
label qst_BigTroubleLHamun_marbella_khazah_rivals_report:
    KHAZAH_LEADER "Have you made any progress?"
    menu:
        "They're dealt with." (AppearIf = IsGoalVisible(QstBigTroubleLH, 1030)):
            pass
        "Not yet.":
            KHAZAH_LEADER "Hm. Return when the job is done."
            $ LocEnter()
    KHAZAH_LEADER "And just in time."
    KHAZAH_LEADER "Here, your pay."
    $ PlayerAddItem("gold", QstBigTroubleLH().Gang_DealWithRivalsPay)
    $ GoalComplete(QstBigTroubleLH, 1030)
    KHAZAH_LEADER "MARBELLA!"
    MARBELLA "I'M COMING, DAMN IT! GIVE ME A MOMENT!"
    $ CharSetClothes("marbella", "maid")
    show cg_bandit at blurin, cright_f with ease
    show marbella at cleft with easeinleft
    KHAZAH_LEADER "Marbella just came by to discuss the 'finer' details of her role."
    MARBELLA @angry "That's one word for sucking cock and serving drinks..."
    KHAZAH_LEADER "Your friend just risked his life so you could stay under the protection of the Khazah. Don't you think you should thank him — and us — properly?"
    "Marbella blinked, taken slightly aback at the request as her cheeks flushed red."
    MARBELLA @emb "N-Now?"
    MARBELLA @emb "You just want me to get on my knees and suck your cocks like that?"
    KHAZAH_LEADER "No. I want you to ask if we want it."
    KHAZAH_LEADER "Obedience is key to all things."
    MARBELLA @emb "but I-"
    KHAZAH_LEADER "If you expect the Khazah's protection, you must keep to your end of the deal."
    MARBELLA @angry "H-Hold on! M-Maybe we could talk this through!"
    MARBELLA @sad "Uhh, how about an extra five percent instead? Or..."
    KHAZAH_LEADER "Perhaps we should simply call off the deal."
    MARBELLA @shock "WAIT! Wait! Wait!"
    MARBELLA @sad "L-Let's not be hasty now!"
    KHAZAH_LEADER "... I am waiting."
    MARBELLA @emb "{i}*Deep breathe*{/i}"
    MARBELLA @emb "... Do... do you want me to suck your cocks?"
    KHAZAH_LEADER "Is that how we speak to friends of the Khazah?"
    MARBELLA "May I suck your cock... Sir."
    KHAZAH_LEADER "Much better."

    KHAZAH_LEADER "So, how about it, friend?"
    menu:
        "*Pull out your cock for Marbella*":
            label replay_marbella_gang_bj_first:
            $ AutoMus(False)
            $ AutoAmb(False)
            stop ambience fadeout 0.5
            $ PlayMusicRandom("mus_sex")
            MC "Why not?"
            $ PlaySoundRandom("tentFlap")
            "Marbella's eyes widened as she stared at the cock hanging in front of her."
            MARBELLA "Gods... You're hung like a fuckin' horse."
            KHAZAH_LEADER "Marbella... We are waiting."
            MARBELLA "R-Right..."
            scene marbella_gang_bj_nopreg_1 with dissolve
            $ Pause()
            "Dropping to her knees, a nervous Marbella glanced between the two hard cocks in front of her."
            MARBELLA "D-Do I just... umm..."
            MARBELLA "Start."
            KHAZAH_LEADER "Stroke one while you suck the other."
            KHAZAH_LEADER "Then switch until both men are finished, girl."
            MARBELLA "{i}*Sigh*{/i}"
            MARBELLA "(I hope those idiots appreciate what I'm willing to do to keep them safe.)"
            $ PlaySexFx(audio.ves69_100, 1)
            scene marbella_gang_bj_nopreg_2 with dissolve
            $ Pause()
            "Cautiously, Marbella leaned forward, wrapping her soft lips around my cock as she stroked the Khazah leader."
            "I groaned as her tongue worked against the head."
            MC "Ahhh... Mfghh!"
            MARBELLA "{i}*Slurp... Slurp*{/i}"
            "Her mouth inched forward, taking more as she sucked."
            MARBELLA "Mmfghh..."
            MARBELLA "Yhourhh rheallhy bhighh! {i}*Slurp!*{/i}"
            "I smirked at the comment, her mouth still working."
            KHAZAH_LEADER "Over here, girl."
            KHAZAH_LEADER "Before I get lonely."
            $ PlaySexFx(audio.ves69_100, 1)
            scene marbella_gang_bj_nopreg_3 with dissolve
            $ Pause()
            "Marbella pulled away with a soft *plop* before wrapping her lips around the Khazah's cock."
            "He groaned as she moved her head back and forth."
            KHAZAH_LEADER "Faster... Take if faster!"
            KHAZAH_LEADER "Urghhh...!"
            "Marbella did as she was asked as the man grunted in approval of her 'skills.'"
            $ PlaySexFx(audio.ves69_150, 1)
            scene marbella_gang_bj_nopreg_5 with dissolve
            $ Pause()
            KHAZAH_LEADER "Ahhh! That's it, girl!"
            KHAZAH_LEADER "You know how to pleasure cock."
            KHAZAH_LEADER "I'm sure the other Khazah are going to love you, heh..."
            $ PlaySexFx(audio.ves69_150, 1)
            scene marbella_gang_bj_nopreg_4 with dissolve
            $ Pause()
            "After a few moments, she pulled away again,"
            "pressing her lips back onto me as her pace quickened."
            "As she stroked the other faster, her eyes lifted toward me."
            "There was a shy, desperate need for approval as she continued,"
            "and every soft moan I gave only encouraged her further."
            MARBELLA "(Oh gods, I can't believe I'm actually doing this!)"
            MARBELLA "(Fuck... I feel like some kind of bloody whore doing this!)"
            MARBELLA "(I guess I kinda am now, aren't I?)"
            MARBELLA "(... Well shit, at least I'm finally getting some for a change!)"
            MARBELLA "(Mmmfghh... This could...)"
            MC "Ahh! Marbella!"
            MC "I'm getting close!"
            MARBELLA "(G-Get a little addictive!)"
            KHAZAH_LEADER "Ahh! Me too!"
            KHAZAH_LEADER "Come on!"
            "Marbella pulled away, stroking both eagerly."
            MARBELLA "Come on, come on!"
            $ PlaySexFx(audio.kiara_bj_finish)
            scene marbella_gang_bj_nopreg_finish with flash
            $ UnlockGalSceneAndGrantXp("marbella", "gang_bj")
            $ ReduceInfectionFromSex("marbella")
            $ Pause()
            "I finished first, shortly followed by the Khazah."
            "Marbella gasped slightly in surprise,"
            "then her mouth curved into a sheepish smile as her cheeks burned red."
            MARBELLA "I'm, uhhh... better at this than I thought!"
            KHAZAH_LEADER "You were built for this, little dwarf."
            MARBELLA "Call me little and dwarf in the same sentence again, and next time I'll bite it off."
            KHAZAH_LEADER "Uhhh... Queen?"
            MARBELLA "Much fuckin' better."
            $ StopReplay()
            scene black with dissolve
            $ AutoMus(True)
            $ AutoAmb(True)
            "I pulled away as Marbella wiped herself clean with a rag."
            $ LocSet("hamun_khazah_hideout")
            $ LocFlush(dissolve)
            show marbella at left
            show cg_bandit at center
            show mc at right_f
            KHAZAH_LEADER "Nicely done, girl."
            KHAZAH_LEADER "Now go fetch the boys some drinks."
            hide marbella
            show cg_marbella_back_maid at left_f 
            $ PlaySound("audio/cfx/spank.ogg")
            "Marbella grumbled under her breath as she did as she was told."
            "Each man she walked past taking a swip at her ass."
            hide cg_marbella_back_maid with easeoutleft
            "It jiggled with each impact, quickly turning pink."
            $ PlaySound("audio/cfx/spank.ogg")
            MARBELLA "OI! Fuckin' cut it out! The lot of you!"
            "The men laughed and cheered."
            $ LocFlush()
            show cg_bandit at center
            with dissolve
        "Perhaps another time.":
            KHAZAH_LEADER "Not your type, perhaps?"
            KHAZAH_LEADER "Very well. Marbella, serve the others some drinks."
            hide marbella with dissolve
            "With a huff, Marbella turned and headed toward the bar."
            show cg_bandit at blurin, center with ease

    $ QstComplete(QstBigTroubleLH)
    KHAZAH_LEADER "Now then, there is one more matter of business I'd like to discuss."
    MC @think "Which is?"
    KHAZAH_LEADER "There are... strange reports of something killing our men in the night."
    MC @talk "You think Lord Zanzibat hired someone else?"
    KHAZAH_LEADER "Perhaps, but..."
    KHAZAH_LEADER "The bodies we've found have bites and claw marks, like an animal's."
    KHAZAH_LEADER "We've found other bodies too, so whatever is doing this isn't targeting only us."
    KHAZAH_LEADER "Either way, I want the thing gone."
    MC @serious "And why would I help you?"
    MC @serious "I don't work for the Khazah."
    KHAZAH_LEADER "True..."
    KHAZAH_LEADER "Should you do it, I would reward you handsomely as a friend of the Khazah."
    MC @think "How so?"
    KHAZAH_LEADER "Supplies."
    KHAZAH_LEADER "Coin, medicine, food... I could have a package prepared for you."
    KHAZAH_LEADER "Adventurers are never short on such things."
    KHAZAH_LEADER "Well... No need to decide now."
    KHAZAH_LEADER "If you kill whatever that thing is, I will reward you all the same."
    $ NoteUnlock("marbella_gang_hunt_face")
    MC @talk "I shall think on it."
    MC "(Those supplies could be useful... Maybe I should look into it.)"
    $ CharSetClothes("marbella", "normal")
    $ LocEnter()

###########################################################################################################################################
# next the face section happens
# after the face, the player returns to the Khazah hideout. 
label qst_BigTroubleLHamun_marbella_khazah_rivals_talk_about_face:
    KHAZAH_LEADER "Did you deal with whatever was attacking my men?"
    menu:
        "It won't be a problem anymore." (AppearIf = (QstGetProgress(RomanceMarbella) == 1)):
            KHAZAH_LEADER "This is wonderful news!"
            $ QstSetProgress(RomanceMarbella, 1000)
            $ DialogueHamunKhazahLeader()
            $ NoteLock("marbella_gang_report_face")
            $ NoteUnlock("marbella_gang_package_reminder")
            KHAZAH_LEADER "For your services, I shall have a supply box prepared for you every two weeks."
            KHAZAH_LEADER "Also... Feel free to use Marbella whenever you wish."
            KHAZAH_LEADER "You are a friend of the Khazah now."
            KHAZAH_LEADER "Come to us if you need help."
        "Not yet.":
            KHAZAH_LEADER "Hmm... Whatever it is, it continues to trouble us."
            return
