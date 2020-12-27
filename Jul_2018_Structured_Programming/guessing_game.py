'''
Created on 11 Nov 2018

@author: Pei Xuan

A simple game application that allows a single player to play a guessing game repeatedly.
Chips are used to bet on the next number.
'''
from random import shuffle
import math

def main():
    outfile = open("Q3Out.txt","w")  #Creates and writes into a file for displaying number of chips
    
    chipAmt = 50  #Initialize starting game chips
    while True:  #Loops a brand new game till user chooses to quit program
        maxNum = gameIntro(chipAmt)  #Prints an introduction and get max number for game from player
        winSeq = randSeq(maxNum)  #Get random sequence of numbers for game
        
        print("Current Number is {}".format(winSeq[0]))
        print("Guess if the next number is higher or lower.")
        
        gameInfo = (False,chipAmt)  #Initialize gameInfo[0] to false as game has not ended yet
        roundNum = 1  #Initialize current round
        while gameInfo[0] is False and gameInfo[1] != 0:  #Loop till game has ended
            chipAmt = gameInfo[1]
            gameInfo = gameRound(winSeq, chipAmt, roundNum, outfile)  #Runs a round of the game
            roundNum += 1
        
        if gameInfo[1] == 0:  #Unable to play due to having no chips to bet
            break   #Break the loop, ends the program
        
        else:
            stop = input("<ENTER> to play and any letter to stop: ")
            if stop != "":  #If any input is detected
                print("Not playing again. You have {} chips left.".format(chipAmt))
                break  #Break the loop, ends the program
    
    outfile.close()  #Closes text file for number of chips
            

def gameIntro(chipAmt):
    #Short introduction and obtains max number from player
    maxNum = int(input("Enter the max number to generate from 1. The number should be at least 4: "))
    print("Playing {} rounds of guesses".format(maxNum - 3))
    print("chips = {}".format(chipAmt))
    
    return maxNum
    
def randSeq(maxNum):
    #Obtain sequence of numbers to be used for guesses
    winSeq = [i+1 for i in range(maxNum)]  #Get sequence of whole numbers from 1 to maxNum
    shuffle(winSeq)  #shuffle list to get final random sequence of numbers for game
    
    return winSeq

def gameRound(winSeq, chipAmt, roundNum, outfile):
    #Runs a single round of the guessing game
    guess = maxGuess(winSeq, roundNum)  #Gets guess from player
    
    if guess == False:  #If maximum rounds of guesses are reached
        gameInfo = (True,chipAmt)
        return gameInfo
    
    roundInfo = {"Revealed Number":{"Round num":roundNum,"Number":winSeq[roundNum-1],"Guess":guess},\
                 "Next Number":{"Round num":roundNum+1,"Number":winSeq[roundNum],"Guess":"N/A"}}
    

    chipAmt = chipCalc(roundInfo, chipAmt, winSeq)
    print("Number is {}!".format(roundInfo["Next Number"]["Number"]))
    print("Chips = {}".format(chipAmt))
    print("Chips = {}".format(chipAmt), file = outfile)  #Prints to Q3Out.txt file
    gameInfo = (False,chipAmt)
        
    if chipAmt == 0:      
        print("Game ending as player cannot bet \nPlayer has no more chips to play new game.")
        gameInfo = (True,0)
        return gameInfo
    
    return gameInfo


def maxGuess(winSeq, roundNum):
    #Identifies the max number of guesses the player can make and get guess input
    maxRounds = len(winSeq) - 3
    if roundNum > maxRounds:
        guess = False
    else:
        while True:  #Loops until valid input is given
            guess = input("Round {0}) Make a guess h/l or <ENTER> to skip {0} of {1} rounds: "\
                  .format(roundNum,maxRounds)).lower()
            if guess == "h" or guess == "l" or guess == "":  #If guess is valid
                break  #Stop this loop
            else:
                print("Please input a valid guess h/l or <ENTER>")
            
    return guess
    
def chipCalc(roundInfo, chipAmt, winSeq):
    #Calculates current and any changes in chips
    '''
    If player guesses correctly, wins twice bet amount
    If player guesses wrongly, loses bet amount
    If revealed value is 1 or maxNum, wins 1/2 bet amount 
    '''
    
    #Calculate maxNum using winSeq
    maxNum = sorted(winSeq)[-1]  #Sort winSeq, and take the last (highest) value
    #Find out if revealed value is 1 or maxNum
    halfBetValue = False  #Initialize this variable first
    revealedValue = roundInfo["Revealed Number"]["Number"]
    if revealedValue == maxNum or revealedValue == 0:
        halfBetValue = True
    
    #Obtaining correct answer for this round
    if roundInfo["Next Number"]["Number"] > roundInfo["Revealed Number"]["Number"]:
        roundAns = "h"
    
    else:
        roundAns = "l"
    
    
    roundGuess = roundInfo["Revealed Number"]["Guess"]  #Getting player guess for this round

    if  roundGuess == "":  #If player skipped this round
        return chipAmt  #Returns chipAmt with no change, no betting for this round
    
    
    bet = getBet(chipAmt)  #Get player bet
    if roundGuess != roundAns:  #If player makes a wrong guess
        chipAmt -= bet
    
    elif roundGuess == roundAns and halfBetValue is True:  #If revealed value is 1 or maxNum, wins 1/2 bet amount 
        chipAmt += math.ceil(bet/2)  #math.ceil is used because round does not round 0.5 up, but to the nearest even integer.
    
    else:  #roundGuess == roundAns
        chipAmt += bet*2
    
    
    return chipAmt


def getBet(chipAmt):
    #get a valid bet from player and return it
    while True:  #Loop till valid bet amount is given
        bet = int(input("Place an amount for bet: "))
        if bet <= chipAmt:
            return bet
        else:
            print("You cannot bet more chips than you have")
        
    

if __name__ == '__main__':
    main()
