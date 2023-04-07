# Ask for the name of somebody the user wants to invite to a party. 
# After this, display the message “[name] has now been invited” and add 1 to the count. 
# Then ask if they want to invite somebody else. 
# Keep repeating this until they no longer want to invite anyone else to the party 
# and then display how many people they have coming to the party

count = 0
invite_more = "y"

while invite_more == "y":
    invited_person = input("Enter a name of a person you want to invite\n")
    print(f"{invited_person} has now been invited")
    count += 1
    invite_more = input("Do you want to invite someone else?\n")

print(f"You have invited {count} people to the party")
