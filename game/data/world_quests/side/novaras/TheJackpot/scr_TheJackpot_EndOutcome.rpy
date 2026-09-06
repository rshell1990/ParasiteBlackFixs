label qst_jackpot_return_from_bd:
    if config.developer:
        "DEV-ONLY: set barati game outcome to?"
        menu:
            "pass (change nothing)":
                pass
            "won":
                $ QstTheJackpot().LostBDSolo = False
            "lost": 
                $ QstTheJackpot().LostBDSolo = True
                "DEV-ONLY: winward alive?"
                menu:
                    "pass (change nothing)":
                        pass
                    "yes":
                        pass
                    "no (killed)":
                        $ QstTheJackpot().MrWinwardDead = True
    $ GoalComplete(QstTheJackpot, 100)

    if QstTheJackpot().LostBDSolo:
        if QstTheJackpot().MrWinwardDead == True:
            jump qst_jackpot_outcome_murder_1
        else:
            jump qst_jackpot_lost_outcome_root
    else:
        jump qst_jackpot_won_outcome_1

label qst_jackpot_lost_outcome_root:
    $ LocFlush()
    show mr_winward at center_f
    show mrs_winward at right_f
    with dissolve
    show mc at left with easeinleft
    "Upon entry into the store, I was immediately preyed upon by both Mr and Mrs Winward."
    MR_WINWARD @angry "Well, well well!"
    MR_WINWARD @angry "Look who decided to show up!"
    MRS_WINWARD @angry "Don't blame him! Going to that place was YOUR decision!"
    MR_WINWARD @angry "Nevermind that!"
    MR_WINWARD @think "I bet everything we had on that game..."
    MR_WINWARD @sad "If we don't do something... We... We may have to sell the store."
    MRS_WINWARD @shock "WHAT?!"
    MR_WINWARD @sad "It's... a possibility."
    MR_WINWARD @sad "I borrowed a few small loans on-top and-"
    MRS_WINWARD @angry "I COULD KILL YOU!!"
    MR_WINWARD @shock "H-Hold on now!"
    MR_WINWARD @think "Uhh..."
    menu:
        #REQUIRES 'MIND-GAMES' PERK - NETORI/CUCKOLD ROUTE
        "{i}*Use your powers to convince Mr Winward to be happy with what he has{/i}*" (Req_Perk = "perception_warp"): 
            $ QstTheJackpot().Outcome = "control"
            jump qst_jackpot_outcome_control

        #SHARING/PIMPING ROUTE
        "{i}*Propose Kionni uses her body to make coin*{/i}": 
            $ QstTheJackpot().Outcome = "pimp"
            jump qst_jackpot_lost_outcome_pimp_share

