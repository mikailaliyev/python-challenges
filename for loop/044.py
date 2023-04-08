# Ask how many people the user wants to invite to a party. 
# If they enter a number below 10, ask for the names and after each name display “[name] has been invited”. 
# If they enter a number which is 10 or higher, display the message “Too many people”

invited_list = int(input("How many people do you want to invite to a party?\n"))
if invited_list < 10:
    for i in range(0, invited_list):
        guest_name = input("Enter a guest name\n")
        print(f"{guest_name} has been invited")
else:
    print("Too many people")
