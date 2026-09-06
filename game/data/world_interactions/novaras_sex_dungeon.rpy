init python:
    # enabled by DoorNovarasSexDungeon
    @AppendToAllQuests
    class NovarasSexDungeon(LogicModule):
        def __init__(self):
            super().__init__()

            self.CanSummon = True

        def onNoon(self):
            self.CanSummon = True
            return

        def onStart(self):
            QstStart(DoorNovarasSexDungeon)
            return

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_bordello_sex_dungeon":
                if self.CanSummon:
                    btnMods["btn_novaras_bordello_dungeon_summon"] = BtnJumpLabel(_("Summon"), "novaras_sex_dungeon_summon")
                else:
                    btnMods["btn_novaras_bordello_dungeon_summon"] = BtnJumpLabel(_("Summon"), "novaras_sex_dungeon_summon_cannot")
            return LocButtonMod(directMods = btnMods)

label novaras_sex_dungeon_summon_cannot:
    MC "(I have already done that tonight.)"
    $ LocEnter()

label novaras_sex_dungeon_summon:
    $ tmpvar = []
    if QstGetProgress(RomanceMika) >= 1:
        $ tmpvar.append("mika")
    if len(tmpvar) > 0:
        menu:
            "Summon Mika.":
                jump novaras_sex_dungeon_mika
            "Not now.":
                $ LocEnter()
    else:
        MC "(I can't think of anyone to summon.)"
        call screen ok_popup(label = _("Developers note"), text = _("As of now you can only summon Mika, provided you have romanced her enough."))
        $ LocEnter()

label novaras_sex_dungeon_mika:
    $ NovarasSexDungeon().CanSummon = False
    $ TimeAdvBy(TIME_1H * 3)
    scene black with dissolve
    $ Pause(1.0)
    $ LocFlush()
    show mc at cleft
    show mika at cright_f
    with dissolve
    MIKA @blush "U-Umm... You wanted to meet me here?"
    MIKA @blush "A really nicely dressed lady said she was to bring me to you here..."
    "Mika's eyes darted around the various sex contraptions littered around the place."
    MIKA @lewd "... You didn't invite me here to just talk, did you?"
    "I smirked towards Mika."
    MC @lewd "I had other things on my mind..."
    "Mika bit down on her lower lip, breathing heavily."
    MIKA @lewd "S-So... Which one do you want to try with me?"
    menu:
        "Stocks":
            jump novaras_sex_dungeon_mika_stocks

label novaras_sex_dungeon_mika_stocks:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Stripped of her clothes, Mika nervously placed herself into the hole, locking herself in for me."
    ### show idle front
    scene mika_sex_dungeon_wall_idle_front
    with dissolve
    $ Pause()
    MIKA "T-This is weird!"
    MIKA "I can't s-see you!"
    ### show idle split
    scene mika_sex_dungeon_wall_idle_split
    with dissolve
    $ Pause()
    "Staring at her bubbly, naked blue ass in front of me, my cock throbbed with excitement as Mika wiggled slightly in her restraints."
    "Above her head, somehow, there was an image of her likeness that only made the whole thing more arousing for me."
    "Upon a brief closer inspection, it seemed the image of her had indeed been drawn and colored in such a remarkably short time."
    "Tonight... Mika was just my willing sex toy, my bitch, and nothing more."
    "Gently, I aligned myself behind Mika's rump, giving her ass a light slap as the fat jiggled and her toes curled in response."
    MIKA "Ahh!"
    MIKA "{i}*Giggles*{/i} D-Daddy... What are you doing to me back there?"
    "Stepping behind her wiggling, cute ass, I placed down my cock against the crack of her butt and began to move back and forth."
    MIKA "A-Ahhh... I never n-noticed how heavy your thing actually felt."
    MIKA "G-Gods, it f-feels nice..."
    ### show idle side
    scene mika_sex_dungeon_wall_idle_side
    with dissolve
    $ Pause()
    "Mika's hands twitched and struggled slightly as I stared down at her tight asshole and pussy."
    MIKA "{i}*Huff*{/i} T-This is... Mhmm..."
    MIKA "{i}Kinda exciting.{/i}"
    MIKA "I feel so s-slutty knowing you're just staring at my butt back there!"
    "As I continued to gently rub and slap my cock against her soft butt, I knew I had to make a choice..."
    "How did I want her?"
    menu:
        "Put it in her pussy":
            jump novaras_sex_dungeon_mika_vag

        "Put it in her ass":
            jump novaras_sex_dungeon_mika_anal

