default dros_player_ref = _("Master")

init python:
    @AppendToAllQuests
    class RomanceDros(LogicModule):
        def __init__(self):
            super().__init__()

            self.sawPostTransformFirstMeet = False
            self.fuckedOnce = False
            self.fuckedToday = False
            self.playerRef = None

        def onNoon(self):
            self.fuckedToday = False

        def onStart(self):
            self.playerRef = player_name

        def extraDialogue(self):
            yield ("dros_root", DNode(_("How have you been?"), "rom_Dros_howYouBeen"))
            if QstIsActive(RomanceDros):
                if not self.fuckedToday:
                    yield ("dros_root",DNode(_("Close the store... Your ass is mine."), "rom_Dros_closeTheStore"))
                else:
                    yield ("dros_root",DNode(_("Close the store... Your ass is mine."), "rom_Dros_store_sex_cooldown"))

label rom_Dros_howYouBeen:
    $ rng = RngInt(1,3)
    if rng == 1:
        DROS @smile 'Good actually!'
        if CharGetVar("dros", "Transformed") == True:
            DROS @lewd "Though I must admit, I'm not quite sure how to feel when people are so obviously staring at my chest now."
            DROS @smile 'Flattered I guess?'
    if rng == 2:
        DROS @talk 'The shop has been very busy recently.'
        DROS @talk "Lot's of orders and all that."
        DROS @lewd "{i}...Any idea how you could help your horny elf slut blow off some steam?{/i}"
    if rng == 3:
        DROS @sad 'Lonely... Gods, I wish we had more time together.'
        DROS @sad "I um, {i}pray for your safe return when I know you're away.{/i}"
        DROS @smile 'Silly, I know... But it makes me feel better.'
    return