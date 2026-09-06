label qst_BiteBark_4_BuyMeat:
    show butcher at cright_f 
    with dissolve
    show mc at left with easeinleft
    show elena_w at cleft with easeinleft
    BUTCHER "Ahh... You look like a man who appreciates only the finest meat!"
    BUTCHER "Interested in what you see?"
    BUTCHER "Or perhaps some meat for your friend here?"
    MC @talk "Yes, I'd like something for my... companion."
    BUTCHER "Of course sir."
    "Turning to face my furry companion, I knelt down and held out a piece of fresh meat which she gently took from my hand."
    "After a few moments, she had quickly made short work of the meal."
    hide butcher with dissolve
    MC @smile "Well, someone was hungry!"
    "Gently, I reached out to pet the wolf, but instinctively she moved back away from my hand."
    hide elena_w with dissolve
    MC @sad "(Hm, this could be tougher than I first thought.)"
    ADARA @talk "[player_name!t]?"
    show adara at cright_f with easeinright
    MC @surprised "Adara?"
    show mc at cleft with easeinleft
    ADARA @smile "It's good to see you!"
    ADARA @talk "How goes all that adventuring?"
    MC @talk "As well as it can I suppose."
    MC @smile "I just came here to get some food for this one."
    show mc at blurin, cleft_f
    "As I motioned my hand down towards the wolf, I realized she had wandered off."
    MC @surprised "What?"
    MC @angry "Where did she go?"
    show mc at blurin, cleft
    ADARA @shock "...Umm."
    ADARA @shock "Did you lose something?"
    show mc at blurin, cleft_f
    MC @angry "I... Yes, I need to go find her before she vanishes for good!"
    hide mc with easeoutleft
    "I turned to heel, waving to Adara as I hurried off to find the wolf." #MC off screen for rest of scene
    MC @talk "Talk to you again!"
    show adara at center_f with ease
    ADARA @shock "[player_name!t]! Wait! I-"
    ADARA @sad "{i}*Sigh*{/i} maybe next time..."
    hide adara with dissolve
    $ Pause(0.25)
    show mc at center_f with easeinright
    MC "(She couldn't have gone too far...)"
    hide mc with easeoutleft
    $ QstSetProgress(QstBiteBark, 4)
    window hide
    $ LocSet("novaras_dist_market")
    $ LocFlush(dissolve)
    $ LocEnterQ()
