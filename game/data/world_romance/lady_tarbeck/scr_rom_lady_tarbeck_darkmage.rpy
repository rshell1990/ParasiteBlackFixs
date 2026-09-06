init python:
    notesLib["tarbeck_rom_darkmage_meettomorrow"] = Note(
        _("Meet Lady Tarbeck tomorrow"),
        _("Lady Tarbeck has asked to meet me at the Manor, tomorrow."),
    )
    notesLib["tarbeck_rom_darkmage_talktozanzibataboutgrimoire"] = Note(
        _("Talk to Lord Zanzibat about the grimoire"),
        _("Lord Zanzibat might be able to help procure a griomoire on dark mages for Lady Tarbeck."), 
    )
    notesLib["tarbeck_rom_darkmage_wait_for_zanzibat"] = Note(
        _("Return to Lord Zanzibat in a day or so"),
        _("I should wait a day and then see if Lord Zanzibat has found that grimoire..."),
    )
    notesLib["tarbeck_rom_darkmage_bring_book"] = Note(
        _("Return to Lady Tarbeck"),
        _("I should bring this grimoire back to Lady Tarbeck..."),
    )
    notesLib["tarbeck_rom_darkmage_return_after_book"] = Note(
        _("Return to Lady Tarbeck in a day or two"),
        _("I should check in on Lady Tarbeck in a day or two..."),
    )
    notesLib["tarbeck_rom_darkmage_return_after_dark"] = Note(
        _("Return to Lady Tarbeck after dark"),
        _("That dark mage will be arriving this evening... I should head back to the Tarbeck manor after dark."),
    )
    notesLib["tarbeck_rom_darkmage_return_next_morning"] = Note(
        _("Return to Lady Tarbeck in the morning"),
        _("Lady Tarbeck has asked me to come see her again in the morning... I wonder what she has planned?"),
    )
    notesLib["tarbeck_rom_darkmage_return_next_night"] = Note(
        _("Return to Lady Tarbeck tomorrow night"),
        _("Lady Tarbeck has asked me to escort her to a brothel this evening from the Tarbeck manor... What is she planning?"),
    )
    notesLib["tarbeck_rom_darkmage_return_after_brothel"] = Note(
        _("Return to Lady Tarbeck tomorrow evening"),
        _("Lady Tarbeck has asked me to join her at the manor this evening while Lord Tarbeck is meant to be away."),
    )
    notesLib["tarbeck_rom_darkmage_meet_at_lords"] = Note(
        _("Meet Lady Tarbeck at Lord Tarbeck's quarters"),
        _("Lady Tarbeck has asked me to meet her in Lord Tarbeck's chambers this morning... I wonder what this is about?"),
    )
    notesLib["tarbeck_rom_darkmage_meet_at_brothel_rep"] = Note(
        _("Meet Lady Tarbeck at the brothel"),
        _("I have agreed to meet up with Lady Tarbeck at the brothel tonight."),
    )

# at day
# the morning after the player locks into the Dark Mage route.
# auto-trigger when the player enters the Tarbeck manor.
label rom_tarbeck_darkmage_meet_manor:
    $ QstSetProgress(RomanceLadyTarbeck, 2)
    $ NoteLock("tarbeck_rom_darkmage_meettomorrow")
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @talk "... We need to talk."
    MC @think "Have you thought on what I said?"
    LADY_TARBECK @sad "I... Yes."
    LADY_TARBECK @sad "I want to understand... I want to know this part of myself."
    LADY_TARBECK @think "But where would I even begin with this?"
    LADY_TARBECK @sad "I don't know any dark mages!"
    MC @think "This is Hamun, surely-"
    LADY_TARBECK @talk "They don't exactly advertise themselves..."
    "Lady Tarbeck paused."
    MC @talk "Why not just ask your husband to help you find-"
    LADY_TARBECK @talk "Absolutely not. Even if he understood, he wouldn't allow me anywhere near dark mages."
    LADY_TARBECK @think "But... Perhaps."
    LADY_TARBECK @talk "Maybe...?"
    MC @think "What is it?"
    LADY_TARBECK @talk "What if... We didn't find a dark mage?"
    LADY_TARBECK @talk "What if one found me?"
    MC @think "I don't understand."
    LADY_TARBECK @talk "A dark mage's grimoire... If I could procure one, perhaps... I could use it to lure a dark mage to me?"
    MC @think "And how do you plan to do that?"
    LADY_TARBECK @talk "{i}... I claim to have in my possession a dark mage's grimoire and let it be known I'm looking to sell it.{/i}"
    MC @talk "The inquisition will-"
    LADY_TARBECK @talk "They do not have official jurisdiction in Hamun."
    LADY_TARBECK @talk "They could stomp their feet all they want."
    MC @serious "Lord Tarbeck is bound to hear-"
    LADY_TARBECK @talk "Leave that to me. I'll make sure only the {i}right{/i} people hear..."
    MC @serious "My lady... Dark mages aren't something to be toyed with. One could come here and just try to kill you for the book!"
    LADY_TARBECK @smile "That's why I have you."
    LADY_TARBECK @smile "To help keep me safe."
    MC @sad "Lady Tarbeck..."
    LADY_TARBECK @talk "Would you do it for me? Would you find a grimoire?"
    MC @serious "I don't exactly-"
    LADY_TARBECK @sad "Please... I need your help."
    MC @sad "{i}*Sigh*{/i} Fine, I shall look for one... But no promises."
    LADY_TARBECK @smile "Thank you, [player_name], you won't regret this."
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    with dissolve
    show mc at cright_f with easeinright
    MC "(Where in the world am I going to find a dark mage's grimoire?)"
    MC "(... Perhaps, Lord Zanzibat could help?)"
    $ NoteUnlock("tarbeck_rom_darkmage_talktozanzibataboutgrimoire")
    $ LocEnter()

###################################################################
# SCENE 2 - LORD ZANZIBAT DIALOGUE
# IMPLEMENTATION NOTES :

# - If the player cannot or does not pay, exit the conversation 
# and retain: 
label rom_tarbeck_darkmage_zanzibat_grimoire_first:
    ZANZIBAT @think "Oh... This will be interesting."
    ZANZIBAT @talk "What is it?"
    MC @talk "Could you procure a dark mage's grimoire for me?"
    "Lord Zanzibat stared at me for the longest time."
    ZANZIBAT @laugh "Hahahahahaha!"
    ZANZIBAT @talk "What possible reason could you have for one of those things?"
    ZANZIBAT @think "... Is this some kind of attempt to enhance your existing powers?"
    ZANZIBAT @serious "I would strongly advise steering clear of anything to do with dark mages."
    MC @talk "No, it's not for me."
    ZANZIBAT @think "Then why?"
    MC @talk "Can you procure it, or not?"
    "Lord Zanzibat paused, his eyes curiously looking me up and down."
    ZANZIBAT @talk "... I could ask."
    ZANZIBAT @talk "But the cost would be high."
    ZANZIBAT @talk "Two thousand coins."
    menu:
        "Deal.":
            ZANZIBAT @talk "Good."
        "Fifteen hundred..." (Req_Barter = 12):
            $ RomanceLadyTarbeck().Darkmage_ZanzibatFee = 1500
            ZANZIBAT @talk "Hmm, very well."
    MC @think "I suppose I can trust you to be discreet about this?"
    ZANZIBAT @smile "I'm almost offended..."
    ZANZIBAT @talk "I haven't made it this far by learning how not to keep a secret."
    "A slight smile appeared on his lips."
    ZANZIBAT @smile "Just beware whoever you give this book to. It will be unlikely to stay a secret for long..."
    ZANZIBAT @smile "These things tend to get out rather quickly."
    $ RomanceLadyTarbeck().Darkmage_TalkedToZanzibatBoutBookOnce = True
    label rom_tarbeck_darkmage_zanzibat_grimoire_repeat:
    ZANZIBAT @talk "Now then, do you have the coin?"
    menu:
        "Here." (Req_Gold = RomanceLadyTarbeck().Darkmage_ZanzibatFee):
            $ NoteLock("tarbeck_rom_darkmage_talktozanzibataboutgrimoire")
            $ PlayerRemItem("gold", RomanceLadyTarbeck().Darkmage_ZanzibatFee)
            ZANZIBAT @smile "Excellent."
            ZANZIBAT @talk "Return in a day or so. I will see what I can find."
            $ QstSetProgress(RomanceLadyTarbeck, 3)
            $ QstSetDelay(RomanceLadyTarbeck, 1)
            $ NoteUnlock("tarbeck_rom_darkmage_wait_for_zanzibat")
        "Not yet.":
            ZANZIBAT @talk "Then return when you do."
    $ LocEnter()

#############################################
# SCENE 3 - ZANZIBAT ESTATE
# IMPLEMENTATION NOTES :
# - Trigger: auto-trigger when the player enters Zanzibat's estate.
# - Outcome: add the Dark Mage Grimoire as a key item and direct the player back to Lady Tarbeck.
label rom_tarbeck_darkmage_zanzibat_pickup_grimoire:
    $ NoteLock("tarbeck_rom_darkmage_wait_for_zanzibat")
    show zanzibat at center
    with dissolve
    ZANZIBAT @smile "Ahh... I was wondering when I might see you."
    "Lord Zanzibat handed over a cloth-covered book."
    $ PlayerAddItem("qst_darkmage_grimoire")
    ZANZIBAT @talk "Be careful with it..."
    ZANZIBAT @talk "These books are often more trouble than they are worth."
    MC @talk "Thank you."
    $ NoteUnlock("tarbeck_rom_darkmage_bring_book")
    $ QstSetProgress(RomanceLadyTarbeck, 4)
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush(dissolve)
    show mc at cleft with easeinleft
    MC "(Now I just need to give this back to Lady Tarbeck and pray this plan of hers actually works.)"
    $ LocEnter()