########### vag
label novaras_sex_dungeon_mika_vag:
    #### side slow
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    scene mika_sex_dungeon_wall_vag_side_slow
    with dissolve
    $ Pause()
    "Gently, with both hands squeezing her ass, I pressed the head of my cock against Mika's wet womanhood."
    "She let out a little gasp as she felt the cock push against her lips, her butt slightly jerking in surprise before she felt the head slip in with ease."
    MIKA "A-Ahhh...!"
    "Mika let out a soft moan as I pushed my cock with ease deeper inside of her."
    MIKA "M-Mhhfhh!"
    MIKA "By Palam's - Mhhmm!"
    MIKA "I can f-feel you stretching me out so much!"
    MIKA "You feel so big like this!"
    #### side fast
    $ PlaySexFx("audio/sex_sounds/nijah_miss_2.ogg", 1)
    scene mika_sex_dungeon_wall_vag_side_fast
    with dissolve
    $ Pause()
    "Mika's still visible hands coiled and squeezed as her toes once again curled and flexed in response."
    "Her tight, wet pussy squeezed me excitedly as I slowly began to move in and out of her."
    "While I couldn't see her face, from the other side, her hot, heaving breathing and moans only became more and more frequent."
    MIKA "I - I never knew being - Mhmm!"
    MIKA "R-Restrained could make me f-feel so hot and..."
    MIKA "{i}Powerless.{/i}"
    "With every thrust into her tight hole, Mika let out another shuddering moan as the sound of flesh colliding loudly rang out through the room."
    MIKA "F-Faster... Mhmm... Go faster!"
    ## split fast
    scene mika_sex_dungeon_wall_split_fast
    with dissolve
    $ Pause()
    MIKA "Just use my pussy! That's why you b-brought me here!"
    "With my hands still squeezing at her tight ass, feeling the soft, fatness of her cheeks between my fingertips, I began to thrust faster into her."
    "Wet squelching sounds soon became louder as Mika grunted in approval."
    MIKA "Ah! Ah! Ahh!"
    MIKA "Y-Yes! I love you! I love you so much!"
    MIKA "I love you, I love you, I love you, I love you!!"
    "Bemused at her comment, I couldn't help but smirk at her loud declarations of love as she so keenly took my cock."
    "With one hand still on her ass, I grabbed hold of one of the handlebars, giving me a greater ease by which to push and pull myself into Mika's welcoming hole."
    MIKA "N-Nghhh!"
    MIKA "D-Daddy?"
    "She whimpered between hot, heavy breaths."
    MIKA "C-Call me your little slutty mage, please?"
    MC "Mika... Ahh...!"
    MIKA "Mmhhfh! Y-Yes sir?"
    MC "You're tight blue ass belongs to me, do you understand?"
    MIKA "A-Ahh! Yes! I understand!"
    MIKA "Mhhfh!"
    MC "You're not just my little slutty mage."
    MC "You're my whore, my bitch, my little Palam cock-sleeve for draining my balls!"
    ## front fast
    scene mika_sex_dungeon_wall_vag_front_fast
    with dissolve
    $ Pause()
    MIKA "Y-YES! That's what I - Ahh! Wanna be for you!"
    "Mika's cock twitched in excitement as I slapped her ass once again."
    MIKA "F-Fuck me! FUCK ME HARDER NOW!"
    MIKA "P-Please! I w-wanna feel you fill me up so much!"
    MIKA "Breed your little s-slutty mage!"
    "Now, drenched in sweat and abandoning all reason, I grabbed hold of both of the handles as I slammed myself into Mika."
    "Her wails and howls of pleasure filled the room as I slammed and bottomed out my cock as deeply as I could into her."
    "The soft fatness of her butt acting as a cushion as the lewd, wet sounds of our flesh slapping together became louder and more frequent."
    "{i}*Phap!* *Phap!* *Phap!*{/i}"
    MIKA "H-Hrghhh! Yessss!"
    MIKA "T-That's right! Fuck me, my love!"
    MIKA "Your cock feels so amazing!"
    MIKA "Fill me up! Don't stop until you f-fill me up!"
    "By now, the intensity and passion of our fucking had finally caught up with me."
    "Drenched in sweat, my own cock had become achingly sensitive as my balls, full and heavy, felt ready to unload my seed into her welcoming womb."
    MC "M-Mika, I'm gonna-"
    MIKA "D-Do it! Just let it out!"
    MIKA "I wanna cum with you!! Ahh!"
    ### finish (front art)
    $ PregRoll("mika")
    $ UnlockGalFlag("mika", "sex_dungeon_wall", "var_vag")
    $ UnlockGalSceneAndGrantXp("mika", "sex_dungeon_wall")
    $ ReduceInfectionFromSex("mika")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    scene mika_sex_dungeon_wall_vag_front_finish
    with dissolve
    $ Pause()
    "Unable to hold back any longer, I slammed and bottomed out as deeply as I could into Mika, grunting loudly as I pumped her welcoming hole full of my seed."
    MC "H-HRGHHHH...!"
    "As she felt the rush of hot, thick seed pouring into her womb, Mika gasped, her whole body shaking as her pussy gripped my cock and refused to let go."
    MIKA "M-MMMFGHHHHHH!!"
    ### show finish split
    scene mika_sex_dungeon_wall_split_finish
    with dissolve
    $ Pause()
    "Eventually, after pouring every last drop into her, I slowly began to unsheathe my cock, inch by inch, out of her now well-fucked pussy."
    "With a light *PLOP* sound, my deflating cock fully slipped out of her hole as Mika shuddered in pleasure, my seed dripping down freely out of her hole onto the floor."
    MIKA "{i}S-So good...{/i}"
    ## flush show them both
    $ LocFlush()
    $ CharSetClothes("mc", "pants")
    $ CharSetClothes("mika", "naked")
    show mc at cleft
    show mika at cright_f
    with dissolve
    "Unlocking and releasing Mika from the contraption, with shaky legs, she rose back to her feet to face me, flushed red."
    MIKA @lewd "{i}*Huff*{/i} That was incredible! {i}*Huff*{/i}"
    MIKA @lewd "I f-feel so sore now! Mmm..."
    jump novaras_sex_dungeon_mika_conclusion

