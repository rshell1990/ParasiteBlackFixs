label qst_little_lies_on_enter_1:
    show mika at center with dissolve
    MIKA @sad "Aww damn it..."
    MIKA @sad "Well, W-What did Sister Divine ask you to do?"
    MIKA @angry "I a-already passed their stupid exams! What more do they want from me?"
    "Mika turned back towards tending to the garden, watering some plants."
    MC @talk "What are you doing up here?"
    MIKA @talk "G-Gardening."
    MIKA @sad "{i}It reminds me of home...{/i}"
    "There was a hint of sadness in that last sentence."
    menu qst_little_lies_on_enter_1_menu:
        "The garden here is quite beautiful.":
            MIKA @talk "Mmm, it is."
            MIKA @talk "There are normally servants who look after it, or some of the other girls help out occasionally."
            MIKA @talk "B-But I like getting my hands dirty, though, so I help out a lot!"
            "Mika pouts."
            MIKA @angry "They wouldn't let me plant seeds and stuff though to grow some stuff we could eat..."
            jump qst_little_lies_on_enter_1_menu
        "Do you get on with the other girls?":
            MIKA @talk "I mean, I g-guess so?"
            MIKA @talk "I know they care, even Zara deep down ... But ..."
            MIKA @talk "Most of them have known each other since they were little, I came in a little later, so I guess it's a little different for me?"
            MIKA @talk "Or, maybe they just think I'm dumb."
            MIKA @talk "Mmm, t-that's probably it."
            MIKA @angry "... W-Why you asking about all this anyway?"
            MIKA @think "I don't wanna talk about it anymore..."
            jump qst_little_lies_on_enter_1_menu
        "Sister Divine wants me to teach you to be able to defend yourself.": #continues main story
            MIKA @scared "W-Wha...?"
            MIKA @scared "I don't ... I don't need to fight! I'm a mage of Palam!"
            MIKA @angry "I passed all the exams! What more do they want? HMM?"
            MIKA @angry "Is anyone else being asked to redo stuff, or just me?"
            MC @talk "This isn't about exams; what if the Demorai break through the walls, and you're forced to face them head-on?"
            MIKA @scared "I-"
            MIKA @angry "S-Shut up!"
            hide mika with moveoutright
            "Mika stormed off in a huff."
            show mc at left with dissolve
            MC @talk "Mika!"
            MC @talk "...Damn it."
            MC @talk "(Looks like I'm going to need to take a different approach if I'm going to get her to do what I want.)"

    hide mc with dissolve
    $ QstSetProgress(QstLittleLies, 1)
    $ LocEnterQ()

label qst_little_lies_on_enter_2:
    #Scene 4 - GIRLS DORM - MIKA can be found here 
    show mika at center with dissolve
    MIKA @angry "Hmph! What do you want?"
    MC @think "I understand you're afraid of fighting, Mika, but if you don't learn, then-"
    "Mika pouted."
    MIKA @angry "I d-don't wanna fight!"
    MC @angry "Then we're both stuck, aren't we?"
    MIKA @angry "HMPH!"
    "I sighed, rubbing my brow in frustration as I wondered how was I ever going to get through to this girl?"
    MC @talk "Okay, I can see this isn't getting us anywhere."
    MC @talk "So you tell me, what do {i}you{/i} want in return for letting me teach you to fight?"
    "Mika seemed taken aback by the question; she blinked in surprise and then pondered the thought."
    MIKA @shock "W-What I want?"
    MIKA @think "Ummm ..."
    MIKA @scared "Uhhh...!!"
    MIKA @smile "I-I know!"
    MIKA @smile "I want a section of the gardens upstairs just for farming!"
    MC @think "What?"
    MIKA @angry "Look, pretty flowers are nice and all that! But ..."
    MIKA @angry "I've wanted to grow some nice vegetables and stuff up there for years, but they keep saying {i}OOoOoh no! The gardens not for that!{/i}"
    MIKA @smile "So, help me get my little farming patch, and I'll d-do whatever you want!"
    menu qst_little_lies_on_enter_2_menu:
        "How about I just give you some coin instead?":
            label qst_little_lies_on_enter_2_coin_offer:
                MIKA @angry "Hmph!"
                MIKA @angry "In that case, I won't do it less than ... than ..."
                MIKA @shock "T-TWENTY THOUSAND COINS!"
                MC @surprised "Are you mad?"
                MC @surprised "You expect me to give you twenty thousand coins to teach {i}you{/i} to fight?"
                MIKA @angry "T-Take it or leave it!" 
                $ QstLittleLies().mikaOfferedCost = True
                menu qst_little_lies_on_enter_2_menu_2:
                    "I'll give you five thousand and not a coin more..." (Req_Barter = 6) if (QstLittleLies().persuasionCost != 5000):
                        MIKA @think "...F-Five thousand?" #Success
                        MC @talk "Enough to even buy yourself a {i}actual{/i} patch of farmland."
                        MIKA @think "...F-Fine."
                        MIKA @angry "I'll do as you ask for five thousand."
                        $ QstLittleLies().persuasionCost = 5000
                        jump qst_little_lies_on_enter_2_menu_2
                    "Here, as agreed." (Req_Gold = QstLittleLies().persuasionCost):
                        $ PlayerRemItem("gold", QstLittleLies().persuasionCost)
                        MIKA @shock "B-BY THE GODDESS!"
                        MIKA @shock "You actually paid it?!"
                        MIKA @blush "U-Um, alright, a deal is a deal after all..."
                        $ QstLittleLies().persuasionPaid = True
                        $ QstSetProgress(QstLittleLies, 5)
                        $ LocEnter()
                    "I don't have your coin right now.":
                        MIKA @angry "Hmph! I ain't gonna fight you and stuff just because you {i}say{/i} you'll pay me!"
                        MIKA @angry "I know when someone's trying to trick me! I ain't as stupid as people think!"
                        MIKA @angry "Coin first! THEN I'll do as you ask!" 
                        if QstGetProgress(QstLittleLies) < 2:
                            $ QstSetProgress(QstLittleLies, 2)
                        $ LocEnter()
        "Surely there must be something else you want..." (Req_Charm = 6): #(Low) Charisma check
            label qst_little_lies_on_enter_2_divine_crush:
                MIKA @think "Hmmm..." #success
                MIKA @talk "W-Well ... there is one thing."
                MC @talk "What is it?"
                MIKA @blush "Could ... Could you persuade Sister Divine to umm..."
                "Mika paused, her next sentence almost a nervous whisper."
                MIKA @blush "Y-You know ... {i}With me.{/i}"
                MC @surprised "Wait, what?"
                MC @surprised "But she's-"
                MIKA @blush "I know, she's the head mage at the tower, but..."
                MIKA @sad "I get so j-jealous when she plays with the other girls and not me!"
                MC @surprised "...Wait, what?"
                MIKA @sad "What do you mean, what?"
                MC @surprised "Sister Divine has ... Fucked some of the other mages?"
                MIKA @talk "A couple, of course."
                MIKA @shock "W-Wait, {i}you didn't know that?{/i}"
                MC @think "Is this ... a common practice around here?"
                MIKA @think "I mean, w-well, of course?"
                MIKA @think "What did you think would happen if you shoved a load of horny mages in a tower and told them who they could and {i}should{/i} be spending time with?"
                MIKA @blush "We all kinda, y'know ... {i}L-Learned to look after each other.{/i}"
                $ QstLittleLies().mikaToldAboutHerDivineCrush = True
                menu qst_little_lies_on_enter_2_menu_3:
                    "Has she been with Jana or Zara?":
                        MIKA @talk "N-No, Not as far as I'm aware, no."
                        MIKA @talk "While some mages become couples, for many, it's not always so serious."
                        MIKA @talk "For many, it's just the only way they can find any relief."
                        jump qst_little_lies_on_enter_2_menu_3
                    "How many girls has Sister Divine been with?":
                        MIKA @talk "Hm? Like ... I dunno, a fair few."
                        MIKA @talk "She doesn't say it, but she's lonely too."
                        MC @talk "Has she ... sired any young?"
                        MIKA @blush "Well, if a girl gets pregnant here, we don't discuss who played the role of 'mother' and 'father.'"
                        "Mika chuckled lightly."
                        MIKA @smile "We just offer praise to the gods for this {i}miraculous{/i} birth, of course."
                        jump qst_little_lies_on_enter_2_menu_3
                    "I will give it some thought.":
                        MIKA @talk "Mmm! Let me know what you decide in the end!"
                        if QstGetProgress(QstLittleLies) < 2:
                            $ QstSetProgress(QstLittleLies, 2)
                        $ LocEnter()
                    "I will see about helping set up a little trust between you and Sister Divine.": #Only available if the player passed the charisma check 
                        label qst_little_lies_on_enter_2_offer_date_help:
                            MIKA @shock "Y-YOU WILL?!"
                            MIKA @blush "I mean, um, t-that's great!"
                            MIKA @blush "L-Let me know if she agrees."
                            $ QstLittleLies().askToGoOutWithMika = True
                            $ QstSetProgress(QstLittleLies, 3)
                            $ LocEnter()
        "I will get you your farming patch.":
            label qst_little_lies_on_enter_2_offer_farming_patch_help:
                MIKA @smile "Great!"
                MIKA @smile "I can't believe you're gonna help me!"
                MIKA @blush "I'm uhh, n-not used to people talking me seriously..."
                "Mika paused momentarily, thinking about her own words before she shook her head."
                MIKA @smile "L-Lemme know how it goes!"
                $ QstLittleLies().askToGiveMikaTheFarmingPatch = True
                $ QstSetProgress(QstLittleLies, 3)
                $ LocEnter()

