import requests
import tkinter as tk
from tkinter import ttk
from api import get_currency


datadaricurrency = get_currency
print(datadaricurrency)
get_currency()


root = tk.Tk()
root.title("Currency Exchange Rates")
lebar=500
tinggi=400

screenwidth= root.winfo_screenwidth()
screenheigth= root.winfo_screenheight()

posisitengahwidth= int((screenwidth/2) - (lebar/2))
posisitengahheigth= int((screenheigth/2) - (tinggi/2))

root.geometry(f"{lebar}x{tinggi}+{posisitengahwidth}+{posisitengahheigth}")

root.mainloop()


