import asyncio
import threading
import tkinter as tk
from pathlib import Path
from tkinter import ttk
import hofigyelo_modul_HD as hd

class Begyujtas:
    def __init__(self,root):
        self.root=root
        self.root.geometry("400x480")
        self.root.title("Hőfigyelő - MTMACQ")
        self.root.resizable(False, False)

        self.cim=ttk.Label(self.root,text="Hőfigyelő",font=("Arial", 15, "bold"),anchor="center",padding=15)
        self.cim.grid(row=0,column=0,columnspan=2,sticky="ew")

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

        self.hofok_cimke=tk.Label(self.root,text="Lakás hőfok (°C):")
        self.hofok_cimke.grid(row=4,column=0,padx=5,pady=5)

        self.hofok_megadas=tk.Entry(self.root,bg="white",fg="black")
        self.hofok_megadas.grid(row=4,column=1,padx=10,pady=10)

        self.vizho_cimke=tk.Label(self.root,text="Vízhőmérséklet (kazán) (°C):")
        self.vizho_cimke.grid(row=3,column=0,pady=10, padx=10)

        self.vizho_megadas=tk.Entry(self.root,bg="white",fg="black")
        self.vizho_megadas.grid(row=3,column=1,pady=10, padx=10)

        self.ido_cimke = tk.Label( self.root,text="Ellenőrzési emlékeztető (perc):")
        self.ido_cimke.grid(row=5,column=0,padx=10, pady=8)

        self.ido_megadas = ttk.Spinbox(self.root,from_=1,to=120,width=12)
        self.ido_megadas.set(15)
        self.ido_megadas.grid(row=5,column=1,padx=10,pady=8)


        self.timer_label = tk.Label(self.root,text="Hátralévő idő: 15:00", font=("Arial", 18, "bold"))
        self.timer_label.grid(row=6,column=0, columnspan=2,pady=12)

        self.folytatas_btn = tk.Button(self.root,text="Folytatás",width=20,command=self.folytatas,state="disabled")
        self.folytatas_btn.grid( row=7,column=0,columnspan=2,pady=8)

        self.status_label = tk.Label(self.root,text="Állapot: Nincs elindítva",font=("Arial", 11))
        self.status_label.grid(row=8,column=0, columnspan=2,pady=8)

        self.root.protocol("WM_DELETE_WINDOW",self.ablak_bezarasa)

        self.json_fajl=Path(__file__).with_name("hofigyelo.json")
        self.saved_data=self.adatok_betoltese()


if __name__ == "__main__":
    root = tk.Tk()
    app = hd.Begyujtas(root)
    root.mainloop()