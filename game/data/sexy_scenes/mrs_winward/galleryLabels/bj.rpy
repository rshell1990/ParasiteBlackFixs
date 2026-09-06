label gallery_winward_bj:
    $ tmpvar = {}
#######
    if GalFlag("mrs_winward", "bj", ["dress", "cow"]):
        "Was she wearing her cow outfit?"
        menu:
            "Yes":
                $ tmpvar["cow"] = True
            "No":
                $ tmpvar["cow"] = False

    elif GalFlag("mrs_winward", "bj", "cow"):
        $ tmpvar["cow"] = True

    elif GalFlag("mrs_winward", "bj", "dress"):
        $ tmpvar["cow"] = False
#######
    if GalFlag("mrs_winward", "bj", ["cuck", "no_cuck"]):
        "Was Mr. Winward actively engaged in the scene?"
        menu:
            "Yes":
                $ tmpvar["cuck"] = True
            "No":
                $ tmpvar["cuck"] = False

    elif GalFlag("mrs_winward", "bj", "cuck"):
        $ tmpvar["cuck"] = True

    elif GalFlag("mrs_winward", "bj", "no_cuck"):
        $ tmpvar["cuck"] = False
#######
    if tmpvar["cuck"] == True:
        jump gallery_winward_bj_cuck
    else:
        if GalFlag("mrs_winward", "bj", ["winward_watches", "winward_gone"]):
            "Was Mr. Winward around at all?"
            menu:
                "Yes":
                    $ tmpvar["winward_watches"] = True
                "No":
                    $ tmpvar["winward_watches"] = False

        elif GalFlag("mrs_winward", "bj", "winward_watches"):
            $ tmpvar["winward_watches"] = True

        elif GalFlag("mrs_winward", "bj", "winward_gone"):
            $ tmpvar["winward_watches"] = False
        if tmpvar["winward_watches"]:
            jump gallery_winward_bj_not_cuck_watched
        else:
            jump gallery_winward_bj_not_cuck_solo

