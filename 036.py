# Alter program 035 so that it will ask the user to enter their name and a number 
# and then display their name that number of times.

user_name = input("Enter your name\n")
iteration_count = int(input("Enter a number you want it to be repeated\n"))
for i in range(0, iteration_count):
    print(user_name)