label qst_little_lies_on_enter_3:
    show mika at center with dissolve
    MIKA @talk "Well?"
    menu:
        "I will get you your farming patch." if not QstLittleLies().askToGiveMikaTheFarmingPatch:
            jump qst_little_lies_on_enter_2_offer_farming_patch_help
        "How about I just give you some coin instead?" if (not QstLittleLies().mikaOfferedCost and QstGetProgress(QstLittleLies) < 4):
            jump qst_little_lies_on_enter_2_coin_offer
        "About the coin..." if (QstLittleLies().mikaOfferedCost and QstGetProgress(QstLittleLies) < 4): #ALT - If the player has already mentioned giving money and negotiated, the question is "About the coin..." - cuts to the 'As agreed' or 'I don't have the coin yet' choice.
            jump qst_little_lies_on_enter_2_menu_2
        "About your garden patch for farming..." if QstLittleLies().mikaGotFarmingPatch: #IF PLAYER HAS AGREED TO HELP MIKA GET HERSELF A FARM PATCH 
            MIKA @talk "Any luck?"
            menu:
                "Sister Divine's agreed to your request.": #If sister divine has agreed via payment of coin, the bear hide, OR because of the player's previous seduction
                    MIKA @shock "She ... {i}She actually agreed?{/i}"
                    MIKA @shock "By the gods! How in all the realms of hell did she agree?"
                    MC @smile "That's {i}my{/i} business, not yours."
                    "As Mika's initial shock began to pass, it quickly gave way to excitement."
                    MIKA @smile "Ooooh! This is amazing news!"
                    MIKA @smile "I'll start with tomatoes! And then, I'm gonna try to grow-"
                    MC @serious "Hold now, remember our deal, Mika."
                    MC @talk "Your combat training must come first."
                    MIKA @angry "Seriously?!"
                    MIKA @sad "But-"
                    MC @talk "You may garden in your spare time... In the meanwhile, though, we will be sparring."
                    MIKA @sad "Awww, damn it ..."
                    MIKA @talk "Alright, I agree. It's not like I got much room to argue after you pulled off something I've been begging for for who knows how long."
                    MIKA @think "Umm, I guess I'll meet you in the rooftop gardens? There's a section of ground we often use for combat training up there."
                    MIKA @think "I'll be waiting for you..." #MIKA leaves
                    $ QstSetProgress(QstLittleLies, 5)
                    $ LocEnter()
        "Surely there must be something else you want..." (Req_Charm = 6) if not QstLittleLies().mikaToldAboutHerDivineCrush:
            jump qst_little_lies_on_enter_2_divine_crush
        "I will see about helping set up a little trust between you and Sister Divine." if (QstLittleLies().mikaToldAboutHerDivineCrush and QstGetProgress(QstLittleLies) < 4 and not QstLittleLies().askToGoOutWithMika):
            jump qst_little_lies_on_enter_2_offer_date_help
        "About sister Divine..." if QstLittleLies().askToGoOutWithMika: #Available if the player offered to try and help arrange a tryst between her and Sister Divine
            MIKA @blush "W-What did she say?"
            menu:
                "I'll get back to you shortly with her answer." if not QstLittleLies().mikaWillHaveHerDate:
                    MIKA @blush "Okay..." #ends dialogue
                    $ LocEnter()
                "She said to meet her in the tower bathhouse this evening." if QstLittleLies().mikaWillHaveHerDate: #If sister Divine agreed
                    MIKA @shock "She ... {i}She actually agreed?{/i}"
                    MIKA @shock "I ... I don't believe it!"
                    MC @think "Isn't this what you asked for?"
                    MIKA @scared "Y-Yes, but never in a hundred years did I think she'd actually agree!"
                    MIKA @blush "W-What do I do now?"
                    MC @smile "Get ready and meet her tonight, of course."
                    MIKA @blush "W-Would you maybe watch over me?"
                    MC @surprised "What?"
                    MIKA @shock "W-What if she changes her mind?!"
                    MIKA @sad "Y-You don't have to stay and watch or anything."
                    MC @surprised "Why do you want me there?"
                    MIKA @scared "I -I don't know!"
                    MIKA @scared "In case something goes wrong?"
                    MIKA @blush "Urghh, I'm sorry, I don't even know why I'm saying all this."
                    MIKA @blush "This is all happening so fast, and now I'm just so damn nervous."
                    menu:
                        "You don't need me there.":
                            MIKA @sad "I ... Yes, of course."
                            MIKA @talk "I asked for this, and I've got it."
                            MIKA @blush "T-Time to take some responsibility."
                            MC @talk "And our deal?"
                            MIKA @talk "Tomorrow I'll study whatever you want."
                            MIKA @blush "T-Tonight though..."
                            MIKA @blush "{i}Tonight is just for me.{/i}" #Continues main quest - skips sister divine x MIKA scene
                            $ QstLittleLies().mikaXDivineSceneSkipped = True
                            $ QstSetProgress(QstLittleLies, 5)
                        "I'll be there to keep an eye on you.":
                            MIKA @smile "You will?"
                            MIKA @blush "O-Okay, I'll see you at the bathhouse."
                            MIKA @blush "No idea what time she's arriving this evening, but I'll be there!" #Additional part of the quest to look out for MIKA at the bathhouse in the evening 
                            $ QstLittleLies().mikaXDivineSceneSkipped = False
                            $ QstSetProgress(QstLittleLies, 4.1)
                    $ LocEnter()
        "Nothing for now.":
            MIKA @talk "Then I'll be here waiting..." #Ends conversation
            $ LocEnter()
