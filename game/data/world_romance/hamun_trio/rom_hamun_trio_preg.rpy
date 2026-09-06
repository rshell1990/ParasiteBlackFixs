init python:
# its actually gonna track preg for the other two chicks too
    @AppendToAllQuests
    @RegisterPregModuleFor("lady_belamore")
    class PregHamunTrio(BasePregModule):
        def __init__(self):
            super().__init__()

            self.CharID = "lady_belamore"
            self.GaveBirthNotifText = _("Lady Belamore and her friends have given birth!")

            self.Name1 = _("Kristal")
            self.Name2 = _("Tifania")
            self.Name3 = _("Herculus")

            self.ShowPostImpreg_First = False
            self.ShowPostImpreg_Rep  = False
            self.ShowPostBirth_First = False
            self.ShowPostBirth_Rep   = False

#############################################################
        def PostImpreg(self):
            if self.NumImpregs == 1:
                self.ShowPostImpreg_First = True
            elif self.NumImpregs >= 2:
                self.ShowPostImpreg_Rep = True
            return

        def PostBirth(self):
            if self.NumBirths == 1:
                self.ShowPostBirth_First = True
            elif self.NumBirths >= 2:
                self.ShowPostBirth_Rep = True
            return

        def onEnter(self):
            if GetLocID() == "hamun_tarbeck_mainhall":
                if IsDaytime():
                    Label = None
                    if self.ShowPostBirth_First:
                        Label = "rom_hamun_trio_birth_first"
                    elif self.ShowPostBirth_Rep:
                        Label = "rom_hamun_trio_birth_rep"
                    elif self.ShowPostImpreg_First:
                        Label = "rom_hamun_trio_impreg_first"
                    elif self.ShowPostImpreg_Rep:
                        Label = "rom_hamun_trio_impreg_rep"
                    if Label is not None:
                        return TriggeredEvent(Label, priority = 3)
            return

label rom_hamun_trio_impreg_first:
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    show mc at cleft with easeinleft
    $ PregHamunTrio().ShowPostImpreg_First = False
    LADY_BELAMORE @angry "Where is he?!"
    show lady_narisha at cright
    show lady_belamore at right
    show lady_bargore at center
    with dissolve
    LADY_NARISHA @smile "MY KNIGHT! I'm having your baby! Hehe!"
    MC @surprised "What?"
    LADY_BARGORE @talk "Correction... {i}We{/i} are having your babies."
    MC @think "You're all... pregnant?"
    LADY_BELAMORE @angry "Yes, you fucking-!"
    show lady_belamore at shake
    LADY_BELAMORE @angry "Grghh! I knew we should have never agreed to... FUCK!"
    LADY_NARISHA @smile "It's gonna be soooo cute.... A boy, I think?"
    LADY_BARGORE @talk "Narisha... You're already married, you moron."
    "Lady Narisha pouted."
    LADY_NARISHA @angry "True love won't be stopped!"
    LADY_BARGORE @talk "Urghhh..."
    LADY_BELAMORE @sad "I think my husband might buy it, or at least pretend to ignore his suspicions to avoid a scandal, but..."
    LADY_BELAMORE @sad "Damn you, man."
    MC @sad "... Lady Belamore."
    MC @sad "Narisha... Bargore."
    MC @talk "I will be there for the three of you whenever I can."
    "For the first time, Lady Belamore's face flushed pink with embarrassment as she heard an answer she wasn't expecting."
    LADY_BELAMORE @emb "You-"
    LADY_BELAMORE @emb "... W-Well, that's..."
    LADY_BELAMORE @emb "GOOD!"
    hide lady_belamore with easeoutleft
    "She hurried out of the hall, completely flustered, as the two women chased after her."
    LADY_NARISHA "Lady Belamore! Wait! We need to discuss matching names!"
    hide lady_narisha with easeoutleft
    LADY_BARGORE "Oh gods, next time I'll just make sure I swallow instead."
    hide lady_bargore with easeoutleft
    show mc at center with ease
    $ Pause(0.5)
    $ LocEnter()

