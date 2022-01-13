class Drevo:

    def __init__(self, *args, **kwargs):
        '''Ustvari dvojiško drevo.

        - Drevo() ustvari prazno dvojiško drevo
        - Drevo(podatek, levo, desno) ustvari dvojiško drevo z
          danim podatkom v korenu ter levim in desnim sinom. Če kakšen od sinov
          manjka, se privzame, da je prazen.
        '''
        if args:
            assert len(args) == 2
            self.prazno = False
            self.kljuc = args[0]
            self.podatek = args[1]
            # če levega ali desnega sina ne podamo, ustvarimo prazno drevo
            self.levo = kwargs.pop('levo', None) or Drevo()
            self.desno = kwargs.pop('desno', None) or Drevo()
        else:
            self.prazno = True
        # poleg že obdelanih konstruktor ne sme sprejeti drugih argumentov
        assert not kwargs

    def __repr__(self, zamik=''):
        if self.prazno:
            return 'Drevo()'.format(zamik)
        elif self.levo.prazno and self.desno.prazno:
            return 'Drevo({1}, {2}, {3})'.format(zamik,self.hash, self.kljuc, self.podatek)
        else:
            return 'Drevo({1},\n{0}      levo = {2},\n{0}      desno = {3})'. \
                format(
                zamik,
                self.podatek,
                self.levo.__repr__(zamik + '             '),
                self.desno.__repr__(zamik + '              ')
            )

    def __eq__(self, other):
        if self.prazno and other.prazno:
            return True
        elif not self.prazno and not other.prazno:
            return (
                    self.podatek == other.podatek and
                    self.levo == other.levo and
                    self.desno == other.desno
            )
        else:
            return False

    def __hash__(self):
        if self.prazno:
            return hash(())
        else:
            return hash((self.podatek, self.levo, self.desno))

class Slovar:

    def __init__(self):
        self.slovar = Drevo()
        self.velikost = 0

    def vstavi(self, kljuc, vrednost):
        trenutno = self.slovar

        key = hash(kljuc)
        while not trenutno.prazno:
            if trenutno.hash == key:

