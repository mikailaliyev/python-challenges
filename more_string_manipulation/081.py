# Ask the user to type in their favourite school subject.
# Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-

user_favorite = input("Enter your favorite school subject\n")
for i in user_favorite:
    print(i, end="-")
