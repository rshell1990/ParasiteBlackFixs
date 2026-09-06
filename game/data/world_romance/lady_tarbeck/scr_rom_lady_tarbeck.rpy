#########################################################
# tarbeck post-quest romance
# Requires completion of The Tarbecks Part II.
# Lady Tarbeck's first post-quest interaction permanently selects one route: 
# ROMANCE, DARK_MAGE, BIMBO or CLOSED.
# Event priority: birth events, pregnancy announcements, scheduled events, random events, default interaction
# Lady Tarbeck cannot become pregnant until RomanceStage == 5
# LIBRARY, QUARTERS and BELAMORE appointments remain active until completed.
# Pregnancy and birth events temporarily override appointments but do not clear them.
# After RomanceStage == 5, her default location is the Tarbeck manor main hall daytime
# The bg_tarbeck_playroom_hallway and its connected sex rooms remain locked 
# unless their associated scene is active.
#########################################################
label rom_tarbeck_intro:
    $ NoteLock("tarbeck_rom_1visit")
    $ QstSetProgress(RomanceLadyTarbeck, 1)
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @shock "Oh!"
    LADY_TARBECK @blush "I, umm, didn't expect you back so soon..."
    "Lady Tarbeck paused nervously."
    LADY_TARBECK @blush "A-About what my husband said..."
    LADY_TARBECK @angry "AND THIS IS ABSOLUTELY NOT ME AGREEING TO HIS ABSURD PROPOSAL!"
    LADY_TARBECK @blush "... But... umm... humoring the idea a little."
    LADY_TARBECK @blush "How would it work?"
    MC @think "What do you mean, my lady?"
    LADY_TARBECK @talk "I mean, I have no idea how any of this works anymore... I've been married for years!"
    LADY_TARBECK @sad "I don't even really... fully know myself anymore."
    LADY_TARBECK @happy "Sometimes I just wish I was a happy fool... Life would certainly be easier as a silly, happy, beautiful girl..."
    "A voice rumbled from within."
    SHYAHTAN "(That could be arranged.)"
    menu:
        "{image=[ICON.HEART]} Why don't we just... spend a little time together and see where it takes us?": 
            $ RomanceLadyTarbeck().Kind = "romance"
            LADY_TARBECK @think "Like... a proper courting?"
            LADY_TARBECK @sad "... It feels so strange thinking about things like that."
            LADY_TARBECK @sad "Especially knowing I'm a married woman, hardly some young damsel anymore."
            MC @talk "The choice is yours, my lady."
            "Lady Tarbeck paused for a moment to think."
            LADY_TARBECK @blush "... V-Very well."
            LADY_TARBECK @blush "I suppose this is, at least, something I'd be most comfortable with."
            LADY_TARBECK @talk "Could... Could we maybe head back to the markets this evening?"
            MC @smile "The markets, my lady?"
            LADY_TARBECK @sad "I treated you pretty horribly the first time we went there."
            LADY_TARBECK @smile "... I would like to make it up to you."
            MC @smile "Then shall I escort you, or-"
            LADY_TARBECK @talk "Just meet me there."
            LADY_TARBECK @smile "And... don't be late."
            $ NoteUnlock("tarbeck_rom_romance_meetmarket")

        "{image=[ICON.HEART]} Then let's find out who you are... starting with learning more about your dark magecraft.": 
            $ RomanceLadyTarbeck().Kind = "darkmage"
            LADY_TARBECK @scared "I... No."
            LADY_TARBECK @scared "It's far too dangerous."
            LADY_TARBECK @sad "A merchant lord's wife... becoming a dark mage?"
            LADY_TARBECK @sad "It's a scandal, even for Hamun."
            LADY_TARBECK @sad "{i}Not to mention the risk of what I might become...{/i}"
            MC @talk "You've spent so long denying this part of yourself."
            MC @sad "A part that isn't going away just because you will it so."
            LADY_TARBECK @sad "I... But what of duty?"
            LADY_TARBECK @sad "What of honor?"
            MC @talk "I think... dark mage or not, you would still be a good person."
            MC @sad "But I need to know you will be able to defend yourself if I leave Hamun."
            LADY_TARBECK @sad "I... I don't know."
            MC @talk "You have lived your whole life in service of everyone else."
            MC @sad "Isn't it time you put yourself first, just once?"
            LADY_TARBECK @sad "I... I need to think."
            LADY_TARBECK @sad "Come back tomorrow. Until then..."
            LADY_TARBECK @sad "I need to be alone."
            $ NoteUnlock("tarbeck_rom_darkmage_meettomorrow")

        "{image=[ICON.HEART]} ... Would you choose to be a silly, happy, beautiful girl?" (Req_Perk = "perception_warp"):
            $ RomanceLadyTarbeck().Kind = "bimbo"
            LADY_TARBECK @smile "Would I choose it if I had the choice?"
            LADY_TARBECK @smile "I mean, maybe?"
            LADY_TARBECK @talk "But... it's impossible."
            SHYAHTAN "(It can be arranged...)"
            MC @think "(Really?)"
            SHYAHTAN "(Yes... though we would need some... genetic material.)"
            MC @think "If... I told you it was possible, that I could make it happen..."
            MC @think "What would you say?"
            LADY_TARBECK @shock "I-"
            LADY_TARBECK @think "What would it even entail?"
            SHYAHTAN "(Severe body modification, enhanced strength, fertility and dopamine at the expense of a few neurons.)"
            MC @think "(Uhh... What does-)"
            SHYAHTAN "(She will be beautiful, happy and healthy... but lacking in intelligence.)"
            MC @talk "You would be beautiful and happy, but..."
            MC @talk "Your wit may be dulled quite significantly."
            LADY_TARBECK @think "So I'd be an idiot?"
            MC @think "Well... that's one way to put it."
            "Lady Tarbeck paused, considering the proposition."
            LADY_TARBECK @sad "... Hmm."
            MC @think "... You're not saying no?"
            LADY_TARBECK @talk "I... I need time to think."
            LADY_TARBECK @talk "Please, come back in a few days."
            MC "As you wish, my lady."
            $ QstSetDelay(RomanceLadyTarbeck, 2)
            $ NoteUnlock("tarbeck_rom_bimbo_meetinacoupledays")

        "{image=[ICON.HEART_CROSS]} My lady, perhaps it is in everyone's interest that we just stay friends.":
            $ RomanceLadyTarbeck().Kind = "closed"
            $ QstComplete(RomanceLadyTarbeck)
            LADY_TARBECK @shock "I-"
            LADY_TARBECK @sad "... Yes, that probably is for the best."
            "The words she spoke were betrayed by the soft sadness in her voice."
            LADY_TARBECK @sad "Well, I suppose the world seems to have other plans for you anyway..."
            LADY_TARBECK @sad "... Good luck, [player_name]."
            LADY_TARBECK @sad "I think you're going to need it."

    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()

