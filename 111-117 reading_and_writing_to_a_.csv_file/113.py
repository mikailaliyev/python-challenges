# Using the Books.csv file, ask the user how many records they want to add to the list 
# and then allow them to add that many. 
# After all the data has been added, ask for an author 
# and display all the books in the list by that author. 
# If there are no books by that author in the list, display a suitable message
import csv

file = open("Books.csv", "r")
print(file.read())
file.close()

record_count = int(input("How many records do you want to add?\n"))

file = open("Books.csv", "a")
for i in range(0, record_count):
    new_title = input("Enter a title: ")
    new_author = input("Enter an author: ")
    new_year = input("Enter a release year: ")
    file.write(str(new_title + ", " + new_author + ", " + new_year + "\n"))
file.close()
print()
what_author = input("Enter an author name to search\n")
file = open("Books.csv", "r")
print()
found = 0
for i in file:
    if what_author in i:
        found += 1
        print(i)
        
if found == 0:
    print("There is no such an author in the list")

print(f"---\n{found} records founded\n---\n")
