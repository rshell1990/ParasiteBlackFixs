label qst_jackpot_unicorn_barati:
    $ QstSetProgress(QstTheJackpot, 1, Silent = True)
    show mr_winward at right_f with dissolve
    show mc at left with easeinleft
    MR_WINWARD @angry "Urghh, what in the hells do you want, lad?"
    MR_WINWARD @angry "Can't you see me and some friends are about to play a couple of games of {i}Barati?{/i}"
    "Looking over towards Mr Winward's {i}friends,{/i} they seemed considerably younger than him, smiling and whispering amongst themselves."
    "When I focused in my senses on them, there was a distinct smell to them, a hint of blood on their knuckles and boots that they had tried to wash away and mask with vinegar."
    "Their eyes shifted as they glanced around the tavern, carefully on the lookout for anyone who might approach them."
    MC @serious "({i}Card sharks and swindlers.{/i})"
    BLACK "({i}Threat,{/i})"
    MC "If you play with them, you'll lose."
    MR_WINWARD @think "What are you talking about?"
    MC @angry "Can't you see they're working together? They're going to rip you off!"
    MR_WINWARD @angry "Bah! What do you know?"
    MR_WINWARD @laugh "Stay out of my way, boy, a fool like you'd be eaten alive in the games I play! Huehuehue!"
    "Laughing smugly to himself, the old man dragged himself over to the table to sit down."
    MC "(Fuck... This idiot is going to get himself robbed or worse.)"
    $ GoalComplete(QstTheJackpot, 0)
    BLACK "({i}They conspire to force the old man to bet beyond his funds, afterwards, they will likely inflict bodily harm on him.{/i})"
    BLACK "({i}Once they take him to a secluded spot, it would be our optimal time to intervene.{/i})" 
    menu:
        "I know my way around a game of Barati; I'll play against them myself.": 
            jump qst_jackpot_unicorn_ill_play_myself

        "I'll let the old man lose and protect him afterwards.": 
            hide mr_winward with easeoutright
            hide swindler with easeoutright
            jump qst_jackpot_unicorn_watchem_lose_then_protect

label qst_jackpot_unicorn_ill_play_myself:
    $ GoalShow(QstTheJackpot, 10)

    show mr_winward at center with easeoutleft
    show swindler at right with easeinright
    "Heading over towards their table, I pulled out a pouch of coins and dropped them down onto the table."
    MC @smile "Room for one more?"
    MR_WINWARD @shock "What do you think you're doing, lad?"
    MR_WINWARD @angry "Get off this table! You're not playing!"
    "The men looked around the table and nodded to each other, the leader of the group turned to smile towards me."
    SWINDLER "It's no concern of ours; join us..."
    scene cg_cardtable with dissolve
    "(Barati game is under construction!)"
    MR_WINWARD @shock "BUT HE-!"
    SWINDLER "As long as he has the coin to play, he can."
    "The group chuckled as the old man furiously sat back in his seat, mumbling beneath his breath."
    SWINDLER "Are you ready to begin, friend?"
    MC @smile "Of course, {i}friend.{/i}"
    menu:
        "(WIP) Win": # barati entry point
            $ LocFlush()
            show mc at left
            show mr_winward at center
            show swindler at right
            with dissolve
            jump qst_jackpot_unicorn_player_won_barati

        "(WIP) Lose":
            $ LocFlush()
            show mc at left
            show mr_winward at center
            show swindler at right
            with dissolve
            $ GoalFail(QstTheJackpot, 10)
            SWINDLER "Thanks for the coin, friends."
            MC "(Shit.)"
            MR_WINWARD @angry "Bloody fool! I told you this game was no good for you!"
            SWINDLER "Shall we keep playing, Mr Winward?"
            MR_WINWARD  "Aye, I've got the coin for a few more rounds!"
            MC  "You really shouldn't keep playing with them."
            MC @serious "They've nearly bled you dry."
            MR_WINWARD @angry "I'll do with my coin as I bloody wish!"
            hide mr_winward with easeoutright
            hide swindler with easeoutright
            MC @angry "...Very well then."
            MC "(Hm, well that didn't go to plan.)"
            MC "(Perhaps I should stick around though and see how the old man gets on?)"
            jump qst_jackpot_unicorn_watchem_lose_then_protect

