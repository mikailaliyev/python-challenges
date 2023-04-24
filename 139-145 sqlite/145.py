# Create a program that displays input options to db:
# It should save the data to an SQL database called
# TestScores when the Add button is clicked. 
# The Clear button should clear the window
from tkinter import *
import sqlite3

with sqlite3.connect("TestScores.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Results(
    id INTEGER PRIMARY KEY,
    student_name text NOT NULL,
    student_grade integer NOT NULL
    )""")    

def add():
    name = input_name.get()
    grade = input_grade.get()
    cursor.execute("INSERT INTO Results(student_name, student_grade) VALUES(?, ?)", (name, grade))
    db.commit()
    
def clear():
    input_name.delete(0, END)
    input_grade.delete(0, END)
    input_name.focus()

window = Tk()
window.geometry("380x210")
window.title("TestScores")
window.resizable(FALSE, FALSE)

label_name = Label(text="Enter student's name:")
label_name.place(x=40, y=40)

input_name = Entry()
input_name.place(x=160, y=43, width=150)
input_name.focus()

label_grade = Label(text="Enter student's grade:")
label_grade.place(x=40, y=80)

input_grade = Entry()
input_grade.place(x=160, y=83, width=150)

add_button = Button(text="Add", command=add)
add_button.place(x=160, y=120, width=60)

clear_button = Button(text="Clear", command=clear)
clear_button.place(x=240, y=120, width=60)


window.mainloop()
db.close()






