# Create a .csv file that will store the following data. Call it “Books.csv"
import csv

file = open("Books.csv", "w")
file.write(str("To Kill A Mockingbird, Harper Lee, 1960\n"))
file.write(str("A Brief History of Time, Stephen Hawking, 1988\n"))
file.write(str("The Great Gatsby, F. Scott Fitzgerald, 1928\n"))
file.write(str("The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"))
file.write(str("Pride and Prejudice, Jane Austen, 1813\n"))
file.close()

file = open("Books.csv", "r")
print(file.read())
file.close()
