# Show the user a line of text from your favourite poem
# and ask for a starting and ending point. 
# Display the characters between those two points

favorite_line = "To be, or not to be, that is the question"
print(favorite_line)

start_point = int(input(f"Enter a number between 0 and {len(favorite_line)}\n"))
end_point = int(input(f"Enter a number between 0 and {len(favorite_line)}\n"))
print(favorite_line[start_point:end_point])
