from random import randint

class Deck:

    def __init__(self):
        self.__cards = []

    def addCard(self, card):
        self.__cards.append(card)
    
    def shuffle(self):
        cardCount = len(self.__cards)

        for i in range(cardCount):
            randNum = randint(0, cardCount - 1)
            temp = self.__cards[randNum]
            self.__cards[randNum] = self.__cards[i]
            self.__cards[i] = temp

    def draw(self):
        topCard = self.__cards.pop()
        return topCard