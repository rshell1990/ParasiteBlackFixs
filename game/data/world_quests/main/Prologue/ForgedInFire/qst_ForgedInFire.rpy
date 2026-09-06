init python:
    @AppendToAllQuests
    class QstForgedInFire(BaseQuest):
        GOALS = {
            0: QuestStage(_("Get your gear from the barracks"), hintTxt = _("I must go to the barracks and get my set of Scouts Gear. Looks like this place is what I'll be calling home for... gods only know how long, so I better get used to it.")),
            1: QuestStage(_("Return to the yard"), hintTxt = _("Locked and loaded, it's time to go to the fort yard. Quartermaster Joakim mentioned some captain taking over, so I guess we'll get to swing these swords quite soon...")),
            2: QuestStage(_("Show up at the training area"), hintTxt = _("We have fallen under command of Captain Duprey, a brutal veteran warrior of the Alderay. My priorities have changed now: I am to survive {i}the training itself{/i}, not whatever they use the Scouts for.")),
            3: QuestStage(_("Go to sleep"), hintTxt = _("Exhausted and battered, I am almost through my first day at Fort Sebastian. I should now muster all of my strength to get to my bunk at the barracks...")),
            4: QuestStage(_("Keep attending the training sessions"), hintTxt = _("Under the command of Captain Duprey we are to train very hard, on our way to become real warriors.\nI must now attend daily training sessions to improve my fighting skills.")),
            5: QuestStage(_("Attend the test"), hintTxt = _("We have gone through a rather extensive training program. Captain Duprey mentioned a test of some sorts, to see if we are prepared for some more in-depth training maneuvers. We are to show up at the yard at dawn, as usual."))
            }
        TITLE = _("Forged in Fire")
        DESCRIPTION = _("Me and Markus are now members of the Scouts Corp, a reconnaissance branch of the Alderian army. I am to follow whatever the Empire demands of me and to hopefully live through it.")

        def __init__(self):
            super().__init__()

            self.XpReward = 150
            # when mc enters medward after duprey kicks a guys face in, theres some narrative going on.
            # the var turns false for a one-off
            self.ShowHeadbuttLines = True
            # at stage when mc's told to "train up", next day kiara will be outside till player sees her poison-scene once
            self.ShowKiaraWithPoisonTrinket = True
            # at "train up" stage this counter increments with each training stage player has seen and the training scenes (and night scenes) swap out accordingly
            self.TrainingProgress = 0

            self.IsMain = True

        def onEnter(self):  
            if self.progress == 0:
                if GetLocID() == "novaras_fort_seb_barracks":
                    return TriggeredEvent("qst_ForgedInFire_EnterBarracksToGetGear") 
            elif self.progress == 2:
                if GetLocID() == "novaras_fort_seb_train":
                    return TriggeredEvent("qst_ForgedInFire_AtTrainingYard")
            elif self.progress in [3, 4, 5]:
                # sleep time missed
                if IsInTimeFrame(TIME_NIGHT, TIME_DAWN):
                    return TriggeredEvent("qst_ForgedInFire_CaughtOutsideOfAllowedTime")
                # training time missed
                elif IsInTimeFrame(TIME_MORNING, TIME_LATEEVENING):
                    if self.progress != 3:
                        if GetLocID() != "novaras_fort_seb_train":
                            # guard escorts player to training event
                            return TriggeredEvent("qst_ForgedInFire_CaughtSkippingTraining")
                        else:
                            # begin training event
                            return TriggeredEvent("qst_ForgedInFire_BeginNextTrainingEvent")
            if self.ShowHeadbuttLines:
                if GetLocID() == "novaras_fort_seb_medward":
                    return TriggeredEvent("qst_ForgedInFire_EnterMedwardAfterHeadbuttLines")

        def locationMod(self):
            btnMods = {}
            btnMods["btn_novaras_fort_seb_yard_toCity"] = BtnJumpLabel(STR_NAV.TO_CITY, "qst_ForgedInFire_CantLeaveSebastian")
            if self.progress == 0:
                if GetLocID() == "novaras_fort_seb_yard":
                    btnMods["btn_novaras_fort_seb_yard_to_medward"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT_MEDWARD, "qst_ForgedInFire_CantGoToMedwardOrTrainArea")
                    btnMods["btn_novaras_fort_seb_yard_to_train"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT_TRAIN, "qst_ForgedInFire_CantGoToMedwardOrTrainArea")
            elif self.progress == 2:
                if GetLocID() == "novaras_fort_seb_barracks":
                    btnMods["btn_novaras_fort_seb_barracks_to_captain_office"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT_CAPTAIN_OFFICE, "qst_ForgedInFire_CantEnterCaptainsOffice")
            elif self.progress == 3:
                if GetLocID() == "novaras_fort_seb_barracks":
                    btnMods["btn_novaras_fort_seb_barracks_to_captain_office"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT_CAPTAIN_OFFICE, "qst_ForgedInFire_CantEnterCaptainsOffice")
                    btnMods["btn_novaras_fort_seb_barracks_bed"] = BtnJumpLabel(_("Bunk"), "qst_ForgedInFire_YourBunk")
            elif self.progress == 4 or self.progress == 5:
                if GetLocID() == "novaras_fort_seb_barracks":
                    btnMods["btn_novaras_fort_seb_barracks_to_captain_office"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT_CAPTAIN_OFFICE, "qst_ForgedInFire_CantEnterCaptainsOffice")
                    btnMods["btn_novaras_fort_seb_barracks_bed"] = BtnJumpLabel(_("Bunk"), "qst_ForgedInFire_YourBunk")

                elif GetLocID() == "novaras_fort_seb_yard":
                    if self.ShowKiaraWithPoisonTrinket:
                        if GetGameDay() % 2 == 0:
                            if IsInTimeFrame(TIME_DAY_START, TIME_DAY_END):
                                if CharGetVar("kiara", "met") == True:
                                    btnMods["btn_novaras_fort_seb_kiara_talk"] = BtnJumpLabel(_("Kiara"), "qst_ForgedInFire_TalkKiaraSuicidePill")
                                else:
                                    btnMods["btn_novaras_fort_seb_kiara_talk"] = BtnJumpLabel(_("Scout Girl"), "qst_ForgedInFire_TalkKiaraSuicidePill")

                elif GetLocID() == "novaras_fort_seb_train":
                    # this assumes a training session in question will skip time to light end
                    # if training doesnt, the button will reappear same day after training
                    if IsDaytime():
                        btnMods["btn_novaras_fort_seb_train_begin"] = BtnJumpLabel(_("Hang around until the training session starts"), "qst_ForgedInFire_BeginNextTrainingEvent")

            return LocButtonMod(directMods = btnMods, priority = 1)

        def onStart(self):
            AutoTimeFreeze(True)
            CharAddRelEntry("markus", "after_scouts")
            return

        def onComplete(self):
            AutoTimeFreeze(False)
            CharMeet("kiara", Silent = True)
            CharMeet("duprey", Silent = True)
            CharMeet("borras", Silent = True)
            if "WarriorHeavySlash" not in CharGetVar("markus", "CharSkills"):
                worldChars["markus"]["CharSkills"]["WarriorHeavySlash"] = 1
            return

