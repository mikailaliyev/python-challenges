# Ask the user for their name and their age. 
# Add 1 to their age and display the output: [Name] next birthday you will be [new age].

user_name = input("What is your name?\n").lower().capitalize()
user_age = int(input("How old are you?\n"))
new_age = user_age + 1
print(f"{user_name} next birthday you will be {new_age}")