#######################
# SCENE 4 - TARBECK MANOR, MAIN HALL
# IMPLEMENTATION NOTES :
# - Journal: 
# - Trigger: auto-trigger when the player enters the Tarbeck manor while carrying the Dark Mage Grimoire.
# - Outcome: permanently remove the grimoire from inventory, 
# update the journal, and begin the wait for Scene 5 
# (available 2 days in-game later).
label rom_tarbeck_darkmage_bring_grimoire:
    $ NoteLock("tarbeck_rom_darkmage_bring_book")
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @shock "Do you have it?!"
    MC @think "How did you-"
    LADY_TARBECK @talk "Our spies told us that you visited Lord Zanzibat and that he has been inquiring about an... {i}unusual{/i} artefact recently."
    LADY_TARBECK @smile "Doesn't take a genius to figure out what happened."
    MC @talk "Yes, I have it."
    LADY_TARBECK @smile "YES!"
    "She clapped her hands together cheerfully."
    LADY_TARBECK @smile "Show me."
    show mc at nod
    $ PlayerRemItem("qst_darkmage_grimoire")
    "I handed over the book, shielded only by a brown rag. Lady Tarbeck traced her fingers over the cover and shuddered."
    LADY_TARBECK @shock "I... I can {i}feel{/i} something resonate from it."
    LADY_TARBECK @think "It's... So strange!"
    "Lady Tarbeck took the book carefully from my hands."
    MC @think "What now?"
    LADY_TARBECK @smile "Now... I lay the bait."
    LADY_TARBECK @talk "Give me a day or two."
    LADY_TARBECK @talk "Let's see if one of them really does take the bait..."
    scene black with dissolve
    $ QstSetProgress(RomanceLadyTarbeck, 5)
    $ QstSetDelay(RomanceLadyTarbeck, 2)
    $ NoteUnlock("tarbeck_rom_darkmage_return_after_book")
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()

#######################
# SCENE 5 - TARBECK MANOR, MORNING
# IMPLEMENTATION NOTES :
# - Availability: morning, at least two full days after Scene 4.
# - Trigger: auto-trigger when the player enters the Tarbeck manor.
label rom_tarbeck_darkmage_return_after_grimoire:
    $ NoteLock("tarbeck_rom_darkmage_return_after_book")
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @happy "I... I think we have something!"
    LADY_TARBECK @think "A buyer... Someone's coming here tonight to purchase the grimoire!"
    MC @serious "Then I should be with you tonight."
    MC @serious "I'm not letting you put yourself at risk like this without some kind of security."
    "Lady Tarbeck's cheeks flushed red as her heart fluttered."
    LADY_TARBECK @blush "Y-Yes... That sounds like a good idea."
    LADY_TARBECK @blush "C-Come back here tonight, after dark."
    $ NoteUnlock("tarbeck_rom_darkmage_return_after_dark")
    LADY_TARBECK @talk "I'll be waiting..."
    scene black with dissolve
    $ QstSetProgress(RomanceLadyTarbeck, 6)
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()


#########################
# SCENE 6 - TARBECK MANOR, MAIN HALL, NIGHT
# IMPLEMENTATION NOTES :
# - Journal: ""
# - Trigger: auto-trigger when the player enters the Tarbeck manor after dark.
# - The narrated training montage does not advance gameplay time.
# - After cg_lady_tarbeck_dark_mage_studies, 
# permanently switch Lady Tarbeck to her Dark Mage sprite 
# and portrait on this route.
# - Outcome: play the first thighjob scene, 
# then update the journal for Scene 7 the following morning.
label rom_tarbeck_darkmage_meetmage:
    $ NoteLock("tarbeck_rom_darkmage_return_after_dark")
    show cg_lazarian at center
    show lady_tarbeck at cright_f
    with dissolve
    show mc at left with easeinleft
    "No sooner had I entered the hall than I saw Lady Tarbeck speaking with a mysterious robed man."
    "He tilted his head towards me, then began taking a few anxious steps back."
    LAZARIAN "T-There must be some mistake! Haha!"
    LAZARIAN "I am just a humble, uhh, collector!"
    LADY_TARBECK @shock "Wait, please!"
    show cg_lazarian at blurin, center_f
    "The man tried to flee, but before he could, I stepped in front of him, holding out my hand to stop him."
    MC @serious "Stop."
    show cg_lazarian at shake
    LAZARIAN "I... I REALLY MUST GET GOING!"
    LADY_TARBECK "MY PARENTS WERE DARK MAGES!"
    show cg_lazarian at blurin, center
    "The man stopped in his tracks, slowly turning towards Lady Tarbeck."
    LAZARIAN "... What did you say?"
    LADY_TARBECK @sad "My parents were dark mages..."
    LADY_TARBECK @sad "Please, this isn't a trap."
    LADY_TARBECK @sad "I need someone to... to..."
    LADY_TARBECK @shock "To teach me!"
    "All at once, the man's entire body language changed, his voice becoming firmer."
    LAZARIAN "... You don't know what you're asking for."
    LADY_TARBECK @shock "I do! I have magecraft that I can't control! I-"
    LAZARIAN "This isn't a game."
    LAZARIAN "Do you even understand the risks of what you're asking?"
    LAZARIAN "The number of dark mages who go mad?"
    LAZARIAN "... You'll be hunted, despised, misunderstood..."
    LAZARIAN "{i}And one day you'll prove every bad thing they say about you right.{/i}"
    LAZARIAN "This isn't a life... Not really."
    LADY_TARBECK @angry "I am who I am! I'm not running away anymore!"
    LADY_TARBECK @angry "E-Either you'll help me, or I'll find another dark mage who will!"
    LAZARIAN "Are you fucking mad?"
    LAZARIAN "It's a miracle I arrived instead of-"
    "The man sighed, rubbing his brow."
    LAZARIAN "... Fine, let's say I did teach you."
    LAZARIAN "What's in it for me?"
    LADY_TARBECK @think "C-Coin? I was thinking-"
    LAZARIAN "Not enough."
    LADY_TARBECK @think "What?"
    LAZARIAN "Eighty thousand coins... And a ship to the Dead Lands with a home waiting for me across the Black Ocean."
    LADY_TARBECK @shock "That is..."
    LAZARIAN "My price."
    LAZARIAN "If you don't like it, good luck finding a non-crazy dark mage who won't try to teach you the joys of living turned inside out."
    MC @serious "And how do we know you aren't just a crazy psychopath pretending he's alright until I turn my back?"
    LAZARIAN "Well, you're both just going to have to have a little faith, aren't you?"
    LADY_TARBECK @think "The Dead Lands... But it's... so dangerous there."
    LAZARIAN "At least I'll be free."
    LAZARIAN "... So, do we have a deal, or not?"
    MC @serious "Lady Tarbeck, you should think before-"
    LADY_TARBECK @talk "Deal."
    LAZARIAN "{i}*Sigh*{/i}"
    LAZARIAN "Fine, I'll come by tomorrow and begin teaching you."
    LAZARIAN "This would normally take years, but... I suppose a crash course over a few months should at least leave you able to figure out the rest yourself."
    MC @serious "If you try-"
    LAZARIAN "Relax, lover boy."
    LAZARIAN "I can smell the two of you plan to fuck from here."
    "Lady Tarbeck's cheeks burned red."
    LADY_TARBECK @blush "W-Wha...?"
    LAZARIAN "I only fuck the undead."
    MC "..."
    LADY_TARBECK @shock "... I-"
    LAZARIAN "... What? Did you think the dating pool was wide for a dark mage or something?"
    LAZARIAN "Besides, nothing beats a ghoul cheated on by her husband two centuries ago who's still after a little petty revenge."
    MC @talk "Didn't need to know that."
    LADY_TARBECK @think "When does the first lesson begin?"
    LAZARIAN "{i}Now.{/i}"
    scene black with dissolve
    #Brief fade to black
    scene cg_lady_tarbeck_dark_mage_studies with dissolve
    "... Until what felt like sunrise, Lazarian gave Lady Tarbeck a crash course."
    "Over the course of the next few days, Lady Tarbeck spent her time aggressively reading and practising circles and other strange incantations."
    "Lazarian, for all his strange quirks... was a remarkable teacher, and he seemed equally impressed by Lady Tarbeck's insistence and questioning."
    "At some point, Lady Tarbeck appeared before me... {i}differently.{/i}"
    scene black with dissolve
    $ CharSetVar("lady_tarbeck", "variant", "darkmage")
    $ CharSetPortrait("lady_tarbeck", "images/characters/lady_tarbeck/darkmage/portrait.webp")
    #Cut to Lady Tarbeck Dark Mage sprite from here on out.
    $ Pause(0.25)
    $ LocFlush()
    show mc at cleft
    show lady_tarbeck at cright_f
    with Dissolve(1.0)
    $ Pause()
    LADY_TARBECK @smile "Well... What do you think?"
    MC @shock "You look..."
    MC @shock "{i}Different.{/i}"
    LADY_TARBECK @smile "It's strange... I can feel the energy coursing through my body more clearly now."
    LADY_TARBECK @smile "It's like it's... changed me."
    LAZARIAN "That's because it has... Now you're no longer suppressing it."
    show cg_lazarian at right_f with easeinright
    show lady_tarbeck at blurin, center with ease
    #Enter Lazarian
    LAZARIAN "But now I think it's time {i}you{/i} took the next step."
    LADY_TARBECK @think "Which is?"
    LAZARIAN "After doing some research, I am convinced the god you draw your magecraft from is Marvessa... An old god of indulgence."
    LADY_TARBECK @shock "Indulgence... Me?"
    LAZARIAN "Likely, your pious life has been the reason you've managed to suppress the power more easily."
    LAZARIAN "But now, if you want to unlock your powers fully... You need to indulge."
    LADY_TARBECK @think "In what?"
    LAZARIAN "{i}Whatever your heart truly desires.{/i}"
    "Lady Tarbeck paused for a moment, her eyes lighting with a strange sparkle as she turned towards me, saying nothing."
    LAZARIAN "We can continue your training once you're done..."
    MC @think "What are you going to do in the meantime?"
    LAZARIAN "Read... Swim in the waters, whatever I please."
    LAZARIAN "{i}*Sigh*{/i} You people really are missing out on an undead brothel..."
    hide cg_lazarian with easeoutleft
    "Without another word, the dark mage slipped past, wandering off and leaving Lady Tarbeck and me alone."
    #show lady_tarbeck at blurin, center
    "Lady Tarbeck stepped closer to me."
    LADY_TARBECK @smile "So... I must indulge in my desires."
    "She laughed softly."
    LADY_TARBECK @smile "And I suppose if I said..."
    LADY_TARBECK @blush "{i}You...{/i} were my desire..."
    LADY_TARBECK @blush2 "You wouldn't have any qualms?"
    MC @smile "None at all."
    "Lady Tarbeck bit down on her lower lip."
    LADY_TARBECK @blush "W-Would you mind if I used my magecraft?"
    LADY_TARBECK @blush "I want... to try a few things."
    MC @think "Just be careful and don't-"
    "I barely had time to finish the sentence when an excited Lady Tarbeck waved her hand, her eyes glowing a faint purple."
    "I suddenly found myself restrained within a circle of enchantment as Lady Tarbeck began stripping away my clothes."
    MC "Lady Tarbeck!"
    LADY_TARBECK "Well, before I let you fuck me, I think it's only fair we do a little... umm..."
    LADY_TARBECK "{i}Foreplay?{/i}"
    label replay_tarbeck_darkmage_thighjob:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    scene lady_tarbeck_darkmage_thighjob_idle
    with dissolve
    $ Pause()
    if IsFirstTime():
        "Lady Tarbeck stripped off some of her clothes and tugged down her panties as she lay on top of me, wedging my cock between her thighs."
        MC "Ahh... What do you think you're-"
        LADY_TARBECK "{i}Indulging.{/i}"
        LADY_TARBECK "I want to savour every moment with this cock."
        LADY_TARBECK "If this is the path I have to walk..."
        LADY_TARBECK "{i}I want you dying to fuck me.{/i}"
        LADY_TARBECK "{i}Dying.{/i}"
        LADY_TARBECK "{i}To.{/i}"
        LADY_TARBECK "{i}Fuck.{/i}"
        LADY_TARBECK "{i}Me.{/i}"
    #Repeat time
    else:
        "Lady Tarbeck giggled as she once again wrestled my cock between her thighs."
        "She pushed the member against her glistening womanhood."
        LADY_TARBECK "You know, I really do appreciate the feel of your cock there."
        LADY_TARBECK "My fat ass... Your huge cock..."
        LADY_TARBECK "They both look so good together, don't they?"
    $ PlaySexFx(audio.adara_hj_loop, 1)
    scene lady_tarbeck_darkmage_thighjob_1
    with dissolve
    $ Pause()
    if IsFirstTime():
    #First time continued
        "Lady Tarbeck began to move, sliding her ass back and forth as she squeezed my cock between her thighs."
        LADY_TARBECK "{i}*Huff*{/i} I still can't believe I'm doing this..."
        LADY_TARBECK "G-Gods, all this freedom is so... {i}intoxicating.{/i}"
        "She squeezed tightly around my cock."
        MC "Hrghh... You know when the time comes for this, I'll-"
        LADY_TARBECK "Fufu... That's what I'm counting on."
        LADY_TARBECK "But till then..."
    #Repeat time continued
    else:
        "Once more, Lady Tarbeck ground her ass against my cock as she began to move rhythmically back and forth."
        "With my cock squeezed between her thighs and nestled beneath her already wet pussy, she moaned happily."
        LADY_TARBECK "I'm surprised you—Ahh...!"
        LADY_TARBECK "Asked for this again."
        LADY_TARBECK "Here I was thinking you'd just be bending me over all around the manor, fufu."
        MC "Don't get ahead of yourself."
        MC "Your ass is still mine, even if I let you indulge every now and then."
        LADY_TARBECK "{i}I wouldn't have it any other way... darling.{/i}"
    $ PlaySexFx(audio.adara_hj_loop_x2, 1)
    scene lady_tarbeck_darkmage_thighjob_2
    with dissolve
    $ Pause()
    #First time
    if IsFirstTime():
        "She began to move faster, squeezing my cock tighter between her thighs."
        "With every movement, as my cock brushed up against her, I felt like it might slip inside by accident at any moment."
        "With every close brush, Lady Tarbeck let out another moan."
        LADY_TARBECK "S-Soon... {i}*Huff*{/i}"
        LADY_TARBECK "Soon you'll be—Ahh!"
        LADY_TARBECK "I-Inside of me..."
        LADY_TARBECK "Another man..."
        LADY_TARBECK "N-Not my husband..."
        "The more she spoke, the more aroused she became."
        MC "Lady Tarbeck, if you keep going like that, I'll—Ahh...!"
        LADY_TARBECK "A-Are you close?"
        LADY_TARBECK "Cum..."
        LADY_TARBECK "{i}Cum for me.{/i}"
    #Repeat time
    else:
        "Lady Tarbeck squeezed her thighs tighter as she began to move faster."
        "Her teasing, wet pussy slid against my cock, making me shudder with delight as she let out trembling, hot breaths."
        LADY_TARBECK "You're so fucking close... I can feel it."
        LADY_TARBECK "C-Cum for me."
        LADY_TARBECK "Cover my fat ass in cum and finish already!"
        LADY_TARBECK "Do it!"
        MC "Lady Tarbeck! I-"
        $ UnlockGalFlag("lady_tarbeck", "thighjob", "var_rep")
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "thighjob")
    $ ReduceInfectionFromSex("lady_tarbeck")
    $ PlaySexFx(audio.adara_hj_finish)
    scene lady_tarbeck_darkmage_thighjob_cum
    with flash
    $ Pause()
    # First time
    if IsFirstTime():
        MC "HRGHHH...!"
        "No sooner had she finished speaking than I painted Lady Tarbeck's ass with a coat of white."
        "As she felt the splash against her, she gasped, and then her lips curled into a smile."
        LADY_TARBECK "Oh my..."
        LADY_TARBECK "That was a lot."
        MC "A lot that should be sloshing about in your womb right about now."
        LADY_TARBECK "In time... All in time..."
    # Repeat time
    else:
        MC "C-CUMMINGGG!"
        "Lady Tarbeck laughed as she felt the splash of hot seed coat her ass."
        LADY_TARBECK "You know... I'm starting to get used to being covered in your seed."
        LADY_TARBECK "Perhaps I should have you cum in a container and make those spiteful bitches wear your seed as well, hmm?"
        MC "Devious little minx..."
    $ StopReplay()
    # Post-sex scene
    scene black with dissolve
    if not IsFirstTime():
        $ SetRepeatVariant(False)
        $ AutoMus(True)
        $ LocEnter()
    $ LocFlush()
    show mc at cleft
    show lady_tarbeck at cright_f
    with dissolve
    "Lady Tarbeck released me from the circle with a snap of her fingers."
    LADY_TARBECK @smile "Lord Tarbeck will be home soon..."
    $ AutoMus(True)
    "Playfully, Lady Tarbeck twirled a few strands of her hair around her finger."
    LADY_TARBECK @smile "Why don't you stop by tomorrow?"
    LADY_TARBECK @blush "I'll be sure to make it worth your time..."
    $ CharSetLover("lady_tarbeck")
    scene black with dissolve
    $ QstSetProgress(RomanceLadyTarbeck, 7)
    $ NoteUnlock("tarbeck_rom_darkmage_return_next_morning")
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()

