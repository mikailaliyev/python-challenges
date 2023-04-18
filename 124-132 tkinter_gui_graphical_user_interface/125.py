# Write a program that can be used instead of rolling a six-sided die in a board game. 
# When the user clicks a button it should display a random whole number between 1 to 6 (inclusive)
from tkinter import *
import random

def dice_roll():
  rand_num = random.randint(1, 6)
  textbox['text'] = rand_num

window = Tk()
window.geometry("250x250")
textbox = Message(text="Push the button to roll the dice")
textbox.place(x=0, y=0)
button = Button(text="Push me", command=dice_roll)
button.place(x=10, y=150)
window.mainloop()