label qst_jackpot_won_outcome_1:
    $ LocFlush()
    show mr_winward at right_f
    show mrs_winward at center
    with dissolve
    show mc at left with easeinleft
    MRS_WINWARD @scared "Where were you?!"
    MR_WINWARD @happy "Heh heh heh! Would you relax, woman?"
    MR_WINWARD @happy "Your little friend here and I managed to win big!"
    show mrs_winward at blurin, center_f
    MRS_WINWARD @shock "You... {i}You... did?{/i}"
    MR_WINWARD @angry "Didn't ya just hear me?"
    MR_WINWARD "From now on, things will be better around here!"
    MRS_WINWARD @shock "What do you mean?"
    MR_WINWARD @happy "Heh heh, you'll see soon enough..."
    MR_WINWARD "For now though, I need to lay down for a while..."
    "As Mr Winward past by Kionni, he suddenly stopped, gently putting his hand on her shoulder."
    MR_WINWARD "Oh... You mind keeping our friend here {i}company{/i} again?"
    show mr_winward at blurin, right
    hide mr_winward with easeoutright
    "Mrs Winward blushed profusely as Mr Winward stumbled on by into the bedroom, slamming the door behind him."
    show mrs_winward at cright_f with easeoutright
    show mc at cleft with easeinleft
    MC @think "...We don't need to-"
    MRS_WINWARD @embarr "N-No... I... I would like that with you."
    MRS_WINWARD @embarr "I just wasn't expecting, um... {i}this{/i}."
    "As I stepped closer towards her, she gently pressed her index fingers together, taking a shy step back."
    MRS_WINWARD @embarr "Do you mind if I change into something more... {i}interesting?{/i}"
    MC @smile "Interesting you say?"
    MC @lewd "Be my guest."
    show mrs_winward at blurin, cright
    hide mrs_winward with easeoutright
    "As Mrs Winward hurried into one of the backrooms, I waited patiently as I heard her undressing only a few feet away."
    MRS_WINWARD "...Oh my."
    MC @think "Mrs Winward?"
    MRS_WINWARD "P-Promise you won't laugh!"
    MRS_WINWARD "Oh gods..."
    MC  "I won't laugh, now come out..."
    $ CharSetClothes("mrs_winward", "cowl")
    show mrs_winward at cright_f with easeinright
    "Slowly, Mrs Winward appeared sheepishly from around the corner, blushing profusely."
    MRS_WINWARD @embarr "I... Oh gods, what am I doing wearing this?"
    MRS_WINWARD @embarr "I must look ridiculous."
    "As I felt my cock harden in excitement, I stepped closer towards her once again like a predator ready to pounce."
    MRS_WINWARD @blush "...O-Oh, I haven't been looked at like that for quite some time."
    MRS_WINWARD @lewd "S-So you {i}do{/i} like what you see?"
    MC @lewd "I do... {i}I very much do.{/i}"
    "As the tension in the air thickened, Mrs Winward, now slightly more confident, turned to wave her round butt towards me, gently slapping it."
    MRS_WINWARD "W-Well then, what are you waiting for young man?"
    MRS_WINWARD "This fat ass isn't going to fuck itself!"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    scene mrs_winward_doggywall_cow_nopreg_idle_solo with dissolve
    $ Pause()

    "Aligning myself behind Mrs Winwards soft, large rump, she lightly rubbed her butt up against my manhood as she bit down on her lower lip."
    MRS_WINWARD "Is that big cock all for me, deary?"
    MRS_WINWARD "Fufu {image=[ICON.HEART]} Your cock is so wonderfully huge and thick dear, you might need to take it easy on me!"
    "As her wetness brushed up against me along with her pubic hair, I knew what Mrs Winward needed, and I wasn't going to waste anytime giving it to her!"
    "Grabbing her hair and pulling, she gasped as she felt my cock plunge deeply into her tight, wet hole."
    
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)
    scene mrs_winward_doggywall_cow_nopreg_slow_solo with dissolve
    $ Pause()

    MRS_WINWARD "H-Hmhmmffhhh!!"
    "Slowly, I began to thrust my cock in and out of Mrs Winward's pussy."
    "Her ass rippled with every thrust as I squeezed my free hand on her round ass for better grip, feeling the fat slip between my fingers."
    MRS_WINWARD "D-Dear! Ahh!"
    MRS_WINWARD "You feel so - Mhmm! Big!"
    "Hot moans escaped Mrs Winward's lips as her legs began to tremble whilst my cock continued to plunge in and out of her tight clutching hole."
    "As her wet pussy grew more accustomed to my member, I began to move faster."
    "The sounds of sweet flesh colliding grew louder and more frequent as Mrs Winward's guttural moans filled the room."
    MRS_WINWARD "Ahh! Ahh! Mhmfghh! C-Careful! You're-"
    MRS_WINWARD "Oooooooooh!! {image=[ICON.HEART]}"
    "Her sweet groans of pleasure became more frequent as I took Mrs Winward from behind."
    "I wondered what Mr Winward would think if he ever saw his wife's lewd expressions as she felt my cock fill her up properly?"
    MC "Have you ever been fucked this deeply, Mrs Winward?"
    MRS_WINWARD "M-Mhhfhhhgh!"
    MRS_WINWARD "I-It's like you're - Hrghhh! Re-shaping all my insides!"
    MC "That doesn't answer the question!"
    MRS_WINWARD "A-Ahhh! N-No! I've never even SEEN anyone bigger than you!"
    "Satisfied with her answer, I slammed my cock to the hilt, determined to fuck her senseless so she'd know for sure {i}who{/i} her body belonged to from now on..."

    $ PlaySexFx("audio/sex_sounds/forgean_100.ogg", 1)
    scene mrs_winward_doggywall_cow_nopreg_fast_solo with dissolve
    $ Pause()

    MRS_WINWARD "M-MHHHHHHHHHFFFHH!"
    MRS_WINWARD "P-Please! {i}*Huff*{/i} Mhfghhh!"
    MRS_WINWARD "F-Fill me up!"
    MRS_WINWARD "I don't know how much more I can - Mhhhfhh! Take!"
    "I continued to have my way with her for a little while longer, enjoying the feeling of her pussy squeezing my member with desperation to bring me to climax."
    "Eventually, she got her wish."
    "As my balls began to tighten and rise, my cock, still plunging mercilessly in and out of her now trembling body, began to feel increasingly ready for release."
    MRS_WINWARD "{i}*Huff*{/i} F-Finish dear! {i}*Huff*{/i} I beg you! P-Please!!"
    "Giving her what she wanted, I dug my hand deep into the soft flesh of her large, round ass and slammed deeply into her."
    "Grunting loudly, I flooded Mrs Winward's womb with my hot, thick seed."
    MC "H-HRGHHHHH!!"

    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    $ ReduceInfectionFromSex("mrs_winward")

    $ UnlockGalFlag("mrs_winward", "doggy_wall", "no_cuck")
    $ UnlockGalFlag("mrs_winward", "doggy_wall", "cow")
    $ UnlockGalFlag("mrs_winward", "doggy_wall", "nopreg")
    $ UnlockGalFlag("mrs_winward", "doggy_wall", "vag")

    scene mrs_winward_doggywall_cow_nopreg_finish_solo with flash
    $ Pause()

    $ UnlockGalSceneAndGrantXp("mrs_winward", "doggy_wall")

    "Mrs Winward gasped as she felt the rush of warm fluid pouring into her."
    "Her eyes rolled back as she trembled and nearly collapsed back into my arms."
    "I held her up as I continued to pump my load into her body."
    "Only a soft whimper escaped her lips as I held her body upright in my arms."
    MRS_WINWARD "M-Mhmmm..."
    MRS_WINWARD "Oh gods...That was..."
    MRS_WINWARD "...{i}Oh my...{/i}"
    "Slowly, As I unsheathed my cock from Mrs Winward's now loosened hole, she shuddered as my seed spilled out of her onto the floor." 
    $ LocFlush()
    show mc at cleft
    show mrs_winward at cright_f
    with dissolve
    "Letting go of her hair, her legs shook and buckled as she slid down onto the floor in a puddle of our cum."
    "Catching her breath, I slowly helped her back to her feet as she sweatily looked towards me, brushing her now ruffled hair over her shoulder."
    "Licking her lips, she giggled."
    MRS_WINWARD @lewd "{i}*Phew!*{/i}"
    $ AutoMus(True)
    MRS_WINWARD @lewd "You really put this old lady through her paces back there!"
    MRS_WINWARD @lewd "I had no idea it could feel so... so..."
    "She giggled, playfully tapping at my chest."
    MC @smile "Good?"
    MRS_WINWARD @lewd "Mmmm, {i}incredible.{/i}"
    MRS_WINWARD @lewd "Come here tomorrow, {i}deary,{/i} I'm sure we all have so much to talk about now."
    MC @smile "I'm sure we will."
    "My smile melted her, and shyly, she giggled as she nervously looked away."
    MRS_WINWARD @blush "G-Get home safe now, deary, I don't think I'll be able to keep standing much longer."
    MRS_WINWARD @lewd "These old bones need some rest after what you just put them through."
    MC @smile "I shall return soon, goodbye... Kionni."
    scene black with dissolve
    "With trembling legs, Mrs Winward saw me out, my cum still seeping out of her and running down her leg onto the floor as she did so."
    $ CharSetClothes("mrs_winward", "normal")
    $ LocSet("novaras_dist_house")
    $ LocFlush()
    show mc at cright_f
    with dissolve
    MC "(Hmm... Mr Winward mentioned he had some kind of plan.)"
    MC "(As long as he doesn't interfere with me and Kionni's {i}fun{/i} he can do as he likes...)"
    hide mc with easeoutleft
    $ GoalShow(QstTheJackpot, 110)
    $ QstSetProgress(QstTheJackpot, 110)
    $ QstSetDelay(QstTheJackpot, 1)
    $ LocEnter()