########################################################################################################
# SCENE 7 - TARBECK MANOR, MORNING
# IMPLEMENTATION NOTES :
# - Availability: the morning after Scene 6.
# - Trigger: auto-trigger when the player enters the Tarbeck manor.
label rom_tarbeck_darkmage_returnaftermage:
    $ NoteLock("tarbeck_rom_darkmage_return_next_morning")
    show mc at cleft with easeinleft
    MC @talk "Lady Tarbeck? Are you here?"
    show lord_tarbeck at cright_f with easeinright
    TARBECK "My wife is... indisposed."
    show mc at nod
    MC @talk "Lord Tarbeck."
    TARBECK @talk "She's currently bathing and preparing herself for your... {i}date.{/i}"
    "There was an awkward silence between us for a moment."
    TARBECK @smile "Relax... I haven't suddenly changed my mind."
    TARBECK @talk "Though her behaviour recently has been... {i}odd.{/i}"
    TARBECK @talk "Even for her."
    MC "(Let's hope you don't stumble upon some magecraft incantations...)"
    MC @talk "I'm sure she's just getting used to the idea."
    TARBECK @think "Perhaps, but I think... She might be a little upset with me."
    MC @think "How so?"
    TARBECK @talk "She happened to catch me the other night with, uhh... Two ladies."
    TARBECK @talk "One of whom already bore me a son, haha!"
    "He let the laughter awkwardly peter out."
    TARBECK @sad "I think... Perhaps she wanted to talk about something serious, but her expression changed all at once after she saw me."
    TARBECK @talk "Come join me for some breakfast at the dining table. I insist."
    TARBECK @talk "Lady Tarbeck will be down shortly."
    show lord_tarbeck at blurin, cright
    hide lord_tarbeck with easeoutright
    show mc at center with ease
    $ Pause(0.25)
    hide mc with easeoutright
    "Not exactly able to refuse, I smiled and awkwardly joined Lord Tarbeck at the dining table."
    scene black with dissolve
    $ Pause(0.25)
    $ LocSet("hamun_tarbeck_dining")
    label replay_tarbeck_darkmage_tablebj:
    scene lady_tarbeck_darkmage_tablebj_idle
    with dissolve
    $ Pause()
    if IsFirstTime():
        TARBECK "... I just don't understand it."
        TARBECK "Has she mentioned it or anything strange recently?"
        MC "No, not that I can think of."
    else:
        TARBECK "It's good you wanted to catch up with me on things."
        TARBECK "Lady Tarbeck seems... very different these days."
        TARBECK "I still don't know how or why she grew her hair out so long, so fast."
        TARBECK "But I have to admit, she seems happier..."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    scene lady_tarbeck_darkmage_tablebj_1
    with dissolve
    $ Pause()
    if IsFirstTime():
        "Looking beneath the table, I saw a small circular portal appear."
        "My eyes widened as Lady Tarbeck's head popped through it, and she motioned for me to be quiet as she carefully pulled out my cock."
        TARBECK "[player_name]?"
        TARBECK "Is something the matter?"
        MC "Uhh, n-no, Lord Tarbeck."
        "Smiling and licking her lips, Lady Tarbeck smacked the cock lightly against her cheek, kissing the head."
        TARBECK "Well then, what are your thoughts on what I said?"
    else:
        "Down beneath the table, another circular portal appeared as Lady Tarbeck's head popped through."
        "She licked her lips expectantly, watching as I carefully pulled out my cock."
        "Slapping the meat against her cheek, she carefully kissed the head, running her tongue gently down the shaft to kiss the balls."
        TARBECK "So... What are the two of you getting up to? Lady Tarbeck has teasingly remained tight-lipped about your little 'adventures.'"
    $ PlaySexFx(audio.kiara_bj_loop, 1)
    scene lady_tarbeck_darkmage_tablebj_2
    with dissolve
    $ Pause()
    if IsFirstTime():
        "Wrapping her lips around my cock, I nearly banged my knees on the table there and then as the lewd little wife got to work."
        MC "F-FUCK!"
        TARBECK "... Pardon?"
        MC "I mean, uhh... She's, uhh, going through a lot of changes."
        MC "I'm sure she will—Mmm... T-Talk to you when she's ready."
        "Lady Tarbeck did her best to suppress a laugh as she twisted and churned her tongue over the head of my cock."
        MC "(Gods, this woman!)"
        TARBECK "Hmm... So you don't think I have anything to worry about?"
        MC "N-No, my lord."
        MC "I don't think-"
    else:
        #repeat time continued
        "All at once, Lady Tarbeck opened her mouth and swallowed a few inches of my cock."
        "Thrashing it about in her mouth like a sweet, her tongue playfully twisted and licked around the shaft."
        MC "A-AHHH!"
        TARBECK "... Is everything alright?"
        MC "Y-Yes, uh... Spasm in my leg."
        "Lady Tarbeck did her best to suppress a laugh as she sucked on my cock."
        TARBECK "So then... What are you two getting up to?"
        MC "We... Uh..."
        "I felt Lady Tarbeck's teeth lightly press against my member."
        MC "(Ow!)"
        MC "I think she might kill me if she discovered you found out."
        "The edges of Lady Tarbeck's mouth, despite being stuffed with my cock, curved into an approving smile."
        TARBECK "Ahh, damn!"
        TARBECK "The anticipation is killing me..."
    scene lady_tarbeck_darkmage_tablebj_3
    with dissolve
    $ Pause()
    #first time
    if IsFirstTime():
        "Lady Tarbeck pushed her head forward, swallowing more of my cock as her lips glided back and forth faster."
        MC "YOU HAVE ANYTHINGGGGG TO WORRY ABOUT!"
        "Lady Tarbeck did her best once again to suppress a laugh."
        TARBECK "... Well, that was more assuredly confident than I expected."
        LADY_TARBECK "{i}*Slurp* *Slurp*{/i}"
        LADY_TARBECK "Mhmmm..."
        TARBECK "Did you hear something?"
        MC "N-No! Not at all!"
        TARBECK "I swore I heard-"
        TARBECK "Hm, must be my imagination."
        TARBECK "Anyway, I do appreciate you taking the time to talk to me."
        MC "O-Of course, Lord Tarbeck."
        "It was becoming increasingly hard to focus on Lord Tarbeck's words."
        "My balls, feeling heavier and fuller by the hour, felt desperate to unload."
    #repeat
    else:
        "Lady Tarbeck's mouth opened slightly wider as she stuffed more of my cock down her throat."
        "Looking down, I watched as the greedy, corrupted little dark mage slid her wet mouth over my cock faster."
        "Her eyes remained locked onto me the whole time like a predator as she coated my cock in her warm, shiny saliva."
        TARBECK "Can't you tell me anything about what the two of you are up to?"
        MC "Ahh...!"
        MC "I can tell you one thing."
        TARBECK "Oooh!"
        TARBECK "Go on, what is it?"
        "As Lady Tarbeck continued to suck my cock furiously beneath the table, it was becoming impossibly difficult not to finish down her throat there and then."
        MC "We... {i}*Huff*{/i} Mess around closer than you think."
        TARBECK "Hoho! How excellent!"
        TARBECK "I did the same thing with Lady Visharia. Wonderful fat ass!"
        "The words seemed to trigger a tinge of spite in Lady Tarbeck, who thrashed her tongue furiously in response with reckless abandon."
        LADY_TARBECK "{i}*Slurp!* *Slurp!*{/i}"
        LADY_TARBECK "Bhasterdhh!"
        LADY_TARBECK "(Don't worry, 'darling,' I'll be sure to drain [player_name] ten times as much as you've dumped into your whores!)"
        LADY_TARBECK "(I have a lot of catching up to do, it seems!)"
        TARBECK "There's that sound again!"
        TARBECK "Did you hear it?"
        MC "N-No..."
        MC "(Oh gods, I'm going to cum in front of him any moment!)"
        TARBECK "Perhaps the servants are fucking nearby again?"
        $ UnlockGalFlag("lady_tarbeck", "tablebj", "var_rep")
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "tablebj")
    $ PlaySexFx(audio.kiara_bj_finish)
    $ ReduceInfectionFromSex("lady_tarbeck")
    scene lady_tarbeck_darkmage_tablebj_cum
    with flash
    $ Pause()
    if IsFirstTime():
        "As Lady Tarbeck swallowed my cock deeper, her nose pressed up against my pubic hair as she took the last few inches."
        "As she did so, the sudden sensation overtook me."
        "With a short gasp, I barely suppressed my groan as she swallowed my load."
        TARBECK "... Are you alright?"
        TARBECK "You're pulling a strange expression."
        MC "Y-Yes... {i}*Huff*{/i} Just the heat is, uhh... getting to me."
        TARBECK "Oh! You really must be careful!"
        scene black with dissolve
        "Slowly, Lady Tarbeck dragged her lips off my cock, and with the slightest {i}*pop,*{/i} I watched my cock spring free from her mouth."
        "Smiling, her head retreated back through the portal, which closed behind her..."
    else:
        "Lady Tarbeck pushed herself forward once more, swallowing the last few inches as her nose pressed up against my pubic hair."
        "As her tongue thrashed and beat, once more, I barely stopped myself from moaning loudly as I fed the repressed little dark mage her lunch."
        "As she swallowed down every drop, Lord Tarbeck, blissfully unaware, watched my contorted expression."
        TARBECK "The heat again?"
        MC "Y-Yes... It's very..."
        MC "{i}*Huff* Intense.{/i}"
        scene black with dissolve
        "Lady Tarbeck slowly pulled her lips away from my cock, dragging them off inch by inch as her eyes refused to blink the entire time."
        "When my cock was finally released, fully cleaned by her mouth, she smiled and motioned 'shhh' as her head retreated back through the portal, which once again closed behind her."
    $ StopReplay()
    $ AutoMus(True)
    ## cont both
    "As I carefully put my cock away, Lady Tarbeck herself appeared a few moments later and entered the dining hall, smiling as if nothing had happened."
    $ LocFlush()
    show mc at cright_f
    show lord_tarbeck at right_f
    with dissolve
    show lady_tarbeck at cleft with easeinleft
    TARBECK @talk "Ah! There you are!"
    TARBECK @talk "I was just talking to our friend here."
    LADY_TARBECK @smile "I hope you weren't boring him with talks of business, dear."
    LADY_TARBECK @blush "{i}Why... He looks like he's just been drained.{/i}"
    if not IsFirstTime():
        scene black with dissolve
        $ LocSet("hamun_tarbeck_mainhall")
        $ LocEnter()
    TARBECK @talk "Of course not. Anyway, I must get going. You've reminded me that business does call."
    LADY_TARBECK @smile "Of course, dear."
    show lord_tarbeck at center_f with ease
    "As he turned to leave, Lady Tarbeck stopped him."
    LADY_TARBECK @smile "OH, darling!"
    "Before he could go, Lady Tarbeck made a point of throwing herself into his arms and kissing him passionately."
    TARBECK @smile "Oh!"
    TARBECK @talk "Thank you, my love."
    TARBECK @think "Though... Have you been drinking wine or something? You taste a little... {i}different.{/i}"
    LADY_TARBECK @smile "Just some sweets brought in from Newyark, dear."
    TARBECK @talk "I see... Well, enjoy yourselves."
    hide lord_tarbeck with easeoutleft
    MC @smile "Remind me never to get on your bad side."
    LADY_TARBECK @smile "Mmm... Tomorrow night."
    LADY_TARBECK @smile "I want to go to a brothel."
    MC @think "What?"
    LADY_TARBECK @smile "I have a plan... Pick me up here and take me to one."
    MC @think "Is this... one of your plans?"
    LADY_TARBECK @blush2 "Well, you'll have to find out, won't you?"
    LADY_TARBECK @talk "Till then, I have more studies to do."
    hide lady_tarbeck with easeoutleft
    "Lady Tarbeck blew me a kiss as she left, but my eyes were firmly locked onto her swaying ass as she moved."
    show mc at center_f with ease
    MC "(Just what is she planning?)"
    scene black with dissolve
    $ NoteUnlock("tarbeck_rom_darkmage_return_next_night")
    $ QstSetProgress(HouseLockTarbeckHouse, 4)
    $ QstSetProgress(RomanceLadyTarbeck, 8)
    $ QstSetDelay(RomanceLadyTarbeck, 1)
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()

