init python:
    Barati_Players = {}
    Barati_Players["someplayer"] = {
        "max_bet": 100,
        "min_bet": 10,
        "games_today": 3
    }

label barati_game_start:
    hide screen Barati_DisplayCards
    hide screen Barati_PlayerNames
    hide screen Barati_BothRowScores
    hide screen Barati_ChooseActionButtons
    hide screen Barati_DebugInterface
    
    scene black with dissolve

    $ BaratiGame.RoundCurrent = 0
    $ BaratiGame.RoundVictories = {0: 0, 1: 0}
    $ BaratiGame.GameWinner = None
    $ BaratiGame.PlayersCards = {0: {X: [] for X in range(BaratiGame.CardRows)}, 1: {X: [] for X in range(BaratiGame.CardRows)}}
    $ BaratiGame.StandingRows = {X: {Y: False for Y in range(BaratiGame.CardRows)} for X in range(2)}

    scene barati_game_board with dissolve

    "[DEBUG] Barati game started"

    show screen Barati_DisplayCards()
    show screen Barati_PlayerNames()
    show screen Barati_DebugInterface()

    with dissolve

    while Barati_KeepGameGoing():
        hide screen Barati_BothRowScores
        hide screen Barati_ChooseActionButtons

        $ BaratiGame.RoundCurrent += 1
        "[DEBUG] Starting next round #[BaratiGame.RoundCurrent]"
        call barati_round_start from _call_barati_round_start

    "[DEBUG] Barati game over"

    $ Barati_EvaluateGameResults()

    if BaratiGame.GameWinner == 0:
        "[DEBUG] Left player won the game"
    elif BaratiGame.GameWinner == 1:
        "[DEBUG] Right player won the game"
    else:
        "[DEBUG] The game ends in a draw"

    $ Barati_PayOrLoseVictoryGold()

    hide screen Barati_DisplayCards
    hide screen Barati_PlayerNames
    hide screen Barati_BothRowScores
    hide screen Barati_ChooseActionButtons
    hide screen Barati_DebugInterface
    scene black with dissolve

    $ renpy.pause(0.25)
    return


label barati_round_start:
    $ BaratiGame.RoundWinner = None
    $ BaratiGame.ActiveSide = 0
    $ BaratiGame.PlayersCards = {0: {X: [] for X in range(BaratiGame.CardRows)}, 1: {X: [] for X in range(BaratiGame.CardRows)}}
    $ BaratiGame.CurrentDeck = BaratiGame.BaseDeck.copy()
    $ BaratiGame.StandingRows = {X: {Y: False for Y in range(BaratiGame.CardRows)} for X in range(2)}
    $ BaratiGame.SideHadNoActions = {0: False, 1: False}

    $ renpy.random.shuffle(BaratiGame.CurrentDeck)

    "[DEBUG] Round [BaratiGame.RoundCurrent] starts"
    $ Barati_DrawStartingCardsForBothPlayers()
    with None

    show screen Barati_BothRowScores()

    while Barati_KeepRoundGoing():
        $ BaratiGame.ActiveSide = 0
        while BaratiGame.ActiveSide < 2:
            if Barati_SideCanAct(BaratiGame.ActiveSide):
                if BaratiGame.ActiveSide == 0:
                    "[DEBUG] Left player turn"
                    call screen Barati_ChooseActionButtons(BaratiGame.ActiveSide, True)
                    show screen Barati_ChooseActionButtons(BaratiGame.ActiveSide)
                else:
                    "[DEBUG] Right player turn"
                    $ Barati_DoAITurn(BaratiGame.ActiveSide)
            else:
                if BaratiGame.ActiveSide == 0:
                    "[DEBUG] (no actions available for left side)"
                else:
                    "[DEBUG] (no actions available for right side)"

            $ BaratiGame.ActiveSide += 1

    $ Barati_EvaluateRoundResults()
    "[DEBUG] Round over"
    if BaratiGame.RoundWinner == 2:
        "[DEBUG] It's a draw!"
    elif BaratiGame.RoundWinner == 0:
        "[DEBUG] Left player won"
    elif BaratiGame.RoundWinner == 1:
        "[DEBUG] Right player won"
    return


