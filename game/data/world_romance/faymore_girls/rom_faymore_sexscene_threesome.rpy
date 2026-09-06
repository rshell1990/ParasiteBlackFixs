label romance_faymore_girls_threesome:
########## next up is more like Faymore "romance" section right?
    # The player returns to the Faymore estate in the evening.
    # FIRST TIME VARIANT 
    $ tmpvar["clothes"] = "naked"
    $ tmpvar["variant"] = "vag"
    
    if IsFirstTime():
        show mc at center with easeinleft
        MC @think "... Hello? Is anyone—"
        CHANYI @lewd "Welcome."
        hide mc
        show chanyi at cleft
        show anya at cright
        with dissolve
        "As I looked up, I saw both women atop the stairs, giggling, as Anya wrapped herself around Chanyi."
        "My cock throbbed at the sight of them... And what they wore."
        MC @surprised "... Which god's favor have I won to be rewarded with this sight?"
        CHANYI @laugh "Fufu, charming."
        ANYA @lewd "Chanyi, the rules."
        CHANYI @laugh "Hm? Oh yes."
        CHANYI @laugh "Some ground rules before we begin."
        CHANYI @talk "First, you tell no one about our... arrangement here."
        CHANYI @talk "What's said during our '{i}playtime{/i}' stays in playtime, yes?"
        CHANYI @laugh "Secondly, you don't try to get between me and my beloved here."
        CHANYI @laugh "Anddd..."
        CHANYI @lewd "Thirdly, we tell you what we are in the mood for tonight."
        MC @smile "Very well."
        MC @smile "And what are you in the mood for tonight?"
        "The two women gave a knowing look at each other."
    #REPEAT VARIANT 
    else:
        show chanyi at cleft
        show anya at cright
        with dissolve
        "The two ladies descended the stairs once more to greet me."
        "My cock sprang to life almost immediately at the sight of them both."
        CHANYI @lewd "I'm glad you could join us again."
        ANYA @happy "Last time was so much fun! {i}*Giggles!*{/i}"
        CHANYI @laugh "It was..."
        CHANYI @laugh "We thought it might be fun to give you a choice tonight."
        "Chanyi smirked."
        CHANYI @lewd "Tell us... if we offered you the chance to fuck our asses tonight, would you?"
        menu:
            "Your asses better be ready to be stretched like they never have before...": 
                #anal
                ANYA @lewd "See? I told you he wouldn't be able to resist!"
                CHANYI @laugh "Hardly a surprise, men will fuck anything with a hole."
                "Chanyi's hand slipped around to grope and slap at Anya's butt, the sound ringing through the hall."
                ANYA @shock "OOOH!"
                CHANYI @lewd "And your ass is a particularly irresistible one anyway!"
                $ tmpvar["variant"] = "anal"
            "Another time, I want you like the first time.": 
                #Vaginal
                CHANYI @laugh "Mmm, very well."
                $ tmpvar["variant"] = "vag"
        #Both variants continued 
        ANYA @happy "A-And one more thing."
        ANYA @lewd "... What do you think of the lingerie?"
        menu:
            "They make you all the more beautiful.": 
                $ tmpvar["clothes"] = "ling"
                #Girls stay in lingerie
                ANYA @happy "The lingerie stays on then, it seems."
            "There's nothing more beautiful than both of you wearing nothing at all.": 
                $ tmpvar["clothes"] = "naked"
                #Girls strip naked
                "The two women looked at each other and smirked before stripping down."
                CHANYI @laugh "Fine then, beast."
                CHANYI @laugh "Have us take off our very expensive lingerie and just be butt-naked for you."
                CHANYI @laugh "Sheesh, the lack of appreciation."
                MC @smile "I'll make it up to you both by eating your asses."
                CHANYI @lewd "... I {i}might{/i} be willing to overlook this matter depending on performance then."
    #ALL VARIANTS CONTINUED 
    CHANYI @lewd "Our quarters, now..."
    label replay_faymore_threesome:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    #Brief fade to black
    "The women each took an arm of mine as they happily escorted me to their bedchambers."
    #Cut to Faymore women's bedroom
    "No sooner had Chanyi carefully closed the door behind us, the two women leapt onto me."
    "Their hands greedily pulled at my clothes, stripping me as they touched, licked and kissed every part of me."
    #FIRST TIME
    if IsFirstTime():
        CHANYI "How do you like him, dear?"
        ANYA "You could chip a tooth on his abs..."
    #REPEAT TIME
    else:
        CHANYI "Mmm... Just as {i}toned{/i} as we remember."
        ANYA "It's too bad we can't keep you locked up here to play with whenever we want..."
    "I push the mildly disturbing comment aside."

    #BOTH CONTINUED
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_1
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_1
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_1
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_1
    with dissolve
    $ Pause()

    "The two women continued to laugh as they lowered themselves to their knees."
    "As my cock sprang out in front of them, Anya's jaw dropped as Chanyi licked her lips greedily."
    CHANYI "Now THIS is more like it!"
    "Anya began to kiss at my cock with her delicate lips,"
    "gently tugging at the skin with her teeth as she lathered my cock with praise."
    ANYA "Chanyi... {i}*Huff*{/i} His thing is making my head feel all funny."
    # FIRST TIME
    if IsFirstTime():
        CHANYI "That's because you're a little cock-drunk slut around men who needs me to keep you in line."
        "Anya let out a shuddering moan as the two women worked diligently to kiss at my cock."
        "My cock prodded at Chanyi's cheek as she pressed her fingers into herself."
        CHANYI "See? I find you alllll the best things!"
        CHANYI "Just think, if you were still with that bore of a man, all the things you'd have missed out on."
        "Anya could only murmur in an almost drunken haze a response."
        ANYA "Yheshh Chanyi..."
        ANYA "{i}*Kiss*{/i} Itshh bhighher."
    # REPEAT TIME
    else:
        CHANYI "I'm not surprised..."
        CHANYI "You've been having me finger you, imagining this big prick inside you again since the first time."
        "The two women worked in sync, praising and kissing at my cock."
        "Their hands reached between their thighs as my cock continued to prod and push against Chanyi's cheek."
        CHANYI "Fufu... So eager."
        CHANYI "Has our friend here missed my mouth that much?"
    # BOTH CONTINUED
    "Chanyi grinned, and as she did, she didn't realize Anya's hand subtly moving to the back of her head."
    CHANYI "I bet you—"

    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_2
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_2
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_2
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_2
    with dissolve
    $ Pause()
    $ PlaySexFx(audio.kiara_bj_loop, 1)

    CHANYI "MMFGH!?"
    "With the lightest push forward, Chanyi's lips opened as they wrapped around my cock."
    "The katai's tongue twisted and beat against my cock as the two women continued to tease out every moment with my member."

    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_3
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_3
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_3
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_3
    with dissolve
    $ Pause()

    #FIRST TIME
    if IsFirstTime():
        ANYA "Mmm... Don't let her fool you."
        ANYA "Chuuu... {i}*Kiss*{/i}"
        ANYA "Chanyi goes weak at the knees for a big cock too."
        ANYA "That's why she gets {i}so{/i} wet watching me take it, don't you?"
    #REPEAT TIME
    else:
        ANYA "You know what you should do?"
        ANYA "You should steal Chanyi from me."
        "Chanyi squirmed, offering the faintest protest as her lips dragged back and forth over my cock."
        CHANYI "ANYHAA!"
        ANYA "{i}*Huff*{/i} You should keep fucking her till her mind snaps!"
        ANYA "And then you should m-make me watch so I learn that she's yours now!"
        ANYA "Oh gods... The shame and betrayal would drive me crazy!"
        "Chanyi playfully slapped Anya's breast, making the sadomasochistic woman moan softly."
        ANYA "Ahh... Sorry, dear."
        ANYA "{i}I know you'd never leave me...{/i}"

    #BOTH CONTINUED
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_4
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_4
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_4
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_4
    with dissolve
    $ Pause()

    "Chanyi could only groan in response, dragging her lips forward and back as she sucked my cock."
    ANYA "She just likes to bully me into it, fufu..."
    ANYA "But that's— {i}*kiss*{/i} fine with me."
    ANYA "{i}I like it when she bullies me.{/i}"

    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_6
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_6
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_5
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_5
    with dissolve
    $ Pause()
    $ StopSexFx()

    "Chanyi pulled her lips away, smirking at her handiwork and my cock covered in their kisses."
    CHANYI "That's right, {i}slut.{/i}"
    CHANYI "I own your ass."
    CHANYI "And I {i}love...{/i}"
    "Her hand reached back to spank and grope at Anya's soft butt."
    ANYA "Mmfghh!"
    CHANYI "{i}LOVE.{/i}"
    CHANYI "Bullying you to fuck who I want."
    #FIRST TIME
    if IsFirstTime():
        MC "(I think they both might be a little crazy...)"
    #REPEAT TIME
    else:
        MC "(Yes, they're definitely crazy.)"
        MC "(But gods be damned, do they fuck good to bring me back here!)"
    #BOTH CONTINUED
    MC "I'm starting to feel lonely here."
    CHANYI "Oh, are you now?"
    CHANYI "Did you hear that, Anya? The meat-stick feels lonely."
    ANYA "Chuu~ Play nice, Chanyi."
    ANYA "And wrap those lips around his cock again."

    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_7
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_7
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_7
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_7
    with dissolve
    $ Pause()
    $ PlaySexFx(audio.kiara_bj_loop, 1)

    "Chanyi grinned, doing exactly that."
    "This time though, she moved faster, taking my cock deeper into her throat as she groaned hotly."
    CHANYI "{i}*Slurp!* *Slurp!*{/i}"

    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_4
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_4
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_7
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_7 
    with dissolve
    $ Pause()

    #FIRST TIME
    if IsFirstTime():
        ANYA "She's good at it, isn't she?"
        MC "A-Ahh! Oh fuck!"
        MC "I didn't think she'd—"
        ANYA "Fufu, I'm well aware of how good that mouth of hers can be."
    #REPEAT TIME
    else:
        MC "Ahhh!"
        ANYA "Feels like your cock is being massaged by a goddess, doesn't it?"
        MC "She's... {i}*Huff*{/i} very talented."
    #BOTH CONTINUED
    "Chanyi's tongue danced and twisted around my cock as Anya seemed only to coax her on."

    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_7
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_7
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_6
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_6
    with dissolve
    $ Pause()

    ANYA "Is he good, Chanyi?"
    CHANYI "Mmfghh! Shoo ghooodhh! {i}*Slurp!*{/i}"
    ANYA "Just imagine how much fun you two could have!"
    ANYA "You could tie me up and both force me to watch as you fuck."
    ANYA "You could make me beg and cry just so you both touch—"
    "Something in Anya's words set me over the edge,"

    $ PlaySexFx(audio.kiara_bj_finish)
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_cum_1
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_cum_1
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_cum_1
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_cum_1
    with flash
    $ Pause()

    "I grunted, my aching cock exploding its load into Chanyi's mouth as it spilled through the seal of her lips."
    MC "FUCK!"
    CHANYI "Mmfhh?!"
    ANYA "Hahaha!"
    ANYA "Did my words do the trick?"
    ANYA "Or was it Chanyi's mouth?"

    $ PlaySexFx(audio.kiara_bj_finish)
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_cum_2
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_cum_2
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_cum_2
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_cum_2
    with flash
    $ Pause()

    CHANYI "Mmhfhh! Shoo mhuchh!"
    ANYA "Come here, Chanyi."
    ANYA "Don't forget to share!"
    "The two women stopped to passionately kiss each other, passing my load back between their mouths as they swallowed it down together."

    $ PlaySexFx(audio.nijah_doggy_loop, 1)
    #FIRST TIME
    if IsFirstTime():
        MC "... Gods."
        MC "You two might be the craziest girls I've ever met."
        MC "And there's some stiff competition right now."
        CHANYI @laugh "I'm sure we'd love to meet the competition sometime."
        CHANYI @lewd "Especially if they're as gifted as you..."
        ANYA @happy "Chanyi, let's not wait any longer."
        ANYA @happy "Let's have some {i}real{/i} fun."
    else:
        #REPEAT TIME
        if tmpvar["variant"] == "vag":
            MC "Ha! I swear you both just exist to ruin men."
            CHANYI @laugh "We'll {i}ruin{/i} you."
            MC @lewd "You can try."
            ANYA @lewd "Mmm, we most certainly can."
            CHANYI @lewd "Come on, time to move onto the main course!"
        #REPEAT (ANAL) TIME
        if tmpvar["variant"] == "anal":
            if CharIsVisiblyPreg("chanyi"):
                if tmpvar["clothes"] == "ling":
                    scene faymore_threesome_preg_ling_8
                else:
                    scene faymore_threesome_preg_naked_8
            else:
                if tmpvar["clothes"] == "ling":
                    scene faymore_threesome_nopreg_ling_8
                else:
                    scene faymore_threesome_nopreg_naked_8
                $ Pause()
            MC "I mean this with all respect, but I'm fairly certain the most trained brothel whores couldn't keep up with you two!"
            ANYA "How sweet of you to say, fufu."
            CHANYI "Are you ready, Anya?"
            CHANYI "To feel this huge cock destroy your ass?"
            ANYA "Mhmm! Y-Yes..."
            ANYA "My ass is yours to order as you see fit."
    #BOTH CONTINUED
    "The two women climbed onto the bed as Anya lay down and spread her legs expectantly."
    "Chanyi crawled onto the bed beside her, gently pressing her lips against hers."
    ANYA "Don't go easy on me, either of you!"
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_8 with dissolve
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_8 with dissolve
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_8 with dissolve
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_8 with dissolve
    $ Pause()

    "I gently aligned my cock against her glistening womanhood,"
    "patting it against her body as I lightly teased what was to come."
    CHANYI "Do you really think that cock is going to go easy on you?"
    CHANYI "{i}He's going to ruin you.{/i}"
    CHANYI "{i}He's going to fucking break you and everyone's going to know it.{/i}"
    "Anya let out a trembling sigh."
    ANYA "Y-Yes, haha... my reputation's going to be ruined!"

    if tmpvar["variant"] == "vag":
        if CharIsVisiblyPreg("chanyi"):
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_preg_ling_9
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_preg_naked_9
        else:
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_nopreg_ling_9
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_nopreg_naked_9
        with flash

    elif tmpvar["variant"] == "anal":
        if CharIsVisiblyPreg("chanyi"):
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_preg_anal_ling_1
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_preg_naked_anal_1
        else:
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_nopreg_ling_anal_1
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_nopreg_naked_anal_1
        with dissolve
        $ Pause()
    #FIRST TIME
    if IsFirstTime():
        "Chanyi motioned for me, and slowly, I began to push my cock into her."
        ANYA "OH GODS, OH GODS, OH GODSSSSS!"
        ANYA "He's s-stretching me so much!!"
    else:
        #REPEAT TIME
        if tmpvar["variant"] == "vag":
            ANYA "A-AHH!"
            ANYA "I d-don't think I'm ever— Mhmm!"
            ANYA "going to get used to it!"
        #REPEAT (ANAL) TIME
        elif tmpvar["variant"] == "anal":
            "Carefully, I teasingly rubbed my cock against Anya's tight backdoor,"
            "lightly prodding at the hole to test for resistance as she cooed."
            ANYA "Mhmm... M-My ass..."
            ANYA "He's going to fuck my ass, Chanyi."
            CHANYI "He's not just going to fuck it."
            "Chanyi grinned evilly."
            CHANYI "{i}He's going to fucking destroy your ass.{/i}"
            "Anya could only shudder in delight at the thought."
            "As i pushed my cock against the entrance of her ass,"
            "Anya could only gasp as her tight hole gave way and spread to accommodate my member."
            ANYA "Y-You're in! Mmfghh!"
            ANYA "You're in my ass!"

    #FIRST TIME AND REPEAT CONTINUED
    if tmpvar["variant"] == "vag":
        CHANYI "Just imagine if they knew what you were really like."
        CHANYI "You'd be the talk of the city."
        CHANYI "Anya Faymore, abandons her husband, abandons everything for cock."
        ANYA "Y-YESS! Mmmfgh! I'd be RUINED!"
        ANYA "H-Harder! Fuck me harder!"
        ANYA "Both of you! Tell me I'm pathetic!"
        ANYA "A pathetic little whore o-only good for— Mmfghh!"
        ANYA "being someone's p-plaything!"

    if tmpvar["variant"] == "vag":
        $ PlaySexFx(audio.nijah_doggy_loop2, 1)

        if CharIsVisiblyPreg("chanyi"):
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_preg_ling_10
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_preg_naked_10
        else:
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_nopreg_ling_10
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_nopreg_naked_10
        with flash
        $ Pause()

    elif tmpvar["variant"] == "anal":
        if CharIsVisiblyPreg("chanyi"):
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_preg_anal_ling_2
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_preg_naked_anal_2
        else:
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_nopreg_ling_anal_2
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_nopreg_naked_anal_2
        with dissolve
        $ Pause()

    "I began to slam my cock into Anya, her tight hole squeezing around me as every insult hurled at her only seemed to make her tighter."
    CHANYI "Tell her, tell her how you could fuck any woman."
    CHANYI "That she's just something to dump your loads into."
    "Anya groaned happily once again, squeezing around me."
    ANYA "D-Do it!"
    ANYA "Please, please, please...!"
    ANYA "Tell me I'm worthless!"
    MC "... You're less than worthless."
    ANYA "Ahh!"
    MC "You're what we fuck when all other options are out."
    ANYA "MMFGHH!"
    "Anya's pussy felt like a death grip around my cock as I continued to slam into her."
    "Chanyi grinned towards me, eager to hear what terrible thing I said next."
    MC "Personally, it's ridiculous someone like you living in a house like this."
    ANYA "Y-Yes it is!"
    MC "You don't even deserve rights, you should be {i}public{/i} property."
    MC "Put in the stocks in the square for anyone to fuck, spit on, and beat when they feel like it."
    ANYA "Y-YESSS! OH GODS!! IT BURNS... THE SHAME BURNS AND IT'S S-SO FUCKING HOT!"
    ANYA "THAT'S WHAT I D-DESERVE, FOR FAILING AS A WIFE AND B-BEING SEDUCED!"
    "Anya's mouth suddenly hung agape, her whole body tightening as she climaxed around me."
    ANYA "MMMFGHHHHHHHH....!!"
    CHANYI "Haha! Did you just cum?"
    CHANYI "Tsk, tsk, tsk!"
    CHANYI "... Do it, fill her up and give her worthless pussy its reward."
    ANYA "Y-Yeshhhh..."
    "Slamming into her, she didn't exactly need to ask at this point."

    $ PlaySexFx(audio.nijah_doggy_finish)
    if tmpvar["variant"] == "vag":
        if CharIsVisiblyPreg("chanyi"):
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_preg_ling_cum_3
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_preg_naked_cum_3
        else:
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_nopreg_ling_cum_3
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_nopreg_naked_cum_3
        with flash
    elif tmpvar["variant"] == "anal":
        if CharIsVisiblyPreg("chanyi"):
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_preg_anal_ling_cum
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_preg_naked_anal_cum
        else:
            if tmpvar["clothes"] == "ling":
                scene faymore_threesome_nopreg_ling_anal_cum
            elif tmpvar["clothes"] == "naked":
                scene faymore_threesome_nopreg_naked_anal_cum
        with flash
    $ Pause()

    "Forcing my cock to the hilt and burying it within her tight hole, I grunted once again, pouring my load into her eager hole."
    MC "HRGHHH! Take it!!"
    "Anya's eyes rolled back as she felt the seed pour into her."
    "No sooner had I finished, Chanyi licked her lips in anticipation."

    if tmpvar["variant"] == "anal":
        #REPEAT (ANAL) TIME 
        "Chanyi smirked as she watched my cock sink in and out of Anya's ass."
        CHANYI "Do you like it, Anya?"
        CHANYI "Do you like doing something only the most disgusting, common wenches do?"
        "Anya's ass tightened around my cock at her words."
        ANYA "Y-Yes!"
        ANYA "P-Please, bully my ass!"
        ANYA "Make me feel like this is all I am good for!"
        "Chanyi motioned for me to move faster as she continued to torment her wife."
        CHANYI "Oh, this is all you're good for."
        CHANYI "Tell her... Tell her this meaty ass is just made for taking cock."
        "Chanyi looked towards me, playfully signaling once more."
        MC "We should just put you in chastity really."
        ANYA "Mmfghh! N-Nooooo!"
        ANYA "That's too— {i}*Huff*{/i} cruel!"
        MC "No one's going to want your worthless pussy anymore."
        MC "We'll just leave it open at the back for any men who want to cum in your rear."
        "Anya's breathing became heavier as I spoke."
        ANYA "Y-Yes... That sounds... Ahhh!"
        ANYA "Like what I deserve!"
        CHANYI "Beg him, Anya."
        CHANYI "Beg him to cum in your ass."
        CHANYI "Beg him because it's all you deserve..."
        "Anya began to tremble and shake, her eyes rolling back."
        ANYA "Please cum in this worthless slut's ass."
        ANYA "She needs your cum in her ass to remind her of her place!"
        "As I slammed into her rear, my aching balls tightened."
        MC "T-TAKE IT THEN!"
        "Anya's eyes widened as she felt the explosion of seed pouring into her ass."
        "She trembled, shuddering with an orgasm, drooling and exhausted."
        "Pulling my cock free, Chanyi didn't waste a moment."

    #ALL CONTINUED
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_11
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_11
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_11
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_11
    with flash
    $ Pause()

    #FIRST TIME
    if IsFirstTime():
        CHANYI "I hope you don't think you're done yet."
        MC "{i}*Huff*{/i} You two are..."
        MC "{i}Insatiable.{/i}"

    #REPEAT TIME
    else:
        if tmpvar["variant"] == "anal":
            #REPEAT (ANAL) TIME 
            CHANYI "Now me."
            CHANYI "Watching you fuck her ass has got me... {i}intrigued.{/i}"
            "As Anya twitched on the bed, Chanyi raised herself into position."
            CHANYI "Come on, I can see you're still hard."
            CHANYI "What are you waiting for?"
            CHANYI "Shove that prick in my—"
        elif tmpvar["variant"] == "vag":
            "Chanyi, biting her lower lip, motioned for me."
            CHANYI "Now that my dear wife is satisfied..."
            CHANYI "It's my turn."

    #ALL CONTINUED
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_12
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_12
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_12
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_12
    with dissolve
    $ Pause()

    "I wasted no time, slamming into Chanyi as my arm wrapped around her throat."
    CHANYI "GAHHHHH!"
    "Her body quivered as she squeezed around me."
    CHANYI "H-Hard...!"
    CHANYI "You're so—"
    CHANYI "Uffffhh!"
    CHANYI "{i}Fucking hard!{/i}"
    CHANYI "{b}HARDER!{/b}"
    "I slammed into her harder, tightening my hold."
    MC "You uptight bitch!"
    MC "Is this what you need?!"
    CHANYI "Glughh! Y-YHESHH!"
    MC "For someone who likes being in charge,"
    MC "you love being put in your place!"
    CHANYI "Urghhh...!"
    MC "{i}And do you know where that place is, slut?{/i}"
    MC "Right here, with your ass raised and ready for my cock!"
    "She tightened around me as I drove deeper."

    if IsFirstTime():
        $ UnlockGalFlag("anya_and_chanyi", "threesome", "var_first")
    else:
        $ UnlockGalFlag("anya_and_chanyi", "threesome", "var_rep", notify = False)

        if CharIsVisiblyPreg("chanyi"):
            if tmpvar["variant"] == "vag":
                if tmpvar["clothes"] == "ling":
                    $ UnlockGalFlag("anya_and_chanyi", "threesome", "var_preg_vag_ling")
                elif tmpvar["clothes"] == "naked":
                    $ UnlockGalFlag("anya_and_chanyi", "threesome", "var_preg_vag_naked")
            elif tmpvar["variant"] == "anal":
                if tmpvar["clothes"] == "ling":
                    $ UnlockGalFlag("anya_and_chanyi", "threesome", "var_preg_anal_ling")
                elif tmpvar["clothes"] == "naked":
                    $ UnlockGalFlag("anya_and_chanyi", "threesome", "var_preg_anal_naked")
        else:
            if tmpvar["variant"] == "vag":
                if tmpvar["clothes"] == "ling":
                    $ UnlockGalFlag("anya_and_chanyi", "threesome", "var_nopreg_vag_ling")
                elif tmpvar["clothes"] == "naked":
                    $ UnlockGalFlag("anya_and_chanyi", "threesome", "var_nopreg_vag_naked")
            elif tmpvar["variant"] == "anal":
                if tmpvar["clothes"] == "ling":
                    $ UnlockGalFlag("anya_and_chanyi", "threesome", "var_nopreg_anal_ling")
                elif tmpvar["clothes"] == "naked":
                    $ UnlockGalFlag("anya_and_chanyi", "threesome", "var_nopreg_anal_naked")

    $ UnlockGalSceneAndGrantXp("anya_and_chanyi", "threesome")
    $ ReduceInfectionFromSex("chanyi")
    $ PregRoll("chanyi")
    $ PlaySexFx(audio.nijah_doggy_finish)
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_preg_ling_cum_4
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_preg_naked_cum_4
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_threesome_nopreg_ling_cum_4
        elif tmpvar["clothes"] == "naked":
            scene faymore_threesome_nopreg_naked_cum_4
    with flash
    $ Pause()

    "She cried out as I finished inside her."
    CHANYI "F-FUCKERRRR...!!"
    "Fully spent, I rolled off her."
    CHANYI "{i}*Huff*{/i} Cheating— {i}*Huff*{/i} bastard..."
    if not IsFirstTime():
        if tmpvar["variant"] == "anal":
            #REPEAT (ANAL) TIME
            MC "You really think your ass can handle it?!"
            CHANYI "Gahhh!"
            CHANYI "{i}Fuck you!{/i}"
            "I laughed, thrusting harder as she groaned."
            MC "I prefer you like this!"
            MC "Much more agreeable!"
            CHANYI "B-Bastard!"
            "She suddenly trembled, tightening hard around me."
            CHANYI "MMMFGHHHH!"
            "I came again, holding her tight."
            CHANYI "M-MY ASS!"
            "When I pulled out, she looked ready to collapse."
            "My seed spilled from her."
            MC "Gods, girl... You could kill a man with that thing!"
    # ALL CONTINUED
    "I gently slapped Chanyi's butt as she groaned."
    "Rising back to my feet, I began to put my clothes back on as I left the women in their post-fuck haze."
    "With a final glancing look towards them, the two had crawled into bed together and were tenderly kissing one another."
    "I smirked, carefully leaving so as not to disturb them too much."
    $ StopReplay()
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ AutoMus(True)
    $ LocEnter()