label qst_jackpot_unicorn_player_won_barati:
    $ GoalComplete(QstTheJackpot, 10)
    SWINDLER "YOU CHEATED!"
    MC @smile "Now, now... You've lost, accept it."
    MR_WINWARD @shock "I ... I don't believe it!"
    MR_WINWARD @shock "By the gods, lad, how did you-"
    SWINDLER "Give us back our fucking coin before we-!"
    "As he reached for his blade, the group quickly Realized the entire tavern's eyes were drawn to the commotion."
    "One of the other bandits gently rested his hand on the ones shoulder and whispered something into his ear, as he did so, he let go of his blade quickly."
    hide swindler with easeoutright
    "The men departed, glaring at me as they passed by, leaving the coin on the table for me to collect."
    MC @think "(There's a chance they may be waiting outside to jump us.)"
    BLACK "({i}They will die.{/i})"
    BLACK "({i}But I can feel their scent moving further away from us... Perhaps they do not wish to draw any more attention than they already have.{/i})"
    MC  "(One can only hope so.)"
    show mr_winward at blurin, cright_f with easeoutright
    MR_WINWARD @shock "Ho ho! I can't believe it, lad!"
    MR_WINWARD @happy "{i}We{/i} sure showed them, eh?"
    MC @think "...{i}We?{/i}"
    MR_WINWARD @happy "{i}*Cough!*{/i} Well, uhh... I clearly threw them off their game!"
    MR_WINWARD  "So, how's it about it lad, what's my cut?"
    menu:
        "I'll give you back your buy-in and not a coin more.":
            $ tmpvar = "buy-in"
            MR_WINWARD @angry "BAH! Come on now!"
            MR_WINWARD @angry "Give us at least a few of those winnings, would ya?!"
        "Your cut is nothing. Fuck off.": 
            $ tmpvar = "nothing"
            MR_WINWARD @angry "Aw come on, lad! Don't be like that!"
            MR_WINWARD @angry "I ain't been nothing but nice to ya!"
    MC @think "Why would I give a single coin to you?"
    MC @angry "You've been nothing but a complete ass since we've met."
    MR_WINWARD @think "Uhh... Well, perhaps I have been a little hard on ya..."
    MR_WINWARD @shock "But perhaps I've got an idea that might interest you!"
    MC @think "...Go on."
    MR_WINWARD @happy "I've seen the way you looked at my wife's tits."
    MR_WINWARD @laugh "Don't know what you see in that used-up hag at this point, but how's about I uhh, {i}push{/i} her towards giving you some relief?"
    MC @serious "...Are you serious?"
    MR_WINWARD @happy "Course I am!"
    MR_WINWARD @happy "In return... I get some of those winnings, and you uhh...perhaps {i}help me out{/i} in my next game."
    MC  "You're planning to do this again?"
    MR_WINWARD @think "I am, with much higher stakes."
    MR_WINWARD  "I ain't tell the wife nothing, {i}but I have been making some small winnings here and there...{/i}"
    MR_WINWARD  "Been saving up for a high-stakes game."
    MR_WINWARD  "Figured though, could use some backup..."
    MR_WINWARD  "So, how about it? You interested?"
    MC @serious "...I'll think about it."
    MR_WINWARD @happy "Ahh! Knew you were a smart one! Don't worry, lad, you won't regret a thing!"
    MR_WINWARD @happy "Come around in a day or so once I've softened her up, fufu! Don't worry, I'll keep to my end of the deal!"
    "After handing over another hundred of the coins into Mr Winward's hand, he merrily made his way out of the tavern humming to himself."
    if tmpvar == "buy-in":
        $ PlayerAddItem("gold", 300)
    if tmpvar == "nothing":
        $ PlayerAddItem("gold", 500)
    $ tmpvar = {}
    show mr_winward at blurin, cright
    hide mr_winward with easeoutright
    show mc at center with easeinleft
    MC "(You wouldn't think he basically just offered up his wife's ass to us.)"
    BLACK "{i}(This male is weak, but he is convinced he is strong... Humans are... fascinating.){/i}"
    $ GoalShow(QstTheJackpot, 40)
    $ LocEnter()

