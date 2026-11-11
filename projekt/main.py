import tkinter as tk
import math as m
import _json as json
from tkinter import ttk
from tkinter import messagebox as mbox


#Ablak
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("600x300")
        self.title("Hőfigyelő - MTMACQ")
        self.resizable(False, False)

        gomb_gyujtas=ttk.Button(text="Begyujtás",command=gomb_gyujtas)
        gomb_gyujtas.grid(row=0, column=0)

app = App()
app.mainloop()