label qst_ForgedInFire_CantLeaveSebastian:
    "As I approached the gates, two guards crossed their halberds in front of me."
    show cg_guard at left with easeinleft
    show cg_guard at right_f as guard2 with easeinright
    "One of the guards addressed me with a heavy, hallowing voice:"
    show cg_guard at shake
    GUARD "Your leave permit, scout."
    MC "Huh?"
    GUARD "Present your leave permit, as dispatched by your direct commanding officer."
    "The guard sized me up."
    GUARD "That would be Captain Duprey."
    GUARD "And I suspect you have no such permit."
    show cg_guard at shake
    GUARD "About-turn!"
    "I watched them stand still for a moment and then turned around, disappointed."
    $ LocFlush(dissolve)
    MC "(It seems like I'm not getting out anytime soon.)"
    GUARD "Double-march!"
    MC "*Sigh* Sir yes sir..."
    $ LocEnter()

label qst_ForgedInFire_EnterMedwardAfterHeadbuttLines:
    $ QstForgedInFire().ShowHeadbuttLines = False
    show mcprologue at left with easeinleft
    "That was the building they dragged that poor recruit towards."
    "Rows of actual comfy beds, shelves full of various potions and tools, civilian-looking people hurrying about past me..."
    "It was clearly a section of the fort fully devoted to supporting our physical well-being."

    RECRUIT "Ow! What are you~"
    "Over at the corner of the room, a nurse and a physician were likely putting that recruit's face back together."
    "As I remembered the scene in vivid details, a snapping sound echoed across the room."
    play sound "audio/cfx/duprey_headbutt.ogg"
    RECRUIT "{b}Aaaagh!!!{/b}"
    MC "(On the upside, he won't have no face time with Captain Duprey anytime soon.)"
    MC "(I should go to the training area now.)"
    MC "(I don't want to end up in here, one way or another.)"
    $ LocEnter()

