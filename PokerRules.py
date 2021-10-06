
from playerData import Player


class PokerRules():
    """ Takes a Gamestate and returns possible plays"""
    # : int is a hint which type is expected ...(self, pC: int, )
    def __init__(self, gamestate):
        self.gamestate = gamestate
        self.smallBlind = 1  # in € also int


    def getPossibleMovesForNextPlayer(self, gamestate):
        activeplayer = gamestate.playerList[gamestate.activePlayerIndex]
        # Der aktive spieler macht im Server einen Zug. Der Index wird im Gamestate aktualisiert
        # Gamestate kommrt
        # Der player vom aktiven Index+1 erhält geupdatete Regeln

        # in state and 1 player out rules for that player
        return None
        # self.gamestate.playerList[0].playMoves["Fold"] = False
        # Change possible Moves on all Player



## Flop
# erste runde links vom big blind fängt an
# plays Fold-aussteigen Call-mit Raise-erhöhen  (not check-schieben, set)  ...   # Bet = setzen am Anfang der Runde

# andern runden  der small blind fängt an
# Alle moves möglich
# wenn alle checken weiter.

# spieler mit letzter erhöhung oder setzung zeigt zuerst (sonst der small blind)
# alle blinds eins weiter rotieren dann neue runde