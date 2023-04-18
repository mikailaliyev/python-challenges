# Create a window that will ask the user to enter a name in a text box. 
# When they click on a button it will add it to the end of the list that is displayed on the screen. 
# Create another button which will clear the list

from tkinter import *
def add():
    user_name = input.get()
    if len(user_name) > 0:
        names.append(user_name)
        input.delete(0, END)
        output['text'] += f"{names[-1]}\n"  

def delete():
    names.clear()
    output['text'] = ""
    print(names)

names = []

window = Tk()
window.title("Names")
window.geometry("400x400")

label = Label(text="Enter your name:")
label.place(x=0, y=5)

input = Entry(text = "")
input.place(x=100, y=5)
input.focus()


add_button = Button(text="Add", command=add, width=5)
add_button.place(x=250, y=0)

delete_button = Button(text="Delete", command=delete, width=5)
delete_button.place(x=300, y=0)

output = Message(text="")
output.place(x=0, y=50)

window.mainloop()