from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import font
from tkinter import messagebox
from tkinter import colorchooser
import os, sys

root = Tk()
root.title("resize")
root.geometry("600x480")

clicked = True
count=0

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def chechifwon():
    global winner
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic", "congrats")
        disable_all_buttons()
        # itd itd..
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic", "congrats")
        disable_all_buttons()
        # itd itd..

def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        chechifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        chechifwon()
    else:
        messagebox.showerror("tic Tac Toe", "pick another box")

b1 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b1))
b2 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b2))
b3 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b3))

b4 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b4))
b5 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b5))
b6 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b6))

b7 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b7))
b8 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b8))
b9 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()
