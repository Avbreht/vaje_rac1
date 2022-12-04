# Dvojiško drevo 1

**Ime:** Žiga Avbreht

**Datum:** 30.11.2020

---
## Testni primeri
Delal bom teste na naseldnjih drevesih:

drevo1 = Drevo(5, levo=Drevo(3, levo=Drevo(1)), desno=Drevo(2, levo=Drevo(6), desno=Drevo(9, levo=Drevo(4))))
drevo2 = Drevo()
drevo3 = Drevo(16, levo=Drevo(4, levo=Drevo(2, levo=Drevo(1))))
drevo4 = Drevo(3, desno=Drevo(4, desno=Drevo(6, desno=Drevo(8, desno=Drevo(10)))))
drevo5 = Drevo(6)

---

## Part 1

**Napišite funkcijo vrni_koren(drevo), ki vrne podatek v korenu drevesa, če pa je drevo prazno pa vrne None.**

```
def vrni_koren(drevo):
    if drevo.prazno:
        return None
    else:
        return drevo.podatek

>>>
print(vrni_koren(drevo1))
print(vrni_koren(drevo2))
print(vrni_koren(drevo3))
print(vrni_koren(drevo4))
print(vrni_koren(drevo5))

>>>
5
None
16
3
6

```

---

## Part 2

**Napišite funkcijo je_list(drevo), ki preveri ali je podano drevo list.**

```
def je_list(drevo):
    if drevo.prazno:
        return False
    elif drevo.desno.prazno and drevo.levo.prazno:
        return True
    return False
>>>

print(je_list(drevo1))
print(je_list(drevo2))
print(je_list(drevo3))
print(je_list(drevo4))
print(je_list(drevo5))

>>>
False
False
False
False
True

```
---

## Part 3

**Napišite funkcijo nikoli_levo(drevo), ki preveri, da ima vsako vozlišče drevesa kvečjemu desno poddrevo.**

```
def nikoli_levo(drevo):
    if drevo.prazno:
        return True
    else:
        if drevo.levo is not None:
            return False
        else:
            return nikoli_levo(drevo.desno)

>>>
print(nikoli_levo(drevo1))
print(nikoli_levo(drevo2))
print(nikoli_levo(drevo3))
print(nikoli_levo(drevo4))
print(nikoli_levo(drevo5))

>>>
False
True
False
False
True
```
---

## Part 4

**Napišite funkcijo visina(drevo), ki izračuna višino dvojiškega drevesa.**

```
def visina(drevo):
    if drevo.prazno:
        return 0
    else:
        return 1 + max(visina(drevo.levo), visina(drevo.desno))

>>>
print(visina(drevo1))
print(visina(drevo2))
print(visina(drevo3))
print(visina(drevo4))
print(visina(drevo5))

>>>
4
0
4
5
1

```
---
