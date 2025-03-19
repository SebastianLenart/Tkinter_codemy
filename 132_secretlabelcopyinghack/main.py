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

my_label = Label(root, text="Label 1")
my_label.pack()

my_text = StringVar()
my_text.set("This is Label 2")

my_entry = Entry(root, bd=0) #state="readonly", textvariable=my_text
my_entry.insert(0, "This is cool label 2")
my_entry.config(state="readonly")
my_entry.pack()





root.mainloop()
