#####################################################################################################
######### valchek route ############
label qst_thecomingstorm_valchek_atmarket:
# Player goes to deal with Valchek - player heads over towards the market 
    # this auto-triggers in market district
    $ QstTheComingStorm().ValchekSawMarketEnterScene = True
    show mc at cright_f with easeinright
    MC "(Hmm... Carina said Valchek would be here.)"
    MC "(But where?)"
    MC "(Perhaps someone might be able to point me in the right direction.)"
    $ LocEnter()

#### new option with luciusmal:
label qst_thecomingstorm_valchek_atlucius_initial:
    $ QstTheComingStorm().ValchekMetLuciusOnce = True
    LUCIUSMAL @think "Valchek?"
    LUCIUSMAL @talk "I'd recommend you avoid that one."
    LUCIUSMAL @talk "He's been making quite a stir in this part of Novaras recently."
    MC @serious "Where might I find him?"
    LUCIUSMAL @talk "You won't."
    LUCIUSMAL @talk "Him and his men are probably holed up in some safehouse nearby."
    "The merchant chuckled."
    LUCIUSMAL @talk "He's practically in hiding, only comes out when he needs to."
    LUCIUSMAL @talk "Rumor has it, he's angered quite a few unscrupulous characters..."
    "The merchant's gaze turned back toward me."
    LUCIUSMAL @smile "Of course... I could arrange for him to meet you."
    LUCIUSMAL @smile "{i}For a price, of course.{/i}"
    $ GoalComplete(QstTheComingStorm, 250)
    LUCIUSMAL @smile "Say... three hundred coins?"
    menu qst_thecomingstorm_valchek_atlucius_initial_menu:
        "For such a valued customer as myself?" (Req_Barter = 9) if QstTheComingStorm().ValchekLuciusMalArrangeCost == 300:
            $ QstTheComingStorm().ValchekLuciusMalArrangeCost = 150
            LUCIUSMAL @think "Hmm... Well, you {i}are{/i} one of my most treasured customers!"
            LUCIUSMAL @smile "One-fifty, friend, and not a coin less!" 
            jump qst_thecomingstorm_valchek_atlucius_initial_menu

        "Here is your coin." (Req_Gold = QstTheComingStorm().ValchekLuciusMalArrangeCost):
            $ PlayerRemItem("gold", QstTheComingStorm().ValchekLuciusMalArrangeCost)
            LUCIUSMAL @smile "Wonderful, friend!"
            # only if it is a re-visit:
            if IsGoalVisible(QstTheComingStorm, 260):
                $ GoalComplete(QstTheComingStorm, 260)
            LUCIUSMAL @smile "Return here this evening... I shall see what can be done!"
            $ GoalShow(QstTheComingStorm, 270)
            LUCIUSMAL @sad "I must insist though, uhh..."
            LUCIUSMAL @angry "You don't make a mess of my store."
            LUCIUSMAL @angry "I agreed to arrange a meeting, {i}not{/i} a bloodbath."
            MC "(Well, that could be a problem.)"
            MC @angry "You better not cross me on this."
            MC @angry "I'm running out of time."
            LUCIUSMAL @smile "I'm an honest merchant, friend."
            LUCIUSMAL @smile "{i}A deal is always a deal.{/i}"
            BLACK "({i}Let us hope he remembers his own words.{/i})"
            MC @talk "Very well then."
            MC @talk "I'll be back..."
            $ LocEnter()

        "I don't have the coin.": 
            LUCIUSMAL @sad "What a shame..."
            LUCIUSMAL @smile "Well, you let me know when you do, and I'll arrange the meeting!"
            if not IsGoalVisible(QstTheComingStorm, 260):
                $ GoalShow(QstTheComingStorm, 260)
            $ LocEnter()

label qst_thecomingstorm_valchek_atlucius_repeat:
    LUCIUSMAL @talk "Of course, you pay - I set up the meeting."
    jump qst_thecomingstorm_valchek_atlucius_initial_menu

