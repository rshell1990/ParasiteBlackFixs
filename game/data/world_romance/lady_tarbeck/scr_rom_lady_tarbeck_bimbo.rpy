screen RomLadyTarbeckKillBandits():
    if not block_wait_global and not block_wait_dynamic and wLocs[GetLocID()].CanWait:
        if QstGetProgress(RomanceLadyTarbeck) == 2:
            if not IsDaytime():
                fixed:
                    fit_first True
                    align (0.18, 0.81)
                    text tra(_("Gangs slain: %s/3")) % RomanceLadyTarbeck().Bimbo_SlainGangs:
                        xalign 0.5
                        yoffset -40
                    add "images/gui/buttons_loc/underlay.webp":
                        xalign 0.5
                    imagebutton:
                        idle "images/gui/buttons_loc/fight.webp"
                        hovered TooltipSetUI(_("Seek trouble"))
                        unhovered TooltipClearUI()
                        focus_mask "images/gui/buttons_loc/underlay.webp"
                        xalign 0.5
                        action [TooltipClearUI(), Hide("RomLadyTarbeckKillBandits"), Jump("rom_tarbeck_bimbo_hunt_bandits_btn")]

init python:
    notesLib["tarbeck_rom_bimbo_meetinacoupledays"] = Note(
        _("Meet Lady Tarbeck in a couple days"),
        _("Lady Tarbeck asked for some time to mull things over... I should give her a day or two."),
    )
    notesLib["tarbeck_rom_bimbo_huntbandits"] = Note(
        _("Hunt bandits in the docks"),
        _("Shyahtan insists that, if we are to alter Lady Tarbeck's body, we need to consume some bandits... I should probably hang around the docks at night."),
    )
    notesLib["tarbeck_rom_bimbo_report_bandits"] = Note(
        _("Return to Lady Tarbeck"),
        _("It's time to head back to Lady Tarbeck to begin her... {i}transformation.{/i}"),
    )
    notesLib["tarbeck_rom_bimbo_return_tomorrow"] = Note(
        _("Return to Lady Tarbeck tomorrow"),
        _("Shyahtan says I need to let Lady Tarbeck rest until tomorrow... I hope she will be alright."),
    )
    notesLib["tarbeck_rom_bimbo_return_in_couple_days"] = Note(
        _("Return to Lady Tarbeck in a couple days"),
        _("I should check in on Lady Tarbeck in a few more days..."),
    )
    notesLib["tarbeck_rom_bimbo_return_later_again"] = Note(
        _("Return to Lady Tarbeck tomorrow"),
        _("Lord Tarbeck asked for some time alone with Lady Tarbeck after her 'transformation'... I should come back in a day or so."),
    )
    notesLib["tarbeck_rom_bimbo_join_breakfast"] = Note(
        _("Join Lady Tarbeck for breakfast tomorrow"),
        _("Lady Tarbeck has invited me to join her for breakfast, at the mansion's dining hall... Maybe I should take her up on the offer?"),
    )
    notesLib["tarbeck_rom_bimbo_party"] = Note(
        _("Join Lady Tarbeck at the party"),
        _("Lady Tarbeck has invited me to join her for a party at the manor tonight. Maybe I should take her up on the offer?"),
    )
    

label rom_tarbeck_bimbo_meet_coupledays:
    $ NoteLock("tarbeck_rom_bimbo_meetinacoupledays")
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    "As the great doors swung open, Lady Tarbeck approached me timidly,"
    "her hands nervously clasped together."
    LADY_TARBECK @sad "A-Ah... You're back."
    LADY_TARBECK @blush2 "I wanted to discuss... {i}your proposal.{/i}"
    MC @sad "My lady, it was just one idea. There are other options we can-"
    LADY_TARBECK @talk "I want to do it."
    MC @shock "What?"
    LADY_TARBECK @blush2 "I want... to stop thinking so much."
    LADY_TARBECK @think "I've already secured this house's future, or at least done more than my share."
    LADY_TARBECK @sad "I was thinking... W-With all the years my husband has spent enjoying himself..."
    LADY_TARBECK @sad "{i}When do I get my turn?{/i}"
    LADY_TARBECK @sad "Or will I spend the rest of my life dealing with petty politics and-"
    "Lady Tarbeck let out a sigh just at the thought of it all."
    MC @think "These changes... They're permanent, you understand that?"
    "Lady Tarbeck nodded."
    LADY_TARBECK @sad "I... I understand."
    LADY_TARBECK @talk "...Now, tell me how we do it?"
    SHYAHTAN "(We must eat.)"
    MC "(What?)"
    SHYAHTAN "(Tell her to give us a few days.)"
    MC @talk "Uhh, I'll need to get back to you."
    LADY_TARBECK @think "Oh, uh... alright?"
    LADY_TARBECK @talk "I guess... return when you're ready?"
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    with dissolve
    show mc at center_f with easeinright
    MC @think "(What was that about?)"
    SHYAHTAN "(We must hunt.)"
    SHYAHTAN "(Without sustenance, we will lack the excess genetic material required to modify her body.)"
    MC "(Then... What do we propose?)"
    SHYAHTAN "(This city will hardly miss a few bandits...)"
    MC @talk "(Well... Macabre, but... I agree.)"
    SHYAHTAN "(Once we have slain them and consumed their flesh, we can return to our soon-to-be mate.)"
    $ NoteUnlock("tarbeck_rom_bimbo_huntbandits")
    $ QstSetProgress(RomanceLadyTarbeck, 2)
    $ LocEnter()

##########################
# scene 2
# Journal note: ""
# An icon appears in the Hamun docks during the evening: 
# "Hunt Bandits 0/3".
# Clicking it triggers the following encounter.
# After all 3/3 groups of bandits are slain, 
# progress to the next scene.

label rom_tarbeck_bimbo_hunt_bandits_btn:
    MC "(I can scout the streets to try and find some bandits.)"
    menu:
        "DEBUG: auto-complete" (AppearIf = config.developer):
            $ RomanceLadyTarbeck().Bimbo_SlainGangs = 3
            $ QstSetProgress(RomanceLadyTarbeck, 3)
            $ NoteUnlock("tarbeck_rom_bimbo_report_bandits")
            $ NoteLock("tarbeck_rom_bimbo_huntbandits")
            $ LocEnterQ()
        "{image=[ICON.CLOCK]} Look for rival gangs":
            hide screen RomLadyTarbeckKillBandits
            scene black 
            with dissolve
            $ TimeAdvBy(TIME_2H)
            jump rom_tarbeck_bimbo_hunt_bandits_try
        "Move on":
            show screen HamunFindKhazahRivals()
            $ LocEnterQ()


label rom_tarbeck_bimbo_hunt_bandits_try:
    # 50%
    if RngInt(1, 2) == 1:
        pass
    else:
        # Fail variant
        scene black with dissolve
        "I wandered around aimlessly, finding nothing of note."
        $ LocFlush()
        show mc at cright_f
        with dissolve
        MC "(No luck this time, it seems.)"
        $ LocEnter()

    scene black with dissolve
    "While wandering through the darkened alleyways of Hamun at night,"
    "a group of men circled and approached us."
    $ LocFlush()
    show mc at center
    with dissolve
    show cg_bandit at right_f
    with dissolve
    show cg_bandit2 at left
    with dissolve
    BANDIT "Looks like someone made a wrong turn..."
    BANDIT "Hand over everything you've got... Including the women."
    SHYAHTAN "(Wonderful. Fresh meat.)"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")

    $ tmpvar = {}
    if RomanceLadyTarbeck().Bimbo_SlainGangs == 0:
        $ tmpvar["chosen_team"] = [
            {"e_bandit":10}, 
            {"e_bandit":10}, 
            {"e_bandit":10}
        ]
    elif RomanceLadyTarbeck().Bimbo_SlainGangs == 1:
        $ tmpvar["chosen_team"] = [
            {"e_raider":10}, 
            {"e_raider":10}, 
            {"e_raider":10}
        ]
    elif RomanceLadyTarbeck().Bimbo_SlainGangs == 2:
        $ tmpvar["chosen_team"] = [
            {"e_monstorus_experiment":10}, 
            {"e_monstorus_experiment":10}, 
            {"e_raider":10}
        ]
    $ StartBattle(BattleData(BackgroundImage = "pbat_hamun_street", CharIDList_Right = tmpvar["chosen_team"]))
    $ tmpvar = {}
    $ AutoMus(True)
    $ RomanceLadyTarbeck().Bimbo_SlainGangs += 1
    if RomanceLadyTarbeck().Bimbo_SlainGangs == 3:
        $ LocFlush()
        with dissolve
        show mc at cleft with easeinleft
        SHYAHTAN "(Enough... We have procured enough sustenance.)"
        MC @think "(Now what?)"
        SHYAHTAN "(Let us return to Lady Tarbeck and begin her transformation.)"
        $ QstSetProgress(RomanceLadyTarbeck, 3)
        $ NoteUnlock("tarbeck_rom_bimbo_report_bandits")
        $ NoteLock("tarbeck_rom_bimbo_huntbandits")
        $ LocEnter()
    else:
        $ LocEnter()

