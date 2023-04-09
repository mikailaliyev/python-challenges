# Randomly choose a number between 1 and 5. 
# Ask the user to pick a number. 
# If they guess correctly, display the message “Well done”, 
# otherwise tell them if they are too high or too low 
# and ask them to pick a second number. 
# If they guess correctly on their second guess, display
# “Correct”, otherwise display “You lose”
import random

random_number = random.randint(1, 5)
user_input = int(input("Enter a number\n"))

if user_input == random_number:
    print("Well done")
else:
    if user_input > random_number:
        print("Too high")
        second_try = int(input("Guess again\n"))
        if second_try == random_number:
            print("Correct")
        else:
            print("You lose")
    else:
        print("Too low")
        second_try = int(input("Guess again\n"))
        if second_try == random_number:
            print("Correct")
        else:
            print("You lose")