#####################################################################################################
# Returning to the merchant store after dark
label qst_thecomingstorm_valchek_return_to_store_after_dark_to_meet_valchek:
    play sound "audio/cfx/door_knock.ogg"
    "As I knocked on the closed merchant's door, a voice answered from the other side."
    LUCIUSMAL "We're closed!"
    MC @serious "It's me. Open up."
    scene black with dissolve
    "After a few moments, I heard the click of the bolt as the door opened, and I stepped inside the merchant's store."
    $ LocSet("novaras_store_int")
    $ LocFlush()
    with dissolve
    show mc at center_f with easeinright
    "As the door closed behind me, I suddenly felt something sharp press against my back."
    show valchek_hood at cright_f with dissolve
    "A group of masked men sat around the store, watching me closely."
    VALCHEK "So... I hear you've been looking for me."
    MC @serious "Valchek, I take it?"
    VALCHEK "I am."
    $ GoalComplete(QstTheComingStorm, 270)
    VALCHEK "Which one of them sent you? Umak?"
    MC @talk "Carina."
    VALCHEK "Ah, that would have been my second guess."
    VALCHEK "Well, I suppose she told you to kill me, right?"
    VALCHEK "So tell me... why shouldn't I just kill {i}you{/i} here and now?"
    menu:
        "{image=[ICON.SWORDS]} You can't kill me... You all are already dead.":
            show mc at cleft_f with ease
            $ Pause(0.1)
            show mc at blurin, cleft
            "Valchek's eyes darkened."
            VALCHEK "Is that so?"
            show valchek_hood at shake
            VALCHEK "Men! Your blades!"
            "As I reached for my weapon, I felt a sudden sharp impact."
            scene black with flash
            play sound "audio/cfx/door_crash.ogg"
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            "Valchek leapt forward, delivering a powerful kick to my chest that sent me crashing through the merchant's door."
            LUCIUSMAL "No no no! MY DOOOOR!"
            $ LocSet("novaras_dist_market")
            scene bg_alleyway_night
            show mc at cright_f
            with dissolve
            show valchek_hood at cleft with easeinleft
            show cg_bandit at left with easeinleft
            "Climbing back to my feet, I found Valchek and his men surrounding me, blades drawn."

            $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys_night", CharIDList_Right = [{"e_thug":7}, {"e_bandit":5}, "valchek"], CanTransform = False)) 

            "Slaughtered, Valchek's men lay in lifeless pools of their own blood."
            "Valchek, wounded and clutching a deep wound in his stomach, tried to crawl away."
            $ AutoMus(True)
            scene bg_alleyway_night
            show mc at cright_f
            show valchek_hood at cleft
            VALCHEK "F-Fuck... Fine."
            show valchek_hood at shake
            VALCHEK "I knew it would - {i}*Cough*{/i} end this way eventually."
            VALCHEK "Just thought I had more... {i}Ughh{/i}... Time..."
            show mc at center_f with ease
            VALCHEK "Make it quick, bas—"
            show mc at shake
            hide valchek_hood with dissolve
            "With a swift slash across his throat, Valchek's head hit the ground."
            "He gurgled, choking on his own blood, his body twitching before he finally fell still."
            show mc at blurin, center
            MC "(I'm sure news will spread to Carina quickly.)"
            MC "(I should head back to Carina.)"
            show mc at cright with ease
            $ GoalShow(QstTheComingStorm, 280)
            show luciusmal angry at left with easeinleft
            show luciusmal angry at shake
            LUCIUSMAL @angry "Damn you, man! We had a deal!"
            LUCIUSMAL @angry "Now people will think I set Valchek up!"
            show mc at blurin, cright_f
            MC @angry "I promised not to kill them inside your store."
            MC @angry "As you can see, they're dead {i}outside{/i} of it."
            show luciusmal angry at shake
            LUCIUSMAL @angry "Bah! To hells with you!"
            show luciusmal at blurin, left_f
            hide luciusmal with easeoutleft
            "The merchant stormed back inside his store, muttering curses under his breath."
            show mc at blurin, cright
            hide mc with easeoutright
            $ LocEnter()

        "Because I'll slaughter all of you before you stand a chance." (Req_Perk = "terrifying"):
            "Valchek's men exchanged nervous glances."
            "The room tensed, the air thick with hesitation."
            VALCHEK "... Good enough reasoning for me."
            VALCHEK "Then what do you want?"
            pass

        "Because I might be your only chance of survival." (Req_Charm = 12):
            VALCHEK "Hmph... Well, it's not like I have many other options, do I?"
            VALCHEK "What do you want from me?"
            pass

        "You're a wanted bandit... I could have come here with a dozen guards." (Req_Barter = 9): 
            VALCHEK "True."
            VALCHEK "And you haven't drawn your blade yet, so..."
            VALCHEK "What do you want from me?"
            pass
    
    show mc at cleft_f with ease
    $ Pause(0.1)
    show mc at blurin, cleft

    menu qst_thecomingstorm_valchek_spared_talk_menu_1: 
        "You've made a lot of enemies... Why haven't you left the city already?":
            VALCHEK "Ha... You really think they aren't waiting for me to try that?"
            VALCHEK "The minute I leave this city, I'll find myself hanging from a tree."
            VALCHEK "No... It's better to stay here. I know Novaras better than any of them."
            menu qst_thecomingstorm_valchek_spared_talk_menu_2:
                "So you plan to fight them?": 
                    VALCHEK "I don't have the manpower for a full-scale war."
                    VALCHEK "But I've got enough men to know where I can hit them where it hurts."
                    jump qst_thecomingstorm_valchek_spared_talk_menu_2
                "You can't hide forever. They're going to find you.":  
                    VALCHEK "Wanna bet?" 
                    jump qst_thecomingstorm_valchek_spared_talk_menu_1
        "Carina doesn't care if you're dead or not, but she wants you gone.":
            pass

    VALCHEK "And you believe that psycho whore?"
    VALCHEK "She had her own brother killed after she {i}forgave{/i} him for stealing from her."
    VALCHEK "You really think she'll forgive me for starting a turf war?"
    MC @talk "What if we faked your death?"
    VALCHEK "Ha! Fake my death?"
    VALCHEK "You think Carina's going to settle for anything less than my head on a table?"
    MC @talk "I needn't take your head, only enough to convince her you're gone."
    MC @serious "... And you leave the city, never giving her or anyone else cause to believe otherwise."
    VALCHEK "Hmm..."
    "Valchek pondered my proposal, his fingers tapping anxiously against the merchant's counter."
    VALCHEK "Alright, I'll humor you. What's your plan?"
    MC @think "What could you give me as proof to bring to her?"
    VALCHEK "Proof, hmm?"
    "Reaching up, Valchek pressed his fingers into his eye socket and pulled out a false, marble eye."
    "He tossed it toward me."
    show valchek_hood at nod
    $ PlayerAddItem("qst_valchek_eye")
    VALCHEK "That should more than suffice."
    VALCHEK "But now what?"
    "I glanced around the store, searching for inspiration."
    "Then, I saw it."
    MC @talk "We smuggle you out in one of the merchant's barrels."
    show luciusmal at left with easeinleft
    "The merchant, who had been silently observing, suddenly grinned."
    LUCIUSMAL @smile "Funny you should suggest such a thing!"
    "He stroked his facial hair mischievously."
    LUCIUSMAL @smile "Now, I've never smuggled someone {i}out{/i} of Novaras before, however..."
    VALCHEK "Have you been holding out on me!?"
    LUCIUSMAL @smile "Now, now! You simply never asked!"
    LUCIUSMAL @smile "And you've been such a loyal customer, well..."
    VALCHEK "I swear, if this is some foul trick—"
    LUCIUSMAL @talk "A large barrel of wine with a secret compartment at the bottom. Built to hold one adult."
    LUCIUSMAL @talk "Hardly comfortable, but it does the job."
    LUCIUSMAL @talk "If any nosy guard inspects the barrel, they'll just find regular wine and call it a day."
    LUCIUSMAL @talk "I'm willing to do all this..."
    LUCIUSMAL @smile "{i}For a price, of course.{/i}"
    VALCHEK "Name it."
    LUCIUSMAL @talk "Not a question of coin."
    LUCIUSMAL @smile "I simply ask for a favor."
    VALCHEK "This better not be one of your tricks..."
    LUCIUSMAL @talk "I've been eager to arrange a meeting with Lady Carina."
    LUCIUSMAL @talk "I have some... business to discuss with her."
    MC @think "Why not just ask her directly?"             
    LUCIUSMAL @smile "Oh no no no, you can't just meet with her unless you're {i}invited{/i} first!"
    LUCIUSMAL @talk "And that's all I ask..."
    MC @talk "If I speak to her... you'll help us."  
    LUCIUSMAL @smile "By the Merchant's Guild, I swear it."
    LUCIUSMAL @smile "Do we have a deal?"
    MC @talk "... Fine."
    $ GoalShow(QstTheComingStorm, 290)
    LUCIUSMAL @smile "Marvelous!"
    LUCIUSMAL @talk "Tell Lady Carina that Caskell of the Merchant's Guild asks for her!"
    "He offered a curt bow."
    LUCIUSMAL @talk "I eagerly await your answer!"
    hide mc with easeoutright
    scene black with dissolve
    $ LocSet("novaras_dist_market")
    $ LocEnter()

