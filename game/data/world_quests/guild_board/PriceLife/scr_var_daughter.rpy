label qst_guild_price_life_daughter_start:
    scene black with dissolve
    $ LocNameSetTemp(_("Novaras Outskirts"))
    "Following the instructions left by both the Merchant and the marauders ransom note, I headed East towards the forests."
    $ TimeAdvTo(TIME_VISUAL_DAWN)
    $ AutoMus(False)
    $ PlayMusic("audio/music/3_Novaras_L.ogg")
    "Deep into the woods after several hours of travel, I stumbled into the marauders camp, where the Merchants daughter, a feline looking humanoid, was held captive in a cage."
    scene bg_forest
    show cg_callie_cage at right_f
    show cg_raider at center_f
    with dissolve
    show mc at left with easeinleft
    MARAUDER_LEADER "About time one of you showed up."
    MARAUDER_LEADER "You here for the girl then?"
    MC @talk "I am. Is she unharmed?"
    MARAUDER_LEADER "Ask her yourself."
    "The marauder turned back towards the girl trapped in her cage."
    show cg_raider at blurin, center
    MARAUDER_LEADER "OI! YOU'RE FINE AREN'T YOU GIRL?"
    "The katai growled from her cage."
    CALLIE "Release me now! Or else my father will-"
    MARAUDER_LEADER "SHUT IT CUNT!"
    show cg_raider at blurin, center_f
    MARAUDER_LEADER "... See? She's fine, mouthy as ever ... Now, onto business then."
    MARAUDER_LEADER "Did you bring the coin?"
    MC @talk "I did."
    'The Marauder leader smiled.'
    MARAUDER_LEADER "Well then, this is just perfect."
    MARAUDER_LEADER "What's to stop me just killing you, keeping the ransom coin for ourselves and selling this little slut off as a slave?"
    MARAUDER_LEADER "We outnumber you three to one."
    menu:
        "You can try to kill me, but then you'll just be hunted down like dogs by whoever is sent next.":
            MARAUDER_LEADER "HA! I'll take my chances!"
            MARAUDER_LEADER "Now drop the sword."
            "The leader whistled and pointed at one of the men, who moved to place a blade towards the girl in the cage."
            CALLIE "P-PLEASE DON'T KILL ME!"
            MC @angry "(Fuck.)"
            MC @angry "(I can't just drop my blade, but if I don't, they'll just kill the girl!)"
            MARAUDER_LEADER "What are you waiting for, boy?"
            MARAUDER_LEADER "DROP IT!"
            MC @angry "(Fuck, I can't believe I'm going to do this!)"
        "{i}This. (Transform){/i}":
            pass
    play sound2 "audio/cfx/transform.ogg"
    scene black with flash
    $ AutoMus(False)
    $ PlayMusic("audio/music/15_Experiments.ogg")
    'Stepping a few feet away from the Marauders, their eyes widened in horror as I tore at my own flesh, revealing the monstrous form beneath.'
    scene bg_forest
    show mc_transformed at left
    show cg_raider at cright_f
    show cg_callie_cage at right_f
    with dissolve
    MARAUDER_LEADER "WHAT THE FUCK?!"
    MC '{b}Would you like to resume negotiations?{/b}'
    "The fumbling leader of the marauders mumbled yes as he stared up and down horrified at the creature before him."
    menu:
        "My terms are you hand over the girl before I cut you all fucking down.":
            jump qst_guild_price_life_daughter_threaten

        "The Merchant is willing to offer half your asking price for the return of his daughter.":
            jump qst_guild_price_life_daughter_negotiate

label qst_guild_price_life_daughter_threaten:
    MARAUDER_LEADER "... Fuck off!"
    MARAUDER_LEADER "You think we're just going to walk away from here with nothing after risking our necks?!"
    menu:
        "{image=[ICON.SWORDS]} I will enjoy feasting on your carcasses.":
            MARAUDER_LEADER "What? F-fuck..."
            jump qst_guild_price_life_daughter_done_talking

        "Live and fight another day, or throw your life away trying to fight me here and now ... choose." (Req_Charm = renpy.random.randint(6, 8)):
            MARAUDER_LEADER "...Boys, let's uh ... Let's go."
            'There was some grumbling from the rest of the marauders, but none of them dared to speak up.'
            MC 'Release the girl ... {i}Now.{/i}'
            "Letting the Merchant's daughter out of the cage, she sheepishly hurried to hide behind me."
            MC '... Now leave.'
            jump qst_guild_price_life_daughter_kidnappers_leave

