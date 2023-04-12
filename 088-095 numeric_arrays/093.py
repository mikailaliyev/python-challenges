# Ask the user to enter five numbers. 
# Sort them into order and present them to the user. 
# Ask them to select one of the numbers. 
# Remove it from the original array and save it in a new array

from array import *

arr1 = array ('i', [])
arr2 = array ('i', [4])

while len(arr1) < 5:
    user_input = int(input("Enter a number\n"))
    arr1.append(user_input)
arr1 = sorted(arr1)
print(f"Here your array of numbers: {arr1}")

user_choice = int(input("Choose a number from the array\n"))
if user_choice in arr1:
    arr1.remove(user_choice)
    arr2.append(user_choice)
    arr2 = sorted(arr2)
    print(f"Result: {arr1}")
    print(f"Deleted number: {arr2}")
else:
    print("The number is not in the array!")
