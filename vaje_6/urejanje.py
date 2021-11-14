
from merilnik import izmeri_cas, izpisi_case, oceni_potreben_cas, narisi_in_pokazi_graf, test_gen_sez, test_fun_kvad


def urejanje_z_mehurcki(tab):
    n = len(tab)
    for i in range(n):
        for j in range(n-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab


# print(izmeri_cas(urejanje_z_mehurcki, test_gen_sez(10000)))

def urejanje_z_zlivanjem(tab):
    if len(tab) > 1:
        sredina = len(tab) // 2
        levi_sez = tab[:sredina]
        desni_sez = tab[sredina:]
        urejanje_z_zlivanjem(levi_sez), urejanje_z_zlivanjem(desni_sez)
        i, j, k = 0, 0, 0
        while i < len(levi_sez) and j < len(desni_sez):
            if levi_sez[i] < desni_sez[j]:
                tab[k] = levi_sez[i]
                i += 1
            else:
                tab[k] = desni_sez[j]
                j += 1
            k += 1
        while i < len(levi_sez):
            tab[k] = levi_sez[i]
            i += 1
            k += 1
        while j < len(desni_sez):
            tab[k] = desni_sez[j]
            j += 1
            k += 1

primer = test_gen_sez(10)
urejanje_z_zlivanjem(primer)
print(primer)


