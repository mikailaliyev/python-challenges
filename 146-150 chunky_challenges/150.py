# A small art gallery is selling works from different artists and wants to keep track of the paintings using an SQL database. 
# You need to create a user-friendly system to keep track of the art. 
# This should include using a GUI.
# The art gallery must be able to add new artists and pieces of art.
# Once a piece of art has been sold, the data about that art should be removed from the main SQL database 
# and stored in a separate text file.
# Users should be able to search by artist, medium or price.

from tkinter import *
import sqlite3

#------DATABASE------
with sqlite3.connect("Art_records.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Contacts(
               artist_id INTEGER PRIMARY KEY,
               name text NOT NULL,
               address text NOT NULL,
               town text,
               county text,
               postcode text NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Arts(
               piece_id INTEGER PRIMARY KEY,
               artist_id integer NOT NULL,
               title text NOT NULL,
               medium text NOT NULL,
               price text NOT NULL
)""")


contacts = [['1','Martin Leighton', '5 Park Place', 'Peterborough', 'Cambridgeshire', 'PE32 5LP'],
            ['2','Eva Czarniecka', '77 Warner Close', 'Chelmsford', 'Essex', 'CM22 5FT'],
            ['3','Roxy Parkin', '', '90 Hindhead Road', 'London', 'SE12 6WM'],
            ['4','Nigel Farnworth', '41 Whitby Road', 'Huntly', 'Aberdeenshire', 'AB54 5PN'],
            ['5','Teresa Tanner', '70 Guild Street', '', 'London', 'NW7 1SP']]

arts = [['1', '5', 'Woman with black Labrador', 'Oil', '220'],
        ['2', '5', 'Bees & thistles', 'Watercolour', '85'],
        ['3', '2', 'A stroll to Westminster', 'Ink', '190'],
        ['4', '1', 'African giant', 'Oil', '800'],
        ['5', '3', 'Water daemon', 'Acrylic', '1700'],
        ['6', '4', 'A seagull', 'Watercolour', '35'],
        ['7', '1', 'Three friends', 'Oil', '1800'],
        ['8', '2', 'Summer breeze 1', 'Acrylic', '1350'],
        ['9', '4', 'Mr Hamster', 'Watercolour', '35'],
        ['10', '1', 'Pulpit Rock, Dorset', 'Oil', '600'],
        ['11', '5', 'Trawler Dungeness beach', 'Oil', '195'],
        ['12', '2', 'Dance in the snow', 'Oil', '250'],
        ['13', '4', 'St Tropez port', 'Ink', '45'],
        ['14', '3', 'Pirate assassin', 'Acrylic', '420'],
        ['15', '1', 'Morning walk', 'Oil', '800'],
        ['16', '4', 'A baby barn swallow', 'Watercolour', '35'],
        ['17', '4', 'The old working mills', 'Ink', '395']]

for i in contacts:
    cursor.execute("""INSERT OR IGNORE INTO
                   Contacts(artist_id, name, address, town, county, postcode) 
                   VALUES(?, ?, ?, ?, ?, ?)""", i)

for i in arts:
    cursor.execute("""INSERT OR IGNORE INTO 
                   Arts(piece_id, artist_id, title, medium, price) 
                   VALUES(?, ?, ?, ?, ?)""", i)
    
db.commit()

#------FUNCTIONS------
def add_artist():
    #getting input data
    name = input_artist_name.get()
    address = input_artist_address.get()
    town = input_artist_town.get()
    county = input_artist_county.get()
    postcode = input_artist_postcode.get()
    #writing datat into database
    cursor.execute("""INSERT OR IGNORE INTO Contacts
                   (name, address, town, county, postcode) VALUES(?, ?, ?, ?, ?)""",[name, address, town, county, postcode])
    db.commit()
    
def add_art():
    #getting input data
    id = input_arts_artist_id.get()
    title = input_art_title.get()
    medium = input_art_medium.get()
    price = input_art_price.get()
    
    #writing datat into database
    cursor.execute("""INSERT OR IGNORE INTO 
                   Arts(artist_id, title, medium, price) 
                   VALUES(?, ?, ?, ?)""", [id, title, medium, price])
    db.commit()
    
def search():
    #getting input data
    name = input_search_artist_name.get()
    medium = input_search_art_medium.get()
    price = input_search_art_price.get()
    
    #searching if an input has data
    if len(name) > 0:
        cursor.execute(f"""SELECT Contacts.name, Arts.title, Arts.medium, Arts.price FROM Arts, Contacts 
                    WHERE Arts.artist_id = Contacts.artist_id AND Contacts.name = ? ORDER BY Contacts.artist_id""", [name])
    if len(medium) > 0:
        cursor.execute(f"""SELECT Contacts.name, Arts.title, Arts.medium, Arts.price FROM Arts, Contacts 
                    WHERE Arts.artist_id = Contacts.artist_id AND Arts.medium = ? ORDER BY Contacts.artist_id""", [medium])
    if len(price) > 0:
        cursor.execute(f"""SELECT Contacts.name, Arts.title, Arts.medium, Arts.price FROM Arts, Contacts 
                    WHERE Arts.artist_id = Contacts.artist_id AND Arts.price = ? ORDER BY Contacts.artist_id""", [price])
    
    #putting acquired data into Listbox
    item = 0 
    records = 0 
    for i in cursor.fetchall():
        records += 1
        i = list(i)
        results_box.insert(item + 1, ", ".join(i))
        item += 1
    results_box.insert(0, f"Found {records} records:") 
        
#------GUI------
window = Tk()
window.title("Art Gallery")
window.geometry("600x600")
window.resizable(FALSE, FALSE)

artist_part = Label(text="Artist information")
artist_part.place(x=250, y=5)

artist_name = Label(text="Artist name:")
artist_name.place(x=20, y=40)

input_artist_name = Entry()
input_artist_name.place(x=100, y=43)

artist_address = Label(text="Artist address:")
artist_address.place(x=280, y=40)

input_artist_address = Entry()
input_artist_address.place(x=380, y=43)

artist_town = Label(text="Town:")
artist_town.place(x=20, y=80)

input_artist_town = Entry()
input_artist_town.place(x=100, y=83)

artist_county = Label(text="County:")
artist_county.place(x=280, y=80)

input_artist_county = Entry()
input_artist_county.place(x=380, y=83)

artist_postcode = Label(text="Postcode:")
artist_postcode.place(x=20, y=120)

input_artist_postcode = Entry()
input_artist_postcode.place(x=100, y=123)

button_add_artist = Button(text="Add artist", command=add_artist)
button_add_artist.place(x= 380, y=119, width=125, height=25)

#Arts part
arts_part = Label(text="Art information")
arts_part.place(x=250, y=150)

arts_artist_id = Label(text="Artist ID")
arts_artist_id.place(x=20, y=180)

input_arts_artist_id = Entry()
input_arts_artist_id.place(x=100, y=183)


art_title = Label(text="Title:")
art_title.place(x=20, y=220)

input_art_title = Entry()
input_art_title.place(x=100, y=223)

art_medium = Label(text="Medium:")
art_medium.place(x=280, y=180)

input_art_medium = Entry()
input_art_medium.place(x=380, y=180)

art_price = Label(text="Price:")
art_price.place(x=280, y=220)

input_art_price = Entry()
input_art_price.place(x=380, y=223)

button_add_artist = Button(text="Add art", command=add_art)
button_add_artist.place(x= 380, y=261, width=125, height=25)

button_sold = Button(text="Sold", command=search)
button_sold.place(x= 380, y=300, width=125, height=25)


#Search and sales part
search_sales_part = Label(text="Search and Sales")
search_sales_part.place(x=250, y=320)

search_artist_name = Label(text="Artist name:")
search_artist_name.place(x=20, y=360)

input_search_artist_name = Entry()
input_search_artist_name.place(x=100, y=363)

search_art_medium = Label(text="Medium:")
search_art_medium.place(x=280, y=360)

input_search_art_medium = Entry()
input_search_art_medium.place(x=380, y=363)

search_art_price = Label(text="Price:")
search_art_price.place(x=20, y=400)

input_search_art_price = Entry()
input_search_art_price.place(x=100, y=403)


button_add_artist = Button(text="Search", command=search)
button_add_artist.place(x= 380, y=400, width=125, height=25)

results_part = Label(text="Results:")
results_part.place(x=20, y=440)

results_box = Listbox()
scrollbar = Scrollbar(results_box)
scrollbar.pack(side=RIGHT, fill=BOTH)
results_box.pack(side = LEFT, fill = BOTH)
results_box.config(yscrollcommand=scrollbar.set)
results_box.place(x=22, y=460, width=483, height=80)
scrollbar.config(command=results_box.yview)

window.mainloop()
db.close()