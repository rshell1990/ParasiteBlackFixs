label qst_TheTarbecks_Ingrid_ReturnToGarden:
    $ CharSetVar("ingrid", "mask", True)
    show mc at cleft with easeinleft
    "A cool night breeze passed over me—a rare breath of fresh air in the humid desert heat."
    show ingrid at cright with easeinleft
    $ Pause(0.5)
    hide ingrid with easeoutright
    "Suddenly, a woman burst past me, tears streaking through her ruined makeup as she fled."
    MC @think "(What in the hells?)"
    show cg_guard_hamun as guard1 at cright with easeinleft
    show cg_guard_hamun as guard2 at right with easeinleft
    GUARD "Which way did she go?"
    GUARD "We must find her!"
    GUARD "Lord Tarbeck will not tolerate failure!"
    hide guard1
    hide guard2
    with easeoutright
    MC @serious "(Damn it...)"
    show mc at center with ease
    MC @serious "(This is the last thing I need right now.)"
    MC @serious "(Do I ignore this and keep playing Tarbeck’s games...)"
    MC @serious "(...or do I try to find that woman?)"
    $ QstTheTarbecks().IngridProgress = 1
    $ GoalShow(QstTheTarbecks, 9)
    $ LocEnter()

label qst_TheTarbecks_Ingrid_Investigate:
    show ingrid at center
    show cg_guard_hamun as guard1 at left
    show cg_guard_hamun as guard2 at right_f
    with dissolve
    GUARD "Finally found you."
    $ GoalComplete(QstTheTarbecks, 9)
    INGRID @scared "Please!"
    INGRID @scared "Please, just let me go!"
    show cg_guard_hamun as guard1 at cleft with ease
    GUARD "Don’t make this harder than it needs to be... girl."
    show ingrid at cright with ease
    "The panicked woman’s eyes met mine."
    "Before I could speak, she croaked out a desperate plea."
    show ingrid at shake
    INGRID @scared "H-Help me! Please!"
    INGRID @scared "I'M LORD ROLLO'S WIFE!"
    show cg_guard_hamun as guard1 at shake
    GUARD "FUCK!"
    show cg_guard_hamun as guard1 at center with ease
    GUARD "YOU STUPID CUNT!"
    GUARD "WHY DID YOU HAVE TO SHOUT THAT?!"
    show mc at left with easeinleft
    show cg_guard_hamun as guard1 at blurin, center_f
    GUARD "..."
    MC @serious "...Hold on a moment, let’s just—"
    GUARD "Sorry."
    GUARD "We can’t take any chances."
    "The guards reached for their blades."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    MC @angry "...Fuck!"
    # just in case
    $ TransformMC(False)
    $ TransformMarkus(False)
    $ TransformKiara(False)
    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice
    if QstTheTarbecks().PartyCompanion != "esme":
        $ PartyAddChar(QstTheTarbecks().PartyCompanion, Silent = True)
    $ StartBattle(BattleData(BackgroundImage = "pbat_tarbeck_garden_night", CharIDList_Right = ["e_guard_hamun", "e_guard_hamun"], CanTransform = False))
    if QstTheTarbecks().PartyCompanion != "esme":
        $ PartyRemChar(QstTheTarbecks().PartyCompanion, Silent = True)
    "The second guard collapsed to the ground, choking on his own blood."
    $ LocFlush()
    show mc at cleft
    show ingrid at cright_f
    with dissolve
    INGRID @smile "Oh gods—thank you!"
    INGRID @smile "Thank you so much!"
    $ AutoMus(True)
    MC @angry "You nearly got me killed!"
    INGRID @sad "I—I’m sorry, I—"
    "The woman broke down into sobs."
    INGRID @cry "Oh gods..."
    MC @think "...Who are you?"
    INGRID @sad "I am Ingrid Castilay."
    $ CharMeet("ingrid") 
    INGRID @sad "Wife of Lord Rollo Castilay."
    INGRID @sad "Please..."
    show ingrid at center_f with ease
    INGRID @sad "You have to help me escape this place!"
    INGRID @sad "I beg you!"
    menu:
        "I've never heard of the Castilays before...":
            INGRID @angry "Is this really the time for a history lesson?"
            INGRID @sad "We are an old southern house."
            MC @think "You mean one of the houses forced north when the war began?"
            INGRID @angry "Yes!"
            INGRID @angry "Now please—can we focus on what matters?!"
        "What are you even doing here?":
            pass
    INGRID @sad "Lord Tarbeck lent my husband coin."
    INGRID @sad "It was to fund an expedition south—to reclaim our lands."
    MC @think "What...?"
    MC @angry "Is your husband mad?"
    MC @angry "He thinks a few hired swords can do what the Alderian army couldn't?"
    INGRID @angry "We had no choice!"
    INGRID @angry "All our mines are in the south!"
    INGRID @angry "Our coffers are empty!"
    MC @serious "Urgh..."
    MC @think "That still doesn’t explain why {i}you{/i} are here."
    show ingrid at cright_f with ease
    INGRID @sad "...My husband offered me as collateral."
    MC @smile "Hah!"
    MC @angry "Some husband."
    INGRID @angry "We had no choice!"
    INGRID @sad "He swore he would return, but..."
    MC @think "{i}He hasn’t?{/i}"
    INGRID @sad "...No."
    show ingrid at blurin, cright
    INGRID @sad "And now Lord Tarbeck has me..."
    INGRID @scared "{i}Performing{/i} for him."
    INGRID @cry "I can’t endure this nightmare any longer!"
    show ingrid at blurin, cright_f
    INGRID @cry "Please—you must help me escape!"
    INGRID @cry "I’ll do anything you ask!"
    "Ingrid fumbled desperately through her belongings."
    INGRID @sad "T-These gold tokens!"
    INGRID @sad "I have at least a dozen!"
    INGRID @sad "They must be worth something, right?"
    INGRID @sad "I can pay you properly once I’m free!"
    menu:
        "Agree":
            pass
        "Refuse to help Ingrid escape":
            MC @talk "I’m sorry, my lady."
            MC @talk "I’m here for my own reasons."
            MC @talk "Helping you escape is too risky."
            INGRID @angry "You...!"
            INGRID @sad "Please."
            INGRID @scared "I can't escape without your help! I beg of you!"
            $ QstTheTarbecks().IngridProgress = 2
            $ LocEnter()
    # cont
    label qst_TheTarbecks_Ingrid_Investigate_helpingrid:
    INGRID @shock "You’ll... help me?"
    show ingrid at center_f with ease
    INGRID @smile "Thank the gods!"
    MC @think "Easy—we still need a plan."
    INGRID @talk "The maids whispered of a secret passage in the gardens."
    INGRID @talk "Find Lady Tarbeck."
    INGRID @talk "She knows where it is."
    MC @think "Lord Tarbeck’s wife?"
    INGRID @talk "She is nothing like him."
    INGRID @talk "She is kind..."
    INGRID @talk "{i}Sincere.{/i}"
    INGRID @talk "She has helped others escape before."
    show ingrid at cright_f with ease
    INGRID @talk "Please—it’s the only way."
    menu:
        "On it.":
            INGRID @sad "Please... hurry!"
            pass
        "How will I recognize her?":
            INGRID @talk "She dresses plainly."
            INGRID @angry "She refuses gowns—her silent protest."
            INGRID @talk "She spends most of her time in the library, check there!"
            pass
    $ QstTheTarbecks().IngridProgress = 3
    $ GoalShow(QstTheTarbecks, 10)
    $ LocEnter()

