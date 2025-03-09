from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Codemy.com Image Viewer")

frame = LabelFrame(root, text="This is my Frame..", padx=5, pady=5) # indside
frame.pack(padx=100, pady=100) # outside

b = Button(frame, text="Message")
b.pack()



root.mainloop()