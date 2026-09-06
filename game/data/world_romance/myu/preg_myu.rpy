init python:
    @AppendToAllQuests
    @RegisterPregModuleFor("myu")
    class PregMyu(BasePregModule):  
        def __init__(self):
            super().__init__()

            self.CharID = "myu"
            self.BabyNameDefault = _("Lyu")
            self.GaveBirthNotifText = _("Myu has given birth.")

############ custom vars
            self.told_about_preg = False
            self.post_birth_scene = True

        def PostImpreg(self):
            self.told_about_preg = False
            return

        def PostBirth(self):
            self.post_birth_scene = True
            return

        def onEnter(self):  
            if GetLocID() in ["azul_safehouse", "azul_safehouse_bedroom"]:
                if self.post_birth_scene:
                    self.post_birth_scene = False
                    return TriggeredEvent("rom_myu_post_birth_scene")
                if CharIsVisiblyPreg("myu"):
                    if self.told_about_preg == False:
                        self.told_about_preg = True
                        if self.NumImpregs == 1:
                            return TriggeredEvent("rom_myu_post_impreg_scene")

        def extraDialogue(self):
            if self.NumBirths > 0:
                yield("myu_root", DNode(_("How's %s?") % self.LastBornBabyName, "rom_myu_how_is_baby"))

label rom_myu_post_impreg_scene:
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    show mc at cleft with easeinleft
    show myu at center_f with easeinright
    MYU @joy "Myu did it! Myu was good wife!"
    MC @talk "Myu? What are you talking about?"
    "Myu took my hand and placed it on her belly."
    MYU @talk "{i}Baby...{/i} We make baby."
    MC @surprised "You're... pregnant?"
    'Myu nodded happily.'
    MYU @joy "Now Myu can also become a good Mommy AND a good wife!"
    MYU @sad " ...[player_name!t] is happy, right?"
    MC @think "Uhh..."
    MC @smile "Of course, Myu!"
    MC @think "Just a lot for me to think about, I guess."
    MYU @talk "It's okay, Myu will do good!"
    MYU @joy "No worries!"
    MC @think "Do you need me to get food or..."
    MYU @smile "Don't worry, Myu learnt a lot about looking after self."
    MYU @smile "Baby will be strong."
    MYU @talk "Can feel your 'gift' inside of it already."
    MC @surprised "Uh, my-"
    MYU @talk "Don't worry, my love."
    MYU @smile "Baby good."
    MC @talk "Uhh, right."
    MC @talk "Well, let me know if you need anything then I suppose."
    'Myu stepped forward and gave me a quick hug before pulling away, going about her business as normal.'
    show myu at blurin, center
    hide myu with easeoutright
    BLACK "({i}Good{/i}.)"
    BLACK "({i}Is good to have such a willing brood with such unique genetic makeup{/i}.)"
    MC "(You say some strange things sometimes...)"
    $ LocEnter()

label rom_myu_post_birth_scene:
    show mc at cleft with easeinleft
    show cg_myu_baby at center with easeinright
    MYU @joy "Baby!"
    'Myu, somewhere between absolute joy and a strange smug pride, hurried around the room holding the small, strange translucent child in her arms.'
    'Myu held out the baby towards me.'
    MYU @smile "See? We do good!"
    MC @talk "I..."
    "For a moment, I almost panicked seeing the sudden bundle of responsibility laying before me, and all the worry that would follow."
    "The sudden paternal pride began to swell, overpowering any concerns and worries I had in the moment about the small child before me."
    "Whether that was the influence of the Dark Passenger or not, I wasn't sure."
    "The small blue tentacle for an arm reached out and wrapped around my thumb."
    MYU @joy "See? They know you're their papa!"
    MC "Is it... A boy, or?"
    MYU @think "Hm?"
    MYU @smile "They're whatever they want to be!"
    MYU @think "We should probably give them a name though..."
    $ PregMyu().LastBornBabyName = renpy.input(_("What name shall we give, my love?"), default = PregMyu().BabyNameDefault)
    MYU @smile "Oooh, okay!"
    MYU @smile "Myu like that name!"
    MYU @talk "I best feed the little one and put her down to rest for a while."
    MYU @smile "Stay for a little while if you want, Myu doesn't mind.{image=[ICON.HEART]}"
    $ LocEnter()

label rom_myu_how_is_baby:
    MC @talk "How is [PregMyu().LastBornBabyName], Myu?"
    $ rng = RngInt(0, 3)
    if rng == 0:
        MYU @joy "Everything is good! Today, Myu was showing them how to make basic stuff like hammers!" 
        MYU @think " ...They managed to make a point blade too..."
        MYU @joy "But hopefully [PregMyu().LastBornBabyName] will play nice with others and not stabby them!"
    elif rng == 1:
        MYU @think "Today, they just mostly slept."
        MYU @smile "[PregMyu().LastBornBabyName] keeps pushing themselves so hard to change form that they just make themselves sleepy!"
    elif rng == 2:
        MYU @sad "They are a little sad today... little unwell." 
        MC @talk "Do they need anything?"
        MYU @talk "Just rest... And maybe Myu's new mama soup!"
        MYU @smile "Want to try some?"
        MC @talk "Uh, another time, Myu."
        MYU @smile "M'okay!"
    elif rng == 3:
        MYU @think "Today, Myu help [PregMyu().LastBornBabyName] read and learn books!" 
        MYU @think " ...Need to try to stop them trying to eat the books."
    return