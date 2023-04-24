# Using the BookInfo database, ask the user for an author’s name 
# and then save all the books by that author to a text file, 
# with each field separated by dashes so it looks as follows:
#
# 5 - Murder of the Orient Express - Agatha Christie - 1934
# 8 - The murder of the links - Agatha Christie - 1923
# 10 - The secret adversary - Agatha Christie - 1921
# 11 - The seven dials mistery - Agatha Christie - 1929
#
# Open the text file to make sure it has worked correctly.
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
    
author_name = input("Enter author name:\n")
cursor.execute("SELECT * FROM Books WHERE author = ?", [author_name])
for i in cursor.fetchall():
    file = open("Authors.txt", "a")
    newList = list(i)
    file.write(f"{newList[0]} - {newList[1]} - {newList[2]} - {newList[3]}\n")
    file.close()
    
file = open("Authors.txt", "r")
print(file.read())
file.close()
db.close()