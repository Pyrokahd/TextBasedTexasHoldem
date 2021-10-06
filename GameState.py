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
        self.activePlayerIndex = 0

        self.deckmanager = Cards.DeckManager()
        # self.deck = self.deckmanager.deck  # todo delete ?

        self.roundPhase = 0  # 0 = vor dem flop, 1 = flop (3cards), 2 = turn(4cards), 3 = river(5cards), 4 = showdown(show cards)
        self.tableCards = {"1": None, "2": None, "3": None, "4": None, "5": None}

        self.pot = 0



    def roundInitialization(self):
        # Blinds setzen
        randomPlayer = random.choice(self.playerList)
        randomPlayer.smallBlind = True
        #self.activePlayerIndex = self.playerList.index(randomPlayer)

        bigBlindIndex = self.playerList.index(randomPlayer)+1  # im Uhrzeigersinn addieren = die playerList
        # wenn es der letze spieler ist, wieder bei 0 anfangen
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
        # draw cards for player
        for player in self.playerList:
            player.cards = {"1": self.deckmanager.drawCard(), "2": self.deckmanager.drawCard()}

    def getActivePlayerBasedOnPhase(self):
        if self.roundPhase == 0:
            # Get active player (the player after bigBlind in the first round)
            for player in self.playerList:
                if player.bigBlind:
                    # wenn der Index über die liste geht bei 0 anfangen
                    if self.playerList.index(player) + 1 > len(self.playerList)-1:
                        self.activePlayerIndex = 0
                    else:
                        self.activePlayerIndex = self.playerList.index(player) + 1
        elif self.roundPhase == 1:
            # TODO continue here
            return






