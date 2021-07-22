import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9")
while chances<5:
    guess = int(input("Enter your guess"))
    if guess == number :
        print("YOU WON!!")
    elif guess<number:
        print("Your guess is less than number ")
    elif guess>number:
        print("Your guess is greater than number ")
    chances = chances+1
if not chances<5:
    print("YOU LOSE! the number is ",number)