# Create a program that will ask the user to enter a name 
# and then select the gender for that person from a drop-down list. 
# It should then add the name 
# and the gender (separated by a comma) to a list box when the user clicks on a button
from tkinter import *

def add():
    gender = gender_options['text']
    name = user_input.get()
    if gender != "Select your gender":
        output.insert("end", f"{name.lower().capitalize()}, {gender}")
        user_input.delete(0, END)
        select_genter.set("Select your gender")
        user_input.focus()

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
add_button.place(x=10, y=50, width=80)

output = Listbox()
output.place(x=10, y=80, width=380, height=100)
window.mainloop()