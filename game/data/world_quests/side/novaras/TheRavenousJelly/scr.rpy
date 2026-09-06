label qst_ravenJelly_inspectSlime:
    if QstRavenousJelly().growStage == 1:
        "The small slime creature inside slithered around in its container."
        "It seemed to look towards me when I peered inside, so I know I have its attention."
    elif QstRavenousJelly().growStage == 2:
        "The slime was slithering around inside of its container."
        "It seemed slightly larger than the last time I saw it, and its reactions sharper as it looked expectantly towards me."
    elif QstRavenousJelly().growStage == 3:
        "The slime was noticeably larger than before, and once it noticed me, it waited expectantly for another feeding." 
    elif QstRavenousJelly().growStage == 4:
        "The slime now was literally dripping outside of the rims of the container, its size having grown considerably."
        "It looked towards me once again, waiting for food."
    menu qst_ravenJelly_inspectSlime_menu:
        "Feed the slime." if PlayerItemQty("red_meat") > 0:
            if QstRavenousJelly().fedToday:
                "The slime doesn't seem interested in any more food today."
                jump qst_ravenJelly_inspectSlime_menu
            else:
                $ QstRavenousJelly().fedToday = True
                $ PlayerRemItem("red_meat", 1)
                "As I gently placed down the meat, the slime crawled its way eagerly towards it and began to swallow the meat whole."
                "Through its translucent body, I could see the meat slowly dissolving inside of it."
                "Satisfied, I closed the lid."
                if QstGetProgress(QstRavenousJelly) == 1:
                    $ QstSetProgress(QstRavenousJelly, 2)
                MC "(I should feed it again tomorrow I guess.)"
                jump qst_ravenJelly_inspectSlime_menu
        "Close the lid.":
            "I gently closed the lid and put the container back underneath my bed."
            $ LocEnterQ()