# Trio pregnancy announcement - later pregnancies
# Auto-trigger once per later trio pregnancy during DAY entry to the Tarbeck estate.
# This event overrides standard manor interactions and lower-priority scheduled events.
label rom_hamun_trio_impreg_rep:
    $ PregHamunTrio().ShowPostImpreg_Rep = False
    show mc at cleft with easeinleft
    show lady_narisha at cright
    show lady_belamore at right
    show lady_bargore at center
    with dissolve
    LADY_BELAMORE @smile "Hello... How's your day going?"
    LADY_BELAMORE @smile "Fantasticccc..."
    LADY_BELAMORE @smile "If you could be so kind as to-"
    LADY_BELAMORE @angry "STOP KNOCKING US ALL UP AT ONCE."
    LADY_BELAMORE @angry "Do you know how ridiculous this is getting?!"
    LADY_NARISHA @smile "Hehe... Two babies... Three babies... Four babies!"
    LADY_BARGORE @think "I just get my husband blind drunk and convince him we did it... Seems to work so far."
    MC @surprised "All of you... Again?"
    LADY_BELAMORE @talk "Yes, you and that silly prick of yours seem determined to punish our wombs for eternity!"
    MC @think "Do you need help, or anything?"
    LADY_BELAMORE @emb "I-"
    LADY_BELAMORE @angry "Stop being so nice, damn it!"
    hide lady_belamore with easeoutleft
    "Lady Belamore scurried away, muttering that I was a bastard as the two women chased after her once more."
    hide lady_narisha with easeoutleft
    LADY_NARISHA "Hehe! We could start a club for all the little ones to play together!"
    hide lady_bargore with easeoutleft
    LADY_BARGORE "Terrible idea..."
    $ LocEnter()

# Trio birth scene - first completed pregnancy.
# Auto-trigger once when the synchronized trio pregnancy timer completes.
# This event takes priority over all appointments and standard manor interactions.
label rom_hamun_trio_birth_first:
    $ PregHamunTrio().ShowPostBirth_First = False
    $ PregHamunTrio().ShowPostImpreg_First = False
    show mc at left with easeinleft
    $ Pause(0.5)
    $ tmpvar = {}
    $ tmpvar["stored_preg"] = CharGetPreg("lady_belamore")
    $ CharSetPreg("lady_belamore", 4)
    show lord_tarbeck at cright_f
    show lady_narisha at right
    show lady_belamore at center
    show lady_bargore at cleft
    with dissolve
    "As the great doors to the Tarbeck estate opened, Lord Tarbeck stood watching Lady Belamore and her friends, amused as they cradled three crying babies wrapped in blankets."
    TARBECK @smile "Well... You've been prolific, haven't you?"
    "Lady Belamore snapped her head towards me as the three women came over."
    LADY_NARISHA @smile "AREN'T THEY JUST THE CUTEST?!"
    LADY_NARISHA @smile "He's going to be the manliest knight in the realm when he grows up! Just like his father!"
    LADY_BARGORE @talk "Not going to lie, I mostly leave it up to the maids to look after this one..."
    LADY_BELAMORE @talk "Well... I hope you're bloody happy!"
    MC @smile "Quite, actually."
    "Lady Belamore growled, but as she looked down at the tiny baby in her arms, and it reached out with its tiny fingers to touch her, her expression softened ever so slightly."
    LADY_BELAMORE @talk "{i}*Sigh*{/i}"
    LADY_BELAMORE @talk "What do you think of the name..."
    $ PregHamunTrio().Name1 = renpy.input(_("What do you think of the name..."), default = PregHamunTrio().Name1)
    LADY_BELAMORE @talk "It's... acceptable, I suppose."
    LADY_BARGORE @talk "I had something a little different in mind. I was thinking of..."
    $ PregHamunTrio().Name2 = renpy.input(_("I had something a little different in mind. I was thinking of..."), default = PregHamunTrio().Name2)
    LADY_BARGORE @talk "Glad we're in agreement."
    LADY_NARISHA @smile "This little prince I think we should call...!"
    $ PregHamunTrio().Name3 = renpy.input(_("This little prince I think we should call...!"), default = PregHamunTrio().Name3)
    LADY_NARISHA @smile "Teehee!"
    LADY_BELAMORE @talk "Well, you've seen them now..."
    "Lady Belamore turned her head towards Lord Tarbeck."
    LADY_BELAMORE @angry "You'd better keep to your word!"
    TARBECK @smile "My lips are sealed... Unlike your legs."
    hide lady_belamore with easeoutleft
    "In a huff, Lady Belamore stormed off as her friends chased after her."
    hide lady_bargore
    hide lady_narisha
    with easeoutleft
    show mc at cleft with ease
    MC @think "What was that about?"
    TARBECK @smile "Just some... assurances, in case their husbands discover their infidelities."
    TARBECK @smile "I will make sure the children are cared for. Not for their sake, {i}for yours.{/i}"
    MC @think "I... Thank you."
    $ CharSetPreg("lady_belamore", tmpvar["stored_preg"])
    $ tmpvar = {}
    "Lord Tarbeck said nothing else, tapping me on the shoulder as one does a friend before heading down a corridor, happily humming to himself."
    $ LocEnter()

