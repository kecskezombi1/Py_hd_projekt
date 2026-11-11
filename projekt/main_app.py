import tkinter as tk
from tkinter import ttk, messagebox


class Begyujtas:
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x300")
        self.root.title("Hőfigyelő - MTMACQ")
        self.root.resizable(False, False)

        self.cimke=ttk.Label(root,text="Begyújtas", font=("Arial", 25, "bold"))
        self.cimke.grid(column=1,row=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = Begyujtas(root)
    root.mainloop()