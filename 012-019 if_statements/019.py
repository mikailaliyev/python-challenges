# Ask the user to enter 1, 2 or 3. 
# If they enter a 1, display the message “Thank you”, 
# if they enter a 2, display “Well done”, 
# if they enter a 3, display “Correct”. 
# If they enter anything else, display “Error message”

user_number = int(input("Enter 1, 2 or 3\n"))
if user_number == 1:
    print("Thank you")
elif user_number == 2:
    print("Well done")
elif user_number == 3:
    print("Correct")
else:
    print("Error message")
