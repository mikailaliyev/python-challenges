# Create a new program that will generate two random whole numbers between 10 and 50. 
# It should ask the user to add the numbers together and type in the answer. 
# If they get the question correct, display a suitable image such as a tick; 
# if they get the answer wrong, display another suitable image such as a cross. 
# They should click on a Next button to get another question
import random
from tkinter import *
random_one = random.randint(10, 50)
random_two = random.randint(10, 50)

def random_numbers():
    random_one = random.randint(10, 50)
    random_two = random.randint(10, 50)
    return random_one, random_two

def check_result():
    user_answer = input_result.get()
    if len(user_answer) > 0:
        user_answer = int(user_answer)
        total = random_one + random_two
        input_result.delete(0, END)
        if user_answer == total:
            answer_image = PhotoImage(file = "./133-138 more_tkinter/134_images/tick.png")
            photo_indicator.image = answer_image
        else:
            answer_image = PhotoImage(file = "./133-138 more_tkinter/134_images/cross.png")
            photo_indicator.image = answer_image
        photo_indicator['image'] = answer_image
        photo_indicator.update()    


def next_challenge():
    global random_one, random_two
    random_one, random_two = random_numbers()
    label["text"] = f"{random_one} + {random_two} = ?"
    answer_image = PhotoImage(file = "")
    photo_indicator.image = answer_image
    photo_indicator['image'] = answer_image
    photo_indicator.update()    

window = Tk()
window.title("Adding random numbers")
window.geometry("350x150")
window.resizable(FALSE, FALSE)

label = Label(text=f"{random_one} + {random_two} = ?")
label.place(x=10, y=5)

message = Label(text="Enter the result: ")
message.place(x=10, y=40)

input_result = Entry(text="")
input_result.place(x=100, y=42)
input_result.focus()

check_button = Button(text="Check", command=check_result)
check_button.place(x=10, y=80, width=80)

next_button = Button(text="Next", command=next_challenge)
next_button.place(x=100, y=80, width=80)

answer_image = PhotoImage(file="")
photo_indicator = Label(image=answer_image)
photo_indicator.image = answer_image
photo_indicator.place(x=250, y=30, width=50, height=50)

window.mainloop()