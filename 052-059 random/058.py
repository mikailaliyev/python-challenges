# Make a maths quiz that asks five questions 
# by randomly generating two whole numbers to make the question (e.g. [num1] + [num2]).
# Ask the user to enter the answer. 
# If they get it right add a point to their score. 
# At the end of the quiz, tell them how many they got correct out of five
import random

user_points = 0
for i in range(0, 5):
    random_number1 = random.randint(0, 5)
    random_number2 = random.randint(0, 5)
    sum = random_number1 + random_number2
    print(f"{random_number1} + {random_number2} = ?")
    user_answer = int(input("Enter the answer\n"))
    print()
    if user_answer == sum:
        print("Wright! You got a point!")
        user_points += 1

print(f"You got {user_points} points")