# Using the BookInfo database from program 141, 
# display the list of authors and their place of birth. 
# Ask the user to enter a place of birth 
# and then show the title, date published 
# and author’s name for all the books by authors who were born in the location they selected
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for i in cursor.fetchall():
    print(i)
    
birth_place = input("Enter a place of birth:\n")
cursor.execute("""SELECT Books.title, Books.date_published, Authors.name 
               FROM Authors, Books WHERE Authors.name=Books.author AND Authors.place_of_birth=?""", [birth_place])
for i in cursor.fetchall():
    print(i)

db.close()