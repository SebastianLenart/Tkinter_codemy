import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("600x400")

def info():
    dimension_label = Label(root, text=root.winfo_geometry())
    dimension_label.pack()

    height_label = Label(root, text="height" + str(root.winfo_height()))
    height_label.pack()

    x_label = Label(root, text="X:" + str(root.winfo_x()))
    x_label.pack()

my_button = Button(root, text="click me", command=info)
my_button.pack()

root.mainloop()