label qst_TheTarbecks_TalkToLady:
    if QstTheTarbecks().IngridProgress == 4:
        show lady_tarbeck at cleft with dissolve
        show mc at cright_f with easeinright
        LADY_TARBECK "Go now, get Lady Castilay out of here."
        $ LocEnter()
    elif QstTheTarbecks().IngridProgress == 5:
        show lady_tarbeck at cleft with dissolve
        show mc at cright_f with easeinright
        LADY_TARBECK "I hope Lady Castilay gets out of here safely..."
        $ LocEnter()
    show lady_tarbeck at cleft with dissolve
    show mc at cright_f with easeinright
    MC @think "Lady Tarbeck?"
    show lady_tarbeck at blurin, cleft
    LADY_TARBECK @scared "Hm?"
    LADY_TARBECK @talk "Do I know you?"
    MC @smile "No, but—"
    $ CharMeet("lady_tarbeck")
    LADY_TARBECK @sad "I won’t play my husband’s {i}games{/i}."
    LADY_TARBECK @sad "There are plenty of others who would indulge you."
    menu:
        "I need your help." if QstTheTarbecks().IngridProgress == 3:
            LADY_TARBECK @think "My help?"
            MC @serious "Lady Castilay."
            $ GoalComplete(QstTheTarbecks, 10)
            "Lady Tarbeck’s eyes widened."
            LADY_TARBECK @scared "...What of her?"
            MC @talk "She’s hiding in the gardens."
            MC @talk "She says you know of a passage she can use to escape."
            LADY_TARBECK @scared "I—"
            LADY_TARBECK @think "How do I know I can trust you?"
            MC @talk "If I meant to betray her, I already would have."
            MC @talk "She believes you can help."
            show lady_tarbeck at center with easeinleft
            "Lady Tarbeck glanced around before producing a small key."
            LADY_TARBECK @talk "There is a mermaid statue in the gardens."
            LADY_TARBECK @talk "Use this key to open the passage beneath it."
            LADY_TARBECK @talk "It will take you beyond the manor grounds."
            LADY_TARBECK @talk "But be careful..."
            LADY_TARBECK @talk "My husband keeps one of his... {i}curiosities{/i} down there."
            MC @think "Curiosities?"
            LADY_TARBECK @talk "The creature obeys only him."
            LADY_TARBECK @talk "I’ve never seen it myself..."
            LADY_TARBECK @scared "Only the remains of those he fed to it."
            show lady_tarbeck at cleft with ease
            MC "(What in the hells have I gotten myself into now?)"
            LADY_TARBECK @sad "Good luck..."
            LADY_TARBECK @sad "You’ll need it."
            $ QstTheTarbecks().IngridProgress = 4
            $ GoalShow(QstTheTarbecks, 11)
        "Farewell.":
            LADY_TARBECK @talk "Enjoy your evening."
    $ LocEnter()

