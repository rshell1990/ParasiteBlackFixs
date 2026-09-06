init python:
    def PartyAddChar(char_ID, Silent = False):
        if char_ID not in worldChars:
            raise Exception("PartyAddChar: Unknown character: %s" % char_ID)
        if not CharInParty(char_ID):
            store.player_party.append(char_ID)
            # Update the character"s XP in order to catch up with the MC
            if char_ID != "mc":
                AddExperienceToMatchPlayer(char_ID)
                RecalcSkillAndAttrPoints(char_ID)
            if not Silent:
                AddNotif(tra(_("%s joins your party!")) % tra(worldChars[char_ID]["name"]), Kind = "char_joins_party")

        ### achievement
        if GetPartySize() >= 4 and can_unlock_achievement("A_WARRIOR_NEEDS_HIS_ALLIES"):
            unlock_achievement("A_WARRIOR_NEEDS_HIS_ALLIES")
        return

    # returns True/False if char with given id is in player party
    def CharInParty(CharID):
        Assert(isinstance(CharID, str), "CharInParty(%s): CharID must be a string!" % CharID)
        Assert(CharID in worldChars, "CharInParty(%s): CharID %s not found!" % (CharID, CharID))
        return CharID in store.player_party

    # returns integer amount of chars in player party
    def GetPartySize():
        return len(store.player_party)

    # removes char from party AND unequips their items, does a notification
    def PartyRemChar(char_ID, Silent = False):
        if CharInParty(char_ID):
            for SlotID in EQP_SLOTS.ALL:
                UnequipItem_CharID(char_ID, SlotID)

            store.player_party.remove(char_ID)

            if char_ID in PlayerCombatTeam:
                store.PlayerCombatTeam.remove(char_ID)
            if not Silent:
                AddNotif(tra(_("%s leaves your party!")) % CharGetName(char_ID), Kind = "char_leaves_party")
        return

####################################
    def PartyTalkToChar(CharID):
        TargetLabel = (CharIDPartyDialogueLabelMap[CharID] if CharID in CharIDPartyDialogueLabelMap else "talk_fallback")
        renpy.jump(TargetLabel)
        return

    def PlayerCanSpeakToPartyChars():
        if (not block_wait_global and not block_wait_dynamic and wLocs[GetLocID()].CanWait and not PartyCharsTalkBlocked):
            return True
        else:
            return False

# to be able to toggle on the fly
default PartyCharsTalkBlocked = False

label talk_fallback:
    "We had an interesting conversation."
    $ LocEnter()