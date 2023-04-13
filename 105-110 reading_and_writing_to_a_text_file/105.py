# Write a new file called “Numbers.txt”. 
# Add five numbers to the document which are stored on the same line and only separated by a comma. 
# Once you have run the program, look in the location where your program is stored 
# and you should see that the file has been created. 
# The easiest way to view the contents of the new text file on a Windows system is to read it using Notepad
import random
file = open("Numbers.txt", "w")
for i in range(0, 5):
    num = random.randint(0, 100)
    if i == 4:
       file.write(f"{num}")
    else:
        file.write(f"{num}, ")
file.close()
