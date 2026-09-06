init python:
    @AppendToAllQuests
    @RegisterPregModuleFor("lady_tarbeck")
    class PregLadyTarbeck(BasePregModule):
        def __init__(self):
            super().__init__()

            self.CharID = "lady_tarbeck"
            self.GaveBirthNotifText = _("Lady Tarbeck has given birth!")

            self.BabyName = _("Harlok")

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
                    if RomanceLadyTarbeck().Kind == "romance":
                        if self.ShowPostBirth_First:
                            Label = "rom_tarbeck_birth_first"
                        elif self.ShowPostBirth_Rep:
                            Label = "rom_tarbeck_birth_rep"
                        if CharIsVisiblyPreg("lady_tarbeck"):
                            if self.ShowPostImpreg_First:
                                Label = "rom_tarbeck_impreg_first"
                            elif self.ShowPostImpreg_Rep:
                                Label = "rom_tarbeck_impreg_rep"
                    elif RomanceLadyTarbeck().Kind == "darkmage":
                        if self.ShowPostBirth_First:
                            Label = "rom_tarbeck_darkmage_birth_first"
                        elif self.ShowPostBirth_Rep:
                            Label = "rom_tarbeck_darkmage_birth_rep"
                        if CharIsVisiblyPreg("lady_tarbeck"):
                            if self.ShowPostImpreg_First:
                                Label = "rom_tarbeck_darkmage_impreg_first"
                            elif self.ShowPostImpreg_Rep:
                                Label = "rom_tarbeck_darkmage_impreg_rep"
                    elif RomanceLadyTarbeck().Kind == "bimbo":
                        if self.ShowPostBirth_First:
                            Label = "rom_tarbeck_bimbo_birth_first"
                        elif self.ShowPostBirth_Rep:
                            Label = "rom_tarbeck_bimbo_birth_rep"
                        if CharIsVisiblyPreg("lady_tarbeck"):
                            if self.ShowPostImpreg_First:
                                Label = "rom_tarbeck_bimbo_impreg_first"
                            elif self.ShowPostImpreg_Rep:
                                Label = "rom_tarbeck_bimbo_impreg_rep"
                    if Label is not None:
                        return TriggeredEvent(Label, priority = 1)
            return

label rom_tarbeck_impreg_first:
    $ PregLadyTarbeck().ShowPostImpreg_First = False
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @sad "We... We need to talk."
    LADY_TARBECK @sad "{i}Now.{/i}"
    MC @think "Lady Tarbeck? What is it?"
    "Lady Tarbeck looked down, her hands gently rubbing over her stomach."
    LADY_TARBECK @blush "It seems..."
    LADY_TARBECK @blush "Our activities have gotten us a little more than we bargained for."
    MC @surprised "My lady, I-"
    LADY_TARBECK @blush "L-Lord Tarbeck is willing to raise him... Her... Whatever they turn out to be."
    LADY_TARBECK @think "He can hardly criticize me, given his own bastards could fill this hall."
    MC @talk "What do you need of me, my lady?"
    LADY_TARBECK @blush "Nothing, I-"
    LADY_TARBECK @sad "... Just don't forget us, alright?"
    LADY_TARBECK @sad "I don't care where the road leads you... Find one back to me."
    MC @surprised "Lady Tarbeck... I-"
    LADY_TARBECK @smile "And..."
    LADY_TARBECK @talk "That's all I had to say."
    LADY_TARBECK @smile "May the new gods always protect you, [player_name]."
    $ LocEnter()

label rom_tarbeck_impreg_rep:
    $ PregLadyTarbeck().ShowPostImpreg_Rep = False
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @angry "Ahem!"
    "Lady Tarbeck pouted as she hurried over."
    LADY_TARBECK @talk "Am I a bakery?"
    MC @think "What?"
    LADY_TARBECK @smile "Because you keep putting a bun in the oven."
    MC @talk "... You-"
    MC @surprised "You're pregnant?!"
    LADY_TARBECK @smile "Well done, genius."
    MC @embarr "I mean, I-"
    LADY_TARBECK @blush2 "What did you think would happen if you kept sticking your cock in me?"
    LADY_TARBECK @smile "The gods would just decide, 'Ooh, that's enough for now.'"
    "She laughed softly."
    LADY_TARBECK @smile "Don't worry... Nothing's changed."
    LADY_TARBECK @talk "Except my horniness."
    MC @smile "I can fix that."
    LADY_TARBECK @blush2 "Oh, I know you can."
    LADY_TARBECK @talk "Return to me soon, [player_name]."
    LADY_TARBECK @smile "I imagine I'm going to need your services again soon."
    $ LocEnter()

