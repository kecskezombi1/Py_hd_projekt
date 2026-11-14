import asyncio
import logging
import math
import threading
from pathlib import Path
from tkinter import ttk, messagebox
import main_app
import tkinter as tk
from desktop_notifier import DesktopNotifier

logging.basicConfig(filename=Path(__file__).with_name("hofigyelo.log") ,level=logging.INFO, format='%(asctime)s : %(message)s',encoding='utf-8')
class Begyujtas:
    def __init__(self,root):
        self.root=root

class Begyujtas(main_app.Begyujtas):
    def __init__(self, root):
        super().__init__(root)

        self.active=False
        self.check_wait=False
        self.timer_id=None
        self.remaning=15*60
        self.nofi_minute=15
        self.next_time=None

        self.notification_loop = asyncio.new_event_loop()
        self.notification_ready = threading.Event()
        self.notification_thread = threading.Thread(target=self.notification_worker, daemon=True)
        self.notification_thread.start()

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

        self.ido_cimke = tk.Label( self.root,text="Ellenőrzési emlékeztető (perc):",bg="slategray",fg="white")
        self.ido_cimke.grid(row=5,column=0,padx=10, pady=8)

        self.ido_megadas = ttk.Spinbox(self.root,from_=1,to=120,width=12)
        self.ido_megadas.set(15)
        self.ido_megadas.grid(row=5,column=1,padx=10,pady=8)


        self.timer_label = tk.Label(self.root,text="Hátralévő idő: 15:00", font=("Arial", 18, "bold"),bg="slategray", fg="white")
        self.timer_label.grid(row=6,column=0, columnspan=2,pady=12)

        self.folytatas_btn = tk.Button(self.root,text="Folytatás",width=20,command=self.folytatas,state="disabled")
        self.folytatas_btn.grid( row=7,column=0,columnspan=2,pady=8)

        self.status_label = tk.Label(self.root,text="Állapot: Nincs elindítva",bg="slategray", fg="white",font=("Arial", 11))
        self.status_label.grid(row=8,column=0, columnspan=2,pady=8)

        self.root.protocol("WM_DELETE_WINDOW",self.ablak_bezarasa)

    def folytatas(self):
        if not self.aktiv or not self.ellenorzesre_var:
            return
        adatok = self.adatok_beolvasasa()
        if adatok is None:
            return
        self.naplozas(f"Ellenőrizve | Kazán: {adatok[0]} °C | " f"Lakás: {adatok[1]} °C")

        self.ellenorzesre_var = False

        self.folytatas_btn.config(state="disabled")
        self.vizho_megadas.config(state="readonly")
        self.hofok_megadas.config(state="readonly")

        self.status_label.config(text="Állapot: Figyelés folyamatban")

        self.uj_idozites()

    def adatok_beolvasasa(self):
        try:
            vizhofok = float(self.vizho_megadas.get().replace(",", "."))
            lakashofok = float(self.hofok_megadas.get().replace(",", "."))
            if not (math.isfinite(vizhofok) and math.isfinite(lakashofok)):
                raise ValueError

            if not -30 <= vizhofok <= 150:
                raise ValueError

            if not -30 <= lakashofok <= 60:
                raise ValueError

            return vizhofok, lakashofok

        except ValueError:
            messagebox.showerror("Hibás adat","Adj meg érvényes hőmérsékleteket!",parent=self.root)
            return


    def start_btn_clicked(self):
        if self.active:
            return

        adatok = self.adatok_beolvasasa()

        if adatok is None:
            return

        try:
            perc = int(self.ido_megadas.get())

            if not 1 <= perc <= 120:
                raise ValueError

        except ValueError:
            messagebox.showerror("Hibás időköz","1 és 120 perc közötti egész számot adj meg!", parent=self.root)
            return

        self.nofi_minute = perc
        self.active = True
        self.check_wait = False

        self.start_btn.config(state="disabled")
        self.end_btn.config(state="normal")
        self.folytatas_btn.config(state="disabled")
        self.ido_megadas.config(state="disabled")

        self.vizho_megadas.config(state="readonly")
        self.hofok_megadas.config(state="readonly")

        self.status_label.config( text="Állapot: Figyelés folyamatban" )

        self.naplozas(f"Begyújtás | Kazán: {adatok[0]} °C | " f"Lakás: {adatok[1]} °C | "f"Emlékeztető: {perc} perc")

        self.uj_idozites()

    def end_btn_clicked(self):
        messagebox.showinfo(message="Elvégezte a begyújtást",icon="warning")
        self.end_btn.config(state="disabled")
        self.start_btn.config(state="normal")
        self.folytatas_btn.config(state="disabled")

        self.vizho_megadas.config(state="normal")
        self.hofok_megadas.config(state="normal")
        self

    def notification_worker(self):
        asyncio.set_event_loop(asyncio.new_event_loop())

        self.notifer=DesktopNotifier(app_name="Hőfigyelő")
        self.notification_ready.set()
        self.notification_loop.run_forever()

        self.notification_loop.close()



    def naplozas(self,text):
        logging.info(f"naplozas | {text}")

    def ablak_bezarasa(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        if self.active:
            self.naplozas("Program bezárva aktív figyelés közben van!")

        self.active = False

        if self.notification_loop.is_running():
            self.notification_loop.call_soon_threadsafe(self.notification_loop.stop)

        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Begyujtas(root)
    root.mainloop()
