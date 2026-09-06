
label rom_ElenaRepCooking:
    ELENA @talk "{i}Cooking?{/i}"
    show elena lewd
    ELENA @lewd "... Is it the food you're asking for, or-"
    MC "..."
    ELENA @lewd "I um, I'll get the apron and start then."

    $ AutoMus(False)
    $ PlayMusic(wLocs["mc_house_kitchen"].dn_music.dayTrack)
    
    call center_text(_("Twenty minutes later...")) from _call_center_text_3

    $ PlayMusicRandom("mus_sex")
    $ HideUI(True)
    $ tmpvar["elena_cooking_clothes"] = CharGetClothes("elena")
    $ CharSetClothes("elena", "apron")
    scene elena_cooking_1 with dissolve
    'Between my legs, Elena wrapped her tits shyly around my cock and pressed them together.'
    'Moving them up and down, her face flushed red from embarrassment.'
    ELENA "H-How's this?"
    ELENA "Does it feel nice?"
    MC "Ahh! Elena ...!"
    "Caught off guard, Elena's warm breasts squeezed my thick member with ease."
    ELENA "Hey! Your food will go cold!"
    ELENA "J-Just let me carry on down here, okay?"
    "Did Elena really think this was some normal daily occurrence between lovers? Or was she just playing along for my sake?"
    "Grabbing the spoon, I did my best to try and focus on the food like she asked, but it was impossible to focus on it with what was going on beneath the table."
    "Every time I ate the food though, Elena with her elated smile would move faster, pressing her breasts together tighter as she worked my cock teasingly."
    ELENA "I'm doing a good job, huh? {image=[ICON.HEART]}"
    "I simply grunted in response, my cock began to tighten as the hot pressure mounted."
    MC "{i}*Huff*{/i} E-Elena ... Mmff ..."
    ELENA "{i} ... Tell me I'm a good girl?{/i}"
    MC "Ahh ...! What?"
    ELENA "{i}Tell me I'm a good girl who'll get lots of head-pats for this!{/i}"
    MC "Ahh! You're the best girl, Elena! The bestest girl!"
    ELENA "{i}*Heavy breathing*{/i} {image=[ICON.HEART]}"
    ELENA "T-That's right, {i}I am a good girl!{/i}"
    ELENA "And g-good girls get all the affection!!"
    scene elena_cooking_2 with dissolve
    "Elena seemed almost possessed, huffing and panting as she furiously milked my cock."
    MC "A-Ahh! T-That's it! Elena!"
    MC "I'm close ...!"
    ELENA "D-Do I make a good s-slut too for you?"
    MC "(Just what has [regina_ref_cap!t] been teaching her?!)"
    MC "Y-Yes! You're a good slut for me Elena!"
    ELENA "Ahhh! It's so shameful hearing you talk about me like that ..."
    ELENA "Do it more! Give your head-pat slut all of your cum!"
    ELENA "I want all of it to cover me like a good slut!"
    MC "(Oh fuck! I can't hold it anymore!)"
    MC "HRGHHH! E-ELENA YOU SLUT!" 
    "Unable to hold back any longer, Elena gasped as felt the first stream of hot cum splash onto her tits and face." #Cum
    scene elena_cooking_finish_1 with flash
    $ ReduceInfectionFromSex("elena")
    ELENA "Ooh!"
    "As another stream of my cum splashed onto her, and then another ... and another, Elena giggled and laughed, half in arousal, half embarrassment."
    ELENA "Does it ever stop?"
    MC "{i}*Huff*{/i} Around you? {i}*Huff*{/i} Never."
    ELENA "Fufu ... {image=[ICON.HEART]}"
    #Fade to black 
    $ PlayMusic("audio/music/33_Elena.ogg")
    scene black with dissolve
    '... After that, Elena rose to her feet and began to try and wipe the cum out of her fur, returning to her usual self.'
    $ HideUI(False)
    scene bg_mc_house_kitchen with dissolve
    #back to showing characters etc 
    show mc at cleft
    show elena grumpy at cright_f
    with dissolve

    ELENA @grumpy "AHHH! It's all in my fur!"
    MC @think "You weren't complaining a moment ago."
    ELENA @grumpy "Yes, but now I have to actually deal with the consequences of my actions!"
    "Elena after her grumbles became shy once more."
    show elena sad
    ELENA @sad "So ... You did enjoy that, right?"
    ELENA @sad "You didn't just say all that stuff to make me happy?"
    ELENA @angry "And don't think for a moment I'll tolerate you calling me a slut!"
    show elena grumpy
    ELENA @grumpy "T-That was just pillow talk I've been practising."
    MC @smile "Haha, of course you made me happy."
    MC @smile "If only I could have all my food like that!"
    ELENA @lewd "W-Well ... We'll see."
    ELENA "({i}I can't believe her advice worked so well ... I thought it strange at first she was so open discussing these things but-{/i})"
    ELENA "(No, I shouldn't dwell on it too much!)"
    ELENA @smile "A-Anyway then, I'm going to clean myself up."
    show smile
    ELENA @smile "Be back shortly."
    show elena smile at cright
    hide elena smile with easeoutright

    scene black with dissolve

    $ AutoMus(True)
    $ CharSetClothes("elena", tmpvar.pop("elena_cooking_clothes"))
    $ LocEnter()