############################
# Scene 3
# Journal note: ""
# Scene auto-triggers upon entering Tarbeck Manor.
label rom_tarbeck_bimbo_meet_after_bandits_slain:
    $ NoteLock("tarbeck_rom_bimbo_report_bandits")
    show mc at cleft with easeinleft
    show lady_tarbeck at cright_f with easeinright
    "Lady Tarbeck hurried towards me anxiously."
    LADY_TARBECK @think "Is... Is it time?"
    MC @talk "Yes, it's time."
    LADY_TARBECK @talk "Oh... That's wonderful, ummm..."
    "She paused awkwardly."
    LADY_TARBECK @think "So, what now exactly?"
    SHYAHTAN "(Take her to her quarters... We will need to put her to sleep for what comes.)"
    MC @talk "Let's go to your chambers, Lady Tarbeck."
    scene black with dissolve
    $ LocSet("hamun_tarbeck_quarters_lady")
    "She nodded, leading us to her private quarters."
    $ LocFlush()
    show lady_tarbeck at cright_f
    show mc at cleft
    with dissolve
    LADY_TARBECK @talk "Well... What now?"
    LADY_TARBECK @think "We should hurry before my husband returns from one of his trips."
    LADY_TARBECK @sad "He may... try to intervene."
    MC @talk "Of course..."
    SHYAHTAN "(Lay her on the bed.)"
    "I carefully guided Lady Tarbeck towards the bed, and as she lay down, she asked innocently,"
    hide lady_tarbeck with dissolve
    show mc at center with ease
    LADY_TARBECK "W-What happens-"
    "Suddenly, Lady Tarbeck's eyes grew heavy as she struggled to stay awake."
    LADY_TARBECK "What is... What is happening to-"
    "And just like that, Lady Tarbeck was blissfully asleep."
    MC "(What happened? Why did she just-)"
    SHYAHTAN "(I released a sedative to put her into a slumber.)"
    SHYAHTAN "(It will make the process easier for her... Now...)"
    SHYAHTAN "(Place our hand on her chest.)"
    "My hand reached out, carefully resting on her chest."
    play sound "audio/cfx/dark_chime.ogg"
    "As it did, the veins on my hand seemed to bulge as I felt something slither through it."
    "For the briefest moment, Lady Tarbeck winced as whatever left my hand buried itself inside her."
    MC "(Is she... going to be alright?)"
    SHYAHTAN "(She will be fine.)"
    MC "(... What happens now?)"
    SHYAHTAN "(... We return tomorrow.)"
    MC "(What?! What will she eat? What will-)"
    SHYAHTAN "(She will be fine. {i}It{/i} will keep her alive.)"
    MC "(What is {i}it?{/i})"
    SHYAHTAN "(It is a subspecies we can create. It will modify her body mass and neurological-)"
    "Shyahtan paused."
    SHYAHTAN "(... She will be safe. That is what matters.)"
    MC "A-Alright..."
    MC "I guess I'll come back tomorrow."
    show mc at blurin, center_f
    hide mc with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ QstSetProgress(RomanceLadyTarbeck, 4)
    $ NoteUnlock("tarbeck_rom_bimbo_return_tomorrow")
    $ QstSetDelay(RomanceLadyTarbeck, 1)
    $ LocEnter()


#####################################
#Scene 4
# Journal note: ""
#Scene auto-triggers upon entering Tarbeck Manor in the morning.
label rom_tarbeck_bimbo_return_after_rest:
    show lord_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    $ NoteLock("tarbeck_rom_bimbo_return_tomorrow")
    TARBECK @angry "WHAT IN THE WORLD HAVE YOU DONE?!"
    MC @think "What?"
    TARBECK @angry "MY WIFE! SHE'S..."
    TARBECK @angry "...C-COCOONED!"
    MC @think "...What?"
    scene cg_lady_tarbeck_transformation_1 
    with dissolve
    "Lord Tarbeck stormed off, saying nothing, but clearly expecting me to follow."
    $ LocSet("hamun_tarbeck_east_wing")
    "Heading towards Lady Tarbeck's room, I found she was no longer sleeping peacefully in her bed."
    "She was suspended inside a cocoon-like substance, a floating mass with tendrils attached to her body as she drifted peacefully within."
    "The room itself had transformed from a dignified noblewoman's bedroom into something more akin to a hive, dripping with slime and strange substances."
    $ LocFlush()
    show lord_tarbeck at cleft
    show mc at left
    with dissolve
    TARBECK @angry "What have you done to her?!"
    TARBECK @angry "What is this thing?!"
    MC @serious "Nothing she did not ask me to do."
    TARBECK @sad "I... What are you doing?"
    MC @talk "She wanted to change her body. When... {i}this{/i} is done with whatever it's doing..."
    MC @talk "She will be different, like she wanted."
    TARBECK @sad "She..."
    TARBECK @angry "Why did neither of you consult me?!"
    MC @talk "She felt you might try to stop her."
    TARBECK @sad "Of course I damn well would have!"
    TARBECK @angry "I tried to have the servants get her out! But the moment I tried, she seemed..."
    TARBECK @sad "In pain."
    "Lord Tarbeck paused, his anger fading as he gazed towards his wife, then back at me."
    SHYAHTAN "(ENSURE HE DOES NOT INTERFERE WITH THE PROCESS, OR I WILL DEAL WITH HIM MYSELF.)"
    MC @talk "It's dangerous for her if you touch her."
    MC @talk "She needs to stay in there until she's done."
    TARBECK @sad "...She will be alright, yes?"
    SHYAHTAN "(Yes.)"
    MC @talk "Yes."
    TARBECK @angry "Because if she is not... I swear upon the old gods and the new, I will-"
    MC @talk "A few more days, and she will be ready."
    TARBECK @sad "...Fine, I..."
    TARBECK @angry "...Go. Leave us alone for now."
    TARBECK @sad "You've done enough."
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    with dissolve
    show mc at cright_f with easeinright
    MC @talk "That could have gone better."
    SHYAHTAN "(Now that she is cocooned, she will be ready in a few days.)"
    SHYAHTAN "(Return then.)"
    $ NoteUnlock("tarbeck_rom_bimbo_return_in_couple_days")
    $ QstSetProgress(RomanceLadyTarbeck, 5)
    $ QstSetDelay(RomanceLadyTarbeck, 2)
    $ LocEnter()



