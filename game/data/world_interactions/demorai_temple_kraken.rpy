init python:
    @AppendToAllQuests
    class DemoraiTempleKraken(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "demorai_temple_interior":
                btnMods["BtnKrakenWater"] = BtnJumpLabel(_("Water"),"world_clickable_temple_kraken")
            return LocButtonMod(directMods = btnMods)

label world_clickable_temple_kraken: # outside quest
    'Peering into the depths of the stagnant water over the edges of the erected stone pathways gave me an uneasy feeling.'
    'I could not see what was down there, but I could sense movement beneath that blackened water all the same.'
    'Just how deep did these waters run?'    
    menu:
        "Touch the water":
            'Placing my hand into the water, the ripples once again waved across the still waters.'
            scene cg_demorai_temple_kraken with flash
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            'This time though, bursting out of the waters came a fury of tentacles thrashing wildly!'
            MC '(FUCK!)'
            scene black with dissolve
            "I transformed, preparing myself for battle."
            $ TransformMC(True)
            $ TransformMarkus(True)
            $ StartBattle(BattleData(BackgroundImage = "pbat_demorai_temple", CharIDList_Right = ["e_kraken"]))
            scene black with dissolve
            $ TransformMC(False)
            $ TransformMarkus(False)
            "After slashing and tearing off one of the beasts' tentacles that dropped down into the waters, the beast howled in rage as it quickly retreated and submerged itself back into the black depths from where it came."
            $ LocFlush(dissolve)
            $ AutoMus(True)
            MC '{i}...How the hell does that thing even live down here?{/i}'
            "I noticed on the floor, some strange shimmering gem that wasn't there before."
            $ QstComplete(DemoraiTempleKraken)
            $ PlayerAddItem("qst_kraken_gem")
            MC '(Huh? What is this thing?)'
            $ LocEnter()

        "Step away":
            'Deciding it was probably not a good idea to continue messing with the water, I stepped back.'
            MC "(Whatever's in there isn't going to appreciate me splashing around.)"
            $ LocEnter()