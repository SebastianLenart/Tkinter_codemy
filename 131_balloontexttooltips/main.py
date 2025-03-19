from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tooltip Example")
root.geometry("500x500")

# Tworzenie tooltipa za pomocą ttk
tooltip = ttk.Label(root, text="To jest tooltip!", background="lightyellow", borderwidth=1, relief="solid")
tooltip.pack_forget()  # Ukryj tooltip początkowo

def show_tooltip(event):
    tooltip.place(x=event.x_root - root.winfo_rootx() + 10, y=event.y_root - root.winfo_rooty() + 10)

def hide_tooltip(event):
    tooltip.place_forget()

my_button = Button(root, text="Kliknij mnie")
my_button.pack()

# Przypisz tooltip do przycisku
my_button.bind("<Enter>", show_tooltip)
my_button.bind("<Leave>", hide_tooltip)

root.mainloop()