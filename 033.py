# Ask the user to enter two numbers.
# Use whole number division to divide the first number by the second 
# and also work out the remainder 
# and display the answer in a user-friendly way 
# (e.g. if they enter 7 and 2 display “7 divided by 2 is 3 with 1 remaining”).
import math

first_number = int(input("Enter a number\n"))
second_number = int(input("Enter another number\n"))
whole_division = first_number // second_number
remainder = first_number % second_number
print(f"{first_number} divided by {second_number} is {whole_division} with {remainder} remaining")
