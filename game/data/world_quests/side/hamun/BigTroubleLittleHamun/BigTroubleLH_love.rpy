label qst_BigTroubleLHamun_marbella_love_offer:
    MARBELLA @think "A merchant lord?"
    MARBELLA @sad "What's his offer?"
    MC @talk "Twenty percent of the profits in return for his protection."
    MC @think "{i}And... I'll need to do him a favor.{/i}"
    MARBELLA @think "What kind of favor?"
    MC @talk "I just need to clear out a few gangs around the city."
    MARBELLA @shock "Are you fucking crazy?!"
    MARBELLA @sad "No, mate, look... You can't do all this for me."
    MARBELLA @sad "That's too bloody much."
    "Marbella paused as she pondered the offer uneasily."
    MARBELLA @sad "... Is there no other choice than to get in bed with a merchant lord?"
    MARBELLA @angry "They're not exactly much better than the Greater Trading Company to begin with."
    menu:
        "He's your best bet.":
            MARBELLA @sad "I guess you're right..."
            MARBELLA @sad "But I can't ask you to do what he's asking for me!"
            MC @talk "The choice to help you is my own, Marbella."
            MARBELLA @concern "... B-Bloody idiot."
            show mc at blurin, cright
            MARBELLA @sad "F-Fine."
            show marbella at center with ease
            "As I turned to leave, Marbella's hand reached out to grab mine."
            MARBELLA @shock "Wait!"
            show mc at blurin, cright_f
            MC @think "What is it?"
            MARBELLA @emb "{i}Kneel.{/i}"
            MC @think "Huh?"
            MARBELLA @emb "... C-Could you kneel down for me?"
            MARBELLA @angry "I'm fucking short, mate, so kneel for me a second!"
            menu:
                "{i}*Kneel down*{/i}":
                    "As I knelt down onto one knee, Marbella approached, her hands gently pressing against my cheeks."
                    MARBELLA "Y-You're a stupid, handsome bastard."
                    MC "I-"
                    hide mc
                    hide marbella
                    with dissolve
                    show cg_marbella_mc_kiss at center_f with dissolve
                    "Marbella leaned forward, pressing a firm kiss against my lips."
                    "I blinked, taken aback by her forwardness before closing my eyes."
                    "After a few tender seconds passed, she pulled back."
                    hide cg_marbella_mc_kiss
                    show mc at cright_f
                    show marbella at cleft
                    with dissolve
                    MARBELLA @emb "G-Go on now."
                    MARBELLA @angry "And if you tell any of the boys about that kiss, I'll knock your lights out!"
                    show mc at blurin, cright
                    hide mc with easeoutright
                    "I smiled as I left."
                    show marbella at center with ease
                    "If I listened carefully, I could hear just how fast Marbella's heart was beating."
                    MARBELLA @sad "... Bloody hells, Marbella, why'd you have to do something stupid like that?"
                "Marbella... I have to go.":
                    "Marbella stared at my face for a moment, reading my expression carefully before dejectedly looking away."
                    MARBELLA @sad "A-Alright then."
                    scene black with dissolve
            $ GoalComplete(QstBigTroubleLH, 1)
            if IsGoalVisible(QstBigTroubleLH, 2):
                $ GoalHide(QstBigTroubleLH, 2, Silent = True)
            if IsGoalVisible(QstBigTroubleLH, 3):
                $ GoalHide(QstBigTroubleLH, 3, Silent = True)
            $ GoalShow(QstBigTroubleLH, 100)

            $ QstBigTroubleLH().Kind = "love"
            $ LocSet("hamun_dist_docks")
            $ LocEnter()
        "Let me see what other options there are.":
            MARBELLA @talk "Alright then... Let me know."
            jump qst_BigTroubleLHamun_return_to_marbella_options

