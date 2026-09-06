
init python:
    Barati_Players = {}
    Barati_Players["someplayer"] = {}

    # stuff to consider for BaratiPlayer:
    # max bet
    # min bet
    # how many games he can do today
    # how many he resets daily
    # daily reset code

default BaratiGame = None

###################################################################################################
# starts AND RESTARTS game
label barati_game_start:
    # hides screns in case they been shown
    hide screen Barati_DisplayCards
    hide screen Barati_PlayerNames
    hide screen Barati_BothRowScores
    hide screen Barati_ChooseActionButtons
    hide screen Barati_DebugInterface
    
    scene black
    with dissolve
    # reinit per-game vars:
    $ BaratiGame.RoundCurrent = 0
    $ BaratiGame.RoundVictories = {0:0, 1:0}
    $ BaratiGame.GameWinner = None
    # also clear player cards
    $ BaratiGame.PlayersCards = {0:{X:[] for X in range(BaratiGame.CardRows)}, 1:{X:[] for X in range(BaratiGame.CardRows)}}
    $ BaratiGame.StandingRows = {X:{Y:False for Y in range(BaratiGame.CardRows)} for X in range(2)}

    # show background board
    scene barati_game_board with dissolve # < - can probably change

    DEBUG "Barati game started"

    show screen Barati_DisplayCards()
    show screen Barati_PlayerNames()
    show screen Barati_DebugInterface()

    with dissolve

    # loop rounds
    while Barati_KeepGameGoing():
        hide screen Barati_BothRowScores
        hide screen Barati_ChooseActionButtons

        $ BaratiGame.RoundCurrent += 1
        DEBUG "Starting next round #[BaratiGame.RoundCurrent]"
        call barati_round_start from _call_barati_round_start
    DEBUG "Barati game over"

    $ Barati_EvaluateGameResults()

    if BaratiGame.GameWinner == 0:
        DEBUG "Left player won the game"
    elif BaratiGame.GameWinner == 1:
        DEBUG "Right player won the game"
    else:
        DEBUG "The game ends in a draw"

    $ Barati_PayOrLoseVictoryGold()

    hide screen Barati_DisplayCards
    hide screen Barati_PlayerNames
    hide screen Barati_BothRowScores
    hide screen Barati_ChooseActionButtons
    hide screen Barati_DebugInterface
    scene black
    with dissolve

    $ Pause(0.25)
    return

label barati_round_start:
    # reset per-round vars
    # reshuffle deck

    ### dynamic per-round vars
    $ BaratiGame.RoundWinner = None
    $ BaratiGame.ActiveSide = 0
    $ BaratiGame.PlayersCards = {0:{X:[] for X in range(BaratiGame.CardRows)}, 1:{X:[] for X in range(BaratiGame.CardRows)}}
    $ BaratiGame.CurrentDeck = BaratiGame.BaseDeck.copy()
    $ BaratiGame.StandingRows = {X:{Y:False for Y in range(BaratiGame.CardRows)} for X in range(2)}
    $ BaratiGame.SideHadNoActions = {0: False, 1: False}

    $ renpy.random.shuffle(BaratiGame.CurrentDeck)

    DEBUG "Round [BaratiGame.RoundCurrent] starts"
    # draw starting 2 cards for each row
    $ Barati_DrawStartingCardsForBothPlayers()
    with None

    # per-round yep
    show screen Barati_BothRowScores()

    while Barati_KeepRoundGoing():
        $ BaratiGame.ActiveSide = 0
        while BaratiGame.ActiveSide < 2:
            if Barati_SideCanAct(BaratiGame.ActiveSide):
                if BaratiGame.ActiveSide == 0:
                    DEBUG "left player turn"
                else:
                    DEBUG "right player turn"
                if BaratiGame.ActiveSide == 0:
                    call screen Barati_ChooseActionButtons(BaratiGame.ActiveSide, True)
                    show screen Barati_ChooseActionButtons(BaratiGame.ActiveSide)
                else:
                    $ Barati_DoAITurn(BaratiGame.ActiveSide)
            else:
                if BaratiGame.ActiveSide == 0:
                    DEBUG "(no actions available for left side)"
                else:
                    DEBUG "(no actions available for right side)"

            $ BaratiGame.ActiveSide += 1

    $ Barati_EvaluateRoundResults()
    DEBUG "round over"
    if BaratiGame.RoundWinner == 2:
        DEBUG "it's a draw!"
    if BaratiGame.RoundWinner == 0:
        DEBUG "left player won"
    if BaratiGame.RoundWinner == 1:
        DEBUG "right player won"
    return