label qst_jackpot_won_outcome_2:
    $ GoalComplete(QstTheJackpot, 110)
    $ LocFlush()
    show mr_winward at right_f
    show mrs_winward at center
    with dissolve

    show mc at left with easeinleft

    "Upon entry into the store, I was immediately preyed upon by both Mr and Mrs Winward."
    MR_WINWARD  "Ah, there you are."
    MRS_WINWARD @lewd "H-Hello again, deary."
    MR_WINWARD @angry "Deary this, deary that, he fucked you didn't he?"
    MR_WINWARD @angry "He's not some little boy is he!"
    MRS_WINWARD @angry "There's something {i}little{/i} around here and it isn't him."
    MR_WINWARD @angry "BAH! Listen here you old-"
    MC @angry "ENOUGH!"
    MR_WINWARD "..."
    MRS_WINWARD "..."
    MC @serious "You wanted to talk about something, right?"
    MC @serious "Get to the point and stop arguing!"
    MR_WINWARD  "Well, now that I have the coin, it's time I restored this households name to it's former glory!"
    MRS_WINWARD @think "What does that mean?"
    MR_WINWARD  "It's simple, there's another game soon, and once I-"
    MRS_WINWARD @angry "NO! Absolutely not!"
    MR_WINWARD @angry "BAH! Woman! What are you blabbering on about now?"
    MR_WINWARD @angry "With just one more game, I can restore our family name and-"
    MRS_WINWARD @angry "It's never just {i}one{/i} more game with you!"
    MRS_WINWARD @angry "I've had enough!"
    MRS_WINWARD @angry "If you wanna pursue this, you can do it without me!"
    MR_WINWARD @angry "Who do you think you are?"
    MR_WINWARD @angry "I WON THAT COIN! I GET TO DECIDE WHAT HAPPENS TO IT!"
    MRS_WINWARD @angry "You didn't win anything! {i}He{/i} did!"
    MRS_WINWARD @angry "And without him, you'd have lost it all like you always do!"
    menu:
        # invest stuff
        "{i}*Convince Mr Winward to invest in the business they have currently*{/i}" (Req_Barter = 7):
            $ QstTheJackpot().Outcome = "invest"
            jump qst_jackpot_won_outcome_invest

        # REQUIRES 'MIND-GAMES' PERK - NETORI/CUCKOLD ROUTE
        "{i}*Use your powers to convince Mr Winward to be happy with what he has{/i}*" (Req_Perk = "perception_warp"):
            $ QstTheJackpot().Outcome = "control"
            jump qst_jackpot_outcome_control

        # DIVORCE
        "{i}*Don't intervene.*{/i}":
            $ QstTheJackpot().Outcome = "divorce"
            jump qst_jackpot_won_outcome_divorce

