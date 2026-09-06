## this file has all the script that happens at start and on finish,
## stuff in the middle like rooms or alt ingrid route is in corresp files

label qst_TheTarbecks_MeetGarenFirstTimeAtPaleDragon:
    show garen at cright_f with dissolve
    show mc at cleft with easeinleft
    GAREN @talk "Ahh, you're here. Good."
    $ GoalComplete(QstTheTarbecks, 0)
    GAREN @talk "Now that Zanzibat has been dealt with, the next issue is Lord Tarbeck."
    MC @serious "Am I to presume that once more I'm risking my life fighting monsters?"
    GAREN @talk "Not this time."
    GAREN @talk "Lord Tarbeck is a different kind of animal to Zanzibat."
    MC @think "Hmm?"
    show sypha at left with easeinleft
    SYPHA @happy "Tarbeck is rarely seen in public, but he is known for throwing extravagant parties."
    SYPHA @happy "He refuses most face-to-face meetings, preferring to use proxies for business."
    SYPHA @talk "These parties are one of the few chances someone might actually speak to him directly."
    SYPHA @think "They are exclusive—only those within his trusted circle usually receive an invitation."
    SYPHA @happy "{i}Thankfully, I have secured one for us...{/i}"
    SYPHA @happy "I'm certain we can find information there that could be used against him."
    SYPHA @think "{i}But first, we’ll need appropriate attire to attend.{/i}"
    $ tmpvar = [1, 2, 3]
    label qst_TheTarbecks_MeetGarenFirstTimeAtPaleDragon_PreChoiceMenu:
    if len(tmpvar) > 0:
        menu:
            "What kind of 'parties' are we talking about here?" if 1 in tmpvar:
                $ tmpvar.remove(1)
                SYPHA @talk "The invite-only kind."
                SYPHA @happy "{i}And filled with delectable pleasures...{/i}"
                SYPHA @happy "Lord Tarbeck’s appetites are becoming quite legendary, from what I hear."
                jump qst_TheTarbecks_MeetGarenFirstTimeAtPaleDragon_PreChoiceMenu
            "Why not try to persuade Lord Tarbeck directly?" if 2 in tmpvar:
                $ tmpvar.remove(2)
                GAREN @angry "Lord Tarbeck hates us."
                GAREN @angry "A deal many years ago went... {i}poorly{/i}."
                GAREN @talk "For him, at least."
                GAREN @angry "He’s never forgotten it."
                GAREN @talk "Had the fool read the contract properly, he’d have been fine."
                MC @think "Or you could try {i}not{/i} screwing over your clients."
                GAREN @angry "He was the greedy one."
                GAREN @angry "Young and naive."
                jump qst_TheTarbecks_MeetGarenFirstTimeAtPaleDragon_PreChoiceMenu
            "Where do we find clothes on such short notice?" if 3 in tmpvar:
                $ tmpvar.remove(3)
                SYPHA @happy "There’s a tailor here in Hamun."
                SYPHA @happy "Giselra—one of the finest in the city."
                SYPHA @talk "I suggest we head there."
                jump qst_TheTarbecks_MeetGarenFirstTimeAtPaleDragon_PreChoiceMenu
    else:
        GAREN @smile "I look forward to hearing the results of your work..."
        show garen at blurin, cright
        hide garen with easeoutright
        $ QstSetProgress(QstTheTarbecks, 1)
        $ GoalShow(QstTheTarbecks, 1)
        MC @angry "(How much longer do they plan to have me do their dirty work?)"
        $ LocEnter()

###################################################################################################
label qst_TheTarbecks_VisitGiselraOrderClothes:
    $ CharMeet("giselra")
    $ QstTheTarbecks().ShowGiselraFirstQstEnterScene = False
    show giselra at cright_f
    with dissolve
    show mc at cleft with easeinleft
    GISELRA @smile "Hmm?"
    GISELRA @shock "Oooh! Welcome! Welcome to Giselra’s!"
    GISELRA @smile "Looking for something tailored, perhaps?"
    GISELRA @smile "You’d look quite dashing in light blue, I think!"
    GISELRA @smile "The finest craftsmanship in all of Hamun, no need to look elsewhere!"
    if CharIsMet("giselra"):
        show sypha at left with easeinleft
        MC @smile "I am looking for some clothes for me and my comp—"
        SYPHA @happy "I am his wife."
    else:
        MC @smile "Well met, Giselra."
        show sypha at left with easeinleft
        MC @smile "I am [player_name!t], and these are my comp—"
        SYPHA @happy "His wife."
    "I gave Sypha a glance..."
    "But she ignored me completely."
    GISELRA @shock "Ooh! How... lovely!"
    GISELRA @smile "Please, browse my wares."
    GISELRA @smile "If you need anything, just call!"
    hide giselra with easeoutleft
    show mc at cright
    show mc at blurin, cright_f
    show sypha at cleft
    with ease
    MC @angry "Enough with this {i}wife{/i} nonsense."
    MC @angry "We are not married! We’re—"
    SYPHA @happy "Shh, stop worrying, {i}dear{/i}."
    SYPHA @happy "I’ve already laid claim to you."
    SYPHA @happy "{i}By law, you are mine.{/i}"
    MC @angry "That’s not how this works!"
    SYPHA @talk "Details, details."
    SYPHA @talk "Come—we need to find you something nice to wear."
    hide sypha with easeoutright
    MC @sad "{i}*Sigh*{/i}"
    show mc at center with ease
    MC "(What in the seven hells is wrong with this girl?)"
    $ LocEnter()

label qst_TheTarbecks_GiselraBuyClothes:
    GISELRA @smile "Ahh, and what’s the occasion?"
    MC @talk "A... party."
    GISELRA @smile "Then allow me to take your measurements."
    scene black with dissolve
    "The tailor notes each measurement carefully."
    "I can’t help but notice her smirk as her hands run along my chest, lingering a few seconds too long."
    $ LocFlush()
    show giselra at center
    with dissolve
    GISELRA @smile "All done!"
    $ GoalComplete(QstTheTarbecks, 1)
    $ GoalShow(QstTheTarbecks, 2)
    GISELRA @smile "I can have something exquisite ready in about a week."
    GISELRA @smile "Only two thousand coins."
    MC @surprised "TWO THOUSAND?!"
    GISELRA @talk "I’m sorry, dear."
    GISELRA @talk "If you plan to attend parties like this, you’ll need the {i}right{/i} clothes."
    GISELRA @talk "And the {i}right{/i} fabrics aren’t cheap."
    MC @serious "I can see that."
    GISELRA @smile "When you have the coin, come see me and I’ll begin immediately."
    jump qst_TheTarbecks_GiselraBuyClothesMenu

label qst_TheTarbecks_GiselraBuyClothesMenu:
    menu:
        "I have the coin for the clothes." (Req_Gold = 2000):
            $ PlayerRemItem("gold", 2000)
            pass
        "Be seeing you.":
            GISELRA @smile "Come back anytime, handsome."
            $ QstSetProgress(QstTheTarbecks, 2)
            $ LocEnter()
    GISELRA @smile "Ahh! Very good!"
    GISELRA @smile "I’ll get to work right away."
    GISELRA @smile "Come back in a week, lovely."
    $ GoalComplete(QstTheTarbecks, 2)
    $ QstTheTarbecks().GiselraClothesReadyDay = ((GetGameDay() + 1) if config.developer else (GetGameDay() + 7))
    $ QstSetProgress(QstTheTarbecks, 3)
    $ GoalShow(QstTheTarbecks, 3)
    $ LocEnter()

label qst_TheTarbecks_GiselraClothesTooEarly:
    GISELRA @talk "Sorry, love. It’s still not ready yet."
    return

