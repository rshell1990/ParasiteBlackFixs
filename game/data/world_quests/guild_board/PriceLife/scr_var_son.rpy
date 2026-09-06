label qst_guild_price_life_son_start:
    scene black with dissolve
    $ LocNameSetTemp(_("Novaras Outskirts"))
    "Following the instructions left by both the Merchant and the marauders ransom note, I headed East towards the forests."
    $ TimeAdvTo(TIME_VISUAL_DAWN)
    $ AutoMus(False)
    $ PlayMusic("audio/music/3_Novaras_L.ogg")
    "Deep into the woods after several hours of travel, I stumbled into the marauders camp, where the Merchants son, a feline looking humanoid, was held captive in a cage."
    scene bg_forest
    show cg_trayan_cage at right_f
    show cg_raider at center_f
    with dissolve
    show mc at left with easeinleft
    MARAUDER_LEADER "About time one of you showed up."
    MARAUDER_LEADER "You here for the boy then?"
    MC @talk "I am. Is he unharmed?"
    MARAUDER_LEADER "Ask him yourself."
    "The marauder turned back towards the boy trapped in his cage."
    show cg_raider at blurin, center
    MARAUDER_LEADER "OI! YOU'RE FINE AREN'T YOU BOY?"
    "The katai meekly nodded, but I noticed a few darkened bruises around his body."
    show cg_raider at blurin, center_f
    MARAUDER_LEADER "See? He's fine... Now, onto business then."
    MARAUDER_LEADER "Did you bring the coin?"
    MC @talk "I did."
    'The Marauder leader smiled.'
    MARAUDER_LEADER "Well then, this is just perfect."
    MARAUDER_LEADER "What's to stop me just killing you, keeping the ransom coin for ourselves and selling this little cunt off as a slave?"
    MARAUDER_LEADER "We outnumber you three to one."
    menu:
        "You can try to kill me, but then you'll just be hunted down like dogs by whoever is sent next.":
            MARAUDER_LEADER "HA! I'll take my chances!"
            MARAUDER_LEADER "Now drop the sword."
            "The leader whistled and pointed at one of the men, who moved to place a blade towards the boy in the cage."
            "He could only whimper and cry from his confinement, pleading for his life."
            MC @angry "(Fuck.)"
            MC @angry "(I can't just drop my blade, but if I don't, they'll just kill the boy!)"
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
    show cg_trayan_cage at right_f
    with dissolve
    MARAUDER_LEADER "WHAT THE FUCK?!"
    MC '{b}Would you like to resume negotiations?{/b}'
    "The fumbling leader of the marauders mumbled yes as he stared up and down horrified at the creature before him."
    menu:
        "My terms are you hand over the boy before I cut you all fucking down.":
            jump qst_guild_price_life_son_threaten

        "The Merchant is willing to offer half your asking price for the return of his son.":
            jump qst_guild_price_life_son_negotiate

label qst_guild_price_life_son_threaten:
    MARAUDER_LEADER "... Fuck off!"
    MARAUDER_LEADER "You think we're just going to walk away from here with nothing after risking our necks?!"
    menu:
        "{image=[ICON.SWORDS]} I will enjoy feasting on your carcasses.":
            MARAUDER_LEADER "What? F-fuck..."
            jump qst_guild_price_life_son_done_talking

        "Live and fight another day, or throw your life away trying to fight me here and now ... choose." (Req_Charm = renpy.random.randint(6, 8)):
            MARAUDER_LEADER "...Boys, let's uh ... Let's go."
            'There was some grumbling from the rest of the marauders, but none of them dared to speak up.'
            MC 'Release the boy ... {i}Now.{/i}'
            "Letting the Merchant's son out of the cage, he sheepishly hurried to hide behind me."
            MC '... Now leave.'
            jump qst_guild_price_life_son_kidnappers_leave