label qst_jackpot_won_outcome_divorce:
    MR_WINWARD @angry "You... YOU BITCH!"
    MRS_WINWARD @angry "...Get out."
    MR_WINWARD @shock "...What?"
    MRS_WINWARD @angry "GET OUT!"
    MRS_WINWARD @angry "We're finished! Do you hear me? FINISHED!"
    "Mr Winward froze, not believing what he was hearing."
    MR_WINWARD @shock "You... You want me to go?"
    MRS_WINWARD @sad "I can't keep doing this anymore with you."
    MRS_WINWARD @cry "Just... Just go already!"
    "As Mrs Winward began to cry, Mr Winward, perhaps finally accepting that, he truly had gone too far, simply nodded."
    MR_WINWARD @sad "...I'll uh, I best be going then..."
    hide mr_winward with easeoutleft
    "Without another word, he shuffled his way out of the store, closing the door sadly behind him."
    MRS_WINWARD @cry "{i}*Sniff*{/i} I just... I just can't do it with him anymore."
    MC @sad "Kionni..."
    MRS_WINWARD @cry "Just go please?"
    MRS_WINWARD @cry "I... I need some time alone."
    scene black with dissolve
    $ LocSet("novaras_dist_house")
    jump qst_jackpot_over

label qst_jackpot_outcome_control:
    MC @serious "Mr Winward, I have an idea."
    MR_WINWARD @angry "What is it?"
    "Suddenly I reached out and grabbed a hold of Mr Winward's head, he panicked and squirmed for a moment, struggling against my grasp as Kionni gasped in horror."
    MRS_WINWARD @scared "W-What are you doing?!"
    MR_WINWARD "AHH! LET GO OF ME! LET ME GO!"
    $ AutoMus(False)
    stop music fadeout 0.5
    $ AutoAmb(False)
    play ambience "audio/ambience_scenes/whispers.ogg"
    play sound "audio/cfx/darkness_erupt.ogg"
    scene cg_winward_control with flash
    "From one of my palms, a small centiped like tentacle crawled out of the flesh and worked its way through Mr Winward's ear."
    MR_WINWARD "AHH! WHAT IS THAT! IT'S CRAWLING! IT'S-"
    "Suddenly, Mr Winward gasped and all of his resistance stopped."
    $ LocFlush()
    show mc at right_f
    show mr_winward at center_f
    show mrs_winward at left
    with dissolve
    "I could feel it inside of him, now connected to his mind as he waited slack-jawed, eyes staring off into nothing."
    BLACK "({i}Command him.{/i})"
    "A wicked, perverse thought crossed my mind."
    MC @smile "...You know what I think, Mr Winward?"
    MC @smile "I think watching me fuck your wife drives you wild with lust."
    "Kionni blushed profusely, watched bewildered as to what was happening."
    MRS_WINWARD @shock "What... What's happening?"
    MRS_WINWARD @shock "Are you casting some kind of craft on him?"
    "I continued on, ignoring Kionni."
    MC "I think from now on, you'll be happy as long as Kionni is happy, and you won't worry about coin anymore as long as the bills can be paid."
    MC "In fact, you'll be far more concerned with your {i}real passion.{/i}"
    MC "{i}...Masturbating to the thought of me fucking your wife.{/i}"
    MC "That's now the main focus of your goals, finding new and exciting ways to get my cock inside of her."
    MC "Do you understand?"
    "Mr Winward nodded, and once I was done, he shook his head as if coming out of a daze."
    $ AutoMus(True)
    $ AutoAmb(True)
    MRS_WINWARD @shock "D...Dear?"
    MRS_WINWARD @shock "Are you okay?"
    MR_WINWARD @happy "Ho ho! I've never been better my love!"
    MR_WINWARD @happy "In fact, I think I might go out and celebrate with a drink tonight!"
    "Kionni seemed perplexed by his sudden change in attitude, glancing towards me before forcing an awkward smile."
    MRS_WINWARD @happy "Umm, if you wish to dear, t-that's fine by me."
    MR_WINWARD @happy "How about I try find you some lovely new clothes while I'm out?"
    MR_WINWARD @lewd "The thought of him tearing off your dress and fucking you silly is already making me hard!"
    "Unable to believe what she was hearing, Kionni's eyes glanced towards me in disbelief, then back towards her goofily grinning husband."
    MRS_WINWARD @shock "W-What did you say?!"
    MR_WINWARD @happy "Huehue! Come here sweetie."

    hide mc
    hide mr_winward
    hide mrs_winward
    show cg_winward_tits at center
    with dissolve

    "Nervously, Kionni stepped closer towards her husband, and as she did so, he grabbed and tugged down her dress, exposing her large breasts as she gasped in shock." 
    "Holding them up in both hands, he turned to look towards me."
    MR_WINWARD "What do you think? Nice and ripe aren't they?"
    MRS_WINWARD "D-DEAR! W-WHAT DO YOU THINK YOU'RE DOING?!"
    MR_WINWARD "Showing him your lovely huge tits dear!"
    MR_WINWARD "He really should shove his cock between them more often I think!"
    MRS_WINWARD "W-What has gotten into you?!"
    MR_WINWARD "Huhue! I haven't been this happy in years!"
    MR_WINWARD "Turn around dear."
    MRS_WINWARD "W-What?!"
    hide cg_winward_tits
    show cg_winward_ass at center
    with dissolve

    "Spinning Kionni around, she blushed profusely from embarrassment as he hiked up her dress for me, giving me an eyeful view of her fat ass." 
    "The old man grinned as he showed off his wife's rear towards me."
    MR_WINWARD "Plenty of cushion for the pushin'!"
    MRS_WINWARD "Oh g-gods...!"
    MRS_WINWARD "This is so shameful!"
    MR_WINWARD "Do you think she'll still be good for breeding some young'uns with you?"
    "Finally having enough, Kionni managed to pull herself away from Mr Winward's grasp, re-adjusting her dress as she stood there flustered and confused."
    hide cg_winward_ass 
    show mc at cright_f
    show mrs_winward at cleft_f
    show mr_winward at left
    with dissolve

    MR_WINWARD "Hehehe! My wife sure is the cutest sometimes!"
    MR_WINWARD "Anyway, I'll see you both later!"
    show mr_winward at blurin, left_f
    hide mr_winward with easeoutleft
    "Happily humming to himself, Mr Winward closed the store door behind himself gently, beaming with pride."

    show mrs_winward at blurin, cleft

    MRS_WINWARD @shock "He... "
    MRS_WINWARD @think "What did you do to him?"
    MRS_WINWARD @think "You never said you possessed magecraft!"
    MC @think "It's uh, a long story..."
    MRS_WINWARD @sad "I... I don't know what you've done to him, but..."
    MRS_WINWARD @sad "Is this right? You've... {i}changed him.{/i}"
    MC  "If he carried on the path he was on, he would have gotten himself killed and dragged you further into financial ruin."
    MRS_WINWARD @sad "I-"
    MRS_WINWARD @sad "I suppose you're right."
    MRS_WINWARD @embarr "...Where do we go from here?"
    MC @smile "To the bedroom, of course."
    "Kionni's hot breath trembled with excitement as she heard those words."
    MRS_WINWARD @shock "I... I have some work I need to finish today."
    MRS_WINWARD @blush "B-But tomorrow, we could-"
    MC @smile "Then I shall see you tomorrow."
    MRS_WINWARD @lewd "M-Mmm... That sounds nice."
    scene black with dissolve
    $ LocSet("novaras_dist_house")
    jump qst_jackpot_over

