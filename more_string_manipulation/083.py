# Ask the user to type in a word in upper case. 
# If they type it in lower case, ask them to try again. 
# Keep repeating this until they type in a message all in uppercase

user_word = input("Enter a word in UPPERCASE\n")
while user_word.islower():
    user_word = input("Please enter a word in UPPERCASE!\n")
print("Thank you!")
