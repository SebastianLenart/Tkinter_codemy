from tkinter import *
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("400x400")

# panels
panel_1 = PanedWindow(bd=4, relief="raised", bg="red")
panel_1.pack(fill=BOTH, expand=1)

left_label = Label(panel_1, text="left panel")
panel_1.add(left_label)

# create second panel
panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=4, relief="raised", bg="blue")
# panel_2 = PanedWindow(panel_1, orient=HORIZONTAL, bd=4, relief="raised", bg="blue")
panel_1.add(panel_2)

top = Label(panel_2, text="top panel")
panel_2.add(top)

bottom = Label(panel_2, text="bottom panel")
panel_2.add(bottom)



root.mainloop()