label qst_jackpot_won_outcome_invest:
    MC "Why not invest more in the hide tanning business you're already in?"
    show mr_winward at shake
    MR_WINWARD @angry "The business is too slow!"
    MRS_WINWARD @shock "That's not true!"
    MRS_WINWARD @sad "It only seems slow because I'm going as fast as I can!"
    MC @think "Why not invest in an apprentice?"
    MR_WINWARD @think "...An apprentice?"
    MC "You could pay them half the rate of a professional, train them up and increase production output."
    MR_WINWARD @think "Hmm..."
    MR_WINWARD "Perhaps... We could look into it."
    MR_WINWARD @think "Do you really think an apprentice will make much of a difference?"
    MRS_WINWARD "I could double or even triple our income with a competent pair of hands by my side."
    MR_WINWARD "... Very well."
    MRS_WINWARD @shock "Really?"
    MR_WINWARD "Why not? A good idea is a good idea."
    "Kionni beamed a bright smile."
    MRS_WINWARD @happy "Oh dear! This will be wonderful!"
    MR_WINWARD @happy "I suppose it will, won't I?"
    "Mr Winward paused for a moment, looking back and forth between his wife and me."
    "Upon catching my gaze, Mrs Winward blushed once again awkwardly, pushing her hair over her shoulder."
    show mr_winward at nod
    MR_WINWARD "...I suppose from the way she keeps looking at you like that, my wife here still wants to keep seeing you."
    MRS_WINWARD @shock "I...!"
    MR_WINWARD "No point trying to deny it."
    MR_WINWARD "Look dear, let's not pretend things haven't changed between us these last few years."
    MR_WINWARD "So, how about this, as long as you ignore any of my... {i}indiscretions,{/i} you two keep seeing each other?"
    MRS_WINWARD @think "...I can live with that."
    MR_WINWARD @happy "Good."
    MR_WINWARD "Is that good with {i}you?{/i}"
    show mc at nod
    "I nodded."
    MR_WINWARD "Well then, that settles that!"
    MR_WINWARD @happy "If you both'll excuse me, I'm going to go grab a drink to celebrate!"
    MR_WINWARD "...Have fun while I'm gone."
    hide mr_winward with easeoutleft
    "As Mr Winward left, closing the door behind him, the air was palpable between me and Kionni."
    show mc at cleft
    MC @smile "...Should we-"
    MRS_WINWARD @embarr "I... I need to finish some work up here still."
    MRS_WINWARD @blush "...But perhaps tomorrow when it comes dark you could return?"
    MC @smile "Then I shall see you tomorrow."
    MRS_WINWARD @blush "U-Until then..."
    scene black with dissolve
    $ LocSet("novaras_dist_house")
    jump qst_jackpot_over

