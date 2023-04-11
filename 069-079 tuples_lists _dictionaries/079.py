# Create an empty list called “nums”. 
# Ask the user to enter numbers. 
# After each number is entered, add it to the end of the nums list 
# and display the list. 
# Once they have entered three numbers, ask them if they still want the last number they entered saved. 
# If they say “no”, remove the last item from the list.
# Display the list of numbers

nums = []

for i in range(0, 3):
    user_input = int(input("Enter a number\n"))
    nums.append(user_input)
    print(nums)
    print()

still_want = input(f"Do you still want {nums[-1]} in the list?\n")
if still_want == "no":
    nums.remove(nums[-1])

print(nums)
