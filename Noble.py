from random import randint


class Noble:

    def __init__(self, cardCost):
        self.__cardCost = {
            "diamond": cardCost[0],
            "sapphire": cardCost[1],
            "emerald": cardCost[2],
            "ruby": cardCost[3],
            "onyx": cardCost[4]
        }
        self.__prestige = 3

    # Generate nobles per amount of players
    @staticmethod
    def initalize(playerCount):
        listOfNobleCosts = [[4, 4, 0, 0, 0], [0, 4, 4, 0, 0], [0, 4, 0, 4, 0], [4, 0, 0, 0, 4], [0, 0, 0, 4, 4],
                            [3, 3, 3, 0, 0], [3, 3, 0, 0, 3], [0, 3, 3, 3, 0], [3, 0, 0, 3, 3], [0, 0, 3, 3, 3]]

        # Randomly select noble costs to create noble objects to be appended to nobles array 
        nobles = []
        for _ in range(playerCount + 1):
            randNum = randint(0, len(listOfNobleCosts) - 1)
            nobleCost = listOfNobleCosts.pop(randNum)
            newNoble = Noble(nobleCost)
            nobles.append(newNoble)
        return nobles

    def getPrestige(self):
        return self.__prestige

    def getCardCost(self):
        return self.__cardCost