# After gathering the four names, ages and shoe sizes, 
# ask the user to enter the name of the person they want to remove from the list. 
# Delete this row from the data and display the other rows on separate lines

count = 0

people = {}

for i in range(0, 2):
    name = input("Enter a name\n")
    age = int(input("Enter age\n"))
    shoe_size = input("Enter shoe size\n")
    people[name] = {'age': age, 'shoe_size': shoe_size}
    print()

print(people)
delete_person = input("Enter a name of a person you want to delete\n")
del people[delete_person]

for i in people:
    print(i, people[i]["age"], people[i]['shoe_size'])
