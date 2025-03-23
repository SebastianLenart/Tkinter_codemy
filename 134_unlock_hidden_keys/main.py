from subprocess import check_output
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, filedialog
from datetime import date

root = Tk()
root.title("resize")
root.geometry("500x500")

my_label = Label(root, text="My Label")
my_label.pack()

for key in my_label.keys():
    print(key)
# print(my_label.keys()) # wszystkie argumenty/atrybuty

print(8*"*")
print(my_label["relief"]) # -> flat
print(my_label["text"]) # -> My Label

root.mainloop()
