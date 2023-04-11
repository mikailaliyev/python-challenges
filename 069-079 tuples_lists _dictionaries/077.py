# Change program 076 so that once the user has completed their list of names, 
# display the full list and ask them to type in one of the names on the list. 
# Display the position of that name in the list. 
# Ask the user if they still want that person to come to the party. 
# If they answer “no”, delete that entry from the list and display the list again

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

print(name_list)
user_select = input("Type a name from the list\n")
print(f"{user_select}'s position on the list is {name_list.index(user_select)}")
still_selected = input(f"Do you still want to invite {user_select} to your party?\n")
if still_selected == "no":
    del name_list[name_list.index(user_select)]
print(name_list)
