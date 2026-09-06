init python:
    @AppendToAllQuests
    class EventNovarasHangings(LogicModule):
        def __init__(self):
            super().__init__()

            self.nextHangingDay = -1
            self.IntervalInDays = 7  # < - how many days between each event happening
            self.ClickableLocID = LocEvent_GetFreeNovarasDistrict()
            # og list
            self.VariantsListOriginal = [1, 2, 3, 4, 5]
            # dynamic list is copied and randomzied everytime it's drained
            self.VariantsListDynamic = []
            self.SeenToday = False

        # first time is a on-enter cut-in
        def onEnter(self):  
            if GetLocID() == self.ClickableLocID:
                if IsDaytime():
                    if self.progress == 0:
                        self.progress = 1
                        self.nextHangingDay = GetGameDay() + RngInt(self.IntervalInDays - 1, self.IntervalInDays + 1)
                        return TriggeredEvent("ev_novaras_execution")

        # 1) repeat chooses a loc ID
        def onMidnight(self):
            if self.progress == 1:
                # if hanging was today, roll clickable id (for the next one) and sched. next one
                if GetGameDay() == self.nextHangingDay:
                    self.ClickableLocID = LocEvent_GetFreeNovarasDistrict()

                    self.nextHangingDay = GetGameDay() + RngInt(self.IntervalInDays - 1, self.IntervalInDays + 1)
                    self.SeenToday = False

                # if next hanging day is in the past, something broke so re-schedule it
                if self.nextHangingDay < GetGameDay():
                    self.nextHangingDay = GetGameDay() + RngInt(self.IntervalInDays - 1, self.IntervalInDays + 1)
                    self.SeenToday = False

        # 2) and displays a button at corresp loc
        def locationMod(self):
            btnMods = {}
            if self.progress == 1:
                if IsDaytime():
                    if self.nextHangingDay == GetGameDay():
                        if GetLocID() == self.ClickableLocID:
                            if self.SeenToday == False:
                                BtnID = LocIDList_NovarasCityStreets_SharedBtnIDMap[self.ClickableLocID]
                                btnMods[BtnID] = BtnJumpLabel(_("The hangings"), "ev_novaras_execution_click")
            # TEST POSITIONS
            # for locID, btn in LocIDList_NovarasCityStreets_SharedBtnIDMap.items():
            #     btnMods[btn] = BtnJumpLabel(_("The hangings"), "ev_novaras_execution_click")
            return LocButtonMod(directMods = btnMods)

label ev_novaras_execution_click:
    show mc at cleft with easeinleft
    MC "(They're doing the hangings again.)"
    MC "(Wonder who it is this time...)"
    menu:
        "Approach.":
            $ EventNovarasHangings().SeenToday = True
            hide mc with easeoutright
            jump ev_novaras_execution
        "Move on.":
            hide mc with easeoutright
            $ LocEnterQ()

label ev_novaras_execution:
    if len(EventNovarasHangings().VariantsListDynamic) == 0:
        $ EventNovarasHangings().VariantsListDynamic = EventNovarasHangings().VariantsListOriginal.copy()
        $ renpy.random.shuffle(EventNovarasHangings().VariantsListDynamic)
    $ tmpvar = EventNovarasHangings().VariantsListDynamic.pop()
    if tmpvar == 1:
        jump ev_novaras_execution_var_1
    if tmpvar == 2:
        jump ev_novaras_execution_var_2
    if tmpvar == 3:
        jump ev_novaras_execution_var_3
    if tmpvar == 4:
        jump ev_novaras_execution_var_4
    if tmpvar == 5:
        jump ev_novaras_execution_var_5

