import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from random import choice, shuffle


root = Tk()
root.title("resize")
root.geometry("600x400")

def button_hover(e):
    my_button["bg"] = "white"
    status_label.config(text="Iam hovering over the button")
def button_hover_leave(e):
    my_button["bg"] = "white"
    status_label.config(text="")

my_button = Button(root, text="click me")
my_button.pack()

status_label = Label(root, text="test", bd=1, relief=SUNKEN, anchor=E)
status_label.pack(fill=X, side=BOTTOM, ipady=2)


my_button.bind("<Enter>", button_hover) # po najechaniu kursora
my_button.bind("<Leave>", button_hover_leave) # po odjechaniu kursora

root.mainloop()