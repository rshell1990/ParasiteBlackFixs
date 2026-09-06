init python:
    @AppendToAllQuests
    @RegisterPregModuleFor("marbella")
    class PregMarbella(BasePregModule):  
        def __init__(self):
            super().__init__()

            self.CharID = "marbella"
            self.GaveBirthNotifText = _("Marbella has given birth.")
############## custom vars
            self.ShareFirstImpregNews    = False
            self.ShareSecondImpregNews   = False
            self.DoPostBirthScene = False

            # cycles
            self.TodayPregFeelingLines = 0 
            self.TodayHowIsChildLines = 0 
            return

        def PostImpreg(self):
            # 1st time
            if self.NumImpregs == 1:
                self.ShareFirstImpregNews = True
            elif self.NumImpregs > 1:
                self.ShareSecondImpregNews = True
            return

        def PostBirth(self):
            self.DoPostBirthScene = True
            return

        def extraDialogue(self):
            if CharGetPreg("marbella") == 4:
                yield ("marbella_root", DNode(_("How is the little one?"), "rom_marbella_shared_preg_howischild", order = 99))
            if CharIsVisiblyPreg("marbella"):
                yield ("marbella_root", DNode(_("How are you feeling?"), "rom_marbella_shared_preg_howfeeling", order = 99))

        def onEnter(self):
            if GetLocID() == "hamun_miningco":
                if IsDaytime():
                    EventLabel = None
                    if CharIsVisiblyPreg("marbella"):
                        if self.ShareFirstImpregNews:
                            if RomanceMarbella().Kind == "dom":
                                EventLabel = "rom_marbella_dom_preg_share_first_impreg_news"
                            elif RomanceMarbella().Kind == "gang":
                                EventLabel = "rom_marbella_gang_preg_share_first_impreg_news"
                            elif RomanceMarbella().Kind == "love":
                                EventLabel = "rom_marbella_love_preg_share_first_impreg_news"                            

                        elif self.ShareSecondImpregNews:
                            self.ShareSecondImpregNews = False
                            if RomanceMarbella().Kind in ["dom", "love"]:
                                EventLabel = "rom_marbella_domlove_preg_share_further_impreg_news"
                            elif RomanceMarbella().Kind == "gang":
                                EventLabel = "rom_marbella_gang_preg_share_further_impreg_news"

                    elif self.DoPostBirthScene:
                        self.DoPostBirthScene = False
                        EventLabel = "rom_marbella_shared_preg_postbirth"

                    if EventLabel is not None:
                        return TriggeredEvent(EventLabel)


##############
#Marbella pregnancy content (Dom) - Scene begins after entering the crooked shaft"
label rom_marbella_dom_preg_share_first_impreg_news:
    $ PregMarbella().ShareFirstImpregNews = False
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    show marbella at cleft 
    with dissolve
    show mc at cright_f with easeinright
    MARBELLA @sad "Ummm... Love."
    MARBELLA @sad "We really need to talk."
    MC @think "What is it?"
    show marbella at shake
    MARBELLA @angry "You knocked me is what!"
    MC @surprised "What?"
    MARBELLA @emb "You heard me, you and that fat prick of yours did the job."
    MARBELLA @emb "Now I've got a bun in the oven."
    "Pride swells within me, and a strange warm feeling."
    MC @smile "That's wonderful news."
    MARBELLA @shock "I... You're not worried?"
    MC @smile "No, I'm happy."
    MARBELLA @shock "... Oh!"
    MARBELLA @emb "Umm, I wasn't expecting that."
    MARBELLA @think "But, I take it you ain't givin' up... Whatever the hells is it you are exactly?"
    MC @serious "No, I'm afraid I can't."
    MC @smile "but I'll do my best to stay within you and the child's life."
    "Marbella sighed, her hands nervously running over her belly."
    MARBELLA @talk "Didn't exactly imagine me-self as a mother right now..."
    MARBELLA @talk "But, if you're serious about doing your best to stay in our lives."
    MARBELLA @emb "I guess... We could try make this work?"
    MARBELLA @smile "Alright, I love-"
    "marbella stopped herself, her cheeks bright red."
    MARBELLA @emb "I mean, yer ass better check in from time to time."
    MC @smile "I will."
    hide marbella with dissolve
    "With a slightly nervous smile, Marbella turned to head back to work."
    show mc at center_f with ease
    SHYAHTAN "(How pleasing...)"
    $ LocEnter()

