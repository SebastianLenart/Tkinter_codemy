from subprocess import check_output
from tkinter import *
from tkinter import messagebox
from datetime import date
import tkinter.ttk as ttk

root = Tk()
root.title("resize")
root.geometry("500x500")


root.attributes("-alpha", 0.5)

my_label = Label(root, text="Hello")
my_label.pack()

def slide(x):
    root.attributes("-alpha", my_slider.get())
    slide_label.config(text=str(round(my_slider.get(), 2)))

my_slider = ttk.Scale(root, from_=0.1, to=1.0, value=0.7, orient=HORIZONTAL, command=slide)
my_slider.pack()

slide_label = Label(root, text="")
slide_label.pack()

def make_solid(e):
    root.attributes("-alpha", 1)


def new_window():
    global new
    new = Toplevel()
    new.attributes("-alpha", 0.5)
    new.bind("<Button-1>", make_solid)

new_window = Button(root, text="new window", command=new_window)
new_window.pack()


root.mainloop()
