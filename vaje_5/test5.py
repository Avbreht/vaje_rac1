from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama

v = Vozel(1)
v.naslednji = Vozel(4)


w = None
dodaj_na_konec(w, 1)
print(w)

k = dodaj_na_konec(None, 1)
print(k)

