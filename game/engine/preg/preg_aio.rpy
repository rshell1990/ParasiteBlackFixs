init -1 python:
    # gives you char's preg value, can range from 0 to 4. 0 is no-preg, 1-2-3 are stages, 4 is "post-birth" stage, each stage is week-long.
    def CharGetPreg(CharID):
        return CharGetVar(CharID, "preg")
    # DONT FUCK AROUND WITH THIS unless uk now what you doin
    def CharSetPreg(CharID, Val):
        CharSetVar(CharID, "preg", Val)
        return
    # to easily tell "that char is preg" in a visual sprite sense, also used alot in logic
    def CharIsVisiblyPreg(CharID):
        if _in_replay:
            return store.Sex_SharedPregFlag
        if 1 <= CharGetPreg(CharID) <= 3:
            return True
        return False

    def PregRoll(CharID, ChanceOverride = None):
        if _in_replay:
            return
        Assert(CharID in PregModuleClassesForChars, "char ID %s not found in PregModuleClassesForChars! (pregroll)" % CharID)

        PregModule = PregModuleClassesForChars[CharID]
        if ChanceOverride:
            PregChance = ChanceOverride
        else:
            PregChance = PregModule().ImpregChance
        Roll = RngInt(1, 100)
        if config.developer:
            if Roll <= PregChance:
                AddNotif("DEBUG: rolled impreg for id %s, rolled %s, target is %s or less, SUCCESS" % (CharID, Roll, PregChance))
            else:
                AddNotif("DEBUG: rolled impreg for id %s, rolled %s, target is %s or less, FAIL" % (CharID, Roll, PregChance))

        if Roll <= PregChance:
            # 'impregnate' section
            if not QstIsActive(PregModule):
                QstStart(PregModule)

            if PregModule().IsPreg == True:
                if config.developer:
                    AddNotif("DEBUG: successfully rolled impreg for id %s but theyre already preg" % CharID)
                return

            PregModule().IsPreg = True
            PregModule().IsInPregMode = True
            PregModule().NumImpregs += 1

            if PregModule().ImpregnatedNotifShow:
                AddNotif(PregModule().ImpregnatedNotifText, Kind = "char_impregnated")

            PregModule().PostImpreg()
        return

    def CharGetBirths(CharID):
        Assert(CharID in PregModuleClassesForChars, "char ID %s not found in PregModuleClassesForChars! (chargetbirths)" % CharID)
        PregModule = PregModuleClassesForChars[CharID]
        return PregModule().NumBirths

################ internals
    PregModuleClassesForChars = {}
    def RegisterPregModuleFor(CharID):
        def Decorate(Class):
            store.PregModuleClassesForChars[CharID] = Class
            return Class
        return Decorate

###### preg module is a slightly overloaded subtype of an lm
## it has some special functions and fields shared among most preg lms
    class BasePregModule(LogicModule):
        def __init__(self):
            super().__init__()
            self.priority = 1 # <- all preg events are bumped priority-wise

        ##### names ids
            self.CharID = "undefined (its a bug)" # set per-instance

            self.BabyNameDefault = "debug"
            self.BabyNameRandomList = ["debug1", "debug2", "debug3"]

            self.LastBornBabyName = _("the child") # stores the player choice/input
        ##### notifs
            self.GaveBirthNotifText = _("Someone has given birth...")
            self.GaveBirthNotifShow = True

            self.ImpregnatedNotifText = _("I feel like something important just happened.")
            self.ImpregnatedNotifShow = True 
        ##### preg-stages logic
            self.ImpregChance = 33 # base chance in %
            self.IsPreg       = False # IMPORTANT, this one means "pregnant, but not given birth yet"
            self.IsInPregMode = False # but this one is "pregnant OR HAS ALREADY GIVEN BIRTH AND IN LAST STAGE"
            self.duration     = 0
            self.step_length  = 7
        ##### bookkeeping
            self.NumImpregs = 0   # increment each impregnation
            self.NumBirths  = 0   # increment each birth

        #### override per-module if ya need any vars tied to post-impregnation
        def PostImpreg(self):
            pass
        # same as above
        def PostBirth(self):
            pass

        ##### shared processing
        def onMidnight(self):
            # if impregnated, increment duration
            if self.IsInPregMode:
                self.duration += 1
            else:
                return    

            # handle setting pregnancy state of a char based on time
            # bump stage 1
            if self.step_length <= self.duration < self.step_length * 2:
                CharSetPreg(self.CharID, 1)
            # bump stage 2
            elif self.step_length * 2 <= self.duration < self.step_length * 3:
                CharSetPreg(self.CharID, 2)
            # bump stage 3
            elif self.step_length * 3 <= self.duration < self.step_length * 4:
                CharSetPreg(self.CharID, 3)
            # no bump, give birth logic & hang out with baby for this last period
            elif self.step_length * 4 <= self.duration < self.step_length * 5:
                CharSetPreg(self.CharID, 4)                

                # 'give birth' section
                if self.IsPreg == True:
                    if self.GaveBirthNotifShow:
                        AddNotif(self.GaveBirthNotifText)
                    self.NumBirths += 1
                    self.IsPreg = False
                    self.PostBirth()

            # reset to 0
            elif self.duration >= self.step_length * 5:
                CharSetPreg(self.CharID, 0)
                self.IsInPregMode = False
                self.IsPreg = False # <- for safety, realistically this is likely unnecessary but who the fuck knows
                self.duration = 0
            return
