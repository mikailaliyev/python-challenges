# Using the BookInfo database, ask the user to enter a year 
# and display all the books published after that year, 
# sorted by the year they were published
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

input_year = input("Enter a start year:\n")

cursor.execute("SELECT title, date_published FROM Books WHERE date_published > ? ORDER BY date_published", [input_year])
for i in cursor.fetchall():
    print(i)

db.close()