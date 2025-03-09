from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("resize")
root.geometry("600x400")

my_pic = Image.open("/home/sebastian/GitHub/Tkinter_codemy/77_rezise_img/img.png")
# resize img
resized = my_pic.resize((300, 225))

new_pic = ImageTk.PhotoImage(resized)

my_label = Label(root, image=new_pic)
my_label.pack()

root.mainloop()