# Ask the user to enter a new password. 
# Ask them to enter it again. 
# If the two passwords match, display “Thank you”. 
# If the letters are correct but in the wrong case, display the message “They must be in the same case”,
# otherwise display the message “Incorrect”

user_password = input("Enter a new password\n")
user_password_repeated = input("Repeat the password\n")

if user_password == user_password_repeated:
    print("Thank you")
elif user_password.lower() == user_password_repeated.lower():
    print("They must be in the same case")
else:
    print("Incorrect")