#####################################################################################################
# Returning to Lady Carina with news of Valchek's death
# New dialogue option appears: "Valchek is dead..."
label qst_thecomingstorm_valchek_report_death_conclusion:
    CARINA @talk "Yes, I did hear about that little spectacle in the streets."
    CARINA @talk "I would have preferred things were done a little more quietly, but..."
    CARINA @smile "What's done is done."
    $ GoalComplete(QstTheComingStorm, 280)
    MC @talk "I've fulfilled my end of the deal."
    CARINA @talk "And I shall fulfill mine."
    CARINA @smile "Give me a month."
    MC @angry "What?! I don't have time for—"
    CARINA @talk "And I need time to check my contacts."
    MC @angry "It'll already be too late by then!"
    "Carina paused, tilting her head slightly as she studied my expression carefully."
    CARINA @think "... Not that I care, but why are these men so important to you?"
    MC @talk "The Demorai are planning something... beyond just the siege itself."
    CARINA @think "And you know this because...?"
    MC @talk "It doesn't matter. Let's just say I have a reliable source."
    MC "(At least, I hope they are still a reliable source.)"
    CARINA @talk "Hmm..."
    CARINA @talk "Fine then, give me three days at least."
    CARINA @talk "Even I can't move faster than that."
    MC @talk "Very well, I'll return in three days."
    MC "(Perhaps there's something else I can do in the meanwhile?)"
    $ GoalShow(QstTheComingStorm, 300)
    $ QstSetDelay(QstTheComingStorm, 3)
    $ LocEnter()