label qst_TheTarbecks_TalkToIngrid:
    show ingrid at cright_f with dissolve
    show mc at cleft with easeinleft
    if QstTheTarbecks().IngridProgress == 2:
        INGRID @sad "Have you changed your mind?"
        INGRID @sad "Please... Help me!"
        menu:
            "Fine, I will help you.":
                jump qst_TheTarbecks_Ingrid_Investigate_helpingrid
            "It's still too risky.":
                INGRID @angry "I'll sooner take my own life than go back!"
                INGRID @sad "... You're my only hope."
                $ LocEnter()

    elif QstTheTarbecks().IngridProgress in [3, 4]:
        INGRID @talk "Have you spoken to Lady Tarbeck?"
        menu:
            "Yes." if QstTheTarbecks().IngridProgress == 4:
                INGRID @smile "Really? What did she say?"
                MC @talk "I have the key."
                $ GoalComplete(QstTheTarbecks, 11)
                MC @talk "Do you know of a statue of a mermaid in these gardens?"
                INGRID @think "A statue of a—"
                show ingrid at shake
                INGRID @shock "...!"
                INGRID @shock "Come! This way—quickly!"
                hide ingrid with easeoutleft
                show mc at blurin, cleft_f
                hide mc with easeoutleft
                INGRID @shock "Before more guards see us!"
                scene black with dissolve
                jump qst_TheTarbecks_ReturnToIngridWithKey
            "Not yet.":
                INGRID @sad "Please hurry... I beg of you!"
                $ LocEnter()

