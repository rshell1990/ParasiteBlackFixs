init python:
    @AppendToAllQuests
    class BlackDiamondArena(LogicModule):
        def __init__(self):
            super().__init__()

            # prog 1 is "met bookkeeper"
            self.canBet = 1000 # number player bets will be deducted from this
            self.currBet = 0
            self.resetDay = -1 # if a bet is placed, we start a 6 day countdown
        
        def onEnter(self):  
            if GetLocID() == "novaras_black_diamond_arena":
                if self.progress == 0:
                    return TriggeredEvent("black_diamond_arena_firstEnter")

        def locationMod(self):
            btnMods = {}
            btnMods["btn_bkeeper_talk"] = BtnJumpLabel(_("Talk to Bookkeeper"), "black_diamond_bookkeeper_talk")
            return LocButtonMod(directMods = btnMods)

        def onMidnight(self):
            if GetGameDay() == self.resetDay:
                self.canBet = 1000
                self.resetDay = -1

        def placeBet(self, Amount):
            if self.resetDay == -1:
                self.resetDay = GetGameDay() + 6
            self.canBet -= Amount
            self.currBet = Amount
            PlayerRemItem("gold", Amount)
            
label black_diamond_arena_firstEnter:
    $ QstSetProgress(BlackDiamondArena, 1)
    #SCENE 3 - NEW LOCATION ADDED TO BLACK DIAMOND - UNDERGROUND MONSTER FIGHT ARENA 
    #Upon entering the Arena for the first time 
    'As I stumbled down the flight of stairs, I heard the bellowing roar of cheers and something snarling down below.'
    'Coming upon a great darkened underground Arena, men gathered around and cheered as two reptilian beasts slashed and tore at each other in the fight pit below.'
    'The one leapt and gripped the others throat with its teeth, ripping it out in a violent bloody display that the crowd roared with pleasure too.'
    MC '(What is this place?)'
    show cg_bandit at center_f
    with dissolve
    
    BOOKKEEPER 'Oi!'
    MC @surprised 'Huh?'
    BOOKKEEPER 'Zer are no freeloaders! Either place a bet, or fuck off!'
    MC @talk 'A bet?'
    BOOKKEEPER 'Iz stupid or something?'
    jump black_diamond_bookkeeper_talk

label black_diamond_bookkeeper_talk:
    show cg_bandit at center_f
    with dissolve
    if BlackDiamondArena().canBet < 50:
        BOOKKEEPER "No. You off limit. Come back in a few dayz."
        MC "Okay."
        $ LocEnter()
    BOOKKEEPER 'Beasts fight below, you bet.'
    BOOKKEEPER "Your beast wins, you get coin."
    BOOKKEEPER "Zat's it, you want bet?"
    menu black_diamond_bookkeeper_talk_menu:
        "I'd like to place a bet.":
            BOOKKEEPER 'How much?'
            menu:
                "50 coins." if PlayerItemQty("gold") >= 50 and BlackDiamondArena().canBet >= 50:
                    $ BlackDiamondArena().placeBet(50)
                "250 coins." if PlayerItemQty("gold") >= 250 and BlackDiamondArena().canBet >= 250:
                    $ BlackDiamondArena().placeBet(250)
                "500 coins." if PlayerItemQty("gold") >= 500 and BlackDiamondArena().canBet >= 500:
                    $ BlackDiamondArena().placeBet(500)
                "1000 coins." if PlayerItemQty("gold") >= 1000 and BlackDiamondArena().canBet >= 1000:
                    $ BlackDiamondArena().placeBet(1000)
                "On second thought...":
                    jump black_diamond_bookkeeper_talk_menu
            BOOKKEEPER 'Very good!'
            BOOKKEEPER 'Enjoy fight! Collect coin after if win!'
            jump black_diamond_arena_fight
        'What are the rules?':
            BOOKKEEPER 'Rules iz simple!'
            BOOKKEEPER 'You bet on either creature to win, first to kill zer other wins.'
            BOOKKEEPER 'Az newbie, you iz only able to bet one thousand coins a week.'
            BOOKKEEPER 'Coin pay upfront before bet go on.'
            MC @talk 'That seems odd, why the limit?'
            BOOKKEEPER 'Too many try cheat.'
            BOOKKEEPER 'One try poisoning a beasty and placing huge bet on other.'
            BOOKKEEPER 'Now, only trusted members can make big bets.'
            jump black_diamond_bookkeeper_talk_menu
        'No thanks.':
            BOOKKEEPER 'Than leave already!'
            $ LocEnter()

label black_diamond_arena_fight:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    play sound2 "audio/cfx/crowd_cheer_smaller.ogg"
    $ tmpvar = {}
    $ tmpvar["left"] = [{"e_lizardmonster":RngInt(9, 13)}]
    $ tmpvar["right"] = [{"e_lizardmonster":RngInt(9, 13)}]
    $ StartBattle(BattleData("pbat_tarbeck_tunnel", CharIDList_Left = tmpvar["left"], CharIDList_Right = tmpvar["right"], LeftSideForcedAIControl = True, ContinueOnDefeat = True, GrantXp = False, GiveLoot = False))
    $ tmpvar = {}
    scene black with dissolve
    $ LocFlush()
    with dissolve
    $ AutoMus(True)
    if LastBattleOutcome == "defeat":
        MC "(Damn... I lost.)"
    elif LastBattleOutcome == "victory":
        MC "(Well... That's wasn't the easiest thing to watch.)"
        MC "(Looks like I won though!)"
        $ PlayerAddItem("gold", BlackDiamondArena().currBet * 2)
    $ BlackDiamondArena().currBet = 0
    $ LocEnterQ()

