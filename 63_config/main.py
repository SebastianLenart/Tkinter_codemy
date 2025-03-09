from tkinter import *
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("400x400")

def something():
    my_label.config(text="this is new text")
    root.config(bg="blue")
    my_button.config(text="neww")

global my_label
my_label  = Label(root, text="this is my text")
my_label.pack()
my_button = Button(root, text="click me", command=something)
my_button.pack()

root.mainloop()