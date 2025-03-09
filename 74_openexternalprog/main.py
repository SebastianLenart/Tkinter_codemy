from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

from PIL.ImageOps import expand
from tkcalendar import *


root = Tk()
root.title("resize")
root.geometry("600x400")

def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    os.system('"%s"' % my_program) # bez spacji teraz

def open_notepad():
    os.system('open_notepad') # Permission denied


my_button = Button(root, text="open program", command=open_program)
my_button.pack()

my_button2 = Button(root, text="open notepad", command=open_notepad)
my_button2.pack()

my_label = Label(root, text="")
my_label.pack()

root.mainloop()