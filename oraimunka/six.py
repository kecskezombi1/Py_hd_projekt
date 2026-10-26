import tkinter as tk
from tkinter import ttk,messagebox
import random as r

class Kockadobas:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.title("Kockázás")
        self.eredmenyek = {i: 0 for i in range(1, 7)}

        self.cim_cimke = ttk.Label(
            root, text="Kockajáték", font=("Arial", 16, "bold")
        )
        self.cim_cimke.grid(row=1, column=0, padx=10, pady=10)

        self.dobas_szam = tk.StringVar(value="10")
        self.dobas_szam_be = ttk.Entry( root, textvariable=self.dobas_szam  )
        self.dobas_szam_be.grid(row=1, column=1)

        # button
        self.btn = ttk.Button(root, text="Dobás", command=self.dobas)
        self.btn.grid(row=2, column=1)

        self.exitbtn = ttk.Button(root, text="Exit", command=root.destroy)
        self.exitbtn.grid(row=2, column=0)

        self.dobas_eredmenye = ttk.Label(root, text="Eredmény", font=("Arial", 20, "bold"))
        self.dobas_eredmenye.grid( row=3, column=1, padx=10, pady=10)

    def dobas(self):
        try:
            db = int(self.dobas_szam.get())
        except ValueError:
            messagebox.showerror( title="Hiba",  message="Nem számot adott meg!", icon="error")
            return

        if not 1 <= db <= 10000:
            messagebox.showerror(title="Hiba", message="A dobások számának 1 és 10000 között kell lennie." )
            return

        for _ in range(db):
            dobott_ertek = r.randint(1, 6)
            self.eredmenyek[dobott_ertek] += 1

        szoveg = '\n'.join(f'{oldal}. = {darab}' for oldal, darab in self.eredmenyek.items())

        self.dobas_eredmenye.config(text=szoveg)



root = tk.Tk()
app = Kockadobas(root)
root.mainloop()