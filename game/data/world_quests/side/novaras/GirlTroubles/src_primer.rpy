label primer_girl_troubles_1:
    show mc at cright with easeinleft
    MESSENGER "Wait! Hold up!"
    show mc at blurin, cright_f
    "Stopping in my tracks, I turned to face the young boy hurrying towards me."
    show messenger at cleft with easeinleft
    MC @think "Can I help you?"
    MESSENGER "Sister Divine requests your presence at the tower of Palam at once."
    MC @talk "Sister Divine?"
    MC @talk "Did you say why?"
    MESSENGER "No sir, but she said it was a matter most urgent."
    MESSENGER "Now, if you'll excuse me, I've got to deliver my next message!"
    show messenger at cleft_f
    $ Pause(0.1)
    hide messenger with easeoutleft
    MC "(Hmm... I should stop by the tower of Palam when I get a chance.)"
    $ QstSetProgress(PrimerGirlTroubles, 1)
    $ NoteUnlock("GirlTroublesNote")
    $ LocEnter()

label primer_girl_troubles_2:
    show divine at center_f
    with dissolve
    show mc at left with dissolve
    if QstIsActive(RomanceDivine):
        DIVINE @talk "Ah, there you are."
        "Divine steps out from behind her desk, a playful glint in her eye as she moves closer."
        hide divine
        hide mc
        show cg_mc_divine_kiss at center
        with dissolve
        "Without a word, she wraps her arms around me, her lips finding mine in a slow, deliberate kiss."
        MC "(Her touch is familiar, warm...)" 
        "My hand drifts down instinctively, fingers grazing her waist before resting on her backside."
        DIVINE @happy "Mmm... You never change, do you?"
        "She lets out a soft, breathy laugh, before gently pushing away, cheeks flushed."
        hide cg_mc_divine_kiss
        show divine at center:
            yoffset 50
        with dissolve
        MC @smile "That's quite a desk you’ve got there, you know. I'd love to see you—"
        DIVINE @laugh "Easy, easy! I didn’t call you here for {i}that.{/i}" 
        DIVINE @happy "Though, maybe later... if there's time."
    else:
        "Sister Divine stands behind her desk, her expression unreadable as she watches me enter."
        DIVINE @talk "It’s good to see you again. I’ve been meaning to speak with you."
    #Both routes continued
    MC @talk "So, what's this about?"
    DIVINE @talk "Tell me, what do you know about the tower?"
    MC @think "Hm? Not much..."
    MC @talk "I know mages of Palam are taken from their parents from a young age to join the order."
    DIVINE @talk "Being a mage is a lifelong commitment, and many start young at one of the smaller holds before coming here."
    DIVINE @talk "It's best to think of this tower as a kind of university, but to mages, any hold under their magecraft is considered a second home they're expected to return to throughout their life periodically."
    DIVINE @talk "Suffice it to say I care for each and every girl who comes here, many of whom I've known to some degree since they were small."
    MC @talk "I see... But why the urgent summoning? Where do I fit into all this?"
    DIVINE @talk "Since this war began, Mages have been, with the end of every terminus ceremony, sent towards the front."
    DIVINE @talk "Thankfully, many of my girls are usually kept back to help deal with the wounded, so losses are limited."
    DIVINE @talk "With that said, Alcott's government continues to put more and more pressure on getting out the door, regardless of capabilities."
    "Sister Divine paused uncomfortably."
    DIVINE @talk "... Last month, four of my girls stationed at a camp were killed by a surprise ambush."
    DIVINE @talk "From what reports I have, the girls panicked and fumbled their spells."
    DIVINE @sad "... They weren't ready."
    MC @sad "That's horrible."
    DIVINE @angry "Standards are slipping..."
    DIVINE @sad "And my girls are dying for it."
    menu primer_girl_troubles_2_menu:
        "Have you tried appealing to the higher-ups?":
            DIVINE @talk "I've tried."
            DIVINE @talk "The officials don't care for the quality of Mages, only that there {i}are{/i} Mages."
            DIVINE @talk "My concerns fall on deaf ears."
            jump primer_girl_troubles_2_menu
        "Forgive me, but people die in war... As horrible as it may be Sister, it's almost inevitable some won't come home.":
            DIVINE @angry "I am aware people 'die' in war; I'm not a fool."
            DIVINE @talk "But there are only ever so many mages per year, and magecraft is a lifelong commitment to master."
            DIVINE @talk "It's not as simple as replacing a simple grunt... No offense."
            MC @talk "None taken."
            jump primer_girl_troubles_2_menu
        "I'm still waiting to hear what I have to do with this...": #continues story
            DIVINE @talk "Three girls of mine, troublesome issues with each."
            DIVINE @talk "I've put my foot down and held them back from being assigned to the front."
            MC @talk "Why?"
            DIVINE @talk "They're not ready... And I'm not prepared to knowingly send some of my girls to their deaths."
            DIVINE @talk "Now, I don't have time to resolve these issues myself; I have to prepare the next batch of mages, who are already showing similar issues, for next year's terminus ceremony."
            DIVINE @talk "I want you to become their... Mentor."
            MC @surprised "Mentor? Me? I don't even possess any magecraft!"
            DIVINE @talk "Ah, but that's where you and your 'gift' come in nicely."
            DIVINE @talk "The Alderian government have refused to send me a mage capable of helping me, so I need the next best thing."
            DIVINE @talk "Someone capable of really motivating these girls."
            MC "(Meaning someone she can threaten to blackmail if I ever speak about what I see in here.)"
            MC @talk "How am I supposed to do that?"
            DIVINE @talk "The method doesn't concern me; as long as the girls aren't harmed, I don't care what you do. "
            DIVINE @talk "For each girl dealt with, I'll give you seven hundred coins. Does that sound fair?"
            menu primer_girl_troubles_2_menu_2:
                "But why ask me?":
                    DIVINE @talk "Because I need someone I can trust with this,"
                    DIVINE @talk "And after hearing from Captain Nyx about your recent help with her, it only made sense to ask you."
                    MC @talk "Wait ... Captain Nyx?"
                    DIVINE @talk "The Captain and I are ... {i}often aligned{/i} when necessary."
                    DIVINE @talk "I'd hardly call us friends, but we've come to depend on each other's resources sometimes."
                    jump primer_girl_troubles_2_menu_2
                "What do you mean by {i}you don't care what I do?{/i}":
                    DIVINE @talk "I mean, {i}I don't care what you do.{/i}"
                    DIVINE @talk "As long as they are not hurt, and you don't make a public spectacle of whatever you do with them, I only care about the end results."
                    jump primer_girl_troubles_2_menu_2
                "Who are the girls?": 
                    DIVINE @talk "I cannot tell you until you agree to my request, but I will do my best to answer anymore questions you have." #continues story
                    menu primer_girl_troubles_2_menu_3:
                        "Is it truly that shameful for them?":
                            MC @talk "Mages of Palam are holy ordained, after all."
                            DIVINE @angry "It is shameful when you're praying for a strong male heir or a daughter that you can marry off to another rich noble."
                            DIVINE @talk "Us Mages of Palam are seen as a dead end."
                            MC @talk "But can't Mages of Palam continue a bloodline?"
                            MC @talk "You can sire young with women and can get pregnant yourselves, can you not?"
                            MC @think "How then are you a dead end?"
                            "Sister Divine smiled."
                            DIVINE @happy "It's best not to dwell on such things; we're an uncomfortable blot they've had to learn to accept and tolerate {i}on their terms.{/i}"
                            DIVINE @talk "They prefer the fantasy of us as saint like beings, not real people with real wants and desires." 
                            jump primer_girl_troubles_2_menu_3
                        "And one of these girls comes from these families, I take it?":
                            DIVINE @talk "Yes, to which I expect you to speak to no one."
                            DIVINE @talk "I cannot stress how important these families expect privacy."
                            DIVINE @talk "If they believe we're making a spectacle, those {i}generous donations{/i} will very quickly dry up." #Loops back to the previous menu
                            jump primer_girl_troubles_2_menu_3
                        "I will help you.": #continues story
                            DIVINE @happy "Good, it pleases me to hear that."
                            MC @talk "So what now?"
                            DIVINE @talk "Now you've agreed, I can talk more about the girls in question."
                            DIVINE @talk "There's Jana, Zara and Mika."
                            DIVINE @talk "Which one do you want to know about?"     
                            $ tmpvar = []
                            menu primer_girl_troubles_2_menu_4:
                                "Tell me about Jana." if 0 not in tmpvar:
                                    DIVINE @talk "Ah, Jana Rosenval..."
                                    DIVINE @talk "Her abilities are extremely promising, and she is one of the highest potential candidates I've seen in years."
                                    MC @talk "Then what's the issue?"
                                    DIVINE @angry "Her attitude."
                                    DIVINE @angry "She's been consistently troublesome for as long as I've known her, but the situation this last year has spiraled completely out of hand."
                                    MC @talk "How {i}'out of hand?'{/i}"
                                    DIVINE @talk "Setting a lecture hall on fire, sneaking out and being caught dancing topless at a tavern, constantly getting it brawls with the other girls... The list goes on."
                                    MC @talk "Any idea what's causing the trouble?"
                                    DIVINE @talk "She does come from a particularly {i}'troubled'{/i} home, and it's always been a difficult subject for her to talk about."
                                    MC @talk "How troubled?"
                                    DIVINE @talk "There were signs of physical abuse, but she's never been willing to talk about it."
                                    DIVINE @talk "I need you to help curb her personality issues and deal with whatever's going on in her head."
                                    if 3 not in tmpvar:
                                        $ tmpvar.append(0)
                                    jump primer_girl_troubles_2_menu_4
                                "Tell me about Zara." if 1 not in tmpvar:
                                    DIVINE @talk "Hm, yes, Zara Dawnmoore."
                                    DIVINE @talk "She comes from a wealthy aristocratic family from the south before the war forced them to flee North."
                                    DIVINE @talk "She was a perfect student during her time here, consistently scoring highest on her arcane knowledge and abilities."
                                    DIVINE @talk "Then, during the terminus ceremony, the {i}'incident'{/i} occurred."
                                    MC @think "The 'incident?'"
                                    DIVINE @talk "Before the ceremony, Zara was reported to be in high spirits, if a little tense and on edge."
                                    DIVINE @talk "But the same could be said of any of the mages at the time, so it was dismissed as the usual pre-ceremony anxiety."
                                    DIVINE @talk "A short while after the ceremony, however, Zara received a letter from her parents, who couldn't attend."
                                    DIVINE @talk "She burned the letter before anyone could read it, but whatever was in that letter triggered something within her."
                                    DIVINE @talk "In the night, she went on a rampage, attacking everyone in sight."
                                    DIVINE @talk "It took myself and two other high mages to restrain her abilities, and in the meanwhile, over a dozen students were hurt."
                                    DIVINE @talk "We thought it might have been {i}'Mages madness,'{/i} but there was no sign of it."
                                    MC @talk "What was in the letter?"
                                    DIVINE @talk "We don't know, and Zara won't say."
                                    DIVINE @talk "Now Zara is pretending she had some momentary lapse of judgment and is acting her usual self again."
                                    DIVINE @talk "I'm not going to risk sending her out knowing she could explode at any moment."
                                    MC @talk "I don't remember hearing about this incident anywhere?"
                                    DIVINE @talk "That's because we've buried it and managed the incident in-house ... For now, at least."
                                    DIVINE @talk "I need you to get to the bottom of this issue and deal with it ... fast."
                                    if 3 not in tmpvar:
                                        $ tmpvar.append(1)
                                    jump primer_girl_troubles_2_menu_4
                                "Tell me about Mika." if 2 not in tmpvar:
                                    DIVINE @talk "Yes, Mika Ursan, a lovely girl."
                                    DIVINE @talk "Afraid of her own shadow, but lovely."
                                    MC @talk "{i}Afraid of her own shadow?{/i}"
                                    DIVINE @laugh "I know, I know, but believe me—she panics at the sight of a sparring partner."
                                    DIVINE @talk "Mika's an odd case; her family adore her and refused to hand her over till much, {i}much{/i} later than we usually take on mages."
                                    DIVINE @talk "As such, she has a strong natural sense of her abilities despite displaying very average arcane knowledge."
                                    MC @talk "So, what's the issue?"
                                    DIVINE @talk "{i}The girl is terrified of fighting...{/i}"
                                    DIVINE @talk "She completely failed in any and all practical combat training classes previously."
                                    DIVINE @talk "She just ... cowered."
                                    MC @talk "Then how has she got this far?"
                                    DIVINE @talk "Because practical combat for mages of the Palam is the one thing you {i}can{/i} still fail at and still be allowed to serve in the rear as a healer."
                                    DIVINE @angry "Suffice it to say this push to get mages to the front in quantity rather than quality has been a great source of tension between the council of Mages and the Alderian government."
                                    DIVINE @talk "Now, whilst combat isn't the priority for a mage of Palam, {i}I firmly believe every mage must be able to defend herself in times of crisis.{/i}"
                                    "Sister Divine's face fell darkly."
                                    DIVINE @sad "If the recent deaths are anything to go by ... I've only been proven right."
                                    MC @think "So, you want me to train the girl to fight?"
                                    DIVINE @talk "I need you to teach her to conquer her fears."
                                    DIVINE @talk "She {i}has{/i} to be able to fight if the time comes."
                                    MC @talk "And if she refuses to listen? She's an adult now; she doesn't have to listen to either of us." 
                                    DIVINE @talk "I don't care {i}how{/i} you get her to agree, but I need to know she can handle herself out there."
                                    # After selecting each of the girls 
                                    if 3 not in tmpvar:
                                        $ tmpvar.append(2)
                                    jump primer_girl_troubles_2_menu_4
                                "I think that's it." if (len(tmpvar) >= 3 or 3 in tmpvar):
                                    $ tmpvar = [3]
                                    DIVINE @talk "Now then, should I introduce you to the girls?"
                                    menu primer_girl_troubles_2_menu_5:
                                        "Tell me about the girls again.":
                                            DIVINE @talk "Alright, which one?"
                                            # Menu here looping about the girls to ask about (again)
                                            $ tmpvar = []
                                            jump primer_girl_troubles_2_menu_4
                                        "Let's meet the girls.":
                                            $ tmpvar = {}
                                            DIVINE @talk "Alright, come with me, I shall introduce you."
                                            pass
                                            # continues to below
                                        "I'll get back to you on it shortly.":
                                            $ tmpvar = {}
                                            DIVINE @talk "Return as soon as you can ... I want this trouble behind me sooner rather than later."
                                            hide divine with dissolve
                                            $ QstSetProgress(PrimerGirlTroubles, 2)
                                            $ LocEnterQ()
                        "I'll need some time to think on this.":
                            DIVINE @talk "Of course, but please, give me your answer soon ... Time is a luxury we don't have." #Exits menu
                            #Upon re-speaking to Sister Divine 
                            hide divine with dissolve
                            $ QstSetProgress(PrimerGirlTroubles, 2)
                            if GetLocID() == 'novaras_palam_divine_office':
                                $ LocSet("novaras_palam_e_wing")
                                $ LocFlush(fade)
                            $ LocEnterQ()
    ###########################################################################################################################################
    #Scene 2 - Girls dorm - Tower of Palam 
    #Brief fade to black 
    scene black 
    with dissolve

    $ LocSet("novaras_palam_dorm")
    $ LocFlush()
    show divine at center
    with dissolve
    "A short journey later to the girl's dorm..." #Text on screen 
    "Upon entering the girls' dorm, the immediate warmth of the room hit me from the warm blazing fire."
    "We all knew mages had it easy compared to the rest of us, even young apprentices, but this was leaps and bounds ahead of my experiences."
    DIVINE @happy "Girls! Come!"
    $ CharSetClothes("mika", "dress")
    show mika at right_f with dissolve
    show zara at left with dissolve
    "Sister Divine clapped her hands, and two girls approached, one, the blonde, still yawning after she rolled herself off the side of her bed before dragging herself towards us."
    "When the two girls saw me, the dark-haired one remained stoically unmoved, but the blonde blushed and smiled."
    MIKA @blush "Ooooh! H-Hello!"
    DIVINE @think "Mika."
    MIKA @shock "W-What I do this time?"
    "The second, much more serious girl adjusted her glasses before speaking."
    ZARA @talk "Try to control yourself, Mika."
    MIKA @angry "I - I was just saying hello!"
    MIKA @sad "W-We never get any men visiting us hardly!"
    MIKA @blush "Especially not m-men so..."
    "A shy, blushing Mika averted her gaze and giggled lightly."
    MIKA @blush "Y-You look like you could plow a whole field with just one hand..."
    play sound2 "audio/cfx/zara_slap_mika.ogg"
    show zara at nod
    show mika at shake
    "The other girl, Zara, lightly slapped Mika over the back of the head."
    MIKA @angry "O-Ow!"
    ZARA @talk "We both know the only {i}field{/i} you want to have plowed isn't on any farm."
    MIKA @angry "Grrrr!"
    DIVINE @angry "Oh, for the love of-"
    DIVINE @talk "Right, as I'm sure you've guessed, this is Mika and Zara."
    MIKA @smile "N-Nice to meet you!"
    ZARA @talk "A pleasure, I'm sure."
    DIVINE @talk "This is [player_name!t]; he will be acting as my assistant for a while, so do treat him with the same respect as you would me."
    "The two girls seemed bewildered, though Mika let it show far more."
    MIKA @shock "H-HUH?!"
    MIKA @shock "You m-mean ... A MAN'S ACTUALLY GOING TO BE WORKING HERE?!"
    ZARA @shock "Is this person even qualified? I don't sense any magecraft coming from the person."
    DIVINE @talk "I assure you, Zara, there are no rules {i}requiring{/i} people to have magecraft to work within the tower, nor are men technically barred."
    ZARA @talk "Hmph ... Very well."
    MIKA @angry "Hey! We want {i}more{/i} men around here! Not less!"
    ZARA @talk "All you think about is farming and flirting with boys!"
    MIKA @talk "T-That's not true! I think about - {i}*Yawn*{/i}"
    DIVINE @talk "Mika, were you sleeping again?"
    MIKA @sad "N-No...?"
    DIVINE @angry "How convincing..."
    ZARA @talk "Mika tried to sneak out again under Jana's guidance."
    MIKA @angry "N-No I didn't!"
    DIVINE @angry "MIKA!"
    MIKA @shock "It ... It wasn't my fault!"
    MIKA @shock "Jana said-"
    DIVINE @angry "Jana says a lot of things! You know better!"
    "Sister Divine looked around the room."
    DIVINE @shock "...Wait, where is Jana?"
    "The two girls stared at each other, uncertain how to answer, then back towards Sister Divine."
    MIKA @talk "Uhhh..."
    DIVINE @angry "Mika."
    DIVINE @angry "Where is she?"
    MIKA @talk "W-Well, funny story..."
    MIKA @smile "J-Jana, you see, s-said to go back to the tower without her..."
    DIVINE @shock "WHAT?!"
    MIKA @shock "I t-tried to talk her into coming back, but she wouldn't listen!"
    DIVINE @angry "Grghh! That girl is-"
    DIVINE @talk "{i}*Deep breath*{/i}"
    DIVINE @talk "I'm going to find Jana. The two of you are to follow under [player_name!t]'s direction while I'm gone."
    ZARA @angry "I don't need to be watched over by someone like a child; in fact, the reasoning behind me being held back at all is ludicrous."
    MIKA @angry "Yeah! Me too! I p-passed everything just fine!"
    DIVINE @angry "Neither of you are moving on till I'm satisfied."
    DIVINE @angry "Now excuse me, I have places to be."
    "Sister Divine looked knowingly towards me."
    DIVINE @happy "Let me know if they try anything funny."
    DIVINE @angry "I have more than one way of punishing disobedient brats."
    MIKA @shock "I ain't a rat!"
    ZARA @think "She said {i}brat{/i} you moron."
    MIKA @angry "Grrr! D-Don't call me a-"
    DIVINE @angry "ENOUGH."
    DIVINE @talk "Now goodbye, girls ... {i}BEHAVE{/i} while I'm gone."
    ZARA @talk "...Yes Ms."
    MIKA @talk "Y-Yes ma'am."
    hide divine with dissolve
    "Sister Divine turned to leave, leaving me alone with the two girls who stared expectantly towards you."
    MC @smile "So, then, how about we-"
    ZARA @talk "I've got things to do."
    MIKA @talk "Uhh, m-me too!"
    hide zara with moveoutleft
    hide mika with moveoutright
    "The two girls scurried away ... Looks like this might be tougher than it looks."

    $ QstComplete(PrimerGirlTroubles)
    $ NoteLock("GirlTroublesNote")
    $ CharMeet("zara")
    $ CharMeet("mika")
    $ LocEnterQ()

label primer_girl_troubles_2_menu_repeat:
    DIVINE @talk "Have you decided whether you'll help me?"
    jump primer_girl_troubles_2_menu_3