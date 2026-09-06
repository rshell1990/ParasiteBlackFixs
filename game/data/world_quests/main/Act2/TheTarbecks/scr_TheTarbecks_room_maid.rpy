label qst_TheTarbecks_Room_Maid_main:
    if "maid" in QstTheTarbecks().PlayedInRooms:
        if config.developer:
            "DEBUG: already been to this room. override the block and go again?"
            menu:
                "yes":
                    pass
                "no":
                    jump qst_TheTarbecks_AlreadyPlayedInThisRoom
        else:
            jump qst_TheTarbecks_AlreadyPlayedInThisRoom

    scene black with dissolve
    $ LocSet("hamun_tarbeck_room_maidmaster")
    $ Pause(0.15)
    $ LocFlush(dissolve)
    "Heading into the room, soft music played in the background from a naked, masked band on a small stage as one half of each couple wore some kind of... slutty maid attire."
    show mc at cleft with easeinleft
    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_3
    if QstTheTarbecks().PartyCompanion == "kiara":
        show kiara at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "esme":
        show esme at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "markus":
        show markus_fem at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "ves":
        show ves at left with easeinleft
    "Fixed so that the {i}maid's{/i} ass and tits were fully on display."
    "But curiously, for some of the couples, it was the {i}man{/i} dressed in such a way."
    "The maids wandered around, serving tea, allowing themselves to be fondled, or even openly dropping to their knees to pleasure their {i}masters{/i} for all to see."
    "In each corner, a masked, well-dressed figure watched silently as the lobby grew more and more depraved."
    "One of the masked servers approached me."
    show cg_tarbeck_watcher at cright_f with easeinright
    WATCHER "Greetings."
    WATCHER "Would you like to play {i}Our Master's Servant?{/i}"
    MC @think "What are the rules?"
    WATCHER "It's quite simple. One of you plays the master, the other plays the servant."
    WATCHER "The watchers will select those they believe are the most {i}devoted{/i} servants."
    WATCHER "There is more than one golden token to be won here."
    MC @surprised "Really?"
    WATCHER "Yes, but..."
    WATCHER "That would require the utmost commitment."
    if QstTheTarbecks().PartyCompanion == "kiara":
        jump qst_TheTarbecks_Room_Maid_kiara
    elif QstTheTarbecks().PartyCompanion == "esme":
        jump qst_TheTarbecks_Room_Maid_esme
    elif QstTheTarbecks().PartyCompanion == "markus":
        jump qst_TheTarbecks_Room_Maid_markus
    elif QstTheTarbecks().PartyCompanion == "ves":
        jump qst_TheTarbecks_Room_Maid_ves

