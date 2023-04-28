from tkinter import *

def view():
    user_number = input.get()
    if user_number and user_number.isdigit():
        user_number = int(user_number)
        for i in range(1, 13):
            result = i * user_number
            list.insert(END, f"{i} * {user_number} = {result}")
        input.delete(0, END)
        input.focus()
        

def clear():
    list.delete(0, END)
    input.delete(0, END)
    input.focus()

def clear_input(e):
    input.delete(0, END)

def update_input(e):
    input.insert(0,"only positive integers")

window = Tk()
window.geometry("450x350")
window.title("Times table")

label = Label(text="Enter a number:")
label.place(x=20, y=40)

input = Entry()
input.place(x=113, y=40, width=200, height=25)
input.insert(0, "only positive integers")
input.bind("<FocusIn>", clear_input)
input.bind("<FocusOut>", update_input)
#input.focus()

list = Listbox()
list.place(x=112, y=70, width=200, height=250)

view_button = Button(text="View Times Table", command=view)
view_button.place(x=320, y=39, height=28, width=110)

clear_button = Button(text="Clear", command=clear)
clear_button.place(x=320, y=72, height=28, width=110)
window.mainloop()
