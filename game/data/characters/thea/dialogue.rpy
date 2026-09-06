init python:
    @AppendToAllQuests
    class DialogueThea(LogicModule):
        def __init__(self):
            super().__init__()

            self.askedOut = False
            self.isAdventurer = False

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_adv_guild":
                if IsDaytime():
                    btnMods["btn_thea_talk"] = BtnJumpLabel(_("Talk to Thea"), "nov_thea_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("thea_root",DNode(_("I should go."), "nov_thea_bye", nextNode = "DNodeExit", order = -100))
            if self.isAdventurer:
                yield ("thea_root", DNode(_("I have some questions about adventuring..."), "nov_thea_adv_questions"))
                if not QstIsActive(RomanceThea):
                    yield ("thea_root", DNode(_("So, how about a drink later after you finish work?"), "nov_thea_drink"))
            else:
                yield ("thea_root", DNode(_("I have some questions about adventuring..."), "nov_thea_adv_questions_notAdventurer"))

label nov_thea_talk:
    show thea at center with dissolve
    THEA @smile "Oh hey! Can I help you with something?"
    call processDialogue("thea_root") from _call_processDialogue_41
    $ LocEnter()

label nov_thea_bye:
    THEA @talk "Alright, see ya around!"
    THEA @smile "Good luck on your adventures!"
    $ LocEnter()

label nov_thea_adv_questions:
    THEA @talk "Ask away."
    menu nov_thea_adv_questions_menu:
        'How do I sign up to an Adventure?':
            THEA @talk "Over on the board over there is our list of current jobs needing to be done."
            THEA @talk "Just select the one you want, and we'll handle the paperwork while you get to work."
            THEA @talk "Remember though, you can only choose a quest within your rank as an adventurer."
            jump nov_thea_adv_questions_menu
        'How does the guild work?':
            THEA @talk "It's important to understand how the ranking works."
            THEA @talk "All beginner adventurers are ranked as D-listers."
            THEA @talk "These are the most straightforward and simple quests available to any adventurer."
            THEA @talk "Ranking progresses from D-tier all the way to S-Tier, the rank of legendary adventurers."
            THEA @talk "Of course, as the danger and difficulty of the quests increase each rank, so does the rewards to compensate."
            jump nov_thea_adv_questions_menu
        'How do I move up the guild ranks?':
            THEA @talk "There's a set number of quests per rank that will need to be completed a minimum of at least once."
            THEA @talk "After you've beaten your ranks guild quests, a special one-time quest will open up that once you've completed, your rank will increase."
            THEA @talk "Oh ... And don't worry about running out of quests."
            THEA @talk "Outside of the special guild quests, most guild quests are usually full time occupations in themselves, you'll be able to re-do those quests as many times as you like."
            jump nov_thea_adv_questions_menu
        "I'm done with my questions.":
            THEA @talk "Sure, was there anything else?"
            return

label nov_thea_adv_questions_notAdventurer:
    THEA @talk "Sorry, but I don't remember you being an adventurer."
    MC "What do you mean?"
    THEA @talk "Well, you can get yourself a drink or something, but I can't waste my time explaining the inner workings of the guild to you."
    MC "Can I become an adventurer?"
    "Thea let out a quiet sigh..."
    THEA @talk "That's a three-hundred fifty-something time I've been asked this."
    THEA @talk "Have you reached your Terminus yet?"
    "I swallowed hard."
    MC "Y-yeah."
    THEA @talk "You did? Well, that is how you become an adventurer, you're {i}assigned{/i} this role at your Terminus."
    THEA @talk "What role did the kingdom bestow upon you?"
    MC "(Cannon fodder.)"
    MC "I... I should go."
    "Thea raised an eyebrow."
    THEA @talk "Okay, safe travels then!"
    $ LocFlush(dissolve)
    MC "I should get to the fort now."
    $ LocEnterQ()

label nov_thea_drink:
    if DialogueThea().askedOut:
        THEA @talk "Improve your standing at the guild and maybe we'll talk."
        return
    else:
        $ DialogueThea().askedOut = True
        THEA @smile "I hope you don't think you're the first one to try that."
        MC @smile "I was hoping I'd be the first one you'd say yes to."
        THEA @talk "Hmm, well, I'll think about it ..."
        THEA @talk "I'm sure you're used to girls just falling into your lap, but it takes a little more than that to get me interested."
        MC @smile "Oh?"
        THEA @smile "{i}I wanna see what you can do.{/i}"
        MC @think "What I can do?"
        THEA @smile "Here, {i}at this guild.{/i}"
        THEA @smile2 "There's something about this place that just-"
        THEA @smile "Mmm ... Better not think too hard on it, need to stay focused for work."
        MC @talk "So, you've got a thing for Adventurers then?"
        THEA @smile2 "A-Ah...Maybe a little?"
        THEA @smile "But not just any adventurer walking in off the street, one whose metal has been seriously proven."
        THEA @blush "Think you've got what it takes?"
        MC @talk "I guess we'll see, won't we?"
        return