label qst_TheTarbecks_Room_Maid_kiara:
    show mc at blurin, cleft_f
    MC @think "Well, what do you think?"
    KIARA @smile "Dressin' me up as yer little slutty maid, ehh?"
    "She nudged me with her shoulder."
    KIARA @smile "How about it, handsome?"
    KIARA @talk "Just don't get {i}too{/i} cocky now."
    menu:
        "Let's play.":
            pass
        "Let's pass for now.":
            KIARA @sad "Eh?"
            KIARA @sad "Well, if you think so..."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    KIARA @smile "Oooh! Where do I get my outfit?"
    show mc at blurin, cleft
    WATCHER "Right this way..."
    show cg_tarbeck_watcher at blurin, cright
    hide cg_tarbeck_watcher with easeoutright
    hide kiara with easeoutright
    scene black with dissolve
    $ CharSetClothes("kiara", "maid")
    $ Pause(0.15)
    $ LocFlush()
    show mc at cleft
    with dissolve
    show kiara at cright_f with easeinright
    $ Pause()
    show cg_tarbeck_watcher at right_f with easeinright
    KIARA @smile "Ahh... Quite the tight fit, isn't it?"
    show cg_tarbeck_watcher at blurin, right
    hide cg_tarbeck_watcher with easeoutright
    show kiara at blurin, cright
    KIARA @smile "So, what now? Do I-"
    "The masked server turned to leave; it seemed the finer details were up to us to figure out."
    show kiara at blurin, cright_f
    KIARA @smile "So, what now then... {i}Master?{/i}"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ tmpvar = ["pet", "cards", "drinks"]
    label qst_TheTarbecks_Room_Maid_kiara_choices:
    if len(tmpvar) > 0:
        menu:
            "Have Kiara crawl around beside you as your pet." if "pet" in tmpvar:
                $ tmpvar.remove("pet")
                play sound "audio/cfx/finger_snap.ogg"
                "I snapped my fingers toward the floor."
                MC "Down."
                KIARA @think "W-What?"
                MC @talk "On your knees... {i}pet.{/i}"
                window hide
                hide kiara
                hide mc
                show cg_kiara_maid_leash at center
                with dissolve
                play sound "audio/cfx/body_falling.ogg"
                $ Pause()
                "Kiara blinked, her cheeks burning a light rosy shade of red as she dropped to the floor."
                "As I wandered around, Kiara crawled obediently on her hands and knees beside me."
                "For half an hour, I wandered almost aimlessly around the lobby as Kiara followed at my side."
                "Another couple did the same thing, except this one's wife seemed fully converted, a fake dog tail plugged into her ass."
                PARTY_GUEST "What a lovely pet you have."
                MC "Thank you."
                "I looked down at Kiara, gently petting her head."
                MC "{i}I'm still training this one.{/i}"
                "Kiara's cheeks burned red, and for a moment she gave me the slightest pout, as if to say '{i}Don't push it.{/i}'"
                GUESTS_PET "{i}Woof!{/i}"
                "The woman panted, wagging her tail as she looked toward Kiara longingly."
                PARTY_GUEST "... Would you like to let our pets play for a while?"
                menu:
                    "Let's let them play.":
                        GUESTS_PET "{i}*Woof!*{/i}"
                        "The guest's wife leapt onto Kiara, pinning her to the floor."
                        $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
                        play sound "audio/cfx/body_falling.ogg"
                        scene kiara_tarbeck_maid_pet_1 with dissolve
                        $ Pause()
                        KIARA "W-Whoaaa!"
                        KIARA "E-Easy now, love!"
                        KIARA "U-Uhh, good doggy?"
                        GUESTS_PET "Woooof..."
                        KIARA "(Fuck, just how screwed up is her head?)"
                        KIARA "(Does she really think she's a-)"
                        "The woman began to lick and lap at Kiara's pussy with her tongue."
                        scene kiara_tarbeck_maid_pet_2 with dissolve
                        $ Pause()
                        KIARA "O-Ooooh!"
                        KIARA "S-Shiittttt!"
                        PARTY_GUEST "... Your pet still talking, huh?"
                        PARTY_GUEST "Don't worry, it's taken years to get my wife to fully accept her new role."
                        PARTY_GUEST "You simply have to... {i}break them a bit.{/i}"
                        MC "(What kind of madman would destroy a person like that?)"
                        MC "A-Ahh, yes, of course."
                        "Kiara grinned as the pet-wife continued to pleasure her, twisting and burying her tongue deep into Kiara's pussy as she grunted happily."
                        KIARA "M-Mmmfghhh!"
                        KIARA "Gods... She eats cunt like her life depends on it!"
                        GUESTS_PET "{i}*Woof!*{/i}"
                        "Kiara's eyes began to roll back as the woman's tongue buried deep, twisting and thrashing around inside of her."
                        $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
                        scene kiara_tarbeck_maid_pet_finish with flash
                        $ Pause()
                        KIARA "Mmmfghhhh!!"
                        KIARA "Gods! She's got a tongue like a demon!"
                        scene black with dissolve
                        "Seemingly pleased, the guest's wife suddenly turned around, waving her round ass in Kiara's face."
                        KIARA "... Love, what are you doing?"
                        KIARA "You want me to-"
                        $ PlaySexFx("audio/sex_sounds/ves69_100.ogg", 1)
                        scene kiara_tarbeck_maid_pet_3 with dissolve
                        $ Pause()
                        "Before Kiara could finish, the pet-wife planted her ass firmly onto Kiara's face."
                        KIARA "Mmmfghh?!"
                        GUESTS_PET "W-Woooof!"
                        KIARA "Ahhh! Youhh littlhee!"
                        KIARA "Mhfhhh!"
                        KIARA "T-Thasthyy bitchh..."
                        $ PlaySexFx("audio/sex_sounds/ves69_125.ogg", 1)
                        scene kiara_tarbeck_maid_pet_4 with dissolve
                        $ Pause()
                        "As she forced Kiara's tongue deeper into her pussy, she leaned forward, continuing to lap up Kiara's juices."
                        PARTY_GUEST "Oh my, it seems my wife has taken quite a liking to your pet!"
                        MC "I can see that..."
                        "Kiara reached up to grab the woman's ass, squeezing her cheeks as she buried her tongue deeper."
                        "Their hot moans filled the lobby as eyes were drawn toward us from all around."
                        "A few guests raised their glasses and nodded approvingly as I watched the two sweaty, enthralled pets devour each other's cunts."
                        MC "So, should you win the game, what are you-"
                        PARTY_GUEST "Oh, we just come here for the fun now."
                        PARTY_GUEST "{i}We actually won last year's game.{/i}"
                        MC "What?!"
                        PARTY_GUEST "Yes..."
                        "The man looked down at his wife, wiggling her fat ass on Kiara's face as the two women continued to moan."
                        PARTY_GUEST "{i}We got what we were looking for.{/i}"
                        PARTY_GUEST "Now we just come here for fun."
                        PARTY_GUEST "And you— is there some treasure you seek from Lord Zanzibat?"
                        MC "Of a sort..."
                        PARTY_GUEST "Ahh, interesting."
                        $ PlaySexFx("audio/sex_sounds/ves69_finish")
                        scene kiara_tarbeck_maid_pet_finish_2 with flash
                        $ UnlockGalSceneAndGrantXp("kiara", "tarbeck_maid_pet")
                        $ Pause()
                        KIARA "MMMMFGHHH?!"
                        "The two women squirmed and shook on the floor, a hot, wet mess as Kiara was brought to climax."
                        PARTY_GUEST "Done already, dear?"
                        GUESTS_PET "{i}*Woof!*{/i}"
                        "The guest's wife leapt off Kiara, returning to her master's side, rubbing her face against his leg."
                        "Kiara lay sprawled out and breathless, still twitching from her orgasm."
                        KIARA "A-Ahhhh...."
                        KIARA "G-Good doggy..."
                        KIARA "Such a— {i}*huff*{/i} good doggy..."
                        $ LocFlush()
                        show mc at cleft
                        show cg_kiara_maid_kneel at cright_f
                        with dissolve
                        PARTY_GUEST "Well, I must leave you to it."
                        PARTY_GUEST "... Oh, here, by the way."
                        PARTY_GUEST "We won't be needing this."
                        "The masked man handed me a small gold token."
                        $ PlayerAddItem("qst_tarbeck_golden_token")
                        MC "Thank you."
                        PARTY_GUEST "Come now, dear. Let's go find your sister and mother."
                        GUESTS_PET "WOOF!"
                        MC "(... Did he just say-)"
                        hide cg_kiara_maid_kneel
                        show kiara at cright_f
                        with dissolve
                        "With shaky legs, Kiara dragged herself back to her feet."
                        KIARA @talk "That woman ain't human."
                        KIARA @talk "Gods..."
                        #MC @talk "Come on, we're not done yet."
                        jump qst_TheTarbecks_Room_Maid_kiara_choices
                    "I'm afraid not.":
                        PARTY_GUEST "Hmm... A shame."
                        "The guest turned to leave, tugging on his {i}pet's{/i} collar as she followed him."
                        MC "(Damn... I hope I didn't screw us out of a token there somehow.)"
                        jump qst_TheTarbecks_Room_Maid_kiara_choices
            "Have Kiara suck your cock while you play card games." if "cards" in tmpvar:
                $ tmpvar.remove("cards")
                $ PlaySexFx("audio/sex_sounds/ves69_100.ogg", 1)
                scene kiara_tarbeck_maid_cards_3 with dissolve
                $ Pause()
                "Taking a seat at a nearby table, a woman on her hands and knees sucked at her partner's cock as he casually drew cards."
                PARTY_GUEST "Ahh! Can I help you?"
                GUESTS_PET "{i}*Slurp!*{/i} Mhmmm..."
                PARTY_GUEST "Ahh! Careful with the teeth, dear."
                GUESTS_PET "Mmm... ❤️"
                PARTY_GUEST "Interested in a game of cards?"
                "I looked toward Kiara, who nodded and smiled, her eyes flicking between me and the woman on her knees."
                "As I took a seat, Kiara knelt between my legs, pulling out my cock and playfully slapping it against her cheek."
                KIARA "Yer getting quite bold, love, just presumin' I'll suck your cock whenever you want."
                MC "It's {i}sir{/i} to you."
                KIARA "Mmmm... Yes, {i}sir.{/i}"
                $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
                scene kiara_tarbeck_maid_cards_1 with dissolve
                $ Pause()
                "Kiara barely finished her sentence before she took my cock into her mouth."
                KIARA "Mmmfghh...!"
                "Her lips slid back and forth as she looked up at me obediently."
                PARTY_GUEST "How about a game of Barati to pass the time?"
                MC "A-Ahh... Why not?"
                "Over the course of the game, Kiara did her best to please me, inch by inch swallowing more of my cock as her lips glided back and forth."
                "Her soft, hot tongue beat against me as I groaned quietly."
                PARTY_GUEST "Do you have your own deck?"
                scene kiara_tarbeck_maid_cards_2 with dissolve
                $ Pause()
                "Kiara slid her mouth forward, taking another inch as she rolled her tongue around the base."
                KIARA "{i}*Slurp!*{/i} Mmfhghh..."
                MC "A-Ahhh!"
                MC "Y-Yes... Mhmm..."
                "The man smiled as he placed his first card down; with a shaky hand, I placed mine."
                "Kiara's tongue thrashed lewdly as the man reached back, gripping his wife's head and forcing her to take him deeper."
                $ PlaySexFx("audio/sex_sounds/ves69_125.ogg", 1)
                scene kiara_tarbeck_maid_cards_4 with dissolve
                $ Pause()
                PARTY_GUEST "Ah! So, is this maid your wife as well?"
                "Kiara's ears seemed to perk up at the comment as she looked up at me, eyes almost starry, her lips wrapped firmly around my cock."
                MC "N-No... I mean, uhh..."
                MC "{i}Perhaps one day?{/i}"
                "Something in my words seemed to flip a switch in Kiara, her mouth suddenly taking me to the hilt, eyes watering as she struggled to hold me down her throat."
                MC "F-FUCKKK!?"
                KIARA "MMMMFGHHHH! {i}*Slurp!*{/i}"
                PARTY_GUEST "Oh my... It seems she rather liked that idea."
                GUESTS_PET "Mmfghh! {i}*Slurp!*{/i}"
                GUESTS_PET "Yhonghhlhovee! Mhfhhh...!!"
                PARTY_GUEST "Don't speak with your mouth full, dear. It's rude!"
                "The woman let out a guttural moan as Kiara became more determined than ever to drain my balls dry."
                $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
                scene kiara_tarbeck_maid_cards_2 with dissolve
                $ Pause()
                MC "{i}*Huff*{/i} K-Kiara..."
                KIARA "{i}*Slurp!*{/i} Mhasthahh! ❤️"
                "For the next fifteen minutes, I drew card after card, barely able to focus on the game at all."
                "Kiara's mouth continued to glide back and forth, coating my cock in her warm, wet saliva."
                "Wiggling her ass, she seemed more incensed than ever by my earlier words."
                "It became harder and harder to keep my focus."
                PARTY_GUEST "Your move..."
                "Wiping sweat from my brow, I dazedly placed a card onto the table."
                "My balls ached and swelled, my cock feeling ready to burst at any moment."
                "My nails dug into the armchair as I fought not to fill Kiara's mouth."
                PARTY_GUEST "Oh my... Hmm, seems you're struggling a bit—"
                $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
                scene kiara_tarbeck_maid_cards_finish_2 with flash
                $ Pause()
                PARTY_GUEST "URGHHHH!"
                "The man's composure broke as his wife pushed her nose into his pubic hair, nuzzling his cock as he groaned loudly, spilling his load into her mouth."
                PARTY_GUEST "OOOOOOOH!"
                PARTY_GUEST "Dear! Couldn't you have waited a moment?!"
                "Unable to hold back any longer, I grabbed the back of Kiara's head and pulled her toward me."
                $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
                scene kiara_tarbeck_maid_cards_finish with flash
                $ UnlockGalSceneAndGrantXp("kiara", "tarbeck_maid_cards")
                $ Pause()
                "Her eyes widened, watering as a muffled whimper escaped her lips."
                "Holding her firmly in place, her tongue thrashed as I poured my hot load into her mouth, feeding her like the good little {i}maid{/i} she was."
                MC "K-KIARAAAAAAA!!"
                "Kiara squirmed between my legs, struggling to breathe as she kicked weakly, desperately swallowing as much as she could."
                "All the while, a wet patch between her legs dripped onto the floor."
                "At last, I released her, letting her pull back and gasp for air."
                KIARA "{i}*Huff!*{/i} Gods!"
                KIARA "You nearly— {i}*Huff*{/i} bloody killed me!"
                MC "A-Ah... I may have gotten a little carried away."
                "Kiara wiped her mouth and smiled."
                KIARA "{i}There are worse ways to die than doing what you love...{/i}"
                $ LocFlush()
                show mc at cleft
                show kiara at cright_f
                with dissolve
                show cg_tarbeck_watcher at left with easeinleft
                "As she rose back to her feet, one of the watchers approached."
                show cg_tarbeck_watcher at nod
                $ PlayerAddItem("qst_tarbeck_golden_token")
                $ Pause(0.3)
                hide cg_tarbeck_watcher with easeoutright
                "Placing a golden token into my palm, the figure bowed before stepping away."
                PARTY_GUEST "Where's our token?!"
                "The watcher didn't answer, simply retreating back to their corner."
                PARTY_GUEST "I swear those bloody things just make the rules up as they go!"
                GUESTS_PET "Come now, dear. Let's go find Karalyse and Morkan—you know you love it when we switch."
                "The two figures smiled as they hurried off to continue their debauchery."
                KIARA @smile "Well... That was interesting."
                #KIARA @talk "What next?"
                jump qst_TheTarbecks_Room_Maid_kiara_choices
            "Have Kiara fetch you drinks." if "drinks" in tmpvar:
                $ tmpvar.remove("drinks")
                KIARA @smile "Drinks?"
                KIARA @smile "Easy enough."
                KIARA @smile "Wait right here... {i}Master.{/i}"
                show kiara at blurin, cright
                hide kiara with easeoutright
                "Kiara chuckled as she swanned off to grab a silver tray, loading it up with glasses filled with wine."
                show mc at center with ease
                "She kept turning her head to glance back at me the whole time, and with the tray balanced in one hand, she did her best to sashay alluringly on her way back."
                KIARA @smile "Mmm, master, would you like a dri—"
                $ LocFlush()
                show mc at center
                with dissolve
                play sound "audio/cfx/bottleBreak.ogg"
                KIARA "SHITTTTT!"
                MC "..."
                show mc at cleft with ease
                show kiara at cright_f with easeinright
                "Crashing to the floor amid shattered glass and spilled wine, Kiara groaned painfully, rubbing the back of her head."
                KIARA "Owwww..."
                MC @surprised "Are you alright?"
                KIARA "Y-Yes, just, uhh..."
                KIARA "I can fix this! Just let me clean it up!"
                show kiara at blurin, cright
                hide kiara with easeoutright
                #Kiara hurries off screen
                MC @surprised "Kiara! Wait!"
                MC @serious "(Damn it...)"
                scene black with dissolve
                "Kiara returned a few moments later, awkwardly trying to sweep up the broken glass."
                "Suffice it to say, our little performance was more embarrassing than tantalizing."
                $ LocFlush()
                show mc at cleft
                show kiara at cright_f
                with dissolve
                KIARA @sad "S-Sorry about that."
                MC "Let's just move on..."
                #KIARA @sad "Mmmm."
                jump qst_TheTarbecks_Room_Maid_kiara_choices
    else:
        KIARA @smile "So, what now... {i}sir?{/i}"
        MC @talk "Come on. We still have more {i}games{/i} to win."
        scene black with dissolve
        $ CharSetClothes("kiara", "dress")
        $ LocSet("hamun_tarbeck_playhallway")
        jump qst_TheTarbecks_Room_Maid_over