#####################################################################################################
# Returning to Lady Carina to ask her to meet with the merchant
label qst_thecomingstorm_valchek_carina_ask_caskell:
    CARINA @angry "Urghhh... He's been trying to meet with me for weeks."
    CARINA @talk "Did he say what he wants?"
    MC @talk "Only that he wishes to speak with you."
    MC @talk "After which, I can deal with your Valchek problem."
    "Carina pondered the thought for a moment, taking another slow drag from her pipe before letting out a heavy sigh."
    CARINA @talk "Fi-ine."
    $ GoalComplete(QstTheComingStorm, 290)
    CARINA @talk "I'll send one of my men to invite him over."
    CARINA @talk "I shall listen to what he has to say."
    $ GoalShow(QstTheComingStorm, 291)
    $ LocEnter()

label qst_thecomingstorm_valchek_carina_report_caskell_day:
    LUCIUSMAL @talk "That is good news indeed!"
    LUCIUSMAL @talk "Come after dark, friend."
    LUCIUSMAL @talk "I will fulfill my part of the deal."
    return

#####################################################################################################
# Final confrontation with Valchek - shop interior
label qst_thecomingstorm_valchek_smuggle_away:
    scene black with dissolve
    $ LocSet("novaras_store_int")
    $ LocFlush()
    show luciusmal at left
    show valchek_hood at cleft
    show mc at cright_f
    with dissolve
    VALCHEK @talk "So... We're good then?"
    LUCIUSMAL @smile "We are indeed."
    $ GoalComplete(QstTheComingStorm, 291)
    LUCIUSMAL @talk "Everything is in order for you to leave and escape to the Free City."
    MC @talk "Better to live and rebuild than die in hiding."
    VALCHEK "Ha! You're the first hired sword I've ever heard say that."
    VALCHEK "{i}... But I am grateful.{/i}"
    show valchek_hood at center with ease
    "Stepping toward me, Valchek pulled back her hood and mask."
    hide valchek_hood
    $ PlaySoundRandom("tentFlap")
    show valchek at center
    with dissolve
    MC @surprised "Wait, you're a-"
    VALCHEK @smile "Woman?"
    MC @surprised "I thought..."
    VALCHEK @talk "It's easier to get by when they think you're a man in this life."
    VALCHEK @talk "Most of them think a woman's only good for spreading her legs and counting coin."
    BLACK "{i}(I admire her survival instincts... She would make a fine mate.{/i})"
    "Valchek stepped closer towards me, gently caressing my cheek, before sharply grabbing my hair and pulling me in for a kiss."
    # art?
    show valchek at nod
    MC "...!"
    VALCHEK @smile "A worthy reward, I hope."
    MC @smile "A surprise... But a welcome one."
    show valchek at cleft with ease
    LUCIUSMAL @smile "Not to interrupt the moment, but we have to move now if we're to get you out of this city in one piece."
    VALCHEK @talk "Lead the way."
    hide luciusmal with easeoutright
    show valchek at right with ease
    show mc at blurin, center with ease
    show valchek at blurin, right_f
    "Valchek turned one last time to look towards me before being ushered away by the merchant."
    VALCHEK @smile "I hope we meet again someday, [player_name!t]."
    VALCHEK @smile "I'll show you what a real woman can do..."
    show valchek at blurin, right
    hide valchek with easeoutright
    $ Pause(0.1)
    MC "(Well, with that sorted, I should return to Lady Carina to inform her of the news.)"
    $ GoalShow(QstTheComingStorm, 292)
    hide mc with easeoutright
    scene black with dissolve
    $ LocSet("novaras_dist_market")
    $ LocEnter()