label qst_jackpot_lost_outcome_pimp_share:
    MC "If I might make a suggestion..."
    "The two of them paused their bickering to look towards me."
    MC @serious "Why don't you kill two birds with one stone?"
    MC "Your wife is desperate for some... {i}affection.{/i}"
    MC "And you are desperate for more coin."
    "There was a long pause before it dawned on the two of them the meaning behind my words."
    MRS_WINWARD @shock "You... YOU CAN'T BE SERIOUS!"
    MR_WINWARD  "I agree, you might be some kind of strange degenerate, but you really think most men will be interested in {i}her?{/i}"
    MRS_WINWARD @angry "You're supposed to defend my honor!"
    MRS_WINWARD @angry "AND WHAT DO YOU MEAN THEY WOULDN'T BE INTERESTED IN ME?!"
    MR_WINWARD @angry "Look at us! We're old woman! What kind of young man is picking you over some tight ass wench?"
    "Mrs Winward coiled her fists into tight balls, gnashing her teeth as she scowled towards her husband."
    MR_WINWARD @think "Do you really think they'll be enough men interested in her?"
    MC @smile "Of course."
    MR_WINWARD  "Hmm..."
    MR_WINWARD @think "And are you willing to manage her and keep her safe?"
    MC  "Yes, I'd keep an eye on her for a small cut."
    MRS_WINWARD @angry "You can't be serious!"
    MRS_WINWARD @angry "Not only would you let me sell my body, you'd let someone else {i}'manage'{/i} me?!"
    MR_WINWARD  "Look woman, don't you think he has a point?"
    MR_WINWARD  "When was the last time we fucked?"
    MRS_WINWARD @scared "...!"
    MR_WINWARD  "Exactly."
    MR_WINWARD  "This could be a way to give us what we both want."
    MRS_WINWARD @sad "...You really care about me that little?"
    MR_WINWARD @angry "Of course I still care for you woman!"
    MR_WINWARD @think "...That's why I know this is the best way."
    MR_WINWARD  "You'll be able to get your {i}needs{/i} met, and I'll be able to slowly rebuild our family's prestige quietly in the background."
    MRS_WINWARD @sad "I... I'll need to think about it."
    "Kionni's eyes met mine."
    MRS_WINWARD @sad 'Could you leave me and my husband alone to talk for a while?'
    MRS_WINWARD @sad "I think it's best we continue this conversation alone..."
    MC  "Very well, I shall return in a day or so."
    MRS_WINWARD @sad "Thank you."
    scene black with dissolve
    $ LocSet("novaras_dist_house")
    jump qst_jackpot_over

