# You need to create a program that will store the user ID and passwords for the users of a system.
# It should display the following menu
#
# 1) Create a new USER ID
# 2) Change a password
# 3) Display all USER IDs
# 4) Quit
#
# Enter Selection:
#
# If the user selects 1, it should ask them to enter a user ID. It should check if the user ID is already in the list. 
# If it is, the program should display a suitable message and ask them to select another user ID. 
# Once a suitable user ID has been entered it should ask for a password. 
# Passwords should be scored with 1 point for each of the following:
# - it should have at least 8 characters;
# - it should include uppercase letters;
# - it should include lower case letters;
# - it should include numbers; and
# - it should include at least one special character such as !, £, $, %, &, <, * or @.
#
# If the password scores only 1 or 2 it should be rejected with a message saying it is a weak password; 
# if it scores 3 or 4 tell them that “This password could be improved.” 
# Ask them if they want to try again. 
# If it scores 5 tell them they have selected a strong password. 
# Only acceptable user IDs and passwords should be added to the end of the .csv file.
# If they select 2 from the menu they will need to enter a user ID, check to see if the user ID
# exists in the list, and if it does, allow the user to change the password and save the changes
# to the .csv file. Make sure the program only alters the existing password and does not create a new record.
# If the user selects 3 from the menu, display all the user IDs but not the passwords.
# If the user selects 4 from the menu it should stop the program.
import csv

print("1) Create a new USER ID\n2) Change a password\n3) Display all USER IDs\n4) Quit")
print()

file = open("Users.csv", "a")
file.write("")
file.close()

def create_user():
    is_occupied = True
    while is_occupied == True:
        user_id = input("Enter user ID:\n")
        file = open("Users.csv", "r")
        reader = list(csv.reader(file))
        if len(reader) == 0:
            is_occupied = False
        found = ""
        for row in reader:
            if row[0] == user_id:
                print("User ID is occupied!\nYou should choose another ID!")
                found = "yes"
                break
        if found != "yes":
            is_occupied = False
        file.close()
        

    user_password = approve_password()


    #writing user id and password to csv file
    file = open("Users.csv", "a")
    file.write(f"{user_id}, {user_password}\n")
    print("Successfully recorder")
    file.close()
    

def password_raiting(raiting, user_password):
    special_chars = ["!", "£", "$", "%", "&", "<", "*", "@"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    raiting_state = {}
    
    #cheking compliance with the rules
    if len(user_password) >= 8:
        raiting += 1
        
    for letter in user_password:
        if letter.isupper():
            raiting_state["up"] = "ok"
        if letter.islower():
            raiting_state["low"] = "ok"
        if letter in special_chars:
            raiting_state["spc"] = "ok"
        if letter in str(numbers):
            raiting_state["nums"] = "ok"
    #adding all raiting check results together
    for i in raiting_state:
        if raiting_state[i] == "ok":
            raiting += 1

    return raiting

def approve_password():
    approved_pass = False
    while approved_pass == False:
        user_password = input("Enter a password:\n")
        raiting = 0
        
        #getting password raiting    
        final_raiting = password_raiting(raiting, user_password)
        if final_raiting == 1 or final_raiting == 2:
            print(f"The password is weak!\nTry again! {final_raiting}")
        elif final_raiting == 3 or final_raiting == 4:
            print(f"This password could be improved {final_raiting}")
            improve_pass = input("Do you want to try again?(y/n)\n")
            if improve_pass == "n":
                approved_pass = True
                return user_password 
        elif final_raiting == 5:
            print(f"You have selected a strong password!{final_raiting}")
            approved_pass = True
            return user_password 
    
def change_password():
    if_user_exists = input("Enter USER ID\n")
    file = open("Users.csv", "r")
    reader = csv.reader(file)
    temp_list = []
    for row in reader:
        temp_list.append(row)
        
    file.close()
    for row in temp_list:
        if temp_list[0][0] == if_user_exists:
            print("Found the USER ID!")
            new_password = input("Enter a new password:\n")
            temp_list[0][1] = new_password
            print("Password changed successfully!")
            break
        else:
            print("USER ID was not found!")
            break
    file = open("Users.csv", "w")
    for i in temp_list:
        file.write(str(i[0]) + ", " + str(i[1]).strip() + "\n")
    file.close()
    
def display_all():
    file = open("Users.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]}")
    file.close()

def main():
    exit = False
    while exit == False:
        print()
        user_selection = input("Enter Selection:\n")
        if user_selection == "1":
            create_user()   
        elif user_selection == "2":
            change_password() 
        elif user_selection == "3":
            display_all()
        elif user_selection == "4":
            print("Program terminated")
            exit = True
        else:
            print("Please choose an option from the list")

main()