init python:
    BaratiGame = None # if not none, we're in a barati game
    Barati_LastGameResult = None
    
    class BaratiGameClass:
        def __init__(self, OpponentID, BetGoldAmt):
            ### constant vars
            # card constants
            self.BaseDeck = [x for x in range(1, 12)] * 3
            self.CardRows = 1
            # rounds limit
            self.MaxRounds = 8
            # display positions
            self.RowXPos = 0.2
            self.RowYPos = 0.25
            self.RowPositions = {
                0:{
                    0:(self.RowXPos, self.RowYPos * 2),
                    1:(self.RowXPos, self.RowYPos),
                    2:(self.RowXPos, self.RowYPos * 3),
                },
            }
            self.RowPositions[1] = {}
            # calc mirror positions
            for RowIndex, RowPosition in self.RowPositions[0].items():
                NewPosX = 1.0 - RowPosition[0]
                NewPosY = RowPosition[1]
                self.RowPositions[1][RowIndex] = (NewPosX, NewPosY)

            self.BetGoldAmt = BetGoldAmt

            ### dynamic per-game vars
            self.RoundCurrent = 0
            # playerID, victories
            self.RoundVictories = {0:0, 1:0}
            self.GameWinner = None # 0 or 1 or 2 (2 is draw but its impossibru)

            ### dynamic per-round vars
            self.ActiveSide = 0
            self.PlayersCards = {0:{X:[] for X in range(self.CardRows)}, 1:{X:[] for X in range(self.CardRows)}}
            self.CurrentDeck = self.BaseDeck.copy()
            self.StandingRows = {X:{Y:False for Y in range(self.CardRows)} for X in range(2)}
            # when during 1 turn (left -> right players) both sides cant act, its considered game over
            self.SideHadNoActions = {0: False, 1: False}
            # 0-1 winning sides, 2 for draw
            self.RoundWinner = None

    def Barati_GameStartPopup(OpponentID):
        renpy.call_screen("Barati_BetPopup", OpponentID, _with_none = False)
        renpy.with_statement(Dissolve(0.25))
        return

    def Barati_GameStart(OpponentID, BetGoldAmt = None):
        global BaratiGame
        BaratiGame = BaratiGameClass(OpponentID, BetGoldAmt)
        renpy.jump("barati_game_start")
        return

    def Barati_PayOrLoseVictoryGold():
        if BaratiGame.BetGoldAmt == None:
            return
        if BaratiGame.GameWinner == 0:
            renpy.say(who = None, what = "you won %s (not really yet)" % BaratiGame.BetGoldAmt)
        elif BaratiGame.GameWinner == 1:
            renpy.say(who = None, what = "you lost %s (not really yet)" % BaratiGame.BetGoldAmt)
        return

    def Barati_DrawCard(Side = 0, Row = 0):
        BaratiGame.PlayersCards[Side][Row].append(BaratiGame.CurrentDeck.pop())
        return        
    
    def Barati_DoAITurn(Side = 0):
        # first gather all rows we can "hit" or "stand"
        RowsToActUpon = []
        for RowIndex in range(BaratiGame.CardRows):
            if Barati_RowCanBeHit(Side, RowIndex):
                RowsToActUpon.append(RowIndex)

        if len(RowsToActUpon) == 0:
            return

        # then decide action, hit or stand
        RowToActUpon = renpy.random.choice(RowsToActUpon)
        RowScore = Barati_GetRawRowScore(Side, RowToActUpon)

        # initially, "hit" is the no-brain action
        Doubt = 0.0

        OpposingSide = (1 if Side == 0 else 0)
        # if enemy side of target row is standing
        if BaratiGame.StandingRows[OpposingSide][RowToActUpon]:
            # if its higher than us, 100% hit (we guaranteed lose if we dont)
            if Barati_GetRawRowScore(OpposingSide, RowToActUpon) > RowScore:
                Doubt = 0.0
            # if its lower than us and stands, dont hit (it's unnecessary to act)
            elif Barati_GetRawRowScore(OpposingSide, RowToActUpon) < RowScore:
                Doubt = 1.0
            # if equal, calc doubt
            else:
                Doubt = max((RowScore - 10) / 11, 0)
        # if enemy side of target row is NOT standing
        else:
            # if its over us, push
            if Barati_GetRawRowScore(OpposingSide, RowToActUpon) > RowScore:
                Doubt = 0.0
            else:
                # just calc doubt
                # get "doubt" value: 0 until 11, starting from 12 to 20 it should be goin towards 1.0
                Doubt = max((RowScore - 10) / 11, 0)
    
        # final hit or stand 
        if RngFloat(0.0, 1.0) > Doubt:
            Barati_HitRow(Side, RowToActUpon)
        else:
            Barati_StandRow(Side, RowToActUpon)
        return

    def Barati_DrawStartingCardsForBothPlayers():
        for Side in range(2):
            for RowIndex in range(BaratiGame.CardRows):
                Barati_DrawCard(Side = Side, Row = RowIndex)
                Barati_DrawCard(Side = Side, Row = RowIndex)

    def Barati_CheckWhetherRowIsBusted(Side, Row):
        if Barati_GetRawRowScore(Side, Row) > 21:
            return True
        return False

    def Barati_EvaluateGameResults():
        if BaratiGame.RoundVictories[0] > BaratiGame.RoundVictories[1]:
            # mc won
            BaratiGame.GameWinner = 0
        elif BaratiGame.RoundVictories[1] > BaratiGame.RoundVictories[0]:
            # mc lost
            BaratiGame.GameWinner = 1
        else:
            # draw (IMPOSSIBLE?)
            BaratiGame.GameWinner = 2
        return 

    def Barati_EvaluateRoundResults():
        RowScores = {
            0:{X:0 for X in range(BaratiGame.CardRows)},
            1:{X:0 for X in range(BaratiGame.CardRows)}}
        WonRows = {0:0, 1:0}

        ### calculate row scores
        for Side in range(2):
            for RowIndex in range(BaratiGame.CardRows):
                RowScores[Side][RowIndex] = Barati_GetEvaluatedRowScore(Side, RowIndex)

        ### figure out how many rows a player has won over another
        for PlayerIndex in range(2):
            OpponentIndex = (1 if PlayerIndex == 0 else 0)
            for RowIndex in range(BaratiGame.CardRows):
                # skip busted row
                if Barati_CheckWhetherRowIsBusted(PlayerIndex, RowIndex):
                    continue
                else:
                    ThisRowScore = Barati_GetEvaluatedRowScore(PlayerIndex, RowIndex)
                    OpposingRowScore = Barati_GetEvaluatedRowScore(OpponentIndex, RowIndex)
                    if ThisRowScore > OpposingRowScore:
                        WonRows[PlayerIndex] += 1

        ### figure out round winner
        # draw
        if WonRows[0] == WonRows[1]:
            BaratiGame.RoundWinner = 2
            return
        # player 0 wins,
        elif WonRows[0] > WonRows[1]:
            BaratiGame.RoundVictories[0] += 1
            BaratiGame.RoundWinner = 0
            return
        # player 1 wins
        else:
            BaratiGame.RoundVictories[1] += 1
            BaratiGame.RoundWinner = 1
            return

    # same as other one but 0 if over 21
    def Barati_GetEvaluatedRowScore(Side, Row):
        Score = Barati_GetRawRowScore(Side, Row)
        if Score > 21:
            return 0
        else:
            return Score
    
    def Barati_GetRawRowScore(Side, Row):
        RowSum = 0
        Aces = 0
        for CardValue in BaratiGame.PlayersCards[Side][Row]:
            # only eval "normal" cards whose value is within 1 to 11
            if 1 <= CardValue <= 10:
                RowSum += CardValue
            if CardValue == 11:
                Aces += 1

        for Ace in range(Aces):
            if RowSum < 11:
                RowSum += 11
            else:
                RowSum += 1

        return RowSum
    
    def Barati_KeepGameGoing():
        # if round number is over max, game over
        if BaratiGame.RoundCurrent >= BaratiGame.MaxRounds:
            return False

        # if one player is away in victories, game over
        BestOfThreshold = int(BaratiGame.MaxRounds / 2) + 1
        if BaratiGame.RoundVictories[0] >= BestOfThreshold or BaratiGame.RoundVictories[1] >= BestOfThreshold:
            return False

        return True

    def Barati_KeepRoundGoing():
        if BaratiGame.SideHadNoActions[0] and BaratiGame.SideHadNoActions[1]:
            return False
        return True

    def Barati_RowCanBeStand(Side, Row):
        if BaratiGame.StandingRows[Side][Row]:
            return False
        if Barati_GetRawRowScore(Side, Row) > 20:
            return False
        return True

    def Barati_StandRow(Side = 0, RowIndex = 0):
        BaratiGame.StandingRows[Side][RowIndex] = True
        return

    def Barati_RowCanBeHit(Side, Row):
        if BaratiGame.StandingRows[Side][Row]:
            return False
        if Barati_GetRawRowScore(Side, Row) < 21:
            return True

    def Barati_HitRow(Side, Row):
        Barati_DrawCard(Side = Side, Row = Row)
        return

    def Barati_SideCanAct(Side):
        # if all enemy rows are bust, we cant
        OpposingSide = (1 if Side == 0 else 0)
        BustedOpponentRows = 0
        for RowIndex in range(BaratiGame.CardRows):
            if Barati_CheckWhetherRowIsBusted(OpposingSide, RowIndex):
                BustedOpponentRows += 1
            if BustedOpponentRows == BaratiGame.CardRows:
                BaratiGame.SideHadNoActions[Side] = True
                return False

        # for each row, if enemy row stands and our corresp. row is higher, we cant
        WonNonStandingRows = 0
        for RowIndex in range(BaratiGame.CardRows):
            if BaratiGame.StandingRows[OpposingSide][RowIndex]:
                if Barati_GetEvaluatedRowScore(Side, RowIndex) > Barati_GetEvaluatedRowScore(OpposingSide, RowIndex):
                    WonNonStandingRows += 1
            if WonNonStandingRows == BaratiGame.CardRows:
                BaratiGame.SideHadNoActions[Side] = True
                return False

        # if any row in this side can be hit or stand, we can act
        for RowIndex in BaratiGame.PlayersCards[Side]:
            if Barati_RowCanBeHit(Side, RowIndex):
                return True
            if Barati_RowCanBeStand(Side, RowIndex):
                return True

        BaratiGame.SideHadNoActions[Side] = True
        return False

    def IsPlayerInBaratiGame():
        if BaratiGame is not None:
            return True
        return False


    Barati_CardSprites = {
        1:"images/card_game/cards/1.webp",
        2:"images/card_game/cards/2.webp",
        3:"images/card_game/cards/3.webp",
        4:"images/card_game/cards/4.webp",
        5:"images/card_game/cards/5.webp",
        6:"images/card_game/cards/6.webp",
        7:"images/card_game/cards/7.webp",
        8:"images/card_game/cards/8.webp",
        9:"images/card_game/cards/9.webp",
        10:"images/card_game/cards/10.webp",
        11:"images/card_game/cards/x.webp",
        # test special
        666:"images/card_game/cards/x.webp",
    }

