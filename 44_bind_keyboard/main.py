from tkinter import *

root = Tk()
root.title("resize")
root.geometry("400x400")

def clicker(event):
    # myLabel = Label(root, text="label" + str(event.x) + ", " + str(event.y)) dotyczy myszki
    # myLabel = Label(root, text="label" + event.char) # dotyczy przycisku z klawiatury
    myLabel = Label(root, text="label" + event.keysym) # dotyczy przycisku z klawiatury
    myLabel.pack()


myButton = Button(root, text="click me")
# myButton.bind("<Button-3>", clicker) # 1 - lewy 2 srdokowy 3 prawy przycisk myszki
# myButton.bind("<Enter>", clicker) # tylko po najechaniu na button
# myButton.bind("<Leave>", clicker) # tylko po opuszczeniu pola obszaru button
# myButton.bind("<FocusIn>", clicker) # sprawdz sobie juz sam
# myButton.bind("<Return>", clicker) # sprawdz sobie juz sam
myButton.bind("<Key>", clicker) # tutaj cos mi nie dziala
myButton.pack()

root.mainloop()