#################### MURDER 
label qst_jackpot_outcome_murder_1:
    $ QstTheJackpot().Outcome = "murder"
    show mrs_winward scared at cright_f
    with dissolve
    show mc at cleft with easeinleft
    "Upon entry into the store, I was immediately pressed upon by a panicking Mrs Winward."
    MRS_WINWARD @scared "W-Where is he?"
    MRS_WINWARD @scared "Where's my husband?"
    MC @sad "Mrs Winward, I-"
    MC @sad "I'm sorry, your husband ... He's ..."
    MC @sad "{i}He's gone.{/i}"
    "Mrs Winward's eyes began to tear up, her lips trembling in worry."
    MRS_WINWARD @scared "W-What do you mean {i}gone?{/i}"
    MC @talk "Some debt collectors cornered him, apparently he borrowed from the wrong people and didn't pay them back in time."
    MC @sad "I'm sorry... They decided to make an example of him."
    MRS_WINWARD @cry "Oh gods, he... We..."
    MRS_WINWARD @cry "I'll have to write to the children, I-"
    MRS_WINWARD @cry "Oh gods, please, just... Just leave me alone."
    MC "(I should probably not press her when she's like this.)"
    MC @talk "Very well, I'll come to check in on you soon."
    MRS_WINWARD @cry "{i}*Sniff*{/i} I just n-need to be alone..."
    scene black with dissolve
    $ Pause(0.5)
    $ LocSet("novaras_dist_house")
    $ LocFlush()
    show mc at cright_f
    with dissolve
    MC "(She's distraught... Did I really make the right decision there?)"
    BLACK "({i}Her husband had no regard for her and would have inevitably dragged her down.{/i})"  
    BLACK "({i}His removal guarantees her happiness in the long-run, her tears will not last.{/i})"
    MC "(I sure hope you're right...)"
    $ GoalShow(QstTheJackpot, 120)
    $ QstSetProgress(QstTheJackpot, 120)
    $ QstSetDelay(QstTheJackpot, 4)
    $ LocEnter()