screen Barati_BothRowScores():
    use Barati_RowScoresAndStatus(0)
    use Barati_RowScoresAndStatus(1)

screen Barati_PlayerNames():
    vbox:
        anchor (0.5, 0.5)
        pos BaratiGame.RowPositions[0][0]
        yoffset -220
        label "Caspian" text_size 50 xalign 0.5
        if BaratiGame.RoundVictories[0] > 0:
            text "Won rounds: %s" % BaratiGame.RoundVictories[0] size 40 xalign 0.5
    vbox:
        anchor (0.5, 0.5)
        pos BaratiGame.RowPositions[1][0]
        yoffset -220
        label "SomeOtherPlayer" text_size 50 xalign 0.5
        if BaratiGame.RoundVictories[1] > 0:
            text "Won rounds: %s" % BaratiGame.RoundVictories[1] size 40 xalign 0.5

screen Barati_RowScoresAndStatus(Side):
    for RowIndex in BaratiGame.PlayersCards[Side]:
        vbox:
            pos BaratiGame.RowPositions[Side][RowIndex]
            yoffset 75
            if Side == 0:
                anchor (0.0, 1.0)
                xoffset 140
            else:
                anchor (1.0, 1.0)
                xoffset -140
            if Barati_GetRawRowScore(Side, RowIndex) > 21:
                textbutton "Bust!"
            elif BaratiGame.StandingRows[Side][RowIndex]:
                textbutton "Stands"
            textbutton "Score: %s" % Barati_GetRawRowScore(Side, RowIndex) 

