########### char refs
default regina_ref = _("Regina")
default erika_ref = _("friend") # mc referring to Erika
default erika_mc_ref = _("friend") # Erika referring to mc

default regina_rel_summary = _("Regina, a close family friend who took me in whilst father was sent off to war. I trust her with my life, though I can't help but feel she's hiding something from me...")
default erika_rel_summary = _("My childhood friend who was also taken in by Regina due to the war. As fierce as she beautiful, Erika has joined the elusive inquisitors. I just hope she's never forced to choose betwen me and them...")

########### char refs capitalized ##########
default regina_ref_cap = _("Regina")
default erika_ref_cap = _("Erika")
default erika_mc_ref_cap = _("Friend")

init python:
    # these are hooks for 'modding'
    def RelSet_Regina():
        # CharSetRelStatus(....
        # store.regina_ref = ...
        RelText["regina"]["initial"]["text"] = store.regina_rel_summary
        CharSetName("regina", store.regina_ref_cap)
        return

    def RelSet_Erika():
        RelText["erika"]["initial"]["text"] = store.erika_rel_summary
        CharSetName("erika", store.erika_ref_cap)
        return