label qst_TheTarbecks_Room_Maid_markus:
    show mc at blurin, cleft_f
    MC @think "Well, what do you think?"
    MARKUS_FEM @angry "... You can't be serious?"
    MARKUS_FEM @angry "You want me to pretend I'm your maid?"
    menu:
        "We need to win this... Think about your brother!":
            pass

        "You're right, let's forget the idea.":
            MARKUS_FEM @talk "Right..."
            MARKUS_FEM @angry "Then let's get out of here before I shove one of those feather dusters up these pervs asses."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    MARKUS_FEM @sad "I-"
    MARKUS_FEM @angry "Urghh!"
    MARKUS_FEM @sad "Fine, whatever."
    show cg_tarbeck_watcher at center_f with ease
    show cg_tarbeck_watcher at nod
    "The watcher handed over a maid outfit with both hands, which Marcia apprehensively took."
    MARKUS_FEM @think "Umm... Thanks."
    show cg_tarbeck_watcher at nod
    $ Pause(0.2)
    show cg_tarbeck_watcher at blurin, center
    hide cg_tarbeck_watcher with easeoutright
    "The figure bowed before retreating."
    MARKUS_FEM @talk "I guess I'll go change into this... Give me a few moments."
    hide markus_fem with easeoutright
    show mc at blurin, cleft
    scene black with dissolve
    "... A short while later, a blushing Marcia returned, cheeks burning red as she inspected the dress."
    $ CharSetClothes("markus", "maid")
    $ LocFlush()
    show mc at cleft
    with dissolve
    show markus_fem at cright_f with easeinright
    MARKUS_FEM @blush "Half my ass is showing."
    MARKUS_FEM @blush "This skirt is way too short!"
    MC @think "I think you'll find that was intentional."
    MARKUS_FEM @talk "Urghh..."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    MARKUS_FEM @talk "Well then, what should we do first?"
    $ tmpvar = ["pet", "cards", "drinks"]
    label qst_TheTarbecks_Room_Maid_markus_choices:
    if len(tmpvar) > 0:
        menu:
            "Have Marcia crawl around as your pet." if "pet" in tmpvar:
                $ tmpvar.remove("pet")
                MARKUS_FEM @surp "... Friend."
                MARKUS_FEM @angry "You must be joking!"
                MC @talk "Relax, it's just pretend play."
                MC @serious "You don't have to have sex with anyone! You just need to crawl around a bit!"
                MARKUS_FEM @angry "Urghh... I should have never agreed to come to this party with you."
                MARKUS_FEM @angry "This is so fucking degrading."
                MC @talk "Mark- I mean, {i}Marcia.{/i}"
                MC @serious "Remember why we're here. If we don't do this, your brother—"
                show markus_fem at shake
                MARKUS_FEM @angry "I know, I know, I KNOW!"
                MARKUS_FEM @sad "{i}*Sigh*{/i}"
                window hide
                hide markus_fem
                hide mc
                show cg_markus_fem_maid_leash at center
                with dissolve
                $ Pause()
                "Marcia lowered herself to the floor on her hands and knees."
                MARKUS_FEM @sad "O-Okay master, uhh... Let's go or something..."
                MC @smile "Convincing stuff."
                MARKUS_FEM @angry "Shut the fuck up."
                "As I wandered around, Marcia crawled obediently beside me."
                "For half an hour, I wandered almost aimlessly around the lobby as Marcia followed."
                "Another couple was doing the same, except this one's wife seemed fully converted, a fake dog tail plugged into her ass as she beckoned us over."
                PARTY_GUEST "What a lovely pet you have."
                MC "Thank you."
                "I looked down at Marcia, gently petting her head as she pouted irritably."
                MC "{i}I'm still training this one.{/i}"
                "Marcia winced, barely restraining herself from a witty comeback."
                GUESTS_PET "{i}Woof!{/i}"
                "The woman panted, wagging her tail as she looked at Marcia longingly."
                PARTY_GUEST "... Would you like to let our pets play for a while?"
                menu:
                    "Let's let them play.":
                        MC @smile "Why not?"
                        MC @smile "Go ahead, Marcia, have some fun."
                        GUESTS_PET "{i}*Woof!*{/i}"
                        "The guest's wife crawled over, wagging her tail as she sniffed, then licked at Marcia's neck."
                        MARKUS_FEM "U-Uhh, good girl?"
                        GUESTS_PET "{i}*Woof!*{/i}"
                        "The woman leapt onto Marcia, cupping her breasts as she kissed, licked, and nipped at her neck."
                        MARKUS_FEM "W-Whoa! Hold on a minute!"
                        MARKUS_FEM "What are you—"
                        MARKUS_FEM "Mmmfghh...!"
                        MARKUS_FEM "{i}*Huff*{/i} Oh... You wanna play, huh?"
                        GUESTS_PET "Arffff?"
                        scene black with dissolve
                        play sound "audio/cfx/body_falling.ogg"
                        "Marcia surged forward, wrestling the squirming wife into submission as she yelped."
                        GUESTS_PET "Mmmfghh??!"
                        MARKUS_FEM "Stop squirming."
                        MARKUS_FEM "It's {i}my{/i} turn."
                        $ PlaySexFx("audio/sex_sounds/ves69_100.ogg", 1)
                        scene markus_fem_tarbeck_maid_pet_loop_1 with dissolve
                        $ Pause()
                        "With fingers pressed into the wife's mouth, Marcia muffled her moans as her other hand worked between the woman's legs."
                        GUESTS_PET "M-Mmfghhh!!"
                        MARKUS_FEM "See?"
                        MARKUS_FEM "Isn't this better?"
                        $ PlaySexFx("audio/sex_sounds/ves69_125.ogg", 1)
                        scene markus_fem_tarbeck_maid_pet_loop_2 with dissolve
                        $ Pause()
                        "As Marcia drove her fingers deeper, the woman's eyes rolled back while her husband watched, amused and uneasy."
                        PARTY_GUEST "Your pet is quite... aggressive."
                        MC "O-Oh yes!"
                        MC "Uhh, still in training."
                        MARKUS_FEM "You like that, huh?"
                        GUESTS_PET "Mmmfffhh!"
                        MARKUS_FEM "Don't worry."
                        MARKUS_FEM "You're in good hands."
                        MARKUS_FEM "{i}Slut.{/i}"
                        "The wife trembled, her breath ragged as Marcia worked her relentlessly."
                        PARTY_GUEST "..."
                        MC "Uhh, lots of work left to do."
                        GUESTS_PET "Mmmmmfghh!"
                        "Her cries grew louder until—"
                        $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
                        scene markus_fem_tarbeck_maid_pet_finish with flash
                        $ UnlockGalSceneAndGrantXp("markus", "tarbeck_maid_pet")
                        $ Pause()
                        GUESTS_PET "MMMFFFFHHHH!!"
                        MARKUS_FEM "Haha, now that's a sound I could get used to!"
                        "Satisfied, Marcia withdrew her fingers, licking them casually as the wife whimpered back to her husband."
                        PARTY_GUEST "Darling! Are you alright?"
                        GUESTS_PET "{i}*Huff*{/i} A-Arff..."
                        MC @surprised "I-I'm sorry!"
                        MC @talk "My pet still gets a little excited!"
                        PARTY_GUEST "... Come along dear. Let's find nicer playmates."
                        "He tugged her lead and left, casting me a displeased look."
                        MC @serious "Urghhh..."
                        $ LocFlush()
                        show mc at cleft
                        show markus_fem at cright_f
                        with dissolve
                        "A smug Marcia rose to her feet."
                        MC @angry "... Really?"
                        MARKUS_FEM @surp "What? We were just having fun!"
                        MC @serious "We're not supposed to scare off guests!"
                        show cg_tarbeck_watcher at left with easeinleft
                        WATCHER "... For your performance."
                        show cg_tarbeck_watcher at nod
                        $ PlayerAddItem("qst_tarbeck_golden_token")
                        MC @think "Huh? But the wife—"
                        WATCHER "A good performance is a good performance."
                        WATCHER "We look forward to seeing more."
                        hide cg_tarbeck_watcher with easeoutright
                        MARKUS_FEM @happy "See? Worked out fine!"
                        MC @think "I guess so..."
                        #MARKUS_FEM @talk "Come on. We need more tokens, don't we?"
                        #MC @talk "Right..."
                        jump qst_TheTarbecks_Room_Maid_markus_choices
                    "I'm afraid not.":
                        PARTY_GUEST "Hmm... A shame."
                        "The guest turned to leave, tugging his {i}pet's{/i} collar as she followed."
                        MC "(Damn... I hope I didn't screw us out of a token there.)"
                        jump qst_TheTarbecks_Room_Maid_markus_choices

            "Have Marcia suck your cock while you play card games." if "cards" in tmpvar:
                $ tmpvar.remove("cards")
                MARKUS_FEM @surp "You cannot be serious!"
                MC @surprised "But, the toke-"
                show markus_fem at shake
                MARKUS_FEM @angry "The answer is no, fool!"
                MARKUS_FEM @blush "Gods, I'd like to still be able to look you in the eye when all of this is over!"
                MC @think "(I should have probably guessed the answer to that one.)"
                jump qst_TheTarbecks_Room_Maid_markus_choices

            "Have Marcia fetch you drinks" if "drinks" in tmpvar:
                $ tmpvar.remove("drinks")
                MC @smile "Marcia, why don't you fetch me some drinks?"
                MARKUS_FEM @angry "Why don't you fetch them your-"
                "Marcia paused, noticing the unwanted attention of the other participants."
                MARKUS_FEM @surp "{i}*Ahem*{/i} I mean..."
                MARKUS_FEM @happy "Right away!"
                MARKUS_FEM @happy "{i}Master...{/i}"
                scene markus_fem_tarbeck_maid_drinks_1 with dissolve
                $ Pause()
                "With a stiff gait, Marcia crossed the hall to retrieve a small tray of wine."
                "On the way back, his eyes widened as hands swiped out to spank his ass."
                scene markus_fem_tarbeck_maid_drinks_2 with dissolve
                $ Pause()
                "No less than three times, Marcia nearly fumbled, barely keeping the drinks from spilling as hands groped his soft, bouncing ass."
                "Gritting his teeth, Marcia returned to my side, looking ready to murder everyone in the room."
                $ LocFlush()
                show mc at cleft
                show markus_fem at cright_f
                with dissolve
                MARKUS_FEM @angry "H-HERE'S YOUR DRINK, SIR."
                MC @think "Uhh... are you alright?"
                MARKUS_FEM @angry "NEVER. BETTER."
                MARKUS_FEM @angry "... Say, wouldn't it be funny if a {i}mysterious{/i} fire started and they were all reduced to charred corpses?"
                MARKUS_FEM @angry "WOULDN'T. THAT. BE. HILARIOUS?"
                "Whether from concern or pure voyeuristic interest, nearly every eye in the room turned toward us."
                MC @scared "{i}Marcia! We're being watched!{/i}"
                MARKUS_FEM @think "{i}H-Huh? U-Uhh...{/i}"
                MARKUS_FEM @think "{i}What do we do exactly?{/i}"
                MC @scared "We need to put on a show!"
                MARKUS_FEM @surp "Well... think of something fast!"
                "I turned to the watching faces, the first idea tumbling from my mouth."
                MC @talk "*AHEM!*"
                MC @smile "I uhh, seem to have misplaced my servant's..."
                MC @think "UHHHH..."
                PARTY_GUEST "Ah, I think I know what you mean."
                PARTY_GUEST "Here, take one of my wife's spares."
                PARTY_GUEST "Don't worry, it hasn't been used."
                "The guest handed over a cut diamond-shaped toy with a polished, phallic metal end."
                "I blinked, then turned to Marcia, whose face went bright red as realization dawned."
                MARKUS_FEM @surp "Y-You want to put-"
                "He glanced at the gathered spectators, sweat trickling down her brow as he forced a smile."
                MARKUS_FEM @happy "O-Of course, master!"
                MARKUS_FEM @happy "T-That's exactly what we were looking for, right?"
                MC @surprised "Uhhh..."
                MC @think "Y-Yes! Exactly!"
                MC @embarr "L-Let's put this in now, shall we?"
                MARKUS_FEM @happy "..."
                MC @smile "..."
                MC @angry "{i}*Whispering*{/i} Bend over. Everyone is watching."
                MARKUS_FEM @angry "{i}*Whispering*{/i} You cannot seriously plan on shoving that up my ass!"
                PARTY_GUEST "... Is there a problem?"
                MC @smile "No, no!"
                MC @smile "She's just shy, that's all."
                MC @smile "Isn't that right, {i}dear?{/i}"
                MARKUS_FEM @blush "Y-Yes."
                PARTY_GUEST "There's nothing to fear."
                PARTY_GUEST "{i}Lord Tarbeck always encourages passion wherever it may be found.{/i}"
                "Marcia pouted, cheeks burning as she muttered under her breath."
                MARKUS_FEM @blush "M-Make sure it's lubed."
                MARKUS_FEM @blush "I don't want to be walking bow-legged all night."
                MC @surprised "Mark- I mean..."
                MC @talk "Marcia..."
                $ PlaySexFx(audio.moans_breaths_loop)
                scene markus_fem_tarbeck_maid_drinks_3 with dissolve
                $ Pause()
                "With a heavy sigh, Marcia turned away, lifting her skirt and tugging down her thin panties."
                "Bending forward, she exposed himself as my cock hardened immediately."
                MARKUS_FEM "*AHEM!*"
                MARKUS_FEM "C-Could you hurry up?"
                MARKUS_FEM "It's definitely not embarrassing at all having you stare back there..."
                MC "R-Right!"
                "I parted one of Marcia's cheeks, instinctively squeezing as she gasped softly."
                "Her body tensed as the toy pressed against her tight rosebud."
                "She winced at first, then exhaled shakily as it slid inside."
                scene markus_fem_tarbeck_maid_drinks_4 with dissolve
                $ Pause()
                $ UnlockGalSceneAndGrantXp("markus", "tarbeck_maid_drinks")
                "Where her asshole had been now glittered a shining diamond."
                MARKUS_FEM "Mmmfghhh!!"
                MARKUS_FEM "I-It's colder than I expected!"
                PARTY_GUEST "That's just the lube."
                PARTY_GUEST "It'll warm up."
                $ StopSexFx()
                "Soft laughter and clinking glasses followed as approval spread through the room."
                MARKUS_FEM "It's... not so bad once you get used to it."
                MARKUS_FEM "{i}My ass still feels full, but-{/i}"
                "He gasped as I squeezed his ass again."
                MARKUS_FEM "What are you doing?!"
                MC "Selling the act."
                MC "The watchers are still looking."
                "Marcia's breathing grew uneven beneath my hand."
                MARKUS_FEM "Never - {i}*Huff*{/i} better!"
                MC "...Was that a moan?"
                MARKUS_FEM "SHUT THE FUCK UP."
                MC "Heh."
                WATCHER "We always appreciate fresh blood."
                WATCHER "Here, for your efforts."
                $ PlayerAddItem("qst_tarbeck_golden_token")
                $ LocFlush()
                show mc at cleft
                show markus_fem at cright_f
                with dissolve
                MC @smile "Great! We got one!"
                MARKUS_FEM @angry "Fantastic. Now excuse me while I find somewhere private to remove this from my ass!"
                show markus_fem at blurin, cright
                hide markus_fem with easeoutright
                show mc at center with ease
                MC @think "(...They seemed to enjoy that more than they'll admit.)"
                scene black with dissolve
                $ Pause(0.25)
                $ LocFlush()
                show mc at cleft
                show markus_fem at cright_f
                with dissolve
                jump qst_TheTarbecks_Room_Maid_markus_choices
    else:
        MARKUS_FEM @talk "I don't think we're going to win anymore tokens here."
        MARKUS_FEM @talk "We should move onto the next room."
        scene black with dissolve
        $ CharSetClothes("markus", "dress")
        $ LocSet("hamun_tarbeck_playhallway")
        jump qst_TheTarbecks_Room_Maid_over

