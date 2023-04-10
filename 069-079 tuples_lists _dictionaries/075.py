# Create a list of four three-digit numbers. 
# Display the list to the user, showing each item from the list on a separate line. 
# Ask the user to enter a three-digit number. 
# If the number they have typed in matches one in the list, 
# display the position of that number in the list, 
# otherwise display the message “That is not in the list”

numbers = [233, 433, 667, 980]
for i in numbers:
    print(i)

user_number = int(input("Enter a trhee-digit number\n"))
if user_number in numbers:
    print(f"{user_number} has index of {numbers.index(user_number)}")
else:
    print("That is not in the list")