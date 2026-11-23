import asyncio
import logging
import math
import time
from encodings import utf_8
import winsound
import json
from pathlib import Path
from tkinter import ttk, messagebox
import tkinter as tk
from desktop_notifier import DesktopNotifier
import main

logging.basicConfig(filename=Path(__file__).with_name("hofigyelo.log") ,level=logging.INFO, format='%(asctime)s : %(message)s',encoding='utf-8')

class Begyujtas(main.Begyujtas):
    def __init__(self, root):
        super().__init__(root)

    def adatok_betoltese(self):
        if self.json_fajl.exists():
            try:
                with open(self.json_fajl,"r",encoding=utf_8) as f:
                    adat=json.load(f)
                if(isinstance(adat,dict)
                        and isinstance(adat.get("futesek"),list)
                ):
                    return  adat
            except (OSError,ValueError):
                logging.exception("JSON betöltési hiba")
        return {
            "beallitasok": {
                "ertesitesi_perc": 15
            },
            "futesek": []
        }

    def saved_data(self):
        try:
            temp = self.json_fajl.with_suffix(".tmp")
            with open(temp, "w", encoding="utf-8") as f:
                json.dump(self.saved_data,f,ensure_ascii=False,indent=4)
            temp.replace(self.json_fajl)

        except OSError:
            logging.exception("JSON mentési hiba")
            messagebox.showerror("Mentési hiba","Nem sikerült az adatok mentése.",parent=self.root)

    def meres_rogzitese(self,esemeny_tipus,vizhofok,lakashofok):
        new_event_house={
            "időpont":time.strftime("%Y-%m-%d %H:%M:%S"),
            "esemeny":esemeny_tipus,
            "kazan":vizhofok,
            "lakasho":lakashofok
        }

        self.saved_data()["futesek"].append(new_event_house)
        self.saved_data

    def folytatas(self):
        if not self.active or not self.ellenorzesre_var:
            return
        adat = self.adatok_beolvasasa()
        if adat is None:
            return
        self.naplozas(f"Ellenőrizve | Kazán: {adat[0]} °C | " f"Lakás: {adat[1]} °C")
        self.meres_rogzitese

        self.ellenorzesre_var = False

        self.folytatas_btn.config(state="disabled")
        self.vizho_megadas.config(state="readonly")
        self.hofok_megadas.config(state="readonly")
        self.ido_megadas.config(state="readonly")

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

    def hangjelzes(self):
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

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

    def uj_idozites(self):
        self.next_time=(time.monotonic()+self.nofi_minute*60)
        self.idozito()

    def idozito(self):
        self.timer_id=None
        if not self.active or self.check_wait:
            return

        self.hatralevo=max( 0,math.ceil(self.next_time - time.monotonic()))
        perc, masodperc=divmod(self.hatralevo,60)

        self.timer_label.config(text=f"Hátralévő idő: {perc:02d}:{masodperc:02d}")
        if self.hatralevo == 0:
            self.ellenorzes_szukseges()
            return

        self.timer_id = self.root.after(250, self.idozito)

    def ellenorzes_szukseges(self):
        self.ellenorzesre_var = True

        self.timer_label.config(text="Ellenőrzés szükséges!")

        self.status_label.config(text="Állapot: Új adatokra vár")

        for entry in (self.vizho_megadas,self.hofok_megadas):
            entry.config(state="normal")
            entry.delete(0, tk.END)

        self.ido_megadas.config(state="normal")
        self.folytatas_btn.config(state="normal")
        self.naplozas("Ellenőrzési emlékeztető lejárt")
        self.ertesites()
        self.hangjelzes()

    def end_btn_clicked(self):
        if not self.active or self.check_wait:
            return

        self.active = False
        self.ellenorzesre_var = False

        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        self.start_btn.config(state="normal")
        self.end_btn.config(state="disabled")
        self.folytatas_btn.config(state="disabled")

        self.ido_megadas.config(state="normal")
        self.vizho_megadas.config(state="normal")
        self.hofok_megadas.config(state="normal")

        self.timer_label.config(text="Figyelés leállítva")
        self.status_label.config(text="Állapot: Befejezve")
        self.naplozas("Figyelés befejezve")

        messagebox.showinfo("Hőfigyelő","A figyelés befejeződött.",parent=self.root)

    def notification_worker(self):
        asyncio.set_event_loop(asyncio.new_event_loop())

        self.notifer=DesktopNotifier(app_name="Hőfigyelő")
        self.notification_ready.set()
        self.notification_loop.run_forever()

        self.notification_loop.close()

    def ellenorzes_szukseges(self):
        self.ellenorzesre_var = True

        self.timer_label.config(text="Ellenőrzés szükséges!")

        self.status_label.config(text="Állapot: Új adatokra vár")

        for entry in (self.vizho_megadas,self.hofok_megadas,self.ido_megadas):
            entry.config(state="normal")
            entry.delete(0, tk.END)

        self.folytatas_btn.config(state="normal")

        self.naplozas("Ellenőrzési emlékeztető lejárt")

        self.ertesites()

    def ablak_megjelenes(self):
        self.root.deiconify()
        self.root.state("normal")

        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.after(100,lambda: self.root.attributes("-topmost", False))
        self.root.focus_force()

    def ertesites(self):
        async def send():
            await self.notifer.send(title="Hőfigyelő – Ellenőrzés",message=("Eltelt a beállított idő! " "Ellenőrizd a kazánt, majd add meg ""az aktuális hőmérsékleteket."))
            self.hangjelzes()
            self.ablak_megjelenes()

        def hiba_ellenorzese(future):
            try:
                future.result()
            except Exception:
                logging.exception( "Nem sikerült elküldeni az értesítést")

        def utemezes():
            future = asyncio.run_coroutine_threadsafe(send(),self.notification_loop)
            future.add_done_callback(hiba_ellenorzese)

        if self.notification_ready.is_set():
            utemezes()
        else:
            logging.warning("Az értesítési rendszer még nem áll készen")

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