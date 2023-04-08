# Ask for a number below 50 and then count down from 50 to that number, 
# making sure you show the number they entered in the output

user_number = int(input("Enter a number below 50\n"))

for i in range(50, user_number - 1,  -1):
    print(i)
