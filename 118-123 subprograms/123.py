# Change the previous program to allow you to do changes. 
# Your menu should now look like this
# 1) Add to file
# 2) View all records
# 3) Delete a record
# 4) Quit program
import csv 

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
  
def delete():
  file = open("Salaries.csv", "r")
  temp = []
  
  for i in file:
    temp.append(i)
  file.close() 
  
  x = 0
  for i in temp:
    print(x, i)
    x += 1
  
  user_choice = int(input("Choose a row to delete\n"))
  del temp[user_choice]
  file = open("Salaries.csv", "w")
  for i in temp:
    file.write(i)
  file.close()
    
def main():
  restart = True
  while restart:
    user_choice = input("1) Add to file\n2) View all records\n3) Delete a record\n4) Quit program\n\nEnter the number of your selection:\n")
    if user_choice == "1":
      add()
    elif user_choice == "2":
      all_records()
    elif user_choice == "3":
      delete()
    elif  user_choice == "4":
      print("Program terminated")
      restart = False
    else:
      print("Choose an option, please")

main()
