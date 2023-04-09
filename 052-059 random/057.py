# Update program 056 so that it tells the user 
# if they are too high or too low before they pick again
import random

random_input = random.randint(1, 10)
user_choice = False

while user_choice == False:
    user_input = int(input("Enter a number\n"))
    if user_input == random_input:
        print("You got it wright")
        user_choice = True
    elif user_input > random_input:
        print("Too high")
    else:
        print("Too low")
