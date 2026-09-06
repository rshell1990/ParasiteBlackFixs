label qst_jackpot_black_diamond_winward:
    show mr_winward at right_f with dissolve
    show mc at left with easeinleft
    $ GoalComplete(QstTheJackpot, 70)
    $ HouseLockBlackDiamond().canExit = False
    MR_WINWARD @happy "Ahh! You've made it, lad!"
    if config.developer:
        "DEV-ONLY: Autocomplete nijah quest?"
        menu:
            "Yes":
                $ QstStart(QstDamzelInDiztrezz)
                "DEV-ONLY: What happened during nijah quest?"
                menu:
                    "frontal assault":
                        $ QstDamzelInDiztrezz().PlayerChoseFrontalAssault = True
                    "assassinated tarek w/poison":
                        $ QstDamzelInDiztrezz().PlayerAssassinatedTarek = True
                    "sold nijah":
                        $ QstDamzelInDiztrezz().PlayerSoldNijah = True
                    "made tarek leave with evidence":
                        $ QstDamzelInDiztrezz().PlayerMadeTarekLeaveEvidence = True
                    "made tarek leave with lies":
                        $ QstDamzelInDiztrezz().PlayerMadeTarekLeaveInquisitors = True
                    "killed tarek with vulshan help":
                        $ QstDamzelInDiztrezz().PlayerSidedWithVulshan = True
                $ QstComplete(QstDamzelInDiztrezz)
            "No (don't change anything)":
                pass

    MC @angry "What are you doing here?"
    MR_WINWARD @think "Remember that high stakes game I talked about?"
    MR_WINWARD @happy "We're having it here!"
    MC @angry "Are you insane? The Black Diamond is-"
    show cg_bandit at center_f with dissolve

    BANDIT "Is this your friend?"
    "The shady-looking guard strolled over towards us."
    MR_WINWARD @happy "Ahh! Yes! This gentleman right here is my friend!"

    if QstIsOver(QstDamzelInDiztrezz):
        if QstDamzelInDiztrezz().PlayerChoseFrontalAssault:
            jump qst_jackpot_black_diamond_damzel_assault
        if QstDamzelInDiztrezz().PlayerAssassinatedTarek:
            jump qst_jackpot_black_diamond_damzel_assassinated
        if QstDamzelInDiztrezz().PlayerSoldNijah:
            jump qst_jackpot_black_diamond_seat_ready
        if QstDamzelInDiztrezz().PlayerMadeTarekLeaveEvidence or QstDamzelInDiztrezz().PlayerMadeTarekLeaveInquisitors:
            jump qst_jackpot_black_diamond_damzel_tarek_left
        if QstDamzelInDiztrezz().PlayerSidedWithVulshan:
            jump qst_jackpot_black_diamond_damzel_vulshan
    else:
        jump qst_jackpot_black_diamond_seat_ready

label qst_jackpot_black_diamond_damzel_vulshan:
    VULSHAN_GUARD "...Ahh! Good to see you again, friend!"
    VULSHAN_GUARD "A friend of the Vulshan is always welcome here!"
    MR_WINWARD @think "You uhh, know these fellows?"
    VULSHAN_GUARD "Haha... We owe a good debt to your friend here, Mr Winward."
    MR_WINWARD @happy "WELL THEN! How about we go play some cards, and you boys-"
    MC  "Go order a drink at the bar and wait, Mr Winward."
    MR_WINWARD @shock "Ehh?"
    MC @serious "Just do it."
    MR_WINWARD @angry "Bah! Fine Fine! No need to yell!"
    hide mr_winward with dissolve
    "Mr Winward briefly slumped off to grab a drink, leaving me alone to chat to the Vulshan guard briefly."
    show cg_bandit at cright_f with easeoutright
    show mc at cleft with easeinleft
    MC  "What are the stakes?"
    VULSHAN_GUARD "Hm? The high roller game? Five thousand coins iz the minimum buy-in."
    MC "(FUCK! That idiot's going to bankrupt himself and Kionni! What the hell is he thinking playing stakes like those?!)"
    MC  "I want you to stop Mr Winward playing, or at least make sure he still walks away with most of his coin."
    VULSHAN_GUARD "I'm sorry, friend, I cannot do that."
    MC @think "Why not?"
    VULSHAN_GUARD "Many of the top gang bosses and merchants attend the games; once your name iz on the list, you're {i}expected{/i} to show, else there's a forfeit cost of the buy-in."
    VULSHAN_GUARD "For most of the big players, this coin iz nothing, but uhhh, I take it losing that kind of coin iz not an option for your friend?"
    MC @serious "Not in the slightest."
    VULSHAN_GUARD "Hmm... I do have an idea, friend."
    VULSHAN_GUARD "I could ply Mr Winward with some drinks and a couple of girls in one of the private rooms."
    VULSHAN_GUARD "Then, I could have {i}Crystal eyes{/i} play in Mr Winward's place."
    MC @think "Crystal eyes?"
    VULSHAN_GUARD "Old gambling shark who owes us a couple of favors."
    VULSHAN_GUARD "I could ask him to take Mr Winward's place; none of the other players will be the wiser."
    MC @think "Will he win?"
    VULSHAN_GUARD "Heh, he could, {i}but he won't.{/i}"
    VULSHAN_GUARD "There'll be too many questions if some newcomer just wins the big game; too many questions are bad for business."
    VULSHAN_GUARD "We'll tell Crystal Eyes to win {i}just enough{/i} so your friend Zer can walk away with some coin, but he won't walk away with the full haul."
    VULSHAN_GUARD "Iz all I can think of..."
    MC "(Hmm, I don't like the idea of putting my faith in someone called {i}Crystal eyes{/i} but the Vulshan vouches for him...)"
    MC @think "(Should I really trust them though? Favor or not, {i}they are criminals.{/i})"
    VULSHAN_GUARD "Let me know your choice..."
    hide cg_bandit with dissolve
    "The Vulshan guard turned and left."
    jump qst_jackpot_black_diamond_winward_waits_for_game

