from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("sliders")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday", "tuessday", "wednesday", "thursday", "friday"
]

clicked = StringVar()
clicked.set("monday")
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="show", command=show).pack()

root.mainloop()