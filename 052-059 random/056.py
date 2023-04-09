# Randomly pick a whole number between 1 and 10. 
# Ask the user to enter a number 
# and keep entering numbers until they enter the number that was randomly picked
import random

random_input = random.randint(1, 10)
user_choice = False

while user_choice == False:
    user_input = int(input("Enter a number\n"))
    if user_input == random_input:
        print("You got it wright")
        user_choice = True
