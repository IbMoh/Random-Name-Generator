import random
from helpers.enums import *

def randomName():
    first = random.choice(FIRSTNAME)
    last = random.choice(LASTNAME)
    return first + " " + last

def anotherName(choice):
    if choice == '1':
        name = randomName()
        print("Here's your name ")
        print(name + "\n")

def start(inputed):
    while inputed.lower() != "x":
        print(f"Wrong input! Inputed: {inputed}")
        inputed = input("Press X to generate a name: ")
    if inputed.lower() == "x":
        name = randomName()
        print("Here's your name " + "\n")
        print(name + "\n")

def again():
    newName = input("Try again? 1 or 0: \n")
    if newName == "1":
        anotherName(newName) 
    else:
        print("Thanks for playing!")
        exit()

def main():

    print("Welcome to our random name generator!")
    choice = input("Press X to generate a name: ")
    start(choice)
    
    while True:
        again()            
            
if __name__ == "__main__":
    main()