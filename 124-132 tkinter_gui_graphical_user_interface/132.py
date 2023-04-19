# Using the .csv file you created for the last challenge, 
# create a program that will allow people to add names and ages to the list
# and create a button that will display the contents of the .csv file by importing it to a list box
from tkinter import *

def results():
    output.delete(0, END)
    file = open("Name&Age.csv", "r")
    for i in file:
        output.insert(END, i)        
    file.close()
    
def save_to_csv():
    name = input_name.get()
    age = input_age.get()
    if len(name) > 0 and len(age) > 0:
        input_name.delete(0, END)
        input_age.delete(0, END)
        file = open("Name&Age.csv", "a")
        file.write(name + ", " + age + "\n")
        input_name.focus()

window = Tk()
window.title("Save to CSV")
window.geometry("250x250")
window.resizable(FALSE, FALSE)


name = Label(text='Enter your name:')
name.place(x=0, y=3)

age = Label(text="Enter your age:")
age.place(x=0, y=27)

input_name = Entry(text="")
input_name.place(x=100, y=5)
input_name.focus()

input_age = Entry(text="")
input_age.place(x=100, y=30)

show_results = Button(text="Show results", command=results)
show_results.place(x=3, y=60)

save_file = Button(text="Save to CSV", command=save_to_csv)
save_file.place(x=80, y=60)

output = Listbox()
output.place(x=2, y=90, height=155)

window.mainloop()