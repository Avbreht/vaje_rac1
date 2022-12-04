
def prideri_index(indeks, zadnji):
    dolzina_vrstice = 5
    vrstica = (indeks + 1) // dolzina_vrstice
    vrstic = zadnji // dolzina_vrstice
    zadnja_vrstica = zadnji % dolzina_vrstice
    stolpec = (indeks - 1)  % dolzina_vrstice
    nov_indeks = vrstic * stolpec + zadnja_vrstica + vrstica
    return nov_indeks

print(prideri_index(10, 14))