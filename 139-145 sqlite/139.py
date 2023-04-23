# Create an SQL database called PhoneBook that contains a table called Names
import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()
    
cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
    id integer PRIMARY KEY,
    FirstName text NOT NULL,
    LastName text NOT NULL,
    Phone_Number text NOT NULL);""")

values = [("1", "Simon", "Howels", "01223 349752"),
          ("2", "Karen",  "Phillips", "01954 295773"),
          ("3", "Darren", "Smith", "01583 749012"),
          ("4", "Anne", "Jones", "01323 567322"),
          ("5", "Mark", "Smith", "01223 855534")]

for i in values:
    cursor.execute("INSERT INTO Names VALUES(?, ?, ?, ?)", i)
db.commit()
db.close()