label ev_novaras_execution_var_1:
    scene cg_hanging_0 with dissolve
    GUARD "LOYAL SUBJECTS OF THE EMPEROR, YOU ARE GATHERED HERE TO WITNESS THE EXECUTION OF THOSE FOUND GUILTY OF COMMITTING CRIMES AGAINST ALDERAY!"
    "Sobbing, one of the soon to be executed cried out to the crowd, pleading for mercy."
    UNKNOWN "Please! By the gods let me go!"
    UNKNOWN "The job I was assigned doesn't pay enough! I had to find work-"
    GUARD "SILENCE SCUM!"
    GUARD "... CHARGED FOR THE CRIME OF TREACHEROUS INTENT FOR SEEKING WORK OUTSIDE OF THEIR ASSIGNED JOBS!"
    GUARD "EACH ONE IS SENTENCED TO DEATH!"
    GUARD "May the gods have pity upon your eternal souls!"
    "Before anyone else could protest, with a wave of his hand the executioner pulled the lever."
    play sound "audio/cfx/hang.ogg"
    $ AutoAmb(False)
    stop ambience fadeout 0.15
    scene cg_hanging_1 with Dissolve(0.1)
    "The doors swung open beneath their feet as the rope snapped their necks."
    "There was a brief bit of struggle in one, who's neck hadn't broken, but after a few moments of wretched squirming and choking, they stopped moving altogether."
    "The crowd clapped unenthusiastically... These executions were never as popular as some of the other."
    GUARD "SO CONCLUDES THIS WEEK'S EXECUTIONS, CONTINUE ABOUT YOUR DAY GOOD CITIZENS!"
    $ AutoAmb(True)
    $ LocEnter()

label ev_novaras_execution_var_2:
    scene cg_hanging_0 with dissolve
    GUARD "LOYAL SUBJECTS OF THE EMPEROR, YOU ARE GATHERED HERE TO WITNESS THE EXECUTION OF THOSE FOUND GUILTY OF COMMITTING CRIMES AGAINST ALDERAY!"
    "One of the bound men squirmed against the rope restraining his arms."
    UNKNOWN "FUCK YOU ALL!"
    UNKNOWN "MAY THE OLD GODS PISS ON YOUR GRAVES AS THEY DEVOUR YOUR BASTARD CHILDREN IN THEIR SLEEP!"
    play sound "audio/cfx/crowd_booing.ogg"
    "The crowd boo'd and tormented the figures on the stage, throwing what food, rocks and dirty they had on hand at the soon to be executed."
    GUARD "SILENCE SCUM!"
    GUARD "... CHARGED FOR THE CRIME OF CONSULTING WITH DARK MAGECRAFT MOST FOUL!"
    GUARD "EACH ONE IS SENTENCED TO DEATH!"
    GUARD "May the gods have pity upon your eternal souls!"
    "With a wave of his hand the executioner pulled the lever."
    play sound "audio/cfx/hang.ogg"
    $ AutoAmb(False)
    stop ambience fadeout 0.15
    scene cg_hanging_1 with Dissolve(0.1)
    "The doors swung open beneath their feet as the rope snapped their necks."
    play sound "audio/cfx/crowd_clap.ogg"
    "The crowd clapped and cheered excitedly... These executions were always some of the most popular."
    GUARD "SO CONCLUDES THIS WEEK'S EXECUTIONS, CONTINUE ABOUT YOUR DAY GOOD CITIZENS!"
    $ AutoAmb(True)
    $ LocEnter()

label ev_novaras_execution_var_3:
    scene cg_hanging_0 with dissolve
    GUARD "LOYAL SUBJECTS OF THE EMPEROR, YOU ARE GATHERED HERE TO WITNESS THE EXECUTION OF THOSE FOUND GUILTY OF COMMITTING CRIMES AGAINST ALDERAY!"
    "One of the bound men squirmed against the rope restraining his arms."
    GUARD "... CHARGED FOR ATTEMPTING TO CORRUPT AND ASSAULT A MAGE OF PALAM!"
    play sound "audio/cfx/crowd_booing.ogg"
    "The crowd boo'd and tormented the figures on the stage, throwing what food, rocks and dirty they had on hand at the soon to be executed."
    UNKNOWN "LIES! ALL LIES!"
    UNKNOWN "SHE THREW HERSELF AT US! ASK HER YOURSELF! ASK WHY HER TESTIMONY WAS DISCARDED AT OUR TRIAL YOU-"
    GUARD "SILENCE!"
    GUARD "YOU WRETCHES HAD YOUR TRIAL AND WERE FOUND GUILTY!"
    GUARD "{i}Now you loathsome beasts attempt to apply a mage of Palam would throw herself so low as to fornicate with you?{/i}"
    GUARD "EACH ONE IS SENTENCED TO DEATH!"
    GUARD "May the gods have pity upon your eternal souls!"
    "With a wave of his hand the executioner pulled the lever."
    play sound "audio/cfx/hang.ogg"
    $ AutoAmb(False)
    stop ambience fadeout 0.15
    scene cg_hanging_1 with Dissolve(0.1)
    "The doors swung open beneath their feet as the rope snapped their necks."
    play sound "audio/cfx/crowd_clap.ogg"
    "The crowd clapped and cheered. but quickly began to disperse, muttering privately amongst themselves about the case no doubt."
    GUARD "SO CONCLUDES THIS WEEK'S EXECUTIONS, CONTINUE ABOUT YOUR DAY GOOD CITIZENS!"
    $ AutoAmb(True)
    $ LocEnter()