##############################################################################################################################
# Romance route 1 - Lord Zanzibat manor
#The player upon returning to Lord Zanzibat - New dialogue option appears 
label qst_BigTroubleLHamun_love_return_to_zanzibat_after_marbella_commits:
    ZANZIBAT @smile "Excellent!"
    $ GoalComplete(QstBigTroubleLH, 100)
    ZANZIBAT @smile "Now then, find the Khazah and eliminate them."
    ZANZIBAT @talk "You have two choices on how best to handle this."
    ZANZIBAT @talk "Simply kick the door in and raise hell."
    ZANZIBAT @talk "{i}Or,{/i} you may want to consider a more subtle approach."
    ZANZIBAT @talk "I have a little... device."
    ZANZIBAT @smile "Simply sneak inside and plant the device in their sleeping quarters somewhere they won't see it."
    ZANZIBAT @smile "The device will do the rest."
    menu:
        "I'd rather just kill them all myself.":
            $ QstBigTroubleLH().Love_KhazahChosenApproach = "kill"
            ZANZIBAT @talk "Brute force it is."
        "I'll plant your device.":
            $ QstBigTroubleLH().Love_KhazahChosenApproach = "device"
            $ PlayerAddItem("qst_bigtroub_poison_device")
            ZANZIBAT @smile "Wonderful."
            ZANZIBAT @talk "Here, some fake paperwork for the fools to sign while you get in."
            ZANZIBAT @talk "If anyone asks, it's for two crates of ale and wine to be delivered."
    ZANZIBAT @talk "Return when the job is done."
    $ GoalShow(QstBigTroubleLH, 105)
    $ LocEnter()

##############################################################################################################################
# Romance route 2-a - (Kill all the Khazah yourself)
# and Romance route 2-b (Poison the Khazah)
# Upon selecting on their hideout
label qst_BigTroubleLHamun_love_khazah_hideout:
    if QstBigTroubleLH().Love_KhazahChosenApproach == "kill":
        $ LocSet("hamun_khazah_hideout")
        $ LocFlush()
        show cg_bandit at center
        show cg_bandit2 at left
        with dissolve
        $ PlaySound(audio.door_crash)
        $ AutoMus(False)
        $ PlayMusicRandom("mus_battle_generic")
        show mc at right_f with easeinright
        "As I booted the door in sharply, blade drawn, a group of startled Khazah jumped from their seats to reach for their sabres."
        show cg_bandit at shake
        KHAZAH_LEADER "What is this?!"
        MC @angry "Lord Zanzibat wants you all gone."
        MC @angry "And I've come to deliver on that."
        show cg_bandit at shake
        KHAZAH_LEADER "You fool!"
        KHAZAH_LEADER "You would put your faith in a merchant lord?!"
        MC @angry "Shut up and die already."
        KHAZAH_LEADER "GUARDS!"
        scene black with dissolve
        jump qst_BigTroubleLHamun_love_khazah_hideout_knivesout
    elif QstBigTroubleLH().Love_KhazahChosenApproach == "device":
        pass
    show mc at cleft with easeinleft
    show mc at nod
    $ PlaySound(audio.door_knock)
    "Knocking on the door, one of the Khazah answered it."
    $ PlaySound(audio.doorthud)
    $ Pause(0.5)
    show cg_bandit at cright_f with easeinright
    KHAZAH "Speak."
    MC @talk "I need someone to sign the paperwork for some ale and wine crates ordered here."
    KHAZAH "Ale and wine?"
    "I showed the paperwork."
    KHAZAH "... Come in."
    scene black with dissolve
    $ LocSet("hamun_khazah_hideout")
    $ LocFlush(dissolve)
    show mc at cright_f with easeinright
    show cg_bandit at cleft with easeinleft
    "As I stepped inside, another one of the Khazah approached."
    KHAZAH "Where is this ale and wine?"
    KHAZAH "We have not ordered any..."
    menu: 
        "Oh, don't fuck with me now... this isn't the right place?" (Req_Charm = 16):
            KHAZAH "What?"
            MC @sad "Is the address wrong? I swear they keep fucking things up."
            show mc at nod
            "I handed over the fake paperwork to the Khazah, whose eyes skimmed over it."
            MC @sad "I'll just take the crates and get out of your way..."
            MC @smile "... Unless you guys want to take them off my hands for a fee?"
            KHAZAH "... Hmm."
            MC @talk "I could simply tell my employer I dropped the stuff off where I told them to."
            KHAZAH "Two crates, you say?"
            KHAZAH "... We would take it off your hands."
            KHAZAH "But before I do so..."
            KHAZAH "{i}Who is your employer?{/i}"
            menu:
                "The Greater Trading Company." (Req_Barter = 14):
                    pass
                "Lord Valenthor (Lie)":
                    KHAZAH "Never heard of him."
                    MC @talk "Oh, uh, he's a new merchant moved to Hamun from Novaras."
                    KHAZAH "... Then if he iz your employer, you must have hiz sigil coin."
                    MC @surprised "What?"
                    KHAZAH "All who work for merchants carry a sigil coin."
                    KHAZAH "You would know this if you actually worked for one."
                    MC @serious "I-"
                    show cg_bandit at shake
                    KHAZAH "SPY! ASSASSIN!"
                    $ AutoMus(False)
                    $ PlayMusicRandom("mus_battle_generic")
                    "The men, upon hearing his cry, sprung up from their seats and places around the room, blades drawn."
                    MC @angry "... Fuck."
                    jump qst_BigTroubleLHamun_love_khazah_hideout_knivesout
        "It's running a little late, should be here soon.":
            KHAZAH "No, it is not running a little late."
            KHAZAH "Because it waz never ordered!"
            MC @serious "Well, someone ordered it!"
            KHAZAH "I handle zer fucking orders."
            KHAZAH "I did not order anything, so cease your lies!"
            MC @surprised "Uhhh... but someone-"
            KHAZAH "Who are you working for?"
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            show cg_bandit at shake
            KHAZAH "GUARDS! WE HAVE AN INTRUDER!"
            MC @angry "Fuck. Violence it is!"
            jump qst_BigTroubleLHamun_love_khazah_hideout_knivesout

    # cont from GTC option
    KHAZAH "Is that so?"
    MC @talk "They stipulate in their terms delivery to the wrong address is non-refundable."
    MC @smile "As long as you cover the fee, I'm sure the GTC would be interested in handling an arrangement with you as well..."
    MC @smile "One more favorable than whoever you're buying all those drinks from right now."
    KHAZAH "Hmm, would four hundred coins cover the courier fee?"
    menu:
        "GTC courier fees are normally six hundred." (Req_Barter = 17):
            KHAZAH "{i}*Sigh*{/i} Of course they are with zer GTC..."
            KHAZAH "Fine, six hundred it is." 
            $ PlayerAddItem("gold", 600)
        "Four hundred should suffice.":
            KHAZAH "Here, your coin."
            $ PlayerAddItem("gold", 400)
    MC @smile "Great, do you have a storeroom for supplies?"
    KHAZAH "Thiz way."
    scene black with dissolve
    "I followed the Khazah into a backroom where they slept, stocked with miscellaneous boxes of food, bottles, and weapons."
    "While the guard was busy, I subtly planted the device in a small crevice in the wall."
    $ PlayerRemItem("qst_bigtroub_poison_device")
    KHAZAH "Just place the crates here, we will sort them out after."
    MC "No problem."
    $ LocFlush(dissolve)
    show mc at cright with easeinleft
    show cg_bandit at cleft with easeinleft
    KHAZAH "Return with zer supplies."
    show mc at blurin, cright_f
    KHAZAH "Remember, if you or the GTC try to play us, the Khazah will have their revenge!"
    MC "Of course..."
    KHAZAH "Now leave."
    show mc at blurin, cright
    hide mc with easeoutright
    show cg_bandit at center with ease
    "As I left the building, I looked back one last time, wondering morbidly about how all of them inside were already dead... They just didn't know it yet."
    MC "(Time to return to Lord Zanzibat.)"
    jump qst_BigTroubleLHamun_love_khazah_hideout_over