##############
#Marbella pregnancy content (gang) - Scene begins after entering the crooked Shaft
label rom_marbella_gang_preg_share_first_impreg_news:
    $ PregMarbella().ShareFirstImpregNews = False
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    show marbella at cleft
    with dissolve
    show mc at cright_f with easeinright
    MARBELLA @concern_lookaway "We... We need to talk."
    MARBELLA @concern "{i}... I'm pregnant.{/i}"
    MC @surprised "Your pregnant?"
    MC @serious "is it... Mine?"
    show marbella at shake
    MARBELLA @angry "Yes! It's bloody yours!"
    "Marbella's cheeks burned red."
    MARBELLA @think "At least I'm pretty sure it is..."
    MC @think "How do you know?"
    MARBELLA @angry "You ever seen a baby growing THIS fast before?"
    MARBELLA @concern "Dunno what you and your spunk are exactly... But, after your little performance at the arena, I KNOW you ain't exactly a normal human."
    MARBELLA @sad "So, uh... Yes."
    MARBELLA @sad "Congrats?"
    MC @talk "I see..."
    MARBELLA @sad "Look, you don't need to feel obliged to stick around or whatever."
    MARBELLA @talk "Gavkat and the other guys are basically already planning on helping raise the littlun anyway."
    MARBELLA @think "Andddd the Khazah are surprisingly supportive."
    MARBELLA @think "I guess because they probably think it could be any of them knocking me up next anyway..."
    MC @smile "If it's our child, I'll still do what I can to help."
    "Marbella blinked, slightly taken aback at the answer."
    MARBELLA @shock "... Oh!"
    MARBELLA @shock "Uhh, didn't really expect that from you."
    MARBELLA @smile "Well, alright... if you're sure."
    MARBELLA @talk "... A-Anyway, I better get back to work."
    MARBELLA @talk "Don't be a stranger, alright?"
    hide marbella with dissolve
    "Marbella turned to leave and tend to her work."
    $ LocEnter()

###############
# Marbella pregnancy content (Romance) - Scene begins after entering the crooked Shaft
label rom_marbella_love_preg_share_first_impreg_news:
    $ PregMarbella().ShareFirstImpregNews = False
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    show marbella at cleft
    with dissolve
    show mc at cright_f with easeinright
    MARBELLA @smile "I'm pregnant! I'M PREGNANT!"
    show marbella at center with ease
    "Marbella excitedly rushed towards me, grabbing my hands and placing them onto her belly."
    MC @surprised "Wait, what?"
    MARBELLA @smile "Well you see, when a man loves a horny dwarf and keeps cumming inside of her, they make a-"
    MC @talk "Very funny."
    MARBELLA @concern "... You are happy, right?"
    MARBELLA @concern_lookaway "I know you probably won't be able to stay by my side with all your galavanting around saving people and stuff..."
    MARBELLA @shock "B-But don't worry!"
    MARBELLA @smile "Gavkat and the others have got my back, I'll be alright, y'know?"
    MARBELLA @sad "... It would just mean a lot if you were still in my life."
    MC @smile "I will do what I can."
    "Marbella's cheeks turned a rosy pink as her eyes seemed to wide, looking up to me with deep admiration."
    MARBELLA @blush "... I fucking love you, big boy."
    "I smiled at her confession, my hand tenderly rubbing at her belly once more."
    MC @smile "I love you too... even if you're a pain in the ass."
    MARBELLA @shock "Oi!"
    MARBELLA @smile "Cheeky..."
    MARBELLA @smile "Anyway, that's the big news."
    MARBELLA @smile "I best be getting back to work but..."
    MARBELLA @blush "Thank you... for everything."
    hide marbella with dissolve
    "With that, and a giddy lightness to her step, Marbella resumed her work."
    show mc at center_f with ease
    MC "(A child with Marbella...)"
    SHYAHTAN "(The correct analysis was 'first' child with Marbella... I sense she is prepared to sire us much more offspring.)"
    MC @think "(Let's just see how things go with this one, alright?)"
    $ LocEnter()

###########
#If player knocks up Marbella again (Romance and Dom)
label rom_marbella_domlove_preg_share_further_impreg_news:
    show marbella at cleft
    with dissolve
    show mc at cright_f with easeinright
    MARBELLA @angry "You bloody did it again!"
    MC @surprised "What?"
    show marbella at shake
    MARBELLA @angry "HOW MANY BLOODY BABIES YOU GONNA PUT IN ME?"
    MC @surprised "You're pregnant again?"
    MARBELLA @emb "Yes..."
    MC @smile "Well, that's great news!"
    MARBELLA @angry "I-"
    MARBELLA @emb "{i}*Sigh*{/i} Stop being so fuckin' adorable about this."
    MARBELLA @angry "It's really hard to be mad at you when you're like this!"
    "Marbella's cheeks continued to burn red."
    MARBELLA @emb ".. You better fuckin' stick around for this one too."
    MC @smile "If I didn't stick around, how would I be able to knock you up again?"
    "Marbella huffed."
    MARBELLA @talk "Cocky bastard..."
    $ LocEnter()

