# Ask the user to enter a number between 1 and 12 and then display the times table for that number

user_number = int(input("Enter a number between 1 and 12\n"))

for i in range(0, 13):
    print(f"{i} * {user_number} = {i * user_number}")
