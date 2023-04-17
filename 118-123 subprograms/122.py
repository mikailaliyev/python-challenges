# Create the following menu: 
# 1) Add to file
# 2) View all records
# 3) Quit program
# If the user selects 1, allow them to add to a file called Salaries.csv which will store their name and salary. 
# If they select 2 it should display all records in the Salaries.csv file. 
# If they select 3 it should stop the program. 
# If they select an incorrect option they should see an error message. 
# They should keep returning to the menu until they select option 

def add():
  file = open("Salaries.csv", "a")
  name = input("Enter your name\n")
  salary = input("Enter your salary\n")
  file.write(name + ", " + salary + "\n")
  file.close()

def all_records():
  file = open("Salaries.csv", "r")
  for i in file:
    print(i)
  file.close()
  
  
def main():
  restart = True
  while restart:
    user_choice = input("1) Add to file\n2) View all records\n3) Quit program\n")
    if user_choice == "1":
      add()
    elif user_choice == "2":
      all_records()
    elif  user_choice == "3":
      print("Program terminated")
      restart = False
    else:
      print("Choose an option, please")

main()
