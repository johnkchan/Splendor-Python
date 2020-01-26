from environment import Environment

 # Check if user entered an acceptable input of 2, 3, or 4
while True:
    playerCount = input("How many players? Please Enter 2, 3, or 4: ")
    if playerCount.isdigit():
        playerCount = int(playerCount)
        if playerCount in [2, 3, 4]:
            break
    print("Invalid Selection!")

game = Environment(playerCount)