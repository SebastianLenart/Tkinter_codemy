import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from random import choice, shuffle


root = Tk()
root.title("resize")
root.geometry("600x400")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")


for thing in range(100):
    Button(second_frame, text=f"Button{thing}").grid(row=thing, column=0)

my_label = Label(second_frame, text="Fridfay").grid(row=3, column=2)

root.mainloop()