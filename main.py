import requests
import tkinter as tk
from tkinter import ttk

def dataapi():
    api_key = "9ba3fa6570a8d2a37397a54f4d172726"
    url = f"https://api.exchangeratesapi.io/v1/latest?access_key={api_key}"

    response = requests.get(url)

        # Memeriksa apakah permintaan berhasil
    if response.status_code == 200:
        # Mengonversi respons menjadi JSON
        data = response.json()
        rates = data['rates']
        

        for currency, rate in rates.items():
            print(f"{currency}: {rate}")
        
    else:
        print("Permintaan gagal dengan kode status:", response.status_code)


dataapi()


root = tk.Tk()
root.title("Currency Exchange Rates")

root.mainloop()
