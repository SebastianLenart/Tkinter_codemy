from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("matplot")
root.geometry("400x400")

def graph():
    hours_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(hours_prices, 50)
    plt.show()

my_btn = Button(root, text="graph", command=graph)
my_btn.pack()






root.mainloop()