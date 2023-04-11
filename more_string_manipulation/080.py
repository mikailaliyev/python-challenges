# Ask the user to enter their first name 
# and then display the length of their first name. 
# Then ask for their surname and display the length of their surname. 
# Join their first name and surname together with a space between and display the result. 
# Finally, display the length of their full name (including the space)

first_name = input("Enter your first name\n")
print(f"Your first name's length is {len(first_name)}")
last_name = input("Enter your last name\n")
print(f"Your last name's length is {len(last_name)}")
full_name = first_name + " " + last_name
print(f"Your full name is {full_name}")
print(f"Your full name's length is {len(full_name)}")
