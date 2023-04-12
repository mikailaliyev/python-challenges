# Create two arrays (one containing three numbers that the user enters 
# and one containing a set of five random numbers). 
# Join these two arrays together into one large array. 
# Sort this large array and display it so that each number appears on a separate line

from array import *
import random
arr1 = array ('i', [])
arr2= array ('i', [])

while len(arr1) < 3:
    user_input = int(input("Enter a number\n"))
    arr1.append(user_input)

for i in range(0, 5):
    arr2.append(random.randint(0, 100))

arr1.extend(arr2)
arr1 = sorted(arr1)

print()
print("We added another 5 numbers and joined arrays together:")
for i in arr1:
    print(i)
