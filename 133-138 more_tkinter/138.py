# Save several images in the same folder as your program 
# and call them 1.gif, 2.gif, 3.gif, etc. 
# Make sure they are all .gif files. 
# Display one in a window and ask the user to enter a number. 
# It should then use that number to choose the correct file name and display the correct image
from tkinter import *

def select():
    user_select = user_input.get()
    print(user_select)
    if user_select == "1":
        image = PhotoImage(file="./133-138 more_tkinter/138_images/1.gif")
        image_box.image = image
    elif user_select == "2":
        image = PhotoImage(file="./133-138 more_tkinter/138_images/2.gif")
        image_box.image = image
    elif user_select == "3":
        image = PhotoImage(file="./133-138 more_tkinter/138_images/3.gif")
        image_box.image = image
    image_box['image'] = image
    image_box.update()
window = Tk()
window.title("Choosing images")
window.geometry("450x350")

label = Label(text="Enter a number from 1 to 3: ")
label.place(x=10, y=10)

user_input = Entry()
user_input.place(x=170, y=13)
user_input.focus()

select_button = Button(text="Pick image", command=select)
select_button.place(x=300, y=10)


image = PhotoImage(file="./133-138 more_tkinter/138_images/1.gif")
image_box = Label(image=image)
image_box.image = image
image_box.place(x = 10, y= 60)

window.mainloop()