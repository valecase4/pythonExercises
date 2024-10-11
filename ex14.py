# Write a program where the computer chooses a number between 1 and 100, and the user has 5 attempts to guess it

######### SOLUTION WITH TRY-BLOCK #########

import random 

number = random.randint(1, 100)

attempts = 5

while attempts > 0:
    user_input = input("Enter a number (1-100): ")

    try:
        user_input = int(user_input)

        if user_input == number:
            print("You won.")
            break
        else:
            attempts -= 1
            print(f"Wrong answer. {attempts} attempts left")
            
    except ValueError:
        print("Please enter a valid integer")

if attempts == 0:
    print(f"I was thinking of {number}")