######################################################################
# SCENE 8 - TARBECK MANOR, EVENING
# IMPLEMENTATION NOTES :
# - Journal: ""
# - Trigger: auto-trigger when the player enters the Tarbeck manor in the evening.
label rom_tarbeck_darkmage_escorttobrothel:
    $ NoteLock("tarbeck_rom_darkmage_return_next_night")
    show lord_tarbeck at right_f
    show lady_tarbeck at cright_f 
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @smile "There you are! Come on, let's go."
    TARBECK @shock "Umm, my love."
    TARBECK @shock "Where do you think you're going at this hour?"
    LADY_TARBECK @blush "{i}Wouldn't you like to know?{/i}"
    TARBECK @shock "I-"
    show lady_tarbeck at center_f with ease
    "Without another word, Lady Tarbeck grabbed my hand as she pulled me out of the manor."
    show mc at blurin, cleft_f
    show lady_tarbeck at blurin, center
    $ Pause(0.1)
    hide lady_tarbeck
    hide mc
    with easeoutleft
    LADY_TARBECK "Come now..."
    LADY_TARBECK "{i}Take me to that place I asked to see.{/i}"
    show lord_tarbeck at center_f with ease
    TARBECK @shock "... Oh!"
    scene black with dissolve
    $ CharSetVar("lady_tarbeck", "darkmage_mask", True)
    "... A short while later, we found ourselves within a brothel, as Lady Tarbeck took on a disguise."
    $ LocSet("hamun_brothel")
    $ LocFlush()
    with dissolve
    show mc at left
    show lady_tarbeck at cleft
    with easeinleft
    MC @talk "Well, we are here."
    LADY_TARBECK @smile "Oh my... An actual den of debauchery!"
    LADY_TARBECK @think "You would think I would be used to seeing one, being married to my husband."
    LADY_TARBECK @talk "But it's strange actually... visiting one myself."
    MC @think "So what do you have planned?"
    "Lady Tarbeck smiled as she looked around."
    LADY_TARBECK @smile "You know... All these poor men coming here."
    LADY_TARBECK @smile "Coin spent night after night... Don't you think, for one night..."
    LADY_TARBECK @blush "Everyone deserves a little {i}fun off the books?{/i}"
    MC @think "What are you talking about?"
    LADY_TARBECK @talk "You see, dear... My portals?"
    LADY_TARBECK @talk "I can open them up anywhere."
    "She licked her lips excitedly."
    LADY_TARBECK @blush "{i}Including to invite a couple of friends here.{/i}"
    #Fade to black - finger snap sfx
    label repeat_tarbeck_darkmage_brothel:
    scene black with dissolve
    if RomanceLadyTarbeck().Romance_ScheduledGig == "date_brothel":
        $ CharSetVar("lady_tarbeck", "darkmage_mask", True)
        $ RomanceLadyTarbeck().Romance_ScheduledGig = None
        $ SetRepeatVariant(True)
        $ NoteLock("tarbeck_rom_darkmage_meet_at_brothel_rep")
        $ RomanceLadyTarbeck().HadSexToday = True
        "Lady Tarbeck was already waiting for me."
    "With a snap of her fingers, portals emerged around the brothel."
    "For the briefest moment, there was panic... Confusion, fear."
    "... Then, slipping out from the portals, beautiful red-skinned women with wings smiled alluringly at the men and Katai around the place."
    SUCCUBUS "... So... {i}We were invited to party then?{/i}"
    $ TimeAdvBy(TIME_05H)
    "{i}... Thirty minutes later.{/i}"
    label replay_tarbeck_darkmage_brothel:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx(audio.ves69_125, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_brothel_preg_idle
    else:
        scene lady_tarbeck_darkmage_brothel_nopreg_idle
    with dissolve
    $ Pause()
    "The night quickly became a blur around us as succubus women fought with Katai whores over clients."
    "... The fighting quickly dissolved into a full-blown orgy as Lady Tarbeck, having somehow persuaded me to transform,"
    "I pressed my cock between her tits as one of my tendrils pushed its way into her tight, wet cunt."
    MC "Gahhh...!"
    MC "How the fuck did you persuade me to go along with-"
    LADY_TARBECK "Stop talking and shove that thing down my mouth."
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_brothel_preg_1
    else:
        scene lady_tarbeck_darkmage_brothel_nopreg_1
    with dissolve
    $ Pause()
    "I didn't need much persuading. Shoving my cock into her mouth, Lady Tarbeck wasted no time sucking on the end of it."
    LADY_TARBECK "Mmmfghh..."
    LADY_TARBECK "Thatshhhitt... {i}*Slurp!*{/i}"
    LADY_TARBECK "Givishit thuuu mheee...!"
    "Her tongue thrashed and beat against the bulbous head as a literal orgy happened behind us."
    "Bemused, more and more people started crowding into the brothel to see what was going on, and quickly, those not fucked by the succubi were snatched up by the Katai girls."
    "{i}I wasn't sure the brothel had ever been so busy before!{/i}"
    LADY_TARBECK "Mhoreee! Mmhh! {i}*Slurp!*{/i}"
    $ PlaySexFx(audio.ves69_150, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_brothel_preg_2
    else:
        scene lady_tarbeck_darkmage_brothel_nopreg_2
    with dissolve
    $ Pause()
    "I pushed my cock faster between her tits as the room dissolved away around us."
    "The more I gave, the more powerful the effects of Lady Tarbeck's magecraft seemed to become."
    LADY_TARBECK "{i}Mhoree! Mhoree! Ghivehh mhee MHOREEE!{/i}"
    "My tendril pushed deeper, thrashing around as her grunts and moans grew louder."
    "I roared in approval, but it barely raised a head around us."
    "The succubi... The scent they released, no one could focus on anything more than fucking wildly around us."
    "Even the Katai, bored of the endless sex thanks to their profession, now fucked like wild animals."
    LADY_TARBECK "Cummhh!!"
    if not IsFirstTime():
        $ PregRoll("lady_tarbeck")
        if CharIsVisiblyPreg("lady_tarbeck"):
            $ UnlockGalFlag("lady_tarbeck", "darkmage_brothel", "var_rep_preg")
        else:
            $ UnlockGalFlag("lady_tarbeck", "darkmage_brothel", "var_rep_nopreg")
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "darkmage_brothel")
    $ ReduceInfectionFromSex("lady_tarbeck")
    $ PlaySexFx(audio.ves69_finish)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_brothel_preg_cum
    else:
        scene lady_tarbeck_darkmage_brothel_nopreg_cum
    with flash
    $ Pause()
    "I roared as I unloaded myself into Lady Tarbeck's mouth."
    "Her cheeks puffed out as she desperately tried to swallow the thick load now seeping from her mouth down onto her tits."
    LADY_TARBECK "Mmmmfghh?!"
    "I let out a low rumble as she continued to suck on the end of my cock for a few moments before carefully pulling her mouth away."
    scene black with dissolve
    $ StopReplay()
    $ AutoMus(True)
    $ Pause(0.25)
    $ LocFlush()
    show mc_transformed at cleft
    show lady_tarbeck at cright_f
    with dissolve
    #MC is transformed for this section
    LADY_TARBECK @smile "Now {i}that...{/i} was fun."
    if not IsFirstTime():
        $ CharSetVar("lady_tarbeck", "darkmage_mask", False)
        scene black with dissolve
        $ SetRepeatVariant(False)
        $ LocEnter()
    LADY_TARBECK @smile "We better get out of here though before everyone starts to come around and-"
    show lady_tarbeck at center_f with ease
    ESME @shocked "WAIT!"
    show lady_tarbeck at blurin, center
    "The two of us paused to look."
    show esme at cright_f with easeinright
    ESME @smile "I don't know what in the world you did but... Could you come around and do it again sometime?"
    LADY_TARBECK @shock "W-What?"
    ESME @smile "Look around you!"
    ESME @smile "Every girl is suddenly booked for the whole night! They're practically queuing up out the doors!"
    LADY_TARBECK @blush2 "Umm, but I... You realise those girls are succubus, right?"
    LADY_TARBECK @talk "That could-"
    ESME @smile "Easy flowing coin is what they are! People turn up to see if they get a free fuck from them, find a massive queue, and then line up for our girls instead!"
    show esme at nod
    "Esme smiled as she suddenly palmed off a bag of coins to Lady Tarbeck."
    LADY_TARBECK @shock "Oh!"
    ESME @smile "Come back soon!"
    show esme at blurin, cright
    hide esme with easeoutright
    #Esme exits off screen
    $ Pause(0.25)
    show lady_tarbeck at blurin, cright_f with ease
    LADY_TARBECK @smile "Well that was... {i}different from what I expected,{/i}"
    MC "Come on, let's get you home."
    LADY_TARBECK @smile "I'm learning so much about my magecraft... It's... It's incredible."
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    "{i}... A short while later.{/i}"
    $ CharSetVar("lady_tarbeck", "darkmage_mask", False)
    $ LocSet("hamun_tarbeck_mainhall")
    $ LocFlush()
    show mc at cleft
    show lady_tarbeck at cright_f
    with dissolve
    LADY_TARBECK @smile "That was... quite exhilarating, wasn't it?"
    MC @talk "Are you alright, do you need-"
    LADY_TARBECK @smile "Yes, yes... I'm fine."
    LADY_TARBECK @smile "... Tomorrow."
    MC @think "Tomorrow?"
    LADY_TARBECK @blush "My husband is away tomorrow night."
    LADY_TARBECK @blush "I want you to come here and make me yours properly tomorrow."
    MC @shock "You mean-"
    LADY_TARBECK @smile "Yes, {i}that.{/i}"
    LADY_TARBECK @smile "I'm ready."
    MC @smile "... Well, tomorrow night I shall be here then."
    show lady_tarbeck at center_f with ease
    hide lady_tarbeck
    hide mc
    show cg_lady_tarbeck_darkmage_kiss_normal at center
    with dissolve
    "Lady Tarbeck grinned, throwing herself forward into my arms for a kiss."
    "Her soft lips met mine as I squeezed at her soft ass before she retreated."
    hide cg_lady_tarbeck_darkmage_kiss_normal
    show mc at cleft
    show lady_tarbeck at cright_f
    with dissolve
    LADY_TARBECK @smile "I can't wait already..."
    scene black with dissolve
    $ QstSetProgress(RomanceLadyTarbeck, 9)
    $ QstSetDelay(RomanceLadyTarbeck, 1)
    $ NoteUnlock("tarbeck_rom_darkmage_return_after_brothel")
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()

#######################################################################################################
# SCENE 9 - TARBECK MANOR, FOLLOWING EVENING
# IMPLEMENTATION NOTES :
# - Journal: ""
# - Trigger: auto-trigger when the player enters the Tarbeck manor in the evening.
# - First-time vaginal portal version is non-pregnant. Anal is repeat-only.
# - Outcome: continue directly into Scene 10 the following morning.
label rom_tarbeck_darkmage_meetafterbrothel:
    $ NoteLock("tarbeck_rom_darkmage_return_after_brothel")
    show lady_tarbeck at cright
    show lord_tarbeck at right_f
    with dissolve    
    show mc at cleft with easeinleft
    "As the great doors to the manor opened, Lady Tarbeck stood beside her husband, visibly irritable."
    "Why was he still here? He was supposed to be away on business?"
    TARBECK @smile "Ah! [player_name]! Good to see you!"
    "My eyes passed back and forth between him and his wife."
    MC @talk "Lord Tarbeck."
    TARBECK @talk "I was supposed to be away on business, but it was cancelled at the last minute."
    LADY_TARBECK @smile "Darling... Dear..."
    LADY_TARBECK @smile "There's always more business. Don't let me take you away from-"
    TARBECK @smile "No, no. I think tonight I shall have a quiet night in and rest."
    TARBECK @smile "Please, [player_name], do feel free to stay the night should you wish."
    TARBECK @smile "I'll go fetch a bottle of wine."
    show lord_tarbeck at blurin, right
    hide lord_tarbeck with easeoutright
    LADY_TARBECK @angry "Grghh!"
    LADY_TARBECK @angry "He's ruining everything!"
    LADY_TARBECK @angry "Now how are we-"
    "She stopped herself for a moment."
    LADY_TARBECK @shock "...!"
    MC @think "Lady Tarbeck?"
    LADY_TARBECK @blush "Sleep in my quarters tonight."
    MC @shock "But... won't Lord Tarbeck expect you to stay with him?"
    LADY_TARBECK @blush "Just trust me. I'll give you a spare key."
    show lord_tarbeck at right_f with easeinright
    TARBECK @smile "So, shall I pour everyone a glass?"
    LADY_TARBECK @smile "Of course, dear..."
    scene black with dissolve
    $ TimeAdvBy(TIME_1H)
    "... The evening continued to drift by as the wine bottle slowly emptied."
    "Eventually, a laughing, drunk Lord Tarbeck retired to his quarters with Lady Tarbeck."
    "Doing as she asked, I made my way towards her private chambers..."
    $ LocSet("hamun_tarbeck_quarters_lady")
    $ LocFlush()
    show mc at cleft
    with dissolve
    MC "(... Well, I suppose I'd better get settled in for tonight.)"
    MC "(Is she planning to sneak out of bed and come here... or?)"
    MC "(Hm... I guess we'll see.)"
    # the repeat jumps to repeat label NOT to replay label 
    # cause theres logic 
    label repeat_tarbeck_darkmage_portal_vag:
    if RomanceLadyTarbeck().Romance_ScheduledGig == "portal_vag":
        $ RomanceLadyTarbeck().Romance_ScheduledGig = None
        $ SetRepeatVariant(True)
        $ NoteLock("tarbeck_rom_romance_meetatquarters")
        $ RomanceLadyTarbeck().HadSexToday = True

    # to be on safe side w/renpy interactions system
    $ Pause(0.25)
    label replay_tarbeck_darkmage_portal_vag:

    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if IsFirstTime():
        "As I lay down on the bed, my eyes staring up towards the ceiling, I wondered what Lady Tarbeck was doing."
        "It seemed strange. I half expected a knock at the door and for her to alluringly ask to come in... But no such knock came."
        "As I resigned myself to the possibility that perhaps nothing would come of it, I heard a whizzing sound."
        "As I looked over, I saw... A round, floating circle omitting a pinkish aura, and instinctively, I reached for a weapon that wasn't there."
        "Suddenly, emerging out of the hole... A pale... Naked ass."
        "I stared for a moment in disbelief, but then..."
        "A smirk crept across my face."
        "It seemed Lady Tarbeck had decided which part of her she wanted to visit me while she stayed tucked up in bed."
    else:
        "As I lay down on the soft bed and waited expectantly, I half-opened an eye as I heard the familiar whizzing sound."
        "Once more, the round, circular portal appeared, emitting a pinkish aura as Lady Tarbeck passed her soft, cute ass through the portal for me."
    scene lady_tarbeck_darkmage_portal_idle
    with dissolve
    $ Pause()
    if IsFirstTime():
        "With the quilt in one hand, I shuffled forward, positioning my cock against her womanhood."
        "Being careful not to make too much sound, I teasingly began to rub my cock against her wet womanhood."
        "I thought I could hear a soft, muffled moan from the other side of the portal but chose to ignore it."
    else:
        "Holding up the quilt, I shuffled forward once more, placing my cock against the familiar soft flesh of Lady Tarbeck's ass."
        "The softest of moans could be heard from the other side as I wedged and gently ground my cock against her ass."
        "As her womanhood glistened in the light, I carefully positioned the head of my cock."
    $ PlaySexFx(audio.adara_hj_loop, 1)
    scene lady_tarbeck_darkmage_portal_vag_1
    with dissolve
    $ Pause()
    if IsFirstTime():
        "As my cock slipped into her tight, warm womanhood, I could feel how wet she already was."
        "I began to slowly thrust, her soft ass bouncing against my cock as I watched my member sink into her."
        "If I listened carefully, I could hear soft moans coming from the other side..."
        LADY_TARBECK "(Oh gods... I can't believe I'm actually doing this!)"
        LADY_TARBECK "(D-Darling.... Don't wake up, please!)"
        LADY_TARBECK "(I need this so badly!)"
        "I wondered where Lady Tarbeck was right now... Had she slipped away from her bed during the night?"
        "... Or was she still lying beside her husband, blissfully asleep as she gave her ass to me... Quite literally."
    else:
        "As I pushed my cock into the tight, already wet hole, I swore I heard an audible groan coming from the other side."
        "I began to move back and forth, sinking my cock into her tight hole as she squeezed around me."
        LADY_TARBECK "(Gods, why do I love this so much?)"
        LADY_TARBECK "(Mmmfghh... After all the times you introduced me to another one of your 'conquests'.)"
        LADY_TARBECK "(D-Darling... You'd understand I'm just balancing the scales, right?)"
        LADY_TARBECK "Mmmfghh...!"
        LADY_TARBECK "(Don't wake up, don't wake up, don't wake up!)"
        LADY_TARBECK "(I need it, I need it so fucking bad!)"
    scene lady_tarbeck_darkmage_portal_vag_2
    with dissolve
    $ Pause()
    if IsFirstTime():
        "*Phap! Phap! Phap!*"
        "The sounds of flesh slapping together grew louder as I moved faster, slamming my cock into her eager, tight hole."
        LADY_TARBECK "Mmmfghh...!"
        LADY_TARBECK "(It's so fucking good!)"
        LADY_TARBECK "(I've never felt so full in my life!)"
        "As her tight womanhood squeezed, if I listened carefully, I could hear the muffled moans growing louder and louder."
        "There was something strangely perverse about fucking her ass like this."
        "The pious Lady Tarbeck, reduced to a literal sex toy for me, a pussy to fuck at my leisure."
        "And as I slammed my cock into her, I began to feel my heavy balls becoming desperately ready to unload into the little corrupted wife."
    else:
        "Knowing what the naughty little wife needed, I slammed my cock faster into her tight hole."
        "*Phap!* *Phap!* *Phap!*"
        "Her ass bounced off my cock with every thrust, the lewd sounds growing louder as I fucked her harder."
        LADY_TARBECK "Mmmfghh...!"
        LADY_TARBECK "(I fucking love his huge cock!)"
        LADY_TARBECK "(Urghh! Why couldn't this useless snoring degenerate next to me be hung like him?)"
        "Her tight pussy squeezed around me as though her life depended on it."
        "And if I listened carefully, I could hear more and more of the muffled, suppressed moans slipping through the other side of the portal."
        MC "(Let's hope Lord Tarbeck remains a heavy sleeper!)"
        "As the naughty married dark mage continued to let me have my way with her, eventually, my heavy balls slapping against her clit only felt heavier and fuller."
        "I knew I couldn't last much longer, and the thought of us nearly being caught only drove me closer to the edge."
    if not IsFirstTime():
        $ PregRoll("lady_tarbeck")
        $ UnlockGalFlag("lady_tarbeck", "portal", "var_rep_vag")
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "portal")
    $ ReduceInfectionFromSex("lady_tarbeck")
    $ PlaySexFx(audio.adara_hj_finish)
    scene lady_tarbeck_darkmage_portal_vag_cum
    with flash
    $ Pause()
    if IsFirstTime():
        "Burying my cock deep into her tight snatch,"
        "I could feel Lady Tarbeck tremble and shake as I emptied my load into her wet, hot pussy."
        LADY_TARBECK "MMMMFGHH!"
        LADY_TARBECK "(Oh gods... He's... He's cumming in me!)"
        LADY_TARBECK "(I let another man other than my husband actually finish inside of me!)"
        scene black with dissolve
        $ AutoMus(True)
        $ StopReplay()
        "Finally spent, I slowly pulled my cock from her well-fucked hole,"
        "Watching as my seed dripped and poured down her ass."
        "Slowly, she shuffled forward, moving her ass away as the portal closed behind her."
        "Rolling over, I slept peacefully until the morning... Wondering how well Lady Tarbeck would sleep."
        $ TimeAdvTo(TIME_MORNING)
        $ QstSetProgress(RomanceLadyTarbeck, 10)
        $ LocFlush()
        show mc at cright_f
        with dissolve
        MC "(Well, that was a pleasant night's sleep.)"
        MC "(I wonder where Lady Tarbeck is?)"
        show cg_guard_hamun at cleft with easeinleft
        MC @think "Hm?"
        GUARD "Lady Tarbeck requests your presence in her and Lord Tarbeck's quarters immediately."
        show cg_guard_hamun at blurin, cleft_f
        hide cg_guard_hamun with easeoutleft
        $ NoteUnlock("tarbeck_rom_darkmage_meet_at_lords")
        show mc at center_f with ease
        $ QstSetProgress(HouseLockTarbeckHouse, 5)
        MC "(I wonder what that's about...)"
    else:
        "I slammed my cock to the hilt of her tight pussy and unloaded into her."
        "My balls ached as I suppressed a groan, filling up the little wife with enough cum sloshing around inside of her that she certainly wouldn't need breakfast in the morning."
        "As I did so, I felt her pussy clasp around me in a death grip as she trembled with her own orgasm."
        LADY_TARBECK "MMMMFGHH!"
        LADY_TARBECK "(So fucking much!)"
        "As her pussy released itself from my cock, I slowly pulled out, watching the white cum seep from her stretched pussy."
        "Slowly, I watched as her ass disappeared back through the portal as it closed behind her."
        "Rolling onto my back, satisfied and drained, I sighed and closed my eyes... Wondering if I'd just fucked Lady Tarbeck to sleep."
        scene black with dissolve
        $ AutoMus(True)
        $ StopReplay()
        $ TimeAdvTo(TIME_MORNING)
        $ SetRepeatVariant(False)
    $ LocEnter()

