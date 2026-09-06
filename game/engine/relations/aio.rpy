default rel_known_chars = set()

# by default, all statuses (PLUS "dead") are shown. 
# this set has all that are currently filtered-out
default RelScreenFilterStatusesExcluded = set()

init -1 python:
    Rel_Status_ID_Strings = {
        "rel_lover":{
            "Title":_("Lover"),
            "Icon":"images/gui/story/heart.webp",
            "ShowNumber":True},

        "rel_friend":{
            "Title":_("Friend"),
            "Icon":"images/gui/story/handshake.webp",
            "ShowNumber":False},

        "rel_acquaintance":{
            "Title":None,
            "Icon":None,
            "ShowNumber":False},

        "rel_enemy":{
            "Title":_("Enemy"),
            "Icon":"images/gui/story/swords.webp",
            "ShowNumber":False}
    }
    # this dict is filled on a per-char basis, in char definitions
    # the entries are for the relationship screen
    RelText = {}
    
    def CharAddRelEntry(CharID, RelTextID):
        if CharID not in RelText:
            raise Exception("Char ID %s not in RelText" % CharID)
        if RelTextID not in RelText[CharID]:
            raise Exception("Relationship text ID %s not in RelText for char ID %s" % (RelTextID, CharID))

        worldChars[CharID]["RelTextIDs"].add(RelTextID)
        return

    def CharRemRelEntry(CharID, RelTextID, Hard = True):
        if CharID not in RelText:
            raise Exception("Char ID %s not in RelText" % CharID)
        if RelTextID not in RelText[CharID]:
            raise Exception("Relationship text ID %s not in RelText for char ID %s" % (RelTextID, CharID))

        if Hard:
            worldChars[CharID]["RelTextIDs"].remove(RelTextID)
        else:
            if RelTextID in worldChars[CharID]["RelTextIDs"]:
                worldChars[CharID]["RelTextIDs"].remove(RelTextID)
        return

    def CharReplaceRelEntry(CharID, OriginalRelTextID, NewRelTextID):
        if CharID not in RelText:
            raise Exception("Char ID %s not in RelText" % CharID)
        if OriginalRelTextID not in RelText[CharID]:
            raise Exception("Relationship text ID %s not in RelText for char ID %s" % (NewRelTextID, CharID))
        if NewRelTextID not in RelText[CharID]:
            raise Exception("Relationship text ID %s not in RelText for char ID %s" % (NewRelTextID, CharID))

        if OriginalRelTextID in worldChars[CharID]["RelTextIDs"]:
            worldChars[CharID]["RelTextIDs"].remove(OriginalRelTextID)
        worldChars[CharID]["RelTextIDs"].add(NewRelTextID)
        return

    def DEBUG_MeetAllChars():
        # THE LIST IS VERY LIKELY OBSOLETE!
        for CharID in [
            "adara",
            "alcott",
            "arlena",
            "arwen",
            "borras",
            "callie",
            "celeste",
            "divine",
            "drax",
            "dros",
            "duprey",
            "elena",
            "erika",
            "helena",
            "kiara",
            "kylisa",
            "babazhul",
            "luciusmal",
            "lukkan",
            "markus",
            "shay",
            "sypha",
            "shani",
            "thea",
            "trayan",
            "myu",
            "nijah",
            "nyx",
            "regina",
            "skallion",
            "vala",
            "ves",
            "vizura",
            "mr_winward",
            "mrs_winward"]:

            CharMeet(CharID)
            CharSetRelStatus(CharID, renpy.random.choice(list(Rel_Status_ID_Strings.keys())))
            if renpy.random.randint(1, 4) == 1:
                worldChars[CharID]["relisdead"] = True
        return

    # add to known
    def CharMeet(CharID, Silent = False, DefaultRel = "rel_acquaintance"):
        # auto-bail to allow spam across script
        if CharID in store.rel_known_chars:
            # in case the defaultrel param was overridden, we setrel silently
            if DefaultRel != "rel_acquaintance":
                CharSetRelStatus(CharID, DefaultRel)
            return
        if not Silent:
            AddNotif(tra(_("New character entry: %s")) % tra(worldChars[CharID]["name"]), Kind = "char_metnew")
        store.rel_known_chars.add(CharID)
        CharSetRelStatus(CharID, DefaultRel)
        return

    # shorthand(s)
    def CharIsMet(CharID):
        if CharID in store.rel_known_chars:
            return True
        return False

    def CharIsAlive(CharID):
        return not store.worldChars[CharID]["relisdead"]

    def CharIsLover(CharID):
        if worldChars[CharID]["relstatus"] == "rel_lover":
            return True
        else:
            return False
    
    def CharSetAcquaintance(CharID, Silent = False):
        # auto-bail to allow spam across script
        if worldChars[CharID]["relstatus"] == "rel_acquaintance":
            return

        # if not met, meet at acquaintance (rough debugging)
        if not CharIsMet(CharID):
            CharMeet(CharID, Silent = Silent)
        return


    # make em listed as lover
    def CharSetLover(CharID, Silent = False):
        if _in_replay:
            return
        # auto-bail to allow spam across script
        if worldChars[CharID]["relstatus"] == "rel_lover":
            return

        # if not met, meet at acquaintance (rough debugging)
        if not CharIsMet(CharID):
            CharMeet(CharID, Silent = Silent)

        # set lover
        CharSetRelStatus(CharID, "rel_lover")
        if not Silent:
            AddNotif(tra(_("%s is now your lover!")) % tra(worldChars[CharID]["name"]), Kind = "char_isnowlover")
        return

    # make em listed as friend (shorthand)
    def CharSetFriend(CharID, Silent = True):
        # auto-bail to allow spam across script
        if worldChars[CharID]["relstatus"] == "rel_friend":
            return

        # if not met, meet at acquaintance (rough debugging)
        if not CharIsMet(CharID):
            CharMeet(CharID, Silent = Silent)

        # set friend
        CharSetRelStatus(CharID, "rel_friend")
        return

    # make em listed as dead
    def CharKill(CharID, Sound = True):
        if Sound == True:
            PlaySound("audio/interface/char_death.ogg", Channel = "guisfx")
        store.worldChars[CharID]["relisdead"] = True
        return

    # make em not dead
    def CharUnKill(CharID):
        store.worldChars[CharID]["relisdead"] = False
        return

    # change rel status to X
    # kinda internal not supposed to be done super manually but you can do it
    def CharSetRelStatus(CharID, RelStatusID):
        if RelStatusID not in Rel_Status_ID_Strings:
            raise Exception("%s is not a valid rel status ID" % RelStatusID)

        worldChars[CharID]["relstatus"] = RelStatusID
        return

    