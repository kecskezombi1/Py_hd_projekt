import turtle as t
import tkinter as tk
from tkinter import Button, messagebox


class App(tk.Tk):

    def exit_app(self):
        self.destroy()

    def left_b(self):
        t.left(90)

    def right_b(self):
        t.right(90)

    def up_b(self):
        self.forward_t()

    def down_b(self):
        try:
            szam = int(self.inputa.get())
            t.back(szam)
        except ValueError:
            messagebox.showerror("Hiba", "Csak számot adj meg!")

    def forward_t(self):
        try:
            szam = int(self.inputa.get())
            t.forward(szam)
        except ValueError:
            messagebox.showerror("Hiba", "Csak számot adj meg!")

    def __init__(self):
        super().__init__()

        self.title("Teknosbeka")
        self.geometry("400x400")
        self.resizable(False, False)
        self.configure(background="white")

        t.title("Teknosbeka")

        quitbtn = Button(
            self,
            text="Quit",
            command=self.exit_app
        )
        quitbtn.place(x=180, y=20)

        self.inputa = tk.Entry(self)
        self.inputa.place(x=60, y=60)
        self.inputa.insert(0, "100")

        upbtn = Button(
            self,
            text="Up",
            command=self.up_b
        )
        upbtn.place(x=140, y=100)

        leftbtn = Button(
            self,
            text="Left",
            command=self.left_b
        )
        leftbtn.place(x=70, y=140)

        downbtn = Button(
            self,
            text="Down",
            command=self.down_b
        )
        downbtn.place(x=140, y=140)

        rightbtn = Button(
            self,
            text="Right",
            command=self.right_b
        )
        rightbtn.place(x=210, y=140)


app = App()
app.mainloop()