###########################################################################################################################
# on ret to carina (smuggled away)
label qst_thecomingstorm_valchek_report_smuggled_conclusion:
    # New dialogue option appears: "Valchek is gone..."
    CARINA @talk "Mmm, I heard rumors that Valchek had all but vanished."
    CARINA @smile "... I suppose that was {i}your{/i} doing then?"
    MC @talk "I've fulfilled my end of the deal."
    CARINA @think "And your proof Valchek is really gone?"
    $ PlayerRemItem("qst_valchek_eye")
    "I rolled the {i}fake glass eye{/i} across the table for Carina to grab and inspect."
    CARINA @talk "... Very good."
    $ GoalComplete(QstTheComingStorm, 292)
    CARINA @talk "And now it's my turn to fulfill my end."
    CARINA @smile "Give me a month."
    MC @angry "What?! I don't have time for—"
    CARINA @talk "And I need time to check my contacts."
    MC @angry "It'll already be too late by then!"
    "Carina paused, tilting her head slightly as she studied my expression carefully."
    CARINA @think "... Not that I care, but why are these men so imperative to you?"
    MC @talk "The Demorai are planning something... beyond just the siege itself."
    CARINA @think "And you know this because...?"
    MC @talk "It doesn't matter. Let's just say I have a reliable source."
    MC "(At least, I hope they are {i}still{/i} a reliable source.)"
    CARINA @talk "Hmm..."
    CARINA @talk "Fine then, give me three days at least."
    CARINA @talk "Even I can't move faster than that."
    MC @talk "Very well, I'll return in three days."
    MC "(Perhaps there's something else I can do in the meanwhile?)"
    $ GoalShow(QstTheComingStorm, 300)
    $ QstSetDelay(QstTheComingStorm, 3)
    $ LocEnter()
