label qst_reunion_tavern:
    #EN. PLAYER HAS NEW QUEST TO MEET ADARA AT THE ‘IRON UNICORN’ IN THE EVENING IF THEY SELECTED TO DO SO.
    #SCENE 2
    #IRON UNICORN
    #EVENING
    #EN. THE PLAYER CLICKS ON ADARA WHOSE WAITING IN THE IRON UNICORN
    #scene bg_tavern_night
    show mc at cleft
    show adara at cright_f
    with dissolve
    ADARA @talk "[player_name!t]! There you are!"
    MC @talk "Come, let’s grab ourselves a table somewhere quiet..."
    MC @talk "I imagine we both have a lot to talk about."
    $ QstSetProgress(QstProperReunion, 2)
    #EN. SCREEN FADES TO BLACK, CUTS TO MC AND ADARA SAT TALKING AT A TABLE.
    ADARA @talk "...I must admit, you look so... {i}different.{/i}"
    ADARA @talk "Is the same for Markus?"
    MC @talk "Uhh, yes... We both look a little different now."
    ADARA @talk "I don’t understand... It’s only been a few months and-"
    ADARA @talk "{i}It’s like you’re a different person!{/i}"
    MC @talk "There’s... a lot that happened while out there, Adara."
    show adara at center_f
    with easeinright
    "Adara’s hand reached out to touch mine, it was warm and soft to the touch."
    "Her eyes widened and seemed to almost sparkle against the slightly flickering flames of the candles."
    ADARA @talk "What happened?"
    ADARA @talk "It must have been terrible... whatever you saw."
    play sound "audio/cfx/dark_chime.ogg"
    scene cg_borras_dead with flash
    $ Pause(0.6)
    scene cg_prologue_duprey2 with flash
    $ Pause(0.6)
    scene cg_kiaradeath with flash
    $ Pause(0.6)
    $ LocFlush()
    show mc at cleft
    show adara at cright_f
    with dissolve
    MC @talk "...It wasn’t good."
    MC @talk "I try not to think about it or it all comes back at once."
    "Adara’s hand squeezed mine."
    ADARA @talk "How did you both get home so fast?"
    MC @talk "Honestly Adara, I can hardly remember."
    MC @talk "The battle was something ferocious and everything was a haze."
    MC @talk "We just woke up in the Hospital beds."
    ADARA @talk "Why were you all even sent out in such a hurry?"
    MC @talk "I can’t really talk too much about it..."
    ADARA @talk "What do you mean?"
    ADARA @talk "We were only told you were heading towards Inma to help with the increased attacks around the border there."
    MC @talk "That was a lie."
    MC @talk "The real mission was kept a secret, we scouted deeper into Demorai territory beyond the Valley of Death."
    ADARA @talk "Huh..."
    MC @talk "We were sent to check up on some old fort when we were attacked there."
    ADARA @talk "How many?"
    MC @talk "Hundreds... Maybe thousands, I can hardly remember with the chaos of it all."
    ADARA @talk "[player_name!t]..."
    MC @talk "Me and Markus were the last ones left, we headed down into the underground of the fort and sealed ourselves in this small cavern."
    ADARA @talk "Then what happened?"
    MC @talk "Well..."
    ADARA @talk "...[player_name!t]?"
    ADARA @talk "You can tell me anything, you know that."
    menu:
        'Allude to the Parasites...':
            $ QstProperReunion().toldParasite = True
            "...I can’t tell her everything, but at least I can tell her some part of the truth about what happened back then."
            MC @talk "...Look, you can’t tell anyone about this, okay?"
            MC @talk "It’s not safe for me to even be talking about this."
            ADARA @talk "I won’t say a word."
            MC @talk "There were these... {i}things{/i} down there."
            ADARA @talk "{i}’Things?’{/i}"
            MC @talk "Like pillars but, containing {i}something{/i} inside them."
            MC @talk "When we touched them, we blacked out and woke up in the Hospital back here."
            ADARA @talk "You don’t remember a thing?"
            MC @talk "I... No."
            MC @talk "But something happened in there and it {i}changed{/i} us."
            ADARA @talk "You mean... {i}Something is inside of you both now?{/i}"
            MC @talk "Don’t say it out loud!"
            MC @talk "Gods only know what the inquisitors would do if they found out..."
            ADARA @talk "But... [player_name!t], what if it’s dangerous?"
            ADARA @talk "[player_name!t], you need to see a mage or someone about it!"
            MC @talk "Adara, you have to keep quiet about this."
            ADARA @talk "And I will but..."
            MC @talk "Adara, I’m fine, okay?"
            MC @talk "Just don’t worry."
            ADARA @talk "How can you ask me to not worry about you?"
            MC @talk "Adara, {i}I’m fine.{/i}"
            MC @talk "I {i}feel{/i} fine."
            ADARA @talk "...Alright, if you say so."
            ADARA @talk "But if something happens you have to promise me you’ll get it looked at."
            MC @talk "I promise."
            "Adara smiled faintly, still anxious and perhaps not entirely believing towards my comment."
        'Lie.':
            $ QstProperReunion().toldParasite = False
            MC @talk "I can hardly remember much of it."
            MC @talk "There was just too much adrenaline coursing through both of us."
            MC @talk "We managed to find a back passage out and just kept riding back to Novaras as fast as we could."
            ADARA @talk "Where did the horses come from?"
            MC @talk "They uh, they were just roaming."
            MC @talk "I think they had bolted from the battle and a few had stumbled their way around where we were."
            ADARA @talk "...R-Right."
            MC @talk "Adara didn’t seem entirely convinced with my story, not that it was exactly a very good one."
            ADARA @talk "...But how did you get back so fast?"
            ADARA @talk "I mean, I heard you came back {i}in a week.{/i}"
            MC @talk "Oh, uh..."
            MC @talk "Well you see, we {i}actually{/i} arrived back about a month ago."
            ADARA @talk "A month?"
            MC @talk "Yeah, apparently we just collapsed and we’ve been bed-ridden and in and out of consciousness for days."
            ADARA @talk "Really?"
            MC @talk "Yeah... really."
            "I hate lying to her like this, but it’s for the best."
            MC @talk "Sorry to be the bearer of bad news."
            MC @talk "Our ‘legendary’ ride home is quite the exaggeration."
            MC @talk "No dragons I’m afraid."
            ADARA @talk "You make a joke out of everything."
            MC @talk "Only the serious stuff."
            "She sighed, and concluded:"
            ADARA @talk "Well, the main thing is you’re back at least."
    MC @talk "Now come on, we didn’t just come here for all this serious talk, right?"
    ADARA @talk "U-Uhh..."
    MC @talk "Adara..."
    ADARA @talk "...N-No, of course not."
    ADARA @talk "Sorry, it’s just so hard to think at the moment."
    MC @talk "Adara, forget about these things that trouble you, okay?"
    MC @talk "I’m home now."
    MC @talk "I’m safe."
    MC @talk "I just want to enjoy myself with you like we used to do, is that too much to ask?"
    ADARA @talk "Okay, I’ll try stop with so many of the questions..."
    show adara joy
    "Adara did her best to feign a smile."
    ADARA @talk "I suppose the round is on me?"
    show adara
    MC @talk "Let’s {i}drink.{/i}"
    ADARA @talk "O-Oh! Well, I wasn’t thinking I’d be too late tonight but..."
    ADARA @talk "I don’t suppose one more could hurt too much, right?"
    #EN. SCREEN FADES TO BLACK, TEXT APPEARS, SEVERAL DRINKS LATER...
    scene black
    show text _("Several drinks later"):
        xalign 0.5
        yalign 0.5
    with dissolve
    $ Pause(1.0)
    $ LocFlush()
    show mc at cleft
    show adara joy at cright_f
    with dissolve
    ADARA @joy "{i}*Giggles*{/i} Stop making me laugh so much!"
    MC @talk "What? It’s true!"
    ADARA @joy "Oh gods, so Markus finally has the looks he dreamed of to match the ego!"
    ADARA @joy "Gods help any woman who doesn’t realize he’s an overgrown child..."
    MC @talk "Oh? And what am I?"
    show adara at nod
    show mc at shake
    "Adara lightly shoved me with her hand tipsily."
    ADARA @talk "Oh hush... You know you’re different."
    ADARA @talk "You’ve always been the one to get him out of trouble."
    show adara at center_f
    with easeinright
    "As we talked, I noticed Adara had continued to inch closer and closer to me, finally wrapping her arms around mine as she leaned in, resting her head onto my chest."
    "Her soft hair smelt nice, like hazelnut, it was a smell I thought I would never smell again."
    MC @talk "I think we both tended to get each other into trouble."
    ADARA @talk "Mmm, maybe..."
    ADARA @talk "It all feels like a long time ago now."
    MC @talk "I suppose it was..."
    "Adara looked towards me, her eyes bright and cheeks flushed rosy red as she spoke."
    ADARA @talk "Did you... {i}meet{/i} anyone while in the scouts?"
    MC @talk "What do you mean?"
    ADARA @talk "Like, {i}a girl...{/i}"

    #EN. DEPENDING ON PLAYER CHOICE DURING PROLOGUE REGARDING KIARA, DECIDES IF THE ANSWER IS A ‘LIE’ OR NOT + WHETHER OPTION B APPEARS AT ALL OR IS HOLLOWED OUT.
    menu:
        'No... There was no one else. (Truth.)' if CharGetVar("kiara", "romanced") == False:
            $ QstProperReunion().toldKiara = None
            ADARA @talk "O-Oh... Okay."
            MC @talk "Why do you ask, Adara?"
            ADARA @talk "...W-Well..."
            ADARA @talk "I’ve been thinking a lot recently, and I t-think there’s something I-"
            ADARA @talk "I..."
            MC @talk "Adara, is there something you want to tell me?"
            ADARA @talk "...Just..."
            ADARA @talk "{i}I’m glad you’re home...{/i}"
            MC @talk "...Oh, uh, right."
        'No... There was no one else. (Lie.)' if CharGetVar("kiara", "romanced") == True:
            $ QstProperReunion().toldKiara = False
            ADARA @talk "O-Oh... Okay."
            MC @talk "Why do you ask, Adara?"
            ADARA @talk "...W-Well..."
            ADARA @talk "I’ve been thinking a lot recently, and I t-think there’s something I-"
            ADARA @talk "I..."
            MC @talk "Adara, is there something you want to tell me?"
            ADARA @talk "...Just..."
            ADARA @talk "{i}I’m glad you’re home...{/i}"
            MC @talk "...Oh, uh, right."
        '...Yes, there was a girl.' if CharGetVar("kiara", "romanced") == True:
            $ QstProperReunion().toldKiara = True
            show adara shock
            "Adara’s eyes widened at the answer,"
            ADARA @shock "T-There was?"
            MC @talk "Yes but..."
            MC @talk "She died during the battle."
            show adara
            ADARA @talk "O-Oh, sorry to hear that."
            MC @talk "Yeah, well... We lost a lot of good people so."
    ADARA @talk "Urghhh, sorry."
    ADARA @talk "I feel like I’ve ruined things tonight now."
    MC @talk "Adara, you haven’t ruined anything."
    ADARA @talk "I have, I always do this and-"
    "Pulling Adara closer towards me, she gasped slightly before settling."
    MC @talk "You haven’t done anything wrong."
    ADARA @talk "...You smell so nice."
    MC @talk "I do?"
    "In that moment, she said nothing as Adara’s hand began to trail down, resting over my crotch."
    ADARA @talk "...C-Can I touch you?"
    MC @talk "A-Adara!"
    ADARA @talk "[player_name!t]..."
    ADARA @talk "I’ve missed touching you."
    menu:
        'Let Adara continue':
            pass
        'Stop Adara':
            "Taking Adara’s hand, I slowly pulled it away."
            MC @talk "It’s a little too public for me..."
            ADARA @talk "Oh..."
            ADARA @talk "Well... Alright."
            "Adara’s voice was soft and quiet, she wouldn’t say it aloud but I could tell she was disappointed."
            ADARA @talk "Well... I think it’s time I headed home."
            MC @talk "Let me escort you."
            ADARA @talk "No, I think it’s alright."
            ADARA @talk "You stay here and enjoy your drink."
            ADARA @talk "Goodbye, [player_name!t]."
            MC @talk "Farewell, Adara."
            #EN. ADARA LEAVES
            hide adara with easeoutright
            MC @talk "{i}*Sigh*{/i}"
            "I’m going to need to make up my mind soon about Adara... I can’t keep her waiting like this forever."
            $ QstComplete(QstProperReunion)
            jump ev_AdaraDream_KO_posttavern
            #EN. EVENT ENDS
    MC @talk "Ahh~"
    MC @talk "Adara..."
    ADARA @talk "Shhh, we don’t want anyone to look this way, right?"
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x2.ogg", 1)
    scene adara_tavern_hj_hidden
    with dissolve
    $ Pause()
    #EN. ADARA/MC SEX SCENE PLAYS, MC FONDLING ADARA WHILE SHE SECRETLY JERKS HIM OFF.
    ADARA @talk "{i}By the gods... it’s... even bigger than I remember!{/i}"
    ADARA '{i}He’s changed so much... Just being near him is-{/i}'
    MC @talk "Ahh, Adara... You’re breathing so loud."
    ADARA @talk "S-Sorry, your hand... it feels nice."
    MC @talk "That’s it Adara..."
    MC @talk "Just like that..."
    MC @talk "Ah..."
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x3.ogg", 1)
    scene adara_tavern_hj_seen
    with dissolve
    $ Pause()
    ADARA '{i}This is so exciting...{/i}'
    ADARA '{i}Gods, I could just imagine the ridicule if w-we were caught but-{/i}'
    ADARA @talk "Are you close?"
    MC @talk "Just a little more Adara..."
    ADARA @talk "Mmmhmm, okay."
    #EN. MC CUMS
    $ ReduceInfectionFromSex("adara")
    $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg", 0)
    scene adara_tavern_hj_finish
    with flash
    $ UnlockGalSceneAndGrantXp("adara", "tavern_hj")
    $ Pause()
    ADARA @talk "...!"
    MC @talk "Ahh!"
    "Now {i}that{/i} was a proper reunion."
    $ QstComplete(QstProperReunion)
    "Adara quickly moved to put my cock away before pulling her hand out and licking the fingers."
    MC @talk "Adara!"
    "Adara blushed bright red."
    ADARA @talk "W-What?"
    ADARA @talk "I gotta clean up your mess somehow..."
    ADARA @talk "It’s all over my hands and it’s sticky."
    MC @talk "Well... Still."
    "The thought made me twitch with excitement once again, despite just finishing."
    BLACK "This one longs to sire you many children."
    "Shut up! Shut up! Shut up!"
    BLACK "She would make a good mate."
    ADARA @talk "[player_name!t]? Is something the matter?"
    ADARA @talk "You looked a little lost in thought a second there."
    MC @talk "Uh, sorry."
    MC @talk "Nothing to worry about."
    #BOTH ROUTES CONTINUED
    $ LocFlush()
    show mc at cleft
    show adara joy at cright_f
    with dissolve
    ADARA @talk "Come on, let’s get out of here."
    MC @talk "Now?"
    ADARA @talk "Yes! Now!"
    show adara joy at center_f
    with easeinright
    "Adara’s voice seemed fuller of life, the drink having given her more courage to act a little more reckless than she normally would."
    hide mc
    hide adara
    with easeoutright
    "Taking my hand, Adara practically dragged me from the {i}’Iron Unicorn,’{/i} taking me off on her merry way like I was some prize she had claimed for the night."
    #SCENE 3
    #EXTERNAL
    #EVENING
    $ LocSet("novaras_dist_market")
    $ LocFlush()
    with dissolve
    $ AutoMus(False)
    $ AutoAmb(False)
    $ PlayMusic("audio/music/7_Novaras_D.ogg")
    play ambience "audio/ambience_loc/citynight.ogg" fadein 1.0

    scene adara_alley_hj_bg
    show mc at left
    show adara at cleft_f
    with dissolve

    "Outside the tavern was the usual bustle of life, people passing by as they did some late-night trading towards the market nearby, or those still with drink in hand clearly stumbling their way towards the pleasure District."
    ADARA @talk "Sometimes it feels like Novaras is at the center of the world, doesn’t it?"
    MC @talk "I haven’t seen enough of the world to say."
    ADARA @talk "[player_name!t], would you-"
    show nijah at right_f as stranger1:
        matrixcolor BrightnessMatrix(-1.0)
    show nijah at center_f as stranger2:
        matrixcolor BrightnessMatrix(-1.0)
    show nijah at cright_f as stranger3:
        matrixcolor BrightnessMatrix(-1.0)
    with easeinright
    "As Adara spoke a group of girls past by smiling and giggling amongst themselves, when they saw me, they hurried over and began to surround."
    
    TALL_GIRL "Hey! I know of you!"
    TALL_GIRL "You’re that Scout everyone is talking about!"
    MC @talk "Uhh..."
    WELL_ENDOWED_GIRL "Yes! Him and his friend’s posters are up everywhere!"
    ASSERTIVE_GIRL "Well, they don’t do you justice! Gods handsome, what are you doing this evening?"
    WELL_ENDOWED_GIRL "Sabatha!"
    ASSERTIVE_GIRL "Oh come, I doubt he’s going to complain too much about the attention, right {i}darling?{/i}"
    ADARA @talk "..."
    MC @talk "Uhh, well I-"
    "As the girls began to giggle, Adara brushed past them to lock a hold around my arm."
    ADARA @talk "If you’ll excuse us, he’s my companion for this evening."
    "As Adara began to pull me away, the girls giggled and made some semi-crude remark as Adara led me off."
    hide stranger1
    hide stranger2
    hide stranger3
    with easeoutright
    MC @talk "Adara! Slow down!"
    ADARA @talk "..."
    MC @talk "They’re gone, Adara."
    show adara at cright_f
    show mc at cleft
    with ease
    ADARA @talk "...Y-Yes, um... sorry"
    ADARA @talk "I shouldn’t have pulled you away like that."
    ADARA @talk "I just... didn’t like how they were looking at you."
    MC @talk "How they were {i}looking{/i} at me?"
    ADARA @talk "..."
    ADARA @talk "I don’t like it when other girls look at you like that."
    MC @talk "..."
    ADARA @talk "..."
    show adara at center_f
    with easeinright
    "Suddenly, Adara lept forward once again, this time, pressing her soft lips against mine."
    "I held her for a few moments before pulling her back and she sighed with relief."
    ADARA @talk "...You have no idea how long I have wanted to do that."
    MC @talk "...Adara."
    ADARA @talk "D-Don’t say anything, please."
    if not QstProperReunion().paidForMedicine:
        ADARA @talk "I must get home, father still needs tending to with his illness."
    else:
        ADARA @talk "With the coin for that medicine you gave me, father’s already feeling much better."
        MC @talk "I’m glad to hear that."
        ADARA @talk "So... I don’t have to go home quite so early yet."
        ADARA @talk "Would... Would you maybe follow me?"
        MC @talk "What?"
        $ CharSetVar("adara", "blush", True)
        "Adara’s cheeks burned red."
        ADARA @talk "{i}...Somewhere more private.{/i}"
        MC @talk "Oh... OH!"
        MC @talk "Well, what did you have in mind?"
        $ CharSetVar("adara", "blush", False)
        "Taking a hold of my hand, Adara led me off down to one of the darkened winding back alleyways, where she promptly shoved me against a wall and pressed another kiss onto me."
        $ AutoMus(False)
        $ PlayMusicRandom("mus_sex")
        ADARA @talk "{i}T-Touch me...{/i}"
        ADARA @talk "Please touch me."
        ADARA @talk "I want to feel your hands on me..."
        hide mc
        hide adara
        show adara_alley_fing
        with dissolve
        $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg",1)
        $ Pause()
        "As Adara turned around, my hands trailed up her body and reached up her dress, pressing my fingers against her wet honeypot."
        ADARA @talk "Ahh! [player_name!t]!"
        ADARA @talk "Y-Yes...~"
        ADARA @talk "Just like that, t-touch me however you want."
        "My other hand greedily moved to reach into her dress and fondle at one of her large breasts while I kissed at her soft neck."
        "Adara closed her eyes and let out soft moans as I pushed my fingers deeper into her wet, tight crevices."
        ADARA @talk "{i}Mmmfgh....{/i}"
        ADARA @talk "Your hands are so rough..."
        ADARA @talk "L-Like an animals..."
        MC @talk "{i}*Huff*{/i} Do you need me to slow down?"
        ADARA @talk "N-No... {i}I like it.{/i}"
        "Beneath my skin, I felt the Parasite searing beneath my flesh."
        "I envisioned turning Adara around, throwing up her skirt and having my way with her here and now."
        "The thought became maddening, all consuming as her grunts and soft moans left me shaking, desperate to go further and take her as my mate."
        "...But this was Adara... One of my oldest friends."
        "Biting hard down onto myself, I felt myself twisting my stomach into knots as I resisted my dark impulses."
        ADARA @talk "[player_name!t]... What’s wrong?"
        MC @talk "Nothing {i}*huff*{/i} Just... {i}hard{/i} not to try go further..."
        ADARA @talk "...S-Soon... soon I’ll be ready for you."
        ADARA @talk "If you w-want me like that still."
        "Adara added nervously..."
        ADARA '{i}He... He wants me like that...{/i}'
        ADARA '{i}He wants me!{/i}'
        ADARA @talk "[player_name!t], I-"
        ADARA @talk "Mmhmm!"
        ADARA @talk "I’m cumming! Yes! YES!"
        "Adara’s head moved back onto my shoulder as I felt her tighten around my fingers."
        "her eyes widened as her mouth hung slightly agape, seemingly choking on air as she trembled slightly."
        "As Adara’s head slumped forward and her body began to relax, she breathed in heavily as I loosened my grip on her."
        $ StopSexFx()
        #stop music fadeout 1.0
        $ PlayMusic("audio/music/7_Novaras_D.ogg")
        play ambience "audio/ambience_loc/citynight.ogg" fadein 1.0
        $ UnlockGalSceneAndGrantXp("adara", "alley_fing")
        hide adara_alley_fing
        show mc at cleft
        show adara at cright_f
        with dissolve
        ADARA @talk "...Thank you."
        ADARA @talk "I... I know I shouldn’t have thrown all this on you like that but-"
        MC @talk "Adara, it’s alright."
        "Adara smiled, and moved forward once again to press a quick kiss onto my lips, as though she was re-affirming whatever was going on between us was still real."
        ADARA @talk "Let’s get out of here before someone sees us."
        "The two of left the alleyway as inconspicuously as possible back onto the lit main streets."
    #BOTH ROUTES CONTINUED
    ADARA @talk "W-Will you walk me back?"
    MC @talk "...Of course, Adara."
    "Adara, taking a hold of my hand, let me escort her back home."
    $ LocSet("novaras_dist_farm")
    $ LocFlush()
    show mc at cleft
    show adara at cright_f
    with dissolve
    "Along the way, she leaned in and rested her head onto my chest as we walked across the bridges back towards her humble home, saying very little along the way."
    ADARA @joy "Well... Thanks for walking me back [player_name!t]."
    MC @talk "Yes... Adara, we should talk about-"
    ADARA @joy "Another time."
    ADARA @joy "T-Tonight, I don’t want to think anymore."
    MC @talk "...Alright, if that’s what you want."
    hide adara with easeoutright
    "Adara softly smiled and waved as she opened the doors to her home, slowly closing the door behind her with a silently mouthed ‘bye.’"
    "And like that, I was alone again."
    MC @talk "{i}*Sigh*{/i}"
    "What am I going to do about all this?"
    $ AutoMus(True)
    $ AutoAmb(True)
    $ QstComplete(QstProperReunion)
    jump ev_AdaraDream_KO_posttavern