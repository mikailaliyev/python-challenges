# Ask the user to enter three numbers. 
# Add together the first two numbers and then multiply this total by the third. 
# Display the answer as: The answer is [answer]

first_number = int(input("enter the first number:\n"))
second_number = int(input("enter the second number:\n"))
third_number = int(input("enter the third number:\n"))
print(f"The answer is {(first_number + second_number) * third_number}")
