def nahrbtnik(W ,v, c, n):
    # če nimamo vec predmetov ali je volumen 0 izhod
    if n == 0 or W == 0:
        return 0
    # predmet ki ga nemoremo dati notri
    if (v[n-1] > W):
        return nahrbtnik(W, v, c, n-1)
    else:
        return max((c[n-1] + nahrbtnik(W - v[n-1], v, c, n-1)), nahrbtnik(W, v, c, n-1))

cene = [60, 100, 120]
teze = [10, 20, 30]
volumen = 50
n = len(cene)
print(nahrbtnik(volumen, teze, cene, n))