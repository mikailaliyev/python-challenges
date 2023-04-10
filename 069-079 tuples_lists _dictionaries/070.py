# Add to program 069 to ask the user to enter a number 
# and display the country in that position

country_names = ("Japan", "Korea", "USA", "Australia", "Canada")
print(country_names)
user_choice = input("Choose of the countries shown above\n")
print(f"The country you chose has the index of {country_names.index(user_choice)}")
print()
user_number = int(input("Add a number to choose a country from the list (less than 5)\n"))
print(f"The country, which index is equivalent to your number is {country_names[user_number]}")