label rom_tarbeck_birth_first:
    $ PregLadyTarbeck().ShowPostBirth_First = False
    show mc at cleft with easeinleft
    "As I entered the great hall of the Tarbeck estate, I heard... crying?"
    show lady_tarbeck at cright_f with easeinright
    "A small, gurgling cry as Lady Tarbeck smiled, cradling the crying babe wrapped in blankets in her arms."
    MC @surprised "Is that-"
    LADY_TARBECK @smile "Our adorable little boy."
    LADY_TARBECK @smile "He's got your eyes... See?"
    LADY_TARBECK @smile "Now, help me pick a name... What about..."
    $ PregLadyTarbeck().BabyName = renpy.input(_("Now, help me pick a name... What about..."), default = PregLadyTarbeck().BabyName)
    LADY_TARBECK @smile "That's a lovely name."
    LADY_TARBECK @smile "Well, I'm going to put this little prince down for his nap."
    "As she began to walk away, Lady Tarbeck looked back and smirked."
    LADY_TARBECK @blush2 "Come see us again soon... I can promise you won't regret it."
    hide lady_tarbeck with easeoutright
    "My eyes remained firmly glued to her ass as I watched her leave."
    show mc at center with ease
    MC @smile "(Did she even need to ask?)"
    $ LocEnter()

label rom_tarbeck_birth_rep:
    $ PregLadyTarbeck().ShowPostBirth_Rep = False
    show mc at cleft with easeinleft
    "Entering the halls of the Tarbeck estate, Lady Tarbeck was once again soothing a small, crying babe wrapped in blankets in her arms."
    show lady_tarbeck at cright_f with easeinright
    "She looked up at me and smiled mischievously."
    LADY_TARBECK @smile "Look, little one!"
    LADY_TARBECK @smile "{i}Father's home...{/i}"
    MC @surprised "Is that really-"
    LADY_TARBECK @talk "Yes..."
    "Lady Tarbeck chuckled."
    LADY_TARBECK @smile "My husband has already received so many congratulations..."
    LADY_TARBECK @talk "I suppose that's the benefit of being so pious for so long."
    LADY_TARBECK @blush2 "No one questions whether {i}I{/i} might misbehave."
    MC @smile "... Is it a boy, or a-"
    LADY_TARBECK @talk "A girl."
    LADY_TARBECK @smile "An adorable baby girl."
    LADY_TARBECK @talk "... Say, what do you think of-"
    $ PregLadyTarbeck().BabyName = renpy.input(_("... Say, what do you think of-"), default = _("Marliene"))
    LADY_TARBECK @smile "I love it."
    LADY_TARBECK @talk "Well, I'd best put this little princess down for a nap."
    LADY_TARBECK @smile "Be sure to, umm... Visit me again soon."
    LADY_TARBECK @blush2 "This oven seems to be open for another bun..."
    hide lady_tarbeck with easeoutright
    "As she walked away, my cock throbbed at the sight of her swaying, cute butt walking down the corridor."
    show mc at center with ease
    MC @smile "(Who could have ever imagined she'd be THIS wild?)"
    $ LocEnter()




#########################################################
#########################################################
#########################################################
################# darkmage variants
label rom_tarbeck_darkmage_impreg_first:
    $ PregLadyTarbeck().ShowPostImpreg_First = False
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @smile "Well... Look who's decided to visit, hmm?"
    MC @think "Lady Tarbeck? Is everything alright?"
    LADY_TARBECK @smile "Oh, I'm better than alright."
    "Lady Tarbeck grabbed at my hand and carefully placed it onto her stomach."
    LADY_TARBECK @smile "It seems the Tarbeck household has secured its future heir..."
    MC @shock "... Is it-"
    LADY_TARBECK @blush "Yes... It is."
    "Lady Tarbeck stepped closer, her hands cupping over my balls as she whispered in my ear."
    LADY_TARBECK "Your big, heavy balls knocked up my poor defenceless womb."
    "She ever so slyly ran her tongue along my neck before retreating."
    MC @shock "Does Lord Tarbeck know?"
    LADY_TARBECK @smile "Of course, he's delighted."
    MC @think "Really?"
    LADY_TARBECK @angry "I don't care if he's not."
    LADY_TARBECK @angry "Given the number of bastards he spent years humiliating me with."
    "Lady Tarbeck took the briefest moment to adjust herself."
    LADY_TARBECK @smile "Ahem... The point is, I am fine, better than fine, really!"
    LADY_TARBECK "And you should definitely... definitely keep putting your spawn in me, one for every little bastard he made."
    MC @shock "I... Uhh..."
    LADY_TARBECK @smile "Just a thought."
    hide lady_tarbeck with dissolve
    "With a quick kiss on the cheek, Lady Tarbeck practically skipped away, happily humming to herself."
    show mc at center with ease
    $ LocEnter()

