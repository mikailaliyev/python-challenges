# Using the Names.txt file you created earlier, display the list of names in Python. 
# Ask the user to type in one of the names 
# and then save all the names except the one they entered into a new file called Names2.txt

file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
user_select = input("Choose a name")
user_select = user_select + "\n"

for i in file:
    if i != user_select:
        file = open("Names2.txt", "a")
        file.write(i)
        file.close()
file.close()
print()
file = open("Names2.txt", "r")
print(file.read())
file.close()