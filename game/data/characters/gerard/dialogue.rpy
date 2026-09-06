init python:
    @AppendToAllQuests
    class DialogueGerard(LogicModule):
        def __init__(self):
            super().__init__()

            # progress: 0 firstmeet, 1 all else
            self.isPresent = None # flips back and forth, starts to work after firstmeet
            

        def onMidnight(self):
            if self.isPresent:
                self.isPresent = False
            else:
                self.isPresent = True

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "adara_house_living_room":
                if self.isPresent == True:
                    if IsDaytime():
                        btnMods["btn_talk_gerard"] = BtnJumpLabel(_("Talk to Gerard"), "gerard_talk")
            return LocButtonMod(directMods = btnMods)
    
        def onEnter(self):  
            if GetLocID() == "adara_house_living_room":
                if self.progress == 0:
                    return TriggeredEvent("gerard_firstmeet")

label gerard_talk:
    show gerard at center_f with dissolve
    GERARD @happy "Ah! There you are."
    GERARD @happy "Could you be a good lad and ask Adara when my soup will be ready?"
    GERARD "I'm starting to feel quite ... {i}quite tired{/i} again..."
    MC @talk "...Gerard?"
    show gerard sleep at center_f
    GERARD "..."
    MC "(Seems he's gone to sleep again.)"
    $ LocEnter()

label gerard_firstmeet:
    $ QstSetProgress(DialogueGerard, 1)
    $ DialogueGerard().isPresent = True
    show gerard at cleft
    with dissolve
    "Upon seeing me, Gerard, Adara's father withdrew further into his seat."
    show mc at right_f with easeinright
    GERARD @shock "Who... Who are you?"
    GERARD @angry "What are you doing in my home?"
    MC @surprised "Gerard, it's me! It's [player_name!t]!"
    "Gerard's eyes wandered over me from top to bottom, as though unconvinced."
    "Then, when the realization hit, he smiled brightly."
    GERARD @happy "Ah! [player_name!t]! It's good to see you!"
    MC @smile "Hello. Gerard, how do you fair?"
    "Adara's father coughed and spluttered before offering a faint, sickly smile."
    GERARD @happy "I struggle to move around much these days, but I keep going all the same."
    GERARD @shock "By the gods though, you've changed!"
    MC @smile "Ah, well, a lot's happened since you last saw me..."
    "Adara emerged from the upstairs, calling out to her father."
    show adara at left with easeinleft
    ADARA @talk "Father, I've prepared your bed for-"
    "Adara's eyes widened when she saw me."
    ADARA @shock "[player_name!t]!"
    $ CharSetVar("adara", "blush", True)
    ADARA "W-What are you doing here?"
    GERARD "Yes, that is a good question..."
    GERARD "What brings you here, [player_name!t]?"
    MC @lewd "Ah, I actually came to see how Adara was doing..."
    "Adara's cheeks burned red as her father looked back and forth from me to her."
    ADARA "Y-You don't need to trouble yourself worrying about me."
    "Gerard smiled and nodded."
    GERARD @happy "Well, you're welcome in our home anytime, [player_name!t]."
    GERARD @happy "Now when are you going to make an honest woman of my daughter?"
    "Adara's eyes widened in horror."
    ADARA @shock "FATHER!"
    MC @surprised "U-Uhh...!"
    "Gerard laughed, and that laugh soon turned into another cough and splutter."
    GERARD @happy "What? You two have known each other since you were small, I always {i}presumed{/i} it was coming one day."
    ADARA "W-We're just friends, that's all."
    GERARD "Friends, hm?"
    GERARD "Me and your mother used to say the same-"
    $ CharSetVar("adara", "blush", False)
    "Adara's father began to cough and splutter once again, the persistent cough this time refusing to let up."
    "Adara gave Gerard some water and gently rubbed his back."
    GERARD "Urghh ... I need some more rest it seems."
    GERARD "Adara, tend to our ... our ..."
    "Gerard seemed to doze off."
    show gerard sleep
    ADARA @sad "{i}*Sigh*{/i}"
    MC @sad "Has his condition shown no sign of improving?"
    ADARA @sad "His health seems to be improving slowly."
    ADARA @sad "{i}Very slowly.{/i}"
    MC @talk "I see..."
    show adara at cright with easeinleft
    ADARA @sad "Just let father rest for now, come ... I'll be in my room should you need me for anything."
    $ LocEnter()