label rom_tarbeck_darkmage_impreg_rep:
    $ PregLadyTarbeck().ShowPostImpreg_Rep = False
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @smile "Well, well, well..."
    LADY_TARBECK @smile "It seems you really took my words to heart."
    "Lady Tarbeck stepped closer, grabbing my hand as she carefully rested it onto her stomach as she whispered alluringly in my ear."
    LADY_TARBECK @blush "Do you intend to keep your little dark mage slut bred all the time?"
    LADY_TARBECK @blush "Or can you just not keep your cock out of me long enough?"
    MC @shock "Another one?"
    "Lady Tarbeck's grin widened."
    LADY_TARBECK @smile "Another one."
    MC @talk "Lady Tarbeck... I-"
    hide lady_tarbeck with dissolve
    "Lady Tarbeck smiled and laughed, leaning forward to kiss me on the cheek before leaving, happily humming to herself."
    show mc at center with ease
    $ LocEnter()

label rom_tarbeck_darkmage_birth_first:
    $ PregLadyTarbeck().ShowPostBirth_First = False
    show mc at cleft with easeinleft
    show lady_tarbeck at cright_f with easeinright
    LADY_TARBECK @smile "There he is...!"
    "Lady Tarbeck smiled, holding the small child wrapped in blankets."
    LADY_TARBECK @smile "Come on, little one. Let's go meet your father..."
    "Her grin widens."
    LADY_TARBECK @blush2 "Your real one."
    "Lady Tarbeck presented the baby to me."
    LADY_TARBECK @smile "A beautiful baby girl..."
    "The small baby's hand reached out, carefully cupping her whole hand around one of my fingers."
    MC @smile "She's beautiful."
    "There's a momentary crack in Lady Tarbeck, the dark mage vanishes, and Lady Tarbeck as she was before is looking down at the small child, our child, and nearly cries."
    LADY_TARBECK @talk "Ahem..."
    LADY_TARBECK @talk "She needs a name, I was thinking..."
    $ PregLadyTarbeck().BabyName = renpy.input(_("She needs a name, I was thinking..."), default = _("Kariena"))
    LADY_TARBECK @smile "Yes... That's the one."
    LADY_TARBECK @talk "Well, if you'll excuse me, I better go put this little one down."
    hide lady_tarbeck with easeoutright
    show mc at center with ease
    $ LocEnter()

label rom_tarbeck_darkmage_birth_rep:
    $ PregLadyTarbeck().ShowPostBirth_Rep = False
    show mc at cleft with easeinleft
    show lady_tarbeck at cright_f with easeinright
    LADY_TARBECK @smile "Welcome back."
    LADY_TARBECK @smile "Come say hello to your new daughter."
    "Lady Tarbeck approached me, smiling as she held a small, crying baby wrapped in blankets."
    "The small baby's hands reached out, as if she cutely wanted to touch my face."
    MC @smile "You have a remarkable talent for making the cutest babies, it seems."
    LADY_TARBECK @smile "Well... I have some help making them, don't I?"
    LADY_TARBECK @talk "Anyway, how do you feel about the name..."
    $ PregLadyTarbeck().BabyName = renpy.input(_("Anyway, how do you feel about the name..."), default = _("Anisa"))
    LADY_TARBECK @smile "Hmm... Very well then."
    LADY_TARBECK @talk "For now, though, I think this little one needs her nap..."
    $ LocEnter()






#########################################################
#########################################################
#########################################################
#First time pregnancy
#triggered auto upon entering into Tarbeck Manor main hall
label rom_tarbeck_bimbo_impreg_first:
    $ PregLadyTarbeck().ShowPostImpreg_First = False
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @smile "WE MADE A TINY TENTACLE MONSTER!"
    MC @shock "... Wait, what?"
    "Lady Tarbeck grabbed my hand and pushed it towards her stomach."
    LADY_TARBECK @smile "See? You put a baby in me!"
    MC @shock "You're pregnant?"
    LADY_TARBECK @smile "Uhuh! What did you think would happen when you kept painting my womb white?"
    LADY_TARBECK @smile "Theyre gonna be the cutest little monster ever!"
    MC @think "I... The child will likely appear human."
    LADY_TARBECK @shock "*Gasp!*"
    LADY_TARBECK @smile "They're gonna be the prettiest little half human baby EVER!"
    MC @think "Does Lord Tarbeck know?"
    LADY_TARBECK @smile "Of course he does!"
    LADY_TARBECK @smile "We're like, gonna get the little ones you and I make to play together with all the little ones he's already made with other women!"
    LADY_TARBECK @smile "We're gonna be like, one big happy family! Hehe!"
    MC @think "... Wait, did you just say little ones... Like more than one, with me and you?"
    LADY_TARBECK @blush "Uhuh, I'm gonna leg lock you ever time we fuck so we can make another one after this!"
    MC @talk "... Well, at least you're honest."
    LADY_TARBECK @smile "I'm gonna go shopping shortly, like, come by from time to time so we can fuck and stuff!"
    LADY_TARBECK @blush "I'll even let you put it in my butt! I promise!"
    "I felt cock stiffen at the comment."
    MC @smile "A... Tempting offer."
    LADY_TARBECK @smile "See you soooon!"
    hide lady_tarbeck with dissolve
    MC @smile "(I should be frightened but...strangely I'm happy?)"
    show mc at center with ease
    $ LocEnter()



