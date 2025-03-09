from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


root = Tk()
root.title("resize")
root.geometry("800x800")

def thing():
    my_label.config(text="you clicked the button")


login_btn = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/66_image_buttons/login.png")

img_label = Label(image=login_btn)
# img_label.pack(pady=20)

my_button = Button(root, image=login_btn, command=thing, borderwidth=10)
my_button.pack()

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()