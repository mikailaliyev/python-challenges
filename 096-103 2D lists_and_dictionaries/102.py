# Ask the user to enter the name, age and shoe size for four people. 
# Ask for the name of one of the people in the list and display their age and shoe size.

count = 0

people = {}

for i in range(0, 2):
    name = input("Enter a name\n")
    age = int(input("Enter age\n"))
    shoe_size = input("Enter shoe size\n")
    people[name] = {'age': age, 'shoe_size': shoe_size}
    print()

what_name = input("Choose a name from the list\n")
if what_name in people:
    print(people[what_name])
else:
    print("Enter a valid name")
