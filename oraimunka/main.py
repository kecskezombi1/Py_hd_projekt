from click import command

import six
import tkinter as tk
from tkinter import ttk
import requests

from oraimunka import backend, kocka_class


def backend_uzenet():
    valasz=requests.get('http://127.0.0.1:5000/api/uzenet')
    messagea=valasz.json()
    backend_cimke.config(text=messagea['uzenet'])

root = tk.Tk()
app= kocka_class.app(root)

backend_cimke=ttk.Label(app,text='Üzenet')
backend_cimke.grid(column=2,row=4)
backend_gomb=ttk.Button(root,text='Üzenet',command=backend_uzenet)
backend_gomb.grid(column=3,row=4)

root.mainloop()