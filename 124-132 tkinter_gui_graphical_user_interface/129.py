# Create a window that will ask the user to enter a number in a text box. 
# When they click on a button it will use the code variable.isdigit() to check to see if it is a whole number. 
# If it is a whole number, add it to a list box, otherwise clear the entry box. 
# Add another button that will clear the list
from tkinter import *

def check():
  user_input = input.get()
  print(user_input.isdigit())
  if user_input.isdigit():
    list.insert(END, user_input)
    input.delete(0, END)
  else:
    input.delete(0, END)

def reset():
  list.delete(0, END)

window = Tk()
window.geometry("320x250")
window.title("Check digit")

label = Label(text="Enter a number:")
label.place(x=0, y=5)

input = Entry(text=0)
input.place(x=90, y=8)
input.focus()

button = Button(text="Check", command=check)
button.place(x = 220, y= 5)

reset_button = Button(text="Reset", command=reset)
reset_button.place(x = 270, y= 5)

list = Listbox()
list.place(x = 0, y= 60, width=320)



window.mainloop()