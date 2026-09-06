init python:
    @AppendToAllQuests
    @RegisterPregModuleFor("vizura")
    class PregVizura(BasePregModule):  
        def __init__(self):
            super().__init__()

            self.CharID = "vizura"
            self.GaveBirthNotifText = _("Vizura has given birth.")
############## custom vars
            self.ShareFirstImpregNews    = False
            self.ShareSecondImpregNews   = False
            self.DoFirstBabyScene        = False
            return

        def PostImpreg(self):
            # 1st time
            if self.NumImpregs == 1:
                self.ShareFirstImpregNews = True
            elif self.NumImpregs > 1:
                self.ShareSecondImpregNews = True
            return

        def PostBirth(self):
            if self.NumBirths == 1:
                self.DoFirstBabyScene = True
            return


label vizura_share_first_impreg_news:
    show cg_goblin_caravan with dissolve
    show vizura at center with easeinright
    $ PregVizura().ShareFirstImpregNews = False
    VIZURA @lewd "Well Well well... Look whatchu done, eh?"
    "Vizura rubbed her belly."
    VIZURA @lewd "You've only gone and knocked me up human, fufu."
    "I felt my heart drop into my stomach."
    MC @surprised "Y-You're-"
    VIZURA @laugh "Uhuh, bred like a mare in heat!"
    VIZURA @happy "Don't worry though, like I said, I don't expect anything from you!"
    VIZURA @lewd "Just thought you should know."
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    jump vizura_caravan_talk_menu

label vizura_share_second_impreg_news:
    show cg_goblin_caravan with dissolve
    show vizura at center with easeinright
    $ PregVizura().ShareSecondImpregNews = False
    VIZURA @lewd "Fufu, you just can't help yourself around me, can you?"
    MC @surprised "What do you-"
    "Vizura rubbed her belly once again."
    VIZURA @lewd "I hope the other ladies don't get jealous knowing you keep getting me pregnant."
    MC @surprised "You're-"
    MC @surprised "{i}Again?{/i}"
    VIZURA @lewd "That's what happens when you keep filling me with load after load, handsome."
    VIZURA @happy "Don't worry though, like I said, I still don't expect anything from you sooo..."
    VIZURA @lewd "Don't you worry that silly huge cock of yours about it, handsome."
    MC "(I'm gonna need to be more careful in the future, else there's going to be a small tribe of goblin's running around looking awfully similar to me.)"
    MC "(...That one might be hard to explain.)"
    jump vizura_caravan_talk_menu

label vizura_first_baby_scene:
    show cg_goblin_caravan with dissolve
    show vizura at center with easeinright
    $ PregVizura().DoFirstBabyScene = False
    "With the small goblin baby in her arms, Vizura approached me smiling from ear to ear as the small child cried."
    VIZURA @happy "Well, look what we made eh?"
    MC @surprised "Is that-"
    VIZURA @happy "It is! Our little future chieftain!"
    VIZURA @happy "Hehe, I picked a good one with you, I can tell he's gonna be real strong already!"
    BLACK "({i}You're welcome.{/i})"
    BLACK "({i}This mate pleases me, she is eager to sire us many young, and our enhanced goblins will easily overpower the weaker native ones.{/i})"
    MC "(Great ... Super goblins, just what the world needs.)"
    jump vizura_caravan_talk_menu