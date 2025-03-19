from tkinter import *
from tkinter import messagebox

import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import pandas as np
from tkinter import ttk, filedialog


root = Tk()
root.title("resize")

app_width = 500
app_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

my_label = Label(root, text=f"Width:{screen_width}, height: {screen_height}")
my_label.pack()




root.mainloop()
