# Change program 136 so that when a new name and gender is added to the list box 
# it is also written to a text file. 
# Add another button that will display the entire text file in the main Python shell window
from tkinter import *

def add():
    gender = gender_options['text']
    name = user_input.get()
    if gender != "Select your gender":
        file = open("Name&age.csv", "a")
        file.write(name + ", " + gender + "\n")
        file.close()
        output.insert("end", f"{name.lower().capitalize()}, {gender}")
        user_input.delete(0, END)
        select_genter.set("Select your gender")
        user_input.focus()

def show_from_csv():
    file = open("Name&age.csv", "r")
    print(file.read())
    file.close()

window = Tk()
window.title("Name&gender")
window.geometry("400x200")

label_name = Label(text="Enter your name: ")
label_name.place(x=10, y = 10)

user_input = Entry(text="")
user_input.place(x=110, y=13)
user_input.focus()

select_genter = StringVar(window)
select_genter.set("Select your gender")
gender_options = OptionMenu(window, select_genter, "male", "female")
gender_options.place(x=240, y=8)

add_button = Button(text="Add", command=add)
add_button.place(x=10, y=50, width=120)

show_csv_button = Button(text="Show from csv", command=show_from_csv)
show_csv_button.place(x=140, y=50, width=120)

output = Listbox()
output.place(x=10, y=80, width=380, height=100)
window.mainloop()
