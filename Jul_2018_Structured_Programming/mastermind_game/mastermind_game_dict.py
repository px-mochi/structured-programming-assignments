'''
Created on 28 Aug 2018

@author: Pei Xuan
'''

# import library modules
from random import randrange
from copy import deepcopy

# main function that runs the whole program
def main():
    printIntro()
    playerData = getInput()
    gameResult,playerData = Game(playerData)
    printSummary(gameResult,playerData)

# Prints the introduction of the game
def printIntro():
    print("This program simulates a game of MasterMind.")
    print("There are 6 colours to choose from, with letters representing each colour.")
    print("\n{0:7} - R\t{1:7} - G\n{2:7} - B\t{3:7} - Y\n{4:7} - O\t{5:7} - P".format("Red","Green","Blue","Yellow","Orange","Purple"))
    print("\nThe winning combination will be [4] random colours. EG: 'RGBY'")
    
    print("At your turn, key in your guess using the letters. EG: 'BYGO'")

    print("\nScore computation:")
    print("A white pin 'W' - each correct colour, wrong position [1 point].")
    print("A black pin 'B' - each correct colour, right position [5 points].")
    print("Only NEW pins will gain points for a player. For example:")
    print("   Turn 1 - WWB [7 points]\n   Next Turn - WBB - [7 + 5(new) = 12 points]")
    print("The player that breaks the code will gain 1 point to the number of games won. ")
    print("If the winning player also has the most points, he gains 2 points instead. \n\n")
    
# Get user input on number of players and player names
def getInput():
    playNum = int(input("How many players are there? "))
    playerData = {} # initialize dict of player data
    
    # Places all names in dict, in format {'Name':{'score':__,'won':__} ...}
    for i in range(playNum):
        name = input("Player {} Name: ".format(i+1))
        playerData[name] = {"score":0,"won":0}
    
    return playerData

# Runs MasterMind and obtains results of one or multiple games
def Game(playerData):
    replay = "" # Initialize replays
    gameResult = [] # Initialize list of game results
    # A list is used instead of a dict because it is just for printing.
    
    while replay == "":
        replay,oneResult,playerData = oneGame(playerData)    
        oneResult_copy = (deepcopy(oneResult)) # Ensures that previous data is not overwritten
        gameResult.append(oneResult_copy)
    
    return gameResult,playerData
    
# Runs one game of MasterMind, print summary of game after game ends
def oneGame(playerData):
    # Resets current scores for the game
    for name in playerData:
        playerData[name]["score"] = 0
    # Dict to store best pin data per game
    bestPin = {"W":0,"B":0} # Resets bestPin
    n = 0  # Resets index of current player
    
    
    # listing available choices for the random selector
    colours = ["R","G","B","Y","O","P"]
    # Generating random winning code
    winCode = ""
    for i in range(4):
        picked = randrange(0,len(colours)) # Picks a random index from the list
        winCode += colours[picked] # Adds the color picked to the winCode string
        colours.remove(colours[picked]) # Remove previously picked color from list
        
    players = list(playerData.keys()) # List of all player names
    
    # Obtain list of names in order of playing
    playingOrder = []
    for i in range (len(players)):
        picked_players = randrange(0,len(players))
        playingOrder.append(players[picked_players])
        players.remove(players[picked_players])

    print("Playing in This order: ",playingOrder)
    
    
    while bestPin["B"] != 4:
        if n == len(playerData):
            n = 0
        
        currentPlayer = playingOrder[n] # Name of current player
        turnPlayer = playerData[currentPlayer] # Obtains data of current player
        
        turnPlayer,bestPin = oneTurn(currentPlayer,turnPlayer,bestPin,winCode)
        playerData[currentPlayer] = turnPlayer
           
        n = n + 1   # increment turn player
        
    if bestPin["B"] == 4:
        playerData_copy = deepcopy(playerData)
        sortedData = list(playerData_copy.items())
        sortedData.sort(key=byPoint, reverse = True)
        highestScorePlayer = sortedData[0][0]
        winner = currentPlayer # Just to maintain formats from Q3
       
        # Updates current number of wins
        playerData[winner]["won"] = int(playerData[winner]["won"]) + 1
        if highestScorePlayer == winner:
            playerData[winner]["won"] = int(playerData[winner]["won"]) + 1
            
        # Prints out current game info
        print(playerData)
        print("Winner:",winner,playerData[winner],"\n")
        oneResult = [playerData,"Winner: " + str(winner)+" "+str(playerData[winner])]
        
        replay = input("<ENTER> to play and any letter to stop: ")
        
        return replay, oneResult, playerData

# Sorts playerData by points
def byPoint(player):
    return player[1]["score"]

# Runs one single turn of MasterMind, outputs current game points and updates bestPin combination
def oneTurn(currentPlayer,turnPlayer,bestPin,winCode):
    name = currentPlayer # Just to maintain formats from Q3
    newPin = guessPin(winCode,name)
    
    Wpin_increase = newPin.count("W")-bestPin["W"]
    Bpin_increase = newPin.count("B")-bestPin["B"]
    
    print("Current Player: {0:<15} Current Score: {1}".format(name,turnPlayer["score"]))
    
    # Add increased pins to score
    if Wpin_increase > 0:
        turnPlayer["score"] = int(turnPlayer["score"]) + (1*Wpin_increase)
    if Bpin_increase > 0:
        turnPlayer["score"] = int(turnPlayer["score"]) + (5*Bpin_increase)
    
    print("Current Player: {0:<15} Updated Score: {1}".format(name,turnPlayer["score"]))
    
    # Update bestPin
    if Wpin_increase > 0:
        bestPin["W"] = newPin.count("W")
    if Bpin_increase > 0:
        bestPin["B"] = newPin.count("B")    
    
    if newPin == "BBBB":
        print("Correct guess!")
    
    return turnPlayer,bestPin
        
# Checks player guess against winCode and output newPin results
def guessPin(winCode,name):
    guess = getGuess(name)
    
    Wpin = ""
    Bpin = ""
    
    for i in range (4):
        if str(guess[i]) == str(winCode[i]):
            Bpin += "B"
        
        elif guess[i] in winCode:
            Wpin += "W"
        
    newPin = Wpin+Bpin
    
    print("Result", newPin) # Print pin result
    
    return newPin

# Obtain guess input from player
def getGuess(name):
    guess = input("{0}, make a guess of 4 colors from RGBYOP: ".format(name)).upper()
    while len(guess) != 4:
        print("Please input a 4 color guess.")
        guess = str(input("{0}, make a guess of 4 colors from RGBYOP: ".format(name))).upper()
        
    return guess
    
# Prints summary of all games
def printSummary(gameResult,playerData):
    print("\nA file will be created to save game data. \nIf an existing file exists, it will be overwritten.")
    saveFile = input("Input save file name: ") + ".txt"
    outfile = open(saveFile, "w")

    
    # Sorts data by wins to get overall winner
    playerData_copy = deepcopy(playerData)
    sortedData = list(playerData_copy.items())
    sortedData.sort(key=byWins, reverse = True)
    overallWinner = str(sortedData[0][0])+" "+str(sortedData[0][1])
    
    # Printing results to file/screen
    for i in gameResult:
        print(i[::2][0],file = outfile)
        print(i[1::2][0],file = outfile)
        print("",file = outfile)
        
    print("\nOverall Winner: {0}".format(overallWinner))
    print("Program end")
    print("Overall Winner: {0}".format(overallWinner), file = outfile)


# Sorts playerData by overall wins
def byWins(player):
    return player[1]["won"]

main()