label qst_jackpot_black_diamond_damzel_tarek_left:
    VULSHAN_GUARD "You... You were the last one to see Tarek before he vanished!"
    MC @serious "({i}Fuck.{/i})"
    MC @angry "I have no idea what you're talking about."
    VULSHAN_GUARD "Iz that so?"
    VULSHAN_GUARD "Perhaps I should speak to the others, see if {i}they{/i} remember you."
    MR_WINWARD @think "You uhh, you two know each other?"
    MC  "Go order a drink at the bar and wait, Mr Winward."
    MR_WINWARD @shock "Ehh?"
    MC @serious "Just do it."
    MR_WINWARD @angry "Bah! Fine Fine! No need to yell!"
    "Mr Winward briefly slumped off to grab a drink, leaving me alone to turn my attention back to the Vulshan guard briefly."
    hide mr_winward with dissolve
    MC  "What do you want?"
    VULSHAN_GUARD "Give me one good reason why I should not have you and your friend cut up into small pieces and fed to a Basark?"
    if QstDamzelInDiztrezz().PlayerMadeTarekLeaveEvidence:
        menu:
            "Would some coin keep your mouth shut?" (Req_Gold = 300):
                $ PlayerRemItem("gold", 300)
                "As I handed the bandit the bag of coin, he felt the weight with his hand and nodded."
                VULSHAN_GUARD "...Finish whatever business you have with your friend and leave."
                VULSHAN_GUARD "Do not linger, others may... {i}ask their own questions.{/i}"
                hide cg_bandit with dissolve

            "Because I'll turn this place into a bloodbath?" (Req_Perk = "terrifying"):
                VULSHAN_GUARD "You...!"
                VULSHAN_GUARD "Do whatever it iz you've come to down and then get the fuck out!"
                VULSHAN_GUARD "I - I mean it!"
                "The Vulshan guard quickly scurried away."
                hide cg_bandit with dissolve
                MC "({i}*Sigh*{/i})"
                MC "(That was a close one.)"

            "Tarek fled because the Vulshan and the Khazahs were about to kill him!":
                VULSHAN_GUARD "...You lie."
                MC @serious "Do I?"
                MC  "The Vulshan and Khazah leaderships knew he was trying to weaken them by handing over their territory."
                VULSHAN_GUARD "Why would he do such a thing?"
                MC  "To try and stabilize his control, the Vulshan and Khazah are too powerful and volatile to control easily. Smaller gang territories are easier to manage in case one steps out of line."
                VULSHAN_GUARD "...I see."
                VULSHAN_GUARD "Tarek was good to me. If what you say is true, I and many of the others here will look the other way at your presence."
                VULSHAN_GUARD "But be warned, other Vulshan and Khazahs, those with more loyalty to the rest of the leadership will not take kindly to your actions here..."
                MC  "...Noted."
                "The Vulshan guard turned and left without saying another word."
                hide cg_bandit with dissolve
                MC "(That was close...)"
                MC "(I better figure something out fast.)"

    if QstDamzelInDiztrezz().PlayerMadeTarekLeaveInquisitors:
        menu:
            "Would some coin keep your mouth shut?" (Req_Gold = 300):
                $ PlayerRemItem("gold", 300)
                "As I handed the bandit the bag of coin, he felt the weight with his hand and nodded."
                VULSHAN_GUARD "...Finish whatever business you have with your friend and leave."
                VULSHAN_GUARD "Do not linger, others may... {i}ask their own questions.{/i}"
                hide cg_bandit with dissolve

            "Because I'll turn this place into a bloodbath?" (Req_Perk = "terrifying"):
                VULSHAN_GUARD "You...!"
                VULSHAN_GUARD "Do whatever it iz you've come to down and then get the fuck out!"
                VULSHAN_GUARD "I - I mean it!"
                "The Vulshan guard quickly scurried away."
                hide cg_bandit with dissolve
                MC "({i}*Sigh*{/i})"
                MC "(That was a close one.)"

            "I had a tip and warned Tarek a raid from inquisitors was coming soon. (Lie)":
                VULSHAN_GUARD "There was no raid! This is a lie, a sham!"
                menu:
                    "What are you talking about? The raid hasn't happened yet!":
                        VULSHAN_GUARD "You expect me to believe zat nonsense?!"
                        hide cg_bandit with dissolve
                        "The Vulshan guard turned and left without saying another word."
                        MC "(Something tells me that went badly...)"

                    "The only reason there wasn't a raid is because Tarek {i}left.{/i}" (Req_Charm = 8):
                        MC @angry "They were hunting him; once they got word he had left the city, they moved their searches elsewhere to find him."
                        MC @angry "Without my warning, he was a dead man walking."
                        VULSHAN_GUARD "...I do not know whether you tell the truth, but I shall warn you now."
                        VULSHAN_GUARD "Tarek was good to me; if what you say is true, I and many of the others here will look the other way to your presence here."
                        VULSHAN_GUARD "But be warned, other Vulshan and Khazahs, those with more loyalty to the rest of the leadership will not take kindly to your actions here..."
                        MC  "...Noted."
                        hide cg_bandit with dissolve
                        "The Vulshan guard turned and left without saying another word."

    jump qst_jackpot_black_diamond_winward_waits_for_game

