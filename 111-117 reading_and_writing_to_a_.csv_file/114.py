# Using the Books.csv file, ask the user to enter a starting year and an end year. 
# Display all books released between those two years
import csv

file = open("Books.csv", "r")
print(file.read())
file.close()
starting_year = int(input("Enter a starting year\n"))
end_year = int(input("Enter an end year\n"))

print()
found = 0
file = open("Books.csv", "r")
reader = csv.reader(file)
list = []
for i in reader:
  list.append(i)

for i in range(0, len(list)):
    if int(list[i][2]) >= starting_year and int(list[i][2]) <= end_year:
      print(list[i])
      found += 1
if found == 0:
    print("There is no records in the list")

print(f"---\n{found} records founded\n---\n")
