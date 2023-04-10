# Ask the user to enter four of their favourite foods 
# and store them in a dictionary so that they are indexed with numbers starting from 1. 
# Display the dictionary in full, showing the index number and the item. 
# Ask them which they want to get rid of and remove it from the list. 
# Sort the remaining data and display the dictionary

favorite_foods = {}
for i in range(0, 4):
    user_favorite_food = input("What is your favorite food?\n")
    favorite_foods[i] = user_favorite_food

print(favorite_foods)
disliked = int(input("Which of thesse you want to remove?\n"))
del favorite_foods[disliked]
sorted(favorite_foods.values())
print(favorite_foods)