############################################
#Scene 5
#Journal note: 
#Scene auto triggers entering into the Tarbeck Manor in the morning
label rom_tarbeck_bimbo_return_tf_again:
    $ NoteLock("tarbeck_rom_bimbo_return_in_couple_days")
    show mc at cleft with easeinleft
    show lord_tarbeck at cright_f with easeinright
    TARBECK @shock "Come quickly! COME!"
    MC @shock "...!"
    show lord_tarbeck at blurin, cright
    $ Pause(0.1)
    hide lord_tarbeck with easeoutright
    hide mc with easeoutright
    scene black with dissolve
    $ LocSet("hamun_tarbeck_quarters_lady")
    scene cg_lady_tarbeck_transformation_2 
    with dissolve
    "Following Lord Tarbeck with no time to explain, I almost tripped as I rushed into Lady Tarbeck's bedroom."
    "There, floating in the cocoon, was not Lady Tarbeck, but a beautiful, voluptuous blonde."
    TARBECK "She... She's been moving!"
    play sound "audio/cfx/poison_gas.ogg"
    "As we watched and waited, indeed, she did move, her eyes opening wide as she reached towards the walls of the cocoon and began to pull them down with ease."
    $ CharSetVar("lady_tarbeck", "variant", "bimbo")
    $ CharSetPortrait("lady_tarbeck", "images/characters/lady_tarbeck/bimbo/portrait.webp")
    $ CharSetClothes("lady_tarbeck", "naked")
    $ LocFlush()
    show lord_tarbeck at cleft
    show mc at left
    show lady_tarbeck at cright_f
    with dissolve
    #From here switch to Lady Tarbeck's Bimbo sprite model permanently. (She is naked for this section.)
    LADY_TARBECK @sad "Uhhh..."
    TARBECK @shock "M-My love..."
    TARBECK @shock "Are you alright?"
    "Lady Tarbeck shook her head, pushing her huge tits forward as she yawned."
    LADY_TARBECK @smile "That was like, a REALLYYYYY crazy nap!"
    "She giggled as she looked down to inspect her body."
    LADY_TARBECK @smile "OH WOW!"
    LADY_TARBECK @smile "My boobs are like, HUGE!"
    LADY_TARBECK @smile "And my butt is so big and nice too!"
    TARBECK @think "U-Uhh... Dear."
    TARBECK @think "You don't quite sound like yourself, perhaps you should lie down and-"
    LADY_TARBECK @smile "NU-UH!"
    LADY_TARBECK @smile "I feel AMAZING!"
    "As her eyes wandered over towards me, she squeezed at her breasts instinctively whilst licking her pillowy lips."
    "My eyes wandered over the piercings and other ornaments hanging from her."
    MC "(How did-)"
    SHYAHTAN "(It is organic.)"
    MC "(Organic?)"
    SHYAHTAN "(The creature replicated an image of herself deep within her mind... Those rings may appear gold, but they are bone.)"
    LADY_TARBECK @blush "Wanna try 'em out? Hehe!"
    "Lord Tarbeck froze, unsure of what to say."
    LADY_TARBECK @blush2 "But like, can you turn into the monster thingy? I like, wanna feel that MONSTER COCK while umm, you do all your crazy tentacle stuff!"
    TARBECK @think "Umm..."
    "Lord Tarbeck turned to me, taken aback and overwhelmed by what his wife had become."
    TARBECK @think "... C-Continue?"
    LADY_TARBECK @smile "YAYY! And don't worry dear! I like, umm, REALLY love you still and stuff!"
    LADY_TARBECK @smile "I'm just MUCH happier now I'm more silly and stuff!"
    TARBECK @think "I... see."
    "Something in Lord Tarbeck's voice seemed more unsure than ever."
    scene black with dissolve
    $ CharSetClothes("lady_tarbeck", "normal")
    "{i}Ten minutes later...{/i}"
    label repeat_tarbeck_bimbo_tj:
    $ Pause(0.1)
    label replay_tarbeck_bimbo_tj:

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx(audio.adara_hj_loop, 1)

    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbotj_preg_idle
    else:
        scene lady_tarbeck_bimbotj_nopreg_idle
    with dissolve
    $ Pause()

    if IsFirstTime():
        "Lady Tarbeck giggled as I held her up by her feet."
        "My huge cock prodding against the soft flesh of her new, heavy tits."
        LADY_TARBECK "Ahhhh...! {i}*Giggles*{/i}"
        LADY_TARBECK "Are you like, umm, watching, honey?"
        LADY_TARBECK "HE'S SO STRONG!"
        "She giggled once again, her eyes firmly locked onto the huge cock in front of her."
        LADY_TARBECK "AND SO BIGGG!"
        TARBECK "Y-Yes... I am watching, dear."
        TARBECK "... Continue."
    else:
        "Lady Tarbeck squirmed once again as I lifted her up by her feet."
        LADY_TARBECK "Weeeeeeeeeeeeee!"
        LADY_TARBECK "My head is all funny being held up like this!"
        LADY_TARBECK "Like, wanna watch me suck his cock, honey?!"
        "Lord Tarbeck smiled and watched, bemused, from the corner."
        TARBECK "Do as you please, my little degenerate."
        LADY_TARBECK "LIKE, I AM THE LUCKIEST GIRL EVER FOR HAVING THE BEST GUYS EVER!"

    $ PlaySexFx(audio.kiara_bj_loop, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbotj_preg_1
    else:
        scene lady_tarbeck_bimbotj_nopreg_1
    with dissolve
    $ Pause()

    if IsFirstTime():
        "With my cock shoved between her two globes, as the end prodded against her pillow-like lips, she instinctively opened her mouth to suckle on the head."
        LADY_TARBECK "{i}*Slurp!*{/i} Lhokkkhh dhearrhhh! {i}*Slurp!*{/i}"
        LADY_TARBECK "{i}*Slurp!* *Slurp!*{/i} Ih chanhh openhh mhyhhh mhouthhh shooo whidee! {i}*Slurp!*{/i}"
        TARBECK "Y-Yes... {i}*Huff*{/i} You can."
        "Lord Tarbeck sat mesmerised as he watched what had become of his wife greedily giving a generous titfuck as she sucked on the end of a monstrous cock."
        MC "{i}*Low rumble*{/i}"
        LADY_TARBECK "Mhhfghh! Heehh lhikeshh mheee! Mmfghh!"
        TARBECK "... K-Keep going, my love."
        TARBECK "I want to see what you can do with this new body."
        LADY_TARBECK "Mhokayhhh!"
    else:
        "Shoving my cock between her pillow-like tits, Lady Tarbeck giggled as she once again stretched her lips over the head of my cock."
        "I thrust forward, fucking the silly little wife's huge tits as her tongue twisted and teased the head of my cock."
        LADY_TARBECK "{i}*Slurp!* *Slurp!*{/i} Itshh lhikeee shooo yhummyhh! {i}*Slurp!*{/i}"
        LADY_TARBECK "{i}*Slurp!*{/i} Amhhh Ihhdhoinghhh ghooodhhh?"
        "I let out a low rumble in approval as Lord Tarbeck watched mesmerised."
        TARBECK "Yes dear, you're doing very good."
        TARBECK "... Now show me what you can really do!"

    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbotj_preg_2
    else:
        scene lady_tarbeck_bimbotj_nopreg_2
    with dissolve
    $ Pause()

    if IsFirstTime():
        LADY_TARBECK "{i}*Slurp!*{/i} Whatdhuyhuuthinkkhh!? {i}*Slurp!*{/i}"
        "I began to move faster, using her tits as nothing more than two soft toys for my amusement as her mouth sucked furiously."
        "She seemed to instinctively fuck like a veteran, her eyes wide with a vacant, doe-eyed look."
        TARBECK "... Gods."
        TARBECK "You look so good, my love."
        LADY_TARBECK "{i}*Slurp!*{/i} Thankhhh yhuuu!"
        LADY_TARBECK "Mhoreee! Ghivehhh mheee mhoreee!"
        "As her soft, delicate mouth continued to please me, I began to feel a growing need to paint the little slut white."
        "As she sensed my climax drawing near, it only seemed to encourage her more."
    else:
        LADY_TARBECK "{i}*Slurp!*{/i} Mokayhhh! Mmfghh!"
        "Lady Tarbeck's lips sucked furiously on the end of my cock as I fucked her huge, soft tits and warm mouth."
        "Any timidness was long gone by now. Lady Tarbeck was a woman with only one thing on her mind."
        "Pleasure."
        "Cock."
        "Sex."
        "Lady Tarbeck giggled and sucked like a veteran whore. Whatever change she had undergone... Well..."
        "There was certainly no timidness anymore."
        LADY_TARBECK "{i}*Slurp!* *Slurp!*{/i} Dhooo Ihh lhookhh ghoodhhh?"
        TARBECK "Yes dear, {i}You look incredible.{/i}"
        "As Lady Tarbeck continued, I felt the burning need to stuff her mouth with my heavy load, and watching her swallow became more and more overwhelming."
        "Until..."

    if CharIsVisiblyPreg("lady_tarbeck"):
        $ UnlockGalFlag("lady_tarbeck", "bimbotj", "var_rep_preg")
    else:
        $ UnlockGalFlag("lady_tarbeck", "bimbotj", "var_rep_nopreg")

    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "bimbotj")

    $ ReduceInfectionFromSex("lady_tarbeck")

    $ PlaySexFx(audio.kiara_bj_finish)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbotj_preg_cum
    else:
        scene lady_tarbeck_bimbotj_nopreg_cum
    with flash
    $ Pause()

    if IsFirstTime():
        "I let out a low rumble as I stuffed Lady Tarbeck's mouth with my load."
        "Her eyes widened as she juggled between giggling playfully and doing her best to swallow the load."
        LADY_TARBECK "Mmfghhh?!"
        TARBECK "... Gods, it's like watching a horse."
        "After pouring my load into her, I slowly pulled my cock out and gently lowered her back onto her feet."
    else:
        "I grunted in approval, slamming my cock between her tits as I pumped her mouth full of my cum."
        "Her eyes widened as her cheeks puffed out, and she did her best to swallow it down while squealing."
        LADY_TARBECK "Mmmfghh!! Shoo mhuchh!!"
        TARBECK "That's it dear, remember what we talked about!"
        TARBECK "Good girls always swallow!"
        "Slowly, after making sure she had suckled out every last drop, I withdrew my cock from her mouth."
    LADY_TARBECK @smile "Phew!"
    LADY_TARBECK @smile "Like, that was AMAZING!"
    if IsFirstTime():
        $ CharSetLover("lady_tarbeck")
    LADY_TARBECK @smile "Did I do good?! Did I? DID I?"
    TARBECK @blush "Y-Yes... You did very well."
    TARBECK @talk "Umm, perhaps you could give me and my wife some time to talk, [player_name]."
    TARBECK @talk "I'm sure we have much to discuss..."
    scene black with dissolve
    $ AutoMus(True)
    $ StopReplay()
    $ LocSet("hamun_dist_merch_lord")
    if IsFirstTime():
        $ QstSetProgress(RomanceLadyTarbeck, 6)
        $ QstSetDelay(RomanceLadyTarbeck, 1)
        $ NoteUnlock("tarbeck_rom_bimbo_return_later_again")
    else:
        $ SetRepeatVariant(False)
    $ LocEnter()



