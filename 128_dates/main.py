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

panic = Label(root, text="Dont panic", bg="black", fg="green")
panic.pack()

today = date.today()
f_today = today.strftime("%A - %B %d, %Y")

today_label = Label(root, text=f_today)
today_label.pack()

days_in_year = 365
todays_day_number = int(today.strftime("%j"))

days_left = days_in_year - todays_day_number

count_label = Label(root, text=days_left)
count_label.pack()


root.mainloop()
