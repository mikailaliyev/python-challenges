# Define a subprogram that will ask the user to pick a low and a high number, 
# and then generate a random number between those two values 
# and store it in a variable called “comp_num”.
# Define another subprogram that will give the instruction “I am thinking of a number…”
# and then ask the user to guess the number they are thinking of.
# Define a third subprogram that will check to see if the comp_num is the same as the user’s guess. 
# If it is, it should display the message “Correct, you win”, otherwise it should keep looping, 
# telling the user if they are too low or too high 
# and asking them to guess again until they guess correctly
import random

def random_number():
    low = int(input("Pick a number\n"))
    high = int(input("Pick a higher number\n"))
    comp_num = random.randint(low, high)
    return comp_num

def guess_number():
    print("I am thinking of a number...")
    user_guess = int(input("Guess what is the number!\n"))
    return user_guess

def is_right(user_number, comp_number):
    while user_number != comp_number:
        if user_number > comp_number:
            user_number = int(input("Too high guess again\n"))
        else:
            user_number = int(input("Too low guess again\n"))
    print("Correct you win")

def main():
    comp_number = random_number()
    user_number = guess_number()
    is_right(user_number, comp_number)

main()