label ev_novaras_execution_var_4:
    scene cg_hanging_0 with dissolve
    GUARD "LOYAL SUBJECTS OF THE EMPEROR, YOU ARE GATHERED HERE TO WITNESS THE EXECUTION OF THOSE FOUND GUILTY OF COMMITTING CRIMES AGAINST ALDERAY!"
    "One of the sobbing men pleaded, his voice soft but breaking as he spoke."
    UNKNOWN "I - I've done nothing wrong!"
    UNKNOWN "All I did was fall in love!"
    GUARD "THAT IS FOR WHATEVER GOD WILL LISTEN TO YOUR CRIES TO DECIDE!"
    GUARD "... CHARGED FOR THE CRIME OF SODOMY, EACH STANDS SENTENCED TO DEATH!"
    play sound "audio/cfx/crowd_booing.ogg"
    "Some of the crowd booed, throwing rocks, food and whatever else they could find at those soon to be hung."
    "...But noticeable, more than a few silent figures quietly slumped away, their faces hidden beneath their hoods."
    GUARD "May the gods have pity upon your eternal souls!"
    "With a wave of his hand the executioner pulled the lever."
    play sound "audio/cfx/hang.ogg"
    $ AutoAmb(False)
    stop ambience fadeout 0.15
    scene cg_hanging_1 with Dissolve(0.1)
    "The doors swung open beneath their feet as the rope snapped their necks."
    play sound "audio/cfx/crowd_clap.ogg"
    "Those who remained to watch, clapped and cheered enthusiastically."
    GUARD "SO CONCLUDES THIS WEEK'S EXECUTIONS, CONTINUE ABOUT YOUR DAY GOOD CITIZENS!"
    $ AutoAmb(True)
    $ LocEnter()

label ev_novaras_execution_var_5:
    scene cg_hanging_0 with dissolve
    GUARD "LOYAL SUBJECTS OF THE EMPEROR, YOU ARE GATHERED HERE TO WITNESS THE EXECUTION OF THOSE FOUND GUILTY OF COMMITTING CRIMES AGAINST ALDERAY!"
    UNKNOWN "...Haha... HAHAHAHA!"
    UNKNOWN "If you people could see what I've seen.."
    UNKNOWN "{i}None of you would blame any of us for leaving.{/i}"
    GUARD "... CHARGED FOR THE CRIME OF DESERTION, THESE SCOUTS BRING SHAME UPON ALL OF US!"
    GUARD "EACH STANDS SENTENCED TO DEATH!"
    play sound "audio/cfx/crowd_booing.ogg"
    "Despite some grumbles amongst the crowd, all who must have known just how horrifying the scouts could be, still chose to boo and jeer at those soon be hung."
    "{i}After all... If those men didn't go out and fight, their sons and daughters might have to.{/i}"
    "And better some nameless scout died in a field somewhere torn apart by a Demorai than someone they knew."
    GUARD "May the gods have pity upon your eternal souls!"
    "With a wave of his hand the executioner pulled the lever."
    play sound "audio/cfx/hang.ogg"
    $ AutoAmb(False)
    stop ambience fadeout 0.15
    scene cg_hanging_1 with Dissolve(0.1)
    "The doors swung open beneath their feet as the rope snapped their necks."
    play sound "audio/cfx/crowd_clap.ogg"
    "The crowd clapped, but it seemed to be more out of necessity rather than anything else."
    GUARD "SO CONCLUDES THIS WEEKS EXECUTIONS, CONTINUE ABOUT YOUR DAY GOOD CITIZENS!"
    $ AutoAmb(True)
    $ LocEnter()
