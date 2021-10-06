from enum import Enum
import Cards
from Cards import CardType

# Das Enum is useless !
class PlayMoves(Enum):
    """
    An Enum with all possible moves a Player can do
    """
    Fold = True  # Passen
    Check = True  # Schieben
    Bet = True  # Setzen
    Call = True  # Mitgehen
    Raise = True  # Erhöhen


class Player():
    """
    A class representing a player with player specific Info (Cards, Money, Blinds)
    """
    def __init__(self, cards={"1": None, "2": None}, money=100, smallBlind=False, bigBlind=False ):
        """
        Init a player with optional starting Values
        :param cards: Dictonary, with 2 Cards from the Card class
        :param money: Int, the amount of money the player has
        :param smallBlind: Boolean, if the player is the smallBlind
        :param bigBlind: Boolean, if the player is the bigBlind
        """
        self.cards = cards
        self.money = money
        self.smallBlind = smallBlind
        self.bigBlind = bigBlind
        self.dealer = False  # no need i think
        # self.possibleMoves = [playMoves.Fold, playMoves.Check, playMoves.Bet, playMoves.Call, playMoves.Raise]
        self.playMoves = {"Fold": True, "Check": True, "Bet": True, "Call": True, "Raise": True}