#########################################################
# Romance route
# Scene 1 - Romance - Hamun markets - Evening
# IMPLEMENTATION NOTES:
# EQUIRES: Route == ROMANCE and RomanceStage == 1.
# Lady Tarbeck appears as a clickable sprite in Hamun Market during the NIGHT only
# and remains there until completed.
# Clicking her starts the scene immediately.
label rom_tarbeck_romance_meet_market:
    $ QstSetProgress(RomanceLadyTarbeck, 2)
    $ NoteLock("tarbeck_rom_romance_meetmarket")
    show lady_tarbeck at cleft with dissolve
    show lady_tarbeck at blurin, cright_f with ease
    show mc at cleft with easeinleft
    LADY_TARBECK @smile "There you are."
    MC @smile "So, my lady, where shall we begin?"
    LADY_TARBECK @smile "This way..."
    show lady_tarbeck at blurin, cright
    hide lady_tarbeck
    hide mc
    with easeoutright
    scene black with dissolve
    $ TimeAdvBy(TIME_1H)
    "For the next hour, Lady Tarbeck moved from stall to stall, inspecting the different wares."
    "With a keen eye, she bartered over some cooked, skewered meat."
    $ LocFlush()
    show lady_tarbeck at cleft
    show mc at cright_f
    with dissolve
    "Biting into one of the skewers, she smiled happily."
    MC @smile "You seem far more comfortable here than you ever do dealing with courts and politics."
    LADY_TARBECK @talk "It's more honest."
    "Lady Tarbeck held one of the skewers to my lips, letting me take a bite."
    LADY_TARBECK @smile "Not bad, hm?"
    MC @smile "Needs more salt."
    LADY_TARBECK @talk "Mm, I know just the stall!"
    "A few minutes later, after more bargaining, some salt was sprinkled over my food as Lady Tarbeck seemed quite pleased with herself."
    LADY_TARBECK @smile "... Would you walk me to the docks?"
    MC @smile "Of course, my lady."
    scene black with dissolve
    $ TimeAdvBy(TIME_1H)
    $ LocSet("hamun_port")
    $ Pause(0.1)
    $ LocFlush()
    show mc at cleft
    show lady_tarbeck at center
    with dissolve
    "Arriving at the docks, Lady Tarbeck smiled as she watched the lights of the boats drift across the water."
    LADY_TARBECK @smile "Pretty, is it not?"
    show lady_tarbeck at blurin, cright_f with ease
    "As I turned toward Lady Tarbeck, she sheepishly brushed a lock of hair over her shoulder."
    LADY_TARBECK @blush "I'm not very... good at all this anymore."
    MC @smile "Stop worrying so much and just enjoy yourself."
    "I stepped closer to Lady Tarbeck as she sighed."
    LADY_TARBECK @sad "What if I can't do this anymore?"
    LADY_TARBECK @sad "I'm not the girl I was back then. I'm-"
    hide mc
    hide lady_tarbeck
    show cg_lady_tarbeck_kiss_normal at center
    "Leaning forward, I silenced Lady Tarbeck with a kiss."
    "Her eyes widened as a surprised whimper escaped her lips."
    LADY_TARBECK "Mmmfgh?!"
    hide cg_lady_tarbeck_kiss_normal
    show mc at cleft
    show lady_tarbeck at cright_f
    with dissolve
    "She lightly pushed me away, her cheeks burning red."
    LADY_TARBECK @shock "Y-You kissed me?!"
    MC @smile "I did."
    LADY_TARBECK @blush2 "Y-You didn't even ask!"
    MC @smile "I didn't."
    MC @smile "I just did what I'd wanted to do since the moment we first met."
    "Lady Tarbeck paused for a moment, her eyes darting up and down my body."
    "I thought for a moment she might snap at me or walk away."
    hide mc
    hide lady_tarbeck
    show cg_lady_tarbeck_kiss_normal at center
    "... Instead, she threw herself forward, planting her lips against mine."
    LADY_TARBECK "Mhmm..."
    "After a few tender moments, she slowly pulled herself away, this time for real."
    hide cg_lady_tarbeck_kiss_normal
    show mc at cleft
    show lady_tarbeck at cright_f
    with dissolve
    LADY_TARBECK @blush "I..."
    LADY_TARBECK @blush "My head feels like it's spinning after that."
    MC @think "Are you alright?"
    LADY_TARBECK @blush "Yes, I just... Take me home, please."
    scene black with dissolve
    "I escorted Lady Tarbeck safely back home."
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    show lady_tarbeck at cleft
    show mc at cright_f
    with dissolve
    LADY_TARBECK @smile "T-Thank you."
    LADY_TARBECK @smile "Tonight was... strange."
    LADY_TARBECK @smile "Strange but fun."
    "Lady Tarbeck paused again, clearing her throat as she spoke."
    LADY_TARBECK @blush "T-Tomorrow... I need to head back to the library to pick up some books."
    LADY_TARBECK @smile "Perhaps... you could meet me there?"
    MC @smile "Of course, my lady."
    MC @lewd "If you let me pick out a book for you to read."
    "Lady Tarbeck blinked at the request, her cheeks flushing red once more as she smiled."
    LADY_TARBECK @smile "V-Very well."
    LADY_TARBECK @smile "Then I shall see you in the morning."
    LADY_TARBECK @smile "{i}... Make sure it's a good book.{/i}"
    hide lady_tarbeck with easeoutright
    show mc at blurin, center with ease
    $ Pause(0.25)
    $ NoteUnlock("tarbeck_rom_romance_meetlibrary")
    $ LocEnter()

