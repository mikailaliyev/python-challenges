# Create a list of two sports. 
# Ask the user what their favourite sport is 
# and add this to the end of the list. 
# Sort the list and display it

sports_list = ["Basketball", "Football"]
user_favorite = input("What is your favorite sport?\n").capitalize()
sports_list.append(user_favorite)
sports_list.sort()
print(sports_list)
