import os
import sys
import time
import random

def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def spacer(word):
    spacer = " "*(20 - len(word))
    return(spacer)

def main():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    words = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu"]
    correct = [0]*26
    incorrect = [0]*26
    points = 0
    perfectRun = True

    while True:
        index = random.randint(0, 25)
        while True:
            clear()
            guess = input(f"{letters[index]} is for ")
            if(guess.strip() != ""):
                break

        guess = guess.lower()
        if(guess == words[index]):
            points += 1
            if(points == 1):
                pointsSpelling = "point"
            else:
                pointsSpelling = "points"

            correct[index] += 1

            input(f"Correct! You have {points} {pointsSpelling}")
        elif(guess == "quit"):
            print(f"word{spacer('word')}correct{spacer('correct')}incorrect")
            print(f"{'-'*60}")
            index = 0
            for i in letters:
                print(f"{words[index]}{spacer(words[index])}{correct[index]}{spacer(str(correct[index]))}{incorrect[index]}") ## nnnnnnnnn -- nineteen
                index+=1

            if(perfectRun == True):
                print("Congratulations, this was a perfect run!")

            input(f"You finished with {points} {pointsSpelling}!")

            sys.exit(0)
        else:
            input(f"Incorrect, it's {words[index]}")
            perfectRun = False
            incorrect[index] += 1
            points -= 1

main()