label qst_jackpot_black_diamond_damzel_assassinated:
    VULSHAN_GUARD "...You... You were there the night Tarek died!"
    MC "(Fuck.)"
    MC  "No idea what or who you're talking about."
    VULSHAN_GUARD "I remember... I escaped amidst all zer carnage."
    MC @think "I think you have the wrong person friend, I have no idea what you're talking about..."
    VULSHAN_GUARD "Iz that so?"
    MR_WINWARD @think "You uhh, you two know each other?"
    MC  "Go order a drink at the bar and wait there, Mr Winward."
    MR_WINWARD @shock "Ehh?"
    MC @serious "Just do it."
    MR_WINWARD @angry "Bah! Fine Fine! No need to yell!"
    "Mr Winward briefly slumped off to grab a drink, leaving me alone to turn my attention back to the Vulshan guard briefly."
    MC @serious "What do you want?"
    VULSHAN_GUARD "From {i}you?{/i}"
    VULSHAN_GUARD "...{i}Nothing.{/i}"
    VULSHAN_GUARD "I hope you enjoy your evening here tonight."
    VULSHAN_GUARD "Spend lots of coin and enjoy yourself..."
    VULSHAN_GUARD "The Vulshan never forgets to pay back one of its..."
    VULSHAN_GUARD "{i}Friends.{/i}"
    "Without saying another word, the Vulshan guard turned and left."
    MC "(...Shit.)"
    MC "(This is bad...)"
    hide cg_bandit with dissolve
    jump qst_jackpot_black_diamond_winward_waits_for_game

label qst_jackpot_black_diamond_damzel_assault:
    $ VULSHAN_GUARD = Character("Khazah Guard")
    VULSHAN_GUARD "Hello friends, the Khazah welcomes you to the Black Diamond..."
    MC @think "The Khazhah? I thought this was still Vulshan territory?"
    "The Khazah guard raised a curious brow."
    VULSHAN_GUARD "It iz strange one such as you knows who we are."
    VULSHAN_GUARD "Most just assume all Ramonian families are the same."
    MC  "I have Ramonian friends."
    VULSHAN_GUARD "I zee..."
    VULSHAN_GUARD "There was... {i}An incident.{/i}"
    VULSHAN_GUARD "Tarek is dead, and with his death, the agreement for the Black Diamond to be uhh, as you would say, {i}neutral ground,{/i} went with him."
    MC  "Ah..."
    VULSHAN_GUARD "Not to worry, Khazah will run this place better than Vulshan ever could."
    VULSHAN_GUARD "{i}*Chuckles*{/i}"
    VULSHAN_GUARD "Your friends seat at the table iz ready."
    VULSHAN_GUARD "We shall announce soon when the players are to take their seats."
    VULSHAN_GUARD "We hope you both enjoy zer rest of your evening..."
    "The Khazah bowed gracefully before turning to leave."
    hide cg_bandit with dissolve
    jump qst_jackpot_black_diamond_winward_waits_for_game