label qst_jackpot_outcome_murder_2:
    show mc at cleft with easeinleft
    MC @talk "Mrs Winward? Are you here?"
    $ GoalComplete(QstTheJackpot, 120)
    MRS_WINWARD "Y-Yes... I'm here."
    show mrs_winward at cright_f with easeinright
    "From the back room, Mrs Winward slumped out to greet me."
    MRS_WINWARD @sad "Hello."
    MC @sad "How are you?"
    MRS_WINWARD @sad "...Fine."
    MC @think "Fine?"
    MRS_WINWARD @sad "{i}*Sigh*{/i} I can't pretend that in the end, there was much love left between us."
    MRS_WINWARD @sad "Nor can I pretend he was a good husband or even much of a father..."
    MRS_WINWARD @sad "But... He {i}was{/i} still my husband."
    MRS_WINWARD @sad "And there was a time he was a different man."
    MC @talk "You need to focus on yourself, Mrs Winward."
    MRS_WINWARD @sad "I know deary... It's just..."
    "Mrs Winward bites down on her lower lip."
    MRS_WINWARD @sad "{i}I'm a terrible wife.{/i}"
    MC @think "What?"
    MC @think "Why would you think that? You put up with, well, {i}him,{/i} for years!"
    MRS_WINWARD @sad "Because..."
    MRS_WINWARD @sad "The first two nights, I spent drinking myself into a stupor over him."
    MRS_WINWARD @sad "But by the third night... I .... I..."
    MRS_WINWARD @embarr "I stopped thinking about him."
    MRS_WINWARD @embarr "{i}B-Because all I could think about was you.{/i}"
    MRS_WINWARD @embarr "What kind of wife would do such a thing?"
    MRS_WINWARD @embarr "T-Thinking about another man like that when her husband hasn't even been buried yet!"
    MC @talk "You're still a woman with needs."
    MRS_WINWARD @sad "But... My husband-"
    MC @sad "Mistreated and abused you."
    MC @sad "He made you miserable, and you know it."
    MRS_WINWARD @sad "I know..."
    MRS_WINWARD @cry "I... I just need more time; he'll be buried three days from now."
    MRS_WINWARD @cry "I'm sorry, p-please... Just let me alone for now."
    MRS_WINWARD @cry "I need... {i}I need to think.{/i}"
    scene black with dissolve
    "Mrs. Winward ushers me out of the house, tears still streaming down her cheeks as she sadly closes the door behind her."
    $ LocSet("novaras_dist_house")
    $ LocFlush(dissolve)
    show mc at cright_f with easeinright
    MC "(This can't go on.)"
    BLACK "({i}Perhaps it would be wise to visit her the day her old mate is buried.{/i})"
    BLACK "(She will need... comforting.)"
    MC "(You make that sound ghoulish...)"
    BLACK "({i}Did we not slay him to claim her for ourselves?{/i})"
    BLACK "({i}Why does morality suddenly concern you now?{/i})"
    MC "(I... I killed him for her sake!)"
    MC "(He was a foul wretch.)"
    BLACK "{i}(Oh course... And removing this obstacle to claim his mate for ourselves was just a bonus, correct?{/i})"
    MC "(...L-Let's just drop it and move on.)"
    $ NoteUnlock("RomWinward_MurderVisitAtGraveyard")
    hide mc with easeoutleft
    jump qst_jackpot_over

#################### ALL ROUTES FALL INTO HERE
label qst_jackpot_over:
    $ QstComplete(QstTheJackpot)
    $ RomanceWinward().RomanceVariant = QstTheJackpot().Outcome
    $ RomanceWinward().CanEnterHouseAtNight = True
    $ QstSetProgress(RomanceWinward, 1)

    if RomanceWinward().RomanceVariant == "invest":
        $ NoteUnlock("RomWinward_VisitTomorrow")
        $ QstSetDelay(RomanceWinward, 1)
        $ QstStart(DialogueMrWinward)

    if RomanceWinward().RomanceVariant == "divorce":
        $ QstSetDelay(RomanceWinward, 6)
        $ NoteUnlock("RomWinward_VisitInAWeek")
        $ QstStart(DialogueMrWinward)

    if RomanceWinward().RomanceVariant == "control":
        $ NoteUnlock("RomWinward_VisitTomorrow")
        $ QstSetDelay(RomanceWinward, 1)
        $ QstStart(DialogueMrWinward)

    if RomanceWinward().RomanceVariant == "murder":
        $ QstSetDelay(RomanceWinward, 3)
        $ RomanceWinward().Murder_FirstGraveyardScene_IsAtGraveyard = True

    if RomanceWinward().RomanceVariant == "pimp":
        $ NoteUnlock("RomWinward_VisitTomorrow")
        $ QstSetDelay(RomanceWinward, 1)
        $ RomanceWinward().Pimp_DayPlayerCanGetHisCut = GetGameDay() + 14
        $ QstStart(DialogueMrWinward)

    $ LocEnter()