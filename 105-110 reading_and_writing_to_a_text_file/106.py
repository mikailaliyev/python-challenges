# Create a new file called “Names.txt”. 
# Add five names to the document, which are stored on separate lines. 
# Once you have run the program, look in the location where your program is stored
# and check that the file has been created properly

file = open("Names.txt", "w")
file.write("Anna\n")
file.write("John\n")
file.write("Bunny\n")
file.write("Jessica\n")
file.write("Johnny\n")
file.close()