label qst_TheTarbecks_GiselraClothesRetrieveAndContinue:
    GISELRA @smile "Ahh! There you are."
    $ GoalComplete(QstTheTarbecks, 3)
    GISELRA @smile "All ready. Why don’t you try it on?"
    scene black with dissolve
    "I changed into the clothes in a small back room."
    "When I emerged, the smiles around me said it all."
    $ CharSetClothes("mc", "suit")
    $ LocFlush()
    show mc at center_f
    show giselra at right_f
    GISELRA "...Oh my."
    hide giselra with easeoutright
    show markus at left
    with easeinleft
    MARKUS @smile "[player_name!t]? Is that really you?"
    show mc at cright_f with ease
    MARKUS @smile "I’m not used to seeing you without shit and blood all over you."
    MC @smile "I’ll be sure to remind you of that when you have to wear one of these someday."
    show markus at blurin, cleft_f
    hide markus with easeoutleft
    show kiara at cleft with easeinleft
    KIARA @smile "Fucking hells..."
    KIARA @smile "You look great!"
    if CharIsLover("kiara"):
        KIARA @blush "Gods... the things I could do to you right now."
        MARKUS @think "Try not to drool before we leave."
    hide kiara with dissolve

    if CharInParty("ves"):
        show ves at cleft with easeinleft
        if CharIsLover("ves"):
            VES @blush "...Y-you look very nice."
            VES @blush "Though I think I prefer you in your armor."
            MARKUS @angry "Of course you would."
            MARKUS @angry "Gods forbid we do anything other than fight and kill."
            show ves at shake
            VES @angry "Tsch!"
            VES @angry "Armor or not, you still look like a fool."
        else:
            VES @talk "Fancy robes in the desert..."
            VES @talk "You humans wear the strangest things."
        hide ves with dissolve

    show sypha at cleft with easeinleft
    SYPHA @happy "Ahhh!"
    SYPHA @happy "You clean up nicely, dear."
    SYPHA @happy "You’ll make excellent sweetness for the eyes on my arm."
    MC @serious "I’m not some toy for you to parade around."
    show sypha at center with ease
    "Sypha traces a finger playfully down my chest."
    SYPHA @laugh "{i}Funny.{/i}"
    show sypha at cleft with ease
    SYPHA @talk "Anyway, you’ll need to choose a companion for the evening."
    MC @think "What? Aren’t you coming?"
    SYPHA @happy "Oh, I’ll be there."
    SYPHA @talk "But I must arrive earlier to meet a contact."
    SYPHA @talk "It would be suspicious for us to arrive together."
    MC @think "So who should I bring?"
    MC @think "What about their attire?"
    SYPHA @happy "Leave the women’s clothing to me."
    show sypha at right with ease
    show sypha at blurin, right_f
    SYPHA @happy "Now then—who will it be?"
    menu qst_TheTarbecks_GiselraClothesRetrieveAndContinue_CompanionChooseMenu:
        "Ves" if (CharInParty("ves") and CharIsLover("ves")):
            $ QstTheTarbecks().PartyCompanion = "ves"
            show ves at cleft with easeinleft
            VES @shock "Me?"
            VES @sad "But I'm not-"
            VES @sad "{i}I'm an orc.{/i}"
            MC @smile "You are who I want."
            "Ves' cheeks burned red."
            VES @blush "V-Very well."
            pass
        "Kiara" if CharIsLover("kiara"):
            $ QstTheTarbecks().PartyCompanion = "kiara"
            show kiara at cleft with easeinleft
            KIARA @happy "Oooh, wanna see me all dressed up aye?"
            KIARA @happy "Well I won't say no to getting to wear a pretty dress!"
            pass
        "Markus":
            $ QstTheTarbecks().PartyCompanion = "markus"
            show markus at cleft with easeinleft
            MARKUS @shock "{i}... I'm sorry, what?{/i}"
            MC @smile "It's perfect, you can change into a woman and no one will suspect a thing."
            MC @serious "If I get in trouble, it'll be good to know you've got my back."
            MARKUS @angry "And if this pervert, Lord tarbeck, just plans for some big orgy where everyone fucks?"
            MARKUS @angry "Friend... There are some lines and boundaries you know."
            MC @talk "You're the only one I trust enough."
            MC @talk "Besides, if that's what it is, we'll just find another way."
            MARKUS @talk "I hope you are right with this..."
            pass
        "Hire a prostitute (Esme)":
            $ QstTheTarbecks().PartyCompanion = "esme"
            MC @think "I’ll hire a working girl to attend with me."
            MC @talk "That’s probably the safest option."
            SYPHA @talk "You certainly won’t be the first man to do so."
            SYPHA @happy "Just be careful she doesn’t enjoy herself {i}too{/i} much..."
            $ QstSetProgress(QstTheTarbecks, 4)
            $ GoalShow(QstTheTarbecks, 4)
            MC "(I should ask around the brothels.)"
            $ LocEnter()
        "DEBUG: add ves if missing and set to lover" if config.developer:
            if not CharInParty("ves"):
                $ PartyAddChar("ves")
            $ CharSetLover("ves")
            jump qst_TheTarbecks_GiselraClothesRetrieveAndContinue_CompanionChooseMenu
        "DEBUG: set kiara to lover" if config.developer:
            $ CharSetLover("kiara")
            jump qst_TheTarbecks_GiselraClothesRetrieveAndContinue_CompanionChooseMenu
    SYPHA @happy "Then it's decided!"
    SYPHA @happy "This is going to be fun!"
    scene black with dissolve
    $ CharSetClothes("mc", "normal")
    $ QstSetProgress(QstTheTarbecks, 5)
    $ GoalShow(QstTheTarbecks, 5)
    $ LocEnter()

label qst_TheTarbecks_SpeakToEsme:
    ESME @talk "Hm?"
    ESME @talk "Like... a date, or?"
    MC @talk "A party."
    ESME @smile "What kind of party?"
    MC @talk "{i}A rich one.{/i}"
    ESME @smile "I see."
    ESME @talk "For the whole evening?"
    ESME @smile "My price is three thousand coins."
    menu:
        "Here you go." (Req_Gold = 3000):
            $ PlayerRemItem("gold", 3000)
            "I handed over the coin."
            pass
        "How about two and a half, and I give you some extra personal attention?" (Req_Gold = 2500, Req_Charm = 9):
            $ PlayerRemItem("gold", 2500)
            ESME @smile "Confident, aren’t we?"
            ESME @smile "{i}I like that.{/i}"
            ESME @smile "Deal."
            pass
        "Consider it an investment. A merchant lord’s party—think of the future clients. How about two thousand?" (Req_Barter = 11, Req_Gold = 2000):
            $ PlayerRemItem("gold", 2000)
            ESME @laugh "A merchant lord, you say..."
            ESME @smile "{i}Interesting.{/i}"
            ESME @smile "All right. Deal."
            pass
        "I don’t have that kind of coin yet...":
            ESME @sad "Shame."
            ESME @smile "Come back when you do."
            return

    $ GoalComplete(QstTheTarbecks, 4)
    $ QstTheTarbecks().PartyCompanion = "esme" # yea 2nd time but just 2make sure
    ESME @sad "Um... there’s a slight problem."
    ESME @sad "I don’t have clothes fit for something like this."
    MC @talk "Do you know the tailor Giselra?"
    ESME @shocked "Of course!"
    ESME @smile "She’s one of the best in the city."
    MC @talk "Tell her you’re my companion for the party."
    MC @talk "She’ll understand."
    ESME @smile "Oooh!"
    ESME @smile "You’re becoming more impressive by the minute."
    ESME @talk "So where is this party?"
    MC @talk "Lord Tarbeck’s mansion."
    ESME @shocked "Lord Tarbeck?"
    ESME @smile "Well..."
    ESME @smile "Sounds like it’ll be a long night."
    ESME @smile "I'll meet you there then."
    $ QstSetProgress(QstTheTarbecks, 5)
    $ GoalShow(QstTheTarbecks, 5)
    hide esme with dissolve
    MC "(I hope I made the right decision...)"
    MC "(I should head to Lord Tarbeck’s estate when the party begins.)"
    $ LocEnter()

label qst_TheTarbecks_DEBUG_CompanionChoice:
    if config.developer:
        "DEBUG: change companion? currently [QstTheTarbecks().PartyCompanion]"
        menu:
            "dont change":
                pass
            "ves":
                $ QstTheTarbecks().PartyCompanion = "ves"
            "esme":
                $ QstTheTarbecks().PartyCompanion = "esme"
            "markus":
                $ QstTheTarbecks().PartyCompanion = "markus"
            "kiara":
                $ QstTheTarbecks().PartyCompanion = "kiara"
    return

