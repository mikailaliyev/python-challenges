# Ask the user to enter numbers. 
# If they enter a number between 10 and 20, save it in the array, 
# otherwise display the message “Outside the range”. 
# Once five numbers have been successfully added, display the message “Thank you” 
# Create an array which contains five numbers (two of which should be repeated). 
# Display the whole array to the user. 
# Ask the user to enter one of the numbers from the array 
# and then display a message saying how many times that number appears in the list

from array import *

nums = array ('i', [1, 2, 3, 4, 4])
for i in nums:
    print(i)
user_choice = int(input("Enter the number from the list\n"))

if nums.count(user_choice) == 1:
    print("The number you chose repeated once in the array")
else:
    print(f"The number you chose repeated {nums.count(user_choice)} times in the array")