label qst_little_lies_bathhouse_scene:
    ####Player finds MIKA at the bathhouse in the Evening####
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ CharSetClothes("mika", "naked")
    $ CharSetClothes("divine", "towel")
    show mika at center with dissolve
    "Mika gently stroked her way up and down the length of the pool almost silently."
    $ CharSetClothes("mika", "water")
    show mika:
        center
        blurin
    "Her wet naked body glistened from the water in the moonlight as she ran her hands through her wet hair and sighed."
    "She looked around for a few moments, her face crestfallen as she swam towards the pool's edge to climb out."
    show divine at left with dissolve
    DIVINE @happy "Room for one more?"
    show mika:
        xzoom -1.0
    with dissolve
    "Mika splashed as she turned startled towards Sister Divine, smiling above her with a towel wrapped around her."
    MIKA @shock "S-Sister Divine?!"
    $ CharSetClothes("divine", "naked")
    show divine:
        left
        blurin
    play sound2 "audio/cfx/cotton_drop.ogg"
    "Sister Divine laughed as she undid the towel around her, allowing it to fall to the floor."
    DIVINE @happy "Come now, the pool's big enough for the two of us, is it not?"
    "Mika's cheeks flushed red as her eyes stared at the dangling appendage between Sister Divine's legs."
    MIKA @blush "Y-Yes it is..."
    MIKA @blush "It's big - I mean, the {i}pool{/i} is big enough."
    play sound2 "audio/cfx/divine_mika_water_noise.ogg"
    $ CharSetClothes("divine", "water")
    show divine:
        left
        blurin
    "Sister Divine smiled knowingly as she stepped into the pool, slowly submerging half of her body."
    DIVINE @happy "Ahh, nice and cool, is it not?"
    MIKA @talk "Y-Yes ..."
    show mika:
        xzoom 1.0
    with dissolve
    "Mika turned her back to Sister Divine, her hands shyly clutching at each of her arms."
    DIVINE @sad "Mika? Is everything alright?"
    MIKA @blush "I ... I'm fine."
    MIKA @blush "I'm s-sorry, I just can't believe this is happening."
    MIKA @sad "... I didn't even think you {i}liked me.{/i}"
    DIVINE @sad "...Mika."
    "The two women sat in the pool in silence for a few moments when Sister Divine finally said,"
    DIVINE @sad "... I've always let the girls approach me if they needed {i}comfort,{/i} never the other way around."
    DIVINE @sad "This place ... This little world we've built to keep ourselves safe inside this tower, it's almost like a dream, you see."
    DIVINE @sad "My greatest fear is that you girls might come to hate me, come to despise and feel I've taken advantage of you."
    "Sister Divine swam closer towards Mika, who continued to shyly look away."
    DIVINE @talk "That's why I never pursued you, Mika."
    MIKA @blush "I ... I see."
    "Sister Divine ever so tenderly wrapped her arms around Mika, whose breath escaped her in surprise."
    # scene here - hug
    scene mika_divine_hug with dissolve
    $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
    DIVINE "You only ever needed to ask..."
    "Mika smiled softly, her cheeks blushing red."
    MIKA "Was that all it would have taken?"
    MIKA "To just ... {i}ask?{/i}"
    "Mika let out a soft gasp as Divine's hands cupped and fondled at Mika's soft breasts."
    MIKA "M-Mfghh!"
    DIVINE "I had hoped you would find love outside this place."
    MIKA "W-What do you mean?"
    DIVINE "... Love, {i}Lust,{/i} this place can become like a trap."
    "Sister Divine's thumbs circled over Mika's hardened nipples."
    MIKA "Ooooh! S-Sister!"
    DIVINE "Us Mages of Palam can rely on each other so much for these base needs, but we start to convince ourselves we can {i}only{/i} find it amongst our own."
    MIKA "{i}*Huff*{/i} A-Are you saying you want to stop, Sister?"
    "Sister Divine smiled reassuringly once more."
    DIVINE "When you leave this place, I want you to find real love, Mika."
    DIVINE "{i}...But tonight, I'll give you the love you need.{/i}"
    "Sister Divine's hand reached down beneath the soft water, gently wrapping around Mika's cock as she stroked back and forth."
    MIKA "M-Mhfff!"
    DIVINE "Shh, let me take care of you tonight."
    DIVINE "You're so pent up, poor thing..."
    "Sister Divine generously applied soft kisses to Mika's neck, who shuddered with pleasure."
    MIKA "S-Sister, {i}*Huff*{/i}"
    MIKA "I can f-feel your ... {i}thing{/i} prodding against my butt."
    "Sister Divine giggled playfully,"
    DIVINE "Are you ready for what's next?"
    "Mika's breath trembled as she lightly nodded, and Sister Divine bent Mika over the pool's edge."
    # scene here - cock on butt
    scene divine_fucking_mika_at_bathhouse_idle with dissolve
    $ StopSexFx()
    "With Mika's round ass waving in front of Sister Divine's face, she stepped up from behind it and grabbed hold of the soft butt."
    "Mika let out another startled gasp as she felt the hard, blue cock wedged between her cheeks, lightly rubbing back and forth."
    MIKA "{i}D-Do it.{/i}"
    "Sister Divine pulled back, aligning the head of her cock against the wet slit opening, and entered into Mika."
    # scene here - slow penetration
    scene divine_fucking_mika_at_bathhouse_slow with dissolve
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    "Mika let out a hot gasp as the member slowly glided inside her womanhood inch by inch."
    MIKA "A-Ahhh...!"
    DIVINE "Hrghh! You're - Mhmm! T-Tight, Mika."
    "As Sister Divine's cock slowly glided in and out of her slowly, Mika groaned in pleasure as she offered a faint smile."
    MIKA "T-Thank you. - Mhfghh!"
    "Divine squeezed the fat flesh of Mika's ass between her fingers as she held on tightly, slowly moving faster as she thrust in and out of Mika."
    DIVINE "Mhff! Are you ready for me to move faster, dear?"
    MIKA "{i}*Huff*{/i} Y-Yes ...!"
    # scene here - fast penetration
    scene divine_fucking_mika_at_bathhouse_fast with dissolve
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    "With a light slap across the butt, Mika whelped in surprise as her butt jiggled a little with the motion."
    "Wet sloshing sounds echoed slightly throughout the bathhouse as the flesh collided."
    "Mika moaned hotly as Sister Divine began to slam deeply into her from behind."
    MIKA "M-Mmfhghhh!!"
    DIVINE "Oooh! MIKA!"
    DIVINE "Y-You're squeezing me - Mhfhh! So tight!"
    MIKA "M-More! Don't s-stop!"
    MIKA "Oooh! I can't help it! I've been waiting for this for so long!"
    "The two women's breasts swung back and forth with every motion as their passionate tryst continued for some time."
    DIVINE "{i}*Huff*{/i} You s-silly girl!"
    DIVINE "You should have - Ahh! Offered me this ass sooner!"
    MIKA "Oooooooh! Yes, Miss! It's all yours! My ass is all yours tonight!"
    "Sister Divine gritted her teeth, the two locked and contorted in pleasure as Sister Divine fucked away at Mika's tight hole."
    "Eventually, the heavy, sweet grunts and moans reached their climax as Mika weakly declared,"
    MIKA "I- I'm c-close!"
    DIVINE "Ahh! M-Myself too!"
    "Divine winced, desperately seeming to try and hold on for Mika's sake."
    MIKA "I-It's okay!"
    MIKA "{i}Fill me up!{/i}"
    DIVINE "B-But-"
    MIKA "Mhhfhh! Do it, sister! DO IT!"
    # scene here cum inside
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    show divine_fucking_mika_at_bathhouse_fast with flash
    show divine_fucking_mika_at_bathhouse_fast with flash
    scene divine_fucking_mika_at_bathhouse with flash
    "Unable to hold back any longer, Sister Divine lunged forward, wrapping her arm against Mika's neck in an almost choke hold-like position."
    "Stood upright, Sister Divine pumped against Mika's ass, pulling her lewd body back onto her member as deeply as she could."
    "Grunting loudly and thrusting as deeply as she could into Mika, she poured her hot load into Mika's womanhood."
    "Mika's tongue flopped out of her mouth as her eyes began to roll back."
    "She choked lightly beneath Sister Divine's grip, and her own, exciting, rock-hard cock splurted out a white stream as she was pumped full of Sister Divine's seed."
    "Releasing her grip, Mika dropped forward, barely catching herself on the pool's edge as the two women turned to face each other breathlessly."
    # hide scene
    $ LocFlush()
    show mika at left
    show divine:
        center
        xzoom -1.0
    with dissolve
    DIVINE @lewd "{i}*Huff*{/i} How was that - {i}*Huff*{/i} my dear?"
    "Mika smiled, biting down at her lower lip alluringly."
    MIKA @lewd "{i}Incredible.{/i}"
    "Sister Divine laughed."
    DIVINE @happy "You drained me dry, girl."
    "Mika softly chuckled with new-found confidence."
    MIKA @lewd "Bet you are glad to see my lazy butt is good for something, huh?"
    "The two girls smirked and shared another small laugh."
    MIKA @blush "... Y-You know how you said I needed to try and find love outside of all this."
    MIKA @blush "D-Do you think maybe [player_name!t] might be interested in a Mage of Palam?"
    MIKA @shock "H-He's not really s-staff, right? So-"
    DIVINE @talk "Those decisions are for him to make, Mika."
    MIKA @blush "But you wouldn't be mad if I ... You know, tried my luck?"
    DIVINE @happy "As long as you and the other girls are happy Mika, {i}I am happy.{/i}"
    "Mika smiled warmly at the comment."
    MIKA "I think I better get out of the pool and dry off for a bit."
    DIVINE "Don't forget your promise, Mika."
    DIVINE "Let him teach you to be able to defend yourself."
    "Mika groaned softly, but that groan coiled into a smile."
    MIKA @smile "Fineeee."
    play sound2 "audio/cfx/divine_mika_water_noise.ogg"
    "As Mika clambered out of the pool, Sister Divine reached out one last time to spank Mika's soft ass."
    play sound2 "audio/cfx/spank.ogg"
    $ CharSetClothes("mika", "towel_water")
    show mika:
        left 
        blurin
    "Mika gasped, and then, grabbing a towel, giggled as she hurried off, her heart beating out of her chest in excitement."
    hide mika with dissolve
    DIVINE @talk "... You can come out now."
    "Stepping out from behind the pillar, Sister Divine smiled coyly as she saw me."
    show mc at left with dissolve
    $ CharSetClothes("divine", "towel_water")
    show divine:
        center
        xzoom -1.0
        blurin
    DIVINE @happy "Did you enjoy the show?"
    MC @smile "I did."
    "Sister Divine smiled alluringly at the comment."
    if QstIsActive(RomanceDivine):
        DIVINE @lewd "I don't mind playing the man for the girls ..." #Variant 1 - If the player HAS romanced Divine already
        DIVINE @lewd "{i}But I've been craving being your woman again since last time.{/i}"
        DIVINE @lewd "Don't keep me waiting, dear."
        hide divine with dissolve
        "As Sister Divine left the bathhouse, I watched over my shoulder at her round ass lightly sway from side to side enticingly."
        "In the corner of her mouth, a sly smile..."
    else:
        DIVINE @lewd "My offer still stands." #Variant 2 - if the player HAS NOT previously romanced Divine
        DIVINE @lewd "Should you change your mind about me."
        DIVINE @happy "No need to answer now ... Just give it some thought."
        "As Sister Divine left the bathhouse, I watched over my shoulder at her round ass lightly sway from side to side enticingly."
        "In the corner of her mouth, a sly smile..."
    $ CharSetClothes("mika", "dress")
    $ CharSetClothes("divine", "normal")
    $ AutoMus(True)
    $ UnlockGalSceneAndGrantXp("mika", "divine_fucking_mika_at_bathhouse")
    $ QstSetProgress(QstLittleLies, 5)
    $ LocEnter()

