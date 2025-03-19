from tkinter import *
from tkinter import messagebox

import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import pandas as np
from tkinter import ttk, filedialog


root = Tk()
root.title("resize")
root.geometry("500x500")


def new():
    pass

def open():
    pass

def disable_new():
    file_menu.entryconfig("New", state="disabled")
    # my_menu.entryconfig("File", state="disabled")

def enable_new():
    file_menu.entryconfig("New", state="normal")

def delete_new():
    file_menu.delete("New")
    # my_menu.delete("File")


my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open)

disable_button = Button(root, text="Disable New", command=disable_new)
disable_button.pack()

enable_button = Button(root, text="Enable New", command=enable_new)
enable_button.pack()

delete_new_btn = Button(root, text="Delete New", command=delete_new)
delete_new_btn.pack()

root.mainloop()
