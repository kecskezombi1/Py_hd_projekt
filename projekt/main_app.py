import tkinter as tk
from tkinter import ttk, messagebox

class Begyujtas:
    def __init__(self,root):
        self.root=root
        self.root.geometry("650x480")
        self.root.title("Hőfigyelő - MTMACQ")
        self.root.resizable(False, False)
        self.root.configure(background="slategray")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        style = ttk.Style()
        style.configure("cim.TLabel",foreground="white",background="slategray", font=("Arial", 15, "bold"),anchor="center",padding=15)

        self.cim=ttk.Label(self.root,text="Begyujtás",style="cim.TLabel")
        self.cim.grid(row=0,column=0,columnspan=2,sticky="ew")


if __name__ == "__main__":
    root = tk.Tk()
    app = Begyujtas(root)
    root.mainloop()