# 1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres. 
# Using these figures, make a program that will allow the user to convert between miles and kilometres
from tkinter import *

def convert():
  user_km_ml = input_km_ml.get()
  user_ml_km = input_ml_km.get()
  if len(user_km_ml) > 0:
    user_km_ml = int(user_km_ml)
    miles = user_km_ml * 0.6214
    input_km_ml.delete(0, END)
    label['text'] = f"Result: {miles} miles\n"
  elif len(user_ml_km) > 0:
    user_ml_km = int(user_ml_km)
    kilometers = user_ml_km * 1.6093
    input_ml_km.delete(0, END)
    label['text'] = f"Result: {kilometers} kilometers\n"
    
window = Tk()
window.title("Miles/kilometers converter")
window.geometry("300x100")
window.resizable(False, False)

label_km_ml = Label(text="Kilometers to miles:")
label_km_ml.place(x=0, y=0)
input_km_ml = Entry(text="")
input_km_ml.place(x=110, y=2)
input_km_ml.focus()

label_ml_km = Label(text="Miles to kilometers:")
label_ml_km.place(x=0, y=20)
input_ml_km = Entry(text="")
input_ml_km.place(x=110, y=22)

label = Label(text="Result: ")
label.place(x=0, y=60)

convert_button = Button(text="Convert", command=convert)
convert_button.place(x=240, y=8)
window.mainloop()
