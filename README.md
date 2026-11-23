Halász Dávid projektje.

MTMACQ

# Hőfigyelő – Kazánellenőrzési emlékeztető

## A projekt célja

A **Hőfigyelő** egy Pythonban készített, Windowsra tervezett asztali alkalmazás, amely emlékezteti a felhasználót a fatüzelésű kazán rendszeres ellenőrzésére. Elsősorban olyan háztartásokban lehet hasznos, ahol a kazán a lakótértől távolabb, például a ház alsó szintjén található.

A felhasználó manuálisan megadja a kazán vizének és a lakásnak a hőmérsékletét, valamint az ellenőrzési emlékeztető időközét. Az alkalmazás visszaszámlál, majd az idő lejártakor asztali értesítéssel és hangjelzéssel figyelmeztet. Az ellenőrzés után új értékek adhatók meg, és a számlálás folytatható.

## Funkciók

- Grafikus kezelőfelület `tkinter` és `ttk` használatával.
- Kazánvíz- és lakáshőmérséklet manuális megadása.
- Állítható emlékeztetési időköz: 1–120 perc, alapértelmezetten 15 perc.
- Visszaszámlálás és ellenőrzésre figyelmeztető állapot.
- Windows-asztali értesítés a `desktop-notifier` csomaggal.
- Hangjelzés a `winsound` modullal.
- A programablak előtérbe helyezése az ellenőrzéskor.
- Új mért adatok megadása és a figyelés folytatása.
- A figyelés kézi leállítása.
- Eseménynapló készítése a `hofigyelo.log` fájlba.


## A projekt fájljai

| Fájl | Szerepe |
| --- | --- |
| `main.py` | A főablak, a gombok, a beviteli mezők és az alapállapotok létrehozása; a program indítása. |
| `hofigyelo_modul_HD.py` | A figyelés, időzítés, adatellenőrzés, értesítések és naplózás metódusai. |
| `README.md` | A projekt dokumentációja. |

A program futtatásakor `hofigyelo.log` naplófájl keletkezhet. A `hofigyelo.json` a JSON-mentés elkészülte után automatikusan generált adatfájl lesz, nem szükséges előre létrehozni.

## Felhasznált modulok

| Modul | Mire szolgál? |
| --- | --- |
| `tkinter`, `tkinter.ttk` | Grafikus felület, vezérlők és eseménykezelés. |
| `asyncio` | Az értesítések aszinkron futtatása. |
| `threading` | Háttérszál használata az értesítési eseményciklushoz. |
| `desktop_notifier` | Asztali értesítések küldése. |
| `winsound` | Windows-hangjelzés. |
| `time` | Időmérés és időpontok kezelése. |
| `math` | Időszámítás és a számértékek ellenőrzése. |
| `logging` | Eseménynapló írása. |
| `pathlib` | Fájlelérési utak kezelése. |
| `json` | A tervezett strukturált adatmentés és -betöltés. |

## Osztályok és metódusok

A `main.py` egy `Begyujtas` nevű alaposztályt tartalmaz, amely létrehozza a grafikus felületet. A `hofigyelo_modul_HD.py` fájlban található `Begyujtas` osztály ebből öröklődik, és a program működését biztosító metódusokat definiálja.

| Metódus | Feladata |
| --- | --- |
| `__init__()` | Az objektum és az alkalmazás alapadatainak előkészítése. |
| `start_btn_clicked()` | A kezdő adatok ellenőrzése és a figyelés indítása. |
| `adatok_beolvasasa()` | A megadott hőmérsékletek beolvasása és ellenőrzése. |
| `uj_idozites()` | A következő figyelmeztetés időpontjának kiszámítása. |
| `idozito()` | A visszaszámlálás frissítése. |
| `ellenorzes_szukseges()` | A figyelmeztetés és az új adatok bekérésének kezelése. |
| `ertesites()` | Asztali értesítés küldése. |
| `hangjelzes()` | Hangjelzés lejátszása. |
| `ablak_megjelenes()` | Az ablak előtérbe helyezése. |
| `folytatas()` | Ellenőrzés után a visszaszámlálás újraindítása. |
| `end_btn_clicked()` | A figyelés leállítása. |
| `naplozas()` | Üzenet rögzítése az eseménynaplóban. |
| `ablak_bezarasa()` | Az alkalmazás bezárásának kezelése. |
| `adatok_betoltese()` | A tervezett JSON-mentéshez az előző adatok betöltése. |
| `adatok_mentese()` | A tervezett JSON-mentéshez az adatok fájlba írása. |

## Telepítés és indítás

**Követelmények:** Python 3, Windows operációs rendszer.

A külső csomag telepítése:

```bash
pip install desktop-notifier
```

Indítás a projekt mappájában:

```bash
python main.py
```

## Használat 

1. Indítsuk el az alkalmazást.
2. Adjuk meg a kazán vízhőmérsékletét és a lakás hőmérsékletét Celsius-fokban.
3. Állítsuk be az ellenőrzési emlékeztető időközét.
4. Kattintsunk a **Begyújtás** gombra.
5. Az idő lejártakor ellenőrizzük a kazánt.
6. Rögzítsük az új hőmérsékleti értékeket, és nyomjuk meg a **Folytatás** gombot.
7. A figyelés lezárásához használjuk a **Vége** gombot.

## Eseménynapló és továbbfejlesztés

A `logging` modul a `hofigyelo.log` fájlban rögzíti többek között a figyelés indítását, az ellenőrzési értesítéseket, a megadott hőmérsékleteket és a leállítást.

Lehetséges továbbfejlesztések: automatikusan létrejövő JSON-adatfájl, fűtési alkalmak összesítése, statisztikák és hőmérsékleti grafikonok.

## Biztonsági megjegyzés

A Hőfigyelő **emlékeztető**, nem automatikus mérő- vagy biztonsági rendszer. Nem érzékeli a kazán tényleges állapotát, és nem helyettesíti a személyes ellenőrzést, a gyártói előírásokat vagy a megfelelő biztonsági berendezéseket. Az alapértelmezett 15 perces időköz nem jelent biztonságos ellenőrzési gyakoriságot minden kazánhoz.
