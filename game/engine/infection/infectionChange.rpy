init python:
    # returns current infection val
    def InfGetValue():
        return InfectionModule().CurrentValue

    # Adjusts infection value and performs relevant checks
    def InfChangeBy(ChangeByRaw, silent = False, cantLose = False, SetTo = False):
        InfModule = InfectionModule()
        ### this is for cases where inf change is called directly
        if not InfModule.isActive:
            return

        OriginalValue = InfModule.CurrentValue

        ChangeBy = round(ChangeByRaw * DIFFICULTY.INFECTION_GAIN[CurrentDifficulty])
        if SetTo:
            InfModule.CurrentValue = ChangeBy
        else:
            InfModule.CurrentValue = ClampValue(OriginalValue + ChangeBy, 0, InfModule.MaxValue)

        if not silent and OriginalValue != InfModule.CurrentValue:
            if InfModule.CurrentValue > OriginalValue:
                AddNotif(tra(_("Infection grows up to ")) + str(int(InfModule.CurrentValue)), Kind = "infection_raise")
            if InfModule.CurrentValue < OriginalValue:
                AddNotif(tra(_("Infection drops to ")) + str(int(InfModule.CurrentValue)), Kind = "infection_decrease")

        if InfModule.CurrentValue >= 100 and not cantLose:
            renpy.jump("defeat_generic")
        return

    # generic function to lower infection when having sex
    def ReduceInfectionFromSex(CharacterID = None, By = None):
        if _in_replay:
            return
        ### if infection module is inactive, bail
        if InfectionModule().isActive == False:
            return

        ### proceed with exec
        InfModule = InfectionModule()

        if CharacterID is not None:

            ### achievement
            global _total_cummed_characters
            if CharacterID not in _total_cummed_characters:
                _total_cummed_characters.append(CharacterID)
            if len(_total_cummed_characters) >= 5 and can_unlock_achievement("YOU_GET_AROUND"):
                unlock_achievement("YOU_GET_AROUND")
            if len(_total_cummed_characters) >= 10 and can_unlock_achievement("STUD"):
                unlock_achievement("STUD")


            ### see if had sex with more than it wants, bail if
            if len(InfModule.SexedTodayCharacterIDs) > InfModule.UniqueDailyChars:
                AddNotif(tra(_("The Parasite seems to be satisfied for today: your infection rate remains unchanged.")), Kind = "parasite_satisfied")
                return

            ### see if had sex with this char, bail if
            if CharacterID in InfModule.SexedTodayCharacterIDs:
                AddNotif(tra(_("The Parasite seems to have lost its interest in this 'mate' for today: your infection rate remains unchanged.")), Kind = "parasite_lostinterest")
                return

            ### if we're here, we're goin. add char ID to sexed today
            InfModule.SexedTodayCharacterIDs.add(CharacterID)

        ### grab result val
        ResultValue = By if By is not None else InfModule.DefaultPerSexReduction

        ### this just consequetively multiplies based off player's gear. what can go wrong right?
        for SlotID in EQP_SLOTS.ALL:
            if worldChars["mc"][SlotID] is not None:
                ItemID = worldChars["mc"][SlotID]
                if all_items[ItemID]["sex_infection_loss_modifier"] != 0.0:
                    ResultValue *= all_items[ItemID]["sex_infection_loss_modifier"]

        InfChangeBy(ResultValue)
        return

    # toggle daily gain True/False
    def InfGainDaily(TrueOrFalse):
        InfectionModule().DailyGain = TrueOrFalse
        return




################# internal stuff ahead
#### this controls infection value AND stores chars you had sex with for infection reduction calc
    @AppendToAllQuests
    class InfectionModule(LogicModule):
        def __init__(self):
            super().__init__()

            self.DailyGain = True

            # start at 25%
            self.CurrentValue = 25
            self.MaxValue = 100
            # reduce bar by 50%
            self.DefaultPerSexReduction = -50

            # set of chars we sexed today
            self.SexedTodayCharacterIDs = set()

            # number of unique daily chars that will reduce infection if sexed
            # increased by perk permanently to 3 later
            self.UniqueDailyChars = 2

        def onMidnight(self):
            # flush unique chars on midnight
            self.SexedTodayCharacterIDs = set()
            return

        def onStart(self):
            # reset in case it was messed with prior to activation
            self.CurrentValue = 25
            self.SexedTodayCharacterIDs = set()
            self.DailyGain = True 
            return