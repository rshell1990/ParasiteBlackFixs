label gallery_nyx_facefuck:
# 1st or rep
    if GalFlag("nyx", "facefuck", "repeat"):
        "Was it our first time?"
        menu:
            "Yes":
                $ tmpvar["variant"] = "first"
            "No":
                $ tmpvar["variant"] = "repeat"
    else:
        $ tmpvar["variant"] = "first"


# clothes
    if GalFlag("nyx", "facefuck", ["slave", "naked"]):
        "Was she wearing her slave outfit?"
        menu:
            "Yes":
                $ tmpvar["clothes"] = "slave"

            "No":
                $ tmpvar["clothes"] = "naked"

    elif GalFlag("nyx", "facefuck", "slave"):
        $ tmpvar["clothes"] = "slave"

    else:
        $ tmpvar["clothes"] = "naked"
    
    if tmpvar["variant"] == "first":
        jump gallery_nyx_facefuck_first
    elif tmpvar["variant"] == "repeat":
        jump gallery_nyx_facefuck_repeat

label gallery_nyx_facefuck_first:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    scene black with dissolve
    "I lightly shoved Nyx down onto the bed and began to move around the other side of the bed." #Cut to black
    NYX "H-Hey! What do you think you're-"
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_dick_on_face_slave with hpunch
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_dick_on_face_naked with hpunch
    $ Pause()
    "Placing my cock down onto Nyx's warm face, her eyes widened in shock." #Cut to cock on Nyx face (upside down bed face fuck)
    NYX "Y-Your-"
    MC "We both know why I came here tonight."
    MC "Now are you going to keep protesting? Or are you going to open those pretty lips and start sucking my cock?"
    "Nyx grumbled shyly, somewhere torn between irritable defiance and aroused."
    NYX "I-I don't have much experience with this kind of thing, how should I-"
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_lick_slave with dissolve
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_lick_naked with dissolve
    $ Pause()
    "I didn't let Nyx finish her question before I forced the head of my cock into her warm, wet mouth and pressed a couple inches into her throat." #lick tease anim 
    NYX "Mmfghh?!?"
    MC "Ahhh, that's it ... Use your tongue."
    MC "Just like that... Mmfghh...Gooood."
    NYX "As her warm mouth slobbered over my cock, she teasingly flicked her tongue over the head, watching me shudder slightly in pleasure."
    NYX "Ha! {i}*Shlick!*{/i} Have I already half-way beaten you already? {i}*Shlick!*{/i} You'll be begging on me for forgiveness on your hands and knees soon!"
    MC "Oh, will I now?"
    NYX "Of course you - {i}*Shlick!*{/i} will!"
    MC "In that case then, I'd better stop going easy on you then, hadn't I?"
    NYX "Huh? {i}*Shlick!*{/i} What are you-"
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_shove_slave with hpunch
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_shove_naked with hpunch
    $ Pause()
    "Nyx's eyes widened in shock as I began to force my cock back and forth in her mouth." #Cock in throat anim (BJ)
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_bj_slave with hpunch
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_bj_naked with hpunch
    $ Pause()
    NYX "Mmfhgh! *Slurp!* MMFFHHH! *Slurp!*"
    "Her hot tongue thrashed around and beat against my cock as her lips struggled to wrap around the thick member now forcing its way down her throat."
    "Fucking the mouth of the uptight Captain Nyx was an exhilarating feeling, as I watched her throat bulge with every motion as she struggled to handle the meat,"
    "She felt incredible, despite her lack of experience and unease, the feeling of her mouth was euphoric."
    NYX "Mmmfhhhh! {i}*Slurp!*{/i}"
    NYX  "(W-What's going on?)"
    NYX "(His ... His cock is in my-)"
    NYX "(Oh gods ... What's this feeling?)"
    NYX "(It's like everything is rushing to my head at once ... I'm feeling so dizzy!)"
    "Her technique was clumsy, with her teeth lightly grazing against my cock occasionally as her eyed began to water, Nyx was clearly not used to be treated like an object such as this."
    "Despite this however, from the red flush of her face and despite her light moans of protest, she didn't resist me at all."
    "If anything, Nyx seemed to be doing her best to relax, as if she wanted to push herself to see how far she could take the cock."
    NYX "(Why is this making me so wet?)"
    NYX "(His hands f-feel so strong pinning me like this.)"
    NYX "(And his c-cock ... Why does it have to be so big?)"
    NYX "(Ahh... Just smelling it turns me on!)"
    NYX "{i}*Slurp!*{/i} Mmfghh! {i}*Slurp!*{/i} MMMFF!"
    MC "Ahh! If only your men could see you now, huh?"
    MC "The Captain of the guard everyone's so scared off, slobbering all over my cock like a greedy whore."
    "Nyx's brow creased as she growled in frustration, but as I continued to slide my cock in and out of her wet mouth, she soon began to relax once more, letting the pleasure wash over her."
    NYX "(W-What's wrong with me? I've never ... Not like this.)"
    NYX "({i}But it tastes so good...{/i})"
    "As Nyx squirmed, she tapped at my leg for air, her body writhing as she began to wane."
    NYX "MMMFGHH!"
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_lick_slave with dissolve
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_lick_naked with dissolve
    $ Pause()
    "Unsheathing my cock from her throat, Nyx kissed the end of my cock as it popped out of her mouth, letting her gasp for air as she collected herself." #Cock lick tease anim
    "She stared up at the hard cock, coated in saliva, dangling in front of her with almost hypnotic eyes, a silvery saliva trail still connected between her mouth and the well fucked cock resting just above her face."
    NYX "{i}*Huff*{/i} You ... {i}*Huff*{/i} bastard!"
    MC "You looked like you were enjoying yourself..."
    NYX "{i}*Huff*{/i} You think I'd - {i}*Huff*{/i} enjoy having this - {i}*Huff*{/i}"
    NYX "{i}*Huff*{/i} Disgusting, {i}*Huff*{/i}"
    NYX "Fat."
    NYX "{i}Huge{/i} cock, rammed down - {i}*Huff*{/i} my throat?"
    MC "Looking at how wet you are, I'd say so..."
    NYX "D-Don't flatter yourself! {i}*Huff*{/i} This is merely for-"
    "As I pressed the head of my cock against her lips once more, she groaned and began to suckle on it."
    NYX "Mmmhhffh~"
    MC "For honor's sake, huh?"
    NYX "Shuudhupp!"
    MC "Don't you dare stop this time till you drain my balls dry!"
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_bj_hand_slave with hpunch
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_bj_hand_naked with hpunch
    $ Pause()
    "I rammed my cock back into Nyx's mouth once more." #BJ anim (again) 
    NYX "{i}*Slurp!* Mmmfghh! *Slurp!*{/i}"
    NYX "(My body feels so hot ... The more he touches me, the more I f-feel like this is what I was meant to be.)"
    NYX "(There's some voice in the back of my head m-messing with me! What is this - Grghh! Magic?)"
    NYXP "({i}Why are you fighting it, silly? Can't you see how much happier you'd be?{/i})" #Change texts marked with P to Pink - these are Nyx's intrusive perverse thoughts 
    MC "Ahh! Nyx! You're m-mouth feels sooo good!"
    MC "Good girl! Ahh! Fuck!"
    NYXP "({i}See? Don't you just feel how wet you get when he calls you a good girl?{/i})" #P
    NYX "(S-Shut up! Shut up! Shut up! SHUT UP!)"
    NYX "(I pushed you away years ago!)"
    NYXP "({i}Oh honey, I didn't go anywhere, I've just been waiting for you to open your eyes!{/i})" #P
    NYXP "({i}I've been telling you all along this is what you need! You're just so stubborn worrying about what those pesky soldiers would think...{/i})" #P
    NYXP "({i}This is what you need though, isn't it? What I told you allll along.{/i})" #P
    NYXP "({i}A fat cock rammed down your throat, in your pussy, up your tight ass...!{/i})" #P
    NYX "(S-Stop talking! I'm a soldier damn it! Grghh!)"
    NYX "Mmfghh! {i}*Slurp!*{/i}"
    NYXP "({i}Ha! It's sooo funny seeing you still try be so serious with a cock shoved in your mouth like that!{/i})" #P 
    NYXP "({i}You can deny me all you want, you can play tough bitch to everyone around you, but I know your truest feelings, don't I?{/i})" #P
    NYX "Mmmfghh! Nghhu!"
    MC "Ahh! Did you say something?! {i}*Huff!*{/i}"
    NYXP "({i}You can protest all you want! You need this ... When you need to stop thinking about all those silly little worries in your head, this is what you need.{/i})" #P
    NYXP "({i}Somebody just once to put your needs first ... Somebody else to make the difficult choices when you've had enough.{/i})" #P 
    NYXP "({i}Somebody to fuck you senseless so all this stress is at least tolerable!{/i})" #p
    MC "{i}*Huff!*{/i} I'm gonna c-cum!"
    MC "I'm so close! Hrghh!"
    NYX "Mmmfghhh! {i}*Slurp!* *Slurp!*{/i}"
    NYX "(W-Wait a minute! I-)"
    NYXP "({i}Shhh, I won't let you ruin this for us ... This is a good thing.{/i})" #p
    NYXP "({i}Come on, slut, your man needs you to drain his balls dry already!{/i})" #P
    MC "OH FUCKKKK!"
    NYX "Mmmfhghh...!!"
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_cum_slave with flash
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_cum_naked with flash
    $ Pause()
    "Unable to hold any longer, I flooded Nyx's throat with my hot load." #Cum CGs
    NYX "Glrghh! Glugghh!!"
    "The pleasure washed over me as despite her squirms of shock and pleading to be let go for air, I held my cock down Nyx's throat as I continued to pump her full of my seed."
    NYX "(C-Can't breathe!)"
    "Nyx's eyes began to roll back as she began to lose consciousness..."
    NYX "(There's s-so much cum!)"
    NYX "(Why does it taste so ...so...)"
    NYX "({i}Good...!{/i})"
    "Nyx did her best to swallow down as much of my load as she could, before, finally spent, I unsheathed my cock from her throat." #Fade to black
    "Coughing up the excess cum that run down her chin and onto her breasts."
    "She wheezed for a few moments before she began to settle down, laying there peacefully on the bed without saying a word..."
    NYXP "({i}See? We're going to have lots of fun from now on with this man~{/i})" #P
    return

