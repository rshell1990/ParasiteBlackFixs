init python:
    @AppendToAllQuests
    class DialogueArwen(LogicModule):
        def __init__(self):
            super().__init__()

            self.celesteCooldown = 4
            self.celesteCosplay = False
            self.firstSex = True
            self.firstAnal = True
            self.firstBJ = True

        def onNoon(self):
            if self.progress > 0:
                self.celesteCosplay = False
                self.celesteCooldown -= 1
                CharSetClothes("arwen", "normal")
                if self.celesteCooldown == 0:
                    self.celesteCooldown = 4
                    self.celesteCosplay = True
                    CharSetClothes("arwen", "celeste")

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_bordello_interior":
                if self.progress == 0:
                    btnMods["btn_talk_arwen"] = BtnJumpLabel(_("Talk to Arwen"), "arwen_talk_firstmeet")
                else:
                    if self.celesteCosplay:
                        btnMods["btn_talk_arwen"] = BtnJumpLabel(_("Talk to Arwen"), "arwen_talk_celeste")
                    else:
                        btnMods["btn_talk_arwen"] = BtnJumpLabel(_("Talk to Arwen"), "arwen_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("arwen_root",     DNode(_("What do you think of the other girls who work here?"), "dialogue_arwen_othergirls"))
            yield ("arwen_root",     DNode(_("What kind of services do you offer?"), "dialogue_arwen_services")) # <-down in world_romance/arwen
            yield ("arwen_root",     DNode(_("Not tonight."), "arwen_bye", nextNode = "DNodeExit", order = -100))

            # as celeste cosplayin
            yield ("arwen_root_cel", DNode(_("Why are you dressed up like Celeste?"),"arwen_whyCeleste"))
            yield ("arwen_root_cel", DNode(_("Another time perhaps."), "arwen_bye_cel", nextNode = "DNodeExit", order = -100))
            yield ("arwen_root_cel", DNode(_("How much?"), "dialogue_arwen_services_cel")) # <-down in world_romance/arwen


label arwen_talk_firstmeet:
    show arwen at center_f with dissolve
    ARWEN @talk "Ooh! You're new!"
    MC @smile 'Do you have a name?'
    ARWEN @talk 'Arwen, a pleasure to make your acquaintance.'
    $ CharMeet("arwen")
    ARWEN @talk 'And what may I call you?'
    MC @talk '[player_name!t].'
    ARWEN @talk "Well, doesn't that just roll off the tongue?"
    ARWEN @talk 'Sooo, are you interested in a little {i}entertainment{/i} this Evening?'
    $ QstSetProgress(DialogueArwen, 1)
    call processDialogue("arwen_root") from _call_processDialogue_35
    $ LocEnter()

label arwen_talk:
    show arwen at center_f with dissolve
    MC @talk "Hey there, Arwen."
    ARWEN @talk "Hello, [player_name!t]."
    ARWEN @talk "Looking for {i}entertainment?{/i}"
    call processDialogue("arwen_root") from _call_processDialogue_36
    $ LocEnter()

label arwen_bye:
    ARWEN @talk "Hmm, shame."
    ARWEN @talk "Maybe next time though, hmm?"
    $ LocEnter()

########################################## CELESTE COSPLAY VERSION
label arwen_talk_celeste:
    show arwen at center_f with dissolve
    MC @talk "Hey Arwen."
    ARWEN @talk 'Why hello there brave adventurer!'
    ARWEN @talk 'Tell me, {i}how much coin would you pay to spend a night with the beautiful Celeste?{/i}'
    ARWEN @talk "Actually, don't even answer that!"
    ARWEN @talk 'We both know that such priceless things would be worth their weight in gold... {i}till now.{/i}'
    call processDialogue("arwen_root_cel") from _call_processDialogue_37
    $ LocEnter()

label arwen_bye_cel:
    ARWEN @talk 'Very well.'
    $ LocEnter()

label arwen_whyCeleste:
    ARWEN @laugh "Because... {i}Who doesn't want to fuck the most beautiful, famous heroine around?{/i}"
    ARWEN @talk "People will pay whatever I ask if they think they'll get at least a taste of what it might be like to have her."
    ARWEN @talk 'Fantasy is a powerful thing... The reality of something rarely meets the expectation.'
    MC @talk 'Very insightful of you.'
    ARWEN @laugh 'I try.'
    return

label dialogue_arwen_services_cel:
    ARWEN @talk "Fifteen hundred coins and {i}Celeste{/i} is all yours."
    MC @talk "That's more than your normal rates..."
    ARWEN @angry 'Do you know how much this outfit cost to make?'
    ARWEN @talk 'Plus all the rallies and things I had to attend to learn to act like her a bit.'
    ARWEN @laugh 'Besides... I offer a {i}unique{/i} experience unlike what my clients normally get.'
    ARWEN @talk "So, fifteen hundred. Interested?"
    menu:
        'Not this time.':
            ARWEN @talk "Then if you don't mind, other customers are waiting."
            return
        'Sounds fun to me!' (Req_Gold = 1500):
            $ PlayerRemItem("gold", 1500)
            jump sexscene_ArwenCelesteChoice # <- down in world_romance/arwen