label qst_jackpot_black_diamond_seat_ready:
    VULSHAN_GUARD "Your seat at the table iz ready."
    VULSHAN_GUARD "We shall announce soon when the players are to take their seats."
    MR_WINWARD @happy "Wonderful! Simply wonderful!"
    "The Vulshan guard turned and left without another word."
    hide cg_bandit with dissolve
    jump qst_jackpot_black_diamond_winward_waits_for_game

label qst_jackpot_black_diamond_winward_waits_for_game:
    show mc at cleft with easeinleft
    show mr_winward at cright_f with easeinright
    MC @angry "Do you have any idea what you've gotten yourself into?"
    MC @angry "The Vulshan? Khazahs? Do you have a death wish?"
    MR_WINWARD @angry "Of course not, boy!"
    MR_WINWARD @shock "But the chance to win here could be life-changing!"
    MC @angry "{i}Yes, being dead is quite the life-changing event...{/i}"
    MR_WINWARD @angry "I'm already dead, boy! I've been living a shell of a life for YEARS!"
    MR_WINWARD @angry "Either you are with me, boy, or you're not!"
    MR_WINWARD @angry "One way or another, I'm going to sit at that table!"
    show mr_winward at blurin, cright
    hide mr_winward with easeoutright
    $ GoalShow(QstTheJackpot, 80)
    "As Mr Winward, in a huff, turned to grab another drink as he waited for the game to begin."
    MC "(Fuck... What are my options here?)"
    $ QstSetProgress(QstTheJackpot, 5)
    $ LocEnter()

label qst_jackpot_black_diamond_winward_2:
    show mr_winward at center_f with dissolve
    MR_WINWARD  "Well? What is it?"
    menu:
        "I'll play at the table in your place.": 
            MR_WINWARD @shock "Really?"
            MR_WINWARD @happy "Heheeeee! Sounds like a plan, me boy!"
            $ GoalComplete(QstTheJackpot, 80)
            MR_WINWARD @happy "I'll wait here for your return."
            MC  "...Right."
            "After some patient waiting, a loud gong rang out, and the various players rose and gathered as two huge metal doors slowly creaked open."
            MC "(Fuck... What trouble have I landed myself in now?)"
            MR_WINWARD @laugh "Make us rich lad! Heh!"
            MR_WINWARD @happy "Oh, and don't forget this!"
            "Mr Winward handed me over his buy-in, a large bag of coins."
            "Shaking my head, I headed into the private game room."
            hide mr_winward with dissolve
            show mc at center with easeinleft
            "Inside, a few figures sat around a large, ornate table, one or two of which briefly looked up to meet my eyes before looking away once more."
            "I didn't recognise anyone in the room, but from the silk fabric of many of their gowns and ornate jewelry they wore, they were either rich merchants or possibly some may have even been low lords." 
            "The same, scantily clad women served and poured their drinks, and around the room, silent, but ever present, the guards waited and watched."
            "One of the guards approached, his dialect unusually crisp clear Alderian for a Ramonian."
            VULSHAN_GUARD "Gentlemen ... The game for today is..."
            VULSHAN_GUARD "{i}Barati.{/i}"
            VULSHAN_GUARD "If you are not already seated, please, take your designated seat."
            scene cg_cardtable with dissolve
            "(Barati game is under construction!)"
            MC "(Well, that's one good thing at least.)"
            MC "(...Can {i}you{/i} help me out once more here?)"
            BLACK "({i}Yes... Though the players here are much calmer, it shall be more difficult to predict when one is lying.{/i})"
            MC "(I guess it's better than nothing.)"
            "Taking a seat at the table, each of the members placed their buy-ins onto silver trays that were taken away."
            "After a brief, quick period of the coin being counted, there was a nod from one guard to the next."
            VULSHAN_GUARD "Now that everyone's initial bet is in, The first hand shall be dealt."
            VULSHAN_GUARD "Remember, you {i}*Must*{/i} match the buy-in of your opponent for each round."
            VULSHAN_GUARD "Should your funds run low, you may agree to increase your buy-in to keep playing."
            VULSHAN_GUARD "The game only ends with the ringing of the gong once more or if a player cannot replenish his funds."
            VULSHAN_GUARD "Good luck, may the gods smile fortune upon you..."
            "As the guard stepped back, we each announced our buy-in and the cards were dealt onto the table in front of each of us."
            jump qst_jackpot_black_diamond_game

        "Is your percieved honor and love of coin really worth more to you than your life?":
            MR_WINWARD @sad "{i}*Sigh*{/i}"
            MR_WINWARD @sad "You just don't get it lad, do you?"
            MR_WINWARD  "Do you have any idea what it's like to have everything and feel it slip between your fingers?"
            MR_WINWARD  "To see those who you always gave to readily, always supported in their time of need... Betray and abandon you like the flip of a coin?"
            MR_WINWARD  "We used to trade our goods as far as Skarshire and Synmaria."
            MR_WINWARD  "Now... Now we have nothing, and all of our {i}friends{/i} are either dead or have turned their backs on us."
            MR_WINWARD  "We were once invited to the finest banquets at the behest of great lords, invited to craft boots as a gift for overseas lords on their hunting trips."
            MR_WINWARD @angry "We can afford bread, soup, and the roof over our heads."
            MR_WINWARD @angry "Perhaps my wife is happy to settle, live and accept it's all gone."
            MR_WINWARD @angry "But not me! I've worked too hard for it to end like this!"
            MR_WINWARD @angry "{i}I must{/i} keep going till the end!"
            MC "(There's no talking him out of this... Damn.)"
            $ LocEnter()
        
        "Nothing for now, I'm still working on a solution...":
            MR_WINWARD @angry "The solution is to WIN boy!"
            MR_WINWARD  "Bahh! I'm gonna grab another drink! You can dither as much as you like!"
            $ LocEnter()
   