label qst_ForgedInFire_CantEnterCaptainsOffice:
    "I approached the door and a guard standing beside it turned to face me:"
    show cg_guard at center_f with dissolve
    
    GUARD "You have no business at the Captains office, recruit."
    "His tone was even but surprisingly chill."
    MC "Yeah, I'm just looking around."
    GUARD "Sure, just don't bother me as you play inquisitor around here."
    "I nodded and stepped back."
    hide cg_guard with dissolve
    MC "(A guard who doesn't sound like he's eating babies for breakfast, who would've thought.)"
    $ LocEnter()

label qst_ForgedInFire_CantGoToMedwardOrTrainArea:
    "I should go to the barracks as instructed."
    "Last thing I want is for these guards to skewer me for displaying any disobedience..."
    $ LocEnter()

label qst_ForgedInFire_CaughtOutsideOfAllowedTime:
    "I was approached by a rather hostile-looking guard."
    show cg_guard at center_f with dissolve
    
    GUARD "Recruit! What are you doing loitering about after dark?!"
    MC "I was just~"
    show cg_guard at shake
    GUARD "I will escort you to your bunk now!"
    MC "*Sigh* Alright, alright..."
    scene black with dissolve
    $ LocSet("novaras_fort_seb_barracks")
    "The guard did as he declared, following me around and even standing beside me as I was undressing to go to bed."
    GUARD "Sweet dreams, soldier!"
    if QstGetProgress(QstForgedInFire) in [4, 5]:
        if QstForgedInFire().TrainingProgress == 0:
            jump qst_ForgedInFire_Training0NightEvent
        if QstForgedInFire().TrainingProgress == 1:
            jump qst_ForgedInFire_Training1NightEvent
        if QstForgedInFire().TrainingProgress == 2:
            jump qst_ForgedInFire_Training2NightEvent
    jump qst_ForgedInFire_SleepAtFort

label qst_ForgedInFire_YourBunk:
    "My bunk."
    menu:
        "Go to sleep.":
            if not IsInTimeFrame(TIME_VISUAL_DAWN, TIME_VISUAL_DUSK):
                $ HealParty()
                if QstGetProgress(QstForgedInFire) in [4, 5]:
                    if QstForgedInFire().TrainingProgress == 0:
                        jump qst_ForgedInFire_Training0NightEvent
                    if QstForgedInFire().TrainingProgress == 1:
                        jump qst_ForgedInFire_Training1NightEvent
                    if QstForgedInFire().TrainingProgress == 2:
                        jump qst_ForgedInFire_Training2NightEvent
                jump qst_ForgedInFire_SleepAtFort
            else:
                MC "(I won't be allowed any pillow-time with the sun still up.)"
                pass

        "On a second thought, not now.":
            pass

    $ LocEnterQ()

### all "go to sleep" branches should fall into this label
### except the unique night events
label qst_ForgedInFire_SleepAtFort:
    scene black with dissolve
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)
    $ Pause(0.5)
    $ TimeAdvTo(TIME_VISUAL_DAWN)
    if QstGetProgress(QstForgedInFire) == 3:
        $ QstSetProgress(QstForgedInFire, 4)
    $ LocEnter()

