init python:
# its actually chanyi but for anya, just track her preg state as chanyi's
    @AppendToAllQuests
    @RegisterPregModuleFor("chanyi")
    class PregFaymoreGirls(BasePregModule):
        def __init__(self):
            super().__init__()

            self.BabyName1 = _("Avalon")
            self.BabyName2 = _("Violet")

            self.CharID = "chanyi"
            self.GaveBirthNotifText = _("Faymore ladies have given birth.")

            self.ShareFirstImpregNews = False
            self.ShareRepImpregNews = False
            self.DoPostBirthScene = False

        def PostImpreg(self):
            # 1st time
            if self.NumImpregs == 1:
                self.ShareFirstImpregNews = True
            elif self.NumImpregs > 1:
                self.ShareRepImpregNews = True
            return

        def PostBirth(self):
            self.DoPostBirthScene = True
            return

        def onEnter(self):
            if GetLocID() == "hamun_faymore_manor":
                if IsDaytime():
                    EventLabel = None
                    if CharIsVisiblyPreg("chanyi"):
                        if self.ShareFirstImpregNews:
                            EventLabel = "faymore_girls_impreg_first"
                        elif self.ShareRepImpregNews:
                            EventLabel = "faymore_girls_impreg_rep"
                    elif self.DoPostBirthScene:
                        self.DoPostBirthScene = False
                        EventLabel = "faymore_girls_give_birth"

                    if EventLabel is not None:
                        return TriggeredEvent(EventLabel)

# first time impreg
label faymore_girls_impreg_first:
    $ PregFaymoreGirls().ShareFirstImpregNews = False
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    show mc at center with easeinleft
    show chanyi at cleft with easeinleft
    show anya at cright with easeinright
    "No sooner had I entered their home, I was beset upon by both ladies."
    "Chanyi, with a deathly serious expression, and Anya, blushing as she looked down towards her stomach and tenderly rubbed it."
    CHANYI @serious "We need to talk."
    MC @think "U-Uhh... Is Anya—"
    CHANYI @serious "No."
    MC @think "Then what is—"
    CHANYI @serious "We both are."
    MC @surprised "...You're... {i}both?{/i}"
    "Chanyi took a deep sigh, rubbing her brow."
    ANYA @happy "We just thought you should know."
    CHANYI @serious "Our lives are complicated enough as it is, listen..."
    CHANYI @serious "We can keep this... {i}arrangement{/i} going."
    CHANYI @serious "But please, don't make this strange, alright?"
    MC @talk "Are you... keeping them?"
    "The two women shared a curious look."
    ANYA @happy "Yes, coin isn't exactly a concern for us."
    CHANYI @talk "We could afford to have a hundred children and it wouldn't make a dent."
    MC @smile "I see."
    CHANYI @laugh "That's not an invitation to try..."
    ANYA @blush "I wouldn't say no to more."
    CHANYI @shock "Urghh! I much prefer your unusual desires to this one."
    "Chanyi pouted."
    CHANYI @talk "But... that's all we had to say, so."
    CHANYI @talk "Do with this as you will."
    hide chanyi
    hide anya
    with dissolve
    "The two women turned to leave, discussing and playfully arguing among themselves over other matters."
    MC @smile "(Two children by two different women...)"
    MC @smile "(I think the prospect would terrify most men.)"
    MC @smile "(But I'm... strangely pleased.)"
    $ LocEnter()

# Repeat pregnancy dialogue
label faymore_girls_impreg_rep:
    $ PregFaymoreGirls().ShareRepImpregNews = False
    show mc at center with easeinleft
    show chanyi at cleft with easeinleft
    show anya at cright with easeinright
    CHANYI @laugh "I have an exciting idea!"
    CHANYI @laugh "{i}Learning to pull out from time to time!{/i}"
    MC @surprised "... Wait, you don't mean—"
    "Anya rubbed at her belly."
    ANYA @blush "You umm, seem really quite determined to keep the Faymore bloodline going."
    CHANYI @think "How the fuck do you keep getting us BOTH pregnant?"
    ANYA @blush "Maybe it's a blessing from the gods..."
    CHANYI @angry "More fucking bills, more like."
    CHANYI @talk "Whatever, nothing has changed, no matter how many children you pump into us."
    ANYA @sad "Be nicer, Chanyi."
    ANYA @lewd "Personally, the thought of him just using you as his breeding—"
    CHANYI @talk "Another time, darling."
    CHANYI @talk "Come on, we have other matters to attend to."
    hide chanyi
    hide anya
    with dissolve
    "Anya playfully waved at me as the two women turned to leave once again."
    MC @smile "(... Well, family gatherings are certainly going to be more interesting if this continues!)"
    $ LocEnter()

#### CHANYI AND ANYA GIVE BIRTH DIALOGUE
label faymore_girls_give_birth:
    show mc at center with easeinleft
    show chanyi at cleft with easeinleft
    show anya at cright with easeinright
    "Upon my entry, the two women approached me, each one cradling a small baby."
    "Anya beamed with pride, whilst Chanyi seemed more reserved, but still couldn't help but lift a soft smile."
    ANYA @happy "A boy and a girl."
    ANYA @happy "Aren't they just the CUTEST?"
    "Chanyi's eyes looked down at her daughter and then up towards me."
    CHANYI @talk "She has your annoying eyes."
    MC @smile "Annoying, huh?"
    ANYA @happy "We were thinking of names!"
    ANYA @talk "Did you have any suggestions?"
    $ PregFaymoreGirls().BabyName1 = renpy.input(_("What names shall we call them?"), default = _("Avalon"))
    $ PregFaymoreGirls().BabyName2 = renpy.input(_("...And?"), default = _("Violet"))
    ANYA @happy "Hmm, good choices."
    ANYA @happy "Hmm... I like it!"
    CHANYI @talk "... It's acceptable."
    CHANYI @talk "Anyway, we best put these little ones down for their nap."
    "Chanyi waved her hand dismissively."
    CHANYI @talk "Go... Do whatever it is you do."
    $ LocEnter()