label gallery_winward_bj_not_cuck_solo:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Following Mrs Winward around the back of the counter, she suddenly squatted down, scrambling to unbuckle my clothes with bated breath."
    "As she pulled out my cock, she licked her lips enticingly at the meal before her."

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_idle with dissolve
    else:
        scene mrs_winward_bj_dress_solo_idle with dissolve
    $ Pause()

    MRS_WINWARD "Mhmm... {i}Such a big boy!{/i}"
    "Mrs Winward's cheeks flushed red as she smelt the thick, heavy member resting on her face, moaning softly as she did so."
    MC "Missed me?"
    MRS_WINWARD "You and your {i}wonderful{/i} cock. {image=[ICON.HEART]}"

    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_slow with dissolve
    else:
        scene mrs_winward_bj_dress_solo_slow with dissolve
    $ Pause()

    "Gently, her tongue slipped out of her mouth to tenderly run along the shaft, and after she gently teased it, she took a deep breath, and wrapped her lips around the head of my cock." #BJ behind counter
    MRS_WINWARD "M-Mhmm!"
    MC "Mhmmff! That's it Mrs Winward, all our time together is really paying off, isn't it?"
    "Mrs Winward, embarrassed, didn't answer, instead, she began to glide her head back and forth in a slow but steady motion."
    "Her soft lips formed a tight seal around my cock as her tongue sheepishly wrapped and teased my member."
    "Her puffy stuffed cheeks were bright red as her eyes looked up pleadingly towards me, unsure if she was doing a good enough job at pleasing me."
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i} Mhmmfhh!"
    MRS_WINWARD "(If only my husband was half as big as him.)"
    MRS_WINWARD "(Urghhh! Forget that moron!)"
    MRS_WINWARD "(I could just worship this cock all night!)"
    "Suddenly, Mrs Winward groaned happily as she threw her head forward, pushing the cock deeper and deeper into her throat as she became enthralled in her task."
    MRS_WINWARD "(It's h-his fault for being such a fool! Mhmm, now a bigger, {i}better{/i} man is here to take care of my needs fufufu! {image=[ICON.HEART]})"

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_fast with dissolve
    else:
        scene mrs_winward_bj_dress_solo_fast with dissolve
    $ Pause()

    "As the minutes passed, more and more, Mrs Winward seemed enthralled and excited with what she was doing."
    MC "Ahh...! You're getting real good at sucking cock, Mrs Winward."
    "Mrs Winward shuddered with pleasure, moaning as she slammed her head forward in excitement, her glasses beginning to steam up."
    MRS_WINWARD "Mhhfhh!"
    "I pulled Mrs Winward's head forward, causing her to momentarily choke for a second from the sudden extra inch pressing down into her throat."
    "Incensed, Mrs Winward once again threw her head forward, surprising me with her sudden keenness as she wrapped her tongue lewdly around my cock."
    "The warm, wet sensation almost overpoweringly pleasant."
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i}"
    MRS_WINWARD "*Slurp* {image=[ICON.HEART]}"
    "Mrs Winward suddenly pressed her head forward, taking my cock fully to the hilt and holding it there."
    "With defiant, fiery eyes she looked up towards me, tongue thrashing furiously around my cock."
    "With her eyes she told me clearly, {i}'You're going to cum down my throat whether you like it or not!'{/i}"
    "I grabbed a hold of Mrs Winward's head and held her there, my balls tightened as I exploded into her mouth."
    "Her eyes widened as she felt the hot rush of my heavy load flood down her throat."
    "I grunted loudly, watching the excess of my seed spill out the sides of her mouth as her eyes began to roll back."
    "Desperately, Mrs Winward tried to swallow down as much of the load as possible, her stomach lightly bulging from the seed being pumped into her as her eyes rolled back."
    MC "H-HRGHHHHH...!"

    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_finish with flash
    else:
        scene mrs_winward_bj_dress_solo_finish with flash
    $ Pause()

    MRS_WINWARD "{i}*Glug!*{/i} Mfhghhh?!"
    "Finally, I released my tight grip on the back of Mrs Winward's head."
    "As she dragged her wet lips off from my cock, with a loud {i}*PLOP*{/i} she pulled her head away and gasped for air, a silvery trail of cum and saliva between her lips and my cock dissipiated quickly to the ground between us."
    MRS_WINWARD "{i}*Huff*{/i} Oh my... {i}*Huff*{/i} Deary..."
    MRS_WINWARD "Looks like I might have to skip eating later! Fufu!"
    return

label gallery_winward_bj_not_cuck_watched:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_slow with dissolve
    else:
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

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_fast with dissolve
    else:
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

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_oldman_slow with dissolve
    else:
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
    
    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_oldman_fast with dissolve
    else:
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
    
    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_fast with dissolve
    else:
        scene mrs_winward_bj_dress_solo_fast with dissolve
    $ Pause()

    "Her eyes widened as she felt the hot rush of my heavy load flood down her throat."
    "I grunted loudly, watching the excess of my seed spill out the sides of her mouth as her eyes began to roll back."
    "Desperately, Mrs Winward tried to swallow down as much of the load as possible, her stomach lightly bulging from the seed being pumped into her as her eyes rolled back."
    MC "H-HRGHHHHH...!"

    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_finish with flash
    else:
        scene mrs_winward_bj_dress_solo_finish with flash
    $ Pause()

    MRS_WINWARD "{i}*Glug!*{/i} Mfhghhh?!"
    MR_WINWARD "Huh? You say something, boy?"
    MC "N-No, Mr Winward! Have a - Ahh! Nice day!"
    MR_WINWARD "Bah!"
    "As Mr Winward left, slamming the door behind him, finally, I released my tight grip on the back of Mrs Winward's head."
    "As she dragged her wet lips off from my cock, with a loud {i}*PLOP*{/i} she pulled her head away and gasped for air, a silvery trail of cum and saliva between her lips and my cock dissipated quickly to the ground between us."
    MRS_WINWARD "{i}*Huff*{/i} Oh my... {i}*Huff*{/i} Deary..."
    MRS_WINWARD "Looks like I might have to skip eating later! Fufu!"
    return