label qst_jackpot_black_diamond_game:
    menu:
        "(WIP) Win": # barati entry point
            "Looking down, bags of coins surrounding me, it dawned on me I'd somehow won."
            $ QstTheJackpot().WonBDSolo = True
            MC @smile "(It worked!)"
            MC "(That old prick is going to be pleased with this.)"
            VULSHAN_GUARD "The games have now concluded. Gather up your earnings when ready, and please return to the main hall,"
            VULSHAN_GUARD "Where complimentary drinks and {i}entertainment{/i} shall be given to you all for the remainder of your evening."
            "As the huge metal doors creaked open, everyone gathered up their belongings as I followed out behind them."
            "I handed over Mr Winward his share, taking some of the profits for myself."
            $ PlayerAddItem("gold", 400)
            MR_WINWARD @happy "Heehee! I knew I could count on ya, boy!"
            MC  "I hope you remember your end of the deal..."
            "Mr Winward pondered the thought for a moment."
            MR_WINWARD @think "My end of the-"
            MR_WINWARD @shock "OH!"
            MR_WINWARD  "You mean me wife?"
            MR_WINWARD @think "Fine, you can lay with her a night... Not sure why you'd even want to."
            MC "(A night?)"
            MR_WINWARD  "Come now, let's leave this place."
            jump qst_jackpot_after_diamond_game

        "(WIP) Lose":
            "As the gong rang out, I looked down to see I had lost."
            $ QstTheJackpot().LostBDSolo = True
            MC "(...Fuck.)"
            MC "(The old man isn't going to be happy about this.)"
            VULSHAN_GUARD "The games have now concluded. Gather up your earnings when ready, and please return to the main hall,"
            VULSHAN_GUARD "Where complimentary drinks and {i}entertainment{/i} shall be given to you all for the remainder of your evening."
            "As the huge metal doors creaked open, everyone gathered up their belongings as I slumped out behind them."
            MR_WINWARD @happy "Well? How much did ya win boy?"
            MR_WINWARD @shock "...Where's... Where's all the coin?"
            MC @think "W-Well, you see..."
            MR_WINWARD @shock "...You...You lost, didn't you?"
            MR_WINWARD @angry "YOU BLEEDIN' IDIOT! HOW COULD YOU LOSE LIKE THAT?!"
            MR_WINWARD @angry "That's it! I've had enough of ya!"
            "In a fit of rage, Mr Winward stormed off before I could stop him."
            MC "(Shit, I should follow him before he does something even more reckless!)"
            jump qst_jackpot_after_diamond_game

################################################################################################################
#If the player decides/he can ask the Vulshan guard for help - AVAILABLE ONLY IF PLAYER HELPED VULSHAN TAKEOVER
label qst_jackpot_black_diamond_vulshan_distraction:
    show cg_bandit at center_f with dissolve
    VULSHAN_GUARD "Have you given my proposal some thought?"
    menu:
        "Tell 'Crystal eyes' the deal is on.":
            VULSHAN_GUARD "Very good."
            $ QstSetProgress(QstTheJackpot, 6)
            $ GoalComplete(QstTheJackpot, 80)
            VULSHAN_GUARD "I shall send some of the girls over towards your friend, and they shall keep him occupied."
            MC @think "How do you plan to stop him from hearing the announcement?"
            VULSHAN_GUARD "Haha, let's say his drinks shall be a little {i}stronger{/i} than we usually serve..."
            VULSHAN_GUARD "He won't even remember when he woke up that there was a game."
            MC "Very well then, let's do this..."
            scene black with dissolve
            "What happened afterwards fell into place fairly quickly."
            "Two of the girls ushered away Mr. Winward to one of the private rooms, already tipsy and more than happy to let two beautiful women distract him; he melted easily in their hands."
            "Now, free from having to worry about that moron losing all his coin, I asked if I was to meet with 'Crystal eyes,' but the Vulshan guard simply raised his hands in protest."
            VULSHAN_GUARD "No, boss, it's best you don't meet."
            VULSHAN_GUARD "Best you stay away, just in case someone has seen us talking."
            VULSHAN_GUARD "Once the game iz over, come speak to me."
            VULSHAN_GUARD "Don't worry, I have just the thing to keep you occupied in one of the private rooms, haha..."
            "With the loud ringing of a gong, some of the players and their bodyguards began to make their way towards another private chamber."
            VULSHAN_GUARD "The game is beginning... I must go..."
            $ GoalShow(QstTheJackpot, 85)
            "The Vulshan guard turned and left to join the others; the bulky metal doors were then closed with a low 'THUD' behind them."
            MC "Hmm, what should I do now?"
            $ LocEnter()

        "Nevermind.":
            MC "I'm still considering it."
            VULSHAN_GUARD "The game starts soon."
            VULSHAN_GUARD "Consider my offer, friend."
            $ LocEnter()

