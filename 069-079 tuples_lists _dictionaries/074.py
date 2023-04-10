# Enter a list of ten colours.
# Ask the user for a starting number between 0 and 4 
# and an end number between 5 and 9. 
# Display the list for those colours between the start 
# and end numbers the user input

colors = ["black", "white", "green", "blue", "yellow", "gray", "indigo", "olive", "navy", "pink"]
starting_number = int(input("Enter a number between 0 and 4\n"))
ending_number = int(input("Enter a number between 5 and 9\n"))
print(colors[starting_number:ending_number])
