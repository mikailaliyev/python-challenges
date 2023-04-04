# Ask the user to type in the first line of a nursery rhyme and display the length of the string.
# Ask for a starting number and an ending number and then display just that section of the text 

nursery_rhyme = input("Enter the first line of a nursery rhyme\n")
print(len(nursery_rhyme)
starting_number = int(input("Enter a starting number\n"))
ending_number = int(input("Enter an ending number\n"))
print(nursery_rhyme[starting_number: ending_number])
