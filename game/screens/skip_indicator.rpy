screen skip_indicator():
    zorder 100
    frame:
        anchor (0.5, 0.5)
        if PlayerItemQty("gold") < 1 or IsPlayerInBattle():
            pos (210, 38)
        else:
            pos (430, 38)
        text _("Skipping"):
            size 25