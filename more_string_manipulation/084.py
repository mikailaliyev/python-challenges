# Ask the user to type in their postcode. 
# Display the first two letters in uppercase

user_postcode = input("Enter your post code\n")
print(f"Your postcode is {user_postcode[:2].upper() + user_postcode[2:]}")
