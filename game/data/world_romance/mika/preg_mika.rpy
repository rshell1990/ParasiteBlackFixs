init python:
    @AppendToAllQuests
    @RegisterPregModuleFor("mika")
    class PregMika(BasePregModule):  
        def __init__(self):
            super().__init__()

            self.CharID = "mika"
            self.GaveBirthNotifText = _("Mika has given birth.")

            self.BabyNameDefault = _("Nora")
            self.BabyNameRandomList = [_("Lucile")]
################## custom vars
            self.post_birth_scene = False
            self.told_about_preg = False
            self.told_about_preg_two = False

        def PostBirth(self):
            self.post_birth_scene = True
            return

        def onEnter(self):  
            if GetLocID() == "novaras_palam_mainhall":
                if self.post_birth_scene:
                    self.post_birth_scene = False
                    if self.NumBirths == 1:
                        return TriggeredEvent("rom_mika_first_post_birth_scene")
                    elif self.NumBirths > 1:
                        return TriggeredEvent("rom_mika_post_birth_scene")

                if CharIsVisiblyPreg("mika"):
                    # second pregnancy news
                    if self.NumImpregs == 1:
                        if not self.told_about_preg:
                            self.told_about_preg = True
                            return TriggeredEvent("rom_mika_first_post_impreg_scene")
                    # first preg news
                    elif self.NumImpregs > 1:
                        if not self.told_about_preg_two:
                            self.told_about_preg_two = True
                            return TriggeredEvent("rom_mika_post_impreg_scene")

        def extraDialogue(self):
            if self.NumBirths > 0:
                yield( "mika_root", DNode(_("How's %s?") % self.LastBornBabyName, "rom_mika_how_is_baby"))


###########################################################################################################################
#Pregnant Mika unique scene
label rom_mika_first_post_impreg_scene:
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    show mc at cleft with easeinleft
    show mika at center_f with easeinright
    "As soon as I entered the great halls, Mika, upon noticing me, came hurrying over, her eyes anxious and wide."
    MIKA @scared "W-We need to talk!"
    MC @think "Mika?"
    MC @think "What is it?"
    MIKA @scared "I'm-"
    show divine at cright_f with easeinright
    DIVINE @happy "Why, blessed with a holy ordained child, of course!"
    MC @surprised "W-What?!"
    "I felt my heart slightly fall into my stomach with the words."
    MC @think "Mika, you're..."
    MC @surprised "{i}Pregnant?{/i}"
    MIKA @blush "I..."
    MIKA @blush "{i}Y-Yes.{/i}"
    DIVINE @happy "Of course, this {i}holy{/i} child is a blessing from Palam."
    DIVINE @happy "Why, a {i}virgin birth,{/i} how wonderful!"
    "Mika opened her mouth to say something, but as Sister Divine snapped her a knowing look, she quickly averted her gaze."
    DIVINE @happy "You must forgive her, [player_name!t]."
    DIVINE @angry "No doubt all reason has left her thanks to the goddess' blessing filling her womb."
    "Mika shyly continued to look away."
    DIVINE @happy "But I trust you can keep quiet about this... {i}miraclulous conception.{/i}"
    DIVINE @happy "We wouldn't want anyone to question the purity of our holy ordained mages, would we?"
    MC @talk "Of course... Sister, my lips are sealed."
    "Seemingly satisfied with my answer, Sister Divine bowed gracefully before leaving."
    show divine at blurin, cright
    hide divine with easeoutright
    MIKA @sad "I'm sorry about that..."
    MIKA @sad "This isn't the first time something like this has happened with other girls."
    MC @sad "Will I still be allowed to see the child?"
    MIKA @shock "I-If you want to!"
    "Mika seemed more surprised than anything that I'd want to still be involved with the child."
    MIKA @sad "But, there's no expectations for you... Between myself and the other mages of Palam, the child would be raised in one of the towers if they're born with the goddess' blessing."
    MIKA @talk "Y-You'd still be allowed to be involved in the child's life if you wish."
    MIKA @talk "As l-long as you could keep the fact you're their father a secret."
    MC @surprised "I-"
    MIKA @shock "Y-You don't need to answer now..."
    MIKA @smile "It's... alright, honestly."
    MIKA @talk "I c-can't ask you to stay here just for me."
    MIKA @smile "B-But if {i}you want to...{/i}"
    MIKA @blush "{i}W-We{/i} can be a part of your life."
    "As I reached out to touch Mika, whose heart was no doubt racing at her declaration, she quickly turned heel and hurried off."
    show mika at blurin, center
    hide mika with easeoutright
    MC @surprised "Mika!"
    show mc at center with ease
    MC "(That girl...)"
    MC "(I might not be able to see her as much as I'd like, but I won't abandon her and our child!)"
    MC "(It's so strange... I thought I might be more afraid; instead, all I feel is a surge of pride and...)"
    MC "(Protectiveness.)"
    BLACK "({i}Our offspring must be protected.{/i})"
    BLACK "({i}I have made sure such doubts are removed from your mind... Our sired young are precious.{/i})"
    MC @think "(You're the reason for that?)"
    BLACK "({i}It would not serve us well for you to fear creating our spawns... I ensure with every new one created, your mind is filled with serotonin and dopamine.{/i})"
    MC @think "(Sero- what?)"
    MC @serious "(Is this some kind of sorcery you speak of?)"
    BLACK "({i}No sorcery, only biology.{/i})"
    BLACK "({i}Relax... You and I are one in the same.{/i})"
    BLACK "({i}Whatever I do, is for our benefit.{/i})"
    "I can't say I particularly always trusted the intent of the strange, dark passenger inside my mind."
    "But if there was one thing I could trust, it was the obsessive nature over 'breeding' the voice inside me had."
    MC "(How many young exactly do you expect me to sire?)"
    MC "(...Hello?)"
    MC "(Hmph... I suppose that answers that then.)"
    $ LocEnter()