label qst_little_lies_class_meet:
    show mika at center with dissolve
    MIKA @scared "Will you be training me now?"
    menu:
        "It's time to spar, Mika.":
            "The blood drained from Mika's face as she turned a paler shade of blue."
            MIKA @scared "I-"
            MIKA @scared "Do we have to?"
            MC @talk "There's no other way."
            "Mika took a deep breath."
            MIKA @sad "Okay ... Okay, follow me to the training ground."
            scene black with dissolve
            "Following Mika to the training grounds, she took a deep breath and turned to face me."
            $ LocSet("novaras_palam_arena")
            $ LocFlush()
            show mika at center with dissolve
            MIKA @angry "So ... So, should I just, {i}attack?{/i}"
            "Mika's hands trembled as she stared petrified towards me."
            "I drew my blade; the only way to fully gauge the depths of Mika's issue would be to see how she reacted under pressure."
            MIKA @scared "W-Wait! What are you-"
            scene black with dissolve
            "As I leapt forward with my strike, I expected Mika to instinctively fire off some kind of counterspell or, at the very least, dodge out of the way."
            play sound2 "audio/cfx/female_long_scream.ogg"
            "Instead, Mika cried as she ducked down to the floor, her hands covering her ears as she screamed."
            "She waited with terrified, gritted teeth for the blade to fall down, and inches away from her face, I stopped the blade's swing."
            "Mika's tightly shut eyes slowly opened, and realizing I hadn't struck her, she slowly rose to her feet again."
            $ LocFlush()
            show mika cry at center 
            with dissolve
            MIKA @angry "You ... YOU BASTARD!"
            MIKA @angry "Why didn't you say you would do that!?"
            MC @angry "Mika! What in the seven hells was that just now?"
            MC @angry "You didn't even try to step out of the way! Do you have a death wish or something?"
            MIKA @scared "I ... I...!"
            MC @serious "Don't you understand? The Demorai won't hesitate! They'll tear you to pieces if you just cower like that!"
            MIKA @angry "I can run away!"
            MC @angry "MIKA!"
            show mika cry:
                shake
            "I grabbed Mika's shoulders, lightly shaking some sense into the girl."
            MC @angry "You cannot just rely on hoping that you can run away from everything, do you understand?"
            MC @angry "Do you think they'll just let you run away?"
            MC @angry "{i}Do you know how fast some Demorai are?{/i}"
            MC @angry "I've had my fill of death already; I watched countless men try and flee, only to be cut down as they did so!"
            MC @serious "You have to fight, Mika."
            MC @sad "{i}You have to fight.{/i}"
            MIKA @scared "I ... But I'm afraid."
            MIKA @cry "{i}I'm so afraid.{/i}"
            play sound2 "audio/cfx/running_steps.ogg"
            hide mika with moveoutright
            "Mika slipped from my grasp, hurrying away with tears stinging her eyes as she did so."
            MC @surprised "MIKA!"
            MC "(Damn it ...)"
            MC "(something's wrong here, fear is normal, but that was...)"
            MC "(That was something else.)"
            MC "(I need to pull her aside and speak to her in private somewhere, get to the bottom of this.)"
            $ QstSetProgress(QstLittleLies, 6)
            $ LocEnter()

        "Not yet; I have some things I need to take care of.":
            MIKA @talk "Ummm, very well then."
            MIKA @talk "Let me know when you're ready, I guess."
            $ LocEnter()