#####################################################################################
label qst_TheTarbecks_ArriveToParty:
    $ QstTheTarbecks().RemoveNonCompanionChars()

    $ CharSetClothes("mc", "suit")
    $ CharSetClothes("ves", "dress")
    $ CharSetClothes("kiara", "dress")
    $ CharSetClothes("markus", "dress")
    $ CharSetClothes("esme", "dress")
    $ CharSetClothes("sypha", "dress")

    $ CharSetBattleSkinID("mc", "mc_party")
    $ CharSetBattleSkinID("ves", "ves_party")
    $ CharSetBattleSkinID("kiara", "kiara_party")
    $ CharSetBattleSkinID("markus", "markus_fem_party")

    "As I waited by the entrance to Lord Tarbeck’s lavish estate, I shifted impatiently."
    show mc at cleft with easeinleft
    MC @serious "(Where are they?)"
    show mc at cright with ease
    show mc at blurin, cright_f
    MC @serious "(Are they running late?)"

    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_8

    if QstTheTarbecks().PartyCompanion == "ves":
        show ves at cleft with easeinleft
        VES @blush "..."
        MC @surprised "...Ves?"
        "I blinked, staring at her in disbelief."
        VES @angry "Not a damn word."
        MC @surprised "Why are you—?"
        VES @angry "Because this is the Free City."
        VES @angry "Not the {i}equal{/i} city."
        VES @angry "And Giselra insisted I wear this damned thing!"
        "My eyes wandered as Ves’s cheeks burned red."
        VES @angry "S-Stop looking at me like that, damn it!"
        MC @embarr "Sorry, you just..."
        MC @embarr "{i}Look cute.{/i}"
        "Her face bloomed crimson as she stammered."
        VES @talk "C-Come on already! Let’s get this farce over with!"
        show ves at left
        with ease
        show mc at blurin, cleft
        with ease
        "Grabbing my hand, Ves dragged me toward the entrance."
        show cg_guard_hamun at cright_f with easeinright
        GUARD "Invitations?"
        "Ves stiffly held them out."
        GUARD "{i}...You may pass.{/i}"
        GUARD "Keep your orc pet on a leash."
        GUARD "We won’t tolerate {i}any{/i} violence."
        VES @angry "I am no one’s {i}pet{/i}, human."
        VES @angry "And you have no right threatening anyone with that puny spear."
        "The guard stepped aside, though his gaze lingered beneath his helm."
        GUARD "{i}...Enjoy the evening.{/i}"
        hide ves
        hide mc
        with easeoutright
    elif QstTheTarbecks().PartyCompanion == "kiara":
        show kiara at cleft with easeinleft
        KIARA @smile "...Good evening, {i}sir{/i}."
        KIARA @laugh "{i}*Giggles*{/i}"
        "She offered a playful bow."
        "It was strange seeing Kiara—normally rough around the edges—so elegantly dressed."
        "I imagined she found me just as unfamiliar."
        MC @surprised "Kiara... you look—"
        KIARA @smile "I clean up nicely in a dress, don’t I?"
        KIARA @smile "Do I pass for a fancy lady?"
        MC @lewd "You look great."
        KIARA @scared "Huh?"
        KIARA @shy "O-Oh!"
        KIARA @blush "You scrub up nicely yourself!"
        "She linked her arm with mine and winked."
        KIARA @smile "Come on, handsome. We’ve got places to be."
        show kiara at left
        with ease
        show mc at blurin, cleft
        with ease
        "At the door, Kiara presented the invitations."
        show cg_guard_hamun at cright_f with easeinright
        GUARD "{i}...Are you certain this is the companion you wish to bring, sir?{/i}"
        MC @think "What do you mean?"
        GUARD "Lord Tarbeck’s guests tend to bring more..."
        GUARD "{i}High-value companions.{/i}"
        KIARA @laugh "....OOOOH!"
        KIARA @smile "You think I’m a cheap whore!"
        MC @serious "Kiara, let’s just—"
        KIARA @angry "That’s right! I’m his cheap, slutty {i}whore{/i}!"
        KIARA @angry "I’ll polish his {i}spear{/i} all night!"
        KIARA @smile "{i}But who’s going to polish your little spear when you get home?{/i}"
        GUARD "Tsch!"
        "The guard stepped aside."
        GUARD "Enjoy the evening."
        hide kiara
        hide mc
        with easeoutright
    elif QstTheTarbecks().PartyCompanion == "markus":
        show markus_fem at cleft with easeinleft
        "For a moment, I didn’t recognize the beautiful blonde woman beside me."
        "I smiled absently—until she nudged me."
        MARKUS_FEM @angry "What the hells are you standing around for?"
        MC @surprised "...M-Markus?"
        MC @surprised "Is that really you?"
        MARKUS_FEM @angry "Who else would it be?"
        MC @smile "Sorry, I just didn’t recognize you."
        MARKUS_FEM @angry "Not a damn word."
        MARKUS_FEM @angry "Now come on—let’s get this over with."
        MC @surprised "Wait!"
        MARKUS_FEM @talk "What?"
        MC @talk "We need a name for you tonight."
        MC @serious "Calling you Markus would raise suspicions."
        MARKUS_FEM @talk "Just call me Marcia."
        MC @talk "Marcia..."
        show markus_fem at left
        with ease
        show mc at blurin, cleft
        with ease
        show cg_guard_hamun at cright_f with easeinright
        "{i}Marcia{/i} handed over the invitations."
        GUARD "Enjoy the evening."
        hide markus_fem
        hide mc
        with easeoutright
    elif QstTheTarbecks().PartyCompanion == "esme":
        show esme at cleft with easeinleft
        "Esme stepped forward, her tail swaying gently."
        "In her ornate dress, she drew every eye in the courtyard."
        "For a moment, I forgot I was used to seeing her clad in little more than gold jewelry."
        ESME @smile "Hello."
        MC @serious "You look..."
        ESME @laugh "Different than you’re used to?"
        MC @embarr "Y-Yes..."
        ESME @smile "Come on, I’d hate to be late."
        show esme at left
        with ease
        show mc at blurin, cleft
        with ease
        show cg_guard_hamun at cright_f with easeinright
        "The guard’s eyes lingered on Esme before stepping aside."
        GUARD "Enjoy the evening."
        hide esme
        hide mc
        with easeoutright

    scene black with dissolve
    $ LocSet("hamun_tarbeck_mainhall")
    $ wLocs["hamun_tarbeck_mainhall"].SetDayNightMatrixClass(None)
    $ BlockWaitGlobal(True)
    $ AutoTimeFreeze(True)
    $ LocFlush(dissolve)

    $ GoalComplete(QstTheTarbecks, 5)

    "Tarbeck’s home was a monument to excess."
    "Teal marble floors were inlaid with solid gold tiles that glittered in the light."
    "At the center stood a grand fountain depicting Siraeth, goddess of lust and desire."
    "Scantily dressed servants wove through the crowd, offering drinks on golden trays."
    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_9
    if QstTheTarbecks().PartyCompanion == "esme":
        show mc at cleft
        show esme at left
        with easeinleft
        ESME @smile "Now {i}this{/i} is a party."
        ESME @smile "So, am I to stay by your side and just look good, or...?"
        MC @talk "Mingle with some of the guests for now. I need to find a friend."
        ESME @talk "Fine. Come get me when you need me."
        hide esme with easeoutright
    elif QstTheTarbecks().PartyCompanion == "ves":
        show mc at cleft
        show ves at left
        with easeinleft
        VES @blush "...Are all humans so..."
        VES @blush "{i}Lustful?{/i}"
        MC @surprised "L-Let's stay focused on the task at hand."
        MC @talk "I need to find Sypha first."
        VES @talk "Don't take too long!"
        VES @shock "From the way some of them are looking at me, I don't think I'll be left to drink quietly in peace..."
        hide ves with easeoutright
    elif QstTheTarbecks().PartyCompanion == "kiara":
        show mc at cleft
        show kiara at left
        with easeinleft
        KIARA @smile "Bloody hells."
        KIARA @smile "Twenty coins says there's a room around here where they all shag."
        MC @serious "Stay focused."
        MC @talk "First things first—I need to find Sypha."
        KIARA @smile "I'll go grab a drink and be my usual charming self in the meantime!"
        KIARA @smile "Come get me if you need me."
        KIARA @blush "Or if you find one of those sex rooms and wanna take me for a whirl."
        hide kiara with easeoutright
    elif QstTheTarbecks().PartyCompanion == "markus":
        show mc at cleft
        show markus_fem at left
        with easeinleft
        MARKUS_FEM @blush "...If I were in my {i}normal{/i} form, I think I'd be overjoyed right now."
        MARKUS_FEM @blush "But I can't help feeling like a piece of meat on a hook, from the way some of them are looking at me."
        MC @talk "I need to find Sypha. Go grab a drink, and try not to draw too much attention to yourself."
        MARKUS_FEM @angry "I swear on the gods, if one of them grabs my ass..."
        MC @serious "I'll be back as quickly as I can."
        MARKUS_FEM @angry "Fine. Find me wherever the drinks are being served..."
        hide markus_fem with easeoutright
    show mc at center with ease
    MC "(Sypha... where in the hells are you?)"
    $ GoalShow(QstTheTarbecks, 6)
    $ QstSetProgress(QstTheTarbecks, 6)
    $ LocEnter()

