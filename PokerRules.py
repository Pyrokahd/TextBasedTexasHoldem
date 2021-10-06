
from playerData import Player


class PokerRules():
    """ Takes a Gamestate and returns possible plays"""
    # : int is a hint which type is expected ...(self, pC: int, )
    def __init__(self, gamestate):
        self.gamestate = gamestate
        self.smallBlind = 1  # in € also int


    def getPossibleMoves(self):
        # in state and 1 player out rules for that player
        return None
        # self.gamestate.playerList[0].playMoves["Fold"] = False
        # Change possible Moves on all Player