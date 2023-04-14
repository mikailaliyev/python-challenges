# Using the Books.csv file, display the data in the file along with the row number of each
import csv

file = open("Books.csv", "r")
line_number = 0
for i in file:
  line = f"row {line_number} - {i}"
  print(line)
  line_number += 1
  
file.close()