#If Marbella is knocked up again (gang)
label rom_marbella_gang_preg_share_further_impreg_news:
    show marbella at cleft
    with dissolve
    show mc at cright_f with easeinright
    MARBELLA @concern "A-Ahh...!"
    MARBELLA @think "G-Guess whose pregnant again? Haha...!"
    MC @think "Is it mine?"
    show marbella at shake
    MARBELLA @angry "Yes! Of course it's bloody yours!"
    MARBELLA @concern_lookaway "{i}Umm... At least I think it is...{/i}"
    MARBELLA @emb "A-Anyway, uhh, just letting you know!"
    hide marbella with dissolve
    "Marbella scarpered off back to work, and I was left wondering if this new child really {i}was{/i} mine..."
    show mc at center_f with ease
    "Regardless, the child would be raised like the others, and I would carry on with my travels."
    "Still though, it did make me uneasy... Had I made the right choice letting her become the Khazah's whore?"
    $ LocEnter()

#Upon re-speaking to Marbella while she's pregnant - new dialogue option "How are you feeling?" - These variants are shared between ALL routes
label rom_marbella_shared_preg_howfeeling:
    # cycle
    $ PregMarbella().TodayPregFeelingLines += 1
    if PregMarbella().TodayPregFeelingLines == 6:
        $ PregMarbella().TodayPregFeelingLines = 0
    # pick
    if PregMarbella().TodayPregFeelingLines == 0:
        MARBELLA @shock "Our littlun's bloody strong!"
        MARBELLA @shock "Restless too, can feel him moving around a lot."
    elif PregMarbella().TodayPregFeelingLines == 1:
        MARBELLA @think "Why do I have a sudden craving all the time for beef?"
    elif PregMarbella().TodayPregFeelingLines == 2:
        MARBELLA @sad "My back hurts, my tits are huge, and I can't sleep... Any other questions?"
    elif PregMarbella().TodayPregFeelingLines == 3:
        MARBELLA @emb "I'm horny is fuck is what I am. When are you going to stick your cock in me?"
    elif PregMarbella().TodayPregFeelingLines == 4:
        MARBELLA @smile "hehe... Find myself lookin' at me bump in the mirror all the time wondering when they're gonna come out."
    elif PregMarbella().TodayPregFeelingLines == 5:
        MARBELLA @think "Gavkat and the others keep insisting on buying em' a pickaxe for when they're born... Little early for that though, don't you think?"
    return

label rom_marbella_shared_preg_postbirth:
    show marbella at cleft with dissolve
    show mc at cright_f with easeinright
    "Marbella smiled, holding the small, crying, wrapped baby in some cloth as she rocked it back and forth soothingly."
    MARBELLA @smile "Come meet yer son handsome."
    MC @surprised "My son?"
    MARBELLA @smile "Aye."
    show mc at center_f with ease
    "I moved closer, gently reaching out as he grabbed a hold of my finger with his small, tiny hands."
    MARBELLA @smile "He's got yer eyes..."
    $ PregMarbella().LastBornBabyName = renpy.input(_("What should we call him?"), default = _("Dukant"))
    MARBELLA @smile "Aye, I like it..."
    MARBELLA @smile "I'm gonna lay him down for some sleep."
    MARBELLA @talk "We'll talk more later, alright?"
    MC @smile "Alright..."
    $ LocEnter()

label rom_marbella_shared_preg_howischild:
    # cycle
    $ PregMarbella().TodayHowIsChildLines += 1
    if PregMarbella().TodayHowIsChildLines == 3:
        $ PregMarbella().TodayHowIsChildLines = 0
    # pick
    if PregMarbella().TodayHowIsChildLines == 0:
        MARBELLA @smile "Sleeping, eatin' and pooping."
        MARBELLA @smile "Like any other happy baby I suppose."
    elif PregMarbella().TodayHowIsChildLines == 1:
        MARBELLA @think "Are babies supposed to be crawling around this early?"
        MARBELLA @shock "I swear he's developin' real fast!"
    elif PregMarbella().TodayHowIsChildLines == 2:
        MARBELLA @smile "He's cute and adorable."
        MARBELLA @smile "Gavkat and the others already adore him."  
    return
