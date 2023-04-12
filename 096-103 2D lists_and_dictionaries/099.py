# Change your previous program to ask the user which row they want displayed. 
# Display that row. 
# Ask which column in that row they want displayed 
# and display the value that is held there. 
# Ask the user if they want to change the value. 
# If they do, ask for a new value 
# and change the data. 
# Finally, display the whole row again

nums = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Select a row you want to be displayed\n"))
print()
print(nums[row])

column = int(input("Which column you want to be displayed?\n"))
print()
print(nums[row][column])

user_change = input("Do you want to change the value? (y/n)\n")
if user_change == 'y':
    user_value = int(input("Enter a new value\n"))
    nums[row][column] = user_value

print(nums[row])
