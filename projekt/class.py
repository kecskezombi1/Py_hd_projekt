from email import message
from tkinter import messagebox
import main_app
import tkinter as tk



class Begyujtas(main_app.Begyujtas):
    def __init__(self, root):
        super().__init__(root)

        self.start_btn=tk.Button(self.root,text="Begyujtás",command=self.start_btn_clicked)
        self.start_btn.grid(row=1,column=0,columnspan=2,pady=10)

        self.end_btn=tk.Button(self.root,text="Vége",command=self.end_btn_clicked,state="disabled")
        self.end_btn.grid(row=2,column=0,columnspan=2,pady=10)

        self.hofok_cimke=tk.Label(self.root,text="Lakás hőfok (°C):",fg="white",bg="slategray")
        self.hofok_cimke.grid(row=4,column=0,padx=5,pady=5)

        self.hofok_megadas=tk.Entry(self.root,bg="white",fg="black")
        self.hofok_megadas.grid(row=4,column=1,padx=10,pady=10)

        self.vizho_cimke=tk.Label(self.root,text="Vízhőmérséklet (kazán) (°C):",fg="white",bg="slategray")
        self.vizho_cimke.grid(row=3,column=0,pady=10, padx=10)

        self.vizho_megadas=tk.Entry(self.root,bg="white",fg="black")
        self.vizho_megadas.grid(row=3,column=1,pady=10, padx=10)

    def start_btn_clicked(self):
        messagebox.showinfo(message="Begyujtás elindítva",icon="info")
        self.start_btn.config(state="disabled")
        self.end_btn.config(state="normal")

    def end_btn_clicked(self):
        messagebox.showinfo(message="Elvégezte a begyujtást",icon="warning")
        self.end_btn.config(state="disabled")
        self.start_btn.config(state="normal")



if __name__ == "__main__":
    root = tk.Tk()
    app = Begyujtas(root)
    root.mainloop()