label qst_jackpot_black_diamond_vulshan_checkup:
    MC "(Do I really want to see what that old man is getting up to?)"
    menu:
        "Yes.":
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
            $ QstTheJackpot().VulshanRouteSeenCheckupScene = True
            scene black with dissolve
            scene bd_girls_jackpot_oldman_slow with dissolve
            $ Pause()
            "As I creaked open the door to inspect the old man, Mr. Winward drunkenly waved a half-drunk bottle as two of the girls pleasured him, stroking him together as they gently ran their tongues on his body."
            MR_WINWARD "I'm gonna be - {i}*Hiccup!*{/i} A richhh mhann shoonnn!"
            MR_WINWARD "Hehehe! Yhou ladies shureee are - Mhmm! P-Pretty!"
            BLACK_DIAMOND_PROSTITUTE "Oh yes! You shall be zuch rich man!"
            OTHER_BLACK_DIAMOND_PROSTITUTE "Iz this fool even listening?"
            BLACK_DIAMOND_PROSTITUTE "Shhh! Just keep him happy new girl!"
            scene bd_girls_jackpot_oldman_fast with dissolve
            $ Pause()
            "The two woman laughed and played along, stroking the old man's cock faster as he grunted and groaned happily."
            "Every so often he'd take a swig from the bottle, or attempted to grope the service girls breasts or asses."
            MR_WINWARD "Ahhh! Shooo mhuchh! Mhmm! Bhetter thannn - {i}*Hiccup!*{/i} Thathhh oldhhh bitchh! Hehe!"
            OTHER_BLACK_DIAMOND_PROSTITUTE "{i}Who is he talking about?{/i}"
            BLACK_DIAMOND_PROSTITUTE "{i}No idea, just smile and let us finish him quickly!{/i}"
            "As the two women continued to stroke at the old man's cock, eventually, his piggish grunts and moans of pleasure rose and rose until..."
            $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
            $ UnlockGalSceneAndGrantXp("bd_girls", "jackpot_oldman")
            scene bd_girls_jackpot_oldman_finish with flash
            $ Pause()
            MR_WINWARD "OOOOOOOOOOOOH!"
            "The old man finally finished, covering the girls hands in his warm seed."
            OTHER_BLACK_DIAMOND_PROSTITUTE "{i}Urghh! Now what?{/i}"
            BLACK_DIAMOND_PROSTITUTE "{i}Must I teach you everything? Clean him up!{/i}"
            "I pulled back, gently closing the door shut."
            MC "(Well, I think I've seen enough of that.)"
            $ AutoMus(True)
            $ LocEnter()

        "No.":
            MC "(I think I'll pass on the free nightmare.)"
            $ LocEnter()

label qst_jackpot_black_diamond_vulshan_couch:
    MC "(Should I just chill until the game ends?)"
    menu:
        "Relax...":
            "Sitting back into the soft furniture, I drank a couple drinks offered freely to me as the time passed by."
            "Eventually, the doors swung open and the players began to slump out of the room, one by one..."
            "The same guard approached me, palming off a large bag of coins to me."
            VULSHAN_GUARD "It was good to see you again, friend."
            VULSHAN_GUARD "Come back again anytime..."
            "Without another word, the guard slipped away as old man Winward stumbled his way down the stairs clutching his head."
            MR_WINWARD  "Urghh... What happened?"
            MR_WINWARD  "Did... Did we win?"
            MR_WINWARD @think "Last thing I remember, I was ... I was..."
            $ QstTheJackpot().WonBDWithVulshanHelp = True
            MC "Yes, we won."
            $ GoalComplete(QstTheJackpot, 85)
            MC "Now come on, let us leave this place."
            MR_WINWARD @sad "{i}Urghhhh... My head...{/i}"
            jump qst_jackpot_after_diamond_game

        "Not yet.":
            MC "(I think I'll take a look around for a little longer.)"
            $ LocEnter()

