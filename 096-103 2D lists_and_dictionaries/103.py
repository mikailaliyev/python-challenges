# Adapt program 102 to display the names and ages of all the people in the dictionary
# but do not show their shoe size.

count = 0

people = {}

for i in range(0, 2):
    name = input("Enter a name\n")
    age = int(input("Enter age\n"))
    shoe_size = input("Enter shoe size\n")
    people[name] = {'age': age, 'shoe_size': shoe_size}
    print()



for i in people:
    print(i, people[i]['age'])
