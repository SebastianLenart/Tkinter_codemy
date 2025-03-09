from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Codemy.com Image Viewer")
root.geometry("400x400")

class Elder:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text="click", command=self.clicker)
        self.myButton.pack()

    def clicker(self):
        print("SDSD")


e = Elder(root)

root.mainloop()