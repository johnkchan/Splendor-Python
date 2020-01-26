from random import randint
from card import Card
from deck import Deck
from noble import Noble
from token import Token
from player import Player
from prettytable import PrettyTable


class Environment:

    def __init__(self, playerCount):
        self.__players = Player.initialize(playerCount)
        self.__nobles = Noble.initalize(playerCount)
        self.__decks = Deck.initialize()
        self.__gemTokens = Token.initalize(playerCount)
        self.__table = []
        self.initializeTable()
        self.initializeGame()

    def getPlayers(self):
        return self.__players

    def getNobles(self):
        return self.__nobles

    def getDecks(self):
        return self.__decks

    def getGemTokens(self):
        return self.__gemTokens

    def getTable(self):
        return self.__table

    def initializeTable(self):
        cardsToBeDrawn = 4
        for deck in self.__decks:
            drawnCards = []
            for _ in range(cardsToBeDrawn):
                drawnCards.append(deck.draw())
            self.__table.append(drawnCards)

    def displayNobles(self):
        print("─────────────────────────────────────────────────────────────────────")
        print("Nobles:")

        header = ["Cost"]
        nobleCosts = [["Diamond"], ["Sapphire"], ["Emerald"], ["Ruby"], ["Onyx"]]

        for i, noble in enumerate(self.__nobles):
            header.append("Noble #" + str(i + 1))
            cardCost = noble.getCardCost()
            
            for i, cost in enumerate(cardCost):
                nobleCosts[i].append(str(cardCost[cost]))
                    
        t = PrettyTable(header)
        for cost in nobleCosts:
            t.add_row(cost)

        print(t.get_string(title="Nobles"))

    def displayTable(self):
        print("─────────────────────────────────────────────────────────────────────")

        decks = [self.__table[2], self.__table[1], self.__table[0]]

        for i, deck in enumerate(decks):
            header = ["Fields"]
            cardDetails = [["Token"], ["Prestige"], ["Diamond"], ["Sapphire"], ["Emerald"], ["Ruby"], ["Onyx"]]
            for cardNum, card in enumerate(deck):
                header.append("Card #" + str(cardNum + 1))
                cardCost = card.getCost()
                cardDetails[0].append(card.getTokenType().title())
                cardDetails[1].append(card.getPrestige())
                cardDetails[2].append(cardCost["diamond"])
                cardDetails[3].append(cardCost["sapphire"])
                cardDetails[4].append(cardCost["emerald"])
                cardDetails[5].append(cardCost["ruby"])
                cardDetails[6].append(cardCost["onyx"])

            t = PrettyTable(header)
            for detail in cardDetails:
                t.add_row(detail)
            print("Tier " + str(len(decks) - i) + " Cards:")
            print(t)

    def displayGemTokens(self):
        print("─────────────────────────────────────────────────────────────────────")
        print("Available Gem Tokens:")

        t = PrettyTable(["Gems", "Quantity"])
        for gem in self.__gemTokens:
            t.add_row([gem.title(), self.__gemTokens[gem]])
        print(t)

    def checkVisitingNobles(self, player):
        visitingNobles = []

        for noble in self.__nobles:
            cardCost = noble.getCardCost()
            playerCardTokens = player.getCardTokens()
            isVisting = True

            for cost in cardCost:
                if playerCardTokens[cost] < cardCost[cost]:
                    isVisiting = False

            if isVisting:
                visitingNobles.append(noble)

        # if len(visitingNobles) == 1:
        #     print("Noble has visited!")
        # elif len(visitingNobles) > 1:
        #     print("Please select visiting noble")

    def takeGemToken(self, amount, gem):
        self.__gemTokens[gem] -= amount

    def takeTableCard(self, deckTier, cardNum):
        devCard = self.__table[deckTier - 1][cardNum - 1]
        self.__table[deckTier - 1][cardNum - 1] = ""
        return devCard

    def drawTableCard(self):
        # Replace Table Card if enough cards in same tier deck
        for tier, deck in enumerate(self.__table):
            for cardNum, card in enumerate(deck):
                if card == "":
                    newCard = self.__decks[tier - 1].draw()
                    self.__table[tier][cardNum] = newCard
        
    def initializeGame(self):
        prestigeWinCondition = 15
        run = True

        while run:
            for player in self.__players:
                self.displayNobles()
                self.displayTable()
                self.displayGemTokens()
                player.displayGemTokens()
                player.actions(self)
                self.drawTableCard()
                self.checkVisitingNobles(player)
                player.incrementTurns()

                if player.getPrestige() >= prestigeWinCondition:
                    print("Player #" + player.getNumber() + " has won!")
                    run = False