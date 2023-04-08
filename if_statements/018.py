# Ask the user to enter a number. 
# If it is under 10, display the message “Too low”, 
# if their number is between 10 and 20, display “Correct”, 
# otherwise display “Too high”.

user_number = int(input("Guess a number\n"))
if user_number < 10:
    print("Too low")
elif user_number > 10 and user_number < 20:
    print("Correct")
else:
    print("Too high")
