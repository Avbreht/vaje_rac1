# Implementacijski izziv!

Industrijski gigant **Šmercator** se je odločil posodobiti svojo podatkovno bazo. Strokovnjaki so določili, da je najpreprosteje uporabljati podatkovno strukturo slovarjev. Ker pa je med epidemijo zaradi paničnega nakupovanja zmanjkalo hash tabel, je potrebno sestaviti novo implementacijo slovarjev. Tako je **Šmercator** odprl razpis **DictPick**, na katero sta se prijavili podjetji **NoChainNoGain**, prvak v verižnih seznamih, in pa **TreeForThee**, ki zagovarja superiornost dvojiških dreves.

Obe podjetji seveda z veseljem izkoriščata poceni študentsko delovno silo, asistent pa nujno potrebuje ekstra denar za praznično nakupovanje. Vaša naloga je, da se razdelite v dve skupini, kjer bo vsaka od skupin zastopala eno od podjetij.
def odprava_krivic(self):
        return 700
# Implementacija

Vsaka od skupin mora implementirati podatkovno strukturo `Slovar` s sledečimi metodami:
- `__init__`, ki vrne prazen slovar;
- `vstavi(kljuc, vrednost)`, ki v slovar pri ključu `kljuc` shrani `vrednost`. Če vrednost že obstaja, naj jo zgolj posodobi;
- `poisci(kljuc)`, ki poišče vrednost, ki je dodeljena ključu. Če takšne vrednosti ni, vrne `None`;
- `__str__`, ki vrne predstavitev slovarja z nizom. Izgled niza naj bo takšen kot pythonov `dict` (torej `{ kljuc : vrednost, ...}`).

Pri tem ekipa **NoChainNoGain** slovar zgradi s pomočjo [verižnih seznamov](https://ucilnica.fmf.uni-lj.si/mod/assign/view.php?id=52384), ki ste jih implementirali v sklopu vaj,
 ekipa **TreeForThee** pa naj v ozadju uporabi [dvojiško drevo](https://gist.githubusercontent.com/matijapretnar/65d4d5f3eec609f4276155cb1cee892d/raw/dvojisko_drevo.py). 
 Podatkovni strukturi lahko seveda poljubno nadgradite, ali pa zgolj uporabljate kot podstrukturo.

*Namig za NoChainNoGain:* Če hranite množico obstoječih ključev slovarja, lahko ločite med vstavljanjem in posodabljanjem, in tako vstavljanje novega ključa naredite mnogo hitrejše.

*Namig za TreeForThee:* Iskalna drevesa so zelo očitno dobra izbira. Ker podatke samo dodajamo, lahko strukturo iskalnih dreves precej enostavno vzdržujete.

*Ideja:* Metodi `vstavi` in `poisci` lahko pokličete tudi znotraj magičnih metod `__setitem__(kljuc, vrednost)`, ki v slovar pri ključu `kljuc` shrani `vrednost`. Če vrednost že obstaja, naj jo zgolj posodobi. 
in  `__getitem__(kljuc)`. Tako boste lahko elemente v slovar dodajali z ukazom `slovar[kljuc] = vrednost` in jih
pridobivali z ukazom `slovar[kljuc]`, kot bi to počeli v navadnih slovarjih;

# Testiranje

**Šmercator** vsekakor ni postal industrijski gigant s slepim zaupanjem. Prepričajte ga v pravilnost svoje implementacije s testi.

# Poklicna Sabotaža

Moralne prakse so redke v gospodarstvu, zato se je **Šmercator** odločil, da podjetjema na skrivaj pošlje implementacijo nasprotnika. Ker je asistent preveč utrujen za skrivne podle igre, se bodo tokrat podle igre odvijale vsem na očeh. Ko skupina konča z implementacijo, naj jo posreduje nasprotnikom (in obratno). Nato vsaka od skupin sestavi testni primer, ki pokaže superiornost lastne implementacije napram nasprotnikovi. Izmerite čas izvajanja za vsako implementacijo.

Primer testa je lahko npr.
```python
for _ in range(1000):
    i = random.randint(0, 10000)
    slovar.vstavi("k"+str(i), i)

for _ in range(1000):
    i = random.randint(0, 10000)
    slovar.poisci("k"+str(i))
```

*Namig za NoChainNoGain:* Glede na časovne omejitve iskalna drevesa verjetno ne bodo imela mehanizmov za uravnoteženje.

*Namig za TreeForThee:* Za primerne podatke bo iskanje v dvojiških drevesih občutno hitrejše.

# Poročilo

Da se prijavite na razpis, je potrebno oddati poročilo v Markdown obliki, ki naj vsebuje:
- Kodo vaše implementacije
- Kratek opis delovanja (par stavkov)
- Testi
- Dokaz, da je vaša implementacija boljša (v tistem primeru). Napišite hitro obrazložitev zakaj je temu tako.

