# Create an array of five numbers between 10 and 100 which each have two decimal places. 
# Ask the user to enter a whole number between 2 and 5. 
# If they enter something outside of that range, display a suitable error message
# and ask them to try again until they enter a valid amount. 
# Divide each of the numbers in the array by the number the user entered 
# and display the answers shown to two decimal places
from array import *
import random

arr = array ('f', [12.55, 84.54, 61.88, 99.11, 57.54])

user_number = int(input("Enter a number between 2 and 5\n"))

while user_number < 2 or user_number > 5:
    user_number = int(input("Try again\n"))

for i in arr:
    end_number = i / user_number
    print(round(end_number, 2))
