# Create a program that will ask the user to enter a number in a box. 
# When they click on a button it will add that number to a total 
# and display it in another box. 
# This can be repeated as many times as they want and keep adding to the total. 
# There should be another button that resets the total back to 0 and empties the original text box, ready for them to start again

from tkinter import *

def add():
  user_number = number_entry.get()
  if len(user_number) > 0:
    user_number = int(user_number)
    previous_number = output['text']
    previous_number = int(previous_number)
    total = user_number + previous_number
    output['text'] = total

def reset():
  number_entry.delete(0, END)
  output['text'] = 0
  number_entry.focus()


window = Tk()
window.title("Add")
window.geometry("250x250")

number_entry = Entry(text=0)
number_entry.place(x=0, y=0)
number_entry.focus()
output = Message(text=0)
output.place(x=0, y=50, width=50)

button = Button(text="Add to total", command=add)
button.place(x=0, y=20)

reset_button = Button(text="Reset", command=reset)
reset_button.place(x = 80, y=20)
window.mainloop()
