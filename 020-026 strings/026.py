# Pig Latin takes the first consonant of a word, 
# moves it to the end of the word and adds on an “ay”. 
# If a word begins with a vowel you just add “way” to the end. 
# For example, pig becomes igpay, banana becomes ananabay, 
# and aadvark becomes aadvarkway. 
# Create a program that will ask the user to enter a word and change it into Pig Latin.
# Make sure the new word is displayed in lower case

user_input = input("Enter a word to change it into Pig Latin\n")
vowels = "aeiou"
if user_input[0] in vowels:
    print(user_input + "way")
else:
    print(user_input[1:] + user_input[0] + "ay")