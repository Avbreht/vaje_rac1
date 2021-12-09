from dvojisko_drevo import Drevo
from ogrevanje import visina, vrni_koren, je_list, nikoli_levo, visina

drevo1 = Drevo(5, levo=Drevo(3, levo=Drevo(1)), desno=Drevo(2, levo=Drevo(6), desno=Drevo(9, levo=Drevo(4))))
drevo2 = Drevo()
drevo3 = Drevo(16, levo=Drevo(4, levo=Drevo(2, levo=Drevo(1))))
drevo4 = Drevo(3, desno=Drevo(4, desno=Drevo(6, desno=Drevo(8, desno=Drevo(10)))))

drevo5 = Drevo(6)

def premi_pregled(drevo):
    if not drevo.prazno:
        yield drevo.podatek
        premi_pregled(drevo.levo)
        premi_pregled(drevo.desno)


print(visina(drevo1))
print(visina(drevo2))
print(visina(drevo3))
print(visina(drevo4))
print(visina(drevo5))