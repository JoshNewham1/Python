import random # Importing random to generate pseudo-random numbers
import os # Importing OS to clear the console
import platform # Importing platform to determine which OS is in use so correct clear command can be issued
from pygame import mixer
gameWon = False
numOfAttempts = 0
operatingSystem = platform.system()

print("Welcome to Mastermind")
input("Press enter to begin the game...")
intToGuess = random.randint(0,9999)
numberList = list(str(intToGuess))
while not (gameWon):
    if (operatingSystem == "Windows"):
        os.system('cls')
    else:
        os.system('clear')
    print(intToGuess)
    numOfAttempts += 1
    correctDigits = 0
    guess = input("Please enter your guess: ")
    guessList = list(guess)
    for i in range(0, len(numberList)):
        if (guessList[i] == numberList[i]):
            correctDigits += 1
    if (intToGuess == int(guess)):
        gameWon = True
    else:  
        print("You have guessed " + str(correctDigits) + " digits correctly...")
        input("Press enter to try again...")
print("Congratulations! You have won the game...")
print("You guessed the number in " + str(numOfAttempts) + " attempts")
mixer.init()
mixer.music.load("tada.mp3")
mixer.music.play()
while mixer.music.get_busy() == True:
    continue