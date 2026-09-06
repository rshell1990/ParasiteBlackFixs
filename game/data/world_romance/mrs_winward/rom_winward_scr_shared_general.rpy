
label nov_mrs_winward_brought_more_hides:
    $ RomanceWinward().SeenSecondHidesBatchScene = True
    show mrs_winward at cright_f with dissolve
    show mc at cleft with easeinleft
    MRS_WINWARD @happy "Ahhh! My favorite customer returns!"
    MRS_WINWARD @happy "Brought me any more hides today?"
    MC @smile "Nice to see you too, Mrs Winward."
    "Mrs Winward giggled playfully."
    MRS_WINWARD @lewd "Would you like some tea, or perhaps-"
    MR_WINWARD @angry "Kionni! KIONNI!"
    MRS_WINWARD @angry "Urghh..."
    show mr_winward at right_f with easeinright
    MRS_WINWARD @angry "What is it dear?"
    MR_WINWARD @angry "Where in the seven hells did you hide my coin bag?"
    MRS_WINWARD @angry "No, you are not gambling away playing cards and getting drunk with your friends again!"
    MR_WINWARD @angry "What?! It's my coin, woman!"
    MRS_WINWARD @angry "No, it's OUR coin!"
    MRS_WINWARD @angry "You barely lift a finger anymore to help out around here as is!"
    MR_WINWARD @angry "BAH! You wait, woman! Perhaps you're happy wasting away in this store on scraps, but once I win my fortune, THEN we'll see how you feel about me!"
    hide mr_winward with easeoutleft
    "As Mr Winward stormed out, Mrs Winward did her best to stay composed but was clearly simmering with rage beneath the surface."
    MRS_WINWARD @angry "That FOOL will be the ruin of us both!"
    MC @think "Does he often gamble away your earnings like that?"
    MRS_WINWARD @angry "Hmph!"
    MRS_WINWARD @angry "It's been like this for a while... He swears down he'll win us enough coin to leave this place."
    MRS_WINWARD @angry "He keeps talking about us moving to Ramon and trying to set up business there."
    MRS_WINWARD @angry "But whatever coin I give him is {i}always{/i} spent and lost forever."
    MRS_WINWARD @angry "But still he asks for more and more..."
    "Suddenly, her eyes widened as the light came back into them."
    MRS_WINWARD @shock "Wait! I have an idea!"
    MRS_WINWARD @blush "W-Would you be interested in helping out an old lady, deary?"
    MC @think "What is it?"
    MRS_WINWARD @sad "My husband... Could you perhaps follow him at night and make sure he doesn't spend too much?"
    MRS_WINWARD @shock "I could give you some coin!"
    MRS_WINWARD @embarr "Or perhaps some other reward?"
    MC  "Hmm... I'll think on it."
    $ QstStart(QstTheJackpot)
    MRS_WINWARD  "Mmm, well, did you have any business you wished to discuss in the meanwhile, deary?"
    call processDialogue("mrs_winward_root") from _call_processDialogue_53
    $ LocEnter()

label rom_winward_plug:
    ARLENA "A {i}special{/i} toy?"
    MC @talk "One with a 'bull' insignia carved into the gem."
    "Arlena raised a brow at the comment."
    ARLENA "...A bull?"
    ARLENA "Why?"
    MC @talk "Can it be done, or not?"
    ARLENA "Of course, though it will take a little more time to produce."
    ARLENA "Come back in a week, I'll try to have it for you by then."
    MC @talk "Thanks."
    ARLENA @smile "You owe me one."
    $ QstSetProgress(EventArlenaOrderButtplugForWinward, 1)
    $ EventArlenaOrderButtplugForWinward().Arlena_ButtplugPickupDay = GetGameDay() + 4
    $ NoteLock("RomWinward_FindButtplug")
    $ NoteUnlock("RomWinward_PickupButtplug")
    return

label rom_winward_plug_notready:
    ARLENA "I'm still working on it."
    ARLENA "Come back in a few."
    MC "Okay."
    return

label rom_winward_plug_pickup:
    ARLENA "Here it is."
    $ QstSetProgress(EventArlenaOrderButtplugForWinward, 2)
    $ PlayerAddItem("qst_winward_plug")
    $ NoteLock("RomWinward_PickupButtplug")
    $ NoteUnlock("RomWinward_BringButtplug")
    ARLENA @smile "Try not to get Markus too excited!"
    MC @think "Haha, very funny."
    MC "(I should give this to Mrs Winward when I have the chance.)"
    return

label rom_winward_plug_bring:
    MRS_WINWARD @happy "Hm? What is-"
    $ PlayerRemItem("qst_winward_plug")
    MRS_WINWARD @shock "O-Oh my...!"
    MRS_WINWARD @embarr "Is this... one of those things I hear are becoming quite popular amongst ladies of the night?"
    MC @smile "You'd be shocked; I'm sure more than a few {i}high-class{/i} ladies are interested as well."
    MRS_WINWARD @embarr "...S-So, I take it that you're interested in more than just looking at my um..."
    MRS_WINWARD @blush "{i}Rear.{/i}"
    MC @smile "And here I was sure you must have felt my eyes on it after all this time staring."
    MRS_WINWARD @lewd "Hmm... Well then, I had best start training with it, hadn't I?"
    MRS_WINWARD @lewd "I'd hate to disappoint my new lover, fufu. {image=[ICON.HEART]}"
    MRS_WINWARD @lewd "G-Give me a few days to umm, try it and {i}adjust.{/i}"
    MRS_WINWARD @lewd "And we'll go from there..."
    $ QstComplete(EventArlenaOrderButtplugForWinward)
    $ RomanceWinward().DayToUnlockAnalSex = GetGameDay() + 1
    return