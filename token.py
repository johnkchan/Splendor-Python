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

        # If amount of players is 3, then 2 tokens should be removed from each gem type
        # If amount of players is 2, then 3 tokens should be removed from each gem type
        tokenRemoval = 0
        if playerCount == 3:
            tokenRemoval += 2
        elif playerCount == 2:
            tokenRemoval += 3

        # There is only 5 gold joker tokens regardless of the amount of players
        for gems in gemTokens:
            if gems == "gold joker":
                gemTokens[gems] = 5
            else:
                gemTokens[gems] = (7 - tokenRemoval)
                
        return gemTokens