##############################################################################################################################
#AFTER MIKA GIVES BIRTH
label rom_mika_first_post_birth_scene:
    show mc at cleft with easeinleft
    show divine at cright_f with easeinright
    "Entering into the great halls of the tower of Palam, alerted to my presence, Sister Divine came hurrying over."
    DIVINE @talk "Come with me."
    MC @think "Sister?"
    DIVINE @talk "Follow..."
    "Leading me down the winding paths and hallways, Divine led me straight towards the girls' quarters, where Mika stood proudly, nursing a small, gurgling, blue baby in her arms." #Cut to girls' dorm
    scene black with dissolve
    $ LocSet("novaras_palam_dorm")
    $ LocFlush()
    show cg_mika_baby at cright_f
    with dissolve
    show mc at cleft with easeinleft
    show divine at left with easeinleft
    MIKA @smile "Hush now, little one..."
    MIKA @smile "D-Daddy is here."
    "I felt the shortness of my breath as I nervously approached the two of them."
    "Seeing my... {i}our{/i} child in her arms."
    "The feeling was overwhelming."
    MIKA @blush "S-She has the blessing."
    MIKA @blush "She's a mage of Palam."
    "As I reached out, one of the small hands of {i}our{/i} baby reached out, ever so gently wrapping around my finger."
    MIKA @blush "{i}S-She likes you.{/i}"
    "Sister Divine stood vanguard over the scene, and while she tried to remain somewhat stoic and pragmatic about the whole thing, her lips curled ever so slightly into a soft smile."
    DIVINE @happy "You should pick a name for her."
    MIKA @shock "I - I haven't even thought about names!"
    MIKA @blush "D-Do you have any ideas?"
    $ PregMika().LastBornBabyName = renpy.input(_("What do you think, my love?"), default = PregMika().BabyNameDefault)
    MIKA @smile "Hmm... I like it."
    DIVINE @talk "You should rest now, Mika."
    MIKA @smile "Mm, yes... Rest sounds good."
    MIKA @smile "C-Come see us soon."
    MIKA @smile "{i}... My love.{/i}"
    "Just saying those words made Mika's cheeks burn red from embarrassment, but after a gentle kiss on her soft lips and the child's forehead, I stepped back, escorted out by Sister Divine."
    DIVINE @talk "Give her a day or so to recover, then come see her." #Cut back to the main hallway
    scene black with dissolve
    $ LocSet("novaras_palam_mainhall")
    $ LocFlush()
    with dissolve
    show mc at cleft_f with easeinleft
    show divine at cright_f with easeinright
    show mc at blurin, cleft
    MC @talk "Sister Divine..."
    MC @talk "I suspected you might be more upset about all of this."
    DIVINE @happy "It's like I told you, [player_name!t]."
    DIVINE @talk "As long as what happens within these walls stays here, it pleases me Mika can find some happiness."
    DIVINE @talk "But if you were to go shouting about this to the outside world..."
    DIVINE @talk "{i} I would have to accuse you as a blasphemer and see that inquisition looks into you.{/i}"
    MC @surprised "...Sister Divine."
    DIVINE @talk "I like you a great deal, [player_name!t]."
    DIVINE @talk "But I take the safety of {i}my{/i} girls very seriously."
    MC @talk "Hmm... I understand."
    DIVINE @happy "Good."
    DIVINE @happy "As long as you remember that, there will be no problems."
    "With a gentle bow, Sister Divine turned to graciously leave."
    hide divine with easeoutleft
    MC "(I hope I never end up on her bad side.)"
    $ LocEnter()

