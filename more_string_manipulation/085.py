# Ask the user to type in their name 
# and then tell them how many vowels are in their name

vowels_count = 0
user_name = input("Enter your name\n")

for i in user_name:
    if i in 'aouei':
        vowels_count += 1

print(f"Your name consist of {vowels_count} vowels")