label qst_TheTarbecks_Room_Maid_ves:
    show mc at blurin, cleft_f
    MC @think "Well, what do you think?"
    VES @sad "I... I do not know."
    VES @angry "This play-pretend of submission is not easy for me to do..."
    menu:
        "You're the only one I could trust to ask...":
            pass

        "Then let's do something else.":
            VES @sad "I ... I am sorry to let you down."
            MC @smile "It's fine, come on, let's find another {i}*game.*{/i}"
            VES @talk "Right."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    VES @blush "W-Well, if that is s-so..."
    VES @blush "Umm...V-Very well."
    MC @surprised "What, really?"
    MC @surprised "I didn't think you'd-"
    show ves at shake
    VES @angry "I will do what needs to be done!"
    VES @angry "I am a warrior! I do not run from such things!"
    show cg_tarbeck_watcher at center_f with ease
    "The server handed Ves her maid outfit, and the defiant posture she wore quickly faltered as her green cheeks turned a rosy red."
    show cg_tarbeck_watcher at blurin, center
    hide cg_tarbeck_watcher with easeoutright
    VES @blush "T-This is just..."
    VES @blush "A BATTLE OF WILLPOWER!"
    "She looked down at the outfit once more and gulped."
    VES @blush "G-Give me a moment..."
    scene black with dissolve
    play sound "audio/cfx/clothes_drop.ogg"
    $ CharSetClothes("ves", "maid")
    $ Pause(0.25)
    $ LocFlush()
    show mc at cleft
    show ves at cright_f
    with dissolve
    $ Pause()
    "... A short while later, a sheepish, nervous Ves returned in the lewd attire."
    "The sight of an orc alone was enough to draw attention,"
    "But an orc as striking as Ves, {i}dressed like that,{/i}"
    "I could practically feel eyes burning into the back of my skull."
    VES @blush "This is..."
    VES @blush "{i}Degrading.{/i}"
    MC @think "Are you sure you're alright to continue?"
    "She clenched her hands, nodding with uneasy determination."
    MC @think "Are you sure you're ready for-"
    VES @angry "Stop stalling!"
    show ves at shake
    VES @angry "Order me around already, coward!"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ tmpvar = ["cards", "pet", "drinks"]
    label qst_TheTarbecks_Room_Maid_ves_choices:
    if len(tmpvar) > 0:
        menu:
            "Have Ves crawl around beside you as your pet." if "pet" in tmpvar:
                $ tmpvar.remove("pet")
                play sound "audio/cfx/finger_snap.ogg"
                "I snapped my fingers toward the floor."
                MC "Down."
                VES @think "W-What?"
                VES @angry "Did you just snap your fingers at-"
                MC @serious "..."
                VES @blush "... W-What would you like me to do."
                VES @angry "{i}Master.{/i}"
                MC @talk "On your knees... {i}pet.{/i}"
                "Ves muttered something beneath her breath, but before too many eyes could be drawn to her {i}disobedience,{/i} she carefully lowered herself to the floor."
                window hide
                hide ves
                hide mc
                show cg_ves_maid_leash at center
                with dissolve
                MC @talk "Come."
                play sound "audio/cfx/finger_snap.ogg"
                "I snapped my fingers once more, and Ves visibly winced, as though fighting the urge to snap back."
                "Her cheeks flushed red as she bit her tongue and followed, crawling behind me."
                "For the next half hour, I wandered almost aimlessly around the lobby as Ves followed at my side."
                "Another couple was doing the same, except their wife appeared fully converted, a fake dog tail plugged into her ass."
                PARTY_GUEST "My... an orc bitch."
                PARTY_GUEST "How unique."
                "I could sense Ves' anger simmering, her upper lip trembling as she fought back a snarl."
                MC "Her name is Ves."
                "Before her temper could flare, I gently patted Ves on the head."
                "To my surprise, her expression softened slightly as she looked up at me."
                MC "{i}She's very precious to me.{/i}"
                "Ves' cheeks burned red, her heartbeat loud enough I could almost hear it."
                VES "....M-Mmmm..."
                PARTY_GUEST "... Oh my."
                PARTY_GUEST "How delightful!"
                "The woman panted, wagging her tail as she tilted her head and moved closer, sniffing at Ves curiously."
                "Ves instinctively recoiled slightly from the strange, perverted human."
                PARTY_GUEST "... It seems my wife is interested in your pet orc."
                PARTY_GUEST "Tell me, do you ever allow your bitch to play with other pets?"
                menu:
                    "Let's let them play.":
                        play sound "audio/cfx/body_falling.ogg"
                        scene ves_tarbeck_maid_pet_1 with dissolve
                        $ Pause()
                        GUESTS_PET "{i}*Woof!*{/i}"
                        "The guest's wife leapt toward Ves, pinning her onto the floor."
                        VES "Gahh!"
                        VES "What are you doing?!"
                        VES "H-Human! Ahh!"
                        GUESTS_PET "Woooof..."
                        VES "(What kind of mad place have I followed [player_name!t] into?!)"
                        $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
                        scene ves_tarbeck_maid_pet_2 with dissolve
                        $ Pause()
                        "The woman began to lick and lap at Ves' pussy with her tongue faster."
                        VES "{i}*Huff*{/i} You..."
                        VES "Mmmfghhh..."
                        PARTY_GUEST "... Does an orc's cunt taste different to a human's?"
                        MC "...W-Well."
                        PARTY_GUEST "I only ask because my wife is absolutely lapping her up."
                        PARTY_GUEST "In fact, I haven't seen her this enthusiastic since we broke in her friend."
                        MC "(What?)"
                        "Ves' face strained as though she were resisting the pleasure, but the pet-wife only grew bolder, twisting and burying her tongue deep into Ves' cunt as she grunted happily."
                        VES "{i}*Huff*{/i} Little..."
                        VES "{i}*Huff*{/i} pet is..."
                        $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
                        scene ves_tarbeck_maid_pet_finish with flash
                        $ Pause()
                        VES "H-Hrghhh!!"
                        VES "So good!"
                        GUESTS_PET "{i}*Woof!*{/i}"
                        "As if pleased by the sounds she was drawing out, the pet-wife pulled back for a moment, turning around to—"
                        VES "NO."
                        $ PlaySexFx("audio/sex_sounds/forgean_100_muffled.ogg", 1)
                        scene ves_tarbeck_maid_pet_3 with dissolve
                        $ Pause()
                        "Ves grabbed the pet-wife with both hands."
                        VES "Pet must learn!"
                        "The woman looked confused for a heartbeat, but then she was shoved down and pinned as Ves pressed her ass to the pet-wife's face."
                        GUESTS_PET "ARRRFFFF!?"
                        PARTY_GUEST "U-Uhh! It seems your pet is..."
                        PARTY_GUEST "Ummm... {i}Dominating.{/i}"
                        "Ves held the woman's head in place as she began to grind her pussy against her face."
                        "The woman squirmed, kicking her feet as the powerful orc took what she wanted."
                        VES "Y-Yes... Mmfghh!"
                        scene ves_tarbeck_maid_pet_4 with dissolve
                        $ Pause()
                        "Ves' face, flushed red with arousal, twisted into a lewd, satisfied grin."
                        VES "K-Keep using your tongue like that!"
                        VES "Don't stop! Mmfghh!"
                        "The pet-wife obeyed, greedily pressing her tongue deep into Ves' cunt and thrashing it about."
                        "Their hot moans filled the lobby as eyes were drawn toward us from all around."
                        "A few guests raised their glasses and nodded approvingly as I looked down at the two sweaty, enthralled pets devouring each other."
                        VES "Ahhh...!"
                        VES "Is that— Oooh! All you have, {i}*Huff!*{/i} little pet?"
                        VES "N-No wonder us orcs d-defeat your—"
                        scene ves_tarbeck_maid_pet_5 with dissolve
                        $ Pause()
                        VES "{i}*Gasp!*{/i}"
                        "Ves gasped as she felt the pet-wife's finger slip into her asshole, the sudden sensation catching her off guard."
                        VES "M-My ass!"
                        VES "Your f-finger is in my a-assss!"
                        PARTY_GUEST "Oh dear... My bitch always wants the others to know she's in charge."
                        PARTY_GUEST "I must admit, this is quite the spectacle!"
                        MC "So, should you win the game, what are you-"
                        PARTY_GUEST "Oh, we just come here for the fun now."
                        PARTY_GUEST "{i}We actually won last year's game.{/i}"
                        MC "What?!"
                        PARTY_GUEST "Yes..."
                        "The man looked down at his wife, still lapping up Ves' pussy while she worked at the orcess' tight ass."
                        PARTY_GUEST "{i}We got what we were looking for.{/i}"
                        PARTY_GUEST "Now we just come here for fun."
                        PARTY_GUEST "And you— is there some treasure you seek from Lord Zanzibat?"
                        MC "Of a sort..."
                        PARTY_GUEST "Ahh, interesting."
                        $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
                        scene ves_tarbeck_maid_pet_finish_2 with flash
                        $ UnlockGalSceneAndGrantXp("ves", "tarbeck_maid_pet")
                        $ Pause()
                        VES "A-AHHHHHHHH?!"
                        "Ves shuddered and shook as she was finally brought to climax."
                        "Sweaty and exhausted, Ves rolled off the pet-wife, desperately trying to catch her breath."
                        PARTY_GUEST "I believe your orc has finished."
                        PARTY_GUEST "Have fun, dear?"
                        GUESTS_PET "{i}*Woof!*{/i}"
                        "The guest's wife wiggled her tail, returning to her master's side where she rubbed her face against his leg."
                        "Ves lay sprawled out and breathless, still twitching from her orgasm."
                        VES "I will..."
                        VES "{i}*Huff*{/i} not be..."
                        VES "{i}*Huff!*{/i} defeated! {i}*Huff!*{/i}"
                        PARTY_GUEST  "Well, I must leave you to it."
                        PARTY_GUEST  "... Oh, here, by the way."
                        PARTY_GUEST  "We won't be needing this."
                        "The masked man handed me a small gold token."
                        $ PlayerAddItem("qst_tarbeck_golden_token")
                        MC "Thank you."
                        PARTY_GUEST  "Come now, dear. Let's go find your sister and mother."
                        GUESTS_PET "WOOF!"
                        $ LocFlush()
                        show mc at cleft
                        show ves at cright_f
                        with dissolve
                        MC "(... Did he just say-)"
                        "With shaky legs, Ves dragged herself back to her feet."
                        VES @talk "N-No... Bring her back!"
                        show ves at shake
                        VES @angry "I didn't make her finish!"
                        VES @angry "I will not allow failure to sully my honor!"
                        MC @talk "Come on, Ves. We have other things to do."
                        VES @angry "Tschhhh!"
                        jump qst_TheTarbecks_Room_Maid_ves_choices
                    "I'm afraid not.":
                        PARTY_GUEST  "Hmm... A shame."
                        "The guest turned to leave, tugging on his {i}pet's{/i} collar as she followed."
                        MC "(Damn... I hope I didn't screw us out of a token there somehow.)"
                        jump qst_TheTarbecks_Room_Maid_ves_choices
            "Have Ves pleasure your cock while you play card games." if "cards" in tmpvar:
                $ tmpvar.remove("cards")
                $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
                scene ves_tarbeck_maid_cards_3 with dissolve
                $ Pause()
                "Taking a seat at a table, a woman on her hands and knees sucked at the cock of her partner as he drew some cards."
                PARTY_GUEST  "Ahh! Can I help you?"
                GUESTS_PET "{i}*Slurp!*{/i} Mhmmm..."
                PARTY_GUEST "Ahh! Careful with the teeth, dear."
                GUESTS_PET "Mmm... ❤️"
                PARTY_GUEST "Interested in a game of cards?"
                "I looked toward Ves, whose cheeks burned red as she squirmed uncomfortably on the spot."
                MC "Ves, do you want to play?"
                VES "I..."
                "Ves bit at her lower lip anxiously."
                VES "...Y-Yes."
                MC "Yes what?"
                "Ves' voice sharpened slightly as she frowned."
                VES "Yes, {i}sir.{/i}"
                scene ves_tarbeck_maid_cards_4 with dissolve
                $ Pause()
                "Ves watched as the other woman greedily wrapped her lips around her partner's cock, gliding her head back and forth."
                "Her cheeks burned bright pink as she gulped, sheepishly lowering herself onto her knees between my legs."
                scene ves_tarbeck_maid_cards_idle with dissolve
                $ Pause()
                "She paused for a moment, too nervous to do anything else."
                VES "I... I must look stupid doing this."
                VES "Look at me, I'm nothing but muscles and all of them are just..."
                VES "Soft, skinny things."
                "I smiled softly, reaching over to pet Ves on the head."
                VES "...W-What are you doing?"
                VES "Why are you petting me like that?"
                "I continued to gently pet Ves as I pulled out my cock."
                "Her eyes widened as the hard member stood to attention before her."
                VES "I..."
                VES "{i}*Gulp*{/i}"
                MC "Take your time, Ves."
                MC "Just try to enjoy yourself."
                "Ves nodded sheepishly, though it was clear she was anxious with all the eyes on her."
                $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x2.ogg", 1)
                scene ves_tarbeck_maid_cards_1 with dissolve
                $ Pause()
                "Gulping, Ves grabbed her bare, heavy tits and wrapped them around my cock."
                "Pushing her soft green mounds together, she began to squeeze and bounce them, massaging my member with her large breasts."
                VES "Is this... okay for you?"
                MC "Ahh! Yes, Ves, just—"
                MC "Mhmm, it needs a little more lubricant."
                VES "Lubricant?"
                VES "O-Oh..."
                "Without thinking, Ves drooled down onto my cock, the warm saliva coating my now glistening member as she squeezed tighter with her tits."
                "My cock slid easily between her breasts as Ves, keenly observing my reactions, grinned."
                $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x3.ogg", 1)
                scene ves_tarbeck_maid_cards_2 with dissolve
                $ Pause()
                VES "Ha!"
                VES "Look at the face you're making!"
                VES "See? Could any of these puny human women squeeze you this hard with their chests?"
                VES "That's why an orc trains their body before anything else!"
                "Ves seemed almost oblivious to the lewdness of her actions now, proudly preoccupied with how {i}strong{/i} she was."
                MC "A-Ahh!"
                MC "No— Mhmm! Ves, this feels..."
                MC "F-Fuck me!"
                "Ves flashed her small fangs as she bounced her heavy tits on my cock."
                "Was she treating this like some kind of warped exercise session?"
                VES "We should train your body more together!"
                VES "P-Push it! Push it harder!"
                "If she was, her hot, trembling breath made it clear this was turning her on more than she'd ever admit."
                MC "V-Ves— {i}*Huff*{/i}"
                "Ves grinned, pressing her tits together as she sped up, watching my cock sink into the green flesh."
                VES "We must— {i}*Huff*{/i} train all your muscles!"
                VES "This is— {i}*Huff!*{/i} the only way to— Mhmm!"
                VES "MAKE YOU STRONGER!"
                $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
                scene ves_tarbeck_maid_cards_4 with dissolve
                $ Pause()
                "Behind us, the couple looked on amused, the wife occasionally pulling away to watch curiously."
                PARTY_GUEST "I never knew orcs were so... passionate."
                GUESTS_PET "Is everything a competition with them, you think?"
                PARTY_GUEST "Haha!"
                PARTY_GUEST "What do you need him to be stronger for, orc?"
                scene ves_tarbeck_maid_cards_2 with dissolve
                $ Pause()
                VES "{i}*Huff!*{/i} To be the best— Ahhh! Mate, of course! {i}*Huff!*{/i}"
                MC "V-Ves! Slow down!"
                MC "I'm—"
                VES "{i}*Huff!*{/i} This muscle needs— Ahh!"
                VES "More—"
                VES "TRAINING!"
                $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg")
                scene ves_tarbeck_maid_cards_finish with flash
                $ Pause()
                MC "FUCKKKKKKKKK!"
                "Unable to hold back any longer, Ves gasped as my twitching cock erupted, splattering her face and green tits with my thick, heavy load."
                "She looked almost {i}surprised{/i} that it had happened."
                VES "{i}O-Oh...!{/i}"
                "As my cock deflated between her tits, Ves' cheeks burned red while I wiped sweat from my brow."
                MC "Oh fuck... {i}*Huff*{/i}"
                MC "You've got tits that could crush a man's head, girl!"
                VES "... P-Perhaps I got a little carried away."
                "The couple laughed as the man filled his wife's mouth with his seed."
                $ UnlockGalSceneAndGrantXp("ves", "tarbeck_maid_cards")
                scene ves_tarbeck_maid_cards_finish_2 with flash
                $ Pause()
                PARTY_GUEST "Darling! Next time we visit Skarshire, we should buy one of those orcish whores!"
                PARTY_GUEST "They seem delightful!"
                GUESTS_PET "Mmfghhh! {i}*Slurp!*{/i} Shoundshhghoodhh dhearhh! {i}*Slurp!*{/i}"
                VES "Grrr!"
                $ LocFlush()
                show mc at cleft
                show ves at cright_f
                with dissolve
                "Ves' hands curled into fists, but before she could explode, one of the watchers approached and handed over a golden token."
                show cg_tarbeck_watcher at left with easeinleft
                WATCHER "For the entertainment you have provided this evening..."
                show cg_tarbeck_watcher at nod
                $ PlayerAddItem("qst_tarbeck_golden_token")
                hide cg_tarbeck_watcher with easeoutright
                MC @angry "Focus, Ves— look!"
                VES @angry "I do not like this place."
                VES @angry "Or these people."
                MC @talk "Just bear with it for now."
                VES @blush "...{i}For you.{/i}"
                VES @blush "I shall bear this shame."
                VES @blush "But no one else."
                # Ves exits off-screen to the left <- nope she doesnt, theres a menu to exhaust
                #MC "(I hope Ves can keep it together.)"
                jump qst_TheTarbecks_Room_Maid_ves_choices
            "Have Ves fetch you drinks." if "drinks" in tmpvar:
                $ tmpvar.remove("drinks")
                MC @talk "Ves, fetch me some drinks."
                VES @talk "Of course..."
                VES @angry "{i}Sir.{/i}"
                show ves at blurin, cright
                hide ves with easeoutright
                show mc at center with ease
                "The word came uneasily to Ves as she reluctantly made her way toward the drinks trays."
                "I watched her muscular body push past the guests, many stepping aside nervously for the orcess."
                "Still, watching her toned green ass swing left to right in those lewd panties made my cock stiffen."
                "There was something maddeningly hot about a mighty warrior orc wearing such slutty clothes so brazenly."
                "And despite the nervousness, I wasn't the only one admiring her."
                "With the drinks loaded onto a silver tray, Ves made her way back with her chest puffed out, as if she had something to prove."
                "A guest, laughing softly at a comment, stepped back directly into Ves' path."
                play sound "audio/cfx/bottleBreak.ogg"
                "Ves came crashing into her, dropping the tray as glass shattered across the floor!"
                PARTY_GUEST "Oh! I'm terribly—"
                VES @angry "Are you trying to challenge me?!"
                VES @angry "WHY DID YOU GET IN MY WAY?!"
                PARTY_GUEST "I—"
                "Ves snarled, baring her teeth as her rage exploded, drawing uneasy attention from guests and even the guards."
                show mc at cleft with ease
                show ves at cright with easeinright
                VES @angry "Fool! I should—"
                MC @angry "Ves!"
                MC @angry "That's enough!"
                show ves at blurin, cright_f
                VES @angry "But—"
                MC @angry "It was an accident."
                VES @angry "..."
                show ves at blurin, cright
                "Ves looked around at the partygoers, her expression softening as she realized all eyes were locked on her."
                VES @sad "...I—"
                show ves at blurin, cright_f
                VES @sad "I am sorry."
                VES @sad "I didn't mean to lose my temper."
                PARTY_GUEST "It's... alright."
                "As murmurs grew louder, Ves looked around helplessly, panic filling her eyes."
                "For a moment, I thought she might actually cry."
                VES @sad "T-This was a mistake!"
                show ves at center_f with ease
                "Ves seemed ready to bolt, but I grabbed her wrist."
                show mc at shake
                MC @angry "Wait!"
                VES @sad "But... I messed everything up!"
                MC @angry "You're right..."
                MC @smile "{i}And what happens to a maid when she messes up?{/i}"
                "Ves paused, taken aback."
                VES @think "They... apologize?"
                MC @smile "{i}They get punished.{/i}"
                VES "W-What?"
                scene ves_tarbeck_maid_drinks_1 with dissolve
                $ Pause()
                "I guided Ves toward a chair. With a sharp pull, she suddenly found herself over my lap, her green, fat ass on full display."
                VES "W-WHAT ARE YOU DOING?!"
                MC "Punishing you for being a bad maid."
                $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
                scene ves_tarbeck_maid_drinks_2 with dissolve 
                $ Pause()
                "Ves gasped as my hand collided with her ass, her cheeks jiggling as her eyes widened."
                VES "EEEEEEP!"
                VES "Grrrr! Release me at once!"
                VES "T-This is so..."
                VES "{i}Degrading!{/i}"
                "My hand came down again, her toned green flesh wobbling lightly."
                "Her cheeks burned red as she averted her gaze, yet she didn't try to break free."
                "{i}Instead, she wiggled and pushed her ass out further.{/i}"
                MC "Really now, Ves?"
                MC "{i}Running away from a challenge?{/i}"
                MC "I thought better of you."
                VES "You... YOU!"
                VES "Grrrr! I AM A PROUD ORC!"
                VES "I can take anything a HUMAN throws at me!"
                MC "Is that so?"
                VES "Yes it—"
                "My hand cracked down on her other cheek, the sound ringing through the hall."
                VES "ISSSSSSSSSS!"
                "Her green cheeks flushed pink as she breathed heavily."
                MC "Are you going to apologize to everyone here?"
                VES "TSCH!"
                VES "I did nothing wrong!"
                VES "Everyone was just in my way!"
                MC "Tsk tsk tsk..."
                "{i}*SLAP!*{/i}"
                MC "Apologize."
                VES "No!"
                "{i}*SLAP!*{/i}"
                MC "Apologize."
                VES "N-No!"
                "{i}*SLAP!*{/i}"
                MC "I can keep this up all night!"
                VES "{i}*Huff*{/i} You— {i}*Huff*{/i} cannot— {i}*Huff*{/i}"
                VES "MAKE ME SUBMIT!"
                MC "Wanna bet?"
                VES "Do your wor—"
                scene ves_tarbeck_maid_drinks_3 with dissolve
                $ Pause()
                "She didn't even finish before a flurry of slaps landed, her ass turning a darker red."
                "{i}*SLAP! SLAP! SLAP! SLAP! SLAP!*{/i}"
                "Her eyes watered, mouth agape as she choked on breath and spit."
                VES "{i}*Huff*{/i} You..."
                VES "Mmmfghhh..."
                "A soft, lewd moan slipped free as she trembled."
                "Her pussy glistened, and when my fingers brushed her lips, she moaned again."
                MC "You know..."
                MC "{i}You're quite the little masochist, aren't you?{/i}"
                VES "S-Shut up... Mhmm..."
                "Another slap landed."
                VES "{i}Oh gods...{/i}"
                MC "Are you ready to apologize?"
                MC "{i}Or do I need to make you finish in front of everyone?{/i}"
                VES "Y-You wouldn't dare!"
                MC "Wouldn't I?"
                "Another slap drew more eyes as Ves gasped, saliva glistening as it dripped to the floor."
                VES "Bas— {i}*Huff*{/i} Bastard!"
                MC "APOLOGIZE."
                VES "N-NEVER!"
                "{i}*SLAP!* *SLAP!*{/i}"
                VES "{i}*Huff*{/i} Hrghh!"
                "{i}*SLAP!* *SLAP!* *SLAP!*{/i}"
                VES "Oh gods... {i}*Huff*{/i}"
                VES "P-Please..."
                "{i}*SLAP!* *SLAP!* *SLAP!*{/i}"
                VES "M-Master..."
                VES "Please..."
                VES "My poor ass."
                MC "Are you ready to apologize?"
                VES "{i}*Huff* *Huff*{/i}"
                MC "...Well?"
                VES "..."
                "{i}*SLAP!*{/i}"
                VES "EEEEEEEHHH!!"
                VES "I—I'M SORRY!"
                VES "{i}*Huff*{/i} P-Please..."
                MC "What are you sorry for?"
                "{i}*SLAP!*{/i}"
                VES "EEEP!"
                VES "I'M SORRY! IT WAS MY MISTAKE!"
                "Ves trembled as the crowd began to clap."
                VES "How... {i}*Huff*{/i} humiliating!"
                VES "Mmmfghhh!"
                "Her body spasmed as her eyes rolled back."
                MC "...Did you just finish?"
                VES "S-Stop... put me down!"
                VES "Please! {i}*Huff!*{/i}"
                scene black with dissolve
                $ StopSexFx()
                "... As I slowly lowered Ves back to her feet, she rubbed at her sore butt with shaking legs."
                $ UnlockGalSceneAndGrantXp("ves", "tarbeck_maid_drinks")
                $ LocFlush()
                show mc at cleft
                show ves at cright_f
                with dissolve
                MC @think "Are you okay?"
                VES @angry "You...!"
                VES @angry "That was humiliating!"
                MC @smile "You didn't seem that mad in the end."
                VES @blush "Everyone saw us!"
                MC @smile "Oh? So if we did it in private, that would have been fine?"
                VES @blush "Yes!"
                VES @blush "I mean no!"
                VES @blush "I mean-"
                show ves at shake
                VES @angry "Grrr! Cease these word games!"
                VES "Let us finish these games and be done with this party!"
                show cg_tarbeck_watcher at center_f with easeinright
                WATCHER "A token... for your efforts."
                show cg_tarbeck_watcher at nod
                $ PlayerAddItem("qst_tarbeck_golden_token")
                $ Pause(0.2)
                show cg_tarbeck_watcher at blurin, center
                WATCHER "The crowd always appreciates a {i}unique{/i} spectacle."
                MC @think "Thanks..."
                hide cg_tarbeck_watcher with easeoutright
                MC "(One more token down.)"
                MC @think "(I just hope Ves isn't {i}too{/i} upset about the spanking...)"
                jump qst_TheTarbecks_Room_Maid_ves_choices
    else:
        VES @talk "I tire of this game."
        VES @talk "Let us try a different room before I crush every human here."
        MC @talk "Right, I don't think there's anymore tokens for us to earn here."
        scene black with dissolve
        $ CharSetClothes("ves", "dress")
        $ LocSet("hamun_tarbeck_playhallway")
        jump qst_TheTarbecks_Room_Maid_over

