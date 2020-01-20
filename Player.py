class Player:
    def __init__(self, number):
        self.__number = number
        self.__prestige = 0
        self.__gemTokens = {
            "diamond": 0,
            "sapphire": 0,
            "emerald": 0,
            "ruby": 0,
            "onyx": 0
        }
        self.__cardTokens = {
            "diamond": 0,
            "sapphire": 0,
            "emerald": 0,
            "ruby": 0,
            "onyx": 0
        }
        self.__reserveCards = []
        self.__turns = 0
        
    def getPrestige(self):
        return self.__prestige

    def addPrestige(self, prestige):
        self.__prestige += prestige

    def getGemTokens(self):
        for gem in self.__gemTokens:
            print(gem,":", self.__gemTokens[gem])

    def addGemToken(self, amount, gem):
        gem = gem.lower()
        self.__gemTokens[gem] += amount

    def getCardTokens(self):
        return self.__cardTokens

    def getTurns(self):
        return self.__turns
    
    def incrementTurns(self):
        self.__turns += 1

    def actions(self):
        print("Player", self.__number + "'s", "Turn")
        print("[1] Take 3 gem tokens of different colors.")
        print("[2] Take 2 gem tokens of the same color.")
        print("[3] Reserve 1 development card and take 1 gold token (joker).")
        print("[4] Purchase 1 face-up development card from the middle of the table or a previously reserved one.")
        choice = int(input("Please Enter Action #:"))

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass