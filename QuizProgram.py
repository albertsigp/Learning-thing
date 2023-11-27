import time
from tkinter import *
from abc import ABC, abstractmethod
from tkinter.font import Font

def calc ():
    global operation_var
    try:
        number1 = int(entry1.get())
        number2 = int(entry2.get())
        operation = operation_var.get()

        if operation == 'Add':
            result = number1 + number2
        elif operation == 'Subtract':
            result = number1 - number2
        elif operation == 'Multiply':
            result = number1 * number2
        else:
            result = 'Invalid Operation'

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")





root = Tk()
root.geometry('1000x600')
titleFont = Font(family='Helvetica', size=20)

entry1 = Entry(root)
entry1.place(x=450,y=200)

entry2 = Entry(root)
entry2.place(x=450,y=250)

startbutton = Button(root, text='Start', bd='10')
startbutton.place(x=500,y=100)

root.title("Matematik tingyting")

# Create a Label widget with some text
label = Label(root, text="Matematik Program", font=titleFont)
label.place(x=400,y=0)

root.mainloop()