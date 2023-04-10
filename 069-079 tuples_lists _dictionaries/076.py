# Ask the user to enter the names of three people they want to invite to a party 
# and store them in a list. 
# After they have entered all three names, 
# ask them if they want to add another. 
# If they do, allow them to add more names until they answer “no”. 
# When they answer “no”, display how many people they have invited to the party

name_list = []
want_more = True

for i in range(0, 3):
    guests = input("Enter a name of your guest\n")
    name_list.append(guests)

while want_more:
    user_answer = input("Do you want to invite more people? (yes/no)\n")
    if user_answer == "yes":
        guests = input("Enter a name of your guest\n")
        name_list.append(guests)
    else:
        print(f"You have invited {len(name_list)} people")
        want_more = False