label qst_guild_price_life_son_negotiate:
    MARAUDER_LEADER "... Is this a fucking joke?"
    show cg_raider at shake
    MARAUDER_LEADER "Half? {i}Fucking half!{/i}"
    MARAUDER_LEADER "Piss off! I'm better off trying to sell him to the Greater trading company!"
    menu:
        "Even with half the asking price, the deal is still worth more than selling him to the greater trading company." (Req_Charm = renpy.random.randint(7, 9)):
            MARAUDER_LEADER "Hmm ... I suppose after all the trouble he's caused, the sooner I get him out of my hands, the better."
            MARAUDER_LEADER "Fine, give us the coin and he's yours."
            menu:
                "Here.":
                    $ PlayerRemItem("qst_ransom_money")
                    'Throwing over the bags filled with coin, the gang grinned as they inspected the coins inside, nodding with approval to their leader that it was all there.'
                    MARAUDER_LEADER "Pleasure doing business with you."
                    jump qst_guild_price_life_son_kidnappers_leave

                "{image=[ICON.SWORDS]} On second thought, fuck off, it's mine.":
                    MARAUDER_LEADER "We had a fucking deal!"
                    MC "And I'm changing it."
                    MARAUDER_LEADER "Aw! Fuck this!"
                    jump qst_guild_price_life_son_done_talking

        "I will pay the other half for the boy's release myself." (Req_Gold = 500):
            jump qst_guild_price_life_son_offer_own_money

        "{image=[ICON.SWORDS]} On second thought, I'll just gut you lot.":
            MARAUDER_LEADER "Aw! Fuck this!"
            jump qst_guild_price_life_son_done_talking

label qst_guild_price_life_son_offer_own_money:
    MARAUDER_LEADER "Heh heh! Glad to see you've come to your senses!"
    MC 'Release the boy, and the coin is yours.'
    'Grinning, the marauder whistled as the cage was opened, and the boy sheepishly scurried out to hide behind me.'
    MARAUDER_LEADER "Now, hand over the coin."
    menu:
        "Here." (Req_Gold = 500):
            $ PlayerRemItem("gold", 500)
            $ PlayerRemItem("qst_ransom_money")
            'Throwing over the bags filled with coin, the gang grinned as they inspected the coins inside, nodding with approval to their leader that it was all there.'
            MARAUDER_LEADER "Pleasure doing business with you."
            jump qst_guild_price_life_son_kidnappers_leave

        "{image=[ICON.SWORDS]} On second thought, fuck off, it's mine.":
            MARAUDER_LEADER "We had a fucking deal!"
            MC "And I'm changing it."
            MARAUDER_LEADER "Aw! Fuck this!"
            jump qst_guild_price_life_son_done_talking

label qst_guild_price_life_son_kidnappers_leave:
    scene black with dissolve
    'The kidnappers said nothing else, moving quickly to pack up what they could before hurrying off in the opposite direction.'
    scene bg_forest
    show mc_transformed at cleft
    show trayan at cright_f
    with dissolve
    MC 'Are you okay?'
    'The katai blushed, nodding as he stared me up and down.'
    MC "If you tell anyone what you've seen-"
    TRAYAN @sad "I won't! I WON'T!"
    TRAYAN @sad "I promise!"
    "I sighed, having the briefest dark thought about killing the boy to keep my secret, but..."
    "{i}No, I couldn't.{/i}"
    "Morality aside, the last thing I needed was some merchant lord investigating his son's death and raising hell on the matter."
    "{i}Even more eyes on all this was the last thing I needed.{/i}"
    TRAYAN @sad "...D-Did my father send you?"
    TRAYAN "My name is Trayan."
    $ CharMeet("trayan")
    TRAYAN " {i}... What are you?{/i}"
    MC "That doesn't matter, what matters is we get you home."
    'Trayan gulped and nodded anxiously.'
    TRAYAN "Y-Yes, of course."
    TRAYAN "Lead the way."
    jump qst_guild_price_life_son_rescued