label qst_jackpot_after_diamond_game:
    scene black with dissolve
    $ QstSetProgress(QstTheJackpot, 70)

    $ LocSet("novaras_dist_pleasure")
    $ LocFlush()
    show mc at cleft
    show mr_winward at cright_f
    with dissolve
    $ HouseLockBlackDiamond().canExit = True
    if QstTheJackpot().WonBDWithVulshanHelp:
        MR_WINWARD @sad "I swear I... Urghh... My head!"
        MR_WINWARD @shock "Did I... Win?"
        MC "Of course you did!"
        MC "We have the coin to prove it, don't we?"
        MR_WINWARD @sad "I swear I ... I remember some girls and-"
        MC @serious "Mr Winward, let's just go already."
        MR_WINWARD @sad "Right, right... Lead the way, ahh..."
        MR_WINWARD @sad "{i}My head is killing me.{/i}"
        $ GoalShow(QstTheJackpot, 100)
        $ LocEnter()

    if QstTheJackpot().WonBDSolo:
        $ GoalComplete(QstTheJackpot, 90)
        MR_WINWARD @happy "Come now, lad."
        MR_WINWARD @think "In my experience with places like these, once you've won, you need to leave as soon as possible!"
        MC  "Lead the way, I'll make sure no one is following us."
        $ GoalShow(QstTheJackpot, 100)
        $ LocEnter()

    if QstTheJackpot().LostBDSolo:
        $ GoalFail(QstTheJackpot, 90)
        MR_WINWARD @angry "Well, I hope you're fucking happy!"
        MR_WINWARD @angry "You've ruined me, boy, RUINED ME!"
        MC @angry "The last thing you should have been doing, you fool, is gambling all your coin away in a place like that!"
        MR_WINWARD @angry "BAH! You wanted me to lose my coin, didn't you?"
        MR_WINWARD @angry "I bet that old bitch put you up to this, didn't she? Hm?"
        BLACK "(This male is proving to be increasingly an obstacle to our objectives... {i}Shall we eliminate him as a threat?{/i})"
        menu:
            "I will get the coin elsewhere.":
                MR_WINWARD @angry "Hmph!"
                MR_WINWARD @angry "I'll believe it when I bloody see it!"
                hide mr_winward with dissolve
                "Angrily, Mr Winward stormed off."
                MC "{i}*Sigh*{/i}"
                $ GoalShow(QstTheJackpot, 100)
                $ LocEnter()

            "Kill Mr. Winward" (Req_Perk = "terrifying"):
                "I couldn't hold it back any longer... More and more, I felt the dark rage swelling inside of me."
                "Consuming all of my thoughts, reason and logic was pushed away some place it could no longer be heard."
                MR_WINWARD @shock "I ... Why are you looking at me like-"
                $ AutoMus(False)
                stop music fadeout 0.5
                play ambience2 "audio/ambience_scenes/whispers.ogg"
                play sound "audio/cfx/darkness_erupt.ogg"
                scene cg_winward_kill with flash
                "With a quick swipe of my hand, the tentacle bolted out from my hand at such speed Mr Winward would have had zero chance to react."
                $ CharKill("mr_winward")
                $ CharAddRelEntry("mr_winward", "killed_by_mc_jackpot")
                $ QstTheJackpot().MrWinwardDead = True
                "The tentacle slashed perfectly clean through Mr Winward's head, and I watched as it rolled across the cobblestone floor."
                "His lifeless body collapsed onto the ground almost instantly, blood pooling from the open wound of his neck."
                $ LocFlush(dissolve)
                show mc at center with easeinleft
                "Realising what I'd just done, a momentary panic washed over me."
                MC @scared "(O-Oh f-fuck! What have we just done?!)"
                BLACK "({i}Let us leave this place. Quickly.{/i})"
                hide mc with easeoutright
                scene black with dissolve
                "Before I could let the gravity of my cold-blooded actions weigh me down, I fled quickly before anyone might stumble upon the ghastly scene."
                MC "(Mrs Winward, she'll-)"
                BLACK "({i}Never need to know... Her foolish husband simply stumbled upon the {i}wrong{/i} people and paid the price.{/i})"
                BLACK "({i}By my estimates, there was an eighty-four-point-six percent chance his outcome was an inevitability anyway on his current reckless path.{/i})"
                "Somehow, the cold calculations of my dark passenger made my horrific crime ever so slightly more tolerable to me... If only a little."
                BLACK "({i}Now we must claim his mate and make her satisfied.{/i})"
                MC "(...You can be terrifying sometimes, you know that?)"
                BLACK "({i}Evidently, so can you...{/i})"
                stop ambience2 fadeout 5.0
                $ AutoMus(True)
                $ GoalShow(QstTheJackpot, 100)
                $ LocSet("novaras_dist_market")
                $ LocEnter()

