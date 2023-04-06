# Ask the user to enter their name and a number. 
# If the number is less than 10, then display their name that number of times; 
# otherwise display the message “Too high” three times

user_name = input("Enter your name\n")
user_number = int(input("Enter a number\n"))

if user_number < 10:
    for i in range(0, user_number):
        print(user_name)
else:
    for i in range(0, 3):
        print("Too high")
