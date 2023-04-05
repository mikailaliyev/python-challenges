# Ask the user to enter an integer that is over 500. 
# Work out the square root of that number and display it to two decimal places.
import math

user_number = int(input("Enter an integer over 500\n"))
multiplied = math.sqrt(user_number)
print(round(multiplied, 2))
