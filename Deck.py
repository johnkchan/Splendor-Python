from random import randint
from card import Card


class Deck:
    
    def __init__(self):
        self.__cards = []

    @staticmethod
    def initialize():
        tier1Data = [
            ["diamond", [0, 1, 1, 1, 1],  0], ["diamond", [0, 1, 2, 1, 1],  0], [
                "diamond", [0, 0, 0, 2, 1],  0], ["diamond", [0, 2, 0, 0, 2],  0],
            ["diamond", [0, 3, 0, 0, 0],  0], ["diamond", [0, 2, 2, 0, 1],  0], [
                "diamond", [3, 1, 0, 0, 1],  0], ["diamond", [0, 0, 4, 0, 0], 1],
            ["sapphire", [1, 0, 1, 1, 1],  0], ["sapphire", [1, 0, 1, 2, 1],  0], [
                "sapphire", [0, 1, 3, 1, 0],  0], ["sapphire", [1, 0, 2, 2, 0],  0],
            ["sapphire", [0, 0, 2, 0, 2],  0], ["sapphire", [1, 0, 0, 0, 2],  0], [
                "sapphire", [0, 0, 0, 0, 3],  0], ["sapphire", [0, 0, 0, 4, 0], 1],
            ["emerald", [1, 1, 0, 1, 1],  0], ["emerald", [1, 1, 0, 1, 2],  0], [
                "emerald", [1, 3, 1, 0, 0],  0], ["emerald", [0, 1, 0, 2, 2],  0],
            ["emerald", [0, 2, 0, 2, 0],  0], ["emerald", [2, 1, 0, 0, 0],  0], [
                "emerald", [0, 0, 0, 3, 0],  0], ["emerald", [0, 0, 0, 0, 4], 1],
            ["ruby", [1, 1, 1, 0, 1],  0], ["ruby", [2, 1, 1, 0, 1],  0], [
                "ruby", [1, 0, 0, 1, 3],  0], ["ruby", [2, 0, 0, 2, 0],  0],
            ["ruby", [0, 2, 1, 0, 0],  0], ["ruby", [3, 0, 0, 0, 0],  0], [
                "ruby", [2, 0, 1, 0, 2],  0], ["ruby", [4, 0, 0, 0, 0], 1],
            ["onyx", [1, 2, 1, 1, 0],  0], ["onyx", [1, 1, 1, 1, 0],  0], [
                "onyx", [0, 0, 1, 3, 1],  0], ["onyx", [2, 2, 0, 1, 0],  0],
            ["onyx", [2, 0, 2, 0, 0],  0], ["onyx", [0, 0, 2, 1, 0],  0], [
                "onyx", [0, 0, 3, 0, 0],  0], ["onyx", [0, 4, 0, 0, 0], 1]
        ]

        tier2Data = [
            ["diamond", [0, 0, 3, 2, 2], 1], ["diamond", [
                2, 3, 0, 3, 0], 1], ["diamond", [0, 0, 1, 4, 2], 2],
            ["diamond", [0, 0, 0, 5, 3], 2], ["diamond", [
                0, 0, 0, 5, 0], 2], ["diamond", [6, 0, 0, 0, 0], 3],
            ["sapphire", [0, 2, 2, 3, 0], 1], ["sapphire", [
                0, 2, 3, 0, 3], 1], ["sapphire", [2, 0, 0, 1, 4], 2],
            ["sapphire", [5, 3, 0, 0, 0], 2], ["sapphire", [
                0, 5, 0, 0, 0], 2], ["sapphire", [0, 6, 0, 0, 0], 3],
            ["emerald", [2, 3, 0, 0, 2], 1], ["emerald", [
                3, 0, 2, 3, 0], 1], ["emerald", [4, 2, 0, 0, 1], 2],
            ["emerald", [0, 5, 3, 0, 0], 2], ["emerald", [
                0, 5, 0, 0, 0], 2], ["emerald", [0, 0, 6, 0, 0], 3],
            ["ruby", [2, 0, 0, 2, 3], 1], ["ruby", [0, 3, 0, 2, 3], 1], [
                "ruby", [1, 4, 2, 0, 0], 2],
            ["ruby", [3, 0, 0, 0, 5], 2], ["ruby", [0, 0, 0, 0, 5], 2], [
                "ruby", [0, 0, 0, 6, 0], 3],
            ["onyx", [3, 2, 2, 0, 0], 1], ["onyx", [3, 0, 3, 0, 2], 1], [
                "onyx", [0, 1, 4, 2, 0], 2],
            ["onyx", [0, 0, 5, 3, 0], 2], [
                "onyx", [5, 0, 0, 0, 0], 2], ["onyx", [0, 0, 0, 0, 6], 3]
        ]

        tier3Data = [
            ["diamond", [0, 3, 3, 5, 3], 3], ["diamond", [3, 0, 0, 3, 6], 4], [
                "diamond", [0, 0, 0, 0, 7], 4], ["diamond", [3, 0, 0, 0, 7], 5],
            ["sapphire", [3, 0, 3, 3, 5], 3], ["sapphire", [6, 3, 0, 0, 3], 4], [
                "sapphire", [7, 0, 0, 0, 0], 4], ["sapphire", [7, 3, 0, 0, 0], 5],
            ["emerald", [5, 3, 0, 3, 3], 3], ["emerald", [3, 6, 3, 0, 0], 4], [
                "emerald", [0, 7, 0, 0, 0], 4], ["emerald", [0, 7, 3, 0, 0], 5],
            ["ruby", [3, 5, 3, 0, 3], 3], ["ruby", [0, 3, 6, 3, 0], 4], [
                "ruby", [0, 0, 7, 0, 0], 4], ["ruby", [0, 0, 7, 3, 0], 5],
            ["onyx", [3, 3, 5, 3, 0], 3], ["onyx", [0, 3, 0, 6, 3], 4], [
                "onyx", [0, 0, 0, 7, 0], 4], ["onyx", [0, 0, 0, 7, 3], 5]
        ]

        deckData = [tier1Data, tier2Data, tier3Data]
        decks = [Deck(), Deck(), Deck()]

        for i in range(len(decks)):
            for card in deckData[i]:
                decks[i].addCard(Card(card[0], card[1], card[2]))
            decks[i].shuffle

        return decks

    # Function adds single card object to self.__cards array 
    def addCard(self, card):
        self.__cards.append(card)
    
    # Function randomizes the position of the cards within self.__cards array
    def shuffle(self):
        cardCount = len(self.__cards)
        for i in range(cardCount):
            randNum = randint(0, cardCount - 1)
            temp = self.__cards[randNum]
            self.__cards[randNum] = self.__cards[i]
            self.__cards[i] = temp

    # Function removes last indexed card from self.__cards array and returns the card
    def draw(self):
        topCard = self.__cards.pop()
        return topCard