label qst_TheTarbecks_CantLeaveParty:
    MC "(I can't leave yet.)"
    MC "(Not until I've found something I can use against Lord Tarbeck.)"
    $ LocEnterQ()

label qst_TheTarbecks_MeetSyphaInGarden:
    show sypha at cright_f
    with dissolve
    show mc at cleft with easeinleft
    SYPHA @happy "Ahh! There you are!"
    $ GoalComplete(QstTheTarbecks, 6)
    SYPHA @happy "Are you enjoying the party?"
    MC @think "It's... {i}unique?{/i}"
    SYPHA @talk "Good. Come with me."
    show sypha at blurin, center with ease
    "Taking my arm, Sypha pulled me away from the other guests."
    SYPHA @talk "The upper floors of the mansion are strictly off-limits to guests."
    SYPHA @talk "Tarbeck’s private quarters are bound to hold something useful—if we can get up there."
    MC @talk "Can’t you just sneak up there or something?"
    SYPHA @happy "Me? Yes."
    SYPHA @talk "You? No."
    SYPHA @think "Not without being swarmed by a few dozen guards and forced to fight your way through."
    SYPHA @happy "Not that I wouldn’t enjoy watching you dominate a room full of weaklings..."
    MC @serious "Then what do you propose?"
    SYPHA @talk "Tarbeck is hosting a series of {i}games{/i} tonight."
    SYPHA @talk "The winners are invited upstairs to his treasure room for a {i}reward{/i}."
    SYPHA @happy "That will be our opening."
    MC @serious "What kind of {i}games?{/i}"
    show sypha at blurin, center_f
    "Sypha smirked mischievously."
    SYPHA @happy "I’m told Lord Tarbeck enjoys keeping things... interesting."
    SYPHA @talk "The games should be starting soon. Head back to the main hall."
    MC @think "And what are you going to do in the meantime?"
    SYPHA @talk "I’ll find my own way upstairs."
    SYPHA @talk "You just find the pretty little toy you brought with you..."
    SYPHA @happy "{i}You’re going to need her.{/i}"
    MC @serious "What does that mean?"
    $ GoalShow(QstTheTarbecks, 7)
    $ QstSetProgress(QstTheTarbecks, 7)
    show sypha at blurin, center
    hide sypha with easeoutright
    "Sypha’s hand brushed my shoulder as she glided away without another word."
    show mc at center with ease
    MC @serious "({i}'Games'{/i}, huh?)"
    $ LocEnter()


label qst_TheTarbecks_PartyBegins:
    play sound "audio/cfx/small_bell.ogg"
    "{i}*Ding!*{/i}"
    $ GoalComplete(QstTheTarbecks, 7)
    scene cg_tarbeck_stairs_speech with dissolve
    "At the sound of a ringing bell, all eyes turned to the jovial Lord Tarbeck."
    TARBECK @smile "Good evening, my esteemed guests!"
    play sound "audio/cfx/small_crowd_applause.ogg"
    "The crowd clapped and cheered as Lord Tarbeck raised his hands, settling them the way one might calm an eager pet."
    TARBECK @smile "Those of you who have joined us before already know—tonight is a very special night."
    TARBECK @smile "Yes, yes... this marks the tenth anniversary of our monthly midnight soirees!"
    TARBECK @smile "Over the years, we have dazzled you, teased you, and..."
    TARBECK @smile "{i}Indulged{/i} desires you didn’t even know you had!"
    play sound "audio/cfx/small_crowd_applause_2.ogg"
    "The applause came again—shorter, but far more eager."
    TARBECK @smile "Tonight, however, we’ve decided to go all out!"
    TARBECK @smile "We want the games this evening to be truly unforgettable!"
    "Tarbeck’s eyes swept across the crowd, lingering on me a moment longer than I liked."
    TARBECK @smile "For those of you new to our little tradition, the rules are simple!"
    TARBECK @smile "Beyond those red doors lies a series of rooms—each offering a new and exciting challenge!"
    TARBECK @smile "Win a challenge, earn a gold token."
    TARBECK @smile "The first couple to turn in five tokens wins!"
    MC "({i}Is that all?{/i})"
    MC "(A few perverted parlor games?)"
    MC "(This should be easy...)"
    TARBECK @smile "But remember—these challenges are not for the faint of heart!"
    TARBECK @smile "Know your limits..."
    TARBECK @smile "{i}And enjoy your evening!{/i}"
    TARBECK @smile "And do keep your eyes open!"
    TARBECK @smile "{i}There may be other games available for those who explore...{/i}"
    TARBECK @smile "Now—let the games begin!"
    $ LocFlush(dissolve)
    "With a sharp clap of his hands, the red chamber doors swung open."
    "Beyond them stretched a long passageway lined with multicolored doors, each marked with strange insignias."
    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_10

    if QstTheTarbecks().PartyCompanion == "esme":
        show mc at cleft
        show esme at left
        with easeinleft
        ESME @smile "Games, huh?"
        ESME @smile "I’ve had clients suggest their own little {i}'games'{/i} before."
        ESME @smile "And here I thought this party was going to be boring..."
    elif QstTheTarbecks().PartyCompanion == "ves":
        show mc at cleft
        show ves at left
        with easeinleft
        VES @blush "[player_name!t], I... I’m not sure about this."
        VES @blush "I’m not very {i}experienced{/i} with things like this."
        MC @smile "Don’t worry, Ves."
        MC @serious "Let’s just see what we’re dealing with."
        VES @blush "{i}V-Very well...{/i}"
    elif QstTheTarbecks().PartyCompanion == "kiara":
        show mc at cleft
        show kiara at left
        with easeinleft
        KIARA @angry "Anyone tries shoving something up my ass and I’ll paint the halls with their guts."
        MC @talk "..."
        KIARA @serious "That said..."
        KIARA @serious "I expect flowers, shiny things, and a whole lot of sweet talk if you try anything."
        MC @talk "So you’re not worried at all?"
        KIARA @smile "I just hope they don’t disappoint..."
        KIARA @smile "I’m looking forward to seeing what kind of trouble we can stir up, darling."
    if QstTheTarbecks().PartyCompanion == "markus":
        show mc at cleft
        show markus_fem at left
        with easeinleft
        MARKUS_FEM @surp "..."
        MC @scared "U-Uh... I’m sure we can—"
        MARKUS_FEM @surp "I swear on the gods, [player_name!t]."
        MARKUS_FEM @angry "{i}Sometimes I fucking hate you.{/i}"
        MC @scared "So... what do we do?"
        MARKUS_FEM @angry "What do you think?"
        MARKUS_FEM @angry "Not like we’ve got much choice now, is there?!"

    $ GoalShow(QstTheTarbecks, 8)
    $ QstSetProgress(QstTheTarbecks, 8)
    MC "(Shit...)"
    $ LocEnter()