#########################################################
# REPEAT:
# - Requires RomanceStage == 5 and an active LIBRARY appointment.
# - Remove Lady Tarbeck from her default manor location and move her to Hamun Library during the DAY.
# - Clear the LIBRARY appointment and restore her default manor schedule after completion.
label rom_tarbeck_romance_meet_library:
    if RomanceLadyTarbeck().Romance_ScheduledGig == "lib":
        $ RomanceLadyTarbeck().Romance_ScheduledGig = None
        $ SetRepeatVariant(True)
        $ NoteLock("tarbeck_rom_romance_meetlibrary")
        $ RomanceLadyTarbeck().HadSexToday = True
    if IsFirstTime():
        $ NoteLock("tarbeck_rom_romance_meetlibrary")
        $ QstSetProgress(RomanceLadyTarbeck, 3)
        show lady_tarbeck at cright_f
        with dissolve
        show mc at cleft with dissolve
        LADY_TARBECK @smile "You made it."
        "Lady Tarbeck closed whatever book she was reading and bounced over towards me."
        "I'd never seen her so 'light' before."
        MC @smile "Picked up the books you came here for?"
        LADY_TARBECK @smile "Yes, but..."
        LADY_TARBECK @blush2 "You mentioned finding a book for me, andddd..."
        "Her hand brushed ever so delicately against mine."
        LADY_TARBECK @blush2 "I want to see what you pick for me."
        "Sensing the challenge, I made my way over to the different bookshelves and traced my finger along the rows."
        hide mc with easeoutright
        show lady_tarbeck at blurin, center with ease
        "Eventually, I found myself drawn to a familiar-sounding name:"
        "a book that had become the subject of scandalous gossip in Novaras a few years ago."
        "{i}The Affairs of Lady Calicross.{/i}"
        show lady_tarbeck at cleft with ease
        show mc at cright_f with easeinright
        "I smirked, handing the book to Lady Tarbeck."
        MC @smile "This one."
        "Lady Tarbeck raised a brow as she curiously took the book."
        LADY_TARBECK @think "Is it... a romance?"
        MC @smile "It caused quite a stir in Novaras in its day."
        "Lady Tarbeck bit down on her lower lip as she flipped through some of the pages."
        LADY_TARBECK @blush2 "C-Come... Take a seat next to me and keep me company while I read a little."
        LADY_TARBECK @blush2 "You know... {i}to keep me safe.{/i}"
    else:
        show lady_tarbeck at cright_f
        with dissolve
        show mc at cleft with dissolve
        LADY_TARBECK @blush2 "Ahh... Should we continue reading from where we left off last time?"
        MC @smile "Let's..."
        LADY_TARBECK @blush2 "Then I'll fetch the book."
    label replay_tarbeck_romance_library_hj:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_handjob_preg_idle
    else:
        scene lady_tarbeck_romance_handjob_nopreg_idle
    with dissolve
    $ Pause()
    "Taking a seat next to Lady Tarbeck, I watched as her eyes carefully swept across the room for anyone who might be watching us."
    "The library was empty today, and as she opened the book and skipped through the pages, she began reading."
    if IsFirstTime():
        LADY_TARBECK "{i}Lady Calicross found herself in an unusual position, or perhaps, a familiar one.{/i}"
        LADY_TARBECK "{i}Legs bent towards her head as her lover, Imana, thrust his member into her tightness.{/i}"
        LADY_TARBECK "{i}It was a good thing Lord Calicross was so very, very far away.{/i}"
        "Lady Tarbeck giggled."
        LADY_TARBECK "Gods, it's very explicit!"
        LADY_TARBECK "Is there... much literature like this in Novaras?"
        MC "If you know where to look, my lady."
        "Lady Tarbeck bit down on her lower lip as she continued skimming through a few more pages, growing hot and flustered as she did so."
        LADY_TARBECK "... Oh my."
        MC "Giving you ideas?"
        LADY_TARBECK "No!"
        LADY_TARBECK "I mean... M-Maybe?"
        "Lady Tarbeck laughed nervously as she continued to read."
        LADY_TARBECK "It's strange to suddenly think about all this kind of thing now."
        LADY_TARBECK "I..."
        "Her eyes flashed towards me."
        LADY_TARBECK "... If... I wanted to be brave."
        LADY_TARBECK "To do something that would have been unthinkable for me just a few days ago."
        LADY_TARBECK "Where would I start?"
        "Now she looked to me like I was a tutor, a guiding hand, as she fluttered her eyes so uncertainly."
        MC "{i}... You start by remembering what it means to touch a different man.{/i}"
        LADY_TARBECK "H-How would-"
        "As I pulled out my cock, Lady Tarbeck nearly fled from her seat instinctively, only barely stopping herself as she looked down towards my member."
        LADY_TARBECK "W-What are you doing?!"
        MC "My lady... There's no one here."
        MC "You said you wanted to do something unthinkable. Well, here it is."
        MC "{i}Touch.{/i}"
        MC "{i}It.{/i}"
        "Lady Tarbeck paused, her eyes frantically darting around."
        "Her mouth opened to voice unfinished protests, each one cut off halfway, but her eyes kept returning to my hard cock."
        LADY_TARBECK "We can't just-!"
        LADY_TARBECK "I... I shouldn't-!"
        LADY_TARBECK "But...!"
        LADY_TARBECK "..."
        "Finally, biting her lower lip, she reached out with a nervous, shaky hand and grabbed my member."
    else:
        LADY_TARBECK "{i}As Lady Calicross found herself in the darkened alleyway, her new lover's hands fumbled to tear away enough of her robes that he might take her here and now.{/i}"
        LADY_TARBECK "{i}She groaned, pressing herself against the wall as she felt him enter her.{/i}"
        "Lady Tarbeck wasted no time, her other hand reaching over to pull out my member and let it flop free."
        MC "... Do you just intend to leave it hanging out like that?"
        "Lady Tarbeck laughed as she cleared her throat."
        LADY_TARBECK "{i}*Ahem*{/i}"
        LADY_TARBECK "{i}Sir Dana! Please! Don't stop! P-Put it here!{/i}"
        LADY_TARBECK "{i}Not even my husband gets to use me here!{/i}"
        "Lady Tarbeck snickered as she read."
        LADY_TARBECK "What do you think?"
        LADY_TARBECK "Would you pull me down some dark alleyway and have your wicked way with me?"
        MC "Right now, if you don't do something, I might just have my wicked way with you right here..."
        "Lady Tarbeck smirked, reaching over to grab my cock."
    $ PlaySexFx(audio.adara_hj_loop, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_handjob_preg_1
    else:
        scene lady_tarbeck_romance_handjob_nopreg_1
    with dissolve
    $ Pause()
    if IsFirstTime():
        "Nervously, Lady Tarbeck's hand began to move back and forth as she stroked my cock."
        "Her cheeks burned red as nervous sweat dripped from her brow, her eyes darting between the book and my cock."
        LADY_TARBECK "I-Is this good?!"
        LADY_TARBECK "G-Gods... Uhh!"
        LADY_TARBECK "{i}What am I doing?!{/i}"
        MC "Ahh... Describe it, {i}my lady.{/i}"
        LADY_TARBECK "T-That's vulgar!"
        MC "And arousing when it comes from your lips."
        LADY_TARBECK "... I-It's..."
        LADY_TARBECK "V-Very thick."
        MC "Thicker than your husband's?"
        LADY_TARBECK "Yes."
        MC "So thick your hand can't quite get around it?"
        LADY_TARBECK "Y-Yes!"
        MC "{i}Big and thick enough that you wonder how it might fit inside you?{/i}"
        LADY_TARBECK "O-Oh gods!"
        LADY_TARBECK "P-Please... Hurry up and finish before someone sees us!"
    else:
        "Lady Tarbeck happily stroked my cock as she hummed to herself, still reading her book."
        MC "Ahh... You've gotten better at this, my lady."
        LADY_TARBECK "Must be all the {i}'practice'{/i} I get in with you."
        "Lady Tarbeck feigned reading, but as her cheeks flushed red, I knew how turned on she was."
        "The noble, pious Lady Tarbeck... stroking her lover's cock in a public library as she read a salacious book."
        LADY_TARBECK "{i}She covered her mouth, moaning over and over again.{/i}"
        LADY_TARBECK "... You know, I think at this point I might be able to outdo Lady Calicross."
        MC "How bold of you to say, my lady."
    $ PlaySexFx(audio.adara_hj_loop_x2, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_handjob_preg_2
    else:
        scene lady_tarbeck_romance_handjob_nopreg_2
    with dissolve
    $ Pause()
    "Biting her lower lip, Lady Tarbeck's hand moved faster as she stroked me, desperate to make me finish quickly."
    if IsFirstTime():
        LADY_TARBECK "I-Is this good for you?!"
        MC "Mhmm... Yes."
        MC "Are you actually able to read while tending to me like this?"
        LADY_TARBECK "Y-Yes..."
        LADY_TARBECK "{i}... With great concentration.{/i}"
        "Lady Tarbeck's delicate hand moved desperately, squeezing lightly as she did her best to make me finish."
        "Her eyes kept nervously darting around, looking for anyone coming or going."
        LADY_TARBECK "P-Please finish!"
        MC "Ask me nicely."
        LADY_TARBECK "I a-am!"
        MC "Say please again."
        LADY_TARBECK "P-Please!"
        MC "Heh, I missed that... Did you say something?"
        LADY_TARBECK "{i}P-Please! Please! Please!{/i}"
        MC "{i}*Huff*{/i} I'm close..."
        MC "That's it—Ahh!"
        MC "Tell me."
        MC "Tell me what you feel."
        LADY_TARBECK "My heart is racing!"
        MC "And?"
        LADY_TARBECK "And... And...!"
        LADY_TARBECK "{i}I-It's so exciting!{/i}"
        MC "Oh fuck!"
        LADY_TARBECK "C-Cum for me."
        LADY_TARBECK "Cum for me, please!"
        MC "HRGHHH...!"
    else:
        LADY_TARBECK "You know..."
        LADY_TARBECK "{i}I get some sick pleasure from doing this to you in public.{/i}"
        LADY_TARBECK "Perhaps my husband's perversions {i}did{/i} rub off on me a little after all."
        MC "And here I was hoping I would get all the credit."
        "Lady Tarbeck laughed, lightly squeezing my cock as she continued to stroke me quickly."
        "Her eyes still swept around the room for anyone who might walk in on us, but..."
        "{i}I wasn't quite sure she would stop if they did.{/i}"
        LADY_TARBECK "I want you to cum for me."
        LADY_TARBECK "I want you to cum. For. Me."
        MC "Ahh! Fuck!"
        MC "Lady Tarbeck! Ahh... I'm close!"
        LADY_TARBECK "Don't hold back."
        LADY_TARBECK "I want you to think about me every night like I think about you."
        LADY_TARBECK "I want your heart to ache..."
        LADY_TARBECK "{i}And I want you to call out my name when you cum.{/i}"
        MC "L-LADY TARBECKKK!"
    # flags
    if not IsFirstTime():
        if CharIsVisiblyPreg("lady_tarbeck"):
            $ UnlockGalFlag("lady_tarbeck", "library_hj", "var_rep_preg")
        else:
            $ UnlockGalFlag("lady_tarbeck", "library_hj", "var_rep_nopreg")
    # scene unlock
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "library_hj")
    # scene end
    $ PlaySexFx(audio.adara_hj_finish)
    $ ReduceInfectionFromSex("lady_tarbeck")
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_handjob_preg_cum
    else:
        scene lady_tarbeck_romance_handjob_nopreg_cum
    with dissolve
    $ Pause()
    if IsFirstTime():
        "Lady Tarbeck gasped as she looked down at the sticky, white seed now covering her hands."
        LADY_TARBECK "Y-You came!"
        LADY_TARBECK "I made you finish!"
        MC "That you did... my lady."
        "With a strange lightness to her and a nervous giggle, she pulled her hand away from my cock and wiped the cum from her hands with a napkin."
        LADY_TARBECK @smile "Oh gods... That was..."
        LADY_TARBECK @smile "Exhilarating!"
        MC @smile "I can hear your heart racing, you know."
        "Lady Tarbeck's eyes were filled with a strange mixture of adoration and lust."
        "It seemed I had awoken something within her after all."
        LADY_TARBECK @blush2 "I haven't touched another man since I married my husband."
        LADY_TARBECK @blush2 "I never knew things could be so..."
        LADY_TARBECK @blush2 "{i}*Huff*{/i} exciting."
        MC @smile "Well, your bedroom awaits, should you wish it, my lady."
        "Her mouth opened as if to answer enthusiastically, but at the last moment, she stopped herself."
        LADY_TARBECK @talk "... N-No, not yet."
        LADY_TARBECK @talk "I'm not ready for that yet."
        MC @talk "I see."
        LADY_TARBECK @talk "Come to see me."
        MC @think "When?"
        LADY_TARBECK @smile "Tomorrow, the day after that! I don't care!"
        LADY_TARBECK @blush2 "{i}I need to see you again.{/i}"
        MC @smile "As you command, my lady."
        MC @talk "Shall I escort you home?"
        LADY_TARBECK @smile "Not tonight... Tonight, I want to walk and..."
        LADY_TARBECK @smile "{i}Enjoy the air.{/i}"
        MC @smile "As you wish."
        $ QstSetDelay(RomanceLadyTarbeck, 1)
        $ NoteUnlock("tarbeck_rom_romance_meetatmanor_afterlibrary")
    else:
        "As the cum splashed onto her hand, Lady Tarbeck instinctively giggled and began licking her fingers clean."
        LADY_TARBECK "Oooh!"
        LADY_TARBECK "That was a big one."
        MC "Too bad it wasn't inside you, my lady."
        LADY_TARBECK "Fufu... Save the next load for the bedroom, my barbarian."
    scene black with dissolve
    $ StopReplay()
    $ AutoMus(True)
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()

##############################################################################################################################################################
# The player returns to the Tarbeck manor. Lady Tarbeck is waiting in the hall.
# IMPLEMENTATION NOTES:
# FIRST TIME:
#- Requires Route == ROMANCE and RomanceStage == 3.
#- Lady Tarbeck waits in the Tarbeck manor main hall until clicked.
#- Clicking her immediately begins the first-time garden scene.
#- She cannot be pregnant.
#- On completion, set RomanceStage = 4 and add the nightcap journal note.
# REPEAT:
#- Requires RomanceStage == 5.
#- Trigger directly from Lady Tarbeck's interaction menu.
#- Fade to black and begin the repeat garden scene immediately.
label rom_tarbeck_romance_meet_manor:
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @smile "There you are!"
    LADY_TARBECK @talk "... Walk with me?"
    scene black with dissolve
    label rom_tarbeck_romance_meet_manor_repeat:
    $ LocSet("hamun_tarbeck_garden_main")
    $ LocFlush()
    show lady_tarbeck at center
    show mc at cleft
    with dissolve
    if IsFirstTime():
        $ NoteLock("tarbeck_rom_romance_meetatmanor_afterlibrary")
        $ QstSetProgress(RomanceLadyTarbeck, 4)
        $ QstSetProgress(HouseLockTarbeckHouse, 3)
        "As we wandered slowly around the gardens, Lady Tarbeck clung to me, brushing herself against me as she smiled softly."
        LADY_TARBECK @smile "The other night was..."
        LADY_TARBECK @smile "{i}Special.{/i}"
        MC @smile "Well, you surprised me with your boldness."
        MC @lewd "... But do you think you'll be able to surprise me again?"
        LADY_TARBECK @shock "I..."
        LADY_TARBECK @shock "I don't know."
        show lady_tarbeck at blurin, center_f
        "I grabbed hold of Lady Tarbeck, pulling her in for a passionate kiss and embrace."
        LADY_TARBECK @blush "You... You're getting far too comfortable grabbing me whenever you feel like it."
        MC @smile "Only because you seem so comfortable when I do grab you, my lady."
        "Lady Tarbeck paused, sheepishly looking around."
        LADY_TARBECK @blush "{i}If...{/i}"
        LADY_TARBECK @blush "If we were to do something, would you be able to keep quiet about it?"
        LADY_TARBECK @blush "N-No one could know..."
        MC @smile "Did you have something in mind?"
        LADY_TARBECK @shock "I... I..."
        hide mc with easeoutleft
        hide lady_tarbeck with easeoutleft 
        "Her breathing grew louder until, suddenly, I felt her hands tugging at me, pulling me behind some bushes."
        MC "My lady! What are you-"
        LADY_TARBECK "I-I don't know!"
        "Dropping to her knees, Lady Tarbeck waited meekly, as though she wasn't quite sure what she was doing."
    else:
        "As we wandered around the gardens, Lady Tarbeck wasted little time grabbing my hand and pulling me behind a familiar bush."
        "Dropping to her knees, she looked up and smiled."
        show lady_tarbeck at blurin, center_f
        LADY_TARBECK "Get it out already."
    label replay_tarbeck_romance_garden_bj:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_bj_preg_idle
    else:
        scene lady_tarbeck_romance_bj_nopreg_idle
    with dissolve
    $ Pause()
    if IsFirstTime():
        "Pulling out my cock, Lady Tarbeck's eyes widened as she stared at the impressive member standing over her head."
        LADY_TARBECK "G-Gods... Seeing it up close like this."
        LADY_TARBECK "It's so..."
        "I could feel Lady Tarbeck's shaky, hot breath on my cock as she looked up, uncertain what to do."
        MC "Well, my lady?"
        LADY_TARBECK "I... I d-didn't really plan this far ahead!"
        LADY_TARBECK "S-Should I kiss it?"
        MC "Kiss it... And then wrap your lips around it."
        LADY_TARBECK "O-Oh...!"
        LADY_TARBECK "That's..."
        LADY_TARBECK "{i}Intimate.{/i}"
        "I couldn't help but laugh."
        MC "You're the one who dragged me here and dropped to your knees, my lady."
        LADY_TARBECK "I... I feel dizzy."
        LADY_TARBECK "Your thing smells so..."
        LADY_TARBECK "{i}Musky.{/i}"
        MC "It's your choice, my lady... We can stop now."
        MC "{i}Or you can show me how bold you really are.{/i}"
        "Lady Tarbeck's eyes lifted towards me as she paused."
        "Slowly, she inched forward, gently kissing the head of my cock before wrapping her lips around it."
    else:
        LADY_TARBECK "Gods... I've been playing with myself while thinking about tasting your cock these last few nights."
        MC "Missed me that much, my lady?"
        LADY_TARBECK "You've made me into such a wanton woman..."
        LADY_TARBECK "I can only think of one suitable punishment for corrupting me so!"
        MC "Which is?"
        "Lady Tarbeck inched forward, tenderly kissing my cock before wrapping her soft, warm lips around it."
    $ PlaySexFx(audio.kiara_bj_loop, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_bj_preg_1
    else:
        scene lady_tarbeck_romance_bj_nopreg_1
    with dissolve
    $ Pause()
    if IsFirstTime():
        "Shyly, she began to glide her lips clumsily back and forth."
        "I groaned approvingly, letting her know I was pleased as she curiously used her tongue to beat my meat."
        LADY_TARBECK "Ishhthishhghoodhh?"
        LADY_TARBECK "{i}*Slurp!*{/i} Mmfghh...!"
        MC "Mhmm! You're doing—Ahh! G-Good..."
        "Lady Tarbeck looked up towards me with innocent, doe-like eyes."
        "Given all the perversions she must have seen in this manor, she was remarkably... shy."
        LADY_TARBECK "ShouldhhIhhghooofastherr?"
        LADY_TARBECK "{i}*Slurp!* *Slurp!*{/i}"
        MC "Y-Yes! Ahh!"
    else:
        "Lady Tarbeck didn't wait."
        "Plunging forward, she wrapped her lips around my cock with desperate neediness and began sucking it."
        MC "Ahhh! GODS!"
        LADY_TARBECK "{i}*Slurp!*{/i} Mmfghh!"
        LADY_TARBECK "Sooghoodh!"
        "Lady Tarbeck's tongue thrashed and twisted, wrapping around my cock as she tried to take me deeper."
        "She tasted and savoured everything."
        MC "Gods, girl, you're getting—Ahh! Good!"
        LADY_TARBECK "Ihadhhhaghoodhhteacherrhh!"
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_bj_preg_2
    else:
        scene lady_tarbeck_romance_bj_nopreg_2
    with dissolve
    $ Pause()
    if IsFirstTime():
        "She began to move faster."
        "Pushing herself forward, she did her best to take me deeper as I groaned happily."
        "{i}She liked that.{/i}"
        "Clumsy and unsure whether what she was doing was working, Lady Tarbeck glided her lips faster."
        MC "Hrghh! G-Gods..."
        "Her lips clung to my cock as though she were sucking for dear life."
        "I thought I'd need to pull her off me to get her to stop."
        LADY_TARBECK "{i}*Slurp!* *Slurp!*{/i}"
        "Lady Tarbeck was like a woman possessed, her heart racing as she continued to pleasure me as best she could."
        "Technique aside, there was something boundlessly hot about her efforts..."
        "Eventually, her sloppy, enthusiastic efforts paid off as I found myself drawing close to the edge."
        MC "Mhmm... Ahh! I'm g-getting close!"
        MC "Where do you want me to-"
        "Lady Tarbeck didn't give me time to finish the sentence."
        "Gliding her lips back and forth, their tight seal firmly squeezed my cock. She'd already decided where she wanted me to finish."
        MC "L-Lady Tarbeck! I'm gonna-"
    else:
        "Lady Tarbeck threw herself forward, swallowing as much of my member as she could."
        "Her soft, eager lips continued to glide as quickly as they could over my cock, coating it in a warm, silvery layer of saliva."
        LADY_TARBECK "{i}*Slurp!* *Slurp!* *Slurp!*{/i}"
        "Lady Tarbeck's skill had improved considerably since she first took me like this."
        "Her tongue still thrashed and wrapped teasingly around my cock as she pushed herself forward."
        "Occasionally, she forced herself forward until her little button nose pressed against my pubic hair."
        MC "Hrghh! Gods, you've gotten good at this!"
        MC "I'm close!"
    if not IsFirstTime():
        if CharIsVisiblyPreg("lady_tarbeck"):
            $ UnlockGalFlag("lady_tarbeck", "garden_bj", "var_rep_preg")
        else:
            $ UnlockGalFlag("lady_tarbeck", "garden_bj", "var_rep_nopreg")
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "garden_bj")
    $ PlaySexFx(audio.kiara_bj_finish)
    $ ReduceInfectionFromSex("lady_tarbeck")
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_bj_preg_cum_1
    else:
        scene lady_tarbeck_romance_bj_nopreg_cum_1
    with flash
    $ Pause()
    "The rush of seed flooded Lady Tarbeck's mouth as she did her best to swallow every drop."
    LADY_TARBECK "Mmmfghhh?!"
    "Lady Tarbeck's eyes widened as I poured myself down her throat."
    "Her hands tapped against my leg as she clutched tightly at my clothes in a slight panic."
    MC "Gods! It's like your lips were made for this!"
    "Once I'd spent every last drop inside her, she slowly pulled her lips away and gasped for air."
    LADY_TARBECK "{i}*Cough!*{/i} You could drown someone in that!"
    "Wiping her lips, Lady Tarbeck rose back to her feet."
    $ StopReplay()
    $ AutoMus(True)
    if IsFirstTime():
        $ LocFlush()
        show mc at cleft
        show lady_tarbeck at cright_f
        with dissolve
        MC @smile "I'm in love."
        "Lady Tarbeck playfully hit my shoulder."
        MC @talk "Ow!"
        LADY_TARBECK "Not the words I expected to hear just because I put my lips around your {i}thing.{/i}"
        MC @smile "What words were you hoping to hear?"
        "Pouting playfully, she inched forward."
        LADY_TARBECK @blush2 "{i}That when I put my lips around your thing, it's the best you've ever had.{/i}"
        "She playfully brushed her hand over my shoulder before leaning over to whisper."
        LADY_TARBECK @blush "Tomorrow... Come to my quarters for a nightcap."
        "Her hand squeezed mine."
        LADY_TARBECK @blush "I'm done being unhappy."
        "She said nothing else, heading off and leaving me alone in the tranquillity of the garden."
        $ NoteUnlock("tarbeck_rom_romance_meetatquarters")
        $ QstSetProgress(HouseLockTarbeckHouse, 4)
    else:
        $ SetRepeatVariant(False)
    $ LocEnter()

label rom_tarbeck_romance_meet_quarters:
    if RomanceLadyTarbeck().Romance_ScheduledGig == "miss_vag":
        $ RomanceLadyTarbeck().Romance_ScheduledGig = None
        $ SetRepeatVariant(True)
        $ NoteLock("tarbeck_rom_romance_meetatquarters")
        $ RomanceLadyTarbeck().HadSexToday = True
    $ CharSetClothes("lady_tarbeck", "ling")
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    $ PlaySound("audio/cfx/doorthud.ogg")
    "As I entered Lady Tarbeck's quarters, she was waiting patiently in her nightgown."
    LADY_TARBECK @smile "You made it."
    show lady_tarbeck at center_f with ease
    "She stepped closer to me and smiled, her hands clasped together nervously."
    MC @think "Is Lord Tarbeck..."
    LADY_TARBECK @blush "Away on business."
    LADY_TARBECK @blush "H-He knows you're here, don't worry."
    MC @talk "I see... Then in that case."
    scene black with dissolve
    label replay_tarbeck_romance_quarters_missionary_vag:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "I didn't wait. Stripping us of our clothes, I pulled Lady Tarbeck into a passionate embrace."
    "Grabbing and squeezing her ass, I kissed her."
    LADY_TARBECK "Mhmmm..."
    "She practically dragged me onto the bed as she spread her legs expectantly."

    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_missionary_preg_idle
    else:
        scene lady_tarbeck_romance_missionary_nopreg_idle
    with dissolve
    $ Pause()

    if IsFirstTime():
        $ NoteLock("tarbeck_rom_romance_meetatquarters")
        $ QstSetProgress(RomanceLadyTarbeck, 5)
        $ QstSetProgress(HouseLockTarbeckHouse, 5)
        $ QstStart(PregLadyTarbeck)
        LADY_TARBECK "{i}*Huff*{/i} P-Please... Don't make me wait."
        LADY_TARBECK "It's... It's been so long..."
        LADY_TARBECK "I've forgotten what it feels like."
        $ CharSetLover("lady_tarbeck")
        "As I rubbed my cock against her glistening womanhood, she gulped."
        "With a gentle thrust, I was inside her."
    else:
        LADY_TARBECK "I've been thinking about this all night."
        LADY_TARBECK "Don't make me wait. I need to feel you inside me again."
        "Her pussy was already wet as I rubbed my cock against her mound."
        LADY_TARBECK "{i}Fuck me.{/i}"

    $ PlaySexFx(audio.kiara_tent_slow, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_missionary_preg_vag_1
    else:
        scene lady_tarbeck_romance_missionary_nopreg_vag_1
    with dissolve
    $ Pause()

    if IsFirstTime():
        "Lady Tarbeck's hands tightened around her legs as I began to thrust into her."
        "At last, the stoic, reserved wife was moaning hotly as she spread her legs for me."
        LADY_TARBECK "Ahhh..."
        LADY_TARBECK "It's been..."
        LADY_TARBECK "{i}*Huff*{/i} So long..."
        "Her soft moans filled the room as the bed began to creak."
        "Her tight, wet hole squeezed around me as her heart raced."
        MC "Ahh! Are you alright, my lady?"
        LADY_TARBECK "Y-Yes..."
        "She bit her lower lip as she looked down at my member sliding in and out of her."
        LADY_TARBECK "I'm... I'm doing it..."
        LADY_TARBECK "I'm actually having s-sex with someone else."
        MC "... Are you ready to feel how good it can be?"
        "She nodded shyly."
    else:
        "Feeling my cock glide in and out of her, Lady Tarbeck moaned softly as she smiled and teased."
        LADY_TARBECK "Gods, I wasn't able to walk straight the last time you-"
        LADY_TARBECK "Ooooh...!"
        LADY_TARBECK "Mmm, who cares?"
        "A mischievous smile appeared on her lips as she watched my member glide in and out of her."
        LADY_TARBECK "The worst that happens is my husband pesters me for details."
        LADY_TARBECK "So, do your worst."
        "Lady Tarbeck licked her lips enticingly as her tight hole squeezed around me."
        LADY_TARBECK "Rearrange this horny wife's insides."

    $ PlaySexFx(audio.kiara_tent_normal, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_missionary_preg_vag_2
    else:
        scene lady_tarbeck_romance_missionary_nopreg_vag_2
    with dissolve
    $ Pause()

    if IsFirstTime():
        "I began to move faster, slamming my cock into Lady Tarbeck as her eyes widened in surprise."
        LADY_TARBECK "O-Oh gods...!"
        LADY_TARBECK "S-Slow down! I haven't-"
        LADY_TARBECK "F-Fuck! It's too much! A-Ahh!"
        "Her moans became louder as, despite her faint protests, her tight snatch squeezed around me in excitement."
        "Her fingers tightened around her legs, but she refused to let them drop as she watched my cock sink in and out of her."
        "As she did her best to muffle the sound of her embarrassed moans, I began to feel her body tighten around me as her breath quickened."
        LADY_TARBECK "I... I think I'm close!"
        LADY_TARBECK "P-Please! Don't stop! Don't stop until you've-"
    else:
        "Slamming my cock into her, Lady Tarbeck only tried to pull her legs wider as she moaned happily."
        LADY_TARBECK "Y-Yes!"
        LADY_TARBECK "Ahh! F-Fuck me harder!"
        "Her skin glistened in the light as sweat trickled down her body."
        "Her moans grew louder as her wet womanhood squeezed tightly around me."
        MC "Mhhfh... You've changed so much since we first met!"
        LADY_TARBECK "No...{i}*Huff*{/i}"
        LADY_TARBECK "I just learned to let go and enjoy myself!"
        LADY_TARBECK "Now don't stop shoving that big prick into me until I cum!"
        "I did as Lady Tarbeck asked, fucking the neglected, unleashed little wife until..."
    if not IsFirstTime():
        $ PregRoll("lady_tarbeck")
        if CharIsVisiblyPreg("lady_tarbeck"):
            $ UnlockGalFlag("lady_tarbeck", "quarters_missionary", "var_rep_preg_vag")
        else:
            $ UnlockGalFlag("lady_tarbeck", "quarters_missionary", "var_rep_nopreg_vag")
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "quarters_missionary")
    $ ReduceInfectionFromSex("lady_tarbeck")
    $ PlaySexFx(audio.kiara_tent_finish)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_missionary_preg_vag_cum
    else:
        scene lady_tarbeck_romance_missionary_nopreg_vag_cum
    with dissolve
    $ Pause()
    MC "C-CUMMINGGG!"
    "Lady Tarbeck gasped as she felt the rush of hot seed pour into her."
    "She shuddered, her whole body tightening around me as she did her best to wring out every drop."
    "As her eyes rolled back in pleasure, a wavering, desperate moan finally escaped her lips."
    LADY_TARBECK "Ooooooohhhh...!"
    LADY_TARBECK "{i}*Huff*{/i} By the gods... That was..."
    scene black with dissolve
    $ AutoMus(True)
    $ StopReplay()
    "She didn't even finish her sentence, dropping her head back onto the bed as she soaked in the post-coital bliss."
    LADY_TARBECK "J-Just a few minutes and I'll...{i}*Huff*{/i} I'll get up..."
    if IsFirstTime():
        $ LocFlush()
        show lady_tarbeck at cright_f
        show mc at cleft
        with dissolve
        "Lady Tarbeck eventually rose to her feet and laughed."
        LADY_TARBECK @smile "We... We actually did it."
        LADY_TARBECK @talk "I feel..."
        LADY_TARBECK @smile "Happy... And ashamed... And..."
        LADY_TARBECK @blush "Oh gods, so many feelings at once!"
        MC @think "Are you alright?"
        LADY_TARBECK @smile "I... Yes."
        LADY_TARBECK @talk "I will be."
        LADY_TARBECK @smile "From now on, I'm going to live free."
        LADY_TARBECK @smile "Damn the consequences! What's the point in piety if it just leaves me miserable?"
        LADY_TARBECK @talk "N-Not when the man I love is right in front of me."
        MC @surprised "Lady Tarbeck..."
        LADY_TARBECK @blush2 "Come see me... When you can."
        LADY_TARBECK @blush2 "I won't hold back anymore."
        LADY_TARBECK @smile "{i}I want all of you from now on... Understand?{/i}"
        MC @smile "... Yes, Lady Tarbeck."
        "Lady Tarbeck smiled."
        LADY_TARBECK @smile "Come see me soon... [player_name]."
        LADY_TARBECK @smile "You won't regret it."
    scene black with dissolve
    $ CharSetClothes("lady_tarbeck", "normal")
    $ LocSet("hamun_dist_merch_lord")
    $ Pause(0.1)
    $ LocEnter()

label rom_tarbeck_romance_meet_quarters_anal:
    if RomanceLadyTarbeck().Romance_ScheduledGig == "miss_anal":
        $ RomanceLadyTarbeck().Romance_ScheduledGig = None
        $ SetRepeatVariant(True)
        $ NoteLock("tarbeck_rom_romance_meetatquarters")
        $ RomanceLadyTarbeck().HadSexToday = True
    label replay_tarbeck_romance_quarters_missionary_anal:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_missionary_preg_idle
    else:
        scene lady_tarbeck_romance_missionary_nopreg_idle
    with dissolve
    $ Pause()
    LADY_TARBECK "{i}*Heavy breathing*{/i}"
    "Lady Tarbeck squirmed slightly as she waited anxiously for what was to come."
    "Her cute asshole twitched as my cock lightly rubbed and prodded against it."
    LADY_TARBECK "B-Be gentle... Alright?"
    LADY_TARBECK "Just because I {i}learned{/i} how to prep this hole w-watching the others."
    LADY_TARBECK "Doesn't mean I'm very good at taking things {i}t-there...{/i}"
    "Gently pushing, Lady Tarbeck bit down on her lower lip as she felt the pressure against her tight little hole."
    "She whimpered and then her ass spread to take the first inch of my cock."
    $ PlaySexFx(audio.kiara_tent_slow, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_missionary_preg_anal_1
    else:
        scene lady_tarbeck_romance_missionary_nopreg_anal_1
    with dissolve
    $ Pause()
    LADY_TARBECK "{i}*Gasp!*{/i}"
    "As she felt my cock plunge into her ass, Lady Tarbeck moaned quietly as it began to churn her insides."
    "Her tight ring squeezed effortlessly around my cock as she whimpered, 'Careful... Careful...!' over and over again."
    MC "Ahh! Did Lord Tarbeck ever imagine you'd take it back here?"
    LADY_TARBECK "{i}*Huff*{/i} H-He asked... {i}*Huff*{/i} Many times."
    LADY_TARBECK "I always said I'd never do something so d-degrading!"
    "I smirked at her answer, slamming my cock faster into her ass."
    $ PlaySexFx(audio.kiara_tent_normal, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_missionary_preg_anal_2
    else:
        scene lady_tarbeck_romance_missionary_nopreg_anal_2
    with dissolve
    $ Pause()
    LADY_TARBECK "F-Fuck! FUCK!"
    LADY_TARBECK "Gods you're BIG! Ahh!"
    MC "Hold on—Ahh! My lady!"
    MC "I'm not done with your ass yet!"
    "Lady Tarbeck held on for dear life as I stretched out her rear."
    "Slamming my cock into her tight ass as she moaned."
    "Straddling the line between pain and pleasure."
    LADY_TARBECK "M-My ass..."
    LADY_TARBECK "Y-You're going to - {i}*Huff*{/i}"
    LADY_TARBECK "MAKE ME CUM FROM MY ASS!"
    "No sooner had the lewd words escaped her lips than I felt Lady Tarbeck tremble as her heart raced."
    MC "Hrghh... I'm close... Your ass... It's-"
    LADY_TARBECK "P-Please! Hurry up and - Ahh! F-Finish!"
    LADY_TARBECK "Before I b-b..."
    LADY_TARBECK "BREAKKK!"
    if CharIsVisiblyPreg("lady_tarbeck"):
        $ UnlockGalFlag("lady_tarbeck", "quarters_missionary", "var_rep_preg_anal")
    else:
        $ UnlockGalFlag("lady_tarbeck", "quarters_missionary", "var_rep_nopreg_anal")
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "quarters_missionary")
    $ ReduceInfectionFromSex("lady_tarbeck")
    $ PlaySexFx(audio.kiara_tent_finish)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_missionary_preg_anal_cum
    else:
        scene lady_tarbeck_romance_missionary_nopreg_anal_cum
    with flash
    $ Pause()
    "Lady Tarbeck shuddered as I buried my cock to the hilt in her tight, cute ass."
    "As she trembled, overcome with pleasure, I grunted and flooded her welcoming, tight hole with my seed."
    LADY_TARBECK "{i}*Gasp!*{/i}"
    MC "Gods... {i}*Huff*{/i} My lady..."
    MC "Has anyone ever told you that you might have the tightest ass in all of Hamun?"
    scene black with dissolve
    $ AutoMus(True)
    $ StopReplay()
    "A blushing Lady Tarbeck dropped her head back onto the bed, covering her rosy cheeks as she laughed softly."
    LADY_TARBECK "I don't know what's more impressive... The fact I managed to take your thing... {i}there.{/i}"
    LADY_TARBECK "Or that somehow this is only going to make my husband happier knowing I did."
    LADY_TARBECK "J-Just a few minutes and I'll... {i}*Huff*{/i} I'll get up..."
    $ CharSetClothes("lady_tarbeck", "normal")
    $ LocSet("hamun_dist_merch_lord")
    $ Pause(0.1)
    $ LocEnter()

    

##############################################################################
label rom_tarbeck_romance_nightvisit:
    $ RomanceLadyTarbeck().Romance_NextPossibleDragonVisitDay = GetGameDay() + 1
    $ PlaySound(audio.door_knock)
    "Rising from my bed, I headed over to open the door."
    $ CharSetClothes("mc", "pants")
    $ LocFlush()
    with dissolve
    show mc at cright_f with easeinright
    show lady_tarbeck at cleft with easeinleft
    MC @surprised "Lady Tarbeck! Why are you here?"
    LADY_TARBECK @smile "I woke up this morning and thought to myself..."
    LADY_TARBECK @blush2 "Wouldn't it be nice to ride your huge, fat cock?"
    MC @smile "Lady Tarbeck, I-"
    "Before I could say another word, Lady Tarbeck shoved me back down onto the bed."
    LADY_TARBECK @blush2 "Sorry, lover. I haven't come here to talk."
    "Stripping herself down, Lady Tarbeck threw herself at me, giggling."
    "Straddling me, she wasted no time slipping my cock into her already wet womanhood."
    label replay_tarbeck_romance_cowgirl:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx(audio.kiara_tent_normal, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_cowgirl_preg_1
    else:
        scene lady_tarbeck_romance_cowgirl_nopreg_1
    with dissolve
    $ Pause()
    "As her tight pussy squeezed around my cock, Lady Tarbeck slowly began to bounce, the bed creaking with each motion."
    LADY_TARBECK "Oh gods... Mhmm!"
    LADY_TARBECK "I've missed this so much!"
    MC "Ahh! Well, this is one hell of a morning call!"
    LADY_TARBECK "Oooh! This is—Ahh! All your fault!"
    LADY_TARBECK "I was a good little, Mmm! Loving wife till you came along!"
    "Lady Tarbeck's tits bounced as she ground herself on top of me, pushing her cute ass down onto my cock as she moaned happily."
    MC "Tsk, tsk, tsk!"
    MC "Anyone would think your husband actually disapproved if they heard you now!"
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_cowgirl_preg_2
    else:
        scene lady_tarbeck_romance_cowgirl_nopreg_2
    with dissolve
    $ Pause()
    "Lady Tarbeck began to move faster, her moans becoming louder as the bed frame slammed against the wall."
    "*THUD* *THUD* *THUD*"
    LADY_TARBECK "Ooooh! You f-fill me up so good!"
    LADY_TARBECK "I love you!"
    LADY_TARBECK "I LOVE YOU, I LOVE YOU, I LOVE YOU!"
    MC "AHH! You certainly love something, alright!"
    "She pushed her ass down hard onto me, desperate to take me as deeply into herself as she could."
    LADY_TARBECK "F-Fuck...!"
    LADY_TARBECK "I'm close! I'm so close!"
    "Lady Tarbeck rode me like a woman possessed, squeezing and flexing her tight hole around my cock as she seemed determined to finish me off."
    MC "Hrghh! Lady Tarbeck! I-"
    LADY_TARBECK "C-Cum! Cum in me, you big-"
    LADY_TARBECK "BIG!"
    "Suddenly, Lady Tarbeck's whole body began to shudder as she ground furiously against me."
    "Her mouth hung agape as a lewd cry escaped her lips while she tightened and squeezed around me."
    LADY_TARBECK "BASTARDDDDDD!"
    "As she pushed her ass down onto me and held it there, I grunted, pulling down on her waist as I found myself unable to hold on any longer."
    "Emptying my heavy balls into the wanton wife."
    MC "HRGHHH...!"
    MC "Gods! Take it all then, you slutty little wife!"

    if CharIsVisiblyPreg("lady_tarbeck"):
        $ UnlockGalFlag("lady_tarbeck", "tavern_cowgirl", "var_rep_preg")
    else:
        $ UnlockGalFlag("lady_tarbeck", "tavern_cowgirl", "var_rep_nopreg")
    $ PregRoll("lady_tarbeck")
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "tavern_cowgirl")
    $ ReduceInfectionFromSex("lady_tarbeck")
    $ PlaySexFx(audio.kiara_tent_finish)

    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_romance_cowgirl_preg_cum
    else:
        scene lady_tarbeck_romance_cowgirl_nopreg_cum
    with flash
    $ Pause()

    "Lady Tarbeck's eyes rolled back as she felt the splash in her womb, letting out another breathless whimper as she squeezed me for every drop."
    "Finally satisfied, she dropped forward onto my chest for a moment, showering me with kisses before rising shakily back to her feet."
    LADY_TARBECK @smile "Enjoy the rest of your day..."
    "She playfully blew me a kiss before leaving."
    scene black with dissolve
    $ StopReplay()
    $ CharSetClothes("mc", "normal")
    $ AutoMus(True)
    $ Pause(0.25)
    $ LocEnter()
