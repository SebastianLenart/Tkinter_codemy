from subprocess import check_output
from tkinter import *
from tkinter import messagebox
from datetime import date
import tkinter.ttk as ttk

root = Tk()
root.title("resize")
root.geometry("500x500")

# root.attributes("-alpha", 0.5)

root.wm_attributes("-transparentcolor", "red") # tu mam blad, na yt dziaa a u mnie nie

my_frame = Frame(root, width=200, height=200, bg="red")
my_frame.pack()


root.mainloop()
