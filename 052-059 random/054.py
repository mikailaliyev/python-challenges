# Randomly choose either heads or tails (“h” or “t”). 
# Ask the user to make their choice. 
# If their choice is the same as the randomly selected value, 
# display the message “You win”, otherwise display “Bad luck”. 
# At the end, tell the user if the computer selected heads or tails
import random

random_choice = random.choice(["h", "t"])
user_choice = input("Make your choice: heads (h) or tails (t)\n")

if user_choice == random_choice:
    print("You win")
else:
    print("Bad luck")

if random_choice == "h":
    print("The computer chose heads")
else:
    print("The computer chose tails")