from random import randint


class Noble:

    def __init__(self, cardCost, image):
        self.__cardCost = {
            "diamond": cardCost[0],
            "sapphire": cardCost[1],
            "emerald": cardCost[2],
            "ruby": cardCost[3],
            "onyx": cardCost[4]
        }
        self.__image = image
        self.__prestige = 3

    # Generate nobles per amount of players
    @staticmethod
    def initalize(playerCount):
        # diamond, sapphire, emerald, ruby, onyx
        noblesList = [
            [[4, 4, 0, 0, 0], 'images/Niccolo Machiavelli.png'],
            [[0, 4, 4, 0, 0], 'images/Suleiman The Magnificient.png'],
            [[0, 4, 0, 4, 0], 'images/Mary Stuart.png'],
            [[4, 0, 0, 0, 4], 'images/Isabella I Of Castile.png'],
            [[0, 0, 0, 4, 4], 'images/Henry VIII.png'],
            [[3, 3, 3, 0, 0], 'images/Anne of Brittany.png'],
            [[3, 3, 0, 0, 3], 'images/Elisabeth Of Austria.png'],
            [[0, 3, 3, 3, 0], 'images/Catherine de Medici.png'],
            [[3, 0, 0, 3, 3], 'images/Charles V.png'],
            [[0, 0, 3, 3, 3], 'images/Francis I Of France.png']
        ]

        nobles = []
        for _ in range(playerCount + 1):
            randNum = randint(0, len(noblesList) - 1)
            nobleData = noblesList.pop(randNum)
            nobles.append(Noble(nobleData[0], nobleData[1]))

        return nobles

    def getPrestige(self):
        return self.__prestige

    def getCardCost(self):
        return self.__cardCost

    def getImage(self):
        return self.__image
