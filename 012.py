# Ask for two numbers. 
# If the first one is larger than the second, display the second number first and then the first number, 
# otherwise show the first number first and then the second.

user_number1 = int(input("Enter the first number\n"))
user_number2 = int(input("Enter the second number\n"))
if user_number1 > user_number2:
    print(user_number2, user_number1)
else:
    print(user_number1, user_number2)
