
test1 = [[5, 0, 0, 0], [2, 8, 0, 0], [7, 3, 4, 0], [5, 6, 10, 1]]

def kovanci_v_trik(vrednosti):
    while len(vrednosti) > 1:
        rezultat = vrednosti[-2]
        spodnji = vrednosti[-1]
        for i in range(len(spodnji) - 1):
            rezultat[i] += max(spodnji[i], spodnji[i + 1])
        vrednosti = vrednosti[:-1]
        vrednosti[-1] = rezultat
    return rezultat[0]

print(kovanci_v_trik(test1))

def kovanci_s_potjo(vrednosti):
    while len(vrednosti) > 1:
        rezultat = []
        for el in vrednosti[-2]:
            rezultat.append((el, ""))
        spodnji = []
        for index in range(len(vrednosti[-1])):
            if index % 2 == 0:
                spodnji.append((vrednosti[-1][index], "L"))
            else:
                spodnji.append((vrednosti[-1][index], "D"))
        tab = []
        for i in range(len(spodnji) - 1):
            vecji = max(spodnji[i], spodnji[i + 1])
            print(vecji)
            tab.append((vecji[0] + rezultat[i][0], vecji[1] + rezultat[i][1]))
            #rezultat[i] = vecji[1] + rezultat[i][1]
        vrednosti = vrednosti[:-1]
        vrednosti[-1] = tab
    return tab

#print(kovanci_s_potjo(test1))

def kovanci_s_potjo1(vrednosti):
    pot = []
    for i in range(len(vrednosti[0])):
        pot.append("")
    while len(vrednosti) > 1:
        rezultat = vrednosti[-2]
        spodnji = vrednosti[-1]
        for i in range(len(spodnji) - 1):
            rezultat[i] += max(spodnji[i], spodnji[i + 1])
            if spodnji[i] > spodnji[i + 1]:
                pot[i] += "L"
            else:
                pot[i] += "D"
        vrednosti = vrednosti[:-1]
        vrednosti[-1] = rezultat
    return pot

#print(kovanci_s_potjo1(test1))

def kovanci_trik_max_glob(vrednosti, k):
    if len(vrednosti) < k:
        return kovanci_v_trik(vrednosti)
    else:
        nove_vred = vrednosti[:k]
        return kovanci_v_trik(nove_vred)