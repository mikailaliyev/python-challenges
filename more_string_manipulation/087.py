# Ask the user to type in a word and then display it backwards on separate lines. 
# For instance, if they type in “Hello” it should display as shown below:
# -> Hello
# -> o
# -> l
# -> l
# -> e
# -> H

user_word = input("Enter a word\n")
for i in range(0, len(user_word)):
    print(user_word[len(user_word) -1 - i])
