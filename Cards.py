from enum import Enum
import random

class CardType(Enum):
    """
    Enum to display the types of cards possible
    """
    # TODO herausfinden wie das genau funktioniert wozu die zuweisung eines Wertes
    Kreuz = 0  # drei kugeln dinger
    Pik = 1  # schwarzes Herz
    Karo = 2  # Raute
    Herz = 3  # Herz


class BaseCard():
    """
    A Class representing a Card
    """
    def __init__(self, type, number):
        """
        Init a card
        :param type: CardType, which type of card ist it (Pik Karo Kreuz Herz)
        :param number: Int, which Value the Card has (1 is Ace, 11, 12 and 13 are Bube, Dame, König)
        """
        # Kreuz Pik Karo oder Herz
        self.type = type
        # 1(Ace),2,3,4,5,6,7,8,9,10,11(Bube), 12(Dame), 13(König)
        self.number = number


    def printCardStats(self):
        """
        prints the Type and Value of the Card
        :return:
        """
        number = self.number
        type = ""
        # Get Value
        if self.number == 1:
            number = "Ass"
        elif self.number == 11:
            number = "Bube"  # jack
        elif self.number == 12:
            number = "Dame"
        elif self.number == 13:
            number = "König"
        # Get Type
        if self.type == CardType.Kreuz:
            type = "Kreuz"
        elif self.type == CardType.Pik:
            type = "Pik"
        elif self.type == CardType.Karo:
            type = "Karo"
        elif self.type == CardType.Herz:
            type = "Herz"

        return f"[{type}|{number}]"


class DeckManager():
    def __init__(self):
        self.deck = self.__createDeck()
        #cardTypesArray = [CardType.Kreuz, CardType.Pik, CardType.Karo, CardType.Herz]
        #for type in cardTypesArray:
        #    for number in range(13):
        #        self.deck.append(BaseCard(type, number))

    def drawCard(self):
        """
        Draws a random card from the deck, removes it, and returns it
        :return:
        """
        card = random.choice(self.deck)
        self.deck.remove(card)
        print(f"new Decksize {len(self.deck)}")
        return card

    def __createDeck(self):
        deck = []
        cardTypesArray = [CardType.Kreuz, CardType.Pik, CardType.Karo, CardType.Herz]
        for type in cardTypesArray:
            for number in range(13):
                deck.append(BaseCard(type, number))
        return deck

    def printDeckSize(self):
        return str(len(self.deck))

    def printDeck(self):
        returnString = f""
        for card in self.deck:
            returnString += card.printCardStats() + "\n"
        return returnString






