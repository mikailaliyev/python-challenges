# You are going to make an on-screen version of the board game “Mastermind”. The
# computer will automatically generate four colours from a list of possible colours (it should
# be possible for the computer to randomly select the same colour more than once). For
# instance, the computer may choose “red”, “blue”, “red”, “green”. 
# This sequence should not be displayed to the user.
# After this is done the user should enter their choice of four colours from the same list the computer used. 
# For instance, they may choose “pink”, “blue”, “yellow” and “red”.
# After the user has made their selection, the program should display how many colours they
# got right in the correct position and how many colours they got right but in the wrong
# position. In the example above, it should display the message “Correct colour in the correct place: 1” 
# and “Correct colour but in the wrong place: 1”.
# The user continues guessing until they correctly enter the four colours in the order they should be in. 
# At the end of the game it should display a suitable message and tell them how many guesses they took.
import random
colors = ["black", "green", "red", "white" ]
user_selection = []
computer_selection = []
for i in range(0, 4):
    random_selection = random.randint(0, len(colors) - 1)
    computer_selection.append(colors[random_selection])
print(computer_selection)
for i in colors:
    print(i)

all_true = False
attempts = 0

while all_true == False:
    temp_list = computer_selection.copy()
    right = 0
    wrong = 0
    print()
    print("Computer has done its choices!\nIt is time to guess all of them!\n")
    for i in range(0, 4):
        user_input = input("Guess a color:\n")
        user_selection.append(user_input)

    for i in range(0, 4):
        if user_selection[i] == temp_list[i]:
            right += 1        
            temp_list[i] = 'c'
            user_selection[i] = 'u'
    for i in range(0, 4):    
        if user_selection[i] in temp_list:
            wrong += 1        
    attempts += 1
    print(f"Correct colour in the correct place: {right}\nCorrect colour but in the wrong place: {wrong}")
    print(user_selection, temp_list)
    user_selection = []

    if right == 4:
        all_true = True
        
print(f"You win!\nIt took {attempts} attemps for you to get it!")