# Alter program 129 to add a third button that will save the list to a .csv file. 
# The code tmp_list = num_list.get(0,END) 
# can be used to save the contents of a list box as a tuple called tmp_list
from tkinter import *

def check():
  user_input = input.get()
  if user_input.isdigit():
    list.insert(END, user_input)
    input.delete(0, END)
  else:
    input.delete(0, END)

def reset():
  list.delete(0, END)

def save_to_csv():
    temp_list = list.get(0, END)
    file = open("Digits.csv", "a")
    for i in temp_list:
        file.write(i + "\n")
    file.close()
    print(temp_list)

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

save_to_csv_button = Button(text="Save", command=save_to_csv)
save_to_csv_button.place(x = 270, y= 40)

list = Listbox()
list.place(x = 0, y= 80, width=320)



window.mainloop()