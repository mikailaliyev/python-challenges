# Display the following menu to the user:
# 1) Addition
# 2) Subtraction
# Enter 1 or 2
# If they enter a 1, it should run a subprogram that will generate two random numbers between 5 and 20, 
# and ask the user to add them together. 
# Work out the correct answer and return both the user’s answer and the correct answer.
#
# If they entered 2 as their selection on the menu, 
# it should run a subprogram that will generate one number between 25 and 50 and another number between 1 and 25 
# and ask them to work out num1 minus num2. 
# This way they will not have to worry about negative answers. 
# Return both the user’s answer and the correct answer.
#
# Create another subprogram that will check if the user’s answer matches the actual answer. 
# If it does, display “Correct”, otherwise display a message that will say “Incorrect, the answer is” 
# and display the real answer.
# If they do not select a relevant option on the first menu you should display a suitable message
import random

def random_one():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    user_decision = int(input(f"Please add {num1} to {num2}\n"))
    return num1, num2, user_decision

def random_two():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    user_decision = int(input(f"Please subtract {num2} from {num1}\n"))
    return num1, num2, user_decision

def check_user(user_decison, answer):
    if user_decison == answer:
        print("Correct")
    else:
        print(f"Incorrect, the answer is {answer}")
    
def main():
    user_choice = input("1) Addition\n2) Subtraction\nEnter 1 or 2\n")
    
    if user_choice == "1":
        num1, num2, user_decision = random_one()
        answer = num1 + num2
        check_user(user_decision, answer)
    elif user_choice == "2":
        num1, num2, user_decision = random_two()
        answer = num1 - num2
        check_user(user_decision, answer)
    else:
        print("You should pick 1 or 2!")
main()