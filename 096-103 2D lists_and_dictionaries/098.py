# Using the 2D list from program 096, ask the user which row they would like displayed 
# and display just that row. 
# Ask them to enter a new value and add it to the end of the row 
# and display the row again

nums = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Select a row you want to be displayed\n"))
print()
print(nums[row])

user_add = int(input("Enter a new value to the row\n"))
nums[row].append(user_add)
print()
print(nums[row])
