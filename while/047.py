# Ask the user to enter a number and then enter another number. 
# Add these two numbers together and then ask if they want to add another number. 
# If they enter “y", ask them to enter another number 
# and keep adding numbers until they do not answer “y”. 
# Once the loop has stopped, display the total


first_number = int(input("Enter a number\n"))
total = first_number
user_answer = "y"

while user_answer == "y":
    user_number = int(input("Enter another number\n"))
    total += user_number
    user_answer = input("Would you like to add a number? (y/n)\n")
print(f"The total is: {total}")
