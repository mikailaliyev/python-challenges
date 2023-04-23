# Using the PhoneBook database from program 139, write a program that will display the following menu:
# Main Menu
# 1) View phone book
# 2) Add to phone book
# 3) Search for last name
# 4) Delete person from phone book
# 5) Quit
# If the user selects 1, they should be able to view the entire phonebook.
# If they select 2, it should allow them to add a new person to the phonebook. 
# If they select 3, it should ask them for a last name 
# and then display only the records of people with the same last name. 
# If they select 4, it should ask for an ID and then delete that record from the table. 
# If they select 5, it should end the program. 
# Finally, it should display a suitable message if they enter an incorrect selection from the menu.
# They should return to the menu after each action, until they select 5
import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()
    
print("Main Menu")

logout = False
while logout == False:
    print()
    print("Select option from menu\n")
    user_choice = input("1) View phone book\n2) Add to phone book\n3) Search for last name\n4) Delete person from phone book\n5) Quit\n")
    if user_choice == "1":
        cursor.execute("SELECT * FROM Names")
        for i in cursor.fetchall():
            print(i)
    elif user_choice == "2":
        newID = input("Enter new ID:\n")
        newName = input("Enter new name:\n")
        newLastName = input("Enter new last name:\n")
        newPhoneNumber = input("Enter new phone number:\n")
        cursor.execute("INSERT INTO Names VALUES(?,?,?,?)", (newID, newName, newLastName, newPhoneNumber))
        db.commit()
    elif user_choice == "3":
        searchLastName = input("Enter last name to search:\n")
        cursor.execute("SELECT * FROM Names WHERE LastName=?", [searchLastName])
        for i in cursor.fetchall():
            print(i)
    elif user_choice == "4":
        delete_name = input("Enter id delete:\n")
        cursor.execute("DELETE FROM Names WHERE id=?", [delete_name])
        db.commit()
    elif user_choice == "5":
        print("Program executed")
        logout = True
    else:
        print("You made wrong choice!\n")

db.close()