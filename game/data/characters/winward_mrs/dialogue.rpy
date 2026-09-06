init python:
    notesLib["winward_leather_standby"] = Note(
        _("Leather to pick up"), 
        _("I've commissioned Mrs. Winward of Novaras tannery to process some animal hides into leather. I should pick it up in about a week."),
        journal_flag_delayed = True)

    notesLib["winward_leather_bring"] = Note(
        _("Tanner's shop needs animal hides"), 
        _("If I gather animal hides during my travels, I can bring them to Mrs Winward, a leatherworker lady at the tanner's shop in Novaras. She can process these hides into usable leather."),
        journal_flag_persistent = True)

    @AppendToAllQuests
    class DialogueMrsWinward(LogicModule):
        def __init__(self):
            super().__init__()

            self.LeatherSchedule = [] # will store [[amount,days], [amount,days]]
            self.LeatherToGiveToPlayer = 0
            self.HidesBroughtIn = 0 # for scene triggers
            self.SeenHidesBroughtScene = False

        def onEnter(self):  
            if GetLocID() == "novaras_tanner_shop":
                if self.progress == 0:
                    return TriggeredEvent("nov_mrs_winward_firstmeet")
                elif not self.SeenHidesBroughtScene:
                    if self.HidesBroughtIn >= 6:
                        return TriggeredEvent("nov_mrs_winward_brought_hides", priority = 1)

        def onMidnight(self):
            NewList = []
            for LeatherEntry in self.LeatherSchedule:
                if LeatherEntry[1] > 0:
                    LeatherEntry[1] -= 1
                if LeatherEntry[1] == 0:
                    self.LeatherToGiveToPlayer += LeatherEntry[0]
                else:
                    NewList.append(LeatherEntry)
            self.LeatherSchedule = NewList
            return

        def OrderLeather(self, Amount):
            self.HidesBroughtIn += Amount
            self.LeatherSchedule.append([Amount, 7])
            NoteUnlock("winward_leather_standby")
            return

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_tanner_shop":
                if IsDaytime():
                    btnMods["btn_talk_mrs_winward"] = BtnJumpLabel(_("Talk to Mrs. Winward"), "nov_mrs_winward_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            if PlayerItemQty("animal_hide") > 0:
                yield ("mrs_winward_root", DNode(_("Could you make me some leather from these hides?"), "nov_mrs_winward_make_leather"))

            yield ("mrs_winward_root", DNode(_("Can you please explain what it is that you do again?"), "nov_mrs_winward_explain"))

            yield ("mrs_winward_root", DNode(_("Tell me a little more about yourself, Mrs Winward."), "nov_mrs_winward_about"))
            yield ("mrs_winward_root", DNode(_("That's all, Mrs. Winward."), "nov_mrs_winward_bye", nextNode = "DNodeExit", order = -100))


label nov_mrs_winward_explain:
    MRS_WINWARD @happy "Why of course, deary!"
    MRS_WINWARD @happy "I work on animal hides, turning them into leather."
    MRS_WINWARD @happy "The procedure is called tanning, and it involves..."
    scene black with dissolve
    $ Pause(1.0)
    $ LocFlush()
    show mrs_winward at center_f 
    with dissolve
    MRS_WINWARD @happy "...So just like that, if you bring me some animal hides, I can produce some fine leather for you!"
    MRS_WINWARD "Deary?"
    MRS_WINWARD "Is there anything else you want to know?"
    MC @smile "What? Ah, right... Let's see..."
    return

label nov_mrs_winward_talk:
    show mrs_winward at center_f with dissolve
    MRS_WINWARD @happy "Yes, deary?"
    call processDialogue("mrs_winward_root") from _call_processDialogue_50
    $ LocEnter()

label nov_mrs_winward_make_leather:
    MRS_WINWARD @happy "Why, of course!"
    MRS_WINWARD @happy "But I can only take so many from you at once... How many do you have?"
    menu:
        "One." if PlayerItemQty("animal_hide") > 0:
            $ PlayerRemItem("animal_hide")
            $ DialogueMrsWinward().OrderLeather(1)
            MRS_WINWARD @happy "Very good, I'll take that off your hands."
            MRS_WINWARD  "Come back next week, and I'll have it ready for you!"
        "Two." if PlayerItemQty("animal_hide") > 1:
            $ PlayerRemItem("animal_hide", 2)
            $ DialogueMrsWinward().OrderLeather(2)
            MRS_WINWARD @happy "Mhmm, lovely! I'll take those off your hands."
            MRS_WINWARD  "Come back next week, and I'll have those ready for you!"
        "Three." if PlayerItemQty("animal_hide") > 2:
            $ PlayerRemItem("animal_hide", 3)
            $ DialogueMrsWinward().OrderLeather(3)
            MRS_WINWARD @happy "Oh my! How wonderful! I'll take those off your hands."
            MRS_WINWARD  "It might be a little tight with so many, but come back next week, and I'll have those ready for you!"
        "Ah, on second thought...":
            MRS_WINWARD  "Let me know when you have something, deary."
    return

label nov_mrs_winward_about:
    MRS_WINWARD @shock "{i}Me?{/i}"
    MRS_WINWARD @happy "Oh my... What do you want to know?"
    menu:
        "How long have you lived in Novaras?":
            MRS_WINWARD @think "Hmmm? How long?"
            MRS_WINWARD @think "We used to live in Gerano before the war forced us to pack up and leave."
            MRS_WINWARD  "Been living in Novaras ever since."
            MC @surprised "You're a southerner?"
            MRS_WINWARD  "{i}Was.{/i}"
            MRS_WINWARD  "Things were better back then. My husband was happier, and the business was doing very well."
            MRS_WINWARD @sad "Now... We get by, but...things are a lot harder."
            MC  "I heard Gerano was surrounded and-"
            MRS_WINWARD @sad "Yes, well, when we heard the news Newheart was dead, we knew it wouldn't be long till they reached Gerano."
            MRS_WINWARD  "So, we packed what we could by wagon and headed straight for Novaras."
            MRS_WINWARD  "Others were even too stubborn to leave or weren't so lucky."
            "Mrs Winward's eyes darkened."
            MRS_WINWARD @sad "My... Those were terrible, {i}terrible{/i} days."
            "She shook her head and forced a smile."
            MRS_WINWARD @happy "Anyway, was that all you wanted to ask?"
        "How long have you been married?": 
            MRS_WINWARD @shock "How long?"
            MRS_WINWARD @happy "Well, I'm sixty-one now and I was married when I came of age sooo..."
            MRS_WINWARD @happy "Forty-three years!"
            MC @smile "Wow, that's a long time to be married!"
            MRS_WINWARD  "Yes... {b}Yes it is.{/b}"
            MC @think "No children?"
            MRS_WINWARD  "Ahh, we have a son and daughter."
            MRS_WINWARD  "But they were sent to work as tanners in Angmurus."
            MRS_WINWARD @think "The thing about having a family trade under the current rules is you might just find yourself sent who knows where."
        "That's all.":
            MRS_WINWARD  "Very well, is there anything else?" #Loops back to main menu 
    return

label nov_mrs_winward_bye:
    MRS_WINWARD @happy "Ah, just let me know if you need anything else, deary!"
    ###Line occurs when Mrs. Winward has the leather player ordered ready - Add leather to inventory
    if DialogueMrsWinward().LeatherToGiveToPlayer > 0:
        MRS_WINWARD @happy "Ah! The leather you ordered is ready; here you go..." #X amount of leather added to inventory (1, 2 or 3)
        $ PlayerAddItem("leather", DialogueMrsWinward().LeatherToGiveToPlayer)
        $ DialogueMrsWinward().LeatherToGiveToPlayer = 0
        if len(DialogueMrsWinward().LeatherSchedule) == 0:
            $ NoteLock("winward_leather_standby")
    return

label nov_mrs_winward_firstmeet:
    $ QstSetProgress(DialogueMrsWinward, 1)
    show mc at left with easeinleft
    MC "(Hmm... Looks like a tanners workplace.)"
    show mrs_winward at right_f with easeinright
    TANNER_LADY @happy "Ahh! Welcome, young man!"
    TANNER_LADY @happy "What brings you to my humble store?"
    MC  "I was just looking around a moment."
    TANNER_LADY @happy "Ahh, are you looking for something in particular?"
    TANNER_LADY @happy "Bags, gloves, tool straps."
    "The woman raised her brow."
    TANNER_LADY @lewd "{i}...A new blade sheath? {/i}"
    MC @smile "Perhaps... What's your name, Tanner?"
    TANNER_LADY @shock "Oh good gods! You'll have to forgive my manners!"
    TANNER_LADY @happy "My name's Kionni dear, but you can call me Mrs Winward."
    MC  "Mrs Winward... I'm [player_name!t]."
    $ CharMeet("mrs_winward")
    MRS_WINWARD @happy "Ahhh! You must be that young man everyone's talking about!"
    MRS_WINWARD @happy "The one they found outside the city walls!"
    MRS_WINWARD @sad "Terrible business, all that."
    MRS_WINWARD  "But at least you're-"
    show mrs_winward at cright_f with easeinright
    show mr_winward at right_f with easeinright
    MR_WINWARD  "Honey! Who is that?"
    MRS_WINWARD @think "Urghh... Excuse me one moment."
    show mrs_winward at blurin, cright
    MRS_WINWARD @angry "What is it dear?"
    MR_WINWARD @angry "Where's my food, woman?"
    MR_WINWARD @angry "I'm starving here!"
    show mrs_winward at shake
    MRS_WINWARD @angry "I GAVE YOU SOME COIN TO GRAB SOME FOOD AT THE IRON UNICORN!"
    MRS_WINWARD @think "I have a busy day here, remember?"
    MR_WINWARD @angry "BAH! Fine!"
    show mr_winward at blurin, right
    hide mr_winward with easeoutright
    "The old man glared at me as he wandered by, slamming the door behind him." 
    play sound "audio/interactables/wooden_door_open_3.ogg"
    $ CharMeet("mr_winward")
    MC @think "What was his problem?"
    show mrs_winward at blurin, cright_f
    MRS_WINWARD @sad "A-Ah, never mind my husband."
    MRS_WINWARD @happy "He's always like that! He'll be fine later!"
    MC  "I see..."
    MRS_WINWARD @happy "I'll let you look around in peace."
    MRS_WINWARD  "Just call and let me know if I can help with anything."
    MC  "Thank you."
    hide mrs_winward with dissolve
    show mc at center with easeinleft
    MC "(If I could get her to convert some animal hide into leather for me, I could either sell on the item or use it to help fashion some new equipment for myself.)"
    $ NoteUnlock("winward_leather_bring")
    $ LocEnter()

label nov_mrs_winward_brought_hides:
    $ DialogueMrsWinward().SeenHidesBroughtScene = True
    show mrs_winward at cright_f with dissolve
    MRS_WINWARD @happy "My! You've been busy, haven't you?"
    show mc at cleft with easeinleft
    MC @smile "Mrs Winward."
    MRS_WINWARD  "Any more hides for me?"
    "As she spoke, Mrs. Winward seemed unusually different today."
    "She brushed her hair over her shoulder and seemed moving closer to me than usual..."
    MC  "I'll have some more hides soon, as usual."
    MRS_WINWARD @blush "I hope you're looking after yourself while out there!"
    MRS_WINWARD @lewd "{i}It would Be an awful shame if something happened to such a nice, young, good-looking man like you. {/i}"
    "Was that a new perfume she was wearing?" 
    "Soft and like violet, the fragrance was new and expensive."
    "No doubt an old bottle she kept for special occasions."
    "As she spoke, she squished her breasts together, clasping her hands beneath."
    MRS_WINWARD @lewd "{i}I bet you have dozens of women chasing after you, don't you?{/i}"
    MC @think "...Mrs Winward, are you-"
    MRS_WINWARD @shock "Oh! I forgot, would you like something to eat deary?"
    MRS_WINWARD @blush "I could make you some nice soup or..."
    MC @smile "No, thank you, Mrs Winward."
    MRS_WINWARD @blush "Are your shoulders tight? They look tight, why don't you let me-"
    MR_WINWARD @laugh "HAHAHAHAHA!"
    show mr_winward at right_f with easeinright
    MRS_WINWARD @shock "D-Darling! I was just-"
    MR_WINWARD  "Fawning over this young man pathetically, yes, I do see."
    MR_WINWARD  "You think he'd be interested in a weathered old pair of boots like you?"
    MRS_WINWARD @angry "You... YOU...!"
    show mrs_winward at shake
    MRS_WINWARD @angry "YOU INSUFFERABLE FUCKING PRICK!"
    MR_WINWARD @laugh "Hehehe! See this lad? This here is why men don't get married."
    MR_WINWARD @happy "A pretty face one day, a tired moaning one the next!"
    MRS_WINWARD @angry "And a once loving husband becomes a bitter old prick who can't even get it up anymore!"
    MR_WINWARD @angry "As if anyone could get it up for you!"
    menu:
        "THAT'S ENOUGH!":
            MRS_WINWARD @shock "...!"
            MR_WINWARD @angry "Who in the hells are you to speak to me like that in my own home?"
            MRS_WINWARD @sad "Dear, that's enough... just... {i}leave{/i} already!"
            MR_WINWARD @angry "Hmph! Fine!"

        "I don't know; something of mine is certainly 'getting up' for her.":
            MRS_WINWARD @shock "Y-You...!"
            MRS_WINWARD @lewd "{i}...O-Oh my!{/i}"
            MR_WINWARD @angry "He's just trying to make you feel better! Don't be ridiculous!"
            "Mr Winward glared towards me."
            MR_WINWARD @angry "I don't know what sick game you're up to telling her that, but-"
            MRS_WINWARD @angry "Please... Just... Just stop and go already!"
            MRS_WINWARD @sad "You've said enough..."
            MR_WINWARD @angry "Hmph!"

    MR_WINWARD @angry "I'm going to the {i}Iron Unicorn,{/i} at least there I can get some FOOD!"
    hide mr_winward with easeoutleft
    "As Mr Winward slammed the door shut behind him, Mrs Winward burst into tears."
    MRS_WINWARD @cry "Oh gods, I'm so embarrassed."
    show mc at center with easeinleft
    MC @sad "Mrs Winward..."
    MRS_WINWARD @cry "I-Im sorry, it's shameful for a woman to be acting like that at my age."
    MC @think "Why does he treat you like that?"
    MRS_WINWARD @cry "He's just resentful. Ever since we had to move to Novaras, he's been like that."
    MRS_WINWARD @cry "He blames everyone and everything for Gerano's fall... Including me, it seems."
    MRS_WINWARD @cry "He just can't seem to accept our family name, which isn't prestigious anymore since we left behind so much."
    MC @think "I understand you fled, but... surely you could rebuild on your good name if it was that prestigious?"
    MRS_WINWARD @cry "{i}We're trying!{/i}"
    MRS_WINWARD @cry "But the equipment, our investments... so much we couldn't take with us."
    MRS_WINWARD @cry "Many of the staff we spent years training to assist us either fled elsewhere or stayed in Gerano till the very end."
    MRS_WINWARD @cry "There's competition everywhere now; it's even harder to start up from scratch, and we're certainly not as young as we were then!"
    MRS_WINWARD @cry "When our prestigious clients found we could no longer meet demand like we used to, well, they went elsewhere."
    MC "Surely you must have bought some coin for you?"
    MRS_WINWARD @sad "{i}*Sniff*{/i} We did, but the costs of the mercenaries to get us to Novaras safely, this shop we were forced to buy..."
    MRS_WINWARD @sad "Prices of everything surged back then. People believed Novaras would be the last stronghold to hold out, and plenty were willing to take advantage of that."
    MRS_WINWARD @sad "What coin was left just slowly dwindled."
    MC @sad "Hmm... I see."
    MRS_WINWARD @sad "Since then, he's been the miserable prick you've just seen."
    MRS_WINWARD @sad "He's resentful about everything."
    MC @think "So, I take you two aren't..."
    MC "{i}Anymore?{/i}"
    "There was a long pause, and when the realization dawned on her, she blushed, deeply embarrassed."
    MRS_WINWARD @shock "N-No... He might try something when he's beyond drunk, but that's it!"
    MRS_WINWARD @embarr "I'm ... I'm sorry for my shameful display earlier."
    MRS_WINWARD @embarr "A married woman my age shouldn't be trying to get attention from a young man like you..."
    menu:
        "{image=[ICON.HEART]} I was rather enjoying the attention...":
            $ CharSetLover("mrs_winward")
            MRS_WINWARD @shock "You...What?"
            MC @smile "Is it that hard to believe?"
            MRS_WINWARD @embarr "But ... I... You can't seriously be interested in an old lady like me!"
            MRS_WINWARD @embarr "Y-You're a young man, you probably have no end of women interested in you, haha..."
            MC @smile "Then it's a good thing I can like more than one type of woman, isn't it?"
            "As I stepped closer towards her, Mrs Winward nervously stepped back, pushing herself up against the counter."
            MRS_WINWARD @shock "W-What are you doing? Deary?"
            "Mrs Winward gasped as she felt my lips press against her."
            hide mc
            hide mrs_winward
            show cg_winward_kiss at center 
            with dissolve
            "As my tongue slipped into her mouth and entwined with hers, she froze nervously at first, but then, sensing this wasn't some cruel trick, allowed herself to sink into the kiss."
            "My hands clambered over her body, squeezing at her large hanging breasts and soft, round ass."
            "When I released her from my grip, she stared breathlessly towards me."
            "Gently, I cupped her cheek before moving my hand down her dress."
            "She softly cooed as I cupped at her bare, naked breasts, pulling them out over the top of her dress."
            MRS_WINWARD @embarr "D-Deary..."
            MRS_WINWARD @embarr "{i}*Huff*{/i} P-Please..."
            MRS_WINWARD @embarr "W-We cannot - Mhmm... D-Do this..."
            MRS_WINWARD @embarr "I'm -"
            MRS_WINWARD @shock "Oooh...!"
            hide cg_winward_kiss
            show mc at cleft
            show mrs_winward at cright_f
            with dissolve
            "Reluctantly, I pulled my hand back, and very sheepishly, Mrs Winward pulled her breasts back into her dress."
            MRS_WINWARD @blush "P-Please, let's just return to focusing on business."
            MRS_WINWARD @lewd "T-This is all too much excitement for these old bones! Haha!"
            "Mrs Winward laughed awkwardly, but it was clear she was struggling to stay focused after what happened."
            "Regardless, I decided it was a good idea not to push my luck too far... yet."
            $ QstStart(RomanceWinward)

        "{image=[ICON.HEART_CROSS]} I understand, but I would appreciate not being dragged into your marital issues.":
            MRS_WINWARD @embarr 'Y-Yes, I understand.'
            MRS_WINWARD @embarr "I promise it won't happen again."     
            "Wiping her tears away, Mrs Winward did her best to smile and reverted to her usual self."
            MRS_WINWARD @embarr "{i}*Sniff*{/i} C-Come back later, deary, I'll help you with whatever then."
            MC  "As you wish."

    MRS_WINWARD  "{i}*Cough*{/i} Now, h-how can I help?" #Loops back to usual default menus and things 
    call processDialogue("mrs_winward_root") from _call_processDialogue_51
    $ LocEnter()