label qst_guild_price_life_son_done_talking:
    $ PlayerRemItem("qst_ransom_money")
    $ PlayerAddItem("gold", 500)
    MARAUDER_LEADER "BOYS! DRAW YOUR BLADES!"
    MARAUDER_LEADER "Looks like we're done talking!"
    MARAUDER_LEADER "Kill it! Fucking kill it now!"


    $ TransformMC(True)
    $ TransformMarkus(True)

    $ PlayMusicRandom("mus_battle_generic")

    $ StartBattle(BattleData("pbat_forest", CharIDList_Right = ["e_raider", "e_raider"]))

    $ TransformMC(False)
    $ TransformMarkus(False)

    "With the last of Marauders dead at my feet, their leader's skull crushed into a bloody pulp beneath my feet, I unlocked the cage of the katai and let him out."

    
    scene bg_forest
    show mc_transformed at left
    show trayan at right_f
    with dissolve
    "The boy's cheeks flushed red as he stared up at me not in horror but ...awe?"
    $ PlayMusic("audio/music/3_Novaras_L.ogg")
    MC 'I am here to rescue you, you have nothing to fear.'
    TRAYAN "You-"
    TRAYAN "{i}You killed all of them.{/i}"
    MC "They would have done the same to me if given the chance."
    TRAYAN "I ... Yes, of course."
    TRAYAN "My name is Trayan."
    $ CharMeet("trayan")
    TRAYAN " {i}... What are you?{/i}"
    MC "That doesn't matter, what matters is we get you home."
    'Trayan gulped and nodded anxiously.'
    TRAYAN "Y-Yes, of course."
    TRAYAN "Lead the way."
    jump qst_guild_price_life_son_rescued

# at this point, all above variants converge
label qst_guild_price_life_son_rescued:
    scene black with dissolve
    'We traveled back along the path for some time.'
    scene bg_forest
    show mc at left
    show trayan at right_f
    with dissolve
    'We traveled back along the path for some time.'
    TRAYAN "...T-Thank you for rescuing me."
    MC "Nothing to thank."
    MC "And you have nothing to thank."
    MC "...Though if you could not tell anyone about what you saw back there when I changed-"
    TRAYAN "O-Oh, of course ... People like us need to look out for each other."
    MC "{i}'People like us?'{/i}"
    TRAYAN "You know ...{i}Non-humans.{/i}"
    'Trayan smiled.'
    TRAYAN "Your secret's safe with me."
    'I thought for a moment about protesting against being called not human, but I decided it was best to avoid the conversation altogether and change the subject instead.'
    MC "Though I must admit, {i}I'm surprised{/i} you're ... Well ..."
    TRAYAN "A katai?"
    MC "Yes."
    MC "Novaras isn't exactly known for its tolerance these days."
    TRAYAN "I'm not from Novaras, we're just visiting."
    TRAYAN "My family lives in the free city of Hamun."
    MC "That so?"
    MC "Are there many of your kind there?"
    TRAYAN "Not many, at least, compared to somewhere like Ramon."
    TRAYAN "But Hamun tolerates us enough to get by."
    MC 'I see.'
    'The Katai boy began to blush as he looked me up and down through the travel, and I kept catching him sneaking looks before shyly averting his eyes.'
    MC 'Is there a reason you keep looking at me?'
    TRAYAN "N-No! Of course not!"
    MC "Oh, {i}But you are looking at me?{/i}"
    TRAYAN "I-"
    'Trayan averted his gaze once again, cheeks bright red.'
    TRAYAN 'N-No ...'
    menu:
        "That's a shame, I was hoping to fuck something tonight.":
            $ QstGuildPriceLife().sex_scene = True
            'The boys eyes widened in shock as he flushed red.'
            'He opened his mouth to say something, but instead chose to look shyly to the floor once again in silence.'
        '(Say nothing.)':
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
    show trayan at right_f
    with dissolve
    MC "Your father only booked one room it seems."
    MC "He really didn't want to spend anymore than he had to, did he?"
    TRAYAN @sad "O-Oh."
    TRAYAN @sad "Father doesn't really care much for me, fourth son and all that."
    MC @talk "Ah, I am sorry to hear that."
    TRAYAN @talk "It's no matter."
    if QstGuildPriceLife().sex_scene:
        jump qst_guild_price_life_son_sex_offer
    else:
        scene black with dissolve
        call center_text(_("Next morning...")) from _call_center_text_2
        jump qst_guild_price_life_son_ending

