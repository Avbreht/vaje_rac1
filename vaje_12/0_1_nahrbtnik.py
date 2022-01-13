vrednosti = [6, 9, 4, 7]
velikosti = [10, 7, 13, 8]

s_0 = [(0, 0)]
z_1 = [(10, 6)]
s_1 = [(0, 0), (10, 6)]
z_2 = [(7, 9), (17, 15)]
s_2 = [(0, 0), (7, 9), (17, 15)]
z_3 = [(13, 4), (20, 13), (30, 19)]
s_3 = [(0, 0), (7, 9), (17, 15), (30, 19)]
z_4 = [(8, 7), (15, 16), (25, 22), (38, 26)]
s_4 = [(0, 0), (7, 9), (15, 16), (25, 22), (38, 36)]

"(72, 20) je narobe saj prištejemo (27, 10) velikost 10 čeprav je element velik 6 (45, 6), torej bi moral biti (72, 16)"

"40"

"ostane nam 11 neizkoriščenega prostora. Vrednost je 26. Lakho samo pogledamo saj so dovolj lepa števila da se vidi. Lahko pa tudi preberemo iz množice S_5"

el = (15, 4)

S_8 = [(0, 0), (9, 5), (11, 6), (20, 11), (36, 15), (52, 18), (60, 20),
      (68, 22), (76, 24), (92, 27), (104, 29), (108, 31), (120, 33), (136, 36),
      (152, 40), (181, 42), (184, 43), (197, 46), (200, 47), (229, 49), (245, 53)]

z_9 = []

for i in S_8:
    z_9.append((i[0] + 15, i[1] + 4))

print(z_9)

"oprtimalna rešitev je (167, 44) torej 44. To naredimo da naredimo še en korak pri tvorbi naših množic in naredimo še množici Z9 in S9"

print(45 + 27)