label gallery_winward_bj_cuck:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Following Mrs Winward around the back of the counter, she suddenly squatted down, scrambling to unbuckle my clothes with bated breath."
    "As she pulled out my cock, she licked her lips enticingly at the meal before her." #Anim 1

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_idle with dissolve
    else:
        scene mrs_winward_bj_dress_solo_idle with dissolve
    $ Pause()

    MRS_WINWARD "Mhmm... {i}Such a big boy!{/i}"
    "Mrs Winward's cheeks flushed red as she smelt the thick, heavy member resting on her face, moaning softly as she did so."
    MC "Missed me?"
    MRS_WINWARD "You and your {i}wonderful{/i} cock. {image=[ICON.HEART]}"

    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
 
    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_slow with dissolve
    else:
        scene mrs_winward_bj_dress_solo_slow with dissolve
    $ Pause()

    "Gently, her tongue slipped out her mouth to tenderly run along the shaft, and after she gently teased it, she took a deep breath, and wrapped her lips around the head of my cock." 
    MRS_WINWARD "M-Mhmm!" #anim 2
    MC "Mhmmff! That's it Mrs Winward, all our time together is really paying off, isn't it?"
    "Mrs Winward, embarrassed, didn't answer, and instead, she began to glide her head back and forth in a slow but steady motion."
    "Her soft lips formed a tight seal around my cock as her tongue sheepishly wrapped and teased my member."
    "Her puffy stuffed cheeks were bright red as her eyes looked up pleadingly towards me, unsure if she was doing a good enough job at pleasing me."
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i} Mhmmfhh!"
    MRS_WINWARD "(If only my husband was half as big as him.)"
    MRS_WINWARD "(I could just worship this cock all night!)"
    MRS_WINWARD "(The s-shame is - Mhmm! So hot! A woman of my age to be cheating on my... my...)"
    "Suddenly, Mrs Winward groaned happily as she threw her head forward, pushing the cock deeper and deeper into her throat as she became enthralled in her task."
    MRS_WINWARD "({i}P-Pathetic husband....!{/i})"
    MRS_WINWARD "(It's his fault for being such a fool! Mhmm, now a bigger, {i}better{/i} man is here to take care of my needs fufufu! {image=[ICON.HEART]})"

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_fast with dissolve
    else:
        scene mrs_winward_bj_dress_solo_fast with dissolve
    $ Pause()

    MRS_WINWARD "(Thank the gods he's such a fool!)"
    "As the minutes passed, more and more, Mrs Winward seemed enthralled and excited with what she was doing."
    MC "Ahh...! You're getting real good at sucking cock, Mrs Winward."
    "Mrs Winward shuddered with pleasure, moaning as she slammed her head forward in excitement, her glasses beginning to steam up."
    MRS_WINWARD "Mhhfhh!"
    "Suddenly, the two of us heard the sounds of what sounded like a grunt coming from the backroom." #anim 3
    
    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_cuck_slow with dissolve
    else:
        scene mrs_winward_bj_dress_cuck_slow with dissolve
    $ Pause()

    MRS_WINWARD "(Urghh! Must he always linger like a pest when I'm trying to please {i}my{/i} man?)"
    "Mrs Winward did nothing to hide her actions, slurping loudly as her head bopped back and forth taking my cock excitedly."
    MRS_WINWARD "Mhhfghh!"
    "I wondered where the old man was exactly, hiding behind something no doubt as he watched in delight as his wife pleasured me."
    MC "Are you watching this old timer?"
    MR_WINWARD "H-Hmm... Y-Yes...!"
    MR_WINWARD "O-Oooh! Can I come closer to get a better-"
    MC "{i}No.{/i}"
    MC "Stay there and don't move."
    MR_WINWARD "But-"
    "Mrs Winward briefly pulled my cock out of her mouth."
    MRS_WINWARD "No dear, do as you're told." #anim 4

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_fast with dissolve
    else:
        scene mrs_winward_bj_dress_solo_fast with dissolve
    $ Pause()

    MR_WINWARD "Ahh! But I want to see more!"
    MC "Where are you even hiding old man?"
    MC "{i}You sound close...{/i}"
    MRS_WINWARD "You'll just have to make do you old pervert!"
    MRS_WINWARD "Mmm, ignore him darling and give me more of that big thing!"
    "I pulled Mrs Winward's head forward, causing her to momentarily choke for a second from the sudden extra inch pressing down into her throat." #anim 5
    MRS_WINWARD "Mmmfghhh!!"

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_cuck_fast with dissolve
    else:
        scene mrs_winward_bj_dress_cuck_fast with dissolve
    $ Pause()

    MR_WINWARD "Oooh! You're both so cruel to me!"
    MC "Ahh! Shut it old man!"
    "The sound of Mr Winward's grunts grew louder, as did the sound of him stroking his cock whilst I shoved my member down Mrs Winward's throat."
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i} Mhhfhghhh! Shooo bhighhh honeyhh!"

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_fast with dissolve
    else:
        scene mrs_winward_bj_dress_solo_fast with dissolve
    $ Pause()

    MR_WINWARD "S-She really sounds like her mouth is full!"
    MR_WINWARD "Don't tell me she's managed to swallow it all?!!" #Anim 6
    MC "Ahhh! Guess you'll never know, will you?"
    MRS_WINWARD "(Fufu, show that failure whose in charge now.{image=[ICON.HEART]})"
    "Incensed, Mrs Winward once again threw her head forward, surprising me with her sudden keenness as she wrapped her tongue lewdly around my cock."
    "The warm, wet sensation almost overpoweringly pleasant."
    MC "Her mouth is - Mhmm! So good!"
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i}"
    MR_WINWARD "..."

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_cuck_fast with dissolve
    else:
        scene mrs_winward_bj_dress_cuck_fast with dissolve
    $ Pause()

    MC "Her lips barely wrap around my cock, but she's learning fast how deep I like it swallowed!"
    MR_WINWARD "Mmm, i-is that so?"
    MR_WINWARD "Well you're welcome to use her mouth anytime you wish!"
    MRS_WINWARD "*Slurp* {image=[ICON.HEART]}"
    MR_WINWARD "Train her to be your perfect little cocksucker!"
    MR_WINWARD "Make her swallow your heavy loads like a good little slut!"
    "Mrs Winward suddenly pressed her head forward, taking my cock fully to the hilt and holding it there."
    "With defiant, fiery eyes she looked up towards me, tongue thrashing furiously around my cock."
    "With her eyes she told me clearly, {i}'You're going to cum down my throat in front of my failure of a husband, whether you like it or not now!{/i}"


    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_solo_finish with flash
    else:
        scene mrs_winward_bj_dress_solo_finish with flash
    $ Pause()

    "As I grabbed a hold of Mrs Winward's head and held her there, my balls tightened as I exploded into her mouth." #cum
    "Her eyes widened as she felt the hot rush of my heavy load flood down her throat."
    "I grunted loudly, watching the excess of my seed spill out the sides of her mouth as her eyes began to roll back."
    "Desperately, Mrs Winward tried to swallow down as much of the load as possible, her stomach lightly bulging from the seed being pumped into her as her eyes rolled back."
    MC "H-HRGHHHHH...!"
    MRS_WINWARD "{i}*Glug!*{/i} Mfhghhh?!"
    "As I finished pouring my seed down her throat, Mr Winward finally stroked himself to finish, howling as I heard two small squirts splashed onto the floor."

    if tmpvar["cow"] == True:
        scene mrs_winward_bj_cow_cuck_finish with flash
    else:
        scene mrs_winward_bj_dress_cuck_finish with flash
    $ Pause()

    MR_WINWARD "OOOOOOH! That's it boy! FILL HER UP GOOD!"
    MR_WINWARD "{i}*Huff*...Gods...{/i}"
    "Fully spent, I released my tight grip on the back of Mrs Winward's head."
    "As she dragged her wet lips off from my cock, with a loud {i}*PLOP*{/i} she pulled her head away and gasped for air, a silvery trail of cum and saliva between her lips and my cock dissipiated quickly to the ground between us."
    MRS_WINWARD "{i}*Huff*{/i} Oh my... {i}*Huff*{/i} Deary..."
    MRS_WINWARD "Looks like I might have to skip eating later! Fufu!"
    return