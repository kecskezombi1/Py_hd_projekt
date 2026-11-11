import sqlite3
from json import JSONDecodeError
from random import randint, random
import six
import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime
import os
import json

class KockaApp(six.Kockadobas):
    def __init__(self,root):
        super().__init__(root)
        self.mentes_gomb=ttk.Button(root,text='Mentés - TEXT',command=self.mentes_txt)
        self.mentes_gomb.grid(row=3,column=2)

        self.mentes_csv_gomb=ttk.Button(root,text='Mentés - CSV',command=self.mentes_csv)
        self.mentes_csv_gomb.grid(row=3,column=3)

        self.mentes_sql_gomb=ttk.Button(root,text='Mentés - SQL',command=self.mentes_sql)
        self.mentes_sql_gomb.grid(row=3,column=4)

        self.mentes_json_gomb=ttk.Button(root,text='Mentés - JSON',command=self.mentes_json)
        self.mentes_json_gomb.grid(row=4,column=2)

        self.veletlen_gomb=ttk.Button(root,text='Véletlen',command=self.veletlendobasszam)
        self.veletlen_gomb.grid(row=5,column=3)

        self.osszesites_cimke=ttk.Label(root,text='xxxx',font=('Arial',16,'bold'))
        self.osszesites_cimke.grid(column=4,row=2)

        self.osszesites_gomb=ttk.Button(root,text='Összesítés',command=self.osszesites_sql)
        self.osszesites_gomb.grid(row=2,column=3)

        self.torles_gomb=ttk.Button(root,text='Torles',command=self.torles_sql)
        self.torles_gomb.grid(row=4,column=3)

        self.dobas()

    def osszesites_sql(self):
        try:
            with sqlite3.connect('mentes.db') as conn:
                cursor=conn.cursor()
                cursor.execute("""
                    SELECT 
                        SUM(egy),
                        SUM(ketto),
                        SUM(harom),
                        SUM(negy),
                        SUM(ot),
                        SUM(hat)
                    FROM dobasok
                """)

                eredmeny=cursor.fetchone()
                if eredmeny is None:
                    self.osszesites_cimke.config(text='Üres')
                    return

                print(eredmeny)
                szoveg=''
                for i in range(6):
                    szoveg += f'{i+1}. = {eredmeny[i]}\n'
                self.osszesites_cimke.config(text=szoveg)

        except sqlite3.Error as e:
            messagebox.showerror(title='Mentes',message=f'Nem sikerült a lekérdezés, hibakód {e}')

    def torles_sql(self):
        valasz=messagebox.askyesno(title='Torles',message='Biztosan hogy töröljem?')
        if not valasz:
            return
        try:
            with sqlite3.connect('mentes.db') as conn:
                cursor=conn.cursor()
                cursor.execute("""
                """)
                conn.commit()

            self.osszesites_gomb.config(text=f'')
            messagebox.showinfo(title='Törlés',message='Töröltem a rekordokat.')
        except sqlite3.Error as e:
            messagebox.showerror(title='Törlés',message=f'Hiba történt{e}')
    def veletlendobasszam(self):
        szam=randint(1,10)
        self.dobas_szam.set(str(szam))
        self.dobas()

    def mentes_sql(self):
        if sum(self.eredmenyek.values())==0:
            messagebox.showwarning(title='Dobás',message="Először dobjon.")
            return

        datum=datetime.now().strftime('%Y.%m.%d')
        try:
            with sqlite3.connect('mentes.db') as conn:
                cursor=conn.cursor()
                cursor.execute("""
                        CREATE TABLE IF NOT EXISTS dobasok (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            datum TEXT,
                            egy INTEGER,
                            ketto INTEGER,
                            harom INTEGER,
                            negy INTEGER,
                            ot INTEGER,
                            hat INTEGER
                            )
                    """)
                print(self.eredmenyek.values())
                cursor.execute("""
                        INSERT INTO dobasok
                        (datum, egy, ketto, harom, negy, ot, hat) VALUES (?,?,?,?,?,?,?)
                    """,(datum,*self.eredmenyek.values()))
                conn.commit()

            messagebox.showinfo('Mentés','Sikeres a mentés.')
        except (sqlite3.Error,OSError):
            messagebox.showerror(title="Hiba", message="Hiba történt!")

    def mentes_txt(self):
            if sum(self.eredmenyek.values())==0:
                messagebox.showwarning(title='Dobás',message="Először dobjon.")
                return
            sor=f'{self.eredmenyek}\n'
            try:
                with open('mentes.txt','a',encoding='utf-8') as f:
                    f.write(sor)
                messagebox.showinfo('Mentés','Sikeres a mentés.')
            except OSError:
                messagebox.showerror(title="Hiba",message="Hiba történt!")

    def mentes_csv(self):
        if sum(self.eredmenyek.values())==0:
            messagebox.showwarning(title='Dobás',message="Először dobjon.")
            return
        fajlnev='mentes.csv'
        adatok=self.eredmenyek.copy()
        adatok['Datum']= datetime.now().strftime('%Y.%m.%d')
        fejlec_kell=os.path.exists(fajlnev)
        try:
            with open(fajlnev,mode='a',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                if fejlec_kell:
                    writer.writerow(adatok.keys())
                writer.writerow(adatok.values())
            messagebox.showinfo('Mentés','Sikeres a mentés.')
        except OSError:
            messagebox.showerror(title="Hiba",message="Hiba történt!")

    def mentes_json(self):
        if sum(self.eredmenyek.values())==0:
            messagebox.showwarning(title='Dobás',message="Először dobjon.")
            return
        fajlnev='mentes.json'
        adatok=self.eredmenyek.copy()
        adatok['Datum']= datetime.now().strftime('%Y.%m.%d')
        try:
            try:
                with open(fajlnev,mode='r',encoding='utf-8') as f:
                    mentett_adatok=json.load(f)
            except FileNotFoundError:
                mentett_adatok={}

            mentett_adatok.append(adatok)

            with open(fajlnev,mode='w',newline='',encoding='utf-8') as f:
                json.dump(mentett_adatok,f,ensure_ascii=False,indent=4)
            messagebox.showinfo('Mentés', 'Sikeres a mentés.')

        except (OSError,JSONDecodeError):
            messagebox.showerror(title="Hiba", message="Hiba történt!")


if __name__ == "__main__":
    root = tk.Tk()
    app = KockaApp(root)
    root.mainloop()

