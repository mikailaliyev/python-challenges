# Display five colours and ask the user to pick one. 
# If they pick the same as the program has chosen, say “Well done”, 
# otherwise display a witty answer which involves the correct colour,
# e.g. “I bet you are GREEN with envy” or “You are probably feeling BLUE right now”. 
# Ask them to guess again; if they have still not got it right, 
# keep giving them the same clue 
# and ask the user to enter a colour until they guess it correctly.
import random 

colors = ["blue", "green", "gray", "black", "white"]
print("Select a color from blue, green, gray, black or white")
correct = False
color_chosen = random.choice(colors)
tip = random.choice([f"I bet you are {color_chosen} with envy" , f"You are probably feeling {color_chosen} right now"])

while correct == False:
    user_choice = input("Guess what color the programe chose\n").lower()
    if user_choice == color_chosen:
        print("Well done")
        correct = True
    else:
        print(tip)