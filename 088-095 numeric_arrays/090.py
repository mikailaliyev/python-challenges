# Ask the user to enter numbers. 
# If they enter a number between 10 and 20, save it in the array,
# otherwise display the message “Outside the range”. 
# Once five numbers have been successfully added, display the message “Thank you” 
# and display the array with each item shown on a separate line
from array import *

nums = array('i', [])
while len(nums) < 5:
    user_number = int(input("Enter a number\n"))
    if user_number > 10 and user_number < 20:
        nums.append(user_number)
    else:
        print("Outside the range")

print("Thank you")
for i in nums:
    print(i)
