class Noble:

    def __init__(self, cardCost):
        self.__cardCost = cardCost
        self.__prestige = 3

    def getPrestige(self):
        return self.__prestige

    def getCardCost(self):
        return self.__cardCost