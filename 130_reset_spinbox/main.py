from subprocess import check_output
from tkinter import *
from tkinter import messagebox
import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import pandas as np
from tkinter import ttk, filedialog
from datetime import date

root = Tk()
root.title("resize")
root.geometry("500x500")

def reset():
    # var = IntVar(root)
    # var.set(0)
    var = StringVar(root)
    var.set("John")
    # my_spin.config(textvariable=var)
    my_spin.config(textvariable=var)

# var = IntVar(root)
# var.set(0)
var2 = StringVar(root)
var2.set("John")



# my_spin = Spinbox(root, from_=0, to=100, textvariable=var)
my_spin = Spinbox(root, values=("John", "Bob"), textvariable=var2)
my_spin.pack()

my_button = Button(root, text="Reset", command=reset)
my_button.pack()

root.mainloop()
