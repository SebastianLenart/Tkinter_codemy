from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import font
from tkinter import messagebox
from tkinter import colorchooser
import os, sys
from openpyxl import Workbook
from openpyxl import load_workbook
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("600x480")

style = ttk.Style()
style.theme_use("clam")  # default, alt, vista, clam
style.configure("Treeview",
                background="#D3D3D3",  # silver
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")  # silver
style.map("Treeview",
          background=[("selected", "green")])


tree_frame = Frame(root)
tree_frame.pack()

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse") # selectmode = extended, None
my_tree.pack()

tree_scroll.config(command=my_tree.yview)


my_tree["columns"] = ("Name", "ID", "Favourite Pizza")
# my_tree.column("#0", width=120, minwidth=25) # 2 opcja
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Favourite Pizza", anchor=W, width=140)

# my_tree.heading("#0", text="Label", anchor=W) # 2 opcja
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favourite Pizza", text="Favourite Pizza", anchor=W)

data = [
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"],
    ["John", 1, "Pepperoni"]
]

my_tree.tag_configure("oddrow", background="white")
my_tree.tag_configure("evenrow", background="lightblue")

global count
count = 0
for record in data:
    if count % 2 == 0:
        my_tree.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1], record[2]),
                       tags=("evenrow",))
    else:
        my_tree.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1], record[2]),
                       tags=("oddrow",))
    count += 1

"""
# my_tree.insert(parent="", index="end", iid=0, text="Parent", values=("John", 1, "Pepperoni"))
my_tree.insert(parent="", index="end", iid=0, text="", values=("John", 1, "Pepperoni"))
my_tree.insert(parent="", index="end", iid=1, text="", values=("Mary", "2", "Cheese"))
my_tree.insert(parent="", index="end", iid=2, text="", values=("Tina", "3", "Ham"))
my_tree.insert(parent="", index="end", iid=3, text="", values=("Bob", "4", "Supreme"))
my_tree.insert(parent="", index="end", iid=4, text="", values=("Erin", "5", "Cheese"))
my_tree.insert(parent="", index="end", iid=5, text="", values=("Wes", "6", "Onion"))

# my_tree.insert(parent="", index="end", iid=6, text="Child", values=("Steve", "1.2", "Peppers"))
# my_tree.move("6", "0", "0")

"""


add_frame = Frame(root)
add_frame.pack()

nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)


def add_record():
    my_tree.tag_configure("oddrow", background="white")
    my_tree.tag_configure("evenrow", background="lightblue")

    global count
    if count % 2 == 0:
        my_tree.insert(parent="", index="end", iid=count, text="Parent",
                       values=(name_box.get(), id_box.get(), topping_box.get()), tags=("evenrow",))
    else:
        my_tree.insert(parent="", index="end", iid=count, text="Parent",
                       values=(name_box.get(), id_box.get(), topping_box.get()), tags=("oddrow",))

    count += 1
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)


def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


def remove_selected():
    x = my_tree.selection()[0]
    my_tree.delete(x)


def remove_many_selected():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

def select_record():
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

    selected = my_tree.focus()
    # temp_label.config(text=selected)
    values = my_tree.item(selected, "values")
    temp_label.config(text=values)

    name_box.insert(0, values[0])
    id_box.insert(0, values[1])
    topping_box.insert(0, values[2])


def update_record():
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(name_box.get(), id_box.get(), topping_box.get()))

    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

def clicker(e):
    select_record()

def moveup():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

def movedown():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)



move_up = Button(root, text="move up", command=moveup)
move_up.pack()

move_down = Button(root, text="move down", command=movedown)
move_down.pack()

update_button = Button(root, text="Save Record", command=update_record)
update_button.pack()

select_button = Button(root, text="Select Record", command=select_record)
select_button.pack()

add_record = Button(root, text="add record", command=add_record)
add_record.pack()

remove_all_btn = Button(root, text="Remove all records", command=remove_all)
remove_all_btn.pack()

remove_one = Button(root, text="remove one selected", command=remove_selected)
remove_one.pack()

remove_many_sel = Button(root, text="remove many selected", command=remove_many_selected)
remove_many_sel.pack()

temp_label = Label(root, text="")
temp_label.pack()

# my_tree.bind("<Double-1>", clicker)
my_tree.bind("<ButtonRelease-1>", clicker)


root.mainloop()
