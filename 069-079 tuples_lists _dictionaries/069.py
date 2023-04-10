# Create a tuple containing the names of five countries and display the whole tuple. 
# Ask the user to enter one of the countries that have been shown to them 
# and then display the index number (i.e. position in the list) of that item in the tuple

country_names = ("Japan", "Korea", "USA", "Australia", "Canada")
print(country_names)
user_choice = input("Choose of the countries shown above\n")
print(f"The country you chose has the index of {country_names.index(user_choice)}")
