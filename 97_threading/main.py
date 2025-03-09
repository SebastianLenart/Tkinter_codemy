import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from random import choice, shuffle
import pygame
import time
from random import randint
import threading

root = Tk()
root.title("resize")
root.geometry("600x400")


def five_seconds():
    time.sleep(5)
    my_label.config(text="5 seconds is up")


def rando():
    random_label.config(text=f"Random number: {randint(1, 100)}")


my_label = Label(root, text="Hello")
my_label.pack()

my_button1 = Button(root, text="5 seconds", command=threading.Thread(target=five_seconds).start())
my_button1.pack()

my_button2 = Button(root, text="pick random number", command=rando)
my_button2.pack()

random_label = Label(root, text="")
random_label.pack()

root.mainloop()
