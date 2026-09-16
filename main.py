import tkinter as tk
import math as m
from logging import config


#Ablak
class App(tk.Tk):
    def __init__(root, sablon_recept=None,sajat_recept=None):
        super().__init__()
        root.sablon_recept = sablon_recept
        root.sajat_recept = sajat_recept
        root.geometry("900x800"), root.resizable(width=False, height=False), root.title("Recept simulator")

        def sablon_recept():
            table1.delete("0", "end")
            recept_s = ["test1", "test2", "test3", "test4"]
            for recept in recept_s:
                table1.insert(tk.END, recept)

        def sajat_recept():
            table1.delete("0", "end")
            recept_o=[]
            for recept in recept_o:
                table1.insert(tk.END, recept)

        def recept_selected(event):
            if table1.curselection():
                btnstart.config(state="normal")
            else:
                btnstart.config(state="disabled")

        #feliratok
        cim= tk.Label(root,
                        text="Üdvözöljünk a Recept simulatorban",
                        font=("Arial", 15, "bold"))
        cim.pack(padx=10, pady=10,side="left")
        cim.place(x=20, y=25)

        label1= tk.Label(root,
                         text="Kérem válaszon a alábbi lehetőségek közül",
                         font=("Arial", 11))
        label1.pack(pady=10)
        label1.place(x=500,y=30)
        #gombok
        btns=tk.Button(root,
                          text="saját recept",
                          font=("Arial", 10, "italic"),
                          command=sajat_recept)
        btns.pack(padx=10,pady=10,side="left")
        btns.place(x=500,y=70,width=100,height=30)
        btno=tk.Button(root,
                       text="sablon recept",
                       font=("Arial", 10, "italic"),
                       command=sablon_recept)
        btno.pack(padx=10,pady=10,side="left")
        btno.place(x=610,y=70,width=100,height=30)
        btnstart=tk.Button(root,
                           text="indítás",
                           font=("Arial", 10, "italic"),
                           state="disabled")
        btnstart.pack(padx=10,pady=10,side="left")
        btnstart.place(x=10,y=300,width=100,height=30)
        #lista
        table1=tk.Listbox(root,)
        table1.pack(padx=10,pady=10,side="left")
        table1.place(x=10,y=100,width=400,height=200)
        table1.bind("<Double-Button-1>", recept_selected)
app = App()
app.mainloop()