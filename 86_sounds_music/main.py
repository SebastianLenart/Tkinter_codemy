import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from random import choice, shuffle
import pygame

root = Tk()
root.title("resize")
root.geometry("600x400")

pygame.mixer.init()

def play():
    pygame.mixer.music.load("bdbcdabcadbciabciu.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

my_button = Button(root, text="play", command=play)
my_button.pack()

my_button2 = Button(root, text="stop", command=stop)
my_button2.pack()

root.mainloop()