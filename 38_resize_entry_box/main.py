from tkinter import *

root = Tk()
root.title("resize")
root.geometry("400x400")

def myClick():
    hello = "Hello" + e.get()
    mylabel = Label(root, text=hello)
    e.delete(0, "end")
    mylabel.pack(pady=10)


e = Entry(root, width=50, font=("Helvetica", 24)) # Nie zmienimy wysokosci, tylko zmieny przez inna czcionke
e.pack(padx=10, pady=10)

myButton = Button(root, text="Enter", command=myClick)
myButton.pack(pady=10)

root.mainloop()