#Repeat pregnancy
#triggered auto upon entering into Tarbeck Manor main hall
label rom_tarbeck_bimbo_impreg_rep:
    $ PregLadyTarbeck().ShowPostImpreg_Rep = False
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @smile "Hehe! Guess who put another adorable little bun in the oven?"
    MC @shock "You're pregnant again?"
    LADY_TARBECK @smile "Uhuh!"
    LADY_TARBECK @blush "I'm gonna have alllll your kittens!"
    "Lady Tarbeck took my hand and placed it onto her stomach affectionately."
    LADY_TARBECK @smile "I love you..."
    MC @shock "... I-"
    LADY_TARBECK @blush "And your big silly cock and very drainable balls."
    MC @smile "Ah... That's more what I expected to hear."
    LADY_TARBECK @smile "Anyway, I gotta go for now!"
    LADY_TARBECK @smile "Thanks for making another baby with me!"
    hide lady_tarbeck with dissolve
    "Lady Tarbeck practically skipped away, happily humming to herself."
    show mc at center with ease
    $ LocEnter()


#birth first time
#triggered auto upon entering into Tarbeck Manor main hall
label rom_tarbeck_bimbo_birth_first:
    $ PregLadyTarbeck().ShowPostBirth_First = False
    show lady_tarbeck at cright_f with dissolve
    show mc at cleft with easeinleft
    "As the great doors to the Tarbeck manor swung ope, Lady Tarbeck was cuddling a small, crying babe wrapped in blankets."
    LADY_TARBECK @smile "Hehe, we made a thing, see?"
    "Lady Tarbeck presented the small baby to me, her hand reaching out to touch at my face."
    LADY_TARBECK @smile "Isn't she just the cutest?!"
    LADY_TARBECK @think "Do you think like, she'll get my smarts before I changed? Or do you think she'll get my boobs and butt now?"
    MC @smile "I wouldn't know, my lady."
    LADY_TARBECK @smile "All well, she's gonna be a little heartbreaker I think."
    LADY_TARBECK @smile "Say, what do you think of the name Princess!"
    LADY_TARBECK @think "... No? Then how about..."
    $ PregLadyTarbeck().BabyName = renpy.input(_("... No? Then how about..."), default = _("Inyara"))
    LADY_TARBECK @smile "That's a pretty name!"
    LADY_TARBECK @smile "Alright, I better go put out little princess down for her sleepy time!"
    hide lady_tarbeck with easeoutright
    "Lady Tarbeck hurried away, bouncing the small babe playfully in her arms as she did so."
    show mc at center with ease
    SHYAHTAN "(She will make a fine mate to keep within our inner sanctum once this world is ours.)"
    MC @think "(... What did you say?)"
    SHYAHTAN "(Nothing, continue breeding her and others.)"
    $ LocEnter()


#repeat birth
#triggered auto upon entering into Tarbeck Manor main hall
label rom_tarbeck_bimbo_birth_rep:
    $ PregLadyTarbeck().ShowPostBirth_Rep = False
    show mc at cleft with easeinleft
    show lady_tarbeck at cright_f with easeinright
    "Lady Tarbeck was gleefully spinning around a small, giggling babe in her arms."
    LADY_TARBECK @smile "He's sooooo cute!"
    MC @shock "Is that-"
    LADY_TARBECK @smile "Another baby we made together of course silly!"
    "Lady Tarbeck giggled and smiled as she presented the small baby towards me, which sat their squirming and gigging to itself."
    LADY_TARBECK @smile "He's like, got your eyes!"
    "I smiled looking down at the small child as Lady Tarbeck pouted cutely."
    LADY_TARBECK @think "Soooo, I did a lot of thinking!"
    LADY_TARBECK @shock "Which as you know is REALLY hard for me!"
    LADY_TARBECK @smile "Anyway, what do you think of the name..."
    $ PregLadyTarbeck().BabyName = renpy.input(_("Anyway, what do you think of the name..."), default = _("Daynmore"))
    LADY_TARBECK @smile "Mmm! I like it!"
    LADY_TARBECK @talk "I'ma go put this little down for some sleepy time!"
    LADY_TARBECK @smile "Come by any time!"
    "Lady Tarbeck took off, happily humming to herself as I wathed her round, enticing ass sway with every motion."
    $ LocEnter()
