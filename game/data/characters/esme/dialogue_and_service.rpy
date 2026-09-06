init python:
    @AppendToAllQuests
    class DialogueEsme(LogicModule):
        def onEnter(self):  
            if GetLocID() == "hamun_brothel":
                if self.progress == 0:
                    return TriggeredEvent("hamun_brothel_esme_firstmeet")

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_brothel":
                btnMods["btn_hamun_brothel_esme_talk"] = BtnJumpLabel(_("Talk to Esme"), "hamun_brothel_esme_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("esme_root", DNode(_("I am interested in your services, Esme."), "hamun_brothel_esme_price_rep"))
            yield ("esme_root", DNode(_("Do only katai work here?"), "hamun_brothel_esme_onlykatai"))

            yield ("esme_root", DNode(_("I should go."), "hamun_brothel_esme_bye", nextNode = "DNodeExit", order = -100))

############################
# The player enters the brothel
label hamun_brothel_esme_firstmeet:
    $ QstSetProgress(DialogueEsme, 1)
    show esme at cright_f 
    with dissolve
    show mc at cleft with easeinleft
    ESME @smile "Welcome to the Kitten's Paw."
    "The katai woman gestured toward herself with a coy smile."
    ESME @lewd "I'm Esme. What pleasures can I offer you tonight?"
    $ CharMeet("esme")
    "Her eyes widened slightly, lips curling into a knowing grin."
    ESME @smile "Well, well... I see we have a celebrity among us tonight."
    MC @think "What?"
    ESME "{i}The Beast of Novaras himself, gracing our humble halls.{/i}"
    "My eyes widened in shock. Esme giggled again, clearly enjoying my reaction."
    MC @surprised "W-What did you just call me?"
    ESME @laugh "Weren't you aware? Posters of you are everywhere."
    ESME @smile "I doubt there's a single soul in Novaras who hasn't heard of {i}the Slayer of the Demorai.{/i}"
    MC @surprised "Slayer...?"
    "She shrugged nonchalantly."
    ESME "Some think you're a hero. Others... just another monster."
    "Her eyes wandered slowly over my body, pupils dilated with interest."
    ESME @lewd "{i}...But you look like quite the man to me.{/i}"
    ESME @smile "So... how about it, {i}hero?{/i}"
    menu hamun_brothel_esme_firstmeet_menu:
        "How much?":
            jump hamun_brothel_esme_price_firsttime
        "Do only katai work here?":
            call hamun_brothel_esme_onlykatai from _call_hamun_brothel_esme_onlykatai
            jump hamun_brothel_esme_firstmeet_menu
        "Perhaps another time.":
            ESME @lewd "As you wish, {i}beast{/i}."
            $ LocEnter()

label hamun_brothel_esme_bye:
    ESME @smile "See you around, handsome!"
    $ LocEnter()

label hamun_brothel_esme_talk:
    show esme at center with dissolve
    ESME @smile "Hi there, {i}beast{/i}!"
    ESME @smile "Looking for some fun?"
    call processDialogue("esme_root") from _call_processDialogue_56
    $ LocEnter()

label hamun_brothel_esme_onlykatai:
    ESME @smile "Mmm, yes. Only katai here."
    MC @think "Are katai girls more popular in Hamun?"
    ESME @laugh "Haha, no more than human girls, honestly."
    MC @think "Then why—"
    ESME @sad "The life of a katai is either to remain in the Tribelands, or to strike out as a merchant."
    ESME "Many girls come seeking seas of coin... only to find the dream is a lie."
    ESME @smile "So... I offer them another way."
    MC @think "You run this place?"
    MC @surprised "And you... Tend to clients as well?"
    ESME @laugh "If I enjoy the company of a client, why not?"
    ESME @lewd "Hardly seems fair my girls get to have all the fun, doesn't it?"
    return

label hamun_brothel_esme_price_firsttime:
    ESME @smile "For you? A special offer."
    ESME "Six hundred coins, and I'm alllll yours."
    ESME "A thousand... if you want to put it in my ass."
    "Esme gently trailed her tail across my crotch."
    ESME @lewd "Believe me... I'm worth every. Single. Coin."
    "The voluptuous katai licked her lips enticingly and purred."
    menu:
        "I want you... and your ass." (Req_Gold = 1000):
            $ PlayerRemItem("gold", 1000)
            "Esme raised a brow, intrigued."
            ESME @smile "My ass, hmm?"
            ESME "Coin first, lover."
            "Esme holds out her hands, and once I place the bag of coins into her posession, she grins."
            ESME @lewd "Now {i}this{/i} is going to be interesting..."
            call hamun_brothel_esme_shared_setup from _call_hamun_brothel_esme_shared_setup
            jump hamun_brothel_esme_anal
        
        "I want you." (Req_Gold = 600):
            $ PlayerRemItem("gold", 600)
            call hamun_brothel_esme_shared_setup from _call_hamun_brothel_esme_shared_setup_1
            jump hamun_brothel_esme_vaginal

        "Another time, perhaps.":
            ESME @sad "Mmm... what a shame."
            ESME "I'll be waiting... {i}beast{/i}."
            $ LocEnter()

label hamun_brothel_esme_shared_setup:
    "Esme, licking her lips, took hold of my hand."
    ESME @lewd "Right this way, {i}master.{/i}"
    scene black with dissolve
    $ LocSet("hamun_brothel_room")
    "She led me toward one of the rooms, my eyes fixed on the hypnotic sway of her round ass."
    "Looking over her shoulder, she smirked before pulling me into a private space."
    $ LocFlush()
    show esme at cright_f
    show mc at cleft
    with dissolve
    "Inside the cool room, she closed the door, then leapt into my arms, planting a hot kiss on my lips."
    "My hands immediately grabbed her fat ass, kneading it eagerly as she pulled back with a grin."
    ESME @smile "Take me in your Slayer form."
    MC @think "My—"
    ESME @laugh "Come on, we've all heard about those tentacles of yours."
    ESME @lewd "{i}I want to see what you can really do.{/i}"
    play sound2 "audio/cfx/transform.ogg"
    hide mc
    show mc_transformed_erect at cleft
    with dissolve
    "Seeing no reason to deny her, my body began to morph—seamlessly now—as her tail swished with excited anticipation."
    "Her eyes dropped instantly to the red, ribbed cock now fully formed before her."
    ESME @smile "...How do you want me?"
    return

label hamun_brothel_esme_price_rep:
    ESME "Six hundred coins, and I'm all yours."
    ESME "A thousand... if you want to put it in my ass."
    "Esme gently trailed her tail across my crotch."
    "The voluptuous katai licked her lips enticingly and purred."
    menu:
        "I want you... and your ass." (Req_Gold = 1000):
            $ PlayerRemItem("gold", 1000)
            "Esme raised a brow, intrigued."
            ESME @smile "My ass, hmm?"
            ESME "Coin first, lover."
            "Esme holds out her hands, and once I place the bag of coins into her posession, she grins."
            ESME @lewd "Now {i}this{/i} is going to be interesting..."
            call hamun_brothel_esme_shared_setup from _call_hamun_brothel_esme_shared_setup_2
            jump hamun_brothel_esme_anal

        "I want you." (Req_Gold = 600):
            $ PlayerRemItem("gold", 600)
            call hamun_brothel_esme_shared_setup from _call_hamun_brothel_esme_shared_setup_3
            jump hamun_brothel_esme_vaginal

        "Another time, perhaps.":
            ESME @sad "Mmm... what a shame."
            ESME "You know where to find me, {i}beast{/i}."
            return

label hamun_brothel_esme_vaginal:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    menu:
        "Standing doggy.":
            jump hamun_brothel_esme_vaginal_standing_doggy
        "Doggy on the bed.":
            jump hamun_brothel_esme_vaginal_doggy_on_bed
        "Missionary.":
            jump hamun_brothel_esme_vaginal_missionary

label hamun_brothel_esme_anal:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    menu:
        "Standing doggy.":
            jump hamun_brothel_esme_anal_standing_doggy
        "Doggy on the bed.":
            jump hamun_brothel_esme_anal_doggy_on_bed
        "Missionary.":
            jump hamun_brothel_esme_anal_missionary

















######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
########### SCENES:
label hamun_brothel_esme_vaginal_standing_doggy:
    scene esme_brothel_standing_intro
    with dissolve
    $ Pause()
    "Grabbing one of her arms, Esme gasped as a tentacle moved to seize and hold her other."
    "Bent forward, her huge ass sticking out, Esme glanced back—surprised at the sudden power and speed with which I moved."
    "As she felt my huge cock gently rub against her soft, round butt, she let out a little whimper and moan."
    ESME "G-Gods, I've taken some things in my time, but—"
    ESME "Y-You might be the biggest!"
    "I cooed and rumbled soothingly, doing my best to put the curvaceous katai at ease."
    MC "We can go at your pace."
    "Esme seemed slightly more at ease by my words as I began to glide my cock back and forth faster on her soft ass."
    "As I rubbed against her, occasionally slapping my meat against her holes and cheeks, she let out a soft sigh, her womanhood beginning to glisten."
    MC "... Are you ready?"
    "Esme nodded slightly, wiggling her huge butt playfully."
    ESME "Go on, {i}master.{/i}"
    ESME "Put it in me."
    "Gently, I aligned myself with her tight slit and pressed forward."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    scene esme_brothel_standing_vag_start_slow
    with dissolve
    $ Pause()
    "A soft gasp and purr escaped her lips as the head forced its way in with ease, and slowly, I sank a few inches into her."
    ESME "Mmmm...! I can {i}feel{/i} you stretching me out so much!"
    ESME "Ahh! Talk about being blessed by the gods!"
    "Carefully, I moved back and forth, dragging my cock out of her before easing it back in—each thrust tightening her grip around me."
    "She continued to wiggle her ass playfully as I took the eager katai, her moans growing more sultry and content."
    scene esme_brothel_standing_vag_tease_tits_slow
    with dissolve
    $ Pause()
    MC "You're very—Mhmm—{i}good{/i} at this."
    "She let out a playful chuckle."
    ESME "Not used to women being able to handle you?"
    MC "Not as well as you."
    "A line of hot sweat slid down her back, her soft tail swishing side to side."
    ESME "You got any—Mhmm!—more tricks?"
    MC "Depends... Can {i}you{/i} handle them?"
    "Esme purred, letting her tail brush up against me teasingly."
    ESME "I can handle whatever you give, {i}master.{/i}"
    
    scene esme_brothel_standing_vag_grab_tits_slow
    with dissolve
    $ Pause()
    "Looping beneath her, two tentacles latched onto her swinging breasts, suckling and massaging them."
    "Esme let out a shuddering moan as I continued to slide deep inside her."
    ESME "G-Gods...!"
    ESME "Mhmmm... ❤️"
    ESME "They're more—Ahh!—gentle than I imagined!"
    MC "I can always go harder."
    "Esme giggled, squeezing tightly around my cock."
    ESME "Do it, {i}master.{/i}"
    ESME "Pound this little kitty harder!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    scene esme_brothel_standing_vag_grab_tits_fast
    with dissolve
    $ Pause()
    "As I slammed into her tight little pussy, her moans grew louder, the fat of her ass rippling with each thrust."
    ESME "Ah! Ah! Yes! That's it!"
    ESME "M-More! Give me more!"
    ESME "Your kitty can take it, Master!"
    "As sweat poured from both of us and I ravaged her eager hole, she pleaded breathlessly,"
    ESME "M-More! Show me more, master!"
    "My {i}kitten{/i} didn’t need to ask twice."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    scene esme_brothel_standing_vag_grab_arm_fast
    with dissolve
    $ Pause()
    scene esme_brothel_standing_vag_grab_head_fast
    with dissolve
    $ Pause()
    "Two more tentacles sprang forth—one pinning her other arm, the other gripping her head."
    "She gasped, fully at my mercy now, held firmly in place as I continued slamming into her."
    ESME "G-Gods... What are you—Mhmm!—doing to me?"
    ESME "This feels u-unlike anything I've ever—Mhhmm!"
    "Her body quivered and trembled around me as her cries echoed in the warm room."
    "Sweat dripped from us both, her body glistening in the candlelight."
    ESME "P-Please! Ahh! I can feel you—Mhmm!—t-throbbing!"
    ESME "Do it! F-Finish!"
    ESME "I want to feel you cum!"
    "As my balls tightened and ached, Esme teasingly wiggled her fat ass, her tail brushing against me again."
    "The sensation caught me off guard—and then it hit: that burning, deep ache to breed her, to claim her fully."
    "With a grunt, I pulled her back hard with my tentacles, bottoming out inside her, and filled her fertile cunt with hot seed."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ ReduceInfectionFromSex("esme")
    $ UnlockGalFlag("esme", "standing", "var_vag")
    $ UnlockGalSceneAndGrantXp("esme", "standing")
    scene esme_brothel_standing_vag_finish
    with flash
    $ Pause()
    MC "{i}*Roars!*{/i}"
    "Esme gasped, eyes rolling back as warmth surged through her trembling body."
    "She clenched down, as though desperate to milk me of every drop."
    ESME "{i}G-Gods...{/i}"
    "She murmured softly before letting out a satisfied coo."
    "As I unsheathed my cock, seed leaked freely from her thoroughly-used hole, and I let her gently collapse onto the bed."
    "She lay there, still and spent, save for her soft breaths and pleased sighs."
    "Letting her rest, I gathered my things, giving her ass a playful slap to watch it jiggle one last time before slipping out."
    jump hamun_brothel_esme_after_sex

label hamun_brothel_esme_anal_standing_doggy:
    scene esme_brothel_standing_intro
    with dissolve
    $ Pause()
    "Grabbing one of her arms, Esme gasped as a tentacle moved in to seize and hold her other."
    "Bent forward, her huge ass sticking out, Esme glanced back—surprised by the sudden power and speed with which I moved."
    "As she felt my huge cock gently rub up against her soft, round butt, she let out a little whimper and moan."
    ESME "G-Go slow, please!"
    ESME "I've taken some big cocks in my ass before, but..."
    ESME "Y-You might be the biggest!"
    "I cooed and rumbled soothingly, doing my best to put the curvaceous katai at ease."
    MC "Are you sure your ass can handle it?"
    "Esme gulped as I began to glide my cock back and forth faster on her soft ass."
    ESME "Y-Yes..."
    "As I rubbed against her, occasionally slapping my meat against her holes and cheeks, she let out a soft sigh as her womanhood began to glisten."
    MC "... Are you ready?"
    "Esme nodded slightly, wiggling her huge butt playfully."
    ESME "Go on, {i}master.{/i}"
    ESME "I'm ready..."
    "Carefully, I aligned my cock with her tight rosebud, prodding a couple times at her back door."
    ESME "It feels so... {i}strange.{/i}"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    scene esme_brothel_standing_anal_start_slow
    with dissolve
    $ Pause()
    "With a slightly forceful push, her ass gave way, stretching around the head of my cock."
    "Esme's eyes widened as she tried her best not to tighten up and resist."
    "She gasped, letting out a shaky, nervous breath as I sank a few inches into her tight asshole."
    ESME "F-FUCKKKK!"
    ESME "A-AHH! M-MY ASS!"
    ESME "H-Hrghhhhhh...!"
    MC "Haha, you need a moment?"
    "Esme growled lowly and snapped back,"
    ESME "D-Don't get so—Ahh!—cocky!"
    ESME "I promised you I—Mhmm!—could take you on—Ahh!"
    "Gritting her teeth but determined to make a point, Esme wiggled her ass and pushed back, burying a few more inches of cock into her defiant rear."
    ESME "{i}A-And I—Grghh! MEAN'T IT!{/i}"
    "Her tight ass squeezing around me felt incredible. I couldn’t help but let out a beastly roar as she moaned, trembling under the force of it."
    "Slowly, she began to move faster, the pain ebbing away as her lubed-up hole adjusted to the stretch."
    ESME "Mmmm...! Y-Yes! Ahh!"
    ESME "I can {i}feel{/i} you stretching my ass so much!"
    ESME "P-Pfffttt! Mhmm!"
    MC "Does it hurt?"
    ESME "{i}*Huff*{/i} A-At first! {i}*Huff*{/i}"
    ESME "Now it's just—Mhmm!"
    ESME "{b}Intense.{/b}"
    scene esme_brothel_standing_anal_tease_tits_slow
    with dissolve
    $ Pause()
    "Gently, I moved back and forth, feeling my cock drag from her ass, only to slide deeper with each push as she clenched tighter around me."
    "She wiggled her butt playfully beneath me, the eager katai moaning happily under my thrusts."
    MC "Your ass is—Grghh!—"
    MC "{i}Pleasing.{/i}"
    "She let out a playful chuckle."
    ESME "Quite the compliment from—Oooh!—a literal beast!"
    ESME "Not used to—{i}*Huff*{/i}—women handling you?"
    MC "Few as well as you."
    ESME "Glad to be—Mfghh!—your little tight-assed katai whore, {i}master...{/i}"
    "A line of hot sweat dripped from her as her soft tail swished in the candlelight."
    ESME "You got any—Mhmm!—more tricks?"
    MC "Depends... Can {i}you{/i} handle them?"
    "Esme purred again, her tail brushing against me teasingly."
    ESME "I can handle whatever you give, {i}master.{/i}"
    scene esme_brothel_standing_anal_grab_tits_slow
    with dissolve
    $ Pause()
    "Looping beneath her, two tentacles latched onto her swinging breasts, suckling and massaging them."
    "Esme moaned as my cock continued to thrust into her now eager ass."
    ESME "G-Gods...!"
    ESME "Mhmmm... ❤️"
    ESME "They're more—Ahh!—gentle than I imagined!"
    MC "I can always go harder."
    ESME "O-Oooooh..."
    "Esme moaned as she trembled, her stretched hole now taking every inch of me with ease."
    ESME "D-Do it... {i}*Huff*{/i}"
    ESME "Fuck this katai slut's ass for all it’s worth!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    scene esme_brothel_standing_anal_grab_tits_fast
    with dissolve
    $ Pause()
    "As I slammed into her tight little ass, her moans grew louder, the fat of her cheeks rippling with every impact."
    ESME "Ah! Ah! Yes! That's it!"
    ESME "P-Pound my ass! H-HARDER!"
    ESME "My ass can take it! ❤️"
    "Sweat poured from us both as I drove into her, abusing her poor little asshole as she pleaded hotly,"
    ESME "M-More! Show me more, master!"
    "My {i}kitten{/i} didn’t need to ask twice."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    scene esme_brothel_standing_anal_grab_arm_fast
    with dissolve
    $ Pause()
    scene esme_brothel_standing_anal_grab_head_fast
    with dissolve
    $ Pause()
    "Two more tentacles sprang forth—one pinning her remaining arm, the other gripping her head."
    "She gasped, completely at my mercy, suspended and held in place as I ravaged her ass relentlessly."
    ESME "G-Gods... What are you—Mhmm!—doing to me?"
    ESME "This feels u-unlike anything I've ever—Mhhmm!"
    "Her body quivered, trembling around me as her moans echoed louder."
    "The room burned with heat as sweat soaked us both, her glistening skin illuminated in candlelight."
    ESME "P-Please! Ahh! I can feel you—Mhmm!—t-throbbing!"
    ESME "Do it! F-Finish!"
    ESME "I want to feel you cum!"
    ESME "FILL MY ASS UP WITH YOUR CUM! ❤️"
    "As my balls tightened and ached, Esme wiggled her fat butt once more, her tail brushing me teasingly."
    "The sudden sensation sent me over the edge, that primal, aching need to claim her overwhelming me."
    "With a savage grunt, my tentacles yanked her back as I bottomed out inside, flooding her bowels with my hot load."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ ReduceInfectionFromSex("esme")
    $ UnlockGalFlag("esme", "standing", "var_anal")
    $ UnlockGalSceneAndGrantXp("esme", "standing")
    scene esme_brothel_standing_anal_finish
    with flash
    $ Pause()
    MC "{i}*Roars!*{/i}"
    "Esme gasped, her eyes rolling back as a splash of thick seed filled her to the brim."
    "She squeezed down around me like she never wanted to let go, milking every drop from me."
    ESME "{i}G-Gods...{/i}"
    "She whispered breathlessly, then let out a soft, satisfied coo."
    "As I pulled out of her, my cum poured freely from her gaping, well-fucked ass, and I let her collapse gently onto the bed."
    "She lay there, motionless save for the slow, blissful breaths and tiny moans that escaped her lips."
    "Deciding to let her rest, I gathered my things, giving her ass a playful slap to watch it jiggle one last time before I left."
    ESME "M-Mhy asshhh... Mhmmm... ❤️"
    jump hamun_brothel_esme_after_sex

label hamun_brothel_esme_vaginal_doggy_on_bed:
    scene esme_brothel_bed_doggy_intro
    with dissolve
    $ Pause()
    "Thrown onto the bed, Esme gasped as two of my tentacles sprang out to grab hold of her arms, holding her round butt in place as she looked over her shoulder uncertainly."
    "With my huge cock pressed and rubbing against her wet holes, she waited anxiously for whatever came next."
    ESME "M-My... You do like my ass, don't you?"
    "She tried to sound confident, but I could hear the tinge of apprehension in her voice as she eyed the size of what was about to enter her."
    MC "I do."
    "Sensing her mild unease, I did my best to soothe her nerves."
    MC "Relax... we'll go as fast as you decide."
    "Slightly reassured by my words, she did her best to boast playfully,"
    ESME "How about we see if {i}YOU{/i} can keep up with me, master!"
    "I chuckled at her brattyness, aligning the head of my cock with her slick entrance."
    "Her lips parted slightly as she felt the head press against her."
    ESME "{i}*Gasp!*{/i}"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    scene esme_brothel_bed_doggy_vag_start
    with dissolve
    $ Pause()
    "Inch by inch, I fed my cock into her, then slowly dragged it out to thrust back in again."
    "Esme bit her lower lip, trying to muffle her moans, but her wetness clenched around me tighter with every motion."
    "Teasingly, I asked her,"
    MC "You ready to handle more?"
    ESME "A-Ahh...! Mhmm...!"
    ESME "I'm just—Ahh!—getting... Mhmm! Warmed up! ❤️"
    scene esme_brothel_bed_doggy_vag_tease_tit
    with dissolve
    $ Pause()
    "Taking that as a challenge, I picked up the pace, slamming into her faster and deeper."
    "She gasped, her mouth hanging open as I watched the fat of her ass ripple with each powerful thrust."
    "{i}*Clap!* *Clap!* *Clap!*{/i}"
    "The sounds of flesh slapping against flesh echoed louder, faster, more intensely."
    ESME "G-Gods...!"
    MC "How are you handling - {i}*huff*{/i} it?"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    scene esme_brothel_bed_doggy_vag_suck_tit
    with dissolve
    $ Pause()
    "I grinned as two more tentacles reached around to attach and suckle onto her soft, heaving breasts."
    "She let out a hot moan, her back arching as I stretched her out from behind while the tentacles kneaded and tugged at her tits."
    ESME "Mmmfghh!"
    ESME "F-Fuck...!"
    ESME "It's unlike—Ahh!—anything I've ever—"
    ESME "Oh gods!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    scene esme_brothel_bed_doggy_vag_grab_head
    with dissolve
    $ Pause()
    "A third tentacle suddenly latched onto her head, pulling it back and arching her spine as I continued to take her without mercy."
    "Her mouth hung open, her little moans syncing perfectly with the rhythm of every thrust."
    ESME "Ah! Ah! Ah! Oh gods! Mhmm! Ahh! ❤️"
    ESME "B-Bastard! You're—Mhmfffh!"
    ESME "{i}C-Cheating!{/i}"
    "She squirmed under the restraint, eyes rolling back as I felt my cock throb harder from her tight grip."
    MC "I can feel you're close."
    "The katai moaned again, protesting weakly,"
    ESME "{i}Cheating! Cheating! Cheating!{/i}"
    ESME "I'm supposed to—"
    ESME "Supposed to—{i}*huff*{/i}"
    ESME "Make you finish!"
    "Pride flickered in her voice as she continued to squirm and struggle—determined to prove something."
    "But the more she feigned resistance with that cute little pout, the more turned on I became, watching her smug confidence unravel in my grip."
    ESME "You—{i}*Huff*{/i}"
    ESME "Bas—"
    "Her eyes widened, her body suddenly tightening and trembling around me."
    ESME "BASTARDDDD!"
    "Satisfied, I kept pounding her defenseless body, her moans pouring out freely now as she lay limp in my hold."
    "Her cries grew more raw, more guttural, until at last..."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ ReduceInfectionFromSex("esme")
    $ UnlockGalFlag("esme", "doggy", "var_vag")
    $ UnlockGalSceneAndGrantXp("esme", "doggy")
    scene esme_brothel_bed_doggy_vag_finish 
    with flash
    $ Pause()
    MC "{i}*ROARSSSSSSSSSS!*{/i}"
    "Gripping her ass tightly, Esme let out one final gasp as a flood of hot seed filled her waiting womb."
    "She shuddered and tensed, straining against the tentacles that held her until at last she gave in, body melting into mine."
    "With a deep, satisfied sigh, she slumped beneath me, still breathing heavy, letting out hot little whimpers and exhausted moans."
    ESME "{i}*Huff*{/i} Gods... You... Mhmmm..."
    MC "Need a moment to rest?"
    ESME "Cocky... Mmfhh... {i}beast.{/i}"
    "She closed her eyes to catch her breath, but her body quickly relaxed, drifting off to sleep as I quietly slipped away."
    jump hamun_brothel_esme_after_sex

label hamun_brothel_esme_anal_doggy_on_bed:
    scene esme_brothel_bed_doggy_intro
    with dissolve
    $ Pause()
    "Thrown onto the bed, Esme gasped as two of my tentacles sprang out to grab her arms, holding her round butt in place as she looked over her shoulder uncertainly."
    "With my huge cock pressed and rubbing against her wet holes, she waited anxiously for whatever was to come next."
    ESME "M-My... You do like my ass, don't you?"
    "She did her best to seem confident, yet I could hear the tinge of apprehension in her voice as she saw the size of the thing about to enter her."
    MC "I do."
    MC "But are you ready to take it..."
    "I lightly prodded the head of my cock against her tight, rosebud asshole."
    MC "{i}Here?{/i}"
    "She shuddered slightly."
    ESME "Y-Yes..."
    ESME "I can handle you anywhere!"
    "Sensing her lingering apprehension, I did my best to soothe her nerves."
    MC "Relax... we'll go as fast as you decide."
    "Slightly reassured by my words, she did her best to playfully boast,"
    ESME "How about we see if {i}YOU{/i} can keep up with me, master!"
    "I chuckled at her brattyness, aligning the head of my cock with her tight rosebud once more."
    MC "Don't worry... this cock self-lubricates."
    ESME "T-That's good to—"
    "Her lips parted slightly as she felt the head begin to push inside."
    ESME "{i}*Gasp!*{/i}"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    scene esme_brothel_bed_doggy_anal_start
    with dissolve
    $ Pause()
    ESME "T-TSCHHH!"
    ESME "M-My a-asshhh! Ahh!!"
    "Inch by inch, I fed my cock into her, watching it stretch her open, sinking deeper into her tight little hole before slowly dragging it back to thrust again."
    "Esme bit her lower lip, wincing in pain but desperately trying to muffle her moans."
    "She didn't want me to know I was {i}'winning'{/i} our little match, but I could feel her ass squeezing around me—clenching and flexing with every push."
    MC "Can your ass handle more?"
    "Esme's hands coiled tightly—she was clearly struggling—but with a teasing grin, she glanced back at me, eyes smoldering."
    ESME "The real—{i}*Huff*{/i}—question is... {i}*Huff*{/i}"
    ESME "If {i}YOU{/i} think you can handle more of {b}this!{/b} ❤️"
    scene esme_brothel_bed_doggy_anal_tease_tit
    with dissolve
    $ Pause()
    "Taking that as a challenge, I began slamming into her harder and deeper."
    "She gasped, mouth agape, as her fat ass rippled from every fierce thrust."
    "{i}*Clap!* *Clap!* *Clap!*{/i}"
    "The sounds of flesh slapping against flesh echoed louder and faster as I took her mercilessly."
    ESME "G-Gods...!"
    MC "Grghh! Can you handle the rest of me?"
    ESME "{i}...The rest of you?{/i}"
    ESME "I don't—"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    scene esme_brothel_bed_doggy_anal_suck_tit
    with dissolve
    $ Pause()
    "I grinned as two more tentacles reached around, attaching to her large, soft breasts, suckling and squeezing them."
    "She let out a hot moan as I continued stretching her out from behind, tentacles groping her tits as my cock throbbed deep in her ass."
    ESME "Mmmfghh!"
    ESME "F-Fuck...!"
    ESME "It's unlike—Ahh!—anything I've ever—"
    ESME "Oh gods!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    scene esme_brothel_bed_doggy_anal_grab_head
    with dissolve
    $ Pause()
    "Suddenly, a third tentacle latched onto her head, pulling it back and arching her body as I ravaged her, fully restrained."
    "The wet sounds of our bodies colliding only grew louder as her moans came faster, syncing with each thrust."
    ESME "Ah! Ah! Ah! Oh gods! Mhmm! Ahh! ❤️"
    ESME "B-Bastard! You're—Mhmfffh!"
    ESME "{i}C-Cheating!{/i}"
    "She squirmed and writhed beneath the restraint, her eyes rolling back as I felt my cock grow even more sensitive inside her."
    ESME "M-My ass!"
    ESME "MY ASSHHH! Mhhfhh!! ❤️"
    MC "I can feel you're close."
    "The katai moaned, breathless, still trying to protest,"
    ESME "{i}Cheating! Cheating! Cheating!{/i}"
    ESME "I'm supposed to—"
    ESME "Supposed to—{i}*huff*{/i}"
    ESME "Make you finish!"
    "Her pride flared even as her body shook beneath me—it wasn't just sex anymore, it was a challenge, a contest she refused to lose."
    ESME "N-Nooo! Not from the—"
    ESME "No one's ever made me cum from {i}that{/i} hole!"
    "But the more cutely she feigned resistance, the more irresistible she became—her once-smug confidence now wrapped around my finger."
    ESME "You—{i}*Huff*{/i}"
    ESME "Bas—"
    "Esme's eyes widened as her body suddenly tightened and trembled around me."
    ESME "BASTARDDDD!"
    "Satisfied, I continued to pound her defenseless body, her moans spilling freely as she lay nearly limp in my grasp."
    "Her cries became more raw, more unintelligible, until finally—"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ ReduceInfectionFromSex("esme")
    $ UnlockGalFlag("esme", "doggy", "var_anal")
    $ UnlockGalSceneAndGrantXp("esme", "doggy")
    scene esme_brothel_bed_doggy_anal_finish 
    with flash
    $ Pause()
    MC "{i}*ROARSSSSSSSSSS!*{/i}"
    "Gripping her ass tightly, Esme let out one last gasp as the flood of hot seed poured deep into her bowels."
    "She shuddered and trembled, still straining helplessly against my tentacles."
    "At last, with a long, hot sigh, her body began to ease—moaning softly, blissfully."
    ESME "{i}*Huff*{/i} My... Asshh... Mhmmm..."
    MC "Need a moment to rest?"
    ESME "Cocky... Mmfhh... {i}beast.{/i}"
    "She closed her eyes to recover, but quickly drifted off into a soft, satisfied sleep as I quietly slipped away."
    jump hamun_brothel_esme_after_sex

label hamun_brothel_esme_vaginal_missionary:
    scene esme_brothel_missionary_intro
    with dissolve
    $ Pause()
    ESME "As you wish..."
    "Pinned down with her legs spread, Esme did her best to hide her anxiousness."
    "But as she felt my huge member rub against her, she swallowed shyly, her heart racing with a cocktail of nerves and excitement."
    ESME "Gods... I've fit some big things before but—"
    ESME "This one might be a challenge."
    "As I rubbed my cock against her slit, she let out a soft moan."
    MC "Are you ready?"
    "She opened her mouth to respond, then simply nodded sheepishly."
    ESME "S-Slowly, please."
    ESME "I’m gonna need a chance to get used to you before I let you go crazy on me!"
    "Gently, I aligned my cock with her tight opening."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    scene esme_brothel_missionary_vag_start
    with dissolve
    $ Pause()
    "As I pressed against her womanhood, she let out a little gasp as her folds spread and gave way to the head, and carefully, I pushed a few inches into her."
    ESME "M-Mmfghhh!"
    "I paused for a moment, letting her catch her breath. After a few anxious exhales, she gave me a cocky little grin."
    ESME "C-Come on, don't go easy on me now."
    ESME "I promised you—ahh!—an unforgettable time, didn't I?"
    "Pleased with her resolve, I pushed in deeper, beginning to fuck her tight hole slowly but deliberately."
    "She moaned hotly, her eyes rolling back as her tail swished and brushed against me."
    ESME "F-Fuck..."
    ESME "Mhmm, some of the girls are—"
    ESME "Ahh!—scared to touch you, but I—Ooh!"
    "She bit her lower lip, panting, before speaking sultrily:"
    ESME "I knew you'd be unforgettable for me too!"
    "I snorted in approval, feeling her tight wetness clench and pulse around me as her body grew hotter beneath mine."
    "Esme's eyes flicked to one of the tentacles slithering from my back."
    scene esme_brothel_missionary_vag_tease_tit
    with dissolve
    $ Pause()
    "It snaked its way over, tongue out, and playfully lathered her breasts in aphrodisiac-laced saliva."
    "She moaned as the tongue flicked her nipple, teasing it to stiffness."
    ESME "M-MMMFGHH!"
    "Each thrust left her more breathless than the last as I tormented her with endless teasing and pressure."
    MC "... Are you ready to see what they can do?"
    "Esme grinned, flashing those feline fangs."
    ESME "Show me what you can—"
    scene esme_brothel_missionary_vag_suck_tits_slow
    with dissolve
    $ Pause()
    "She gasped as two tentacles latched onto her breasts, suckling and squeezing eagerly."
    ESME "{i}*Gasps!*{/i}"
    "Her moans grew louder, needier."
    ESME "Mmfghh!! F-Fuck me!"
    ESME "FUCK ME HARDER!"
    ESME "Destroy this little—ahh!—pussy!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    scene esme_brothel_missionary_vag_suck_tits_fast
    with dissolve
    $ Pause()
    "Her tight hole stretched and clenched with every movement as her heart pounded against her chest."
    "Like a man—or more accurately, {i}a monster{/i}—possessed,"
    "I wanted to devour her, to bury myself in her completely, that feral lust swelling up uncontrollably."
    "She trembled beneath me. For a brief moment I thought she might shatter, until—"
    ESME "P-Please!"
    ESME "Mmmfhhh!"
    ESME "F-Finish in me!"
    ESME "D-Don't stop! Ahhh!"
    ESME "Don't stop till you fill me up!"
    "Pinned beneath me, Esme stared up like willing prey, her moans spilling out in hot gasps as I drove us both toward climax."
    ESME "M-More!"
    ESME "Just a little—"
    "Her entire trembling body suddenly tightened around my cock, her eyes flying wide,"
    "her cunt locking down as a soft, whimpering moan escaped her lips."
    "I growled, driven wild by the urge to claim my mate's womb, my blood pounding with a single thought:"
    "{i}Breed... Breed... Breed.{/i}"
    "I tightened my grip around her hips as she gasped, then cried out—"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ ReduceInfectionFromSex("esme")
    $ UnlockGalFlag("esme", "missionary", "var_vag")
    $ UnlockGalSceneAndGrantXp("esme", "missionary")
    scene esme_brothel_missionary_vag_finish 
    with flash
    $ Pause()
    "feeling the rush of my hot seed pour into her welcoming body."
    "I roared triumphantly, then leaned down to nuzzle her gently as she reached up with trembling fingers to kiss me."
    "Our lips met just as the last few spurts poured into her womb."
    "Slowly, I unsheathed my cock, watching as thick white seed spilled from her well-fucked pussy."
    "Esme looked down between her legs, wide-eyed and amazed."
    ESME "{i}*Giggles*{/i} Are you sure you're not part horse or something?"
    "I rumbled in amused response."
    ESME "{i}*Sigh*{/i} Well, I think I might need to lay down for a while after that!"
    "She winked at me, her legs trembling as she tried to stay upright."
    ESME "Come back anytime, handsome!"
    jump hamun_brothel_esme_after_sex

label hamun_brothel_esme_anal_missionary:
    scene esme_brothel_missionary_intro
    with dissolve
    $ Pause()
    ESME "As you wish..."
    "Pinned down with her legs spread, Esme did her best to hide her anxiousness."
    "But as she felt my huge member rub against her, she swallowed shyly, her heart racing with a mixture of nerves and excitement."
    ESME "...F-Fitting that {i}thing{/i} up my ass is going to be a challenge."
    "Teasingly, I prodded and rubbed the head of my cock against her tight, rosebud."
    MC "Well, if you're not up to it—"
    ESME "Ha! I never back down from a challenge!"
    "Gently, I continued to press against her backdoor as she let out a quiet, nervous whimper."
    MC "In that case..."
    MC "Are you ready?"
    "She opened her mouth to say something, then nodded sheepishly."
    ESME "S-Slowly, please."
    ESME "I’m gonna need a chance to get used to you before I let you go crazy on me!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    scene esme_brothel_missionary_anal_start
    with dissolve
    $ Pause()
    "Gently, I aligned my cock with her tight opening."
    "As I pressed against her rosebud, her toes curled and her breath caught, trembling with nervous anticipation."
    "As her ass gave way and spread to accommodate the head, her mouth opened in shock, eyes going wide—"
    ESME "A-AHHHH!"
    "Carefully, I pushed a few inches into her tight rear."
    ESME "G-GRGGHFHH!!"
    ESME "M-MY AASSHHH! ❤️"
    "I paused, giving her time to steady herself. After a few anxious breaths, she gave me another cocky grin."
    ESME "C-Come on, don’t go easy on me now."
    ESME "I promised you—ahh!—an unforgettable time, didn’t I?"
    ESME "{i}*Huff*{/i} My ass can take it... {i}*Huff*{/i}"
    "Pleased with her resolve, I pushed deeper, beginning to slowly fuck her tight asshole."
    "She moaned hotly, her eyes rolling back, tail swishing and brushing against my skin."
    ESME "F-Fuck..."
    MC "How is it?"
    ESME "S-Stretched and—"
    ESME "{i}F-Full.{/i}"
    MC "Still painful?"
    ESME "A-A little, but—"
    ESME "Oooooh!"
    "The ring of her ass flexed and squeezed around me in pulsing, rhythmic contractions."
    ESME "Some of the girls are—"
    ESME "Ahh!—scared to touch you, but I—Ooh!"
    "She bit her lower lip, panting, voice sultry and defiant."
    ESME "I knew you'd be unforgettable for me as well!"
    "I snorted in approval, feeling her tight ass grip and squeeze me as her body burned hotter beneath me."
    "Esme's eyes flicked toward one of the tentacles slithering from my back."
    scene esme_brothel_missionary_anal_tease_tit
    with dissolve
    $ Pause()
    "It crept forward, tongue flicking out as it lathered her breasts in aphrodisiac-laced saliva."
    "She moaned as the tongue flicked lewdly over her nipple, teasing it to erection."
    ESME "M-MMMFGHH!"
    "Each thrust left her more breathless than the last as I continued teasing every part of her body."
    MC "...Are you ready to see what they can do?"
    "Esme grinned, flashing her feline teeth."
    ESME "Show me what you can—"
    scene esme_brothel_missionary_anal_suck_tits_slow
    with dissolve
    $ Pause()
    "She gasped as two more tentacles reached out and latched onto her breasts, suckling and squeezing eagerly."
    ESME "{i}*Gasps!*{/i}"
    "Esme's moans rose in pitch as she pleaded lewdly:"
    ESME "Mmfghh!! F-Fuck me!"
    ESME "FUCK MY ASS HARDER!"
    ESME "Destroy my little hole!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    scene esme_brothel_missionary_anal_suck_tits_fast
    with dissolve
    $ Pause()
    "Her tight ass stretched wider around me as her heart pounded faster."
    "Like a man—no, {i}a monster{/i}—possessed,"
    "I wanted to consume her whole, driven by a feral, intoxicating lust."
    "She trembled beneath me. For a moment, it felt like she might break—until she cried out again, begging for more."
    ESME "P-Please!"
    ESME "Mmmfhhh!"
    ESME "F-Finish in me!"
    ESME "D-Don't stop! Ahhh!"
    ESME "Don't stop till you fill me up!"
    "Pinned, Esme looked up at me like willing prey, her breath hot and heavy between each desperate moan as we approached the edge."
    ESME "M-More!"
    ESME "Just a little—"
    "Her entire body tightened as her eyes widened,"
    "her tight ass clenching down around my cock as a soft, whimpering moan slipped from her lips."
    "I growled, overcome by the primal need to claim her completely—my blood roaring with one instinctual thought:"
    "{i}Mine... Mine... MINE.{/i}"
    "I tightened my grip on her waist as she gasped, feeling the flood of my hot seed pour into her bowels, her body quivering as she milked every drop."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ ReduceInfectionFromSex("esme")
    $ UnlockGalFlag("esme", "missionary", "var_anal")
    $ UnlockGalSceneAndGrantXp("esme", "missionary")
    scene esme_brothel_missionary_anal_finish 
    with flash
    $ Pause()
    "I roared triumphantly, then leaned in to nuzzle her gently as she reached up, trembling, and kissed me tenderly while the last of my release poured into her."
    "Slowly, I unsheathed my cock from her, watching the excess seed spill out of her gaping ass."
    "Esme looked down, blinking, more stunned than anything at just how much I'd released."
    ESME "Gods... I'm not going to be able to walk straight after that!"
    "I rumbled in amusement."
    ESME "Don't be cute with me now just because your cum's leaking out of my ass!"
    ESME "{i}*Phew*{/i} I think I might need to lay down for a while..."
    "She winked at me, her legs wobbling as she tried not to collapse."
    ESME "Mmm... Come back anytime you want to give me a good workout, handsome!"
    jump hamun_brothel_esme_after_sex

label hamun_brothel_esme_after_sex:
    $ LocSet("hamun_brothel")
    $ AutoMus(True)
    $ LocEnter()