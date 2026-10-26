import sqlite3
from ctypes import c_ushort
from json import JSONDecodeError

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
        self.mentes_gomb.grid(row=1,column=2)
        self.mentes_csv_gomb=ttk.Button(root,text='Mentés - CSV',command=self.mentes_csv)
        self.mentes_csv_gomb.grid(row=1,column=3)
        self.mentes_sql_gomb=ttk.Button(root,text='Mentés - SQL',command=self.mentes_sql)
        self.mentes_sql_gomb.grid(row=1,column=4)
        self.mentes_json_gomb=ttk.Button(root,text='Mentés - JSON',command=self.mentes_json)
        self.mentes_json_gomb.grid(row=2,column=2)

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