label qst_guild_price_life_daughter_negotiate:
    MARAUDER_LEADER "... Is this a fucking joke?"
    show cg_raider at shake
    MARAUDER_LEADER "Half? {i}Fucking half!{/i}"
    MARAUDER_LEADER "Piss off! I'm better off trying to sell her to the Greater trading company!"
    menu:
        "Even with half the asking price, the deal is still worth more than selling her to the greater trading company." (Req_Charm = renpy.random.randint(7, 9)):
            MARAUDER_LEADER "Hmm ... I suppose after all the trouble she's caused, the sooner I get her out of my hands, the better."
            MARAUDER_LEADER "Fine, give us the coin and she's yours."
            menu:
                "Here.":
                    $ PlayerRemItem("qst_ransom_money")
                    'Throwing over the bags filled with coin, the gang grinned as they inspected the coins inside, nodding with approval to their leader that it was all there.'
                    MARAUDER_LEADER "Pleasure doing business with you."
                    jump qst_guild_price_life_daughter_kidnappers_leave

                "{image=[ICON.SWORDS]} On second thought, fuck off, it's mine.":
                    MARAUDER_LEADER "We had a fucking deal!"
                    MC "And I'm changing it."
                    MARAUDER_LEADER "Aw! Fuck this!"
                    jump qst_guild_price_life_daughter_done_talking

        "I will pay the other half for the girl's release myself." (Req_Gold = 500):
            jump qst_guild_price_life_daughter_offer_own_money

        "{image=[ICON.SWORDS]} On second thought, I'll just gut you lot.":
            MARAUDER_LEADER "Aw! Fuck this!"
            jump qst_guild_price_life_daughter_done_talking

label qst_guild_price_life_daughter_offer_own_money:
    MARAUDER_LEADER "Heh heh! Glad to see you've come to your senses!"
    MC 'Release the girl, and the coin is yours.'
    'Grinning, the marauder whistled as the cage was opened, and the girl sheepishly scurried out to hide behind me.'
    MARAUDER_LEADER "Now, hand over the coin."
    menu:
        "Here." (Req_Gold = 500):
            $ PlayerRemItem("gold", 500)
            $ PlayerRemItem("qst_ransom_money")
            'Throwing over the bags filled with coin, the gang grinned as they inspected the coins inside, nodding with approval to their leader that it was all there.'
            MARAUDER_LEADER "Pleasure doing business with you."
            jump qst_guild_price_life_daughter_kidnappers_leave

        "{image=[ICON.SWORDS]} On second thought, fuck off, it's mine.":
            MARAUDER_LEADER "We had a fucking deal!"
            MC "And I'm changing it."
            MARAUDER_LEADER "Aw! Fuck this!"
            jump qst_guild_price_life_daughter_done_talking

label qst_guild_price_life_daughter_kidnappers_leave:
    scene black with dissolve
    'The kidnappers said nothing else, moving quickly to pack up what they could before hurrying off in the opposite direction.'
    scene bg_forest
    show mc_transformed at cleft
    show callie at cright_f
    with dissolve
    MC 'Are you okay?'
    'The katai blushed, nodding as she stared me up and down.'
    MC "If you tell anyone what you've seen-"
    CALLIE @sad "I won't! I WON'T!"
    CALLIE @sad "I promise!"
    "I sighed, having the briefest dark thought about killing the girl to keep my secret, but..."
    "{i}No, I couldn't.{/i}"
    "Morality aside, the last thing I needed was some merchant lord investigating his daughter's death and raising hell on the matter."
    "{i}Even more eyes on all this was the last thing I needed.{/i}"
    CALLIE @sad "... I... I presume father sent you then?"
    CALLIE "My name is Callie."
    $ CharMeet("callie")
    CALLIE " {i}... What are you?{/i}"
    MC "That doesn't matter, what matters is we get you home."
    'Callie nodded.'
    CALLIE "Yes, I think I've had quite enough 'adventure' recently."
    CALLIE "Getting home would be good."
    CALLIE "Lead the way."
    jump qst_guild_price_life_daughter_rescued

