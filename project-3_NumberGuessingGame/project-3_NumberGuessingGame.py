import random

print("Welcome to Number Guessing Game!!")
computer_guess=random.randint(1,100)
number_of_attempts=0

mode=input("Select mode (easy) or (hard): ").lower()

while (mode!='easy' and mode!='hard'):
    print("Enter valid input..")
    mode=input("Select mode (easy) or (hard): ").lower()

if mode=='easy':
    number_of_attempts=10
elif mode=='hard':
    number_of_attempts=5
    
print("Guess a number we have in the range of 100.")

while number_of_attempts>0:
    print(f"You have {number_of_attempts} number of attempts to guess the number!!")
    player_guess=int(input("Guess the number? : "))
    if computer_guess==player_guess:
        print("You guessed the correct number and WON.")
        exit(0)
    elif player_guess>computer_guess:
        print("Too HIGH, Guess again..")
    elif player_guess<computer_guess:
        print("Too LOW, Guess again..")

    print("\n")

print("You LOST, Unable to guess, BETTER LUCK NEXT TIME...")




    