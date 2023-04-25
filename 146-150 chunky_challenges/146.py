# A shift code is where a message can be easily encoded and is one of the simplest codes to use. 
# Each letter is moved forwards through the alphabet a set number of letters to be represented by a new letter. 
# For instance, “abc” becomes “bcd” when the code is shifted by one 
# (i.e. each letter in the alphabet is moved forward one character)
#
# If the user selects 1, they should be able to type in a message (including spaces) and then enter a number. 
# Python should then display the encoded message once the shift code has been applied.
# If the user selects 2, they should enter an encoded message 
# and the correct number and it should display the decoded message 
# (i.e. move the correct number of letters backwards through the alphabet).
# If they select 3 it should stop the program from running.
# After they have encoded or decoded a message the menu should be
# displayed to them again until they select quit


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

def encode():
    user_letters = input("Enter letters:\n").lower()
    user_number = int(input("Enter a shift number:\n"))
    new_letter = ""
    for i in user_letters:        
        total_index = alphabet.index(i) + user_number
        if total_index > len(alphabet) - 1:
            total_index = total_index % len(alphabet)
        encoded = alphabet[total_index]
        new_letter += encoded
    return new_letter

def decode():
    user_letters = input("Enter letters:\n").lower()
    user_number = int(input("Enter a shift number:\n"))
    new_letter = ""
    alphabet.reverse()
    for i in user_letters:        
        total_index = alphabet.index(i) + user_number
        if total_index > len(alphabet) - 1:
            total_index = total_index % len(alphabet)
        encoded = alphabet[total_index]
        new_letter += encoded
    return new_letter

quit = False

while quit == False:
    print("1) Make a code")
    print("2) Decode a message")
    print("3) Quit")
    print()
    user_selection = input("Enter your selection:\n")
    if user_selection == "1":
        encoded = encode()
        print(encoded)
    elif user_selection == "2":
        decoded = decode()
        print(decoded)
    elif user_selection == "3":
        quit = True
    else: 
        print("Please select one option")

