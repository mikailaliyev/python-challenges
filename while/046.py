# Ask the user to enter a number. 
# Keep asking until they enter a value over 5 
# and then display the message “The last number you entered was a [number]” 
# and stop the program

user_number = 0
while user_number <= 5:
    user_number = int(input("Enter a number\n"))
print(f"The last number you entered was a {user_number}")