label qst_little_lies_class_meet_2:
    "Within the girl's dorm, I heard the sounds of soft sobbing and wailing."
    "With her face buried in her hands, Mika sobbed by the lit, warm fire."
    show mika cry at center with dissolve
    MIKA @cry "What? Have you come to humiliate me more?"
    show mc at left with dissolve
    MC @sad "I didn't mean to upset you that way, Mika."
    MC @sad "I'm trying to help you."
    MIKA @sad "{i}*sniff*{/i} It's hopeless."
    MIKA @sad "I can't ... I just can't!"
    MC @talk "...{i}*Sigh*{/i}"
    MC @sad "What was that back there on the training grounds?"
    MC @talk "You were petrified."
    MIKA @sad "... It doesn't matter."
    MIKA @angry "I just don't like fighting! Okay?"
    MIKA @angry "There's nothing more to discuss!"
    MC @talk "Very well, we'll try again tomorrow, hopefully with more luck."
    "The blood drains from Mika's face, and she gulps at the prospect of having to do that again in the morning."
    MIKA @scared "Y-Yes, tomorrow."
    MIKA @angry "I-I'll be ready!"
    MC "Then I shall see you come morning light on the training grounds."
    #MC exits off-screen
    hide mc with dissolve
    MIKA @scared "..."
    $ QstSetProgress(QstLittleLies, 7)
    hide mika with dissolve
    $ TimeAdvTo(TIME_DAY_END)
    $ LocEnter()

