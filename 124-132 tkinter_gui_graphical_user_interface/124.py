# Create a window that will ask the user to enter their name. 
# When they click on a button it should display the message “Hello” and their name 
# and change the background colour and font colour of the message box
from tkinter import *

def greet():
  user_name = entry.get()
  output['bg'] = "red"
  output["fg"] = "white"
  output['text'] = f"Hello, {user_name}"
  
window = Tk()
window.title("Ask a name")
window.geometry("360x250")

label = Label(text = "Enter your name:")
label.place(x =0 , y = 5)

entry = Entry()
entry.insert(0, "")
entry.place(x = 110, y=5)
entry['justify'] = "center"
entry.focus()

output = Message(text = "")
output.place(x = 0, y = 30, width=250, height=20)
output.configure(justify=['left'])

button = Button(text="Show greet", command=greet)
button.place(x=250, y=0)

window.mainloop()