label qst_guild_price_life_daughter_done_talking:
    $ PlayerRemItem("qst_ransom_money")
    $ PlayerAddItem("gold", 500)
    MARAUDER_LEADER "BOYS! DRAW YOUR BLADES!"
    MARAUDER_LEADER "Looks like we're done talking!"
    MARAUDER_LEADER "Kill it! Fucking kill it now!"

    $ TransformMC(True)
    $ TransformMarkus(True)

    $ PlayMusicRandom("mus_battle_generic")

    $ StartBattle(BattleData("pbat_forest", CharIDList_Right = [{"e_raider":1}, {"e_bandit":2}, "e_thug", "e_bandit"]))

    $ TransformMC(False)
    $ TransformMarkus(False)

    "With the last of Marauders dead at my feet, their leader's skull crushed into a bloody pulp beneath my feet, I unlocked the cage of the katai and let her out."    
    
    scene bg_forest
    show mc_transformed at left
    show callie at right_f
    with dissolve
    "The girl's cheeks blushed red as she stared up at me not in horror but ... awe?"
    $ PlayMusic("audio/music/3_Novaras_L.ogg")
    MC 'I am here to rescue you, you have nothing to fear.'
    CALLIE "I guessed that one already by you negotiating my release."
    'I looked around at the piles of dead surrounding us.'
    MC "Apologies about the bloodbath, I-"
    CALLIE "Oh! Don't apologize!"
    CALLIE "I wish every day was this exciting!"
    'The curious Katai fluttered her eyes towards me.'
    MC "Uhh. I-"
    CALLIE "My name is Callie."
    $ CharMeet("callie")
    CALLIE " {i}... What are you?{/i}"
    MC "That doesn't matter, what matters is we get you home."
    CALLIE "A-Ah, I suppose getting home would be good."
    CALLIE "I think I've had quite enough 'excitement' recently ..."
    jump qst_guild_price_life_daughter_rescued

# at this point, all above variants converge
label qst_guild_price_life_daughter_rescued:
    scene black with dissolve
    'We traveled back along the path for some time.'
    scene bg_forest
    show mc at left
    show callie at right_f
    with dissolve
    CALLIE "Thank you for the rescue earlier."
    'Callie paused as she seemed to be pondering my name, realizing she never asked.'
    MC "...[player_name!t]."
    MC "And you have nothing to thank."
    MC "...Though if you could not tell anyone about what you saw back there when I changed-"
    CALLIE "Haha, don't worry about that ... Our kind have to stick together."
    MC "{i}'Our kind?'{/i}"
    CALLIE "Anyone not human, of course."
    CALLIE "They do know well how to make you feel second-class."
    'I thought for a moment about protesting against being called not human, but I decided it was best to avoid the conversation altogether and change the subject instead.'
    MC "I must admit, {i}I'm surprised{/i} you're ... Well ..."
    CALLIE "A katai?"
    MC "Yes."
    MC "Novaras isn't exactly known for its tolerance these days."
    CALLIE "Then it's a good thing I'm not from Novaras, isn't it?"
    MC "Oh?"
    CALLIE "My family lives in the free city of Hamun."
    MC "That so?"
    MC "Are there many of your kind there?"
    CALLIE "Not many, at least, compared to somewhere like Ramon."
    CALLIE "But Hamun tolerates us enough to get by."
    MC 'I see.'
    'The Katai girl continued to watch me throughout the travel, whenever our eyes met, she would flutter her eyes and smile.'
    MC 'Is there a reason you keep looking at me?'
    CALLIE "Why do you think?"
    MC "Your father paid me to-"
    CALLIE "Fuck my father, he's not here."
    MC "You're very forward, aren't you?"
    CALLIE "Am I not your type?"
    menu:
        "On the contrary ... I haven't been able to take my eyes off you either.":
            $ QstGuildPriceLife().sex_scene = True
            'Callie bit at her lower lip.'
            CALLIE "Good to know ... my rescuer."
        'I prefer to keep things professional.':
            CALLIE "Hmph ... Shame."
            'We continued on along the journey mostly in silence.'
    scene black with dissolve
    $ PlayMusic("audio/music/7_Novaras_D.ogg")
    $ TimeAdvTo(TIME_DAY_END)
    scene bg_inn_exterior_night with dissolve
    "Afterwards, darkness began to descend during our travels back, so we stopped our way into one of the many fortress inns now along the path home."
    "This one, according to the guild, was booked accordingly in agreement with the Merchant for rest during the trek back."
    $ LocNameSetTemp(_("Inn Bedroom"))
    scene bg_inn_room_night
    show mc at left
    show callie at right_f
    with dissolve
    MC "Your father only booked one room it seems."
    MC "He really didn't want to spend anymore than he had to, did he?"
    CALLIE @talk "Father is a tight prick who probably negotiated the guild to give him a discount before sending you."
    CALLIE @angry "I'm hardly surprised he'd avoid paying for two rooms."
    MC @talk "Ah, that sounds like a difficult relationship."
    CALLIE @talk "It's no matter."
    if QstGuildPriceLife().sex_scene:
        jump qst_guild_price_life_daughter_sex_offer
    else:
        scene black with dissolve
        call center_text(_("Next morning...")) from _call_center_text_1
        jump qst_guild_price_life_daughter_ending

