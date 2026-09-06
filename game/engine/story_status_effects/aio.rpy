# a dict of CharID:{effectID:duration, effectID:duration}
default StoryStatusEffects = {}

init -1 python:
    # effectID:statmods
    StoryStatEffDefs = {
        "RazaEffect":{
            "StrengthAdd":1,
            "EnduranceAdd":1,
            "DexterityAdd":-2
        },
        # as in, it exists
        "Poison":{},
    }

    def StoryCharIsPoisoned(CharID):
        if StoryCharHasStatusEff(CharID, "Poison"):
            return True
        else:
            return False

    def ItemRazaEffectUser(ItemID, char_ID):
        # check if raza poison already on
        if StoryCharHasStatusEff(char_ID, "RazaEffect"):
            AddNotif(_("Raza seed had no effect."))
            return

        # apply effs
        ApplyStatusEffect_Story(char_ID, "Poison", 6)
        ApplyStatusEffect_Story(char_ID, "RazaEffect", 6)

        RemItemFrom(player_inv, ItemID, 1, FromPlayer = True)
        return

    def ItemStrangeMeatPoisonUser(ItemID, char_ID):
        CharHeal(char_ID, Value = 10)        

        ApplyStatusEffect_Story(char_ID, "Poison", 24)

        RemItemFrom(player_inv, ItemID, 1, FromPlayer = True)
        return

    def ItemAntidoteStory(ItemID, char_ID):
        if not StoryCharHasStatusEff(char_ID, "Poison"):
            return

        if char_ID == "mc":
            AddNotif(_("You are cured of poison!"))
        else:
            AddNotif(_("%s is cured of poison!") % worldChars[char_ID]["name"])

        RemoveStatusEffect_Story(char_ID, "Poison")
        RemItemFrom(player_inv, ItemID, 1, FromPlayer = True)
        return

    def PoisonParty():
        for CharID in player_party:
            ApplyStatusEffect_Story(CharID, "Poison", 6)

    def ApplyStatusEffect_Story(CharID, EffectID, Duration, Silent = False):
        Char = worldChars[CharID]

        if CharID not in StoryStatusEffects:
            StoryStatusEffects[CharID] = {}

        # store health ratio
        StoredHealthRatio = Char["Health"] / Char["HealthMax"]

        # notif
        if Silent == False:
            if EffectID == "Poison":
                if CharID == "mc":
                    AddNotif(_("You are poisoned!"), Kind = "poison_story")
                else:
                    AddNotif(_("%s is poisoned!") % Char["name"], Kind = "poison_story")

        # no stacking or sth, it just bumps to the most longest duration
        if EffectID in StoryStatusEffects[CharID]:
            if Duration > StoryStatusEffects[CharID][EffectID]:
                StoryStatusEffects[CharID][EffectID] = Duration
        else:
            StoryStatusEffects[CharID][EffectID] = Duration 

        Assert(1.0 >= StoredHealthRatio >= 0.0, "Heal ratio must be within 0.0-1.0")
        Char["Health"] = round(Char["HealthMax"] * StoredHealthRatio)
        return

    def StoryCharHasStatusEff(CharID, EffectID):
        if CharID not in StoryStatusEffects:
            return

        if EffectID in StoryStatusEffects[CharID]:
            return True
        else:
            return False

    def TickStoryStatusEffects():
        for CharID in list(StoryStatusEffects):
            MarkedForRemoval = []
            for StatusEffectID in StoryStatusEffects[CharID]:
                StoryStatusEffects[CharID][StatusEffectID] -= 1
                StoryStatusEffect_DoHourlyEffect(CharID, StatusEffectID)

                if StoryStatusEffects[CharID][StatusEffectID] <= 0:
                    MarkedForRemoval.append(StatusEffectID)

            for StatusEffectID in MarkedForRemoval:
                RemoveStatusEffect_Story(CharID, StatusEffectID)
        return

    def RemoveStatusEffect_Story(CharID, EffectID):
        if CharID not in StoryStatusEffects:
            return

        if EffectID not in StoryStatusEffects[CharID]:
            return

        StoryStatusEffects[CharID].pop(EffectID)
        if len(StoryStatusEffects[CharID]) == 0:
            StoryStatusEffects.pop(CharID)
        return

    def StoryStatusEffect_DoHourlyEffect(CharID, EffectID):
        if EffectID == "Poison" and CharID:
            if CharID in worldChars and worldChars[CharID]["Health"] > 1:
                DamageChar(CharID, 10, Lethal = False)
                if CharID == "mc":
                    AddNotif(tra(_("The poison damages you!")), Kind = "story_damage_mc")
                else:
                    if CharID in player_party:
                        AddNotif(tra(_("The poison damages %s!")) % worldChars[CharID]["name"], Kind = "story_damage_nonmc")
        return