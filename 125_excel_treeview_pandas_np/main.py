from tkinter import *
from tkinter import messagebox

import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import pandas as np
from tkinter import ttk, filedialog


root = Tk()
root.title("resize")
root.geometry("300x300")
"""

trudne do zrozumienia !!!

"""
my_frame = Frame(root)
my_frame.pack()

my_tree = ttk.Treeview(my_frame)

def file_open():
    filename = filedialog.askopenfilename(initialdir="Sciezka...",
                                          title="Open a file",
                                          filetypes=(("xlsx", "*.xlsx"), ("All files", "*.*")))
    if filename:
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)
        except ValueError:
            my_label.config(text="File Couldnt be open try again")
        except FileNotFoundError:
            my_label.config(text="File Couldnt be open try again")
    clear_tree()
    my_tree["column"] = list(df.columns)
    my_tree["show"] = "headings"
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)

    my_tree.pack()



def clear_tree():
    my_tree.delete(*my_tree.get_children())

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Spreadsheets", menu=file_menu)
file_menu.add_command(label="Open", command=file_open)

my_label = Label(root, text="")
my_label.pack()

root.mainloop()