label qst_little_lies_class_meet_3:
    show mika at center with dissolve
    MIKA @scared "W-Well?"
    MIKA @scared "Are you ready to try again?"
    menu:
        "Let's do it!":
            MIKA @scared "F-Fine! Ready yourself!"
            MIKA @angry "This time will be different!"
            show mika angry
            "Taking my spot once more on the training ground, I gave Mika ample time to prepare herself."
            "With her hands raised, ready to spellcast, her hands trembled, and her legs seemed ready to buckle at any moment."
            "A bead of sweat dripped down her forehead as she waited with trembling breath for me to make my move..."
            "With my blade drawn, I charged towards Mika once again!"
            "As I drew closer and closer, her hands drew in the energy around her."
            "Perhaps last time really was just a fluke?"
            "She was too tense, but perhaps she just needed-"
            MIKA "AHHHHHH!"
            scene black with dissolve
            play sound2 "audio/cfx/mika_spell.ogg"
            "Mika screamed and cowered once more, looking away as she blindly fired a ball of energy completely off course, slamming it into a wall and leaving a huge gash in its wake."
            $ LocFlush()
            show mc angry at left 
            show mika cry at center
            with dissolve
            MC @angry "MIKA!"
            MIKA @cry "W-What?! I fought back this time!"
            MC @angry "You didn't even look where you were aiming!"
            MC @angry "What if one of the other girls was wandering through?"
            MC @angry "You could kill someone like that!"
            MIKA @cry "I'm - {i}*Sniff*{/i} sorry!"
            MIKA @cry "I didn't mean to! I didn't-"
            MC @think "...Fuck."
            MC @talk "Mika, you need to-"
            show zara at right_f with dissolve
            ZARA "Going well, I see."
            "Looking up, Zara, with her arms folded, moved towards the two of us."
            MIKA @scared "Zara! W-What are you doing here?"
            ZARA @angry "{i}... You have to tell him, Mika.{/i}"
            MIKA @shock "N-No!"
            ZARA @angry "MIKA!"
            MC @serious "Tell me what? What is going on here?"
            MIKA @angry "Nothing! Ignore her!"
            ZARA @angry "Mika, you can't keep what happened a secret any longer!"
            MIKA @angry "I SAID NO!"
            ZARA @angry "... Fine then, do as you wish."
            hide zara with moveoutright
            "Zara turned and left in a huff, leaving me alone with the disgruntled Mika."
            MC @talk "What was that about?"
            MIKA @angry "Nothing, just leave it alone."
            MC @serious "If this has something to do with your training, I can't just-"
            show mika cry:
                center
                xzoom -1.0
            with dissolve
            MIKA @angry "TRAINING THIS! TRAINING THAT!"
            MIKA @angry "Stop pretending like you actually care about me! You hardly even know me!"
            MIKA @sad "{i}You ... You have no idea what I've been through!{/i}"
            "Once again, with tears stinging her eyes, Mika hurried off."
            show mika cry:
                center
                xzoom 1.0
            with dissolve
            hide mika with moveoutright
            MC @surprised "Mika! Wait!"
            MC "(Damn it, what in the seven hells is going on with this girl?)"
            $ QstSetProgress(QstLittleLies, 8)
            $ QstLittleLies().block_dorm_day = day
            $ LocEnter()
        "Not just yet.":
            MIKA @sad "A-Alright, let me know when you're ready."
            $ LocEnter()

label qst_little_lies_dorm_blocked:
    show mc at left with dissolve
    "I can hear sobbing coming from the other side of the door ... I should give Mika some space."
    $ LocEnter()

label qst_little_lies_class_meet_4:
    "As I gently pushed open the door to the girls' quarters, a solemn looking Mika meekly approached me with her hands clasped together."
    show mika at center with dissolve
    MIKA @sad "Please... Must we train today?"
    "The girl's voice began to break."
    MIKA @sad "{i}I... I don't want to train anymore. Please.{/i}"
    "Realizing that pushing the matter was perhaps the wrong course of action, I needed to get to the bottom of whatever was troubling her mind."
    MC @talk "... Why don't we take a break today?"
    "Mika's eyes lit up almost instantly."
    MIKA @shock "You... You really mean it?"
    MC @talk "Training all the time isn't healthy."
    MC @talk "Come, let's go a place I know, {i}The Iron Unicorn.{/i}"
    MIKA @shock "You... You want me to go to a tavern with you?"
    MC @think "Is that a problem?"
    MIKA @sad "N-No, not technically."
    MIKA @sad "But I can't promise you won't get stares being out with me."
    MIKA @sad "People only ever seem to like seeing us outside when it's part of formal ceremonies and things."
    MIKA @sad "Otherwise, people act... {i}differently{/i} around us."
    MC @smile "I'll take my chances."
    MIKA @blush "I-If you're sure..."
    MIKA @talk "When shall we leave?"
    menu:
        "I'll walk with you, come.":
            MIKA @smile "Okay! Let me just grab some coin!" #Brief fade to black - cut to scene 7
            $ LocSet("novaras_tavern")
            $ LocFlush(fade)
            jump qst_little_lies_class_meet_5

        "I have some business to attend first, I'll meet you there.":
            MC @smile "Do you know the way?"
            "Mika smiled."
            MIKA @smile "Don't worry, I'll be there." 
            $ QstSetProgress(QstLittleLies, 8.1)
            $ LocEnter()

