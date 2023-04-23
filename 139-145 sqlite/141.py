# Create a new SQL database called BookInfo that will store a list of authors and the books they wrote.
# It will have two tables. The first one should be called Authors 
# The second should be called Books
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
    
cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
    name text PRIMARY KEY,
    place_of_birth text NOT NULL);""")

values_for_authors = [("Agatha Christie", "Torquay"),
                      ("Cecelia Ahern", "Dublin"),
                       ("J.K.Rowling", "Bristol"),
                       ("Oscar Wilde", "Dublin")]
for i in values_for_authors:
    cursor.execute("INSERT INTO Authors VALUES(?, ?)", i)
db.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
    id integer PRIMARY KEY,
    title text NOT NULL,
    author text NOT NULL,
    date_published integer NOT NULL);""")

values_for_books = [("1", "De Profundis", "Oscar Wilde", "1905"),
                      ("2", "Harry Potter and the chamber of secrets", "J.K. Rowling", "1998"),
                      ("3", "Harry Potter and the prisoner of Azkaban", "J.K. Rowling", "1999"),
                      ("4", "Lyrebird", "Cecelia Ahern", "2017"),
                      ("5", "Murder of the Orient Express", "Agatha Christie", "1934"),
                      ("6", "Perfect", "Cecelia Ahern", "2017"),
                      ("7", "The marble collector", "Cecelia Ahern", "2016"),
                      ("8", "The murder of the links", "Agatha Christie", "1923"),
                      ("9", "The picture of Dorian Grey", "Oscar Wilde", "1890"),
                      ("10", "The secret adversary", "Agatha Christie", "1921"),
                      ("11", "The seven dials mistery", "Agatha Christie", "1929"),
                      ("12", "The year I met you", "Cecelia Ahern", "2014")]
for i in values_for_books:
    cursor.execute("INSERT INTO Books VALUES(?, ?, ?, ?)", i)
db.commit()
db.close()