screen Barati_ChooseActionButtons(Side = 0, Actions = False):
    for RowIndex in BaratiGame.PlayersCards[Side]:
        vbox:
            anchor (0.0, 0.5)
            pos BaratiGame.RowPositions[Side][RowIndex]
            xoffset 140
            hbox:
                if Barati_RowCanBeHit(Side, RowIndex):
                    textbutton "%s) Hit" % (RowIndex + 1):
                        if Actions:
                            action [Function(Barati_HitRow, Side = Side, Row = RowIndex), Return()] 
                        keysym "%s" % (RowIndex + 1)

                if Barati_RowCanBeStand(Side, RowIndex):
                    textbutton "%s) Stand" % (RowIndex + 4):
                        if Actions:
                            action [Function(Barati_StandRow, Side = Side, RowIndex = RowIndex), Return()] 
                        keysym "%s" % (RowIndex + 4)
    hbox:
        align (0.5, 1.0)
        textbutton "specials":
            xoffset 1
            #if Actions:
                #action NullAction()

screen Barati_DebugInterface():
    textbutton "DEV: restart game":
        anchor (1.0, 1.0)
        pos (1.0, 1.0)
        action Jump("barati_game_start")

screen Barati_DisplayCards():
    # player side
    for RowIndex in range(len(BaratiGame.PlayersCards[0])):
        use Barati_CardsRow(0, RowIndex)
    # opponent side
    for RowIndex in range(len(BaratiGame.PlayersCards[1])):
        use Barati_CardsRow(1, RowIndex)
    # deck
    vbox:
        anchor (0.5, 1.0)
        pos (0.5, 0.25)
        add "images/card_game/cards/back.webp" ysize 250 fit "contain" xalign 0.5
        text "x%s" % len(BaratiGame.CurrentDeck) xalign 0.5 text_align 0.5 size 45
        null height 25
        if BaratiGame.RoundCurrent > 0:
            text _("Round %s/%s") % (BaratiGame.RoundCurrent, BaratiGame.MaxRounds) xalign 0.5 size 40
        else:
            text "" size 40

screen Barati_CardsRow(Side, RowIndex):
    hbox:
        anchor (0.5, 0.5)
        pos BaratiGame.RowPositions[Side][RowIndex]
        spacing 15 + (-20 * (len(BaratiGame.PlayersCards[Side][RowIndex]) - 2))
        for Card in BaratiGame.PlayersCards[Side][RowIndex]:
            add Barati_CardSprites[Card] ysize 250 fit "contain"

screen Barati_BetPopup(OpponentID):
    default ChosenBet = 10
    frame:
        align (0.5, 0.5)
        vbox:
            align (0.5, 0.5)
            label "SomeOpponentName"
            text "games they can play today: %s" % 3
            text "min bet: %s" % 10
            text "max bet: %s" % 100
            text "your bet: %s" % ChosenBet
            hbox:
                for BetVal in [10, 20, 30, 40, 50, 100]:
                    textbutton "%s" % BetVal action SetScreenVariable("ChosenBet", BetVal)
            hbox:
                textbutton "Cancel" action Return()
                textbutton "Play" action [Hide("Barati_BetPopup", transition = Dissolve(0.25)), Function(Barati_GameStart, OpponentID, BetGoldAmt = ChosenBet)]
            
