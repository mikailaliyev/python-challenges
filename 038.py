# Change program 037 to also ask for a number. 
# Display their name (one letter at a time on each line) 
# and repeat this for the number of times they entered

user_name = input("Enter your name\n")
iteration_count = int(input("Enter a number of times you want it to be repeated\n"))
for i in range(0, iteration_count):
    for i in user_name:
        print(i)