####################################################################################################
# Scene 6
# Journal note: 
# Two days later in-game, the scene auto triggers upon entering the Tarbeck Manor.
# Bimbo Lady Tarbeck should now be wearing clothes instead of naked.
label rom_tarbeck_bimbo_return_after_tf:
    $ NoteLock("tarbeck_rom_bimbo_return_later_again")
    show mc at cleft with easeinleft
    show lord_tarbeck at cright_f 
    show lady_tarbeck at right_f
    with easeinright
    TARBECK @talk "Ahh, you've arrived."
    LADY_TARBECK @smile "What do you think of my clothes?!"
    LADY_TARBECK @blush "I picked them myself, you know!"
    MC @shock "Very... {i}You.{/i}"
    LADY_TARBECK @blush2 "Teehee!"
    TARBECK @smile "Ahem... My wife and I have been talking and-"
    TARBECK @think "I must admit, this isn't quite what I was expecting."
    TARBECK @talk "But I cannot deny that she is happier."
    LADY_TARBECK @smile "UHUH! I'm like, REALLY happy!"
    TARBECK @talk "Thus, I was going to suggest the two of you-"
    LADY_TARBECK @blush "Like, this is a lot of talking."
    LADY_TARBECK @blush "Can I go upstairs and fuck [player_name] now, please?"
    TARBECK @shock "...!"
    TARBECK @smile "Yes dear, you can go upstairs and fuck him."
    LADY_TARBECK @smile "YAYYY!"
    LADY_TARBECK @smile "Like, I've wanted to do like, this since we first met!"
    LADY_TARBECK @blush "Not that the silly old me would have ever admitted it! Hehe!"
    MC @smile "Is that so?"
    scene black with dissolve
    "Lady Tarbeck reached out to take my hand, practically dragging me to the bedroom as Lord Tarbeck followed, bemused."
    $ LocSet("hamun_tarbeck_quarters_lady")
    "{i}... Not even ten minutes later.{/i}"

    label repeat_tarbeck_bimbo_miss:
    $ Pause(0.1)
    label replay_tarbeck_bimbo_miss:

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    $ PlaySexFx(audio.adara_hj_loop_x2, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbomiss_preg_idle
    else:
        scene lady_tarbeck_bimbomiss_nopreg_idle
    with dissolve
    $ Pause()

    if IsFirstTime():
        LADY_TARBECK "Darling... Are you watching?"
        LADY_TARBECK "This is like, so exciting and ROMANTIC!"
        LADY_TARBECK "Having you both here like this! Hehe!"
        TARBECK "Yes, dear, I'm watching..."
        "Lady Tarbeck's new body glistened in the light as I gently rubbed my cock against her body."
        "Her inviting, wet, tight pussy waited in anticipation of what was to come as she waited with her legs spread."
    else:
        LADY_TARBECK "Mhmm... Like, can we go shopping after this?"
        TARBECK "Whatever you want, my dear."
        "Lady Tarbeck's womanhood glistened excitedly as I rubbed my cock back and forth over her body."
        LADY_TARBECK "Ahh... I can't wait for him to stuff me with that thing again, hehe."
        LADY_TARBECK "...Oooh! Later, can I like, umm, watch you fuck some of the maids?"
        TARBECK "Whatever your heart desires, my love."
        LADY_TARBECK "Thank youuuuu..."
        LADY_TARBECK "Now watch me get stuffed good!"

    $ PlaySexFx(audio.forgean_075, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbomiss_preg_1
    else:
        scene lady_tarbeck_bimbomiss_nopreg_1
    with dissolve
    $ Pause()

    if IsFirstTime():
        "Lady Tarbeck's womanhood squeezed so tightly around me as I slowly slid my member into her; I thought I might have finished there and then."
        "Her pussy was almost {i}inhumanly{/i} tight as she let out a gasp."
        LADY_TARBECK "Ahhh...!"
        LADY_TARBECK "He feels so good in me! Mmfghh..."
        LADY_TARBECK "It's like my little hole was made just for him, hehe!"
        "Lord Tarbeck said nothing. He continued to watch, transfixed, as the huge member slowly entered into his wife."
        MC "Ahh... Gods, you feel incredible!"
        LADY_TARBECK "Like duhhh!"
        LADY_TARBECK "I'm your little fuck toy!"
        LADY_TARBECK "What kind of toy would I be if I wasn't fun to play with, silly?"
    else:
        LADY_TARBECK "MMmfmghhh...!"
        LADY_TARBECK "That feels soooo good!"
        "As my cock sank into Lady Tarbeck's pussy, it was as unbelievably tight as ever."
        "She giggled, watching the member disappear inside of her as her stomach lightly bulged with every thrust."
        LADY_TARBECK "AHH! Mess up my insides!"
        LADY_TARBECK "Look! Isn't that SOOO fun to watch?!"
        TARBECK "Y-Yes, dear."
        LADY_TARBECK "Ahhh! Stop being so gentle!"
        LADY_TARBECK "Fuck me harder! Stuff my pussy with your huge cock!"

    $ PlaySexFx(audio.forgean_100, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbomiss_preg_2
    else:
        scene lady_tarbeck_bimbomiss_nopreg_2
    with dissolve
    $ Pause()

    if IsFirstTime():
        "Possessed, I thrust faster into Lady Tarbeck as her moans grew louder."
        "Her womanhood still clung and squeezed around me as though her life depended on it."
        "And I found myself losing control as I fucked her senseless."
        LADY_TARBECK "Yes! That's it!"
        LADY_TARBECK "Harder! FUCK ME HARDER!"
        MC "(Gods, what is going on?!)"
        MC "(It's like a drug fucking her!)"
        SHYAHTAN "(Species previously experiencing fertility issues or a genetic resistance to our pheromones we artificially altered on some worlds.)"
        SHYAHTAN "(She is now built to breed... {i}with us.{/i})"
        SHYAHTAN "(Thus you may find the experience more... intense than usual.)"
        MC "(YOU CAN SAY THAT AGAIN!)"
        LADY_TARBECK "Hehe! I love the way your face strains!"
        LADY_TARBECK "I can just tell you're ready to like, fill me up!"
        LADY_TARBECK "Come on! Don't stop!"
        LADY_TARBECK "Fucking breed your little slut!"
        MC "F-Fuckk!"
    else:
        "Lady Tarbeck moaned hotly as my cock thrust faster into her."
        "Pounding away at her little pussy, increasingly lewd words came tumbling out of her mouth."
        LADY_TARBECK "Ahh! That's it!"
        LADY_TARBECK "Pound that little pussy! Fill my cunt up!"
        LADY_TARBECK "Ahh! Ahh! FUCK!!"
        LADY_TARBECK "I love it so muchh!!"
        LADY_TARBECK "I love being your little whore!"
        LADY_TARBECK "Your little breeding sow!"
        LADY_TARBECK "Are you watching, honey?"
        LADY_TARBECK "Are you watching him fill me up with his huge cock!"
        MC "F...Fuck...!"
        MC "(I'm hanging on for dear life here!)"
        MC "(Her pussy is incredible!)"
        TARBECK "Haha, yes, dear... I'm watching."
        "Suddenly, by some miracle, Lady Tarbeck's pussy tightened even further as she muttered sweetly, loud enough for us both to hear."
        LADY_TARBECK "Give me all your kittens!"
        LADY_TARBECK "Meowww!"
        "I didn't know whether to laugh or not, but before I could make the choice, my cock decided for me."

    if not IsFirstTime():
        $ PregRoll("lady_tarbeck")
        if CharIsVisiblyPreg("lady_tarbeck"):
            $ UnlockGalFlag("lady_tarbeck", "bimbomiss", "var_rep_preg")
        else:
            $ UnlockGalFlag("lady_tarbeck", "bimbomiss", "var_rep_nopreg")
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "bimbomiss")
    $ ReduceInfectionFromSex("lady_tarbeck")
    $ PlaySexFx(audio.forgean_finish)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbomiss_preg_cum
    else:
        scene lady_tarbeck_bimbomiss_nopreg_cum
    with flash
    $ Pause()

    if IsFirstTime():
        MC "HRGHHH...!"
        "Every muscle tightened in my body as I buried my cock into Lady Tarbeck and flooded her womb with my seed."
        "Her mouth opened as a breathless gasp escaped her parted lips."
        "And I felt her tighten around me too."
        LADY_TARBECK "Oooooh...!"
        LADY_TARBECK "Mhmm... Phew!"
        LADY_TARBECK "Now I'm all stuffed! Haha!"
        LADY_TARBECK "Thanks for the cum!"
        scene black with dissolve
        $ AutoMus(True)
        $ StopReplay()
        "Slowly, I rose back to my feet. For the first time,"
        "I thought {i}my{/i} legs would give out as Lady Tarbeck sprang back to her feet."
        $ LocFlush()
        show mc at cleft
        show lord_tarbeck at right_f
        show lady_tarbeck at cright_f
        with dissolve
        LADY_TARBECK @smile "That was AMAZING!"
        LADY_TARBECK @blush "You should, umm, come back, like, real soon!"
        LADY_TARBECK @smile "Why don't you just join us for breakfast tomorrow?"
        MC @smile "My lady, it would depend on the time. I'm normally quite busy."
        LADY_TARBECK @sad "Booooo!"
        LADY_TARBECK @blush "I pwomiseee I'll make it worth your timeee..."
        "Lord Tarbeck raised a brow as he smirked."
        TARBECK @smile "You are welcome to join us, of course, but please, don't rush on account of my wife's... {i}eagerness.{/i}"
        LADY_TARBECK @smile "Hehe, see you soon, [player_name]."
        scene black with dissolve
        $ LocSet("hamun_dist_merch_lord")
        $ NoteUnlock("tarbeck_rom_bimbo_join_breakfast")
        $ QstSetProgress(RomanceLadyTarbeck, 7)
        $ QstSetDelay(RomanceLadyTarbeck, 1)
        $ QstSetProgress(HouseLockTarbeckHouse, 2)
        $ LocEnter()
    else:
        LADY_TARBECK "Hehe, he's feeding my kitty downstairs so much milk!"
        LADY_TARBECK "Give me every drop!"
        "My body tightened up as I grunted, pouring my thick load into Lady Tarbeck as she moaned hotly."
        "I felt her body tighten and tremble instinctively around me as her lips parted."
        LADY_TARBECK "Ooooh... That's it... Mhmm... Fill me up, hehe."
        MC "(Gods, she really was built to drain me!)"
        scene black with dissolve
        $ AutoMus(True)
        $ StopReplay()
        LADY_TARBECK "Can we, umm, go shopping now?"
        TARBECK "Of course, dear."
        LADY_TARBECK "Yayy!"
        LADY_TARBECK "You just stay here and recover, hehe."
        LADY_TARBECK "But be warned... If you're still here when I get back, I'm draining you again!"
        MC "(Gods have mercy upon me.)"
        $ LocSet("hamun_dist_merch_lord")
        $ SetRepeatVariant(False)
        $ LocEnter()


#########################################################################################################
# One day later - scene auto triggers upon entering the dining hall of the Tarbeck Manor in the morning.
label rom_tarbeck_bimbo_join_breakfast:
    show mc at cleft with easeinleft
    $ NoteLock("tarbeck_rom_bimbo_join_breakfast")
    show lady_tarbeck at center_f with easeinright
    "As I entered the dining hall, an ecstatic Lady Tarbeck rose from her seat and practically flung herself into my arms."
    LADY_TARBECK @smile "YOU CAME! YOU CAME!"
    show lord_tarbeck at cright_f with easeinright
    TARBECK @smile "Good morning, I'll have some fruit and bread brought out for you if you're joining us."
    MC @smile "Thank you."
    scene black with dissolve
    "For the next twenty minutes, I ate the exotic fruit and food brought out to me as Lady Tarbeck laughed and rubbed at my thigh."
    "It was strange, things seemed almost... normal?"

    $ LocFlush()
    show mc at left
    show lady_tarbeck at cleft
    show lord_tarbeck at cright_f
    with dissolve

    LADY_TARBECK @smile "So then, we had two of the maids present themselves to the monster thingy downstairs, and it was SOOOO fun to watch!"
    TARBECK @smile "Yes, yes, it was most enjoyable."
    TARBECK @smile "My wife has developed appetites that could rival even mine, it seems."
    LADY_TARBECK @blush "Uhuh, and speaking of 'appetites' and stuff."
    "Lady Tarbeck's hand reached over to grab at my cock through the fabric."
    LADY_TARBECK @blush "Come give me some dessert."
    TARBECK @smile "This horny already in the morning?"
    LADY_TARBECK @blush "Uhuh, and I can feel how hard you are."
    LADY_TARBECK @blush "Come on, don't keep me waiting."
    MC @smile "Alright, let's head up to your room and-"
    LADY_TARBECK @angry "No chance!"
    LADY_TARBECK @blush "Not when we have a perfectly good table to fuck on!"
    MC @shock "... Oh!"

    label repeat_tarbeck_bimbo_breakfast:
    scene black with dissolve
    $ Pause(0.1)

    label replay_tarbeck_bimbo_breakfast:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbobreakfast_preg_idle
    else:
        scene lady_tarbeck_bimbobreakfast_nopreg_idle
    with dissolve
    $ Pause()

    if IsFirstTime():
        LADY_TARBECK "Ahh! That's it!"
        LADY_TARBECK "Rub that huge cock on my fat ass!"
        "Lady Tarbeck laughed as I slapped my cock on her round, juicy ass, gliding it back and forth as she wiggled her butt enticingly."
        LADY_TARBECK "Haha! That feels amazing! Mmfghh..."
        LADY_TARBECK "You should just like, stay here ALL THE TIME and we could like, FUCK every day!"
        TARBECK "Dear... We discussed this, he's with the Adventurers' Guild, he can't just-"
        LADY_TARBECK "NU UH!"
        LADY_TARBECK "Like urghh, forget all these dumb rules and just fuck me already!"
    else:
        LADY_TARBECK "Teehee! I knew you like, wouldn't stay away for long!"
        LADY_TARBECK "Who has time to be a big, dumb adventurer when I have a perfectly fat ass needing fucked?"
        MC "You have such a way with words..."
        LADY_TARBECK "Like, thanks!"
        "With my cock slapped on her soft, bubbly ass, she wiggled it playfully as I gently rubbed against her."
        LADY_TARBECK "Come on, come onnnn!"
        LADY_TARBECK "Stop teasing and put it in already!"

    $ PlaySexFx(audio.nijah_miss_1, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbobreakfast_preg_vag_1
    else:
        scene lady_tarbeck_bimbobreakfast_nopreg_vag_1
    with dissolve
    $ Pause()

    if IsFirstTime():
        "Lady Tarbeck moaned as she felt the member sink into her."
        LADY_TARBECK "Oooooh...!"
        LADY_TARBECK "It's like, soooo biggg!"
        LADY_TARBECK "Mmffghh! Now THIS is the kind of breakfast I want to wake up to!"
        TARBECK "Don't make too much of a mess, dear."
        TARBECK "We have an event to go to later."
        "Lady Tarbeck wiggled her ass playfully, doing her best to bounce her round butt and match my rhythm."
        LADY_TARBECK "Yes dear, Mmmfghh!"
        LADY_TARBECK "Ahh! Fuck me! FUCK ME HARDER!"
    else:
        "Lady Tarbeck wiggled her butt back onto my cock as she felt my member sink into her womanhood."
        LADY_TARBECK "Ahhh...!"
        LADY_TARBECK "N-Nice and snug stuffed in me! Hehe!"
        "As I began to fuck her, her tits swayed back and forth as her tight pussy squeezed around me."
        LADY_TARBECK "Teehee! He's so naughty with me!"
        LADY_TARBECK "He just can't keep away!"
        TARBECK "Who could resist, my love?"
        LADY_TARBECK "Nawww! That's so SWEET!"
        LADY_TARBECK "Isn't he like, really sweet, [player_name]?"
        MC "{i}*Huff*{/i} I couldn't care less right now!"
        LADY_TARBECK "Mmmfghh... Of course!"
        LADY_TARBECK "Go on, fuck me! FUCK ME SILLY WITH YOUR HUGE COCK!"

    $ PlaySexFx(audio.nijah_miss_2, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbobreakfast_preg_vag_2
    else:
        scene lady_tarbeck_bimbobreakfast_nopreg_vag_2
    with dissolve
    $ Pause()
    
    if IsFirstTime():
        "Grabbing her hair, I began to slam into Lady Tarbeck from behind as her moans increased."
        "It seemed even she was now struggling to control herself as she squirmed in my grasp."
        LADY_TARBECK "Ah! Ah! THAT'S IT!"
        LADY_TARBECK "OH FUCK! HE'S POUNDING ME SO GOOD!"
        LADY_TARBECK "Are you watching, honey?!"
        LADY_TARBECK "He's going to ruin my poor little pussy! Hehe!"
        "Her tight cunt squeezed desperately around me as her ass bounced with every movement."
        "Lord Tarbeck sat and watched curiously as his wife's huge tits swayed with every thrust."
        MC "Hrghh...! I'm getting close!"
        LADY_TARBECK "Like, me toooo!"
        LADY_TARBECK "ME TOOO!!"
        LADY_TARBECK "Ahh!! Do it! Slam that big cock in me!"
        LADY_TARBECK "Don't stop until you fill my little pussy up!"
        LADY_TARBECK "I want it! I want it so-"
    else:
        "Once more grabbing a fistful of her hair, I pounded Lady Tarbeck's round, fat rear from behind."
        "Her moans became louder as I watched the fat of her ass push and jiggle with every thrust,"
        "the lewd sounds of {i}*Phap!* *Phap!* *Phap!*{/i} filling the dining hall."
        LADY_TARBECK "F-FUCK YESS!"
        LADY_TARBECK "Pound my pussy! FUCK ME HARDER PLEASE!"
        "Her huge tits swung back and forth, the jewelry on the ends of her tits lightly jingling as she moaned."
        LADY_TARBECK "C-Come on...! Mmfghh!"
        LADY_TARBECK "I c-can feel you throbbing in me!"
        LADY_TARBECK "Give it to me!"
        "Her tight cunt gripped me with desperation."
        LADY_TARBECK "Fill me up! MAKE ME CARRY YOUR BABIES!"

    if not IsFirstTime():
        $ PregRoll("lady_tarbeck")
        if CharIsVisiblyPreg("lady_tarbeck"):
            $ UnlockGalFlag("lady_tarbeck", "bimbobreakfast", "var_rep_preg_vag")
        else:
            $ UnlockGalFlag("lady_tarbeck", "bimbobreakfast", "var_rep_nopreg_vag")

    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "bimbobreakfast")
    $ ReduceInfectionFromSex("lady_tarbeck")
    $ PlaySexFx(audio.nijah_miss_finish)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbobreakfast_preg_vag_cum
    else:
        scene lady_tarbeck_bimbobreakfast_nopreg_vag_cum
    with flash
    $ Pause()

    if IsFirstTime():
        "I grunted, pulling Lady Tarbeck's head back as I buried my cock deep, flooding her welcoming, needy hole with enough cum to leave her satisfied."
        MC "Grghhh... Fuck!"
        LADY_TARBECK "Oooooooooooooooooh...!"
        LADY_TARBECK "It feelssss shooooo ghooodhhh!"
        LADY_TARBECK "Mmfghhh... I'm a little cum addict for you! Haha!"
        "After making sure I had given her my fill, I slowly and carefully began to pull my cock out from her still desperately tight hole."
        scene black with dissolve
        stop music fadeout 1.0
        $ AutoMus(True)
        $ StopReplay()
        "{i}*POP!*{/i}"
        LADY_TARBECK "Nooooo... Put it back! PUT IT BACK RIGHT WHERE IT BELONGS!"
        TARBECK "Dear... Perhaps you should not spend {i}all{/i} day fucking?"
        LADY_TARBECK "Hmphh!"
        $ LocSet("hamun_tarbeck_mainhall")
        $ LocFlush()
        show lady_tarbeck at cright_f
        show lord_tarbeck at right_f
        show mc at cleft
        with dissolve
        LADY_TARBECK @smile "Phew!"
        LADY_TARBECK @smile "That felt great!"
        LADY_TARBECK @talk "Oh, we're throwing a little party tonight."
        LADY_TARBECK @talk "It's like, REALLY important and stuff!"
        MC @think "Is it?"
        LADY_TARBECK @smile "Mhmm! Like, we're going to show off my new body and stuff!"
        LADY_TARBECK @blush "I'd really, {i}really{/i} like you to come so we can fuck!"
        LADY_TARBECK @smile "It'll be like, a really fun way to let everyone know things are different around here now!"
        TARBECK @talk "Yes, do feel free to come."
        TARBECK @smile "But as that... other, monster form you take."
        TARBECK @smile "My guests love a spectacle, as you know."
        MC @smile "I will see what I can do..."
        $ NoteUnlock("tarbeck_rom_bimbo_party")
        LADY_TARBECK @smile "HOORAY!"
        LADY_TARBECK @smile "See you later!"
        scene black with dissolve
        $ LocSet("hamun_dist_merch_lord")
        $ QstSetProgress(RomanceLadyTarbeck, 8)
        $ LocEnter()
    else:
        "Lady Tarbeck gasped as she felt the splash of hot seed once again pour into her welcoming womb."
        MC "GRGHHH!!"
        LADY_TARBECK "Mmmmfghhhhhhh...!!"
        LADY_TARBECK "I can feel all your cum splashing about inside of me!"
        LADY_TARBECK "Honey! Did you see? He's filled me up SOOO MUCH!!"
        TARBECK "Very good, dear, now clean up before we leave."
        TARBECK "You know I can't have cum seeping out of you during meetings."
        LADY_TARBECK "Hehe, yes darling."
        scene black with dissolve
        stop music fadeout 1.0
        $ AutoMus(True)
        $ StopReplay()
        $ LocEnter()



#######################################################################################
# Scene 7
# Triggered automatically upon entering the Tarbeck Manor main hall in the EVENING (can trigger the same night as Scene 6 after its completion).
# Show Tarbeck Manor party hall BG with guests.
label rom_tarbeck_bimbo_party:
    if RomanceLadyTarbeck().Romance_ScheduledGig == "bimboparty":
        $ RomanceLadyTarbeck().Romance_ScheduledGig = None
        $ SetRepeatVariant(True)
        $ NoteLock("tarbeck_rom_bimbo_party")
        $ RomanceLadyTarbeck().HadSexToday = True

    if IsFirstTime():
        $ NoteLock("tarbeck_rom_bimbo_party")
        show mc at cleft with easeinleft
        show lady_tarbeck at cright_f with easeinright
        LADY_TARBECK @smile "Yayyy! You made it!"
        MC @smile "Lady Tarbeck."
        LADY_TARBECK @blush "I'm so glad you're here!"
        LADY_TARBECK @blush2 "Like, it's time for us to put on a show and stuff!"
        MC @think "Uhh... What did you have in mind?"
        "Lady Tarbeck reached out and grabbed my hand."
        LADY_TARBECK @smile "Come with me! Lord Tarbeck is already tied up!"
        hide mc
        hide lady_tarbeck
        with easeoutright
        MC "Wait! What do you have planned exactly?!"
        scene black with dissolve
        "{i}Twenty frantic minutes later and a lot of lipstick.{/i}"
    else:
        show mc at cleft with easeinleft
        show lady_tarbeck at cright_f with easeinright
        LADY_TARBECK @smile "OOOH! You came!"
        LADY_TARBECK @smile "Come on! I want you to fuck me silly in front of everyone again!"
        "Lady Tarbeck grabbed my hand as she dragged me away."
        hide mc
        hide lady_tarbeck
        with easeoutright
        LADY_TARBECK "Honey! We're tying you up again! Hehe!"
        scene black with dissolve
        TARBECK "{i}*Sigh*{/i} Of course, you little tease..."
        "{i}... Fifteen minutes later.{/i}"

    label replay_tarbeck_bimbo_party:

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimboparty_preg_idle
    else:
        scene lady_tarbeck_bimboparty_nopreg_idle
    with dissolve
    $ Pause()

    if IsFirstTime():
        "The crowd gasped and watched as the once pious and pure Lady Tarbeck,"
        "now stacked with the body of the most delectable of whores, rubbed her fat ass against the cock of a monster,"
        "the fabled {i}saviour of Hamun,{/i} giggling as she'd covered herself with increasingly lewd markings over her body."
        GUEST "Is that Lady Tarbeck?!"
        GUEST_2 "Oh my... I never knew she had it in her!"
        LADY_TARBECK "Welcome everyone!"
        LADY_TARBECK "As you can see! My husband is a little tied up tonight!"
        LADY_TARBECK "And while he's used to fucking most of you, tonight, he's gonna be a little cuck for me! Hehe!"
        "The crowd giggled and murmured. After all, this was Lord Tarbeck."
        LADY_TARBECK "ANYWAY! As you can see from his big, huge cock rubbing against my pussy,"
        LADY_TARBECK "I'm gonna do my bestest to take his cock and have ALLL his babies from now on!"
        "You could almost hear a pin drop. The crowd was used to debauchery, to spectacle, but this..."
        "And Lady Tarbeck no less!"
        LADY_TARBECK "Anyway! Like, your job is to all fuck like crazy!"
        LADY_TARBECK "Because what's an orgy without friends!"
    else:
        LADY_TARBECK "Welcome back everyone!"
        "The crowd clapped and cheered as I rubbed my cock against her wet, inviting hole."
        LADY_TARBECK "Mmmfghh... Given how umm, successful and stuff the last party was,"
        LADY_TARBECK "We decided now was a good time for a repeat!"
        LADY_TARBECK "So like, while I fuck Mr. Monster Cock here! Have fun everyone!"
        "The crowd laughed as Lord Tarbeck struggled weakly against his restraints."
        TARBECK "Someone take the blindfold off so I can see, damn it!"
        LADY_TARBECK "NU-UH, you just get to listen, dear! Hehe!"

    $ PlaySexFx(audio.nijah_doggy_loop2, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimboparty_preg_1
    else:
        scene lady_tarbeck_bimboparty_nopreg_1
    with dissolve
    $ Pause()
    
    if IsFirstTime():
        "My cock pushed into her soaking pussy with ease."
        LADY_TARBECK "Oh FUCK!"
        LADY_TARBECK "Ahh! He's in me! Oooh!"
        LADY_TARBECK "He's so big stretching my little pussy!"
        "The crowd watched excitedly, and slowly the room began to descend into a full-blown orgy right there on the floor."
        "The men fondled the women who sipped at their wine, watching in a mixture of awe and excitement as the principled Lady Tarbeck now literally let a monster ravage her willingly."
        "Soon, women were on their knees, sucking cock, or even lifting their skirts as eager, excited couples began to fuck then and there."
        LADY_TARBECK "Ahhh! Isn't this wonderful, dear?"
        LADY_TARBECK "Everyone is getting on so well!"
        TARBECK "T-That's wonderful, dear! Umm..."
        TARBECK "Could you remove the blindfold so I might see some of the entertainment?"
        TARBECK "... Darling?"
        TARBECK "Are you still there?"
    else:
        "Lady Tarbeck moaned as my cock pushed into her willing meat hole once more."
        LADY_TARBECK "Mmmfghh!"
        LADY_TARBECK "Ahh! You ladies should like- Mmfghh! Fuck him too sometime!"
        LADY_TARBECK "Like, his cock feels like it could re-arrange my insides every time!"
        "The crowd by now was already familiar with the routine,"
        "fondling between eager couples soon turned into a full-blown orgy right there."
        LADY_TARBECK "Ahh! Harder, [player_name]!"
        LADY_TARBECK "I want them all to know I'm the luckiest girl in the room!"
        LADY_TARBECK "Give it to your little bitch harder!"

    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimboparty_preg_2
    else:
        scene lady_tarbeck_bimboparty_nopreg_2
    with dissolve
    $ Pause()

    if IsFirstTime():
        LADY_TARBECK "Ahh! Harder! HARDER!"
        LADY_TARBECK "Show everyone why I'm your little breeding sow!"
        "By now, few people were hardly even paying attention to us,"
        "we were just another pair of participants, fucking intensely in the grand hall."
        "Her tight cunt squeezed excitedly around me as I slammed my cock deep,"
        "{i}she enjoyed having an audience...{/i}"
        TARBECK "C-Come on! Someone release me!"
        TARBECK "I CAN SMELL ALL THE PUSSY FROM HERE!"
        TARBECK "D-Darling! Let me out so I can have some fun too!"
        LADY_TARBECK "Ahh! You have enough wenches most nights!"
        LADY_TARBECK "This is- Mmfghh! MY NIGHT!"
        "As I continued to pound away at her hole relentlessly,"
        "she dug her nails into me as tightly as possible as her eyes rolled back."
        LADY_TARBECK "Cum in me! CUM IN ME! CUM IN-"
    else:
        LADY_TARBECK "AHHHH!"
        LADY_TARBECK "I'M SORRY DEAR! I CAN'T FOCUS RIGHT NOW!"
        LADY_TARBECK "HE'S FUCKING ME SO HARD! Mnmmfghh!"
        "I continued to slam away at Lady Tarbeck's tight, wonderful cunt as the party continued to devolve into full-blown debauchery."
        MC "You like it, don't you?"
        MC "Letting them see me take you like this."
        LADY_TARBECK "It's shoooo ghoodhhhh! Mmfghh!"
        LADY_TARBECK "I love it! I want everyone to see you fuck me all the time!"
        LADY_TARBECK "You should just be able to rip my dress off and fuck me in the street in front of everyone whenever you want!"
        MC "Hrghh! Gods willing, girl, I will!"
        LADY_TARBECK "I can f-feel your big heavy balls slam up against my little pussy!"
        LADY_TARBECK "It's incredible! Please... AHH!"
        LADY_TARBECK "C-Cum in me! Don't stop till you fill me up!"
        "Her nails dug as tightly as they could into me as she trembled, her eyes rolling up as she squirmed."
        LADY_TARBECK "BREED MEEEE!"

    if not IsFirstTime():
        $ PregRoll("lady_tarbeck")
        if CharIsVisiblyPreg("lady_tarbeck"):
            $ UnlockGalFlag("lady_tarbeck", "bimboparty", "var_rep_preg")
        else:
            $ UnlockGalFlag("lady_tarbeck", "bimboparty", "var_rep_nopreg")
    $ UnlockGalSceneAndGrantXp("lady_tarbeck", "bimboparty")
    $ ReduceInfectionFromSex("lady_tarbeck")
    $ PlaySexFx(audio.nijah_doggy_finish)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimboparty_preg_cum
    else:
        scene lady_tarbeck_bimboparty_nopreg_cum
    with flash
    $ Pause()

    if IsFirstTime():
        "As she felt the splash of thick warmth entering her,"
        "Lady Tarbeck's pussy tightened around me as I felt her climax,"
        "her legs and body squeezing as she whimpered weakly."
        LADY_TARBECK "Mmmfghh...!"
        "I held her up for a few moments, letting the intense wave pass before lowering her carefully to the floor."
        "Her legs shook as my cum seeped down from her."
        scene black with dissolve
        $ AutoMus(True)
        $ StopReplay()
        $ LocFlush()
        show mc at cleft
        show lady_tarbeck at cright_f
        with dissolve
        LADY_TARBECK @smile "That was incredibleeee!"
        MC @talk "I'm glad you enjoyed yourself, my lady."
        LADY_TARBECK @smile "I'm going to go lay down in my room for a bit, my legs are all shaky after that!"
        MC @smile "Do you need me to escort you?"
        LADY_TARBECK @blush "Mmm, tempting... But I'm all stuffed!"
        LADY_TARBECK @blush2 "... T-Thank you for helping me do all this."
        LADY_TARBECK @blush "I've never been happier."
        MC @smile "That's wonderful to hear."
        "Lady Tarbeck reached out to take my hand."
        LADY_TARBECK @smile "I want you to come see me whenever you want."
        LADY_TARBECK @blush2 "And... I want you to know, I might be Lord Tarbeck's wife."
        LADY_TARBECK @blush2 "But I'm definitely your girl, alright?"
        LADY_TARBECK @blush "Like, I really, really love you..."
        MC @shock "... Lady Tarbeck."
        LADY_TARBECK @blush "And not just because of that delicious, massive thing dangling between your thighs."
        MC @smile "Ah."
        LADY_TARBECK @smile "Well, I'm gonna go get some rest."
        LADY_TARBECK @smile "Goodnight, handsome!"
        MC @smile "Goodnight, Lady Tarbeck."
        hide lady_tarbeck with dissolve
        "I watched Lady Tarbeck's fat ass, still dripping with my seed, sway back and forth as she ascended the stairs towards her private quarters."
        show mc at center with ease
        MC "(I suppose now would be a good time to take my own leave.)"
        show mc at blurin, center_f
        $ Pause(0.1)
        hide mc with easeoutleft

        TARBECK "... Umm, hello?"
        TARBECK "Could someone at least take the blindfold off?"
        TARBECK "...Hellooooo?"
        scene black with dissolve
        $ QstSetProgress(RomanceLadyTarbeck, 9)
        $ QstSetProgress(HouseLockTarbeckHouse, 5)    
    else:
        "I held onto Lady Tarbeck as tightly as I could, pouring my thick load into her welcoming, tight hole."
        "She gasped, trembling softly as she felt the splash of seed now fill up her womb."
        LADY_TARBECK "Mmmmfghh! G-Godsss...!"
        "I held onto her tightly as her legs began to buckle beneath her, letting the wave of pleasure pass."
        LADY_TARBECK "{i}*Huff*{/i} I love you... I love you, I love you, I LOVE YOU!"
        scene black with dissolve
        $ AutoMus(True)
        $ LocFlush()
        show mc at cleft
        show lady_tarbeck at cright_f
        with dissolve
        MC "My lady, what should I do now?"
        LADY_TARBECK "Mmmfghh... Carry me to my bed, I need some sleepy time after that."
        MC "And your husband?"
        LADY_TARBECK "I'll rescue him in the morning... Hehe."
        hide mc
        hide lady_tarbeck
        with dissolve
        "I did as Lady Tarbeck asked, placing the cute, curvy ditz down onto her bed as she drifted off to sleep, snoring almost immediately."
        $ Pause(0.2)
        show mc at center_f with easeinright
        MC "(... Cute.)"
        scene black with dissolve
        "And with that, I left the manor as the orgy continued around me obliviously."
        TARBECK "... Umm? Hello? Is there anyone going to let me down?"
        TARBECK "Hellooooo!"
        $ SetRepeatVariant(False)
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()



label rom_tarbeck_bimbo_breakfast_anal:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbobreakfast_preg_idle
    else:
        scene lady_tarbeck_bimbobreakfast_nopreg_idle
    with dissolve
    $ Pause()

    "Lady Tarbeck, once more bent over the table, wiggled her butt enticingly towards me."
    "With my cock wedged between her fat ass cheeks, she giggled playfully as I began to slide it back and forth teasingly."
    "Her asshole, still tight but glistening from whatever lube she had applied, winked at me."
    LADY_TARBECK "Are you ready?"
    LADY_TARBECK "Ready to fuck my tight, fat ass?"
    MC "As my cock brushed up against her sphincter, it sent a wave of pleasure through me as I stared at the little brown hole in anticipation."
    LADY_TARBECK "Mhmm, are you watching, dear?"
    LADY_TARBECK "I'm finally ready to take things up the butt, just like you always wanted!"
    TARBECK "Well, yes, but I always did think it would be my-"

    $ PlaySexFx(audio.nijah_miss_1, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbobreakfast_preg_anal_1
    else:
        scene lady_tarbeck_bimbobreakfast_nopreg_anal_1
    with dissolve
    $ Pause()

    "As my cock pushed up against her sphincter, her tight little hole spread as it forced an inch inside of her, and then another, until..."
    LADY_TARBECK "OOOOOOOOH...!"
    LADY_TARBECK "He's in my butt! Mmfghh!"
    LADY_TARBECK "G-Gods! It feels SOOOOOOO good to have him stuff me back there! Hehe!"
    "Her ass was incredibly tight, gripping around my cock as I began to push up against her soft, plump rear."
    "The fat jiggled slightly with every thrust as I buried my member deep inside her."
    LADY_TARBECK "Ahhh...! Do you like my butt?"
    LADY_TARBECK "I can feel how h-hard you are back there!"
    MC "Your ass feels incredible!"
    LADY_TARBECK "Mmm, this butt belongs to you!"
    LADY_TARBECK "Ahh! I LOVE IT!"
    LADY_TARBECK "It feels SOOOO good!"
    MC "(Most women usually need breaking in back here!)"
    MC "(There are lifelong courtesans who struggle more than this!)"
    LADY_TARBECK "Fuck my ass! PULL MY HAIR AND FUCK MY ASS HARDER!"

    $ PlaySexFx(audio.nijah_miss_2, 1)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbobreakfast_preg_anal_2
    else:
        scene lady_tarbeck_bimbobreakfast_nopreg_anal_2
    with dissolve
    $ Pause()

    "Grabbing hold of her hair, I began to slam my cock into her tight ass from behind as she moaned hotly."
    "The table banged with every thrust as the room filled with the sounds of Lady Tarbeck's ass bouncing against me as I buried my cock to the hilt."
    LADY_TARBECK "OH FUCK YES!"
    LADY_TARBECK "THAT'S IT! MMFGHH!"
    LADY_TARBECK "MY ASS WAS MEANT TO TAKE YOUR COCK!"
    "I grunted like an animal, her skin glistening in the light as I continued to have my way with her."
    "Her tight ass indeed was built to take my cock..."
    "And I was going to ensure her tight little rear drained my cock dry as I filled her bowels."
    LADY_TARBECK "Oooooooh!"
    LADY_TARBECK "I love it! I love feeling your huge cock mess up my poor little ass!"
    LADY_TARBECK "A-Ahh..! I'm such a little anal slut!"
    MC "Grghh! Are you ready?"
    MC "I'm g-getting close! Hrghh!"
    LADY_TARBECK "Do it! Do it! DO IT!"

    if CharIsVisiblyPreg("lady_tarbeck"):
        $ UnlockGalFlag("lady_tarbeck", "bimbobreakfast", "var_rep_preg_anal")
    else:
        $ UnlockGalFlag("lady_tarbeck", "bimbobreakfast", "var_rep_nopreg_anal")

    $ ReduceInfectionFromSex("lady_tarbeck")

    $ PlaySexFx(audio.nijah_miss_finish)
    if CharIsVisiblyPreg("lady_tarbeck"):
        scene lady_tarbeck_bimbobreakfast_preg_anal_cum
    else:
        scene lady_tarbeck_bimbobreakfast_nopreg_anal_cum
    with flash
    $ Pause()

    "As my balls slapped against her clit, I buried my cock deep into her ass and squeezed one of her ass cheeks tightly."
    "I grunted with gritted teeth, flooding her rear as Lady Tarbeck let out a loud moan."
    LADY_TARBECK "OOOOOOOH! SHOO MHUCHHH!! Mfghhhh...!"
    "As I filled her ass with cum, Lady Tarbeck trembled, her legs slightly buckling as she laughed."
    LADY_TARBECK "Ha-ha! It feels so creamy back there now! Mmfghh!"
    LADY_TARBECK "I'm like, not gonna be able to sit down properly for a while!"
    TARBECK "I'll be sure to order some extra cushions to your quarters, dear."
    LADY_TARBECK "Thank youuu..."
    LADY_TARBECK "My poor little stretched butt will need them! Hehe!"
    scene black with dissolve
    stop music fadeout 1.0
    $ StopSexFx()
    $ AutoMus(True)
    $ StopReplay()
    $ SetRepeatVariant(False)
    $ LocEnter()
