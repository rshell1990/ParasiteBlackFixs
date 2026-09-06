default Notify_Messages = []

default DEBUG_NotifsSupressed = False

init python:
    Notify_ValidKinds = [
        "generic",

        # preg
        "char_gave_birth",
        "char_impregnated",

        "attr_raised",
        "save_related",

        # party
        "char_joins_party",
        "char_leaves_party",

        # damage
        "story_damage_mc",
        "story_damage_nonmc",

        # chars
        "char_rel_increase",
        "char_rel_decrease",
        "char_rel_increase_unchanged",
        "char_rel_decrease_unchanged",
        "char_metnew",
        "char_isnowlover",

        # infection
        "infection_raise",
        "infection_decrease",
        "parasite_satisfied",
        "parasite_lostinterest",

        # gallery
        "scene_unlocked",
        "scene_updated",

        "heal_party",

        # items
        "gold_handle",
        "item_add",
        "item_rem",

        # quests
        "qst_goal_new",
        "qst_goal_complete",
        "qst_goal_failed",
        "qst_new",
        "qst_fail",
        "qst_complete",

        "note_new",

        "poison_story",
    ]

    def AddNotif(Message = None, Kind = "generic"):
        if not Message:
            return
        if DEBUG_NotifsSupressed == True:
            return
        Assert(Kind in store.Notify_ValidKinds, "Wtf, notification kind %s not valid!" % Kind)

        AddTime = renpy.time.time()

        # Just in case multiple notifications are added fast, 
        # this gives them minorly different time values 
        # so they do not steal displayables meant for other notifications
        if store.Notify_Messages and store.Notify_Messages[-1][1] >= AddTime:
            AddTime = store.Notify_Messages[-1][1] + 0.01

        store.Notify_Messages.append((Message, AddTime, Kind))

        # trim to keep SOME number of messages not all of them
        store.Notify_Messages = store.Notify_Messages[-20:]

        if Kind in ["item_add", "item_rem"]:
            PlaySoundRandomPara("item_handle_generic", Channel = "guisfx")
        elif Kind == "gold_handle":
            PlaySoundRandomPara("item_handle_coins", Channel = "guisfx")
        elif Kind == "note_new":
            PlaySoundPara("audio/interface/note.ogg", Channel = "guisfx")
        elif Kind in ["scene_unlocked", "scene_updated"]:
            PlaySoundPara("audio/interface/gallery_unlock.ogg", Channel = "guisfx")
        elif Kind == "qst_new":
            PlaySoundPara("audio/interface/new_quest.ogg", Channel = "guisfx")
        elif Kind == "poison_story":
            PlaySoundPara("audio/interface/poison_story.ogg", Channel = "guisfx")
        elif Kind == "qst_complete":
            PlaySoundPara("audio/interface/quest_complete.ogg", Channel = "guisfx")
        elif Kind in ["qst_goal_new", "qst_goal_complete", "qst_goal_failed", "qst_new", "qst_fail"]:
            PlaySoundPara("audio/interface/quest_update.ogg", Channel = "guisfx")
        elif Kind in ["char_joins_party", "char_leaves_party"]:
            PlaySoundPara("audio/interface/party_join.ogg", Channel = "guisfx")
        else:
            PlaySound("audio/interface/notification.ogg", Channel = "guisfx", Volume = 0.4)

        # add to history
        NewHistoryEntry = renpy.character.HistoryEntry()
        NewHistoryEntry.what = "NOTIF_" + "{color=#B8B8B8}" + tra(Message) + "{/color}"
        store._history_list.append(NewHistoryEntry)

        
        #renpy.restart_interaction()
        return

    def DEBUG_SupressNotifs(NewVal):
        store.DEBUG_NotifsSupressed = NewVal

    def NotifHardClear():
        store.Notify_Messages = []