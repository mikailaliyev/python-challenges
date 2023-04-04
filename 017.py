# Ask the user’s age. 
# If they are 18 or over, display the message “You can vote”, 
# if they are aged 17, display the message “You can learn to drive”, 
# if they are 16, display the message “You can buy a lottery ticket”, 
# if they are under 16, display the message “You can go Trick-or-Treating”

user_age = int(input("How old are you?\n"))
if user_age >= 18:
    print("You can vote")
elif user_age == 17:
    print("You can learn to drive")
elif user_age == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go Trick-or-Treating")