label qst_jackpot_unicorn_watchem_lose_then_protect:
    "...Sure enough, I watched as Mr Winward lost hand after hand, the group playing against him, smirking as they obviously worked together."
    "Eventually, the game finally ended, and a defeated Mr Winward buried his face in his hands."
    "I watched carefully from the sides as they chatted back and forth a little, the smiles slowly fading from the gang members' faces as Mr. Winward no doubt explained he couldn't pay them."
    "Suddenly, by the scuff of his neck, Mr Winward was dragged outside the tavern."
    $ GoalShow(QstTheJackpot, 20)

    scene black with dissolve
    $ LocSet("novaras_dist_market")
    $ LocFlush(dissolve)
    show mc at cright_f
    "Pushing my way through the merry crowds blocking my way, I headed outside to see the old man was gone."
    MC @serious "(Which way did he go?)"
    BLACK "({i}North...{/i})"
    BLACK "({i}This way...{/i})"
    scene black with dissolve
    $ LocSet("novaras_dist_pleasure")
    $ LocFlush()
    show mr_winward at right
    show swindler at cright_f
    with dissolve
    show mc at left
    "Heading down one of the many cramped, dark backstreet alleyways, I found Mr Winward surrounded by the men."
    $ GoalComplete(QstTheJackpot, 20)
    MR_WINWARD @angry "You can't do this to me! I'm Bilgar Winward of the-"
    show mr_winward at shake
    "They pushed him sharply against the damp wall, causing the air to knock out of his lungs."
    MR_WINWARD @shock "OOOFFHH!"
    "The one bandit drew his blade and held it up towards Mr Winward's face."
    MR_WINWARD @scared "I -I'll pay you all as soon as I can! I swear!"
    SWINDLER "Do I look like a fucking idiot to you?"
    "He pressed the blade against Mr Winward's cheek, ever so gently dragging it down."
    MR_WINWARD @scared "A-AHHH! W-WAIT! Please!"
    "Stepping out into their line of sight, they turned towards me."
    show swindler at blurin, cright
    $ GoalShow(QstTheJackpot, 30)
    SWINDLER "This doesn't concern you, piss off!"
    menu:
        "I can smell the warmth of your blood from here... Leave now, or I shall make rugs from your skinned flesh." (Req_Perk = "terrifying"):
            SWINDLER "F-Fuck! What's wrong with you?!"
            SWINDLER "Get away from me, you monster!"
            "The terrified bandits fled into the darkness of one of the many pitch-black alleyways."
            hide swindler with easeoutright
            MR_WINWARD @scared "{i}*Huff*{/i} Oh gods... I ... Thank you."
            show mr_winward at cright_f with easeinright

        "I'll cover the old fool's debt." (Req_Gold = 400):
            $ PlayerRemItem("gold", 400)
            SWINDLER "Hmm... Very well then."
            "Throwing the coin pouch toward the bandit, he caught it and looked towards Mr Winward, knife waving in front of his face."
            SWINDLER "Next time, pay your debts, old man... Else, you might not be so lucky next time."
            hide swindler with easeoutright
            "With a sharp whistle, the bandits scattered, hurrying off down one of the many darkened alleyways."
            show mr_winward at cright_f with easeinright
            MR_WINWARD @scared "{i}*Huff*{/i} Oh gods... I... Thank you."

        "{image=[ICON.SWORDS]} {i}*Draw your blade*{/i}":
            SWINDLER "BOYS! IT'S ON!"

            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")

            $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys", CharIDList_Right = ["e_bandit", "e_swindler", "e_bandit"], CanTransform = False))

            "As the last of the bandits dropped and collapsed to the floor in a pool of his own blood, a terrified Mr Winward turned shakily towards me."

            $ AutoMus(True)
            $ LocFlush()

            show mc at left
            show mr_winward at cright_f
            MC "Are you alright?"
            MR_WINWARD @scared "{i}*Huff*{/i} You... You killed them all!"
            MR_WINWARD @scared "I ... I thought I was about to be-"
            show mr_winward at shake
            "He gulped, shaking off the thought."
            MR_WINWARD @scared "Y-Yes, I'm alright..."

    $ GoalComplete(QstTheJackpot, 30)

    MC  "Well, my job here is done."
    MC  "Go home, old man."
    show mc at blurin, left_f
    show mr_winward at cleft_f with easeinright
    "As I turned to leave, Mr Winward reached out to grab my arm."
    MR_WINWARD @shock "Wait a minute, lad!"
    show mr_winward at cright_f with easeoutright
    show mc at cleft with easeinleft
    MR_WINWARD @think "I've uhh... got an idea that might interest you!"
    MC @think "...Go on."
    MR_WINWARD @happy "Look, I've seen the way you looked at my wife's tits."
    MR_WINWARD @laugh "Don't know what you see in that used-up hag at this point, but how's about I uhh, {i}push{/i} her towards giving you some relief?"
    MC @serious "...Are you serious?"
    MR_WINWARD @happy "Course I am!"
    MR_WINWARD @happy "In return...  you uhh...perhaps {i}help me out{/i} in my next game."
    MC @serious "You're planning to do this again?"
    MC @angry "After what just happened?"
    MR_WINWARD @think "I am, with much higher stakes."
    MR_WINWARD  "I ain't tellin' the wife nothin,' {i}but I have been making some small winnings here and there...{/i}"
    MR_WINWARD  "Been saving up for a high-stakes game."
    MR_WINWARD  "Figured though, could use some backup..."
    MR_WINWARD @scared "{i}Especially if things end up like this again...{/i}"
    MR_WINWARD  "So, how about it? You interested?"
    MC @serious "...I'll think about it."
    MR_WINWARD @happy "Ahh! Knew you were a smart one! Don't worry, lad, you won't regret a thing!"
    MR_WINWARD @happy "Come around in a day or so once I've softened her up, fufu! Don't worry, I'll keep to my end of the deal!"
    MR_WINWARD  "Now uhh, you mind escorting me out of here?"
    MR_WINWARD @scared "This uh... Ain't no place for an old man at this hour."
    MC  "...Fine."
    scene black with dissolve
    "I escorted Mr Winward safely out of the alleyway."
    $ LocFlush()
    show mc at left
    show mr_winward at right_f
    with dissolve
    MR_WINWARD "Thanks again, lad!"
    hide mr_winward with dissolve
    MC "(You wouldn't think he basically just offered up his wife's ass to us.)"
    BLACK "{i}(This male is weak, but he is convinced he is strong... Humans are...fascinating.){/i}"
    $ GoalShow(QstTheJackpot, 40)
    $ QstSetProgress(QstTheJackpot, 1)
    $ LocEnter()

