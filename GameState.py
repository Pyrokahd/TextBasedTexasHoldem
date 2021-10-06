import random
from PokerRules import PokerRules
from playerData import Player
from Cards import CardType
import Cards


class Gamestate():
    """
    The State of the Game in a given Moment
    """
    def __init__(self, player):
        """

        :param player: Player[], a list of all player classes
        """
        self.playerList = player
        self.playerCount = len(self.playerList)

        self.deckmanager = Cards.DeckManager()
        self.deck = self.deckmanager.deck
        self.tableCards = {"1": None, "2": None, "3": None, "4": None, "5": None}

        self.pot = 0


    def roundInitialization(self):
        # Blinds setzen
        randomPlayer = random.choice(self.playerList)
        randomPlayer.smallBlind = True

        bigBlindIndex = self.playerList.index(randomPlayer)+1  # im Uhrzeigersinn addieren = die playerList
        if bigBlindIndex > (len(self.playerList)-1):
            bigBlindIndex = 0
        self.playerList[bigBlindIndex].bigBlind = True

        for player in self.playerList:
            if player.smallBlind:
                print("small Blind set")
                player.money -= 1
                self.pot += 1
            if player.bigBlind:
                print("big Blind set")
                player.money -= 2
                self.pot += 2

        print("Give Cards")

        # Give Cards


