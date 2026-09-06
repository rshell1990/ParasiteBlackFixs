init python:
    @AppendToAllQuests
    class DemoraiHuntButton(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "valley_of_death":
                btnMods["btn_demoraiHunt"] = BtnJumpLabel(_("Hunt Demorai"),"act1_demoraiHunt")

            return LocButtonMod(directMods=btnMods)

label act1_demoraiHunt:
    if GetPartySize() > 1:
        "As we patrolled around the Valley, it did not take us long to find a squad of Demorai scouts lurking about."
        show mc at cleft with easeinleft
        if CharInParty("markus"):
            show markus at left with easeinleft
            MARKUS 'You ready?'
            MC 'Always.'
            MC 'To battle!'
    else:
        "As I patrolled around the Valley, it did not take me long to find a squad of Demorai scouts lurking about."
    
    $ TimeAdvBy(TIME_1H)
    $ AutoMus(False)
    $ PlayMusic("audio/music/10_Battle1.ogg")
    $ StartBattle(BattleData(BackgroundImage = "pbat_desert", CharIDList_Right = GetEnemyList("valley_demorai_hunt")))
    $ AutoMus(True)
    $ LocEnter()
