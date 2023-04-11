# Create an array which will store a list of integers. 
# Generate five random numbers and store them in the array. 
# Display the array (showing each item on a separate line)

from array import *
import random

ints = array('i', [])

for i in range(0, 5):
    int = random.randint(0, 100)
    ints.append(int)
 
for i in ints:
    print(i)