init python:
    BaratiGame = None
    Barati_LastGameResult = None
    
    class BaratiGameClass:
        def __init__(self, OpponentID, BetGoldAmt):
            self.BaseDeck = [x for x in range(1, 12)] * 3
            self.CardRows = 1
            self.MaxRounds = 8
            self.RowXPos = 0.2
            self.RowYPos = 0.25
            self.RowPositions = {
                0: {
                    0: (self.RowXPos, self.RowYPos * 2),
                    1: (self.RowXPos, self.RowYPos),
                    2: (self.RowXPos, self.RowYPos * 3),
                },
                1: {}
            }
            for RowIndex, RowPosition in self.RowPositions[0].items():
                NewPosX = 1.0 - RowPosition[0]
                NewPosY = RowPosition[1]
                self.RowPositions[1][RowIndex] = (NewPosX, NewPosY)

            self.BetGoldAmt = BetGoldAmt
            self.RoundCurrent = 0
            self.RoundVictories = {0: 0, 1: 0}
            self.GameWinner = None
            self.ActiveSide = 0
            self.PlayersCards = {0: {X: [] for X in range(self.CardRows)}, 1: {X: [] for X in range(self.CardRows)}}
            self.CurrentDeck = self.BaseDeck.copy()
            self.StandingRows = {X: {Y: False for Y in range(self.CardRows)} for X in range(2)}
            self.SideHadNoActions = {0: False, 1: False}
            self.RoundWinner = None

    def Barati_GameStartPopup(OpponentID):
        renpy.call_screen("Barati_BetPopup", OpponentID, _with_none=False)
        renpy.with_statement(Dissolve(0.25))

    def Barati_GameStart(OpponentID, BetGoldAmt=None):
        store.BaratiGame = BaratiGameClass(OpponentID, BetGoldAmt)
        renpy.jump("barati_game_start")

    def Barati_PayOrLoseVictoryGold():
        if store.BaratiGame.BetGoldAmt is None:
            return
        if BaratiGame.GameWinner == 0:
            renpy.say(None, f"You won {store.BaratiGame.BetGoldAmt} gold!")
        elif BaratiGame.GameWinner == 1:
            renpy.say(None, f"You lost {store.BaratiGame.BetGoldAmt} gold!")

    def Barati_DrawCard(Side=0, Row=0):
        if BaratiGame.CurrentDeck:
            BaratiGame.PlayersCards[Side][Row].append(BaratiGame.CurrentDeck.pop())

    def Barati_DoAITurn(Side=0):
        RowsToActUpon = [r for r in range(BaratiGame.CardRows) if Barati_RowCanBeHit(Side, r) or Barati_RowCanBeStand(Side, r)]
        if not RowsToActUpon:
            return

        RowToActUpon = renpy.random.choice(RowsToActUpon)
        RowScore = Barati_GetRawRowScore(Side, RowToActUpon)
        OpposingSide = 1 if Side == 0 else 0

        Doubt = 0.0
        if BaratiGame.StandingRows[OpposingSide][RowToActUpon]:
            if Barati_GetRawRowScore(OpposingSide, RowToActUpon) > RowScore:
                Doubt = 0.0
            elif Barati_GetRawRowScore(OpposingSide, RowToActUpon) < RowScore:
                Doubt = 1.0
            else:
                Doubt = max((RowScore - 10) / 11.0, 0.0)
        else:
            if Barati_GetRawRowScore(OpposingSide, RowToActUpon) > RowScore:
                Doubt = 0.0
            else:
                Doubt = max((RowScore - 10) / 11.0, 0.0)

        if renpy.random.random() > Doubt and Barati_RowCanBeHit(Side, RowToActUpon):
            Barati_HitRow(Side, RowToActUpon)
        elif Barati_RowCanBeStand(Side, RowToActUpon):
            Barati_StandRow(Side, RowToActUpon)

    def Barati_DrawStartingCardsForBothPlayers():
        for Side in range(2):
            for RowIndex in range(BaratiGame.CardRows):
                Barati_DrawCard(Side=Side, Row=RowIndex)
                Barati_DrawCard(Side=Side, Row=RowIndex)

    def Barati_CheckWhetherRowIsBusted(Side, Row):
        return Barati_GetRawRowScore(Side, Row) > 21

    def Barati_EvaluateGameResults():
        if BaratiGame.RoundVictories[0] > BaratiGame.RoundVictories[1]:
            BaratiGame.GameWinner = 0
        elif BaratiGame.RoundVictories[1] > BaratiGame.RoundVictories[0]:
            BaratiGame.GameWinner = 1
        else:
            BaratiGame.GameWinner = 2

    def Barati_EvaluateRoundResults():
        WonRows = {0: 0, 1: 0}

        for PlayerIndex in range(2):
            OpponentIndex = 1 if PlayerIndex == 0 else 0
            for RowIndex in range(BaratiGame.CardRows):
                if Barati_CheckWhetherRowIsBusted(PlayerIndex, RowIndex):
                    continue
                ThisRowScore = Barati_GetEvaluatedRowScore(PlayerIndex, RowIndex)
                OpposingRowScore = Barati_GetEvaluatedRowScore(OpponentIndex, RowIndex)
                if ThisRowScore > OpposingRowScore:
                    WonRows[PlayerIndex] += 1

        if WonRows[0] == WonRows[1]:
            BaratiGame.RoundWinner = 2
        elif WonRows[0] > WonRows[1]:
            BaratiGame.RoundVictories[0] += 1
            BaratiGame.RoundWinner = 0
        else:
            BaratiGame.RoundVictories[1] += 1
            BaratiGame.RoundWinner = 1

    def Barati_GetEvaluatedRowScore(Side, Row):
        Score = Barati_GetRawRowScore(Side, Row)
        return 0 if Score > 21 else Score

    def Barati_GetRawRowScore(Side, Row):
        RowSum = 0
        Aces = 0
        for CardValue in BaratiGame.PlayersCards[Side][Row]:
            if 1 <= CardValue <= 10:
                RowSum += CardValue
            elif CardValue == 11:
                Aces += 1

        for _ in range(Aces):
            if RowSum + 11 <= 21:
                RowSum += 11
            else:
                RowSum += 1

        return RowSum

    def Barati_KeepGameGoing():
        if BaratiGame.RoundCurrent >= BaratiGame.MaxRounds:
            return False
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

    def Barati_StandRow(Side=0, RowIndex=0):
        BaratiGame.StandingRows[Side][RowIndex] = True

    def Barati_RowCanBeHit(Side, Row):
        if BaratiGame.StandingRows[Side][Row]:
            return False
        return Barati_GetRawRowScore(Side, Row) < 21

    def Barati_HitRow(Side, Row):
        Barati_DrawCard(Side=Side, Row=Row)

    def Barati_SideCanAct(Side):
        OpposingSide = 1 if Side == 0 else 0
        BustedOpponentRows = sum(1 for r in range(BaratiGame.CardRows) if Barati_CheckWhetherRowIsBusted(OpposingSide, r))
        
        if BustedOpponentRows == BaratiGame.CardRows:
            BaratiGame.SideHadNoActions[Side] = True
            return False

        for RowIndex in range(BaratiGame.CardRows):
            if Barati_RowCanBeHit(Side, RowIndex) or Barati_RowCanBeStand(Side, RowIndex):
                return True

        BaratiGame.SideHadNoActions[Side] = True
        return False

    def IsPlayerInBaratiGame():
        return store.BaratiGame is not None


    Barati_CardSprites = {
        1: "images/card_game/cards/1.webp",
        2: "images/card_game/cards/2.webp",
        3: "images/card_game/cards/3.webp",
        4: "images/card_game/cards/4.webp",
        5: "images/card_game/cards/5.webp",
        6: "images/card_game/cards/6.webp",
        7: "images/card_game/cards/7.webp",
        8: "images/card_game/cards/8.webp",
        9: "images/card_game/cards/9.webp",
        10: "images/card_game/cards/10.webp",
        11: "images/card_game/cards/x.webp",
        666: "images/card_game/cards/x.webp",
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
            text f"Won rounds: {BaratiGame.RoundVictories[0]}" size 40 xalign 0.5
    vbox:
        anchor (0.5, 0.5)
        pos BaratiGame.RowPositions[1][0]
        yoffset -220
        label "Opponent" text_size 50 xalign 0.5
        if BaratiGame.RoundVictories[1] > 0:
            text f"Won rounds: {BaratiGame.RoundVictories[1]}" size 40 xalign 0.5


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
            textbutton f"Score: {Barati_GetRawRowScore(Side, RowIndex)}"


screen Barati_ChooseActionButtons(Side=0, Actions=False):
    for RowIndex in BaratiGame.PlayersCards[Side]:
        vbox:
            anchor (0.0, 0.5)
            pos BaratiGame.RowPositions[Side][RowIndex]
            xoffset 140
            hbox:
                if Barati_RowCanBeHit(Side, RowIndex):
                    textbutton f"{RowIndex + 1}) Hit":
                        if Actions:
                            action [Function(Barati_HitRow, Side=Side, Row=RowIndex), Return()]
                        keysym str(RowIndex + 1)

                if Barati_RowCanBeStand(Side, RowIndex):
                    textbutton f"{RowIndex + 4}) Stand":
                        if Actions:
                            action [Function(Barati_StandRow, Side=Side, RowIndex=RowIndex), Return()]
                        keysym str(RowIndex + 4)


screen Barati_DebugInterface():
    textbutton "DEV: restart game":
        anchor (1.0, 1.0)
        pos (1.0, 1.0)
        action Jump("barati_game_start")


screen Barati_DisplayCards():
    for RowIndex in range(len(BaratiGame.PlayersCards[0])):
        use Barati_CardsRow(0, RowIndex)
    for RowIndex in range(len(BaratiGame.PlayersCards[1])):
        use Barati_CardsRow(1, RowIndex)
    vbox:
        anchor (0.5, 1.0)
        pos (0.5, 0.25)
        add "images/card_game/cards/back.webp" ysize 250 fit "contain" xalign 0.5
        text f"x{len(BaratiGame.CurrentDeck)}" xalign 0.5 text_align 0.5 size 45
        null height 25
        if BaratiGame.RoundCurrent > 0:
            text f"Round {BaratiGame.RoundCurrent}/{BaratiGame.MaxRounds}" xalign 0.5 size 40


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
            text "Games they can play today: 3"
            text "Min bet: 10"
            text "Max bet: 100"
            text f"Your bet: {ChosenBet}"
            hbox:
                for BetVal in [10, 20, 30, 40, 50, 100]:
                    textbutton str(BetVal) action SetScreenVariable("ChosenBet", BetVal)
            hbox:
                textbutton "Cancel" action Return()
                textbutton "Play" action [Hide("Barati_BetPopup", transition=Dissolve(0.25)), Function(Barati_GameStart, OpponentID, BetGoldAmt=ChosenBet)]