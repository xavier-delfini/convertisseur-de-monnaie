from tkinter import *
from tkinter import ttk
import json
import functions
change = 1.08

print(functions.verif_entry("100",["yen", 0.0071], ["euro", 0.8776]))

"""
f = open("test.json", "r")
dictio=f.read()
y = json.loads(dictio)
"""
main = Tk()
main.title("Convertisseur de devises")
main.resizable(False, False)



conv = ttk.Frame(main, borderwidth=2, relief="ridge", padding="10 10 5 5")
conv.grid(column=0, row=0, sticky=("N", "S", "W"))
conv.columnconfigure(0, weight=1)
conv.rowconfigure(0, weight=1)

amount_enter = StringVar()
ttk.Label(conv, text="Quantité:").grid(column=0, row=0)
name = ttk.Entry(conv, textvariable=amount_enter).grid(column=1, row=0)


main.mainloop()