label qst_guild_price_life_daughter_sex_offer:
    CALLIE @talk "Father's lack of attention tends to allow me a little more 'freedom' than most ..."
    MC @talk "Is that so?"
    CALLIE @happy "Oh yes, especially if the other person can keep a secret."
    CALLIE @blush "Can {i}you{/i} keep a secret?"
    menu:
        "Oh, I can keep a secret.":
            "Callie bit at her lower lip in excitement."
            CALLIE "...Wait here."
            CALLIE "There's something I need to get."
            MC @smile "Take your time."
            hide callie with easeoutright
            'Callie hurried off, and as she did so, I began to undress for the evening.'
            $ CharSetClothes("mc", "pants")
            show mc at blurin, cright_f with easeoutright
            'A short while later, there was a gentle knock at the door once again as Callie returned.'
            $ CharSetClothes("callie", "ling")
            show callie at cleft with easeinleft
            CALLIE @blush "Hello ..."
            $ PlayMusicRandom("mus_sex")
            CALLIE @blush "I heard that I was just your type."
            CALLIE @blush "How convenient, because you're definitely mine."
            scene black with dissolve
            $ CharSetClothes("mc", "normal")
            $ CharSetClothes("callie", "normal")
            'Grabbing a hold of Callie by the shoulders, she let out a little gasp as I threw her onto the bed, stripping off the last of my clothes.'
            CALLIE "So eager!"
            CALLIE @blush "Oh fuck ... Your {i}sword{/i} is certainly something!"
            CALLIE @blush "{i}How will we ever make it fit?{/i}"
            MC @smile "With lots of patience and lubricant."
            'Callie giggled playfully to my remark as I reached around to grab the back of her head.'
            scene callie_bj_ling_1 with dissolve
            $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
            $ Pause()
            'As I pulled her forward towards me, her mouth opened up as she willingly wrapped her lips around my cock.'
            'Her head bobbed back and forth keenly as her tongue thrashed and beat against my cock.'
            CALLIE "{i}*Slurp!*{/i} Mhmmfff!"
            'With a fistful of her hair, I continued to pull her forward to service me.'
            MC "Ahh! That's it ... Mmmfghh!"
            MC "Quite the good little cock-sucker, aren't you?"
            CALLIE  "Mhhfghh! {i}*Slurp!*{/i} Yheshh! Mmm!"
            CALLIE "Mh-Mhoree! Mmffhh! {i}*Slurp!*{/i}"
            'Callie continued to lovingly run her tongue along my cock as her wet mouth slid back and forth, lovingly coating my member in her warm saliva.'
            'I moved faster, thrusting deeper down into her throat as Callie began to let out little flustered choking sounds, struggling to take the length of my cock.'
            'Her muffled moans grew louder as he continued her wet sloppy blowjob, grunting as she threw her head forward, doing her best to take as much of my cock as deeply as she could.'
            'After some time, I finally began to feel my balls tighten as the tight, warm little mouth worked me with such keen delight.'
            'Her bright eyes looked up to me almost shimmering as her cheeks blushed with my cock stuffed into her mouth.'
            'There was a desperation to her face, a keen loving tenderness to {i}know{/i} I was pleased.'
            MC "{i}*Huff*{/i} That's it ... Urghhff! I'm getting close you little slut!"
            scene callie_bj_ling_2 with dissolve
            $ Pause()
            CALLIE "{i}*Slurp!* *Slurp!*{/i} Mmmfhh! Chummm inhhmee!!"
            MC 'A-Ahhhff! Fuck it!'
            MC 'Take it then you little sluttt!!' 
            "Unable to hold back any longer, I yanked Callie's head forward, flooding her mouth with a heavy, hot load." #Blowjob animation ends
            "Her eyes widened as she squealed feeling the warm seed pour into her mouth, but quickly, she did her best to swallow down every drop."
            "Obediently, after tenderly sucking on the head for a few more moments, with a loud *PLOP* she pulled back to show me an empty mouth."
            MC "{i}*Huff*{/i}, good little slut."
            MC "Now stick out that fat butt of yours, time to fill you up."
            'Callie giggled at the comment.'
            CALLIE "Yes sir ..."
            $ StopSexFx()
            scene callie_doggy_prepen with dissolve
            $ Pause()
            'Removing the rest of her barely present clothes, Callie bent over with her round, soft ass arched out towards me.'
            'She smiled as she looked over her shoulder and waited for me.'
            CALLIE "I don't normally do this, but-"
            CALLIE "{i}Pick whatever hole you'd like.{/i}"
            menu:
                'Put it in her ass.':
                    'I pressed the hilt of my wet cock against her tight hole.'
                    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
                    $ UnlockGalFlag("callie_trayan", "callie", "var_anal")
                    scene callie_doggy_anal_naked_1 with dissolve
                    $ Pause()
                    CALLIE "B-Be gentle, I've never had one as big as you ther-"
                    'I pressed the bulbous head of my cock against her tight backdoor, watching it spread around my cock as she squealed.' #Sex animation begins
                    CALLIE "AHH! F-FUCK! You're huge!"
                    CALLIE "H-Hrghh!"
                    MC "Fuck are you tight! Urghh!"
                    MC "Relax your ass a little slut!"
                    CALLIE "T-Trying!"
                    BLACK "(Allow me to assist.)"
                    'As the Dark Passenger whispered in my head, I suddenly felt something course out of my body and flood into Callie.'
                    CALLIE "W-What is-"
                    CALLIE "Ooooh! That f-feels so good!"
                    MC "(What did you do?)"
                    BLACK "(Just a little lubrication and aphrodisiac ... Good for intercourse.)"
                    BLACK "(Though I must warn you ... This hole is not capable of siring young.)"
                    MC "(Ah! No shit! I'm fucking them because its fun!)"
                    BLACK "( ... Interesting.)"
                    "Callie's tight ass squeezed me effortlessly as I stretched out their backdoor, listening out for her hot moans of pleasure and pain interwoven."
                    $ PlaySexFx("audio/sex_sounds/nijah_miss_2.ogg", 1)
                    scene callie_doggy_anal_naked_2 with dissolve
                    $ Pause()
                    "I was soon thrusting in and out of them with ease, the strange lube released allowed me to glide with ease through their tight backdoor,"
                    "And whatever pain Callie was experiencing now gave way to euphoric pleasure."
                    CALLIE "F-Fuck me! Mmmfghh! Its incredible!"
                    CALLIE "FUCK ME HARDER!"
                    CALLIE "FUCK MY ASS! PLEASE! Mmmfghh!"
                    CALLIE "{i}*Huff*{/i} It f-feels sooo good!"
                    "As they continued to throw their ass back onto me, the sounds of flesh slapping echoed throughout the room as the bed-frame continued to rock and hit against the wall."
                    "For some time, I continued to plow their back door, listening to their symphony of moans as their mind became flooded with pleasure."
                    "Finally, I began to feel my own climax draw near, and as I buried my cock tightly in their ass, I grunted and whispered in Callie's ear affectionately,"
                    MC "Where should I finish slut?"
                    CALLIE "Ah! Ah! W-Wherever you want!"
                    CALLIE "Gods! You can do whatever you fucking want to me! Mmff!"
                    CALLIE "I've never felt so good before!!"
                    'Unable to hold back any longer, I gritted my teeth, grunting loudly as I bottomed out inside of her ass.'
                    "Callie's eyes began to roll back in pleasure as she choked on air, shaking and trembling as she felt the rush of warm seed pouring into her."
                    scene callie_doggy_anal_finish with flash
                    
                'Put it in her pussy.':
                    "Pressing the head of my cock against Callie's wet slit, after some pressure, her body yielded as I forced a few inches into her."
                    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
                    $ UnlockGalFlag("callie_trayan", "callie", "var_vag")
                    scene callie_doggy_vag_naked_1 with dissolve
                    $ Pause()
                    CALLIE "{i}*Gasp!*{/i}"
                    CALLIE "Ahh! FUCK!"
                    "I held her there for a few moments, as Callie trembled, breathing heavily as she tried to calm herself down."
                    CALLIE "F-Fuck ... Do all the girls just need to lay down for a while when you're done?"
                    CALLIE "I'm not sure I'll be able to walk if-"
                    "I pressed my cock a few inches deeper, Callie's eyes widened as she gritted her teeth."
                    CALLIE "Oh fuck! Fuck! FUCK!"
                    "I began to move faster, Callie's tight womanhood became wetter with every teasing thrust."
                    CALLIE "Ooooh!"
                    CALLIE "M-Mmfgh! Fuck! F-Faster!"
                    CALLIE "Fuck me you big - {i}*Huff*{/i} dumb-"
                    CALLIE "A-Ahhh! So deep!"
                    MC "You're a real slut deep down, aren't you?"
                    CALLIE "Ahhh! Yes! It's true!"
                    CALLIE "Mmmfghh! I'm such a fucking slut!"
                    CALLIE "Fuck me like the little worthless slut I am!"
                    "Callie squeezed me tightly as I held onto her waist and fucked her furiously, watching as my cock slide in and out of her pussy to the sounds of guttural moans."
                    $ PlaySexFx("audio/sex_sounds/nijah_miss_2.ogg", 1)
                    scene callie_doggy_vag_naked_2 with dissolve
                    $ Pause()
                    MC "Ahh! {i}*Huff!*{/i} Callie!"
                    CALLIE "M-Mmffgh! Fuck! Fuck! FUCK!"
                    CALLIE "Don't you dare stop fucking me idiot!"
                    CALLIE "Give me that big fucking cock!"
                    CALLIE "{i}*Huff*{/i} It f-feels sooo good!"
                    "As they continued to throw their ass back onto me, the sounds of flesh slapping echoed throughout the room as the bed-frame continued to rock and hit against the wall."
                    "For some time, I continued to plow her tight womanhood, listening to their symphony of moans as their mind became flooded with pleasure."
                    "Finally, I began to feel my own climax draw near, and as I buried my cock to the hilt, I grunted and whispered in Callie's ear affectionately,"
                    MC "Where should I finish slut?"
                    CALLIE "Ah! Ah! W-Wherever you want!"
                    CALLIE "Gods! You can do whatever you fucking want to me! Mmff!"
                    CALLIE "I've never felt so good before!!"
                    'Unable to hold back any longer, I gritted my teeth, grunting loudly as I bottomed out inside of their tight cunt, unleashing a hot heavy loud into their welcoming womb.'
                    "Callie's eyes began to roll back in pleasure as she choked on air, shaking and trembling as she felt the rush of warm seed pouring into her."
                    scene callie_doggy_vag_finish with flash

            $ ReduceInfectionFromSex("callie")
            $ UnlockGalSceneAndGrantXp("callie_trayan", "callie")
            $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
            $ Pause()
            "Callie rolled over breathlessly beside me, breathing heavily as she laid in exhausted ecstasy."
            CALLIE "{i}*Huff*{/i} Mmmfhh! {i}*Huff*{/i} Hahaha!"
            'Callie began to drift in and out of consciousness and she spoke sleepily.'
            CALLIE "Don't tell ... Mmm ... Father- {i}*Yawn*{/i}"
            CALLIE "And you can be a different kind of {i}daddy{/i} to me {image=[ICON.HEART]}"
            "Before I could answer her, Callie's eyes fully closed as she drifted off to sleep with a happy, drooling expression on her face."
            $ CharAddRelEntry("callie", "had_sex")
            MC "( ... 'Daddy' huh?)"
        "I think you should get some rest...":
            "Callie's cat ears flopped down in disappointment."
            CALLIE "Urghh..."
            CALLIE "And here I thought you'd be entertaining."
            CALLIE "{i}*Sigh*{/i} Never mind."
    jump qst_guild_price_life_daughter_ending

label qst_guild_price_life_daughter_ending:
    $ AutoMus(True)
    scene black with dissolve
    $ TimeAdvTo(TIME_MORNING)
    "We returned to Novaras by dawn."
    "I delivered Callie back to her father's men safely, and was handed the coin for my services."
    if QstGuildPriceLife().sex_scene:
        "Before she left, Callie wrapped her arms around me in a hug and remarked that if I was ever visiting Hamun, I should ask for her..."
    $ QstComplete(QstGuildPriceLife)
    $ LocNameReset()
    $ LocSet("novaras_dist_market")
    $ LocEnter()