import requests
import tkinter as tk
from tkinter import ttk
from api import get_currency





# Mengambil data kurs mata uang
datadaricurrency = get_currency()

# Kurs IDR sebagai basis
usd_rate = datadaricurrency['USD']


# # Mengonversi semua mata uang ke dalam IDR
currencies_in_usd = {key: rate / usd_rate for key, rate in datadaricurrency.items()}

# # Pilih mata uang tertentu
selected_currencies = {key: currencies_in_usd[key] for key in ['JPY', 'IDR', 'EUR', 'USD']}
print(selected_currencies)

rupiah = 17000
dollar = 2
dollar_ke_rupiah = dollar * selected_currencies['IDR']
rupiah_ke_dollar = rupiah/selected_currencies['IDR']
print(dollar_ke_rupiah)




# # GUI menggunakan tkinter
root = tk.Tk()
root.title("Currency Exchange Rates")


# # Ukuran dan posisi jendela
lebar = 500
tinggi = 400
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
posisi_tengah_width = int((screenwidth / 2) - (lebar / 2))
posisi_tengah_height = int((screenheight / 2) - (tinggi / 2))
root.geometry(f"{lebar}x{tinggi}+{posisi_tengah_width}+{posisi_tengah_height}")
root.configure(bg="white")

# # Label judul
label = tk.Label(root, text="KURS MATA UANG", font=("Arial", 14, "bold"), bg="white", fg="black")
label.pack(pady=10)

tree = ttk.Treeview(root, columns=("Currency", "Rate"), show="headings", height=8)
tree.heading("Currency", text="Currency")
tree.heading("Rate", text="Rate (in USD)")

# Memasukkan data ke Treeview
for currency, rate in selected_currencies.items():
    tree.insert("", "end", values=(currency, round(rate, 4)))

tree.pack(pady=10, fill=tk.BOTH, expand=True)

# # Input jumlah dalam IDR
# input_label = tk.Label(root, text="Masukkan jumlah dalam IDR:")
# input_label.pack(pady=5)
# input_amount = tk.Entry(root, width=20)
# input_amount.pack(pady=5)

# # Dropdown untuk memilih mata uang
# currency_label = tk.Label(root, text="Pilih mata uang tujuan:")
# currency_label.pack(pady=5)
# currency_combobox = ttk.Combobox(root, values=list(selected_currencies.keys()), state="readonly")
# currency_combobox.pack(pady=5)

# # Tombol konversi
# convert_button = tk.Button(root, text="Konversi", command=convert_currency)
# convert_button.pack(pady=10)

# # Label untuk menampilkan hasil
# result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
# result_label.pack(pady=10)

# # Menjalankan GUI
root.mainloop()