label qst_ravenJelly_enterMyu:
    show mc at cleft with easeinleft
    "I stood frozen as I saw the container in which the slime had been contained had spilled over onto the floor."
    "Before me, the mass of goo stared and looked inquisitively before it shifted and formed, its body changing to that of... {i}a woman?{/i}"
    show myu at cright_f with dissolve
    "It clearly didn't need to blink, its whole body was some translucent blue goo, but it did so anyway as it opened its mouth to mimic speaking."
    MYU @scared "M-Myu?"
    MC "(Oh shit...!)"
    $ CharMeet("myu", DefaultRel = "rel_friend")
    "Instinctively, I reached for the handle of my blade, but stopped myself short of drawing it."
    MC @surprised "Uhh, hello?"
    MYU @talk "...M-Myu... Myu!"
    MC @think "Uh, is that your name?"
    MC @smile "Myu?"
    "The thing turned its head inquisitively at the comment."
    MYU @think "{i}...Myu?{/i}"
    MC @talk "Yes, {i}you{/i} are Myu."
    "I pointed towards myself."
    MC @talk "Me... [player_name!t]."
    "The slimelark pointed towards herself."
    MYU @smile "...Myu?"
    MC @smile "Yes, Myu!"
    "Myu beamed brightly."
    MYU @joy "Myu!"
    "I had no idea where the name Myu came from, or why it was the only word she seemed to vocalize."
    "Nor did I even realize slimelarks could even actually communicate with people."
    MC @think "Where did you learn to take that form?"
    "Myu turned her head inquisitively."
    MYU @think "...Myu?"
    MC "(Hm, don't think I'm going to get any answers from her about that one.)"
    "From outside my window, I had at least one answer."
    "Peering out, I realized the slime must have been watching the people passing by and decided to try mimic one of the girls it had seen."
    "Or perhaps, someone who it had seen in the house?"
    "Whatever the reason, why it decided to choose a female form is anyone's guess."
    "Myu approached me, and for a moment, I felt the instinctual need to pull away after what I'd seen slimelarks were capable of."
    "I sensed no hostility coming from her though, instead, I sensed {i}something else.{/i}"
    MYU @blush "Myuuu~"
    "Myu pressed her body up against me and the cool sticky slime of her body tingled pleasantly to my touch."
    "The breasts she had formed of the same substance were somehow... firmer, as though she knew to alter that part of her body somehow."
    MC @lewd "U-Uhh, what are you-"
    MYU @blush "...Myu {image=[ICON.HEART]}"
    MC @surprised "Whoa! Whoa!"
    "I lightly pushed a slightly confused Myu away."
    MYU @think "...Myu?"
    MC "(Shit, this was a terrible idea.)"
    MC "(What was I even thinking taking it... {b}her{/b} home with me?)"
    MC @talk "Listen, uh, you can't stay here."
    MC @talk "You need to go back to be with your own kind."
    "Myu tilted her head at the comments, clearly not understanding."
    MC "(...Great.)"
    MC "({i}Looks like getting rid of her is out of the question{/i}.)"
    MC "(How am I going to keep this a secret from [regina_ref!t]?)"
    MC @talk "Umm, Myu..."
    MC @think "Do you know how to hide?"
    "Once again, Myu didn't answer, staring blankly at me."
    "Grabbing the container, I pointed towards it."
    MC @talk "Can you get back in here?"
    "Myu once again stared blankly."
    MC "(Fuck, this is no good! If she doesn't even understand, then-)"
    "From outside, I could hear the sounds of the front door's hinges creak as it swung open."
    REGINA "I'm home!"
    MC '(Fuck!)'
    MYU @scared 'M-Myu?'
    "I pointed frantically to the container once again in the hopes that Myu might understand."
    MC @scared "{i}*Hushed*{/i} Myu! Hide in here! {i}Please!{/i}"
    "[regina_ref_cap!t]'s footsteps towards my room drew ever closer."
    REGINA "[player_name!t]? Are you home?"
    "Myu suddenly smiled, finally understanding what I wanted."
    MYU @smile "Ah! Myu!"
    hide myu with dissolve
    "Myu dissolved before me into a liquid-like puddle and crawled her way quickly towards the container, filling it with herself."
    "The container was clearly overflowing, but as long as I hide it away from prying eyes, it could go unnoticed."
    show mc at blurin, cright_f with easeinleft
    show regina at cleft with easeinleft 
    "As the door handle to my room turned, I quickly pushed the container aside, waiting for [regina_ref!t] to enter."
    REGINA @smile "Ah! There you are!"
    REGINA @talk "Why didn't you answer me when I called?"
    MC @smile "Uhh, sorry."
    MC @smile2 "I was just a little distracted is all."
    REGINA @talk "Hmm, well, I'll be putting some food on soon, I'll make you a bowl if you're staying here."
    MC @smile "Ahh, thanks."
    REGINA @sad "... Is everything alright?"
    REGINA @talk "You seem a little..."
    REGINA @talk "{i}Pale.{/i}"
    MC @surprised "Huh?"
    MC @think "Oh, nothing... Just didn't get much sleep lately."
    MC @talk "Bad dreams."
    "[regina_ref_cap!t] smiled, but from the way her eyes seemed to stare {i}through{/i} me, I had the distinct feeling she didn't quite believe me."
    REGINA @talk "... I see."
    REGINA @talk "Well, food will be ready soon, so I'll leave you be."
    hide regina with easeoutleft
    "[regina_ref_cap!t] gently closed the door behind her, and I sighed with relief."
    show mc at blurin, cleft with easeinright
    show myu at cright_f with dissolve
    "Myu poured herself back out once again and stood before me."
    MC "(That was too close.)"
    MC "(At least this... {i}thing{/i} knows to hide now if someone comes.)"
    MC "(It's better than nothing I suppose.)"
    MC @talk "Myu, you need to hide yourself in there if anyone comes inside, understand?"
    "Myu gently nodded, not understanding all my words clearly, but understanding enough of what she needed to do."
    MC "(Hmmm, it's still too risky to keep her here.)"
    MC "(I need to move Myu somewhere safer.)"
    $ QstSetProgress(QstRavenousJelly, 3)
    MC "(But where?)"
    MC "({i}... Azul's safe-house?{/i})"
    MC "(I'd need to scout it out, but surely its probably been cleared out and boarded up by now.)"
    MC @think "Myu ... We need to go on a little trip now, do you understand?"
    MC @talk "It's not safe for you to stay here."
    MYU @think "... Myu?"
    MC "{i}*Sigh*{/i}"
    MC @talk "Myu, can you {i}hide{/i} once again?"
    MYU @talk "H-Hide?"
    MC @talk "Yes, {i}hide.{/i}"
    "I pointed towards the container once again Myu smiled and repeated the word."
    MYU @joy "Hide!"
    hide myu with dissolve
    "Myu once again poured herself into the container, and after a few minutes of shaking, settled down."
    show mc at cright with easeinleft
    show mc at nod
    MC "(Alright, now let's get her over to Azul's safe house.)"
    scene black with dissolve
    $ LocSet("azul_safehouse")
    $ LocFlush()
    with dissolve
    show mc at cleft with easeinleft
    "The safe house was cold upon entering, but I could sense no other presence here."
    "The shattered window from where that {i}thing{/i} had broken through to escape had been boarded up, and the cellar door was once again locked."
    MC "(Looking at the place, you wouldn't think this was almost the place I died.)"
    "I looked down towards where the cellar was and felt the hairs on my skin stand up."
    MC "(No... Focus now, it's just a empty house.)"
    MC @talk "Myu, it's time to come out now."
    show myu at cright_f with dissolve
    "Myu poured herself out of the container and curiously inspected her new home."
    MYU @think "...Myu?"
    MC @talk "You need to stay here now, okay?"
    MC @talk "This will be your new home."
    MC @talk "It's much safer here."
    "Myu looked around and inspected the interior."
    MC @think "You uh, can start a fire if need be here."
    MC @talk "There's still a few logs."
    MC @talk "There's also a bedroom in there..."
    show myu at blurin, cright
    hide myu with easeoutright
    MC @think "Well, not that you {i}need{/i} a bed given what you are I guess."
    "After browsing around some of the other rooms, Myu returned timidly towards me."
    show myu at cright_f with easeinright
    MYU @sad "M-Myu... ?"
    MC @sad "Myu, you need to stay here now, understand?"
    MYU "..."
    MC @talk "I'll be back to check on you and get whatever you need."
    show mc at blurin, cleft_f
    "As I turned to leave, Myu tried to follow me out and I had to stop her."
    show myu at center_f with easeinright
    show mc at blurin, cleft
    MC @talk "No, Myu, {i}stay.{/i}"
    MYU @sad "S-Stay?"
    MC @talk "Yes, Myu, {i}stay,{/i} I'll be back soon."
    show mc at blurin, cleft_f
    hide mc with easeoutleft
    "I turned and left, closing the door behind me after making sure Myu wasn't following this time."
    show myu at blurin, center
    MYU @scared "...M-Myu stay... {i}Here?{/i}"
    scene black with dissolve
    $ QstComplete(QstRavenousJelly)
    $ LocSet("novaras_dist_house")
    $ LocEnter()