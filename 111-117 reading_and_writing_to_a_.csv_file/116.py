# Import the data from the Books.csv file into a list. 
# Display the list to the user. 
# Ask them to select which row from the list they want to delete and remove it from the list. 
# Ask the user which data they want to change and allow them to change it.
# Write the data back to the original .csv file, # overwriting the existing data with the amended data
import csv 

file = csv.reader(open("Books.csv", "r"))
list = []

for i in file:
    list.append(i)    


for i in range(0, len(list)):
    print(i, list[i])

delete_row =int(input("Which row you want to delete?\n"))

del list[delete_row]

for i in range(0, len(list)):
    print(i, list[i])
change_data = int(input("Choose a row you want to change\n"))
for i in range(0, len(list[change_data])):
    print(i, list[change_data][i])

change_row_part = int(input("Which part do you want do chahge?\n"))
user_data = input("Add your data\n")
list[change_data][change_row_part] = user_data

for i in range(0, len(list)):
    print(i, list[i])

file = open("Books.csv", "w")
for i in range(0, len(list)):
    file.write(list[i][0]+', ' + list[i][1]+', ' + list[i][2]+'\n')
file.close()

file = open("Books.csv", "r")
print(file.read())
file.close()