# 0/1 nahrbtnik

**Ime:** Žiga Avbreht

**Datum:** 10.1.2022

---
## Izračun množic S in Z

```
S0 = [(0, 0)]
Z1 = [(10, 6)]
S1 = [(0, 0), (10, 6)]
Z2 = [(7, 9), (17, 15)]
S2 = [(0, 0), (7, 9), (17, 15)]
Z3 = [(13, 4), (20, 13), (30, 19)]
S3 = [(0, 0), (7, 9), (17, 15), (30, 19)]
Z4 = [(8, 7), (15, 16), (25, 22), (38, 26)]

Torej S4:
S4 = [(0, 0), (7, 9), (15, 16), (25, 22), (38, 36)]
```

---

## Odgovori na vprašanja

**Pri prepisu množice Z5 je pri natanko enem paru prišlo do napake. Kateri par je napačen in kakšen bi moral biti? Ali lahko napako ugotovimo, ne da bi ponovno računali Z5?**

(72, 20) je narobe saj prištejemo (27, 10) velikost 10 čeprav je element velik 6 (45, 6), torej bi moral biti (72, 16)

**Če imamo na voljo 160 enot prostora, kakšna je optimalna vrednost nahrbtnika?**

40

**Koliko neizkoriščenega prostora nam ostane, če optimalno napolnimo nahrbtnik velikosti 110 s prvimi petimi predmeti. Kakšna je ta optimalna vrednost polnitve? Opiši vse možne načine, kako dosežemo to optimalno vrednost!**

Ostane nam 11 neizkoriščenega prostora. Vrednost je 26. Lakho samo pogledamo saj so dovolj lepa števila da se vidi. Lahko pa tudi preberemo iz množice S5

**Ugotovili smo, da imamo na voljo še en predmet, in sicer velikosti 15 in vrednosti 4 (torej je na voljo 9 predmetov). Kakšna je optimalna vrednost nahrbtnika, ki ima 180 enot prostora? Opiši vse možne načine, kako dosežemo to optimalno vrednost!**

Oprtimalna rešitev je (167, 44) torej 44. To naredimo tako da opravimo še en korak pri tvorbi naših množic in naredimo še množici Z9 in S9


![Semaforji_slika](semaforji.png)