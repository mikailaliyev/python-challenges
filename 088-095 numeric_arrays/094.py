# Display an array of five numbers. 
# Ask the user to select one of the numbers. 
# Once they have selected a number, display the position of that item in the array. 
# If they enter something that is not in the array, ask them to try again until they select a relevant item
from array import *

arr = array ('i', [1,2,3,4,5])
arr = sorted(arr)
print(arr)
user_select = int(input("Select a number from the array\n"))

while user_select not in arr:
    user_select = int(input("Try again, the number is not in the array\n"))

print(f"The position of the selected number is {arr.index(user_select)}")
