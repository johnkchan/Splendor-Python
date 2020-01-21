class Player:
    def __init__(self, number):
        self.__number = str(number)
        self.__prestige = 0
        self.__gemTokens = {
            "diamond": 0,
            "sapphire": 0,
            "emerald": 0,
            "ruby": 0,
            "onyx": 0,
            "gold joker": 0
        }
        self.__cardTokens = {
            "diamond": 0,
            "sapphire": 0,
            "emerald": 0,
            "ruby": 0,
            "onyx": 0
        }
        self.__reservedCards = []
        self.__turns = 0

    @staticmethod
    def initialize(playerCount):
        players = []
        for i in range(int(playerCount)):
            players.append(Player(i + 1))
        return players

    def getNumber(self):
        return self.__number

    def getPrestige(self):
        return self.__prestige

    def addPrestige(self, prestige):
        self.__prestige += prestige

    def getGemTokens(self):
        return self.__gemTokens

    def takeGemTokens(self, amount, gem):
        self.__gemTokens[gem] -= amount

    def addGemToken(self, amount, gem):
        gem = gem.lower()
        self.__gemTokens[gem] += amount

    def getCardTokens(self):
        return self.__cardTokens

    def addCardTokens(self, amount, gem):
        self.__cardTokens[gem] += amount

    def getReservedCards(self):
        return self.__reservedCards

    def getTurns(self):
        return self.__turns

    def incrementTurns(self):
        self.__turns += 1

    def actions(self, environment):
        print("─────────────────────────────────────────────────────────────────────")
        print("Player #" + self.__number + "'s Turn:")
        print("[1] Take 3 gem tokens of different colors.")
        print("[2] Take 2 gem tokens of the same color.")
        print("[3] Reserve 1 development card and take 1 gold token (joker).")
        print("[4] Purchase 1 face-up development card from the middle of the table or a previously reserved one.")
        choice = int(input("Please Enter Action #:"))
        while choice not in [1, 2, 3, 4]:
            print("Not Valid Action #")
            choice = int(input("Please Enter Action #: "))

        # Take 3 gem tokens of different colors.
        if choice == 1:
            selectedGems = []
            for i in range(3):
                prompt = "Please Enter Gem Type #" + str(i + 1) + ": "
                
                while True:
                    gemChoice = input(prompt)
                
                    # Validate if gem choice is not repeated and gem choice is valid gem type
                    isRepeated = True if gemChoice.lower() in selectedGems else False
                    if self.isValidGem(gemChoice) and not isRepeated:
                        break

                    warning = "Invalid Gem Type."
                    if isRepeated:
                        warning += " Gems cannot be repeated"
                    print(warning)

                selectedGems.append(gemChoice.lower())

            for gem in selectedGems:
                self.addGemToken(1, gem)
                environment.takeGemToken(1, gem)

        # Take 2 gem tokens of the same color.
        elif choice == 2:
            prompt = "Please Enter Gem Type: "
            
            while True:
                gemChoice = input(prompt)
            
                if self.isValidGem(gemChoice):
                    break

                print("Invalid Gem Type.")

            gem = gemChoice.lower()
            self.addGemToken(2, gem)
            environment.takeGemToken(2, gem)

        # Reserve 1 development card and take 1 gold token (joker).
        elif choice == 3:
            while True:
                deckTier = input("Please Enter Deck Tier (1, 2, 3): ")
                if deckTier.isdigit() and int(deckTier) in [1, 2, 3]:
                    break
                print("Invalid Deck Tier.")
            deckTier = int(deckTier)

            while True:
                cardNum = input("Please Enter Card Number From Selected Deck Tier: ")
                if cardNum.isdigit() and int(cardNum) in [1, 2, 3, 4]:
                    break
                print("Invalid Deck Tier.")
            cardNum = int(cardNum)
            
            # TODO: Check if reservedCards is maxed out
            devCard = environment.getTable()[deckTier - 1][cardNum - 1]
            self.__reservedCards.append(devCard)
            print("Card #" + str(cardNum) + " from the Tier " + str(deckTier) + " Deck has been reserved.")
            
            if environment.getGemTokens()["gold joker"] >= 1:
                self.addGemToken(1, "gold joker")
                environment.takeGemToken(1, "gold joker")

        # Purchase 1 face-up development card from the middle of the table or a previously reserved one.
        elif choice == 4:
            while True:
                deckTier = input("Please Enter Deck Tier (1, 2, 3): ")
                if deckTier.isdigit() and int(deckTier) in [1, 2, 3]:
                    break
                print("Invalid Deck Tier.")
            deckTier = int(deckTier)

            while True:
                cardNum = input("Please Enter Card Number From Selected Deck Tier: ")
                if cardNum.isdigit() and int(cardNum) in [1, 2, 3, 4]:
                    break
                print("Invalid Deck Tier.")
            cardNum = int(cardNum)
            
            # TODO: Create logic if gemCosts are not met
            devCard = environment.getTable()[deckTier - 1][cardNum - 1]
            cardCost = devCard.getCost()

            isPurchasable = True
            
            for cost in cardCost:
                if cardCost[cost] > (self.getGemTokens[cost] + self.getCardTokens[cost]):
                    isPurchase = False
            
            if isPurchasable:
                for cost in cardCost
                    if cardCost[cost] > 0:
                        self.takeGemTokens -= (cardCost[cost] - self.getCardTokens[cost])

            # Add Prestige from purchased card and increment cardToken
            self.addPrestige(devCard.getPrestige())
            self.addCardTokens(1, devCard.getTokenType())

            # TODO: Remove card from table and draw new card to take its place
                
    def isValidGem(self, gem):
        gem = gem.lower()
        isValid = False

        for gemType in self.__gemTokens:
            if gem == gemType:
                isValid = True
        
        if gem == "gold joker":
            isValid = False

        return isValid
        
