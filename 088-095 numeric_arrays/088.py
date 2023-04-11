# Ask the user for a list of five integers. 
# Store them in an array. 
# Sort the list and display it in reverse order
from array import *

array_storage = array ('i', [])
for i in range(0, 5):
    user_integers = int(input("Enter a list of integers\n"))
    array_storage.append(user_integers)
array_storage = sorted(array_storage)
array_storage.reverse()
print(array_storage)