label qst_TheTarbecks_AlreadyPlayedInThisRoom:
    "(We have already been to this room.)"
    $ LocEnterQ()

label qst_TheTarbecks_WatcherMainhall_TurnInTokens:
    show cg_tarbeck_watcher at cright_f with dissolve
    show mc at cleft with easeinleft
    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_11
    if QstTheTarbecks().PartyCompanion == "ves":
        show ves at left with easeinleft
    if QstTheTarbecks().PartyCompanion == "esme":
        show esme at left with easeinleft
    if QstTheTarbecks().PartyCompanion == "markus":
        show markus_fem at left with easeinleft
    if QstTheTarbecks().PartyCompanion == "kiara":
        show kiara at left with easeinleft
    WATCHER "Are you here to hand in your tokens?"
    menu:
        "Yes." if PlayerItemQty("qst_tarbeck_golden_token") >= 5:
            pass

        "No.":
            WATCHER "I see… Then return when you have enough for a chance to win fabulous prizes!"
            $ LocEnter()

    show mc at nod
    $ PlayerRemItem("qst_tarbeck_golden_token", PlayerItemQty("qst_tarbeck_golden_token"))
    $ GoalComplete(QstTheTarbecks, 101)
    "Upon handing over the tokens, the watcher bowed, glancing to another figure off to the right and giving a silent nod."
    "Moments later, the thunderous ringing of a great gong echoed through the halls as all eyes suddenly turned toward us."
    show cg_tarbeck_watcher at blurin, center with ease
    WATCHER "AND WE HAVE A WINNER FOR THIS EVENING'S GAMES!"
    "Around us, masked figures clapped and cheered, some whistling from the shadows."
    hide cg_tarbeck_watcher with easeoutright
    "Above, descending the grand staircase with a broad, delighted smile, Lord Tarbeck appeared."
    show lord_tarbeck at cright_f with easeinright
    TARBECK @smile "Ahhh! Wonderful! WONDERFUL!"
    TARBECK @smile "Such spirit! Such indulgence! What joy it brings me to see beautiful people embracing the finer pleasures of life!"
    $ CharMeet("lord_tarbeck")
    TARBECK @smile "And what shall I call my new champions of debauchery?"
    MC @smile "[player_name!t]."
    if QstTheTarbecks().PartyCompanion == "ves":
        MC @talk "And this is Ves."
        TARBECK @shock "An Orcess… at my little soirée?"
        TARBECK @smile "What a delightful surprise!"
        VES @talk "... You are smaller than I expected."
        "I nudged Ves discreetly with my elbow."
        VES @think "Uhh… I mean, the pleasure is mine."
    elif QstTheTarbecks().PartyCompanion == "kiara":
        MC @talk "And this is Kiara."
        TARBECK @smile "Kiara, ahhh!"
        TARBECK @smile "From the deep north, perhaps?"
        KIARA @smile "Angmurus. Born and raised."
        TARBECK @smile "Ah, yes… I once had a companion from Angmurus."
        TARBECK @happy "She was… {i}delicious.{/i}"
        "Something about the way he said it made my skin crawl."
        "Kiara's composure shifted slightly."
        KIARA @talk "... {i}Is that so?{/i}"
    elif QstTheTarbecks().PartyCompanion == "markus":
        MC @talk "This is Mark—"
        MC @talk "I mean, Marcia."
        TARBECK @smile "Marcia… my…"
        TARBECK @happy "{i}Aren't you a beauty?{/i}"
        TARBECK @smile "Careful, or I might try to steal you away from your husband!"
        MARKUS_FEM @sad "We're not—"
        MARKUS_FEM @think "I mean, uhh…"
        MARKUS_FEM @happy "You flatter me, my lord."
        "Marcia gave an awkward curtsey."
    elif QstTheTarbecks().PartyCompanion == "esme":
        MC @smile "This is Esme."
        TARBECK @think "Hmm? A katai?"
        TARBECK @think "We do not usually allow… the riff-raff in."
        TARBECK @happy "{i}But exceptions can always be made.{/i}"
        TARBECK @happy "{i}Especially for such beauty.{/i}"
        "Esme's face remained calm, offering only the faintest smile."
        "Whatever she truly felt was known only to herself."
        ESME @smile "A pleasure, my lord."
    TARBECK @smile "Well then! There will be plenty of time for socializing shortly!"
    TARBECK @smile "But first, your prize, I imagine?"
    TARBECK @smile "Come, follow me!"

    $ LocSet("hamun_tarbeck_west_wing")
    $ LocFlush(dissolve)
    show lord_tarbeck at cright with easeinleft
    show mc at cleft with easeinleft
    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_12
    if QstTheTarbecks().PartyCompanion == "ves":
        show ves at left with easeinleft
    if QstTheTarbecks().PartyCompanion == "esme":
        show esme at left with easeinleft
    if QstTheTarbecks().PartyCompanion == "markus":
        show markus_fem at left with easeinleft
    if QstTheTarbecks().PartyCompanion == "kiara":
        show kiara at left with easeinleft
    show lord_tarbeck at blurin, cright_f
    TARBECK @talk "... Oh!"
    TARBECK @talk "Before we continue to the treasure hall, your companion will need to wait behind."
    TARBECK @talk "We have a lovely tea room prepared. Perhaps my wife might even join them…"
    TARBECK @angry "{i}If she can stop incessantly moping about, that is.{/i}"
    MC @think "Why must my companion stay behind?"
    TARBECK @smile "I only allow one guest at a time inside the treasure hall."
    TARBECK @smile "{i}Rules are rules, after all.{/i}"
    MC @serious "(…I need to tread carefully. But perhaps this could be a chance to learn something useful about Tarbeck.)"
    MC @smile "Of course. I understand."
    show mc at blurin, cleft_f
    if QstTheTarbecks().PartyCompanion == "ves":
        MC @smile "Ves, follow the guard to the tea room."
        MC @smile "{i}Maybe see if Lord Tarbeck's wife will give you a little tour?{/i}"
        VES @talk "Hmm… Very well."
        hide ves with easeoutleft
        MC "(I hope Ves understood what I meant…)"
    elif QstTheTarbecks().PartyCompanion == "kiara":
        MC @smile "Kiara, follow the guard to the tea room."
        MC @smile "{i}Maybe see if Lord Tarbeck's wife will give you a small tour?{/i}"
        KIARA @think "A tour?"
        "She studied my face for a moment."
        KIARA @smile "Aye, love."
        KIARA @smile "Pick out something shiny for us. I'll see you soon."
        hide kiara with easeoutleft
    elif QstTheTarbecks().PartyCompanion == "markus":
        MC @smile "Marcia, follow the guard to the tea room."
        MC @smile "{i}Maybe see if Lord Tarbeck's wife will give you a small tour?{/i}"
        MARKUS_FEM @sad "I really think I should stay by your side…"
        MC @smile "Darling… please."
        MC @smile "{i}Trust me.{/i}"
        MC @think "{i}Remember what we discussed earlier.{/i}"
        MARKUS_FEM @think "...I—"
        MARKUS_FEM @surp "...!"
        MARKUS_FEM @happy "Yes. Of course."
        MARKUS_FEM @happy "I shall see you soon, {i}dear.{/i}"
        hide markus with easeoutleft
    elif QstTheTarbecks().PartyCompanion == "esme":
        MC @smile "Esme, follow the guard to the tea room."
        MC @smile "{i}Maybe see if Lord Tarbeck's wife will give you a small tour?{/i}"
        "Esme smiled softly, her hand briefly brushing my arm."
        ESME @smile "Of course, dear. Whatever you desire."
        hide esme with easeoutleft
    show mc at blurin, cleft
    TARBECK @smile "Splendid! Right this way!"
    scene black with dissolve
    "... Several long, gaudy corridors later."
    $ LocSet("hamun_tarbeck_treasury")
    $ LocFlush(dissolve)
    "The emerald doors swung open with a heavy groan, revealing a room so decadent it felt unreal."
    "Towers of gold coins glittered beneath the glow of candlelight."
    "Rubies, emeralds, and sapphires spilled carelessly across carved marble pedestals."
    "Even the ceiling sparkled with embedded diamonds, twinkling like stolen constellations."
    show lord_tarbeck at cright_f
    show mc at cleft
    with dissolve
    TARBECK @smile "Magnificent, isn't it?"
    TARBECK @smile "Every glittering sin this world can offer… and all of it mine."
    MC @surprised "It's… obscene."
    TARBECK @smile "Obscenely beautiful."
    TARBECK @smile "{i}Now… allow me to show you my most precious treasure.{/i}"
    "Something stirred in the shadows."
    "A faint rustle. A whisper of claws on soft gold."
    MC @think "What was that…?"
    TARBECK @talk "{i}Attend me.{/i}"
    "They emerged from the dark like nightmares dressed in silk."
    show lord_tarbeck at right_f with ease
    show kelebeth at cright_f with easeinright
    "Women at first glance… until the inhuman details sharpened."
    "Hooved feet scraping gold."
    "Curved horns rising through cascades of hair."
    "Tails flicking lazily, like predators idly deciding whether to strike."
    show mc at left with ease
    MC "What in the hells are these?"
    TARBECK "Succubi."
    TARBECK "Living embodiments of desire… and exquisite agony."
    "Their eyes glowed red — hungry — as they slinked closer."
    KELEBETH "{i}Mmmm…{/i}"
    KELEBETH "{i}This one smells {b}delicious{/b}, my lord.{/i}"
    "A chill crawled down my spine."
    TARBECK "I have spent years seeking pleasure… and knowledge."
    TARBECK "In that pursuit, I found these creatures."
    TARBECK "We reached… an arrangement."
    "They hissed softly, moving nearer, the air thickening with heat and danger."
    TARBECK "I give them protection."
    TARBECK @smile "In return…"
    TARBECK @happy "{i}They feed.{/i}"
    MC "Feed…?"
    TARBECK "Tell me something."
    TARBECK "Did the GTC send you to steal from me…?"
    TARBECK "{b}Or to murder me?{/b}"
    MC "…Fuck."
    TARBECK "Enjoy yourselves, my darlings!"
    TARBECK "Dinner… is served!"
    KELEBETH "Mmm…"
    KELEBETH "Surrender, prey."
    KELEBETH "We promise to make your death…"
    KELEBETH "{i}deliciously slow.{/i}"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    $ GoalShow(QstTheTarbecks, 102)
    MC "Not tonight!"
    $ TransformMC(True)
    $ TransformKiara(False)
    $ TransformMarkus(True)
    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_13
    if QstTheTarbecks().PartyCompanion == "ves":
        show ves at cleft with easeinleft
        "The doors to the treasure room kicked open as Ves entered, axes in hand."
        VES @angry "[player_name!t]! The bastard's guards just tried to-"
        "Ves' eyes widened as she stared at the three succubus before me."
        MC @serious "Could do with some help here!"
        $ CharHeal("ves")
        $ PartyAddChar("ves")
    elif QstTheTarbecks().PartyCompanion == "kiara":
        show kiara at cleft with easeinleft
        "The doors swung open as Kiara entered, blood stained blade in hand."
        KIARA @angry "It's a setup! The bastards just-"
        KIARA @shock "Oh fuck!"
        MC @angry "Get over here and help me!"
        $ CharHeal("kiara")
        $ PartyAddChar("kiara")
    elif QstTheTarbecks().PartyCompanion == "markus":
        show markus_transformed at cleft with easeinleft
        "The doors burst open as Markus, transformed with blood-stained claws rushed towards me."
        MARKUS "It's a trap! Lord Tarbeck-"
        MC "Little late for the warning!"
        MARKUS "Grghh!"
        $ CharHeal("markus")
        $ PartyAddChar("markus")
    $ StartBattle(BattleData(BackgroundImage = "pbat_treasure_room", CharIDList_Right = ["kelebeth", "e_succubus", "e_succubus"], CanTransform = False))
    scene black with dissolve
    $ TransformMC(False)
    $ TransformMarkus(False)
    "Their confidence shattered."
    "Suddenly trembling, the succubi recoiled, backing away like frightened animals."
    $ LocFlush()
    $ GoalComplete(QstTheTarbecks, 102)
    show mc_transformed at left
    show kelebeth at cright_f
    with dissolve
    SHYAHTAN "{i}You fools think you can claim the body that belongs to SHYAHTAN?!{/i}"
    MC "(What are you doing—)"
    KELEBETH "Wait… that scent…"
    KELEBETH "No… it can't be…!"
    SHYAHTAN "KNEEL."
    $ AutoMus(True)
    "Their wills broke instantly."
    hide kelebeth
    show cg_kelebeth_kneel at cright_f
    with dissolve
    $ Pause()
    KELEBETH "Y-Yes!"
    KELEBETH "M-Mighty one!"
    KELEBETH "Forgive our ignorance!"
    MC "(What in the hells is happening?!)"
    MC "You KNOW them?"
    SHYAHTAN "(Not them. Their kind.)"
    SHYAHTAN "(Their filth stirs an old memory.)"
    show lord_tarbeck at right_f with easeinright
    TARBECK @shock "Wh—what?!"
    TARBECK @angry "Eat him already!"
    KELEBETH @laugh "We wouldn't dare."
    KELEBETH @blush "Not when he belongs to…"
    KELEBETH "{i}a superior race.{/i}"
    show cg_kelebeth_kneel at center_f with ease
    "She crawled toward me reverently."
    "Shyahtan moved my hand — and she pressed her face to it, trembling like a worshipper before a god."
    TARBECK @shock "What…?"
    KELEBETH "We thought your kind extinct."
    KELEBETH "The last divine creation…"
    KELEBETH "{i}Perfect bodies crafted in the Great One's image.{/i}"
    KELEBETH "We feed on lust."
    KELEBETH "None have ever truly satisfied us."
    "Her lips brushed my knuckles. Her hand slid boldly toward my groin."
    KELEBETH "{i}Until you.{/i}"
    TARBECK @shock "Ha… HAHAHA!"
    TARBECK @angry "Impossible!"
    "The hot blood boiled as I snarled at Lord Tarbeck, stepping towards him."
    MC "{b}I'm going to rip out your throat and TEAR YOU APART!{/b}" 
    "Lord Tarbeck cowered for a moment, stepping back terrified as I raised my talons to part his guts from his stomach."
    TARBECK @shock "W-WAIT! PLEASE! I beg of you!"
    TARBECK @shock "What do you want from me?!"
    "Before I could strike, I felt an invincible force restrain my hand."
    SHYAHTAN "(Wait...)"
    SHYAHTAN "(As satisfying as it would be to part his organs from his body...)"
    SHYAHTAN "(Do we not need him alive to get home?)"
    "I stopped, the boiling anger still simmering, but I knew Shyahtan was right."
    MC "(I...)"
    MC "(FUCK!)"
    MC "(I'M SICK OF BEING THE GTC'S LAPDOG!)"
    SHYAHTAN "(Our time will come... Their women... Their coin... Their land.)"
    SHYAHTAN "(It will all belong to us.)"
    "I lowered my hand as the succubus continued to gather around me, snarling at Lord Tarbeck." 
    KELEBETH "You know nothing of devotion."
    KELEBETH "We did not simply give ourselves to them."
    KELEBETH "{i}We were proud to be chosen.{/i}"
    KELEBETH "Please great one... I am called Kelebeth, let me serve you!"
    #show mc_transformed at left
    hide cg_kelebeth_kneel
    show kelebeth at center_f
    with dissolve
    show kelebeth at blurin, cleft_f
    with ease
    hide lord_tarbeck with dissolve
    "The doors burst open."
    show sypha at cright
    show lady_tarbeck at right_f
    with easeinright
    "Sypha strode in with her usual playful smirk... and a blade to Lady Tarbeck's throat."
    SYPHA "Apologies for the delay!"
    TARBECK "Briana!!"
    TARBECK "Unhand her!"
    SYPHA "Everything alright in here, darling?"
    show sypha at blurin, cright_f
    "Then she saw them."
    "The air changed."
    "Her eyes narrowed into razors."
    SYPHA @angry "Remove your hands from him."
    SYPHA "Or I'll remove them permanently."
    show kelebeth at blurin, cleft
    KELEBETH @angry "Watch your tongue, mortal!"
    SYPHA "Demorai sovereign right. He's claimed."
    show mc_transformed at shake
    MC @angry "ENOUGH!"
    MC "STOP FIGHTING!"
    show lord_tarbeck at center with dissolve
    "Tarbeck tried to bolt — Sypha's blade blocked him."
    show sypha at nod
    SYPHA "Ah-ah."
    SYPHA "Stay."
    TARBECK @angry "What do you want?! Kill me and be done with it!"
    MC "I didn't come to kill you!"
    TARBECK "Then WHY?!"
    TARBECK "And don't insult me by denying the GTC sent you!"
    MC @serious "They sent me to find leverage. To make you approve the weapons deal."
    TARBECK @smile "Blackmail."
    TARBECK "Of course."
    TARBECK @angry "You think me a monster?"
    TARBECK @angry "You have no idea what THEY are capable of."
    "His cold gaze flicked to Sypha."
    TARBECK "A Demorai working with them?"
    SYPHA "I have my reasons."
    MC @think "You knew?"
    TARBECK "Everyone knows HER."
    TARBECK "Most who make deals with you end up dead."
    SYPHA @happy "They shouldn't break contracts then."
    MC @angry "Terms. NOW."
    "Lord Tarbeck paused… then smirked."
    TARBECK "Exclusive transport rights."
    TARBECK "And…"
    TARBECK "Two million coins."
    MC "Fine."
    MC "(… I sure hope the GTC really is as rich as everyone believes them to be.)"
    TARBECK "Ah—"
    TARBECK "One more thing."
    "He looked at his wife."
    TARBECK @smile "Make my wife interesting."
    "The world dropped silent."
    LADY_TARBECK @scared "W-What?!"
    TARBECK "We bore each other."
    TARBECK "Were it not for your family, you'd be gone."
    LADY_TARBECK @angry "You cannot be serious!"
    MC "What exactly do you want?"
    TARBECK @angry "Break her."
    TARBECK "Twist her."
    TARBECK "Turn her into something useful."
    TARBECK "Anything other than this miserable, joyless ghost chained to me."
    LADY_TARBECK "We made vows!"
    LADY_TARBECK "I endured your depravity!"
    LADY_TARBECK "Your filth!"
    LADY_TARBECK "And THIS is what you demand of me?!"
    LADY_TARBECK "{i}Haven't you humiliated me enough?!{/i}"
    TARBECK "You will obey."
    TARBECK "Or I strip EVERYTHING."
    TARBECK "Your rooms. Your comforts. Your life."
    "She fled in tears."
    TARBECK @talk "Do not disappoint me, [player_name!t]."
    if QstTheTarbecks().PartyCompanion == "esme":
        TARBECK "Your companion waits outside."
    if not CharIsMet("lady_tarbeck"):
        $ CharMeet("lady_tarbeck")
    KELEBETH @scared "Wait!"
    KELEBETH @sad "At least let us taste him…"
    KELEBETH @blush "{i}We'll behave.{/i}"
    "I glanced at Tarbeck."
    "He shrugged."
    TARBECK "Do as you wish."
    TARBECK "I'll punish them later regardless."
    menu:
        "Fuck the Succubus girls":
            "Sypha's eyes narrowed, glaring daggers at the smug succubus."
            SYPHA @angry "Hmph."
            KELEBETH @laugh "You Demorai are always so confident in your {i}'claims'{/i}."
            KELEBETH @laugh "But it seems to me this one will do exactly as he pleases."
            KELEBETH "{i}*Soft chuckle*{/i}"
            SYPHA @mad "...Is that a little challenge, hell-whore?"
            SYPHA @smug "Perhaps then, we should settle this now?"
            SYPHA @smug "Let's find out who's 'claim' is better."
            scene black with dissolve
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            KELEBETH "Wait—what are you—"
            KELEBETH "{i}*Gasp!*{/i}"
            KELEBETH "... Oh."
            KELEBETH "{b}Interesting!{/b}"
            $ PlaySexFx(audio.moans_breaths_loop, 1)
            $ PlaySexFx2(audio.moans_muffled_suckey, 1)
            scene sypha_tarbeck_succubus_orgy_vag_1 with dissolve
            $ Pause()
            "A moment later, all three succubi were bent over and tightly bound, their asses in the air as Sypha gleefully made Kelbeth eat at her womanhood obediently."
            SYPHA "There, there, dear!"
            SYPHA "Look! They're alllllllll nice and ready for you!"
            KELEBETH "Mhmm… Consider yourself lucky, little Demorai. I'm in a generous mood tonight."
            SYPHA "Such confidence!"
            SYPHA "You woudn't think the three of you folded almost immediately!"
            KELEBETH "Degenerate…"
            SYPHA "A little rich coming from someone who suck's cock to survive, don't you think?"
            $ PlaySexFx(audio.moans_breaths_loop, 1)
            scene sypha_tarbeck_succubus_orgy_vag_2 with dissolve
            $ Pause()
            "Sypha watched as I drew my cock and pressed it to Kelebeth's dripping slit."
            "She groaned deeply, welcoming me as my cock sank into her inch by inch."
            KELEBETH "Mmfghhh! Harder! Give me every drop of your essence!"
            KELEBETH "Break us!"
            SYPHA "Hahaha! Are you already hanging on for dear life?"
            SYPHA "The mighty succubus brought to heel in round one!"
            KELEBETH "Ssssshut up!"
            KELEBETH "You could not possibly understand the connection between our kinds! Cur!"
            KELEBETH "Urghhh!"
            "Her tight heat squeezed and pulsed around me, clinging almost desperately, refusing to let me go."
            "Her slick juices coated me, and whatever they were made of, they hit like aphrodisiac fire in my veins—the world narrowed to heat, flesh, and the pounding need to rut her senseless."
            SYPHA "Darling…"
            SYPHA "Don't just focus on her now!"
            SYPHA "Can't you see her little pets want some attention too?"
            SYPHA "{i}Why don't you show them what you can really do?{/i}"
            $ PlaySexFx(audio.moans_breaths_loop, 1)
            scene sypha_tarbeck_succubus_orgy_vag_3 with dissolve
            $ Pause()
            "Two tentacles emerged, with elongated tongues from the bulbous heads, they licked at each of the succubus' holes, greedily lapping them up."
            "The succubus' moaned and whimpered, pleading their mistress for more, but she was far too occupied between Sypha's pussy and my cock."
            KELEBETH "Mmmfghhh!"
            SYPHA "Your mistress is busy, whores!"
            SYPHA "occupy yourselves!"
            "The two succubus' squirmed, moaning hotly as the tongues contined to lap up their juices."
            SYPHA "Mhhh..."
            SYPHA "What else can those tentacles do?"
            SYPHA "I want to see it with my own eyes!"
            scene sypha_tarbeck_succubus_orgy_vag_4 with dissolve
            $ Pause()
            "The two tentacles thrust forward, attaching onto the succubus' asses as the tongues, squirmed and forced their way deep into their needy cunts."
            "They moaned like beasts in heat, begging, gasping, pleading as the tendrils drove deeper."
            SYPHA "Ahh...!"
            SYPHA "Now THAT's more like it!"
            SYPHA "If only I could have their expressions right now painted! Huehue!"
            "Lewd squelches and desperate cries filled the room as I rearranged their insides."
            "Sypha grabbed Kelebeth by the hair and ground her face between her thighs."
            SYPHA "Ahhh… That's it, whore!"
            SYPHA "Try and play with what's MINE, hmm?"
            KELEBETH "{i}*Slurp!* *Shlick!*{/i}"
            SYPHA "How are their holes, my love?"
            MC "Stop—ahhh—calling me that!"
            MC "And they're TIGHT!"
            MC "Gods… these whores could wring the life out of a lesser man!"
            KELEBETH "MMMMFGHH!!"
            SYPHA "Inferior products before you get to sample me!"
            SYPHA "I can assure you of that!"
            "Kelebeth shuddered, pushing back, her ass bouncing with every thrust."
            "Her 'lesser' sisters writhed, their bodies jolting as the tentacles churned them mercilessly."
            SYPHA "Ghood… little… sucuuubus…"
            KELEBETH "Mmfghhhh…!"
            "Their bodies quaked as they were used, Sypha watching me with possessive delight."
            "Her gaze a curious mix of curiousity and desire."
            "Time lost meaning—heat, flesh, and pleasure drowned everything."
            "Sypha relished every second of control, delighting in watching me tame the so-called queens of desire."
            SYPHA "Do you understand now, little succubus?"
            "Kelebeth and the others could only moan in broken submission."
            SYPHA "This one…"
            SYPHA "{i}Is mine.{/i}"
            "My balls tightened."
            "Sypha sensed it instantly—eyes bright, lips curling as if proud… or possessive… or both."
            "I grabbed Kelebeth's ass, claws digging just enough to draw blood as I slammed deep and stayed there."
            "She wailed, tongue spilling from her mouth as I filled her."
            $ PlaySexFx2(audio.forgean_finish)
            scene sypha_tarbeck_succubus_orgy_vag_finish with flash
            $ Pause()
            MC "{i}*ROARRRRR!*{/i}"
            SYPHA "That's it… Make them beg!"
            SYPHA "Make them addicts!" 
            $ UnlockGalFlag("sypha", "tarbeck_succubus_orgy", "tarbeck_party")
            $ UnlockGalSceneAndGrantXp("sypha", "tarbeck_succubus_orgy")
            "Seed spilled, dripping down her thighs as the other succubi scrambled hungrily beneath, lapping it eagerly from the floor."
            $ StopSexFx()
            "Sypha rose back to her feet, cheeks flushed as her sweat glistened in the light."
            "She adjusted her hair, and smiled victoriously."
            $ LocFlush()
            show mc_transformed at cleft
            show sypha at cright_f
            with dissolve
            SYPHA @happy "There. That was fun, wasn't it?"
            MC @surprised "Did we just…?"
            MC @surprised "With succubi?"
            SYPHA @think "Amateurs."
            SYPHA @happy "Come, husband."
            SYPHA @talk "Before these whores start begging for another round…"
            $ AutoMus(True)
        "Refuse":
            MC @serious "Another time, perhaps."
            "Pitifully, the succubi pouted, their seductive grins fading as they slunk back into the darkness, vanishing from sight."
    scene black with dissolve
    "... A short while later, Lord Tarbeck had his guards escort us out."
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_14

    if QstTheTarbecks().PartyCompanion == "kiara":
        show mc at cright_f
        show kiara at cleft
        with dissolve
        KIARA @angry "Bloody bastards!"
        show kiara at blurin, cleft_f
        "Kiara turned to scream at the manor itself."
        KIARA @shock "YOUR FUCKING DECOR WAS HIDEOUS ANYWAY!"
        show kiara at blurin, cleft
        KIARA @think "Did you find what you were lookin' for?"
        MC @think "Not quite, but..."
        MC @talk "I think I have another way to get Tarbeck to give the GTC what they want."
        KIARA @think "Hmm... well then..."
        KIARA @smile "I guess I'll be heading back to {i}The Pale Dragon.{/i}"
        show kiara at center with ease
        "Kiara stepped closer, gently pressing her lips to my cheek in a soft kiss."
        show kiara at nod
        KIARA @smile "Mwha!"
        KIARA @smile "Thanks for a nice night, love."
        KIARA @smile "We should do it again sometime..."
        KIARA @think "{i}Preferably more just the two of us next time.{/i}"
        MC @embarr "Right. That sounds... nice."
        hide kiara with easeoutright
    elif QstTheTarbecks().PartyCompanion == "ves":
        show mc at cright_f
        show ves at cleft
        with dissolve
        VES @angry "FIRST THEY TRY TO KILL US."
        show ves at shake
        VES @angry "THEN THEY DARE THROW US OUT?!"
        MC @talk "Relax, Ves. We didn't get what we came for, but..."
        MC @think "I have another way in to make Tarbeck agree to the deal."
        VES @talk "...Are you hurt?"
        VES @talk "If they have hurt you, I shall claim their skulls as trophies!"
        MC @talk "I'm fine. No beheadings tonight."
        VES @angry "Tsch!"
        VES @talk "Very well then. I shall return to {i}The Pale Dragon.{/i}"
        show ves at blurin, cleft_f
        show ves at blurin, cleft
        "Ves turned to leave, but paused, glancing back toward me."
        VES @blush "...I would like us to spend more time together."
        VES @blush "As a cou—"
        "Her cheeks burned red."
        VES @blush "As good friends!"
        MC @sad "Ves, I—"
        VES "I must go!"
        show ves at blurin, cleft_f
        hide ves with easeoutleft
        MC @surprised "Ves, wait!"
        MC @angry "(Damn it.)"
    elif QstTheTarbecks().PartyCompanion == "markus":
        show mc at cright_f
        show markus_fem at cleft
        with dissolve
        MARKUS_FEM @talk "Well that didn't exactly go to plan, did it?"
        MC @angry "Not quite."
        MC @think "But I think I have another angle now to force Tarbeck's hand."
        MARKUS_FEM @talk "Hm. Well, that's something at least."
        MARKUS_FEM @angry "Now if you'll excuse me, I'm getting out of this stuffy dress."
        MARKUS_FEM @angry "Gods, how do women wear these things?"
        MC @smile "So, you didn't enjoy being a woman, huh?"
        MARKUS_FEM @think "I didn't say that..."
        MC @surprised "Huh?"
        MARKUS_FEM @think "It's... {i}different.{/i}"
        MARKUS_FEM @talk "What about you? Must've been strange taking me as your date."
        MARKUS_FEM @think "Really? You couldn't find {i}anyone{/i} else?"
        MC @embarr "You were the first person who came to mind."
        MARKUS_FEM @surp "...!"
        MARKUS_FEM @blush "That so?"
        MARKUS_FEM @blush "..."
        MC @embarr "..."
        MARKUS_FEM @blush "I-I'll head back to {i}The Pale Dragon.{/i}."
        MARKUS_FEM @blush "Thanks for… whatever {i}this{/i} was."
        MC @sad "I'll see you later."
        hide markus_fem with easeoutright
        MC "(...Gods, what am I thinking?)"
        MC @angry "(That's Markus, damn it!)"
    elif QstTheTarbecks().PartyCompanion == "esme":
        show mc at cright_f
        show esme at cleft
        with dissolve
        ESME @talk "{i}*Ahem*{/i}"
        ESME @talk "Did you find what you were looking for?"
        MC @think "Kind of... but not quite."
        ESME @sad "Shame."
        ESME @smile "Still, I had a nice night."
        show esme at center with ease
        "Esme stepped closer, her tail swaying lazily."
        ESME @smile "If you ever need a partner in crime again, swing by the {i}Kitten's Paw{/i}."
        ESME @smile "I'm always up for a little {i}fun.{/i}"
        MC @smile "I'll keep that in mind."
        ESME @talk "{i}*Sigh*{/i}"
        ESME @talk "I should get going."
        MC @smile "Be safe, Esme."
        hide esme with easeoutright
        MC @smile "(She was... different than I imagined.)"
    show mc at center_f with ease
    show mc at blurin, center
    MC @serious "(Urghh, focus damn it!)"
    MC @angry "(Fuck... that could have gone better.)"
    MC @think "(Now I need to figure out how to appease BOTH Lord Tarbeck and his wife.)"
    MC @think "(Make her 'interesting,' huh?)"
    MC @think "({i}...Hmmm.{/i})"
    $ LocFlush(dissolve)
    $ QstComplete(QstTheTarbecks)
    $ LocEnterQ()