label qst_jackpot_return_from_unicorn:
    show mc at cleft with easeinleft
    show mrs_winward at cright_f with easeinright
    "Mrs. Winward approached me sheepishly, hands clasped together as she nervously drew close."
    $ GoalComplete(QstTheJackpot, 40)
    MRS_WINWARD @embarr "H-Hello again."
    MC @think "Is something the matter?"
    MRS_WINWARD @embarr "I... Um..."
    MRS_WINWARD @embarr "My husband told me about what happened the other night."
    MRS_WINWARD @embarr "How you kept him safe, but now he owes {i}you{/i} a sizable debt."
    "Mrs Winward bit down on her lower lip, her legs slightly trembling as she stepped closer towards you."
    MRS_WINWARD @embarr "I... I was hoping you might be willing to let me pay off that debt through {i}other{/i} means."
    MRS_WINWARD @sad "Oh gods... This must sound so shameful and pathetic coming from an old woman like myself!"
    MC @smile "It's hardly pathetic; you're still a very attractive woman, you know."
    "My words made Mrs Winward even more flustered."
    MRS_WINWARD @shock "...A-Attractive, you say?"
    MRS_WINWARD @think "W-Well, um..."
    MRS_WINWARD @blush "If you're sure you're happy for me to continue..."
    MRS_WINWARD @lewd "C-Could you come a little closer, please?"
    MRS_WINWARD @lewd "There's something I want to try..."
    "Following Mrs Winward around the back of the counter, she suddenly squatted down, scrambling to unbuckle my clothes with bated breath." 
    "As she pulled out my cock, her eyes widened at the size of it, and a small, audible gasp escaped her lips as it rested down heavily on her soft face."
    MRS_WINWARD "D-Deary...!"
    MRS_WINWARD "Oh... Oh my! You're... {i}Such a big boy!{/i}"
    "Mrs Winward's cheeks flushed red as she smelt the thick, heavy member resting on her face, releasing a soft moan as she did so."
    MC "Bigger than your husbands, I take it, Mrs Winward?"
    MRS_WINWARD "...L-Let's not talk about him right now!"
    MRS_WINWARD "I, umm, have {i}other{/i} things on my mind."
    
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene mrs_winward_bj_dress_solo_idle with dissolve
    $ Pause()

    "Gently, her tongue slipped out of her mouth to tenderly run along the shaft, and after she gently teased it, she took a deep breath and wrapped her lips around the head of my cock." 
    scene mrs_winward_bj_dress_solo_slow with dissolve
    $ Pause()
    MRS_WINWARD "M-Mhmm!"
    MC "Mhmmff! You've definitely had some experience with this over the years, haven't you?"
    "Mrs Winward, embarrassed, didn't answer; instead, she began to glide her head back and forth in a slow but steady motion."
    "Her soft lips formed a tight seal around my cock as her tongue sheepishly wrapped and teased my member."
    "Her puffy stuffed cheeks were bright red as her eyes looked up pleadingly towards me, unsure if she was doing a good enough job at pleasing me."
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i} Mhmmfhh!"
    MRS_WINWARD "(I-I've never even seen one this big!)"
    MRS_WINWARD "(Oh gods... I can't believe I'm actually sucking this man's cock!)"
    MRS_WINWARD "(How shameful... H-How depraved for a woman of my age to be cheating on my... my...)"
    scene mrs_winward_bj_dress_solo_fast with dissolve
    $ Pause()
    "Suddenly, Mrs Winward happily groaned as she threw her head forward, pushing the cock deeper and deeper into her throat as she became enthralled in her task."
    MRS_WINWARD "({i}P-Pathetic husband....!{/i} Oh gods, who am I trying to fool?)"
    MRS_WINWARD "(I've dreamed about this for years!)"
    MRS_WINWARD "(With any luck, my husband's debt won't be cleared just from this, no no, this young man needs to have his way with me a couple of times first at least! Fufufu! {image=[ICON.HEART]})."
    MRS_WINWARD "(Thank the gods he's such a fool!)"
    "As the minutes passed, more and more, Mrs Winward seemed enthralled and excited with what she was doing."
    MC "Ahh... You better get accustomed to having a bigger cock inside you from now on because I intend to make good use of that fat ass of yours, Mrs Winward!"
    "Mrs Winward shuddered with pleasure, moaning as she slammed her head forward in excitement, her glasses beginning to steam up."
    MRS_WINWARD "Mhhfhh!"
    "Suddenly, the two of us heard the sounds of soft footsteps followed by the banging of a wooden cane on the floor as Mr Winward came down."
    scene mrs_winward_bj_dress_oldman_slow with dissolve
    $ Pause()
    MRS_WINWARD "(Oh gods! Please, PLEASE don't see me like this!)"
    MRS_WINWARD "(Not now! Not-)"
    MRS_WINWARD "Mhhfghh!"
    "I pulled Mrs Winward's head forward, letting her know she was to continue even with her husband stood there, causing her to momentarily choke for a second from the sudden extra inch pressing down into her throat."
    MR_WINWARD "You seen Kionni anywhere?"
    MC "No, can't say I - ahh! Have!"
    MR_WINWARD "She was supposed to have my dinner ready thirty minutes ago!"
    MR_WINWARD "Lazy woman is probably out or something..."
    MRS_WINWARD "(GRRRHH! Lazy woman, huh?)"
    scene mrs_winward_bj_dress_oldman_fast with dissolve
    $ Pause()
    "Incensed, Mrs Winward once again threw her head forward, surprising me with her sudden keenness as she wrapped her tongue lewdly around my cock."
    "The warm, wet sensation almost overpoweringly pleasant."
    MC "C-Can't say I've seen her! Nhmm!"
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i}"
    MR_WINWARD "What's that sound?"
    MC "Hm? N-No idea, probably coming from outside."
    MRS_WINWARD "*Slurp* {image=[ICON.HEART]}"
    MR_WINWARD "..."
    MR_WINWARD "Why are you standing behind that counter?"
    MC "Oh, uh, Mrs Winward said she'd be right back and to just stand behind the - Ah! Counter till she gets back!"
    MR_WINWARD "I thought you said you hadn't seen her?"
    MC "My - Ah! Mistake, I meant she'll be back shortly!"
    MR_WINWARD "Hmph! Typical bloody woman!"
    MR_WINWARD "Always thinking about herself and forgetting everyone else!"
    
    "Mrs Winward suddenly pressed her head forward, taking my cock fully to the hilt and holding it there."
    "With defiant, fiery eyes, she looked up towards me, tongue thrashing furiously around my cock."
    "With her eyes, she told me clearly, {i}'You're going to cum down my throat in front of my prick of a husband, whether you like it or not now!{/i}"
    
    "As Mr. Winward turned to leave, grumbling under his breath, I grabbed hold of Mrs. Winward's head and held her there; my balls tightened as I exploded into her mouth." 
    scene mrs_winward_bj_dress_solo_fast with dissolve
    $ Pause()
    "Her eyes widened as she felt the hot rush of my heavy load flood down her throat."
    "I grunted loudly, watching the excess of my seed spill out the sides of her mouth as her eyes began to roll back."
    "Desperately, Mrs Winward tried to swallow down as much of the load as possible, her stomach lightly bulging from the seed being pumped into her as her eyes rolled back."
    MC "H-HRGHHHHH...!"

    $ UnlockGalFlag("mrs_winward", "bj", "dress")
    $ UnlockGalFlag("mrs_winward", "bj", "winward_watches")
    $ UnlockGalFlag("mrs_winward", "bj", "no_cuck")

    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    $ ReduceInfectionFromSex("mrs_winward")
    
    scene mrs_winward_bj_dress_solo_finish with flash
    $ Pause()
    $ UnlockGalSceneAndGrantXp("mrs_winward", "bj")

    MRS_WINWARD "{i}*Glug!*{/i} Mfhghhh?!"
    MR_WINWARD "Huh? You say something, boy?"
    MC "N-No, Mr Winward! Have a - Ahh! Nice day!"
    MR_WINWARD "Bah!"
    "As Mr Winward left, slamming the door behind him, finally, I released my tight grip on the back of Mrs Winward's head."
    "As she dragged her wet lips off from my cock, with a loud {i}*PLOP*{/i} she pulled her head away and gasped for air, a silvery trail of cum and saliva between her lips and my cock dissipated quickly to the ground between us."
    MRS_WINWARD "{i}*Huff*{/i} Oh my... {i}*Huff*{/i} Deary..."
    MRS_WINWARD "Looks like I might have to skip eating later! Fufu!"
    

    $ AutoMus(True)
    $ LocFlush()
    show mc at cleft
    show mrs_winward at cright_f
    with dissolve

    "As Mrs Winward rose back to her feet, she wiped her mouth with her hands and smiled shyly towards me once again, hands clasped together." 
    MRS_WINWARD @embarr "I've not had much experience outside of my husband, and n-never with one like yours."
    MRS_WINWARD @embarr "I hope that was good for you, dear."
    MC @smile "You forgot to ask how much of your husband's {i}debt{/i} doing that would pay back."
    "Mrs Winward chuckled, raising a brow."
    MRS_WINWARD @laugh "{i}Did I?{/i}"
    MRS_WINWARD @blush "I guess we won't be able to deduct that from the debt then, will we? {i}*Sigh*{/i} What a shame..."
    MRS_WINWARD @lewd "I guess you'll just have to have your wicked way with me even longer than anticipated."
    MRS_WINWARD @lewd "Whatever shall my old bones do?"
    MC @smile "So, then... Shall we take this to the bedroom?"
    MRS_WINWARD @blush "Haha! So much energy!"
    MRS_WINWARD @lewd "I had a... {i}small request{/i} before I let you do whatever you please with me."
    MC @think "Go on?"
    MRS_WINWARD  "I was hoping you might be able to procure me some cowhide."
    MRS_WINWARD @blush "T-There's something I've been thinking about making for a while, but I was always too embarrassed to mention it to my husband."
    MRS_WINWARD @angry "He'd probably just tell me my idea was ridiculous or something..."
    MRS_WINWARD "The butcher should be able to procure you one, as I imagine one of the farmers won't be too keen on giving up one of their cattle!"
    if PlayerItemQty("cow_hide") > 0:
        MC @think "Wait, you mean a cow hide, like this one?"
        "I have produced a hide I had with me and presented it to her."
        jump qst_jackpot_return_with_cowh
    else:
        $ GoalShow(QstTheJackpot, 50)
        $ QstSetProgress(QstTheJackpot, 2)
        MC  "I'll see what can be done."
        MRS_WINWARD @happy "Thank you, deary."
        MRS_WINWARD @happy "Let me know when you have it."
        $ LocEnter()

label qst_jackpot_return_with_cowh:
    $ PlayerRemItem("cow_hide")
    MRS_WINWARD @laugh "Oooh! This is perfect!"
    # if we did the market trip, we will have "return with hide" goal active
    if IsGoalVisible(QstTheJackpot, 60):
        $ GoalComplete(QstTheJackpot, 60)
    MRS_WINWARD @scared "B-but... There is something else..."
    MRS_WINWARD @scared "My husband, he... He said to tell you to meet him at {i}The Black Diamond{/i} tonight."
    MRS_WINWARD @scared "What's going on? Why is he asking you to meet him {i}there{/i} of all places?"
    MRS_WINWARD @scared "I-I've only ever heard bad things about that place."
    $ QstSetProgress(QstTheJackpot, 4)
    $ GoalShow(QstTheJackpot, 70)
    $ HouseLockBlackDiamond().canBeAccessed = True
    MC @angry "(That idiot!)"
    MC @serious "I'll make sure he is alright."
    MRS_WINWARD @scared "A-Alright... Just, {i}be safe, please?{/i}"
    $ LocEnter()