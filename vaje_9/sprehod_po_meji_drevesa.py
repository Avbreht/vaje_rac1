
from dvojisko_drevo import Drevo

def izpisi_liste(drevo):
    '''
    :param drevo:
    :return: funkcija izpise vrednosti v listih danega drevesa
    '''
    if not drevo.prazno:
        izpisi_liste(drevo.levo)
        if drevo.desno.prazno and drevo.levo.prazno:
            # izpise vsebino če je list
            print(drevo.vsebina)
        izpisi_liste(drevo.desno)


def izpisi_levi_rob(drevo):
    '''
    :param drevo:
    :return: izpisemo levi rob drevesa od zgoraj navzdol
    '''
    if not drevo.prazno:
        if not drevo.levo.prazno:
            print(drevo.vsebina)
            izpisi_levi_rob(drevo.levo)
        elif not drevo.desno.prazno:
            print(drevo.vsebina)
            izpisi_levi_rob(drevo.desno)

    # če je list ga ne izpišemo ker se nočemo ponavljati

def izpisi_desni_rob(drevo):
    '''
    :param drevo:
    :return: izpisemo desni rob drevesa od spodaj navzgor
    '''
    if not drevo.prazno:
        if not drevo.desno.prazno:
            izpisi_desni_rob(drevo.levo)
            #izpisujemo po rekurzivnem klicu
            print(drevo.vsebina)
        elif not drevo.levo.prazno:
            izpisi_desni_rob(drevo.desno)
            print(drevo.vsebina)


def sprehod_po_meji_drevesa(drevo):
    '''
    :param drevo:
    :return: izpisemo vrednosti v točkah na meji drevesa v nasprotni smeri urinega kazalca
    '''
    if not drevo.prazno:
        #izpisemo koren drevesa
        print(drevo.vsebina)
        izpisi_levi_rob(drevo.levo)
        izpisi_liste(drevo.levo)
        izpisi_liste(drevo.desno)
        izpisi_desni_rob(drevo.desno)


drevo1 = Drevo(5, levo=Drevo(3, levo=Drevo(1)), desno=Drevo(2, levo=Drevo(6), desno=Drevo(9, levo=Drevo(4))))
drevo2 = Drevo(20, levo=Drevo(8, levo=Drevo(4), desno=Drevo(12, levo=Drevo(10), desno=Drevo(14))), desno=Drevo(22, desno=Drevo(25)))

sprehod_po_meji_drevesa(drevo2)