label qst_jackpot_black_diamond_vip_scene:
    $ QstTheJackpot().VulshanRouteSeenVIPScene = True
    scene black with dissolve
    "As I headed into one of the private rooms, a pleasant surprise was awaiting me..."
    $ LocFlush(dissolve)
    show fawha at center with dissolve

    BLACK_DIAMOND_SERVICE_GIRL "How do you want me, sir?"

    $ tmpvar = None
    menu:
        "Keep your clothes on.":
            BLACK_DIAMOND_SERVICE_GIRL "Mhmm, as you wish."
            $ tmpvar = "clothed"
        "Take your clothes off.":
            $ CharSetClothes("fawha", "naked")
            show fawha at nod
            BLACK_DIAMOND_SERVICE_GIRL "Whatever you desire."
            $ tmpvar = "nude"
    
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)

    if tmpvar == "clothed":
        scene bd_girls_jackpot_vip_bj_dress_slow with dissolve
    if tmpvar == "nude":
        scene bd_girls_jackpot_vip_bj_naked_slow with dissolve
    $ Pause()

    BLACK_DIAMOND_SERVICE_GIRL "{i}*Slurp!* *Slurp!*{/i}"
    BLACK_DIAMOND_SERVICE_GIRL "Mhmmmfghh! Shuchhaabhigg mhmmmff!"
    "I let out a sigh as the girl worked her {i}talents{/i} excellently on me."
    "Time seemed to drift by as the girls' tongue and wet mouth glided up and down my cock."
    "I sunk back into the soft furniture, a free bottle drunk between us as the time began to drift on by."
    MC "Mhhfhh..."

    if tmpvar == "clothed":
        scene bd_girls_jackpot_vip_bj_dress_fast with dissolve
    if tmpvar == "nude":
        scene bd_girls_jackpot_vip_bj_naked_fast with dissolve
    $ Pause()

    "I groaned in pleasure as the girl sunk my cock deeper down into her throat, wiggling her round ass enticingly as she did so."
    "The girls' tongue flickered and and beat around my cock occasionally as she let out hot whimpers and muffled words of appreciation."
    BLACK_DIAMOND_SERVICE_GIRL "{i}Mhhfh! *Shlick!*{/i} Shuchahhh - Mhhfhh! Ghooodhh chockhh! {i}*Slurp!*{/i}"
    "Eventually, our brief time of play was at an end."
    "As I felt my balls tighten and rise from her expert teasing, I grunted through gritted teeth to warn her of my impending finish."
    MC "Ahhh...! I'm gonna-"
    BLACK_DIAMOND_SERVICE_GIRL "{i}*Slurp!*{/i} Mhmmfhh! Jhusthh fhinishhh whennhh rheadhyy! {i}*Slurp!*{/i} Mhmmff!"
    "Soon, as her tongue flickered over the head of my cock before gliding down to deep throat my member, she held it there and waited expectently."
    "After her long, continuous teasing, I finally felt overwhelmed with her mouth, and grabbing the back of her head, held at her soft hair as I poured my thick load down her throat."
    MC "H-HRGHHHHH!!"

    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    $ ReduceInfectionFromSex()
    
    if tmpvar == "clothed":
        $ UnlockGalFlag("bd_girls", "jackpot_vip", "var_dress")
    if tmpvar == "nude":
        $ UnlockGalFlag("bd_girls", "jackpot_vip", "var_naked")
    $ UnlockGalSceneAndGrantXp("bd_girls", "jackpot_vip")

    if tmpvar == "clothed":
        scene bd_girls_jackpot_vip_bj_dress_finish with flash
    if tmpvar == "nude":
        scene bd_girls_jackpot_vip_bj_naked_finish with flash
    $ Pause()

    BLACK_DIAMOND_SERVICE_GIRL "{i}*Gulp!*{/i} Mhmmff! {i}*Slurp!*{/i}"
    "As the rush of seed flooded down her throat, I noticed her legs trembling slightly as some sweet, glistening juices dripped down between her legs onto the floor."
    "{i}Had she just finished from sucking my cock alone?{/i}"
    "The girl eagerly swallowed and licked up every last hint of my seed, making sure not to waste a drop."
    "Satisfied my member had been cleaned, she pulled back, wipping her mouth clean with a cloth delicately."
    BLACK_DIAMOND_SERVICE_GIRL "Thank you for zer meal, sir, fufu {image=[ICON.HEART]}"
    scene black with dissolve
    $ AutoMus(True)
    $ CharSetClothes("fawha", "normal")
    "Without another word, the girl rose to her feet, gently bowed and left the room."
    "After allowing myself a few moments to collect myself, I headed outside..."
    MC "(Well, that DEFINITELY killed some time at least, now what?)"
    $ tmpvar = {}
    $ LocEnter()
