class Card:
    
    def __init__(self, tokenType, cost, prestige):
        self.__tokenType = tokenType
        self.__cost = {
            "diamond": cost[0],
            "sapphire": cost[1],
            "emerald": cost[2],
            "ruby": cost[3],
            "onyx": cost[4]
        }
        self.__prestige = prestige

    def getTokenType(self):
        return self.__tokenType

    def getCost(self):
        return self.__cost

    def getPrestige(self):
        return self.__prestige
