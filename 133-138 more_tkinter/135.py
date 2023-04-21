# Create a simple program that shows a drop-down list containing several colours and a Click Me button. 
# When the user selects a colour from the list 
# and clicks the button it should change the background of the window to that colour. 
# For an extra challenge, try to avoid using an if statement to do this
from tkinter import *

def update_color():
    window_color = color_list["text"]
    window.configure(background=window_color)
    print(color_list['text'])

window = Tk()
window.title("Change color")
window.geometry("250x250")

select_color = StringVar(window)
select_color.set("red")
color_list = OptionMenu(window, select_color, "green", "blue", "yellow")
color_list.place(x=10, y=10, width=150)

button = Button(text="Change the color", command=update_color)
button.place(x=10, y=50)

window.mainloop()