###############################################################################################################################
#Mika pregnant repeat variable
label rom_mika_post_impreg_scene:
    show mc at cleft with easeinleft
    show mika at center_f with easeinright
    "As soon as I entered the great halls, Mika, upon noticing me, came hurrying over, her eyes anxious and wide."
    MIKA @scared "U-Ummm..."
    MC @think "Mika?"
    MC @think "What is it?"
    MIKA @scared "I'm-"
    show divine at cright_f with easeinright
    DIVINE @happy "My, my..."
    DIVINE @happy "It seems the gods are indeed working their miracles!"
    "Sister Divine spoke with a hint of anger."
    DIVINE @happy "Mika has been blessed with a holy ordained child once more!"
    MC @surprised "A-Again?!"
    "I felt my heart slightly fall into my stomach with the words."
    MC @think "Mika, you're..."
    MC @surprised "{i}Pregnant?{/i}"
    MIKA @blush "I..."
    MIKA @blush "Y-Yes."
    DIVINE @happy "...{i}Well.{/i}"
    DIVINE @happy "Having gone through this before, I trust you both remember everything we discussed?"
    MC @talk "Yes, of course."
    DIVINE @happy "Good, well then, I shall leave you both be."
    DIVINE @happy "I'm sure you have... {i}much{/i} to discuss." 
    "As Divine turned to leave, Mika sheepishly stepped closer towards me."
    show divine at blurin, cright
    hide divine with easeoutright
    MIKA @sad "I- I know you weren't expecting this again."
    MIKA @sad "Everything we talked about before is still t-true; nothing has changed."
    MIKA @sad "Umm, t-that's all I really have to say."
    MC @smile "Don't worry, Mika, I'll be here for you."
    "Mika smiled warmly at my words."
    MIKA @smile "I - I'm going to head back to the girls' quarters."
    MIKA @smile "I'll be there if you need me."
    show mika at cright_f with ease
    show mika at blurin, cright
    hide mika with easeoutright
    "Taking a few steps back, Mika spun herself around and moved quickly towards the women's quarters."
    show mc at center with ease
    MC "(... Another child with Mika.)"
    MC "({i}A mage of Palam.{/i})"
    MC "(I really do leave my fate to the gods sometimes, don't I?)"
    MC "(I should check in on Mika from time to time... Make sure she and the baby are alright.)"
    $ LocEnter()

##############################################################################################################################
#AFTER MIKA GIVES BIRTH
label rom_mika_post_birth_scene:
    show mc at cleft with easeinleft
    show divine at cright_f with easeinright
    "Entering into the great halls of the tower of Palam, alerted to my presence, Sister Divine came hurrying over."
    DIVINE @talk "Come with me."
    MC @think "Sister?"
    DIVINE @talk "Follow..."
    show divine at blurin, cright
    hide divine with easeoutright
    hide mc with easeoutright
    "Leading me down the winding paths and hallways, Divine led me straight towards the girls' quarters, where Mika stood proudly, nursing a small, gurgling, blue baby in her arms." #Cut to girls' dorm
    scene black with dissolve
    $ LocSet("novaras_palam_dorm")
    $ LocFlush()
    show cg_mika_baby at cright_f
    with dissolve
    show mc at cleft with easeinleft
    show divine at left with easeinleft
    MIKA @smile "Hush now, little one..."
    MIKA @smile "D-Daddy is here."
    "I felt the shortness of my breath as I nervously approached the two of them."
    "Seeing my... {i}our{/i} child in her arms."
    "The feeling was overwhelming."
    MIKA @blush "S-She has the blessing."
    MIKA @blush "She's a mage of Palam."
    "As I reached out, one of the small hands of {i}our{/i} baby reached out, ever so gently wrapping around my finger."
    MIKA @blush "{i}S-She likes you.{/i}"
    "Sister Divine stood vanguard over the scene, and while she tried to remain somewhat stoic and pragmatic about the whole thing, her lips curled ever so slightly into a soft smile."
    DIVINE @happy "You should pick a name for her."
    MIKA @shock "I - I haven't even thought about names!"
    MIKA @blush "D-Do you have any ideas?"
    $ PregMika().LastBornBabyName = renpy.input(_("What do you think, my love?"), default = renpy.random.choice(PregMika().BabyNameRandomList))
    MIKA @smile "Hmm... I like it."
    DIVINE @talk "You should rest now, Mika."
    MIKA @smile "Mm, yes... Rest sounds good."
    MIKA @smile "C-Come see us soon."
    MIKA @smile "{i}... My love.{/i}"
    "Just saying those words made Mika's cheeks burn red from embarrassment, but after a gentle kiss on her soft lips and the child's forehead, I stepped back, escorted out by Sister Divine."
    DIVINE @talk "Give her a day or so to recover, then come see her." #Cut back to the main hallway
    scene black with dissolve
    $ LocSet("novaras_palam_mainhall")
    $ LocFlush()
    with dissolve
    show mc at cleft_f with easeinright
    show divine at cright_f with easeinright
    show mc at blurin, cleft
    MC @talk "Divine..."
    DIVINE @embar "You're very... {i}fertile,{/i} aren't you?"
    MC @embarr "I ... Yes."
    DIVINE @lewd "...{i}Interesting.{/i}"
    show divine at blurin, cright
    hide divine with easeoutright
    "With a smirk, Sister Divine turned heel and made her way down one of the many hallways."
    MC "(Well... That went better than last time.)"
    $ LocEnter()