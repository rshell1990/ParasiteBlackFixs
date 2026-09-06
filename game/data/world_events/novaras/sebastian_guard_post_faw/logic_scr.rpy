init python:
    @AppendToAllQuests
    class EventSebastianGuardPostFawOneOff(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_dist_army":
                btnMods["btn_novaras_fort_seb"] = BtnJumpLabel(STR_LOC.NOV_CITY_FORT, "ev_seb_guard_post_faw_one_off")
            return LocButtonMod(directMods = btnMods)

label ev_seb_guard_post_faw_one_off:
    $ QstComplete(EventSebastianGuardPostFawOneOff)
    show cg_guard at right_f with dissolve
    show mc at left with easeinleft
    GUARD "State your-" 
    "The guard looked me up and down for a moment." 
    GUARD "You... I've seen you..."
    show cg_guard at shake
    GUARD "You're one of these survivors they had brought in!" 
    "The guard contemplated for a moment."
    GUARD "Well, you're no longer a scout, so unless you have business here, I suggest you move on..."
    hide cg_guard with dissolve
    show mc at center with ease
    MC "(So much for serving the empire...)"
    $ LocEnter()
