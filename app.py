from libs.openexchange import OpenExchangeClient
import tkinter as tk
from tkinter import ttk
APP_ID="your api id here"

def conversion():
    client = OpenExchangeClient(APP_ID)
    result.set(str(format(float(client.convert(float(amount.get() or 1), "CAD", "INR")),'.2f'))+' INR')

root = tk.Tk()
root.title("Exchange Rates")

amount = tk.StringVar()
result = tk.StringVar()

top_frame = tk.Frame(root).pack(side="left", fill="both", expand=True)
amount_label = ttk.Label(top_frame, text=" Amount in CAD: ").pack(side="left", padx=(0, 10))
amount_entry = ttk.Entry(top_frame, width=15, textvariable=amount)
amount_entry.pack(side="left")
amount_entry.focus()
convert_button = ttk.Button(top_frame, text="Calculate", command=conversion).pack(side="left", fill="x", expand=True)

res_frame = tk.Frame(root).pack(side="left", fill="both", expand=True)
result_label = ttk.Label(res_frame, textvariable=result).pack(side="left", padx=(0, 10))

root.mainloop()