label qst_TheTarbecks_ReturnToIngridWithKey:
    $ AutoAmb(False)
    play ambience "audio/ambience_loc/desert_night.ogg"
    scene cg_tarbeck_garden_statue_closed
    with dissolve
    show ingrid at right_f with easeinright
    show mc at cright_f with easeinright
    INGRID "This is it!"
    hide mc
    hide ingrid
    with dissolve
    "I carefully inspected the statue, running my hand along the smooth marble until I found it."
    "A small opening—once the key was pressed against it, it slid in with ease."
    "As I turned the key, heavy cogs spun somewhere beneath the stone."
    scene cg_tarbeck_garden_statue_open
    with dissolve
    "The statue groaned, slowly grinding aside to reveal a hidden passage beneath it."
    INGRID @smile "This is it! Come on!"
    "Before I could stop her, Ingrid was already hurrying down the passage."
    MC @surprised "Ingrid! Wait!"
    scene black with dissolve
    stop ambience fadeout 1.0
    "I rushed after her into the dimly lit corridor."
    $ AutoAmb(True)
    scene cg_tarbeck_mermaid_tunnel
    show mc at cright_f
    show ingrid at right_f
    with dissolve
    INGRID "Urgh... I can hardly see a thing down here!"
    INGRID "Are we going the right way?"
    MC "Ingrid! Watch your step—Lady Tarbeck warned there was—"
    $ AutoMus(False)
    stop music fadeout 1.0
    play sound2 "audio/cfx/demorai_roar_med.ogg"
    "Something erupted from the darkness."
    show cg_corpse_eater at left with easeinleft
    $ PlayMusicRandom("mus_battle_generic")
    "A terrible beast burst forward, roaring and gnashing its teeth."
    INGRID "AHHHHHH!"
    MC "Get back!"
    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_1
    if QstTheTarbecks().PartyCompanion != "esme":
        $ PartyAddChar(QstTheTarbecks().PartyCompanion, Silent = True)
    $ StartBattle(BattleData(BackgroundImage = "pbat_tarbeck_tunnel", CharIDList_Right = ["e_corpse_eater"]))
    if QstTheTarbecks().PartyCompanion != "esme":
        $ PartyRemChar(QstTheTarbecks().PartyCompanion, Silent = True)
    scene black with dissolve
    MC @talk "{i}*Huff* *Huff*{/i}..."
    $ LocNameSetTemp(_("An underground tunnel"))
    scene cg_tarbeck_mermaid_tunnel
    show mc at cleft
    MC @talk "It’s safe now. Come on, In—"
    MC @think "Ingrid?"
    show ingrid at cright_f with easeinright
    INGRID @scared "What..."
    INGRID @scared "What in the hells was that thing?!"
    MC @serious "It’s dead."
    MC @serious "Come on—we need to keep moving."
    $ AutoMus(True)
    show ingrid at center_f with ease
    INGRID @scared "H-Haha... ha..."
    INGRID @scared "What in the hells was I even thinking?"
    INGRID @scared "What am I supposed to do when I escape this place?"
    INGRID @sad "Our estate is being held for ransom by Tarbeck’s thugs."
    INGRID @sad "The last of our coin went into my husband’s expedition."
    INGRID @sad "...And I must face the truth."
    INGRID @sad "He is probably dead."
    INGRID @angry "Even our oldest allies at court have abandoned us!"
    INGRID @cry "...What am I to do?"
    INGRID @cry "I can’t survive out there!"
    INGRID @cry "I’m not strong enough!"
    MC @think "(I could tell her to head to the Pale Dragon and lie low.)"
    MC @think "(She won’t like it, but maybe she could work there for a time.)"
    MC @think "(Or I could tell her she’s on her own.)"
    menu:
        "Head to {i}The Pale Dragon{/i}. Tell the woman there that I sent you.":
            $ QstTheTarbecks().IngridRescuedOutcome = "go_to_pale_dragon"
            INGRID @shock "T-The Pale Dragon?"
            MC @talk "Do you know where it is?"
            INGRID @sad "I’ll find it. Don’t worry."
            INGRID @shock "Why..."
            INGRID @shock "Why are you being so kind to me?"
            MC @serious "Just go."
            MC @serious "I’ll meet you there once I’m finished here."
        "You have a good body and a pretty face. Find a brothel.":
            $ QstTheTarbecks().IngridRescuedOutcome = "find_a_brothel"
            INGRID @shock "W-WHAT?!"
            INGRID @shock "You would have me whore myself?!"
            MC @talk "Or don’t."
            MC @serious "You’ve got a good body and a pretty face."
            MC @serious "Snag a man. Sell your ass. I don’t care."
            MC @think "Surely it beats being a hostage to a degenerate merchant lord."
            INGRID @sad "I..."
            INGRID @sad "You’re right."
            INGRID @sad "I need to get out of here—no matter what."
        "You’ll figure it out.":
            $ QstTheTarbecks().IngridRescuedOutcome = "youll_figure_it_out"
            INGRID @sad "...But how?"
            MC @talk "Because you don’t have a choice."
            MC @talk "We just killed his men."
            MC @talk "You really think any lord will be forgiving after that?"
            INGRID @sad "...You’re right."
            INGRID @sad "I need to leave this place—no matter what."
    INGRID @talk "Here..."
    INGRID @talk "Take these golden token things."
    INGRID @talk "Maybe they’ll be worth something to you."
    show ingrid at nod
    $ PlayerAddItem("qst_tarbeck_golden_token", 5)
    $ QstTheTarbecks().CalcGoldTokens()
    INGRID @shock "Wait—"
    INGRID @shock "I never got your name, sir!"
    MC @talk "[player_name!t]."
    INGRID @smile "[player_name!t]..."
    INGRID @smile "I will remember that. I promise."
    "Ingrid smiled faintly as I led her deeper through the tunnels."
    scene black with dissolve
    "Eventually, the passage opened near the docks."
    "As we parted ways, I turned back toward the party, golden tokens heavy in my hand."
    $ LocNameReset()
    $ LocFlush(dissolve)
    show mc at cright_f with easeinright
    MC "(I hope she’s alright...)"
    MC "(Whatever happens.)"
    $ QstTheTarbecks().IngridProgress = 5
    $ LocEnter()