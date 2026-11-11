import main_app
import tkinter as tk



class Begyujtas(main_app.Begyujtas):
    def __init__(self, root):
        super().__init__(root)
        root.resizable(width=0, height=0)



if __name__ == "__main__":
    root = tk.Tk()
    app = Begyujtas(root)
    root.mainloop()
