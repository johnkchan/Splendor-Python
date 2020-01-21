class Token:

    def initalize(playerCount):
        gemTokens = {
            "diamond": 0,
            "sapphire": 0,
            "emerald": 0,
            "ruby": 0,
            "onyx": 0,
            "gold joker": 0
        }

        tokenRemoval = 0
        if playerCount == 3:
            tokenRemoval += 2
        elif playerCount == 2:
            tokenRemoval += 3

        for gems in gemTokens:
            if gems != "gold joker":
                gemTokens[gems] = 7 - tokenRemoval
            else:
                gemTokens[gems] = 5

        return gemTokens