label qst_BigTroubleLHamun_love_khazah_hideout_knivesout:
    if PlayerItemQty("qst_bigtroub_poison_device") > 0:
        $ PlayerRemItem("qst_bigtroub_poison_device", PlayerItemQty("qst_bigtroub_poison_device"), Silent = True, MuteSfx = True)
    $ StartBattle(BattleData("pbat_hamun_street", CharIDList_Right = [{"e_bandit":8}, {"e_bandit":9}, {"e_bandit":8},]))
    $ LocFlush()
    show mc at cright_f
    with dissolve
    "As I cut down the first wave of them, reinforcements arrived from behind."
    show cg_bandit at left with easeinleft
    KHAZAH_LEADER "Get him, you fools!"
    MC @talk "Send as many as you want, it won't matter in the end."
    $ StartBattle(BattleData("pbat_hamun_street", CharIDList_Right = [{"e_bandit":10}, {"e_bandit":9}, {"e_bandit":9}, {"e_bandit":10}]))
    $ LocFlush()
    show mc at cright_f
    show cg_bandit at left
    with dissolve
    KHAZAH_LEADER "Bah!"
    KHAZAH_LEADER "You think just because you killed my men I'm going to let you take my head?"
    MC @serious "I don't expect you to do anything but die."
    KHAZAH_LEADER "YOU WANNA KILL ME?!"
    show cg_bandit at shake
    KHAZAH_LEADER "LET'S SEE YOU TRY!"
    $ StartBattle(BattleData("pbat_hamun_street", CharIDList_Right = [{"e_raider":11}, {"e_khazah_leader":12}, {"e_raider":11},]))
    scene black with dissolve
    "Spluttering blood and clutching at the bloody wound in his neck with his hand,"
    "the Khazah leader tumbled backwards, knocking over a table full of cards and coin as he did so."
    $ LocFlush()
    scene bg_hamun_khazah_hideout_blood
    show mc at cright_f
    show cg_bandit at cleft
    with dissolve
    KHAZAH_LEADER "You are...{i}*Urghh!*{/i}"
    KHAZAH_LEADER "A fool for serving them!"
    KHAZAH_LEADER "When your master - {i}*coughs!*{/i} plunges the dagger in your back, remember my words!"
    KHAZAH_LEADER "Whatever hell I am sent to, I'll see you there!"
    MC "Only so I can kill you again."
    $ PlaySound(audio.knife_slice)
    show mc at shake
    hide cg_bandit with dissolve
    "With a quick swipe of my blade, I silenced him."
    show mc at center_f with ease
    MC "(Well, that's done... Time to report back to Lord Zanzibat, I guess.)"
    jump qst_BigTroubleLHamun_love_khazah_hideout_over

