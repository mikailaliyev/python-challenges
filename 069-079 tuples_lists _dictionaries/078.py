# Create a list containing the titles of four TV programmes 
# and display them on separate lines. 
# Ask the user to enter another show 
# and a position they want it inserted into the list. 
# Display the list again, showing all five TV programmes in their new positions

tv_titles = ["DailyNews", "BreakingNews", "Midnight Show", "Good Morning Folks"]

for i in tv_titles:
    print(i)
print()
user_favorite = input("Add your favorite show to the list\n")
position = int(input("Add its position on the list, a number between 0 and 3\n"))
tv_titles.insert(position, user_favorite)
print(tv_titles)
