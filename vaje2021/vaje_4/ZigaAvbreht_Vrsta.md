# Testno poročilo

**Ime:** Žiga Avbreht

**Datum:** 2.11.2020

---

Na vajah smo uporabljali podatkovno strukturo Vrsta in smo delali naloge s uporabo le te. Zadnja naloga mi je nekoliko nagajala, saj nevem kako naj bi vrste rekurzivno uredil.

## Organizacija dela

Priprava testnega poročila je bila samostojno delo. Prav tako je bilo samo reševanje problemov.

## Komentarji in opombe

Vaje so bile kar zajetne, kljub majehni količini nalog. Torej so bile po konceptih težje kar se mi zdi veliko bolje kot da imamo miljon istih nalog, pri katerih samo pišemo kodo ne da bi rabili kar koli razmišlat.

Testno poročilo se mi ne zdi zanimiv koncept, a se zavedam pomebnosti dokumentiranja in razlaganja napisane kode da jo bo lako se kdo za nami razumel.

# Zavetišče

V nekem živalskem zavetišču sprejemajo pse in mačke (bolj eksotičnih živali pa ne sprejemajo). Pravila zavetišča določajo, da dobi posvojitelj vedno tisto žival, ki je najdlje časa varovanec zavetišča. Pri tem lahko izbira med psom in mačko, lahko pa mu je vseeno glede vrste. Sestavite razred Zavetisce, ki bo upravniku v pomoč pri vodenju zavetišča.

Razred naj ima naslednje metode:

```
__init__(self), ki ustvari prazno zavetišče;
sprejmi(self, ime, vrsta), ki evidentira novo žival z imenom ime, ki je pripadnik vrste vrsta (ta ima lahko vrednost 'pes' ali 'mačka');
oddaj_psa(self), ki vrne ime psa, ki je na vrsti za posvojitev (in ga tudi odstrani iz evidence);
oddaj_macko(self), ki deluje podobno kot oddaj_psa, vendar za mačke;
oddaj_zival(self), ki deluje podobno kot oddaj_psa in oddaj_macko, vendar vrne žival tiste vrste, ki je prva na vrsti za posvojitev.
Metode oddaj_psa, oddaj_macko in oddaj_zival naj vrnejo None, če ustrezne živali ni na voljo
... s primernim okoljem.
```

**Uspešnost reševanja:** 
- rešil `2/2` podnalog in dodatno nalogo

---

## Part 1
**Navodilo:** Besedilo naloge je že besedilo prve podnaloge. Je pa se dodatek:
Namig: Uporabite dve vrsti, tako da v eni hranite pse, v drugi pa mačke. V vrsti hranite pare, ki vsebujejo ime in čas prihoda, npr. ('Taček', 1).

**Rešitev:**
```
from vrsta import Vrsta
import time

class Zavetisce:

    def __init__(self):
        self.macki = Vrsta()
        self.psi = Vrsta()

    def sprejmi(self, ime, vrsta):
        if vrsta == 'pes':
            self.psi.vstavi((ime, time.time()))
        else:
            self.macki.vstavi((ime, time.time()))

    def oddaj_psa(self):
        if self.psi.prazna():
            return None
        pes = self.psi.zacetek()[0]
        self.psi.odstrani()
        return pes

    def oddaj_macko(self):
        if self.macki.prazna():
            return None
        macka = self.macki.zacetek()[0]
        self.macki.odstrani()
        return macka

    def oddaj_zival(self):
        if self.psi.prazna() and self.macki.prazna():
            return None
        pes = self.psi.zacetek()
        macka = self.macki.zacetek()
        if pes[1] < macka[1]:
            self.psi.odstrani()
            return pes[0]
        else:
            return macka[0]
```

Pri *podnalogi 1* nisem imel večjih težav, saj je zgolj prikaz definiranje razreda Zavetisce. Uporabil sem knjižnico time, saj je bil namig da naredimo 2 vrsti in beležimo katera žival je starejša in to je elementarno s time.

**Testi**

Edini robni primeri ki jih lahko napišemo so da je naše zavetišče prazno, kar je ze v samem razredu dobro definirano da nam vrne None.
```
>>> 
zav = Zavetisce()
zav.sprejmi('Doge', pes)
zav.oddaj_macko()

None
```


Lahko tudi probamo sprejeti v zavetisce nekaj kar ni macka ali pes a seveda to nebo delovalo
```
>>> 

zav = Zavetisce()
zav.sprejmi('Nemo', riba)

Traceback (most recent call last):
  File "/home/ziga/PycharmProjects/rac1/vaje_4/test.py", line 5, in <module>
    zav.sprejmi('Nemo', riba)
NameError: name 'riba' is not defined
```


---

## Part 2.

**Navodilo:** Zavetišče je obiskala informacijska pooblaščenka, ki je prepovedala hranjenje časa prihoda živali. Zdaj morate napisati nov razred ZavetiscePoPredpisih, ki naj deluje enako kot Zavetisce, le da ne hrani časov prihoda živali.

Namig: Živali hranite v eni sami vrsti, ki naj vsebuje pare podatkov in sicer ime živali ter vrsto, npr. ('Taček', 'pes').

**Komentar:** Naloga je bila skoraj ista kot prej edino rabili smo pazit da ne uzamemo narobne živali
class ZavetiscePoPredpisih:

    def __init__(self):
        self.vrsta = Vrsta()

    def sprejmi(self, ime, vrsta):
        self.vrsta.vstavi((ime, vrsta))

    def oddaj_psa(self):
        pomozna = Vrsta()
        while not self.vrsta.prazna():
            ziv = self.vrsta.zacetek()
            if ziv[1] == 'pes':
                self.vrsta.odstrani()
                return ziv[0]
            pomozna.vstavi(self.vrsta.zacetek())
            self.vrsta.odstrani()
        while not pomozna.prazna():
            self.vrsta.vstavi(pomozna.zacetek())
            pomozna.odstrani()

    def oddaj_macko(self):
        pomozna = Vrsta()
        while not self.vrsta.prazna():
            ziv = self.vrsta.zacetek()
            if ziv[1] == 'mačka':
                self.vrsta.odstrani()
                return ziv[0]
            pomozna.vstavi(self.vrsta.zacetek())
            self.vrsta.odstrani()
        while not pomozna.prazna():
            self.vrsta.vstavi(pomozna.zacetek())
            pomozna.odstrani()

    def oddaj_zival(self):
        if self.vrsta.prazna():
            return None
        else:
            ziv = self.vrsta.zacetek()
            self.vrsta.odstrani()
            return ziv[0]