############# anal
label novaras_sex_dungeon_mika_anal:
    #### side slow
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    scene mika_sex_dungeon_wall_anal_side_slow
    with dissolve
    $ Pause()
    "With both hands squeezing her ass, a mischievous smirk appears on my lips as I gently prod my cock against Mika's tight-looking rosebud after spitting on it."
    MIKA "W-Wait! That's my-"
    "She let out a little gasp as she felt the cock push against her backdoor, her butt slightly jerking in surprise before she felt the head stretch and force its way into her tight ass."
    MIKA "A-ASSSSS...!"
    "Mika let out a sharp grunt of pain, followed quickly by a soft moan as I pushed my cock an inch or two deeper into her bowels."
    MIKA "Ahhh! F-FUCK!"
    MIKA "By P-Palam... Mmmm!" 
    MIKA "I should have g-guessed you would have picked {i}that{/i} hole, but-"
    #### side fast
    $ PlaySexFx("audio/sex_sounds/nijah_miss_2.ogg", 1)
    scene mika_sex_dungeon_wall_anal_side_fast
    with dissolve
    $ Pause()
    MIKA "Oooh! S-Some warning next time would be nice!"
    MC "Ha, sorry, Mika!"
    MC "Your ass looked too - Ahh! Irresistible!"
    MIKA "O-Oooh! I c-can R-REALLY feel you s-stretching out my butt back there!"
    "Surprisingly, Mika's ass was already smooth and well-lubed. Had she already anticipated I might have tried to fuck her ass tonight?"
    MIKA "O-Oooh! You feel so big like this!"
    "Mika's still visible hands coiled and squeezed as her toes once again curled and flexed in response."
    "Her tight ass squeezed me excitedly as I slowly began to move in and out of her."
    "While I couldn't see her face, from the other side, her hot, heaving breathing and moans only became more and more frequent."
    MIKA "I - I never knew being - Mhmm!"
    MIKA "R-Restrained could make me f-feel so hot and..."
    MIKA "{i}Powerless.{/i}"
    "With every thrust into her tight sphincter, Mika let out another shuddering moan as the sound of flesh colliding loudly rang out through the room."
    MIKA "M-My ashhhh! Mmm! F-FUCK!"
    MIKA "{i}*Huff*{/i} G-Go a little f-faster... Mhmm..."
    MIKA "I-It's okay! Ahh!"
    MIKA "{i}My ass can take it!{/i}"
    ## split fast
    scene mika_sex_dungeon_wall_split_fast
    with dissolve
    $ Pause()
    "With my hands still squeezing at her tight ass, feeling the soft, fatness of her cheeks between my fingertips, I began to thrust faster into her."
    "Wet squelching sounds soon became louder as Mika grunted in approval."
    MIKA "Ah! Ah! Ahh!"
    MIKA "Y-Yes! I love you! I love you so much!"
    MIKA "I love you, I love you, I love you, I love you!!"
    "Bemused at her comment, I couldn't help but smirk at her loud declarations of love as I watched her dark asshole swallow up my cock greedily."
    "With one hand still on her ass, I grabbed hold of one of the handlebars, giving me a greater ease by which to push and pull myself into Mika's back door."
    MIKA "N-Nghhh!"
    MIKA "D-Daddy?"
    "She whimpered between hot, heavy breaths."
    MIKA "C-Call me your little slutty mage, please?"
    MC "Mika... Ahh...!"
    MIKA "Mmhhfh! Y-Yes sir?"
    MC "You're tight blue ass belongs to me, do you understand?"
    MIKA "A-Ahh! Yes! I understand!"
    MIKA "Mhhfh!"
    MC "You're not just my little slutty mage."
    MC "You're my whore, my bitch, my little Palam cock-sleeve for draining my balls!"
    ## front fast
    scene mika_sex_dungeon_wall_anal_front_fast
    with dissolve
    $ Pause()
    MIKA "Y-YES! That's what I - Ahh! Wanna be for you!"
    "Mika's cock twitched in excitement as I slapped her ass once again."
    MIKA "F-Fuck me! FUCK ME HARDER NOW!"
    MIKA "P-Please! I w-wanna feel you fill me up so much!"
    MIKA "F-Fill your s-slutty mage's tight ass!"
    "Now, drenched in sweat and abandoning all reason, I grabbed hold of both of the handles as I slammed myself into Mika."
    "Her wails and howls of pleasure filled the room as I slammed and bottomed out my cock as deeply as I could into her."
    "The soft fatness of her butt acting as a cushion as the lewd, wet sounds of our flesh slapping together became louder and more frequent."
    "{i}*Phap!* *Phap!* *Phap!*{/i}"
    MIKA "H-Hrghhh! Yessss!"
    MIKA "T-That's right! Fuck me, my love!"
    MIKA "Your cock feels so amazing!"
    MIKA "Fill me up! Don't stop until you f-fill me up!"
    "By now, the intensity and passion of our fucking had finally caught up with me."
    "Drenched in sweat, my own cock had become achingly sensitive as my balls, full and heavy, felt ready to unload my seed into her bowels."
    MC "M-Mika, I'm gonna-"
    MIKA "D-Do it! Just let it out!"
    MIKA "I wanna cum with you!! Ahh!"
    ### finish (front art)
    $ UnlockGalFlag("mika", "sex_dungeon_wall", "var_anal")
    $ UnlockGalSceneAndGrantXp("mika", "sex_dungeon_wall")
    $ ReduceInfectionFromSex("mika")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    scene mika_sex_dungeon_wall_anal_front_finish
    with dissolve
    $ Pause()
    "Unable to hold back any longer, I slammed and bottomed out as deeply as I could into Mika, grunting loudly as I pumped her asshole full of my seed."
    MC "H-HRGHHHH...!"
    "As she felt the rush of hot, thick seed pouring into her ass, Mika gasped, her whole body shaking as her ass gripped my cock and refused to let go."
    MIKA "M-MMMFGHHHHHH!!"
    ### show finish split
    scene mika_sex_dungeon_wall_split_finish
    with dissolve
    $ Pause()
    "Eventually, after pouring every last drop into her, I slowly began to unsheathe my cock, inch by inch, out of her now well-fucked ass."
    "With a light *PLOP* sound, my deflating cock fully slipped out of her hole as Mika shuddered in pleasure, my seed dripping down freely out of her hole onto the floor."
    MIKA "{i}S-So good...{/i}"
    ## flush show both
    $ LocFlush()
    
    $ CharSetClothes("mc", "pants")
    $ CharSetClothes("mika", "naked")
    show mc at cleft
    show mika at cright_f
    with dissolve
    "Unlocking and releasing Mika from the contraption, with shaky legs, she rose back to her feet to face me, flushed red."
    MIKA @lewd "{i}*Huff*{/i} That was incredible! {i}*Huff*{/i}"
    MIKA @lewd "My ... My poor ass! Mmm..."
    MIKA @lewd "I'm not going to be able to sit down properly for days, you know!"
    jump novaras_sex_dungeon_mika_conclusion

label novaras_sex_dungeon_mika_conclusion:
    $ AutoMus(True)
    MC @smile "I can call upon you to do this again then?"
    "With a wicked grin, Mika leapt into my arms to kiss my lips."
    MIKA @lewd "You can summon this slutty mage's ass whenever you want... {i}daddy.{/i}"
    scene black with dissolve

    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("mika", "dress")

    "With that, Mika got dressed, and with a quick slap of her butt, she giggled and left me to return to my own devices once again."
    if IsDaytime():
        "The brothel was closing down for the day, so I have slipped outside to the streets."
        $ LocSet("novaras_dist_pleasure")
    $ LocEnter()