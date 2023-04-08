# Ask the user to enter their first name. 
# If the length of their first name is under five characters, 
# ask them to enter their surname and join them together (without a space) and display the name in upper case. 
# If the length of the first name is five or more characters, display their first name in lower case.

first_name = input("Enter your first name\n")
if len(first_name) < 5:
    last_name = input("Enter your last name\n")
    full_name = (first_name + last_name).upper()
    print(full_name)
else:
    print(first_name.lower())
