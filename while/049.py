# Create a variable called compnum and set the value to 50. 
# Ask the user to enter a number. 
# While their guess is not the same as the compnum value, 
# tell them if their guess is too low or too high 
# and ask them to have another guess. 
# If they enter the same value as compnum, 
# display the message “Well done, you took [count] attempts”

compnum = 50
user_guess = int(input("Enter a number\n"))
count = 1
while user_guess != compnum:
    if user_guess > compnum:
        print("Too high")
    else:
        print("Too low")
    count += 1
    user_guess = int(input("Guess again\n"))
print(f"Well done, you took {count} attempts")
