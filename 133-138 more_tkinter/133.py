# Create your own icon that consists of several vertical multi-coloured lines. 
# Create a logo which measures 200 x 150, using Paint or another graphics package. 
# Create the following window using your own icon and logo.
# When the user enters their name and clicks on the Press Me button it should display “Hello” 
# and their name in the second text box
from tkinter import *

def greet():
  name = user_name.get()
  user_greet['text'] = f"Hello {name}"
  

window =Tk()
window.title("Greet user")
window.geometry("300x300")
window.wm_iconbitmap("Logo.ico")
window.configure(background="black")

label = Label(text="Enter your name: ")
label.configure(background="black", foreground="white")
label.place(x=2, y=170)

user_name = Entry(text="")
user_name.place(x=100, y=172, width=180)

photo =PhotoImage(file="image.png")
photo_box = Label(image=photo)
photo_box.place(x=50, y=20, width=200)

press_button = Button(text="Press Me", command=greet)
press_button.place(x=2, y=202, width=90, height=20)

user_greet = Message(text="")
user_greet.place(x=100, y=202, width=180, height=20)

window.mainloop()