label qst_ForgedInFire_TalkKiaraSuicidePill:
    $ QstForgedInFire().ShowKiaraWithPoisonTrinket = False
    show kiara at cright_f with dissolve
    show mcprologue at cleft with easeinleft
    if CharGetVar("kiara", "met") == True:
        "I noticed Kiara standing somberly near the barracks' entrance, inspecting some trinket around her neck."
        "It was a small type of vial with some liquid sloshing about inside that I'd seen only on the women scouts."
        MC @talk "Hey."
    else:
        "I noticed that recruit girl I've seen a few times now standing somberly near the barracks, inspecting some trinket around her neck."
        "It was a small type of vial with some liquid sloshing about inside that I'd seen only on the women scouts."
        MC @talk "Hey..."
        "The girl looked at me."
        KIARA "Yeah?"
        MC "(Now is as good time as any, [player_name!t]...)"
        MC @talk "I'm [player_name!t]. You?"
        "She paused quizzically, as if I asked her to recite the entire pantheon of the old Alderian gods..."
        KIARA "Oh, I'm Kiara, sorry, it's just, this..."
        $ CharSetVar("kiara", "met", True)
        $ CharMeet("kiara", DefaultRel = "rel_friend")
        $ KIARA = Character(_("Kiara"), image = "kiara")
        "Kiara glanced at the trinket in her hand."
    MC @talk "What's that?"
    KIARA @scared "Hm? A-Ah..."
    KIARA @scared "You mean, {i}you don't have them?{/i}"
    MC @think "Have what?"
    KIARA @sad "...I suppose it makes sense they'd only give these to the women."
    "My thoughts naturally gravitated towards it being some type of contraceptive, but from Kiara's deathly face, I got the impression this was something else entirely..."
    MC @talk "What is it?"
    KIARA @sad "{i}Poison.{/i}"
    MC @scared "Poison?"
    KIARA @sad "Yes... Poison."
    KIARA @sad "You see, the Demorai will likely just kill men on sight."
    "There was a long pause before she spoke again."
    KIARA @sad "...But, if they know it's a woman, then-"
    "Kiara let the sentence trail off into nothing as her eyes looked up to meet mine."
    MC @talk "...I see."
    "Clearly uncomfortable with the thought, Kiara put the poisoned vial around her neck away."
    KIARA "Well, I best get back to it."
    MC @talk "...Kiara."
    KIARA "Hm?"
    MC @talk "I don't know how, but..."
    MC @talk "We're gonna survive this somehow, I promise."
    "Kiara smiled."
    $ CharChangeRel("kiara", 1)
    KIARA @happy "Bloody optimist, aren't ya?"
    hide kiara with easeoutright
    "Kiara left with a smile on her face."
    MC "(Gonna survive this, huh?)"
    MC "(I almost convinced myself there!)"
    #hide mcprologue with dissolve
    $ LocEnter()

label qst_ForgedInFire_CaughtSkippingTraining:
    "A couple of guards approached me."
    show cg_guard at left with easeinleft
    show cg_guard at right_f as guard2 with easeinright
    "The bulkier of the guards addressed me:"
    show cg_guard at shake
    GUARD "Hey you!"
    MC "Sir-yes-sir?"
    GUARD "You are! Aren't!"
    "As he waved his halberd at me, another guard interjected in a way friendlier tone:"
    SECOND_GUARD "Do you see the sun up in the sky, recruit?"
    "Seeing exactly what was coming next, I nodded without even looking up:"
    MC "Yeah."
    SECOND_GUARD "And what does that mean?"
    MC "Means we are all but mere insects under its eternal glory."
    "A muffled laugh escaped from underneath the friendlier guard's helmet."
    show cg_guard at shake
    GUARD "It means you maggot supposed to be training!"
    show cg_guard at shake
    GUARD "At the training yard!"
    "With a wave of his halberd, the bulky guard set me on my way."
    scene black with dissolve
    MC "(Join the army they said...)"
    $ LocSet("novaras_fort_seb_train")
    $ LocEnter()

label qst_ForgedInFire_BeginNextTrainingEvent:
    if QstForgedInFire().TrainingProgress == 0:
        jump qst_ForgedInFire_Training0FirstFight

    if QstForgedInFire().TrainingProgress == 1:
        jump qst_ForgedInFire_Training1SkillsAndEnergyAndItems

    if QstForgedInFire().TrainingProgress == 2:
        jump qst_ForgedInFire_Training2Teamwork

    if QstForgedInFire().TrainingProgress == 3:
        jump qst_ForgedInFire_Training3Final

    $ LocEnterQ()