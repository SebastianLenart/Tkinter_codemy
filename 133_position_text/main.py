from subprocess import check_output
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, filedialog
from datetime import date

root = Tk()
root.title("resize")
root.geometry("500x500")

my_label1 = Label(root, text="Stuff\nStuff Stuff\nStuff Stuff Stuff", bd=1, relief="sunken")
my_label1.pack()

my_label2 = Label(root, text="Stuff\nStuff Stuff\nStuff Stuff Stuff", bd=1, relief="sunken", justify="left")
my_label2.pack()

my_label3 = Label(root, text="Stuff\nStuff Stuff\nStuff Stuff Stuff", bd=1, relief="sunken", justify="right")
my_label3.pack()



root.mainloop()
