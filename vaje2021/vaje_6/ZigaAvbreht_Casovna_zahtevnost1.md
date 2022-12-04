# Poročilo

**Ime:** Žiga Avbreht

**Datum:** 15.11.2020

---
## Part 1
Knjižnica merilnik je zelo uporabna za preveranje časovne zahtevnosti določenih algoritmov, ki smo jih delali na vajah 
ki jih bomo delali še v prihodnje. 
Sicer nisem razueml kaj hočete pri zadnji funkicji v knjižnici izmeri čase s tem porovnavanjem a ni samo ideja da mi zabeliži 
časovne zahtevnosti različnih algoritmov za dane sezname.

---

## Part 2

Implementeral sem alogritma bubble sort (urejanje z mehurčki) in merge sort (urejanje z zlivanjem). Po pričakovanjih smo
za urejanje z mehurcki dobili graf kvadratične zatevnosti.

**Primer:** 

```
sez_n = [1000 * i for i in range(10)]
narisi_in_pokazi_graf(urejanje_z_mehurcki, test_gen_sez, sez_n)
```
Ta primer nam vrne to sliko:

![Časovne zahtevnosti](bubble_sort.png)

Urejanje z zlivanjem mi je bilo malo težje za implementerat tako, da sem si še enkrat pogledal predavanje in je šlo po nekaj truda.
Pričakovali smo časovno zahtevnost **n*log(n)*, a graf ne zgleda najboljši za par primerov, ki sem jih napisal. Zato sem
na koncu vključil v poročilo kar isti primer kot za mehurčke

```
sez_n = [1000 * i for i in range(10)]
narisi_in_pokazi_graf(urejanje_z_zlivanjem, test_gen_sez, sez_n)
```

In še pripadajoča slika:

![Časovne zahtevnosti](merge_sort.png)

Graf sicer zgleda kar precej linearen, vrjetno bi se nam na kakih večnih številih dvignil iz linearnaosti a bi rabil 
računalnik malo dlje teči kar na vajah nisem utegnil naredit.