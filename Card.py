class Card:
    def __init__(self, tokenType, cost, prestige):
        self.__tokenType = tokenType
        self.__cost = cost
        self.__prestige = prestige

    def getTokenType(self):
        return self.__tokenType

    def getCost(self):
        return self.__cost

    def getPrestige(self):
        return self.__prestige