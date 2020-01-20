from random import randint
from Card import Card
from Deck import Deck
from Noble import Noble
from Player import Player

class Game:
    
    def __init__(self):
        self.__players = []
        self.__nobles = []
        self.__decks = []
        self.__table = []
        self.__gemTokens = {
            "diamond": 0,
            "sapphire": 0,
            "emerald": 0,
            "ruby": 0,
            "onyx": 0,
            "gold joker": 0
        }
        self.initializeGame()

    def initializeGame(self):
        self.initalizePlayers()
        self.initalizeNobles()
        self.initalizeTokens()
        self.initializeDeck()
        self.initializeTable()
        self.displayGemTokens()
        # self.play()

    # Determine how many players are playing
    def initalizePlayers(self):
        playerCount = input("How many players? Please Enter 1, 2, 3, 4: ")
        for i in range(int(playerCount)):
            self.__players.append(Player(i + 1))

    # Generate nobles per amount of players
    def initalizeNobles(self):
        nobleData = [ 
            [ 4, 4, 0, 0, 0 ], [ 0, 4, 4, 0, 0 ], [ 0, 4, 0, 4, 0 ], [ 4, 0, 0, 0, 4 ], [ 0, 0, 0, 4, 4 ],
            [ 3, 3, 3, 0, 0 ], [ 3, 3, 0, 0, 3 ], [ 0, 3, 3, 3, 0 ], [ 3, 0, 0, 3, 3 ], [ 0, 0, 3, 3, 3 ] 
        ]

        nobleCount = len(self.__players) + 1
        for _ in range(nobleCount):
            randNum = randint(0, len(nobleData) - 1)
            cardCost = nobleData.pop(randNum)
            self.__nobles.append(Noble(cardCost))
            

    def initalizeTokens(self):
        playerCount = len(self.__players)
        
        tokenRemoval = 0
        if playerCount == 3:
            tokenRemoval += 2
        elif playerCount == 2:
            tokenRemoval += 3

        for gems in self.__gemTokens:
            if gems != "gold joker":
                self.__gemTokens[gems] = 7 - tokenRemoval
            else:
                self.__gemTokens[gems] = 5


    def initializeDeck(self):
        tier1Data = [
            ["diamond", [ 0, 1, 1, 1, 1 ],  0], ["diamond", [ 0, 1, 2, 1, 1 ],  0], ["diamond", [ 0, 0, 0, 2, 1 ],  0], ["diamond", [ 0, 2, 0, 0, 2 ],  0],
            ["diamond", [ 0, 3, 0, 0, 0 ],  0], ["diamond", [ 0, 2, 2, 0, 1 ],  0], ["diamond", [ 3, 1, 0, 0, 1 ],  0],["diamond", [ 0, 0, 4, 0, 0 ], 1],
            ["sapphire", [ 1, 0, 1, 1, 1 ],  0], ["sapphire", [ 1, 0, 1, 2, 1 ],  0], ["sapphire", [ 0, 1, 3, 1, 0 ],  0], ["sapphire", [ 1, 0, 2, 2, 0 ],  0],
            ["sapphire", [ 0, 0, 2, 0, 2 ],  0], ["sapphire", [ 1, 0, 0, 0, 2 ],  0], ["sapphire", [ 0, 0, 0, 0, 3 ],  0], ["sapphire", [ 0, 0, 0, 4, 0 ], 1],
            ["emerald", [ 1, 1, 0, 1, 1 ],  0], ["emerald", [ 1, 1, 0, 1, 2 ],  0], ["emerald", [ 1, 3, 1, 0, 0 ],  0], ["emerald", [ 0, 1, 0, 2, 2 ],  0],
            ["emerald", [ 0, 2, 0, 2, 0 ],  0], ["emerald", [ 2, 1, 0, 0, 0 ],  0], ["emerald", [ 0, 0, 0, 3, 0 ],  0], ["emerald", [ 0, 0, 0, 0, 4 ], 1],
            ["ruby", [ 1, 1, 1, 0, 1 ],  0], ["ruby", [ 2, 1, 1, 0, 1 ],  0], ["ruby", [ 1, 0, 0, 1, 3 ],  0], ["ruby", [ 2, 0, 0, 2, 0 ],  0],
            ["ruby", [ 0, 2, 1, 0, 0 ],  0], ["ruby", [ 3, 0, 0, 0, 0 ],  0], ["ruby", [ 2, 0, 1, 0, 2 ],  0], ["ruby", [ 4, 0, 0, 0, 0 ], 1],
            ["onyx", [ 1, 2, 1, 1, 0 ],  0], ["onyx", [ 1, 1, 1, 1, 0 ],  0], ["onyx", [ 0, 0, 1, 3, 1 ],  0], ["onyx", [ 2, 2, 0, 1, 0 ],  0],
            ["onyx", [ 2, 0, 2, 0, 0 ],  0], ["onyx", [ 0, 0, 2, 1, 0 ],  0], ["onyx", [ 0, 0, 3, 0, 0 ],  0], ["onyx", [ 0, 4, 0, 0, 0 ], 1]
        ]

        tier2Data = [
            ["diamond", [ 0, 0, 3, 2, 2 ], 1], ["diamond", [ 2, 3, 0, 3, 0 ], 1], ["diamond", [ 0, 0, 1, 4, 2 ], 2], 
            ["diamond", [ 0, 0, 0, 5, 3 ], 2], ["diamond", [ 0, 0, 0, 5, 0 ], 2], ["diamond", [ 6, 0, 0, 0, 0 ], 3],
            ["sapphire", [ 0, 2, 2, 3, 0 ], 1], ["sapphire", [ 0, 2, 3, 0, 3 ], 1], ["sapphire", [ 2, 0, 0, 1, 4 ], 2],
            ["sapphire", [ 5, 3, 0, 0, 0 ], 2], ["sapphire", [ 0, 5, 0, 0, 0 ], 2], ["sapphire", [ 0, 6, 0, 0, 0 ], 3],
            ["emerald", [ 2, 3, 0, 0, 2 ], 1], ["emerald", [ 3, 0, 2, 3, 0 ], 1], ["emerald", [ 4, 2, 0, 0, 1 ], 2],
            ["emerald", [ 0, 5, 3, 0, 0 ], 2], ["emerald", [ 0, 5, 0, 0, 0 ], 2], ["emerald", [ 0, 0, 6, 0, 0 ], 3],
            ["ruby", [ 2, 0, 0, 2, 3 ], 1], ["ruby", [ 0, 3, 0, 2, 3 ], 1], ["ruby", [ 1, 4, 2, 0, 0 ], 2], 
            ["ruby", [ 3, 0, 0, 0, 5 ], 2], ["ruby", [ 0, 0, 0, 0, 5 ], 2], ["ruby", [ 0, 0, 0, 6, 0 ], 3],
            ["onyx", [ 3, 2, 2, 0, 0 ], 1], ["onyx", [ 3, 0, 3, 0, 2 ], 1], ["onyx", [ 0, 1, 4, 2, 0 ], 2],
            ["onyx", [ 0, 0, 5, 3, 0 ], 2], ["onyx", [ 5, 0, 0, 0, 0 ], 2], ["onyx", [ 0, 0, 0, 0, 6 ], 3]
        ]

        tier3Data = [
            ["diamond", [ 0, 3, 3, 5, 3 ], 3], ["diamond", [ 3, 0, 0, 3, 6 ], 4], ["diamond", [ 0, 0, 0, 0, 7 ], 4], ["diamond", [ 3, 0, 0, 0, 7 ], 5],
            ["sapphire", [ 3, 0, 3, 3, 5 ], 3], ["sapphire", [ 6, 3, 0, 0, 3 ], 4], ["sapphire", [ 7, 0, 0, 0, 0 ], 4], ["sapphire", [ 7, 3, 0, 0, 0 ], 5],
            ["emerald", [ 5, 3, 0, 3, 3 ], 3], ["emerald", [ 3, 6, 3, 0, 0 ], 4], ["emerald", [ 0, 7, 0, 0, 0 ], 4], ["emerald", [ 0, 7, 3, 0, 0 ], 5],
            ["ruby", [ 3, 5, 3, 0, 3 ], 3], ["ruby", [ 0, 3, 6, 3, 0 ], 4], ["ruby", [ 0, 0, 7, 0, 0 ], 4], ["ruby", [ 0, 0, 7, 3, 0 ], 5],
            ["onyx", [ 3, 3, 5, 3, 0 ], 3], ["onyx", [ 0, 3, 0, 6, 3 ], 4], ["onyx", [ 0, 0, 0, 7, 0 ], 4], ["onyx", [ 0, 0, 0, 7, 3 ], 5]
        ]

        tier1Deck = Deck()
        tier2Deck = Deck()
        tier3Deck = Deck()

        for card in tier1Data:
            tier1Deck.addCard(Card(card[0], card[1], card[2]))

        for card in tier2Data:
            tier2Deck.addCard(Card(card[0], card[1], card[2]))

        for card in tier3Data:
            tier3Deck.addCard(Card(card[0], card[1], card[2]))

        self.__decks = [tier1Deck, tier2Deck, tier3Deck]

        for deck in self.__decks:
            deck.shuffle()

    # Draw top 4 cards from each of the three decks
    def initializeTable(self):
        for deck in self.__decks():
            top4Cards = []
            for _ in range(4):
                top4Cards.append(deck.draw())
            self.__table.append(top4Cards)

    def displayGemTokens(self):
        print("Available Gem Tokens")
        for gem in self.__gemTokens:
            print(gem.title(), ":", self.__gemTokens[gem])
        
    # TODO: Complete displayNobles function
    # def displayNobles(self):


    def checkVisitingNobles(self):
        visitingNobleCount = 0
        # for noble in self.__nobles():

        if visitingNobleCount == 1:
            print("Noble has visited!")
        elif visitingNobleCount > 1:
            print("Please select visiting noble")

    def takeGemToken(self, amount, gem):
        self.__gemTokens[gem] -= amount
