# Create a program that will allow the user to create a new .csv file. 
# It should ask them to enter the name and age of a person 
# and then allow them to add this to the end of the file they have just created
from tkinter import *

def create_csv():
    file = open("Name&Age.csv", "w")
    file.close()
    
def save_to_csv():
    name = input_name.get()
    age = input_age.get()
    if len(name) > 0 and len(age) > 0:
        input_name.delete(0, END)
        input_age.delete(0, END)
        file = open("Name&Age.csv", "a")
        file.write(f"{name}, {age}\n")
        input_name.focus()

window = Tk()
window.title("Save to CSV")
window.geometry("250x250")


name = Label(text='Enter your name:')
name.place(x=0, y=3)

age = Label(text="Enter your age:")
age.place(x=0, y=27)

input_name = Entry(text="")
input_name.place(x=100, y=5)
input_name.focus()

input_age = Entry(text="")
input_age.place(x=100, y=30)

create_file = Button(text="Create CSV", command=create_csv)
create_file.place(x=3, y=60)

save_file = Button(text="Save to CSV", command=save_to_csv)
save_file.place(x=80, y=60)

window.mainloop()