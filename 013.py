# Ask the user to enter a number that is under 20. 
# If they enter a number that is 20 or more, display the message “Too high”, 
# otherwise display “Thank you”

user_number = int(input("Enter a number under 20\n"))
if user_number >= 20:
    print("Too high")
else:
    print("Thank you")