label qst_little_lies_class_meet_5:
    show mika at center with dissolve
    MIKA @shock "Ah! Over here!"
    MIKA @talk "I, um, ordered us a bottle!"
    MC @think "Hm? You bought a whole bottle to share?"
    MC @talk "That's too expensive for an apprentice mage; how much do I owe you?"
    MIKA @shock "D-Don't worry about that!"
    MIKA @smile "We're all given a set pay each month, but most of us tend to not know what to do with it half the time."
    MIKA @talk "Only so many books and ingredients you can get your hands on."
    "Mika handed me a cup of wine she had poured me and sipped her drink with both hands."
    MIKA @talk "Sooo, why did you want to speak to me here and not back at the tower?"
    MC @talk "Because walls have ears."
    MIKA @shock "Huh?"
    MC @talk "I wanted to speak to you somewhere where the other mages couldn't hear."
    MIKA @think "Why?"
    MC @talk "Because I want to know why you're so afraid of fighting."
    "Mika sullenly drank at her glass of wine."
    MIKA @sad "I just don't like fighting."
    MC @talk "Mika, you were petrified."
    MIKA @shock "I-"
    MIKA @sad "Yes ... Yes I was, I suppose."
    MC @serious "I need to know what's going on."
    MC @talk "What was Zara talking about before?"
    "Mika hesitated to answer, nervously sipping at her wine."
    MIKA @sad "You ... You were in the scouts, right?"
    MIKA @sad "{i}Before I tell you anything, you tell me why they pulled you out.{/i}"
    $ AutoAmb(False)
    $ AutoMus(False)
    $ PlayMusic("audio/music/42_Flashback.ogg")
    stop ambience
    stop ambience2
    show black with dissolve:
        alpha 0.6
    menu qst_little_lies_class_meet_5_menu:
        "You heard about that?":
            MIKA @think "Everyone's heard about the pair of scouts who were found outside the city walls..."
            MIKA @smile "Andddd, I overheard Sister Divine talking to that blonde Captain lady one time about hiring {i}that{/i} scout to help us."
            MIKA @talk "It doesn't take a genius to figure out who you were when you showed up."
            jump qst_little_lies_class_meet_5_menu
        "{i}*Tell Mika the full, gory story in horrifying detail- omitting only your dark passenger*{/i}":
            scene black
            with dissolve
            "For the next hour, I detailed every horrifying event from my time as a scout to Mika."
            "From the gruelling training to the frantic rush on some elusive secret mission to an ancient fort in Demorai territory."
            "As I spoke of watching Borras' body dissolve screaming beneath the splash of acid, the sinews snapping as the bone dissolved into slush, Mika's face turned paler and paler."
            "I recounted Duprey and Kira's deaths, along with the screaming, agonizing remainder of the scouts at the fort."
            $ LocFlush()
            show black:
                alpha 0.6
            show mika at center
            with dissolve
            MIKA @scared "I ..."
            MIKA @scared "That's horrible."
        "{i}Tell Mika the abbreviated story, sparing the worst details*{/i}":
            scene black 
            with dissolve
            "I did my best to omit the goriest parts of the story, recounting the details as best as I could to Mika."
            $ LocFlush()
            show black:
                alpha 0.6
            show mika at center
            with dissolve
            MIKA @sad "... It must have been pretty awful."
            MC @talk "Trust me."
            MC @serious "{i}I'm sparing you the worst.{/i}"
    #Both routes continued 
    scene black 
    with dissolve
    "After recounting the details to Mika, she seemed to relax somewhat, as though all of this was easier now that I'd told her of my terrible experiences."
    $ LocFlush()
    show black:
        alpha 0.6
    show mika at center
    with dissolve
    MIKA @sad "{i}...You can't tell anyone, please.{/i}"
    MC @talk "Does Sister Divine know this secret?"
    MIKA @sad "No, only Zara and Jana know."
    MC @talk "I need you to talk to me."
    MIKA @sad "..."
    MIKA @sad "I wasn't always l-like this."
    MIKA @sad "I wasn't always so afraid."
    MC @talk "Mika... What happened?"
    MIKA @sad "... When I was younger, about a year {i}before{/i} I joined the Mages of Palam at thirteen, I had this..."
    MIKA @sad "{i}Group of friends.{/i}"
    "Mika smiled faintly."
    MIKA @smile "There were five of us in total."
    MIKA @smile "We all talked about how we'd somehow form an adventure party of our own one day when we grew up."
    "Mika's fingers gently rubbed against the cup."
    MIKA @sad "{i}We... We just didn't want to wait that long.{/i}"
    MIKA @sad "We managed to find the entrance to this, {i}ancient dungeon{/i} hidden behind a clay wall in an old cavern we used to play in."
    MIKA @sad "Rather than let the adults know what we'd found... I ... {i}I made a terrible mistake.{/i}"
    MIKA @sad "{b}I wanted to prove we could be real adventurers... I wanted us to be brave.{/b}"
    MIKA @sad "{b}I talked everyone into it with silly thoughts of endless treasure.{/b}"
    MIKA @sad "And before I knew it... we were heading down there and exploring on our own."
    menu qst_little_lies_class_meet_5_menu_2:
        "Were you at least prepared?":
            MIKA @sad "We gathered what we had before re-grouping to try and take the dungeon."
            MIKA @sad "Some rations of food, an old short sword, a training staff I was using at the time."
            MIKA @sad "{i}... We were in over our heads.{/i}"
            jump qst_little_lies_class_meet_5_menu_2
        "Surely you must have realized how dangerous a dungeon like that could be?":
            MIKA @shock "We-"
            MIKA @sad "We had all heard the stories."
            MIKA @sad "But you know how at that age, the thought of actually dying seems like such an impossible, far away thought."
            MIKA @sad "And we were so desperate to be just like our heroes..."
            jump qst_little_lies_class_meet_5_menu_2
        "Then what happened?": # Continues on the main story 
            pass
    MIKA @sad "We descended deeper into the dungeon."
    MIKA @scared "{i}... It didn't take long for everything to spiral into a nightmare.{/i}"
    MIKA @sad "There were ... {i}These things down there.{/i}"
    MIKA @sad "{i}It was almost like they were waiting for us.{/i}"
    #Cut to CG showing the teens being killed 
    # $ AutoMus(False)
    # $ PlayMusic("audio/music/42_Flashback.mp3")
    scene black
    with dissolve
    URAH "THERE'S TOO MANY OF THEM!"
    TALI "HELP US, MIKA!"
    JARL "Use your magecraft! Help us!!"
    #Cut second CG showing Mika Frozen still in fear 
    show cg_mika_backstory_1 with dissolve
    URAH "MIKA! DON'T JUST STAND THERE! HELP-"
    URAH "URGHHHHH...!!"
    JARL "Urah!"
    #Close up on Mika's eyes - MIKA CAN SEE HER FRIEND BEING DEVOURED 
    show cg_mika_backstory_2 with dissolve
    URAH "AHHHHHHH! G-GET IT OFF OF ME! GET IT-"
    play sound2 "audio/cfx/massive_bone_crack.ogg"
    URAH "Grghhhhhhhh...!!"
    TALI "URAH! NO!"
    TALI "Mika! Please!"
    TALI "DO SOMETHING!"
    #SHOW MIKA RUNNING AWAY - ABANDONING THE OTHERS TO THEIR FATE 
    scene black with dissolve
    JARL "MIKAAAAAAAAAAA!"
    JARL "DON'T LEAVE US! DON'T-"
    #CUT BACK TO TAVERN 
    $ LocFlush()
    show black:
        alpha 0.6
    show mika sad at center
    with dissolve
    MC @sad "...Mika."
    MIKA @sad "I fled from the dungeon, and when I told my parents about it, we packed up to leave that night before anyone realized the others were missing."
    MC @surprised "What, why?"
    MIKA @sad "Because they thought I'd either be blamed for what happened, or the mages of Palam would finally find me and take me away."
    MIKA @sad "So, we left."
    MC @sad "... That's a lot of guilt to carry around this whole time."
    MIKA @sad "I didn't just walk my friends to their deaths..."
    MIKA @sad "I abandoned them, I failed them."
    MIKA @sad "You have no idea what it means to be a coward."
    MIKA @sad "Every time I try and fight, it's like I'm the same, helpless thirteen-year-old again ... {i}watching everyone die around me.{/i}"
    menu qst_little_lies_class_meet_5_menu_3:
        "You were a child...":
            MIKA @sad "I abandoned my friends."
            MIKA @sad "{i}I can still remember their screams...{/i}"
        "You were... But I'll make you strong.":
            "I reached down to tilt Mika's chin up towards me, and as I did so, her eyes looked up starrily towards me."
            MIKA @shock "I ... I'd like that."
            MIKA @cry "I'd like that a lot!"
    #Both routes continued 
    MC "(I'm going to need to be considerate next time of what happened to Mika before... This may take some time.)"
    MC @smile "Now, tomorrow's a new day, and we'll have to work hard to help you overcome what happened. Do you understand, Mika?"
    MIKA @sad "M-Mmm, yes. I understand."
    MC @talk "In the meanwhile, though..."
    MC @smile "What's say you and I finish this wine?"
    "Mika smiled warmly."
    MIKA @smile "T-That sounds nice..."
    #Brief fade to black
    scene black 
    with dissolve
    "...After slowly making our way through the bottle as the time dragged on, Mika opened up more and more about her life to me."
    $ AutoMus(True)
    $ AutoAmb(True)
    $ TimeAdvTo(TIME_MIDNIGHT)
    with dissolve
    "Finally, as the evening dragged on, it was time to take her home."
    $ LocFlush()
    show mika at center
    with dissolve
    MIKA @drunk "T-Thank you for -"
    MIKA @drunk "{i}*Hiccup!*{/i} this evening."
    MIKA @drunk "It's really helped me just to talk about what happened with someone who actually understands."
    if QstTheMagesPath().AvertedGazeDuringBPScene == True:
        "Mika nearly slipped, spilling some of her drink onto her dress."
        MIKA @sad "Oh no..."
        MC @smile "I think you've had more than enough."
        MC @smile "Come, let me walk you back to the tower."
        $ LocSet("novaras_palam_dorm")
        $ LocFlush(fade)
        "I gently helped lower the drunken mage down onto her bed."
        MIKA "Thankhhh..."
        MIKA "Yhouuu...."
        "Her words trailed off as she quickly dozed off into a drunken haze."
        show mc at left with dissolve
        MC "(Hopefully now, we can start moving forward with her training properly.)"
    else:
        "As Mika leaned over to press her hands onto my chest, she slipped slightly, spilling her drink as she pulled back aghast."
        MIKA @shock "I - I'm so sorry!"
        MC @talk "It's fine."
        MC @smile "But I think someone's had enough to drink."
        MIKA @blush "M-Maybe..."
        MIKA @drunk "Walking feels k-kinda funny right now, I'm not sure I'm gonna be able to-"
        "I swept Mika up into my arms with ease." # MC pick-up Mika in arms
        MIKA "O-Oh!"
        MC "Come on, let's get you home."
        MIKA "Y-Yes daddy."
        MIKA "I mean, uhh! Yes s-sir!"
        scene black with dissolve
        "I raised an eyebrow down towards the blushing Mika, who shyly averted her gaze and smiled as I carried her back to the tower."
        $ LocSet("novaras_palam_dorm")
        $ LocFlush(fade)
        "Back in the girls' dorm, I placed her down to rest in her bed before leaving the room quietly."
    $ CharAddRelEntry("mika", "append")
    $ CharChangeRel("mika", 1)
    $ QstComplete(QstLittleLies)
    $ LocEnter()