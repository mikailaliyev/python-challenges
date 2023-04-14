# Using the Books.csv file from program 111, ask the user to enter another record 
# and add it to the end of the file. 
# Display each row of the .csv file on a separate line
import csv

file = open("Books.csv", "r")
print(file.read())
file.close()

new_title = input("Enter a title: ")
new_author = input("Enter an author: ")
new_year = input("Enter a release year: ")
file = open("Books.csv", "a")
file.write(str(new_title + ", " + new_author + ", " + new_year + "\n"))
file.close()

file = open("Books.csv", "r")
for i in file:
    print(i)
file.close()
