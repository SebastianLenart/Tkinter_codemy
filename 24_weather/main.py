from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("sliders")
root.geometry("400x50")
root.configure(background="green")
try:
    api_request = requests.get(" jakis link")
    api = json.loads(api_request.content)
    city = api[0]["ReportingArea"]
    quality = api[0]["AQI"]
    category = api[0]["Category"]["Name"]
except Exception as e:
    api = "Error"

myLabel = Label(root, text=city + " Air quality " + str(quality) + " " + category, font=("Helvetica", 20), background="green")
myLabel.pack()

root.mainloop()

# nie wiem czy dziaa bo nie mam linku do requests !!!
# bez odcinka 25 i 26, tylko obejrzaem stwierdziem ze na ez zeby robic