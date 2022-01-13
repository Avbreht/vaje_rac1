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


kovanci1 = [42, 2, 3, 3, 4, 1]
kovanci2 = [55, 234, 60, 30, 1, 1, 11, 3]
kovanci3 = [1]

print(naj_vsota(kovanci1))
print(naj_vsota(kovanci2))
print(naj_vsota(kovanci3))


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


print(naj_vsota_max_st(kovanci1))
print(naj_vsota_max_st(kovanci2))
print(naj_vsota_max_st(kovanci3))
