# Uvod v dinamično programiranje

**Ime:** Žiga Avbreht

**Datum:** 5.1.2022

---
## Kovanci v vrsti
Naredili smo program, ki nam izračuna kovance v vrsti tako, da dobimo maksimalno vsoto in ne smemo izbrati dveh sosednjih
kovancev. Naredil sem osnovno implementacijo in implemetacijo, ko lahko še prilagodimo maksimalno
število kovancev, ki jih lahko izberemo.

Uporabil sem naslednje tri testne primere:


kovanci1 = [42, 2, 3, 3, 4, 1]

kovanci2 = [55, 234, 60, 30, 1, 1, 11, 3]

kovanci3 = [1]


---

## Osnovna implementacija

**Enostaven primer vračanja optimalne rešitve z uporabo rekurzije.**
```
def rek_kovanci(i, vrednosti):
    if i == 1:
        return vrednosti[0]
    if i == 2:
        return max(vrednosti[0], vrednosti[1])
    brez = rek_kovanci(i-1, vrednosti)
    z = rek_kovanci(i-2, vrednosti) + vrednosti[i-1]
    return max(brez, z)


def naj_vsota(vrednosti):
    return rek_kovanci(len(vrednosti), vrednosti)

>>>

print(naj_vsota(kovanci1))
print(naj_vsota(kovanci2))
print(naj_vsota(kovanci3))

>>>
49
275
1


```

---

## Kovanci v vrsti z dodatkom k

**Dodamo naši funkciji še parameter k, ki nam spremeni to da funkcija uzame največ k mnogo
kovancev.**

```
def rek_kov_max(i,vrednosti, k):
    if k == 0:
        return 0
    if i == 1:
        return vrednosti[0]
    if i == 2:
        return max(vrednosti[0], vrednosti[1])
    brez = rek_kov_max(i - 1, vrednosti, k)
    z = rek_kov_max(i - 2, vrednosti, k-1) + vrednosti[i - 1]
    return max(brez, z)

def naj_vsota_max_st(vrednosti):
    return rek_kov_max(len(vrednosti), vrednosti, 2)
>>>

print(naj_vsota_max_st(kovanci1))
print(naj_vsota_max_st(kovanci2))
print(naj_vsota_max_st(kovanci3))

>>>
46
264
1

```