label gallery_nyx_facefuck_repeat:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    scene black with dissolve
    "I lightly shoved Nyx down onto the bed and began to move around the other side of the bed." #Cut to black
    NYX "Ahh! You're a terror for doing th-"
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_dick_on_face_slave with hpunch
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_dick_on_face_naked with hpunch
    $ Pause()
    "Placing my cock down onto Nyx's warm face, her eyes widened in surprise." #Cut to cock on Nyx face (upside down bed face fuck)
    NYX "Fuck... Everytime I see you waving that bloody thing in my face I just..."
    MC "{i}...Lose it?{/i}"
    NYX ".. S-Shut up!"
    MC "We both know you've been looking forward to a repeat performance."
    MC "Now are you going to keep protesting? Or are you going to open those pretty lips and start sucking my cock like a good girl?"
    "Nyx grumbled shyly, somewhere torn between irritable defiance and aroused."
    NYX "F-Fine, b-but give me a minute to-"
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_lick_slave with dissolve
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_lick_naked with dissolve
    $ Pause()
    "I didn't let Nyx finish before I forced the head of my cock into her warm, wet mouth and pressed a couple inches into her throat."
    "Despite her pleas of asking for more patience, her sweet mouth opened up instantly, she didn't want to wait... {i}She liked it when I took all the silly control away from her.{/i}"
    NYX "Mmfghh!!"
    MC "Ahhh, that's it ... Just like last time, Mhff! Use your tongue."
    MC "You're getting better at this with all our practice we've been getting in I see!"
    MC "... Mmfghh...Gooood slut."
    NYX "As her warm mouth slobbered over my cock, she teasingly flicked her tongue over the head, watching me shudder slightly in pleasure."
    NYX "Ha! {i}*Shlick!*{/i} I've - {i}*Shlick!*{/i} improved since our last duel! {i}*Shlick!*{/i} This time, I'm winning tonight!"
    MC "Oh, is that so?"
    NYX "Of course I - {i}*Shlick!*{/i} will!"
    MC "Then I'd better start treating this more seriously, hadn't I?"
    NYX "{i}*Shlick!*{/i} Mmfghh! You're gonna have to show me what you've-"
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_shove_slave with hpunch
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_shove_naked with hpunch
    $ Pause()
    "Nyx's eyes widened in shock as I began to force my cock back and forth in her mouth."
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_bj_slave with hpunch
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_bj_naked with hpunch
    $ Pause()
    NYX "Mmfhgh! *Slurp!* MMFFHHH! *Slurp!*"
    "Her hot tongue thrashed around and beat against my cock as her lips struggled to wrap around the thick member now forcing its way down her throat."
    "Fucking the mouth of the once uptight Captain Nyx was an exhilarating feeling, as I watched her throat bulge with every motion as she struggled to handle the meat,"
    "She felt incredible, the feeling of her mouth was euphoric."
    "There was greedy, neediness to her eyes, she had missed this indeed, missed feeling my cock sliding down her throat, {i}missed feeling so very powerless to me.{/i}"
    NYX "Mmmfhhhh! {i}*Slurp!*{/i}"
    NYX  "(G-Gods!)"
    NYX "(His ... His c-cock is-)"
    NYX "(Mmmfghh! It's just like I remembered!)"
    NYX "(No! I can't let him know! I can't let him know my legs start shaking when he walks in the room now!)"
    NYX "(A-Ahhh! It's like everything is rushing to my head at once ... I'm feeling so dizzy!)"
    "Her technique, while still clumsy, had improved with practice."
    "More than anything, she seemed determined to ensure I was satisfied as a matter of pride... Not that she'd ever admit it."
    "With her teeth lightly grazing against my cock occasionally as her eyed began to water, Nyx squirmed and writhed beneath me, torn between hating and loving being treated like an object."
    "Despite this however, from the red flush of her face and despite her light moans of protest, she didn't resist me at all."
    "Nyx once more seemed to be doing her best to relax, her heart racing as she tried to push herself to take my cock deeper than before."
    NYX "(Why does this - Ah! Make me feel so wet?)"
    NYX "(I feel so w-weak being pinned by his strong hands.)"
    NYX "(And his c-cock ... Why does it have to be so big?)"
    NYX "(Ahh... F-Fuck! Just smelling it turns me on!)"
    NYX "{i}*Slurp!*{/i} Mmfghh! {i}*Slurp!*{/i} MMMFF!"
    MC "Ahh! One of these days your men are gonna walk in and - Ahh!"
    MC "Catch you slobbering all over my cock like a greedy whore."
    "Nyx's brow creased as she growled in frustration, but as I continued to slide my cock in and out of her wet mouth, she soon began to relax once more, letting the pleasure wash over her."
    NYX "(N-No... Not again! Mhmm! I wanted to...)"
    NYX "({i}W-Win...{/i})"
    NYX "({i}But it tastes so good...{/i})"
    "As Nyx squirmed, she tapped at my leg for air, her body writhing as she began to wane."
    NYX "MMMFGHH!"
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_lick_slave with dissolve
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_lick_naked with dissolve
    $ Pause()
    "Unsheathing my cock from her throat, Nyx kissed the end of my cock as it popped out of her mouth, letting her gasp for air as she collected herself." #Cock lick tease anim
    "She stared up at the hard cock, coated in saliva, dangling in front of her with almost hypnotic eyes, a silvery saliva trail still connected between her mouth and the well fucked cock resting just above her face."
    NYX "{i}*Huff*{/i} Shooo ... {i}*Huff*{/i} Ghoodh!"
    MC "Haha! Finally ready to submit, slut?"
    NYX "{i}*Huff*{/i} Nev-{i}*Huff*{/i}-er..{i}*Huff*{/i}"
    NYX "{i}*Huff*{/i} Make... {i}*Huff*{/i}"
    NYX "{i}Me!{/i}"
    MC "Ha, how long do you really think you can hold out?"
    MC "{i}You're mine, Nyx. Accept it.{/i}"
    NYX "{i}*Huff*{/i} Shut up - {i}*Huff*{/i}"
    NYX "{i}Break me fucker!{/i}"
    MC "As you wish!"
    "As I pressed the head of my cock against her lips once more, she groaned and began to suckle on it."
    NYX "Mmmhhffh~"
    MC "You'll be my perfect little slave when I'm done."
    MC "An embarrassment to the guard, but you won't care!"
    "Nyx squirmed at the comment, only seemingly turned on more by the humiliation."
    NYX "Shuudhupp!"
    MC "Don't you dare stop this time till you drain my balls dry!"
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_bj_hand_slave with hpunch
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_bj_hand_naked with hpunch
    $ Pause()
    "I rammed my cock back into Nyx's mouth once more."
    NYX "{i}*Slurp!* Mmmfghh! *Slurp!*{/i}"
    NYX "(I'm burning up again ... T-This is so g-ghoodh...)"
    NYX "(I k-keeph looking forward to - Ahh! The N-Nhexthh thimee!)"
    NYXP "({i}You're so FUNNY silly!{/i})"
    MC "Ahh! Nyx! You're m-mouth feels sooo good!"
    MC "Good girl! Ahh! Fuck!"
    NYXP "({i}Your pussy just gets SO wet everytime he calls you a good girl! Hehe!{/i})"
    NYX "(G-Ghoo away! S-Shut up! Shut up! Shut up! SHUT UP!)"
    NYX "(S-Stophh interrupting our fun!)"
    NYXP "({i}Oh honey, I'm not interrupting anything! In fact, I'm just so, SO proud of you!{/i})"
    NYXP "({i}Always worrying about what others think! All that worry sure goes out the window when a real man's cock is in your face though, huh?{/i})"
    NYXP "({i}Isn't it amazing? This is what I told you allll along.{/i})"
    NYXP "{i}And you can't stop thinking about it since you've had a taste so you know I'm right! Now just imagine it!{/i}"
    NYXP "({i}A fat cock rammed down your throat, in your pussy, up your tight ass...!{/i})"
    NYX "(S-Stophhh talking! Grghh!)"
    NYX "(S-Stoph mhessin' with mhyyy headhh!)"
    NYX "(T-Thishh is justhh for some relief! T-Thatshh all!)"
    NYX "Mmfghh! {i}*Slurp!*{/i}"
    NYXP "({i}Ha! It's soooooo funny seeing you try and act like you're still in control when your brain's already turning to mush thanks to master's big, fat cock!{/i})" 
    NYXP "({i}Be a slut. Be a happy little slut for master. It's what you were made for.{/i})"
    NYX "Mmmfghh! Nghhu!"
    MC "Ahh! Did you say something?! {i}*Huff!*{/i}"
    NYXP "{i}(Serve him. Drain his balls. Look beautiful for him and give him as many children as he wants.{/i})"
    NYXP "{i}(Get bigger tits! Get a fatter ass and plumper lips to please him with! Even change your hair if he asks!{/i})"
    NYXP "{i}(We both know it's what you REALLY Want!{/i})"
    NYXP "({i}All these silly worries about fighting and wars!{/i})"
    NYXP "({i}When really you want is somebody just once to put your needs first ... Somebody else to make the difficult choices when you've had enough.{/i})" 
    NYXP "({i}Somebody to fuck your tight cunt senseless so all this stress is at least tolerable!{/i})"
    MC "{i}*Huff!*{/i} I'm gonna c-cum!"
    MC "I'm so close! Hrghh!"
    NYX "Mmmfghhh! {i}*Slurp!* *Slurp!*{/i}"
    NYX "(N-No! I didn't want to lose! I-)"
    NYXP "({i}Shhh, you've already lost you silly slut! So stop worrying and just be his good little girl, alright?{/i})"
    NYXP "({i}And like ALL good little sluts, your man needs you to drain his balls dry already!{/i})"
    MC "OH FUCKKKK!"
    NYX "Mmmfhghh...!!"
    "Unable to hold any longer, I flooded Nyx's throat with my hot load."
    if   tmpvar["clothes"] == "slave":
        scene ss_nyx_facefuck_cum_slave with flash
    elif tmpvar["clothes"] == "naked":
        scene ss_nyx_facefuck_cum_naked with flash
    $ Pause()
    NYX "Glrghh! Glugghh!!"
    "The pleasure washed over me as despite her squirms of shock and pleading to be let go for air, I held my cock down Nyx's throat as I continued to pump her full of my seed."
    NYX "(C-Can't breathe!)"
    "Nyx's eyes began to roll back as she began to lose consciousness..."
    NYX "(There's s-so much cum!)"
    NYX "(Why does it taste so ...so...)"
    NYX "({i}Good...!{/i})"
    "Nyx did her best to swallow down as much of my load as she could, before, finally spent, I unsheathed my cock from her throat." #Fade to black
    "Coughing up the excess cum that run down her chin and onto her breasts."
    "She wheezed for a few moments before she began to settle down, laying there peacefully on the bed without saying a word..."
    NYXP "({i}Mhmm, I'm gonna make sure he's ALLLL you think about from now on, fufu~{/i})"
    NYX "(I...{i}*Huff*{/i} Hate you...)"
    return