label qst_BigTroubleLHamun_love_khazah_hideout_over:
    scene black with dissolve
    $ AutoMus(True)
    $ GoalComplete(QstBigTroubleLH, 105)
    $ GoalShow(QstBigTroubleLH, 110)
    $ LocSet("hamun_dist_docks")
    $ LocEnter()


################################################################################################################################
#Scene 3 - The player returns to speak to Lord Zanzibat, a new dialogue option appears 
label qst_BigTroubleLHamun_love_return_to_zanzibat_after_khazah:
    $ GoalComplete(QstBigTroubleLH, 110)
    ZANZIBAT @talk "Ah, good!"
    ZANZIBAT @smile "I shall have my guards sent to protect your dwarf's business."
    ZANZIBAT @talk "From now on, they are under my protection... The GTC will threaten them no more."
    MC @think "Just like that?"
    ZANZIBAT @talk "My word is worth its weight in gold."
    ZANZIBAT @talk "Now go, tell your friend the welcome news."
    $ GoalShow(QstBigTroubleLH, 115)
    $ LocEnter()

################################################################################################################################
# The player returns to Marbella – scene auto starts, Marbella is stood talking next to a city guard.
label qst_BigTroubleLHamun_love_return_to_marbella_after_zanzibat_deal:
    $ GoalComplete(QstBigTroubleLH, 115)
    show marbella at cleft
    show cg_guard_hamun at left
    with dissolve
    show mc at cright_f with easeinright
    MARBELLA @shock "There you are! Are you alright?"
    MC @talk "Lord Zanzibat says you're now under his protection."
    "My eyes turned towards the guard."
    MC @think "Though I suppose you already know that."
    GUARD @talk "I shall be outside if you need me."
    hide cg_guard_hamun with easeoutright
    "The guard turned and left, closing the door behind him."
    MARBELLA @sad "Aye, he was just explaining everything to me."
    MARBELLA @sad "*sigh* Can't say I'm too thrilled about being in bed with a merchant lord."
    MC @think "But surely it's better than being in the pocket of the GTC?"
    MARBELLA @talk "That's a low bar to pass."
    MARBELLA @emb "... Thank you for this."
    MARBELLA @emb "I'm not used to people lookin' out for me like this."
    $ QstComplete(QstBigTroubleLH)
    "Marbella thought for a moment, then spoke shyly."
    MARBELLA @emb "How about I treat you to some food later today?"
    MARBELLA @smile "There's a nice place I know, not too expensive but fancy enough."
    MARBELLA @blush "You know... To celebrate."
    MC @smile "Why not?"
    MARBELLA @smile "Great! Come back here after dark."
    $ NoteUnlock("marbella_love_meet_date")
    MARBELLA @talk "Gonna have me own knight in shining armour take me out! Haha!"
    $ LocEnter()