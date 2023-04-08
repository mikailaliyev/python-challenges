# Task the user to enter a number over 100 
# and then enter a number under 10 
# and tell them how many times the smaller number goes into the larger number in a user-friendly format.

user_number1 = int(input("Enter a number over 100\n"))
user_number2 = int(input("Enter a number under 10\n"))
print(f"{user_number2} goes {user_number1 / user_number2} times into {user_number1}")