label qst_guild_price_life_son_sex_offer:
    TRAYAN @talk "Not being watched as much as the others has its advantages."
    MC @talk "Does it?"
    TRAYAN @blush "Y-Yes."
    TRAYAN @blush "Such as what I get up to in the night."
    'Trayan bite at his lower lip, nervously trying to gauge my response as his cat ears perked up.'
    TRAYAN @blush "Do ... Do you like to get up to things in the night?"
    menu:
        "How long are you going to stand there with your clothes on?":
            "Trayan's ears perked up as he shyly smiled."
            TRAYAN "C-Could you wait here a moment for me?"
            TRAYAN "There's something I need to get."
            MC @smile "Take your time."
            hide trayan with easeoutright
            'Trayan hurried off, and as he did so, I began to undress for the evening.' #MC half naked
            $ CharSetClothes("mc", "pants")
            show mc at blurin, cright_f with easeoutright
            'A short while later, there was a gentle knock at the door once again as Trayan returned.' #Trayan in lingerie 
            $ CharSetClothes("trayan", "ling")
            show trayan at cleft with easeinleft
            TRAYAN @blush "H-Hello ..."
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            TRAYAN @blush "I heard um, you were hoping to fuck something tonight."
            TRAYAN @blush "... M-Maybe that something could be me?" 
            scene black with dissolve
            $ CharSetClothes("mc", "normal")
            $ CharSetClothes("trayan", "normal")

            'Grabbing a hold of Trayan by the shoulders, he let out a little gasp as I threw him onto the bed, stripping off the last of my clothes.' #Cut to Trayan blowjob
            TRAYAN "Y-You're-!"
            TRAYAN @blush "H-How is that supposed to fit inside of me?"
            MC @smile "With lots of patience and lubricant."
            'Trayan sheepishly nodded as I reached around to grab the back of his head.' 
            scene trayan_bj_ling_1 with dissolve
            $ PlaySexFx("audio/sex_sounds/no_voice.ogg",1)
            $ Pause()
            'As I pulled him forward towards me, his mouth opened up as he willingly wrapped his lips around my cock.' #Blowjob Animation begins
            'His head bobbed back and forth keenly as his tongue thrashed and beat against my cock.'
            TRAYAN "{i}*Slurp!*{/i} Mhmmfff!"
            'With a fistful of his, I continued to pull him forward to service me.'
            MC "Ahh! That's it ... Mmmfghh!"
            MC "Quite the good little cock-sucker, aren't you?"
            TRAYAN  "Mhhfghh! {i}*Slurp!*{/i} Yheshh! Mmm!"
            TRAYAN "Mh-Mhoree! Mmffhh! {i}*Slurp!*{/i}"
            'Trayan continued lovingly run his tongue along my cock as his wet mouth slide back and forth, lovingly coating my member in his warm saliva.'
            'I moved faster, thrusting deeper down into his throat as Trayan began to let out little flustered choking sounds, struggling to take the length of my cock.'
            'His muffled moans grew louder as he continued his wet sloppy blowjob, grunting as he threw his head forward, doing his best to take as much of my cock as deeply as he could.'
            'After some time, I finally began to feel my balls tighten as the tight, warm little mouth worked me with such keen delight.'
            'His bright eyes looked up to me almost shimmering as his cheeks blushed with my cock stuffed into his mouth.'
            'There was a desperation to his face, a keen loving tenderness to {i}know{/i} I was pleased.'
            MC "{i}*Huff*{/i} That's it ... Urghhff! I'm getting close you little slut!"
            scene trayan_bj_ling_2 with dissolve
            $ Pause()
            TRAYAN "{i}*Slurp!* *Slurp!*{/i} Mmmfhh! Chummm inhhmee!!"
            MC 'A-Ahhhff! Fuck it!'
            MC 'Take it then you little sluttt!!' 
            "Unable to hold back any longer, I yanked Trayan's head forward, flooding his mouth with a heavy, hot load." #Blowjob animation ends
            "His eyes widened as he squealed feeling the warm seed pour into his mouth, but quickly, he did his best to swallow down every drop."
            "Obediently, after tending sucking on the head for a few more moments, with a loud *PLOP* he pulled back to show me his own and empty mouth."
            MC "{i}*Huff*{/i}, good little slut."
            MC "Now stick out that fat butt of yours, time to fill you up."
            'Sheepishly, Trayan did as he was told.' #Cut to Trayan sex scene
            scene trayan_doggy_1 with dissolve
            $ Pause()
            'Bending down with his round, soft ass in the air, I pressed the hilt of my wet cock against his tight hole.'
            TRAYAN "B-Be gentle, you're the biggest I-"
            'I pressed the bulbous head of my cock against his tight backdoor, watching it spread around my cock as he squealed.' #Sex animation begins
            TRAYAN "AHH! F-Fuck! You're huge!"
            TRAYAN "H-Hrghh!"
            MC "Fuck are you tight! Urghh!"
            MC "Relax your ass a little slut!"
            TRAYAN "T-Trying!"
            BLACK "(Allow me to assist.)"
            'As the Dark Passenger whispered in my head, I suddenly felt something course out of my body and flood into Trayan.'
            TRAYAN "W-What is-"
            TRAYAN "Ooooh! That f-feels so good!"
            MC "(What did you do?)"
            BLACK "(Just a little lubrication and aphrodisiac ... Good for intercourse.)"
            BLACK "(Though I must warn you ... This mate is not capable of siring young.)"
            MC "(Ah! No shit! I'm fucking them because its fun!)"
            BLACK "( ... Interesting.)"
            'Their tight ass squeezed me effortlessly as I stretched their backdoor, listening out for their particularly feminine sounding moans.'
            scene trayan_doggy_2 with dissolve
            $ Pause()
            "I was soon thrusting in and out of them with ease, the strange lube released allowed me to glide with ease through their tight backdoor,"
            "And whatever pain Trayan was experiencing now gave way to euphoric pleasure."
            TRAYAN "F-Fuck me! Mmmfghh! Its incredible!"
            TRAYAN "FUCK ME HARDER!"
            TRAYAN "FUCK MY ASS! PLEASE! Mmmfghh!"
            TRAYAN "{i}*Huff*{/i} It f-feels sooo good!"
            "As they continued to throw their ass back onto me, the sounds of flesh slapping echoed throughout the room as the bed-frame continued to rock and hit against the wall."
            "For some time, I continued to plow their back door, listening to their symphony of moans as their mind became flooded with pleasure."
            "Finally, I began to feel my own climax draw near, and as I buried my cock tightly in their ass, I grunted and whispered in Trayan's ear affectionately,"
            MC "Where should I finish slut?"
            TRAYAN "Ah! Ah! W-Wherever you want!"
            TRAYAN "Gods! You can do whatever you fucking want to me! Mmff!"
            TRAYAN "I've never felt so good before!!"
            'Unable to hold back any longer, I gritted my teeth, grunting loudly as I bottomed out inside of their tight ass, unleashing a hot heavy loud into their now loosened backdoor.'
            "Trayan's eyes began to roll back in pleasure as he choked on air, shaking and trembling as he felt the rush of warm seed pouring into him."
            scene trayan_doggy_finish with flash
            $ ReduceInfectionFromSex("trayan")
            $ UnlockGalSceneAndGrantXp("callie_trayan", "trayan")
            $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
            $ Pause()
            "Trayan rolled over breathlessly beside me, breathing heavily as he laid in exhausted ecstasy."
            TRAYAN "{i}*Huff*{/i} That was {i}*Huff*{/i} the best-"
            $ CharAddRelEntry("trayan", "had_sex")
            "Before I could answer him, his eyes were always closed as he drifted off to sleep with a happy, drooling expression on his face."
            MC "(Well ... Goodnight to you too, I guess!)"
        "Yes, {i}sleeping.{/i}":
            "Trayans' cat ears flopped down in disappointment."
            TRAYAN "O-Oh, of course."
            TRAYAN "Umm, I just thought-"
            'He shook his head.'
            TRAYAN "No, never mind."
    jump qst_guild_price_life_son_ending

label qst_guild_price_life_son_ending:
    $ AutoMus(True)
    scene black with dissolve
    $ TimeAdvTo(TIME_MORNING)
    "We returned to Novaras by dawn."
    "I delivered Trayan back to his father's men safely, and was handed the coin for my services."
    if QstGuildPriceLife().sex_scene:
        "Before he left, Trayan remarked that if I was ever visiting Hamun, I would be welcomed as a guest..."
    $ QstComplete(QstGuildPriceLife)
    $ LocNameReset()
    $ LocSet("novaras_dist_market")
    $ LocEnter()