label qst_TheTarbecks_Room_Maid_esme:
    ESME @smile "So... Shall we play?"
    menu:
        "So... Wanna be my slutty little maid?":
            pass

        "This isn't really my sort of thing.":
            ESME @sad "Boo."
            ESME @angry "BOOO THIS MAN!"
            ESME @angry "You have the chance to have a slutty katai maid and you turn it down, really?"
            MC @talk "There are other games to play."
            ESME @angry "Hmph!"
            ESME @sad "I was really looking forward to trying on the outfit!"
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    ESME @talk "Sure, I'm game."
    WATCHER "Perfect, madam."
    WATCHER "Always a pleasure to welcome a new 'maid' to these games."
    "The figure chuckled."
    WATCHER "Come, let's get you your new uniform..."
    hide esme with easeoutright
    show cg_tarbeck_watcher at blurin, cright
    hide cg_tarbeck_watcher with easeoutright
    scene black with dissolve
    "{i}... Shortly later.{/i}"
    $ CharSetClothes("esme", "maid")
    $ LocFlush()
    show mc at cleft
    show esme at cright_f
    with dissolve
    ESME @smile "Meowww..."
    ESME @smile "{i}Howw may I sherve yhuuu mhastahhh?{/i}"
    "Esme struck a playful pose and winked."
    MC @smile "Very cute."
    MC @smile "Are you going to try and keep that voice up the whole time?"
    ESME @smile "No chance."
    "Esme glanced around, eyes moving from couple to couple, maid to master."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    ESME @talk "Sooooo..."
    ESME @talk "What did you want me to do?"
    $ tmpvar = ["pet", "cards", "drinks"]
    label qst_TheTarbecks_Room_Maid_esme_choices:
    if len(tmpvar) > 0:
        menu:
            "Have Esme crawl around as your pet." if "pet" in tmpvar:
                $ tmpvar.remove("pet")
                ESME @smile "Really?"
                ESME @smile "You're gonna make the katai crawl around like a cat?"
                MC @lewd "... Problem?"
                ESME @smile "Mmm... Not at all."
                "With a slight smirk, Esme lowered herself onto the ground."
                window hide
                hide esme
                hide mc
                show cg_esme_maid_leash at center
                with dissolve
                ESME "Meowww..."
                ESME "Where to, mastah?"
                MC "Follow me."
                ESME "Mmm... nope!"
                MC "What?"
                ESME "What's in it for me?"
                MC "Bargaining?"
                ESME "If you expect me to debase myself and crawl around for all these pervs..."
                ESME "You betterrrrr make it interesting."
                "I glanced around for a moment, and then I saw {i}them,{/i} displayed on trays beside the wine and other toys."
                MC "I have just the thing..."
                scene black with dissolve
                ESME "Hmm? What are you doing back-"
                ESME "MEOWWWWWWW!"
                scene esme_tarbeck_maid_pet with dissolve
                $ Pause()
                ESME "That's cheating!"
                MC "What was?"
                MC "Giving my pet some shiny new jewelry?"
                ESME "Mmfghh..."
                "Esme wiggled and squirmed as the jeweled plug shifted inside her ass."
                ESME "Couldn't you have found a smaller one?"
                MC "For your ass?"
                MC "No."
                ESME "Did you just call my ass fat?"
                MC "Enough talking. {i}Follow.{/i}"
                ESME "{i}... Yeshhh mastahh.{/i}"
                "Esme crawled beside me, her huge ass swaying left to right as the jewel shimmered in the light, tucked snugly in her asshole."
                MC "Still with the voice?"
                ESME "Buthh mastahhh, dhon't yhou WHUVVVV ithhh when I thalkkkk liekkkk thishhhh?"
                "As we wandered the room, pausing now and then to chat with passing guests,"
                "Esme hummed happily to herself, clearly enjoying having the room's attention focused on her."
                MC "Don't you love having things shoved up your ass?"
                ESME "... I preferhh mastahh cockhh up there."
                MC "...!"
                ESME "Hahaha!"
                ESME "{i}Made you hard, didn't I?{/i}"
                MC "You are..."
                MC "More trouble than I thought you'd be."
                "Esme laughed again, and one of the watchers approached, clapping softly."
                $ UnlockGalSceneAndGrantXp("esme", "tarbeck_maid_pet")
                WATCHER "You two make quite the adorable little couple, don't you?"
                $ LocFlush()
                show mc at cleft
                show esme at cright_f
                show cg_tarbeck_watcher at left
                with dissolve
                "For the first time, Esme's cheeks flushed a bright pink as she rose to her feet, averting her gaze."
                WATCHER "Here, on behalf of the house."
                show mc at blurin, cleft_f
                show cg_tarbeck_watcher at nod
                "The watcher handed us a golden token."
                $ PlayerAddItem("qst_tarbeck_golden_token")
                WATCHER "Enjoy the rest of your evening."
                hide cg_tarbeck_watcher with easeoutleft
                "As the figure glided away with a curt bow, I turned back to Esme."
                show mc at blurin, cleft
                MC "Well, that's one down."
                ESME "{i}And here I was getting used to being on my hands and knees for you...{/i}"
                MC @smile "I'm sure there's still time."
                #ESME "Mmm, come then. These tokens aren't going to win themselves."
                #MC "Right."
                jump qst_TheTarbecks_Room_Maid_esme_choices
            "Have Esme suck your cock while you play cards." if "cards" in tmpvar:
                $ tmpvar.remove("cards")
                ESME @smile "Fine, but you better win."
                "Making my way toward a table, a man sat there while his partner—presumably his wife—wrapped her lips around his cock as he inspected his deck of cards."
                MC "How about a game of barati?"
                "The man looked over at Esme, then pulled a face of disgust."
                PARTY_GUEST "Why would I choose to play any game with a disgusting katai?"
                MC "What?"
                "Esme retreated behind me, her confidence faltering."
                PARTY_GUEST "These wretches hoard coin and buy up all the damn land and businesses they can!"
                PARTY_GUEST "There's a whole cabal of them, like that wretch Lord Zanzibat!"
                PARTY_GUEST "Always scheming and plotting!"
                SHYAHTAN "({i}This one's lips continue to flap, but he says nothing of value.{/i})"
                SHYAHTAN "({i}We should cut off his head and claim his mate as our own.{/i})"
                "I clenched my fist, my whole body tensing as I imagined how many bones I could break."
                "Then I felt Esme tug at my sleeve."
                ESME "Wait!"
                ESME "Please... It's not worth it."
                "As Esme pulled me away, the man watched smugly."
                MC @angry "Why did you stop me from beating that fool?"
                ESME @sad "Please... It would only make things worse."
                ESME @sad "I can already imagine the town criers."
                ESME @shock "{i}Violent katai attacks rich noble!{/i}"
                MC @sad "But... Esme."
                ESME @sad "No, please."
                ESME @sad "Being a katai is difficult enough already."
                ESME @sad "You want to help me right now?"
                ESME @sad "Don't let one loud-mouthed cuckold ruin our night."
                ESME @sad "Please... Let's focus on the task at hand, alright?"
                MC @talk "... Alright."
                MC @think "... Say, how'd you know he's a cuckold?"
                ESME @smile "Let's just say that in the lady's privy, another man was pounding away at her."
                ESME @smile "One who was {i}not{/i} her husband."
                MC @smile "Ha!"
                ESME @smile "Come on, let's find something else to do..."
                jump qst_TheTarbecks_Room_Maid_esme_choices
            "Have Esme fetch you drinks." if "drinks" in tmpvar: 
                $ tmpvar.remove("drinks")
                ESME @smile "Of course. I'll be right back."
                show esme at blurin, cright
                hide esme with easeoutright
                "As Esme went to fetch the drinks, I watched her round ass sway back and forth as she balanced a tray in one hand."
                "She made her way back, drawing eyes as she passed."
                show esme at center_f with easeinright
                "With a playful curtsey, she handed me a glass."
                ESME @smile "{i}Mi'lord.{/i}"
                MC @smile "You're quite good at that."
                show esme at cright_f with ease
                ESME @smile "Mhmmm..."
                "Deliberately, Esme flicked one of the drinks with her tail, spilling it down her top."
                ESME @smile "Oh nooo~ My perfect slutty maid outfit is all wet."
                ESME @smile "How ever will I dry myself now?"
                MC @smile "What are you planning?"
                MC @smile "You know they'll rush over with towels any second."
                ESME @smile "Mmm..."
                scene esme_tarbeck_maid_drinks_1 with dissolve
                $ Pause()
                "Undoing her top to expose her wet breasts, Esme grinned as she gently guided me down onto a chair and mounted."
                ESME "I was hoping you'd use your tongue to clean me off, master."
                MC "... Oh!"
                MC "Well, you don't need to tell me twice!"
                scene esme_tarbeck_maid_drinks_2 with dissolve
                $ Pause()
                "Esme pulled my head forward as I began to lap up the spilled drink from her breasts."
                ESME "Mmhh... That's it."
                ESME "L-Like that."
                ESME "Haha! Your tongue tickles!"
                "Ignoring her teasing, I buried my face between her tits."
                "She giggled, running her fingers through my hair."
                ESME "Naughty boy~"
                "All eyes were on us again, and feeling mischievous, I latched onto one of her nipples and began to suck."
                "Esme gasped as my free hand fondled her other breast, her nipples hardening like small diamonds."
                ESME "Mmmffhhh!"
                ESME "Very— {i}*Huff*{/i} naughty!"
                "As she giggled, I tugged lightly at her nipples, my teeth teasing one as she moaned softly."
                ESME "Oooooh..."
                ESME "Careful— {i}*Huff*{/i} dear..."
                ESME "They're s-sensitive."
                ESME "Ahhh!"
                ESME "Mmmfff... You're sucking so hard."
                ESME "It almost makes me want to—"
                "She gasped again, brushing her hand affectionately through my hair."
                ESME "{i}Take all you need... fufu...{/i}"
                $ UnlockGalSceneAndGrantXp("esme", "tarbeck_maid_drinks")
                WATCHER "I'm sorry to interrupt."
                $ LocFlush()
                show mc at cleft_f
                show esme at cright_f
                show cg_tarbeck_watcher at left
                with dissolve
                "I pulled back, looking toward the watcher."
                WATCHER "Here."
                show cg_tarbeck_watcher at nod
                $ PlayerAddItem("qst_tarbeck_golden_token")
                "The watcher placed a golden token into my palm."
                MC @think "But... why?"
                MC @talk "Surely there are more, uhh, exciting things than what we just did."
                WATCHER "The affection itself was... stimulating."
                WATCHER "Now, if you'll excuse me, I have other guests to watch."
                WATCHER "Do enjoy the rest of the games."
                hide cg_tarbeck_watcher with easeoutright
                show mc at blurin, cleft
                jump qst_TheTarbecks_Room_Maid_esme_choices
    else:
        ESME @smile "Well, that was easier than I thought."
        MC @smile "Come on. There's more games to play."
        ESME @smile "Right behind you, handsome."
        scene black with dissolve
        $ CharSetClothes("esme", "dress")
        $ LocSet("hamun_tarbeck_playhallway")
        jump qst_TheTarbecks_Room_Maid_over

label qst_TheTarbecks_Room_Maid_over:
    $ tmpvar = {}
    $ QstTheTarbecks().CalcGoldTokens()
    $ QstTheTarbecks().PlayedInRooms.add("maid")
    $ AutoMus(True)
    $ LocEnter()