# Trio birth scene - later pregnancies. (Repeat)
# Auto-trigger once when each later synchronized trio pregnancy timer completes.
# This event takes priority over all appointments and standard manor interactions.
label rom_hamun_trio_birth_rep:
    $ PregHamunTrio().ShowPostBirth_Rep = False
    $ PregHamunTrio().ShowPostImpreg_Rep = False
    show mc at left with easeinleft
    $ Pause(0.5)
    $ tmpvar = {}
    $ tmpvar["stored_preg"] = CharGetPreg("lady_belamore")
    $ CharSetPreg("lady_belamore", 4)
    show lord_tarbeck at cright_f
    show lady_narisha at right
    show lady_belamore at center
    show lady_bargore at cleft
    with dissolve
    "As the great doors to the Tarbeck estate opened, Lord Tarbeck stood watching Lady Belamore and her friends, amused as they cradled three crying babies wrapped in blankets."
    TARBECK @smile "Well... You've been prolific, haven't you?"
    "Lady Belamore snapped her head towards me as the three women came over."
    LADY_NARISHA @smile "AREN'T THEY JUST THE CUTEST?!"
    LADY_NARISHA @smile "He's going to be the manliest knight in the realm when he grows up! Just like his father!"
    LADY_BARGORE @talk "Not going to lie, I mostly leave it up to the maids to look after this one..."
    LADY_BELAMORE @talk "Well... I hope you're bloody happy!"
    MC @smile "Quite, actually."
    "Lady Belamore growled, but as she looked down at the tiny baby in her arms, and it reached out with its tiny fingers to touch her, her expression softened ever so slightly."
    LADY_BELAMORE @talk "{i}*Sigh*{/i}"
    LADY_BELAMORE @talk "What do you think of the name..."
    $ PregHamunTrio().Name1 = renpy.input(_("What do you think of the name..."), default = PregHamunTrio().Name1)
    LADY_BELAMORE @talk "It's... acceptable, I suppose."
    LADY_BARGORE @talk "I had something a little different in mind. I was thinking of..."
    $ PregHamunTrio().Name2 = renpy.input(_("I had something a little different in mind. I was thinking of..."), default = PregHamunTrio().Name2)
    LADY_BARGORE @talk "Glad we're in agreement."
    LADY_NARISHA @smile "This little prince I think we should call...!"
    $ PregHamunTrio().Name3 = renpy.input(_("This little prince I think we should call...!"), default = PregHamunTrio().Name3)
    LADY_NARISHA @smile "Teehee!"
    LADY_BELAMORE @talk "Well, you've seen them now..."
    "Lady Belamore turned her head towards Lord Tarbeck."
    LADY_BELAMORE @angry "You'd better keep to your word!"
    TARBECK @smile "My lips are sealed... Unlike your legs."
    hide lady_belamore with easeoutleft
    "In a huff, Lady Belamore stormed off as her friends chased after her."
    hide lady_bargore
    hide lady_narisha
    with easeoutleft
    show mc at cleft with ease
    MC @think "What was that about?"
    TARBECK @smile "Just some... assurances, in case their husbands discover their infidelities."
    TARBECK @smile "I will make sure the children are cared for. Not for their sake, {i}for yours.{/i}"
    MC @think "I... Thank you."
    $ CharSetPreg("lady_belamore", tmpvar["stored_preg"])
    $ tmpvar = {}
    "Lord Tarbeck said nothing else, tapping me on the shoulder as one does a friend before heading down a corridor, happily humming to himself."
    $ LocEnter()
