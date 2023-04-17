# Create a program that will allow the user to easily manage a list of names. 
# You should display a menu that will allow them to add a name to the list, change a name in the list, 
# delete a name from the list or view all the names in the list. 
# There should also be a menu option to allow the user to end the program. 
# If they select an option that is not relevant, then it should display a suitable message. 
# After they have made a selection to either add a name, change a name, delete a name or view all the names, 
# they should see the menu again without having to restart the program. 
# The program should be made as easy to use as possible

names = ["John", "Bishop"]

def options():
  user_select = input("1) Add to list\n2) Change a name\n3) Delete a name\n4) View all names\n5) End program\n")
  return user_select

def display_names():
  print("----")
  for i in range(0, len(names)):
    print(i, names[i])
  print("----")
  main()
  
def add():
  print("----")
  new_name = input("Enter a name to add\n")
  names.append(new_name)
  print("New name successfully added")
  print("----")
  main()
  
def change():
  print("----")
  for i in range(0, len(names)):
    print(i, names[i])
  print("----")
  change_name = int(input("Choose a name's number to change\n"))
  new_name = input("Enter a new name\n")
  names[change_name] = new_name
  print("The name successfully changed")
  print("----")
  main()
  
def delete():
  print("----")
  for i in range(0, len(names)):
    print(i, names[i])
  print("----")
  change_name = int(input("Choose a name's number to delete\n"))
  del names[change_name]
  print("The name successfully deleted")
  print("----")
  main()



def main():
  user_select = options()
  if user_select == "1":
    add()
  elif user_select == "2":
    change()
  elif user_select == "3":
    delete()
  elif user_select == "4":
    display_names()
  elif user_select == "5":
    print("----")
    print("Program terminated")
    print("----")
  else:
    print("----")
    print("Please choose an option from the list")
    print("----")
    main()

main()