label rom_tarbeck_darkmage_cantleave:
    MC "(I should probably see what Lady Tarbeck wants first...)"
    $ LocEnterQ()

#################################################################################################
# SCENE 11 - LORD TARBECK'S BEDROOM, MORNING
# IMPLEMENTATION NOTES :
# - Journal: ""
# - Until this scene is completed, prevent leaving the manor and show: 
# (I should probably see what Lady Tarbeck wants first...)
# - Trigger: auto-trigger when the player enters Lord Tarbeck's bedroom. 
# (bg_tarbeck_lord_quarters)
# - Outcome: complete the linear Dark Mage progression, 
# unlock free interaction/repeats, and permit pregnancy from this point onward.
label rom_tarbeck_darkmage_spell:
    $ NoteLock("tarbeck_rom_darkmage_meet_at_lords")
    $ CharSetClothes("lady_tarbeck", "ling")
    show lady_tarbeck at cleft
    with dissolve
    show mc at cright_f with easeinright
    MC @talk "I was summoned for-"
    MC @shock "Lady Tarbeck?!"
    scene black with dissolve
    LADY_TARBECK "...Transform."
    MC "But... Your husband is-"
    LADY_TARBECK "{i}Do it.{/i}"

    label repeat_tarbeck_darkmage_spell_vag:
    $ Pause(0.1)
    label replay_tarbeck_darkmage_spell_vag:

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_spell_preg_idle
    else:
        scene lady_tarbeck_darkmage_spell_nopreg_idle
    with dissolve
    $ Pause()

    if IsFirstTime():
        "Lined up behind Lady Tarbeck as she pushed her ass out towards me."
        "She looked back and smirked smugly with her arms wrapped around Lord Tarbeck, who sat naked in a daze."
        MC "Is he... alive?"
        LADY_TARBECK "Oh, he's better than alive."
        LADY_TARBECK "He's convinced right now we're fucking."
        MC "What?"
        LADY_TARBECK "Just a little spell..."
        LADY_TARBECK "Now stop worrying about him when I'm waving my ass in your face."
    else:
        "Lady Tarbeck smirked as she once again swayed her ass back and forth enticingly."
        LADY_TARBECK "It seems my husband is having another pleasant dream."
        LADY_TARBECK "While he sleeps, why don't you shove that huge prick of yours inside of me?"
        "With my cock wedged between her cheeks as she swayed her hips enticingly back and forth, she didn't exactly need to do much convincing."
        MC "Quite the cruel vixen when you want to be, aren't you?"
        LADY_TARBECK "I think it's only fair the scales get balanced after years of his paramours."
        LADY_TARBECK "Besides... {i}He did give his blessing, fufu.{/i}"
    $ PlaySexFx(audio.nijah_doggy_loop, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_spell_preg_vag_1
    else:
        scene lady_tarbeck_darkmage_spell_nopreg_vag_1
    with dissolve
    $ Pause()

    if IsFirstTime():
        "Lady Tarbeck moaned as my cock sank deeper into her tight womanhood."
        "She squeezed around me as I began to move back and forth, slamming up against her."
        LADY_TARBECK "Ooooh! Fuck!"
        LADY_TARBECK "That's it... Mmfghh..."
        LADY_TARBECK "Gods, your cock feels s-so different like this."
        "Lady Tarbeck cooed and moaned as she wiggled her butt against my cock, laughing as I continued to plough her field from behind."
        MC "Why did you make him - Grghh!"
        MC "{i}Wear that?{/i}"
        "She giggled mischievously."
        LADY_TARBECK "I thought it seemed oddly appropriate to keep his cock caged around me."
        LADY_TARBECK "{i}I prefer him that way when you're fucking me now.{/i}"
    else:
        "Lady Tarbeck wiggled her butt as she felt my cock sink into her tight pussy once more."
        LADY_TARBECK "Ahhh..."
        LADY_TARBECK "Back home where she belongs, fufu."
        "I began to move back and forth, her soft ass bouncing against my cock as her tits swayed with every motion."
        "The fat of her ass cushioned against my cock as I thrust into her each time, watching with delight as my member sank into her."
        LADY_TARBECK "Wondering where it all vanishes to?"
        MC "I seem to remember a blushing, anxious little wife who couldn't dream of taking a cock this big."
        "Lady Tarbeck grinned as she held on tighter to her husband's neck, slamming her ass back into me playfully."
        LADY_TARBECK "And now I'm allllll grown up."

    $ PlaySexFx(audio.nijah_doggy_loop2, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_spell_preg_vag_2
    else:
        scene lady_tarbeck_darkmage_spell_nopreg_vag_2
    with dissolve
    $ Pause()

    if IsFirstTime():
        "Something about her words set me off."
        "I began to move faster, dragging my beastly cock deeper into her as I watched the beaded member drag itself back out."
        "{i}*Phap!* *Phap!* *Phap!*{/i}"
        "The lewd sounds of flesh colliding grew louder as I fucked the tight little wife."
        LADY_TARBECK "Ahh! That's it! Oooh!"
        LADY_TARBECK "Fuck me harder! Show my darling husband how it's done!"
        "She laughed as Lord Tarbeck remained utterly dazed."
        LADY_TARBECK "You just know - {i}*Huff*{/i} He'd be stroking his cock if he could see this."
        LADY_TARBECK "Or he might want your head, fufu. He can be quite temperamental, as you know!"
        "I continued to roughly manhandle Lady Tarbeck as she moaned hotly."
        MC "I'm going to make you cum for that."
        LADY_TARBECK "Ahhh! Yes! YES!"
        LADY_TARBECK "You fucking are, aren't you?"
        LADY_TARBECK "My fucking beast!"
        LADY_TARBECK "You and your big, wonderful beastly cock are going to-"

    else:
        "I let out a low rumble as I began to slam my cock into the needy little dark mage."
        "As my beastly cock sank its beaded member into her, she moaned happily as the sounds of her ass shaking with every thrust grew louder."
        "{i}*Phap!* *Phap!*{/i}"
        LADY_TARBECK "Oh godsssss...!"
        LADY_TARBECK "That's it! Ahh! Fuck me!"
        LADY_TARBECK "Fuck me like an animal while this cuck sits there and daydreams!"
        LADY_TARBECK "Gods, your cock feels so good!"
        "I dragged my claws lightly, pressing against the soft flesh of her ass as she let out another shuddering moan."
        "As I did so, the words tumbled out so instinctively, I thought Shyahtan had said them."
        MC "You belong to me now."
        LADY_TARBECK "Y-Yes! Mmfghh!"
        LADY_TARBECK "It all belongs to you!"
        LADY_TARBECK "My mouth!"
        LADY_TARBECK "My pussy!"
        LADY_TARBECK "My ass!"
        LADY_TARBECK "G-Give my womb what it wants and - Ooooh! Fucking fill me up!"
        LADY_TARBECK "I'm so close! I'm so-"

    if not IsFirstTime():
        $ PregRoll("lady_tarbeck")
        if CharIsVisiblyPreg("lady_tarbeck"):
            $ UnlockGalFlag("lady_tarbeck", "spell", "var_rep_preg_vag")
        else:
            $ UnlockGalFlag("lady_tarbeck", "spell", "var_rep_nopreg_vag")
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "spell")
    $ ReduceInfectionFromSex("lady_tarbeck")
    $ PlaySexFx(audio.nijah_doggy_finish)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_spell_preg_vag_cum
    else:
        scene lady_tarbeck_darkmage_spell_nopreg_vag_cum
    with flash
    $ Pause()

    if IsFirstTime():
        MC "GRGHHHH!"
        $ PlaySound("audio/cfx/transform.ogg")
        "Lady Tarbeck's eyes widened as she felt the rush of warmth enter her."
        "She shuddered, her eyes rolling back as I filled her womb with my seed."
        LADY_TARBECK "Oooooh....!"
        LADY_TARBECK "Planning on expanding this household? Fufu..."
        LADY_TARBECK "Gods, I think I might be able to skip breakfast... and lunch after that."
        scene black with dissolve
        $ AutoMus(True)
        $ StopReplay()
        $ LocFlush()
        show mc at right_f
        show lady_tarbeck at center
        show lord_tarbeck at left
        with dissolve
        "... A short while later, Lady Tarbeck wiped herself clean as she smiled towards me."
        LADY_TARBECK @smile "Good morning to you too, my beast."
        LADY_TARBECK @blush "I think I've indulged more than enough now to continue my training."
        MC "So, we are done?"
        LADY_TARBECK @blush "Oh no, you've made an addict of me, haha!"
        LADY_TARBECK @blush2 "Be sure to come around soon... Very soon... For a repeat performance, my handsome beast."
        scene black with dissolve
        $ CharSetClothes("lady_tarbeck", "normal")
        $ QstSetProgress(RomanceLadyTarbeck, 11)
        $ QstSetProgress(HouseLockTarbeckHouse, 5)
    else:
        "As the heavy load splashed into her welcoming womb, Lady Tarbeck could only shudder."
        MC "{i}*ROARS!*{/i}"
        $ PlaySound("audio/cfx/transform.ogg")
        LADY_TARBECK "AHHHHHHH...!"
        LADY_TARBECK "That's it - Ahh! My beast!"
        LADY_TARBECK "Breed your little bitch good!"
        LADY_TARBECK "Gods... You've stuffed me full."
        LADY_TARBECK "What's my poor defenceless womb to do, swimming around in your seed now?"
        "I playfully slapped her ass, watching the fat jiggle as she giggled."
        scene black with dissolve
        $ AutoMus(True)
        $ StopReplay()
        $ LocFlush()
        show mc at right_f
        show lady_tarbeck at center
        show lord_tarbeck at left
        with dissolve
        LADY_TARBECK "Ahh... Give me a few moments to sort myself out."
        LADY_TARBECK "And thanks for the fuck, {i}darling.{/i}"
        scene black with dissolve
        $ SetRepeatVariant(False)
    $ LocSet("hamun_tarbeck_mainhall")
    $ LocEnter()


label rom_tarbeck_darkmage_spell_anal:
    "Entering Lord Tarbeck's bedroom once more, he sat motionless in the chair, completely out of it,"
    "his cock restrained as Lady Tarbeck waved her fat ass enticingly towards me."
    LADY_TARBECK "Come on now..."
    LADY_TARBECK "Don't keep me waiting."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_spell_preg_idle
    else:
        scene lady_tarbeck_darkmage_spell_nopreg_idle
    with dissolve
    $ Pause()

    "Lady Tarbeck giggled as she felt my cock rub against her soft ass."
    "She wiggled her butt enticingly as I gripped her ass and stared down at the welcoming, lubed-up hole that had been prepared just for me."
    LADY_TARBECK "You know, I think he might have a heart attack if he knew this hole was {i}alllll{/i} for you."
    LADY_TARBECK "Not that I'd ever let his cock near it anyway."
    MC "Are you ready?"
    LADY_TARBECK "To get fucked in the ass?"
    LADY_TARBECK "No... But I am going to enjoy it immensely all the same!"

    $ PlaySexFx(audio.nijah_doggy_loop, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_spell_preg_anal_1
    else:
        scene lady_tarbeck_darkmage_spell_nopreg_anal_1
    with dissolve
    $ Pause()

    "With one sharp push, her tight ass stretched around my cock as she let out a guttural moan."
    LADY_TARBECK "Urghhh...!"
    LADY_TARBECK "F-Fuck... {i}*Huff*{/i} I feel like you're going to tear my poor ass apart back there!"
    "I kept the movement slow as I fucked her tight rear, the ring of her ass gripping around my cock for dear life."
    MC "{i}*Low rumble*{/i}"
    LADY_TARBECK "H-Ha!"
    LADY_TARBECK "My ass feels that good it's left you speechless, hmm?"
    "Gently pressing a claw into the soft flesh of her ass, not enough to penetrate the skin but enough to leave a pinkish mark, she cooed softly."
    LADY_TARBECK "A-Ahh...!"
    LADY_TARBECK "My ass... My ass burns so much..."
    LADY_TARBECK "But I want more! Give it to me!"
    LADY_TARBECK "Give me more!"
    $ PlaySexFx(audio.nijah_doggy_loop2, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_spell_preg_anal_2
    else:
        scene lady_tarbeck_darkmage_spell_nopreg_anal_2
    with dissolve
    $ Pause()

    "Lady Tarbeck's mouth hung agape as I pushed more of my meat into her ass."
    "Slamming up against her, I gave her exactly what she wished for."
    "{i}*Phap!* *Phap!* *Phap!*{/i}"
    "She clung desperately to her husband's neck with gritted teeth as he sat there,"
    "blissfully unaware that his wife was being ass-fucked right in front of him."
    LADY_TARBECK "T-That's it!"
    LADY_TARBECK "THAT'S IT YOU BIG BASTARD!"
    LADY_TARBECK "FUCK MY ASS!"
    LADY_TARBECK "I DON'T WANT TO BE ABLE TO WALK STRAIGHT FOR A WEEK!"
    "As her knees began to buckle, I could sense Lady Tarbeck's growing need to finish as her heart raced."
    "My cock, slamming and pushing its way into her poor, abused ass, inched closer and closer to climax until..."

    if CharIsVisiblyPreg("lady_tarbeck"):
        $ UnlockGalFlag("lady_tarbeck", "spell", "var_rep_preg_anal")
    else:
        $ UnlockGalFlag("lady_tarbeck", "spell", "var_rep_nopreg_anal")
    $ ReduceInfectionFromSex("lady_tarbeck")
    $ PlaySexFx(audio.nijah_doggy_finish)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_darkmage_spell_preg_anal_cum
    else:
        scene lady_tarbeck_darkmage_spell_nopreg_anal_cum
    with flash
    $ Pause()

    "Burying my cock in her ass, Lady Tarbeck whimpered, her hands coiling tightly as she felt the thick, heavy rush of warmth in her bowels."
    LADY_TARBECK "{i}*Gasp!*{/i}"
    MC "{i}ROARRRR!{/i}"
    $ PlaySound("audio/cfx/transform.ogg")
    "I held Lady Tarbeck in place as her legs turned to jelly beneath me, making sure every drop of my load was pushed into her."
    "After a few careful, delicate minutes, I slowly unsheathed my cock from her rear."
    "Her stretched hole gushed out my load, letting it leak onto the floor as she dropped to her knees instinctively."
    scene black with dissolve
    $ StopReplay()
    LADY_TARBECK "That was... {i}*Huff*{/i}"
    LADY_TARBECK "{i}Incredible...{/i}"
    "She offered up an exhausted smile from the floor."
    LADY_TARBECK "Mmm... I'll be back down in a few minutes."
    LADY_TARBECK "Just give me... {i}*Huff*{/i}"
    LADY_TARBECK "{i}A few minutes to recover...{/i}"
    $ SetRepeatVariant(False)
    $ AutoMus(True)
    $ LocEnter()

label rom_tarbeck_darkmage_portal_anal:
    $ RomanceLadyTarbeck().Romance_ScheduledGig = None
    $ SetRepeatVariant(True)
    $ NoteLock("tarbeck_rom_romance_meetatquarters")
    $ RomanceLadyTarbeck().HadSexToday = True
    $ Pause(0.25)
    label replay_tarbeck_darkmage_portal_anal:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    scene lady_tarbeck_darkmage_portal_idle
    with dissolve
    $ Pause()
    "Lying down on the bed, I waited patiently once more for the whizzing sound as the portal appeared."
    "Lady Tarbeck pushed her ass through once more, and as I began to lightly rub my cock teasingly against her asshole,"
    "I smirked as I realized it seemed she had generously applied a good amount of lube to her backdoor."
    MC "(Good girl.)"
    LADY_TARBECK "(Come on... Come on... Come on...)"
    LADY_TARBECK "(I'm so nervous but excited.)"
    $ PlaySexFx(audio.adara_hj_loop, 1)
    scene lady_tarbeck_darkmage_portal_anal_1
    with dissolve
    $ Pause()
    "With one sharp push, her asshole gave way and stretched around my cock."
    "Her butt twitched with the sudden sensation, and I thought she might pull away instinctively."
    "Instead, after keeping still for a few moments, she began to gently rock, giving me the signal to begin moving."
    LADY_TARBECK "(F-FUCKKK...!)"
    LADY_TARBECK "(It burns, but... Ahh!)"
    LADY_TARBECK "(I want him to have it... Mhmm...)"
    LADY_TARBECK "({i}This is *his* hole!{/i})"
    "The tight ring of her ass squeezed my cock effortlessly as I fucked her cute butt."
    "Listening carefully, I could hear her trembling breath on the other side of the portal as I took her rear."
    MC "(Gods, is her ass tight...)"
    LADY_TARBECK "(Ha... It's so strange but... It's starting to feel...)"
    LADY_TARBECK "({i}Kind of nice?{/i})"
    scene lady_tarbeck_darkmage_portal_anal_2
    with dissolve
    $ Pause()
    "Moving faster, I forced a couple more inches into her tight rear as I heard an audible gasp come from the other side."
    "Slamming my cock into her butt, her ass continued to squeeze around me as I fucked her harder."
    LADY_TARBECK "(Y-Yes...!)"
    LADY_TARBECK "{i}*Huff*{/i} Mmfghh...!"
    LADY_TARBECK "(T-Take what you need.)"
    LADY_TARBECK "(Take my poor little ass!)"
    "As I re-arranged Lady Tarbeck's guts, I wondered if her husband was still blissfully asleep next to her."
    "Unaware that his wife was currently giving up her ass for a man just across the hallway?"
    "As her tight butt continued to work and try to wring my cock out for all its worth,"
    "I began to feel a growing, heavy, desperate need to fill this naughty little dark mage's ass with my load..."
    $ PlaySexFx(audio.adara_hj_finish)
    $ UnlockGalFlag("lady_tarbeck", "portal", "var_rep_anal")
    $ ReduceInfectionFromSex("lady_tarbeck")
    scene lady_tarbeck_darkmage_portal_anal_cum
    with flash
    $ Pause()
    "Burying my cock deeply into her rear,"
    "I began to flood the little wife's bowels with my hot load as I felt her tighten and squirm around my cock."
    "I heard an audible moan from the other side as she trembled around my member..."
    "Had she just come from being fucked in the ass?"
    LADY_TARBECK "(F-FUCKKKKKK!)"
    LADY_TARBECK "(My ass feels like it's on fire!)"
    LADY_TARBECK "{i}*Huff* *Huff*...{/i}"
    LADY_TARBECK "(Gods, I'm sweating, but it felt so GOOD!)"
    scene black with dissolve
    $ AutoMus(True)
    $ StopReplay()
    "Slowly, with cum still leaking and pouring out of her tight hole, I watched as Lady Tarbeck's ass vanished back through the portal as it closed behind her."
    "Rolling onto my back, I sighed and closed my eyes, smirking as I wondered if Lady Tarbeck would still be able to walk straight in the morning."
    $ LocEnter()
